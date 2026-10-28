"""Discovery watermark: the search window is driven by the last SUCCESSFUL production run, not a
fixed lookback. A durable JSON blob on a dedicated `auto/updater-state` branch records the last
success time; the window is `watermark - overlap → now`. Failed runs never advance the watermark,
so a later run automatically catches up. If the catch-up window grows too large, the run fails as
needs_attention rather than deep-reviewing a backlog of hundreds.

A production run never invents a window when the state is ABSENT (branch deleted, file missing or
unreadable): it fails as needs_attention and names the recovery, a manual run with an explicit
window_start/window_end override. An override run never advances an existing watermark; when none
exists it seeds one at its window end, which is the bootstrap path for a first or recovered run.
"""
import datetime as dt
import json
import subprocess

from common import config, log

STATE_BRANCH = "auto/updater-state"
STATE_FILE = "watermark.json"

MISSING_STATE_HELP = (
    "The durable discovery watermark is missing: branch `%s` (file `%s`) is the updater's own state "
    "and records when the last successful production run ended. Without it the discovery window is "
    "unknown, so this run refuses to guess one (the old 3-day fallback silently skipped weeks after "
    "the branch was deleted on 2026-10-22). To recover, run the workflow manually in `full` mode "
    "with `window_start` (and optionally `window_end`) set to the range to re-cover, e.g. the day "
    "after the last day known to be covered. That run seeds the watermark at its window end when it "
    "succeeds, and the regular schedule continues from there. Do not delete this branch in branch "
    "cleanups." % (STATE_BRANCH, STATE_FILE))


def _parse(iso):
    if not iso:
        return None
    try:
        d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def now_iso():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


# ---- pure, testable core -------------------------------------------------
def compute_window(now, wm_iso, overlap_hours, max_catchup_days, default_lookback_days,
                   require_watermark=False):
    """Return {start_iso, catch_up_exceeded, basis}. `now`/`wm_iso` are ISO strings.
    With require_watermark (production `full` mode) an absent watermark returns
    basis=missing_watermark and start_iso=None instead of the default lookback."""
    n = _parse(now)
    wm = _parse(wm_iso)
    if wm is None and require_watermark:
        return {"start_iso": None, "catch_up_exceeded": False, "basis": "missing_watermark",
                "missing_watermark": True}
    if wm is None:
        start = n - dt.timedelta(days=default_lookback_days)
        return {"start_iso": start.isoformat(), "catch_up_exceeded": False, "basis": "default_lookback"}
    if (n - wm) > dt.timedelta(days=max_catchup_days):
        return {"start_iso": (n - dt.timedelta(days=max_catchup_days)).isoformat(),
                "catch_up_exceeded": True, "basis": "catch_up_exceeded",
                "backlog_days": (n - wm).days}
    start = wm - dt.timedelta(hours=overlap_hours)
    return {"start_iso": start.isoformat(), "catch_up_exceeded": False, "basis": "watermark",
            "backlog_days": (n - wm).days}


def parse_override(start, end, now, max_days):
    """Parse the manual window override -> None (no override) or {start_iso, end_iso}.

    `start`/`end` are ISO dates (YYYY-MM-DD) or datetimes; empty strings mean unset. A date-only
    start is that day's 00:00 UTC and a date-only end is inclusive (23:59:59 UTC). end defaults to
    now and is clipped to now. Raises ValueError with a readable message on a bad override: end
    without start, unparseable values, start >= end, a future start, or a span over max_days."""
    start = (start or "").strip()
    end = (end or "").strip()
    if not start and not end:
        return None
    if not start:
        raise ValueError("window_end given without window_start")
    n = _parse(now)

    def _one(v, is_end):
        d = _parse(v)
        if d is None:
            raise ValueError("not an ISO date: %r" % v)
        if len(v) == 10 and is_end:                     # date-only end is inclusive
            d = d + dt.timedelta(days=1, seconds=-1)
        return d
    s = _one(start, False)
    e = _one(end, True) if end else n
    e = min(e, n)
    if s >= e:
        raise ValueError("window_start %s is not before window_end %s" % (s.isoformat(), e.isoformat()))
    if (e - s) > dt.timedelta(days=max_days):
        raise ValueError("override spans %d days, over the %d-day limit; backfill in smaller ranges"
                         % ((e - s).days, max_days))
    return {"start_iso": s.isoformat(), "end_iso": e.isoformat()}


def advance_decision(coverage, current_iso, current_state="present"):
    """Decide whether this run may move the watermark -> (advance: bool, ts, reason). Pure.

    - never after incredible discovery (should_advance);
    - never when the current watermark could not be read (non-regression cannot be checked);
    - an override (backfill) run never advances an existing watermark, and seeds one only when the
      state is absent (bootstrap);
    - a regular run advances only forward: a window end at or before the current watermark is a no-op."""
    cov = coverage or {}
    win = cov.get("search_window") or {}
    ts = win.get("end") or cov.get("started_at")
    if not should_advance(cov):
        return False, ts, "discovery not credible (suspicious_empty: %s)" % ",".join(
            cov.get("suspicious_empty", []) or ["?"])
    if not ts:
        return False, ts, "no search-window end recorded"
    if current_state in ("fetch_failed", "unparseable"):
        return False, ts, "current watermark unreadable (%s); refusing to overwrite it" % current_state
    absent = current_state in ("branch_missing", "file_missing") or not current_iso
    if win.get("override"):
        if absent:
            return True, ts, "bootstrap: override run seeds the absent watermark"
        return False, ts, "override (backfill) runs never advance an existing watermark"
    if not absent and _parse(ts) <= _parse(current_iso):
        return False, ts, "window end %s is not after the current watermark %s" % (ts, current_iso)
    return True, ts, "advance"


def is_due(now, wm_iso, min_interval_hours):
    """Scheduled runs proceed only when at least min_interval_hours have passed since the last
    success (true ~N-hour cadence, decoupled from calendar month). No watermark -> due."""
    wm = _parse(wm_iso)
    if wm is None:
        return True
    return (_parse(now) - wm) >= dt.timedelta(hours=min_interval_hours)


def should_advance(coverage):
    """Trusted-watermark invariant: advance ONLY after a discovery run whose mandatory source
    coverage is credible. A run with an unresolved suspicious_empty source (a zero-storm a canary
    could not clear) must not advance the watermark past an interval it failed to ingest. Absent
    flag -> credible (backward-compatible with pre-suspicious-empty coverage files)."""
    return (coverage or {}).get("discovery_credible") is not False


# ---- durable I/O ---------------------------------------------------------
def read_watermark():
    """Read origin/auto/updater-state:watermark.json -> {last_success, state}. state is one of
    present | branch_missing | file_missing | unparseable | fetch_failed, so callers can tell a
    deleted branch from a transient git/network failure instead of collapsing both to None."""
    ls = subprocess.run(["git", "ls-remote", "--exit-code", "--heads", "origin", STATE_BRANCH],
                        capture_output=True, text=True)
    if ls.returncode == 2:                              # remote reachable, no such branch
        return {"last_success": None, "state": "branch_missing"}
    if ls.returncode != 0:
        return {"last_success": None, "state": "fetch_failed"}
    f = subprocess.run(["git", "fetch", "origin", STATE_BRANCH], capture_output=True)
    if f.returncode != 0:
        return {"last_success": None, "state": "fetch_failed"}
    r = subprocess.run(["git", "show", "origin/%s:%s" % (STATE_BRANCH, STATE_FILE)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return {"last_success": None, "state": "file_missing"}
    try:
        iso = json.loads(r.stdout).get("last_success")
    except (json.JSONDecodeError, AttributeError):
        iso = None
    if _parse(iso) is None:
        return {"last_success": None, "state": "unparseable"}
    return {"last_success": iso, "state": "present"}


def read_watermark_iso():
    """Read the last-success timestamp (or None). See read_watermark() for why it is absent."""
    return read_watermark()["last_success"]


def window(mode="full"):
    """Compute the discovery window for a production run using the durable watermark."""
    cfg = config()
    wm = cfg.get("watermark", {})
    n = now_iso()
    w = compute_window(n, read_watermark_iso(),
                       wm.get("overlap_hours", 24), wm.get("max_catchup_days", 14),
                       cfg.get("lookback_days", 3), require_watermark=(mode == "full"))
    w["now_iso"] = n
    log("watermark window: %s (basis=%s, catch_up_exceeded=%s)"
        % (w["start_iso"], w["basis"], w["catch_up_exceeded"]))
    return w
