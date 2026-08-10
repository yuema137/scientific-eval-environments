"""Discovery watermark: the search window is driven by the last SUCCESSFUL production run, not a
fixed lookback. A durable JSON blob on a dedicated `auto/updater-state` branch records the last
success time; the window is `watermark - overlap → now`. Failed runs never advance the watermark,
so a later run automatically catches up. If the catch-up window grows too large, the run fails as
needs_attention rather than deep-reviewing a backlog of hundreds.
"""
import datetime as dt
import json
import subprocess

from common import config, log

STATE_BRANCH = "auto/updater-state"
STATE_FILE = "watermark.json"


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
def compute_window(now, wm_iso, overlap_hours, max_catchup_days, default_lookback_days):
    """Return {start_iso, catch_up_exceeded, basis}. `now`/`wm_iso` are ISO strings."""
    n = _parse(now)
    wm = _parse(wm_iso)
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
def read_watermark_iso():
    """Read the last-success timestamp from origin/auto/updater-state:watermark.json (or None)."""
    subprocess.run(["git", "fetch", "origin", STATE_BRANCH], capture_output=True)
    r = subprocess.run(["git", "show", "origin/%s:%s" % (STATE_BRANCH, STATE_FILE)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout).get("last_success")
    except json.JSONDecodeError:
        return None


def window(mode="full"):
    """Compute the discovery window for a production run using the durable watermark."""
    cfg = config()
    wm = cfg.get("watermark", {})
    n = now_iso()
    w = compute_window(n, read_watermark_iso(),
                       wm.get("overlap_hours", 24), wm.get("max_catchup_days", 14),
                       cfg.get("lookback_days", 3))
    w["now_iso"] = n
    log("watermark window: %s (basis=%s, catch_up_exceeded=%s)"
        % (w["start_iso"], w["basis"], w["catch_up_exceeded"]))
    return w
