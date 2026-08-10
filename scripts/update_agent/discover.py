"""Phase 1 — large-scale discovery (recall-oriented, metadata only).

The three public sources are searched CONCURRENTLY (one deterministic worker thread per source),
each preserving its own request spacing / rate limit. Within a source, synonym queries for one
taxonomy item are consolidated into a single request (search_many). Total discovery wall time is
therefore ~max(arXiv, OpenReview, GitHub), not their sum. This is deterministic API work — no
Claude here (relevance scoring happens after, in run_phase). Per-stage timing is recorded.
"""
import argparse
import datetime as dt
import time
from concurrent.futures import ThreadPoolExecutor

from common import config, taxonomy, search_profiles, write_json, log
from sources import all_sources

# polite inter-request delays (seconds) per source. Each source runs in its OWN thread, so these
# only rate-limit that one source; the three sources still overlap in wall time.
_DELAY = {"arxiv": 3.0, "github": 3.0, "openreview": 1.0}


def _since_iso(days):
    return (dt.datetime.utcnow() - dt.timedelta(days=days)).replace(microsecond=0).isoformat()


def _profile_queries(prof, axis, item):
    qs = (prof.get(axis) or {}).get(item)
    return list(qs) if qs else ["%s LLM agent benchmark" % item]


def _search_source(sname, src, axes_items, global_qs, prof, since, limit, delay,
                   allowed_axes, per_item_cap, now_iso):
    """Deterministic per-source worker (runs in its own thread). Returns records + coverage + timing."""
    t0 = time.monotonic()
    records = {}
    cov_axes = {axis: {} for axis in axes_items}
    item_failures = item_total = requests = 0

    def add(recs, tag):
        for r in recs:
            k = r["id"]
            if k not in records:
                r = dict(r)
                r["matched_profiles"] = []
                r["discovered_at"] = now_iso
                records[k] = r
            if tag not in records[k]["matched_profiles"]:
                records[k]["matched_profiles"].append(tag)

    for axis, items in axes_items.items():
        if allowed_axes is not None and axis not in allowed_axes:
            continue
        for item in items:
            item_total += 1
            qs = _profile_queries(prof, axis, item)
            if per_item_cap:
                qs = qs[:per_item_cap]
            ok = False
            try:
                recs, n = src.search_many(qs, since, limit)
                requests += n
                add(recs, "%s: %s" % (axis[:-1].capitalize(), item))
                ok = True
            except Exception as e:  # operational failure for this item
                log("  ! %s (%s: %s) failed: %s" % (sname, axis, item, e))
            cov_axes[axis][item] = {"queries_attempted": len(qs), "status": "success" if ok else "failed"}
            if not ok:
                item_failures += 1
            if delay:
                time.sleep(delay)

    gok = False
    gatt = 0
    if global_qs:
        try:
            recs, n = src.search_many(global_qs, since, limit)
            requests += n
            add(recs, "Global")
            gok = True
            gatt = 1
        except Exception as e:
            log("  ! %s (global) failed: %s" % (sname, e))
        if delay:
            time.sleep(delay)

    frac_fail = (item_failures / item_total) if item_total else (0.0 if gok else 1.0)
    status = "success" if (frac_fail < 0.5 and (gok or not global_qs)) else "failure"
    return {
        "source": sname, "records": list(records.values()), "cov_axes": cov_axes,
        "global": {"queries_attempted": gatt, "status": "success" if gok else "failed"},
        "status": status, "requests": requests, "wall_s": round(time.monotonic() - t0, 1),
    }


def run(mode, run_dir, now_iso=None, since_iso=None):
    cfg = config()
    tax = taxonomy()
    prof = search_profiles()
    sources = all_sources()

    smoke = mode == "discovery-smoke"
    lookback = cfg["smoke"]["lookback_days"] if smoke else cfg["lookback_days"]
    since = since_iso if (since_iso and not smoke) else _since_iso(lookback)
    now_iso = now_iso or dt.datetime.utcnow().replace(microsecond=0).isoformat()

    axes_items = {}
    for axis in ("domains", "topics", "activities"):
        items = list(tax.get(axis, {}).keys())
        if smoke:
            sample = set(cfg["smoke"].get("sample_%s" % axis, []))
            items = [i for i in items if i in sample]
        axes_items[axis] = items
    global_qs = (prof.get("global") or [])[:2] if smoke else (prof.get("global") or [])

    coverage = {"run_id": run_dir.rstrip("/").split("/")[-1], "mode": mode, "started_at": now_iso,
                "lookback_days": lookback, "sources": {}, "axes": {a: {} for a in axes_items},
                "global_by_source": {}, "timing": {}}

    def make(sname, src):
        delay = 0.0 if smoke else _DELAY.get(sname, 1.0)
        limit = cfg["smoke"]["per_source_limit"] if smoke else cfg["source_limits"][sname]
        allowed = cfg.get("source_axes", {}).get(sname)
        cap = cfg.get("github_queries_per_item") if sname == "github" else None
        return lambda: _search_source(sname, src, axes_items, global_qs, prof, since, limit,
                                      delay, allowed, cap, now_iso)

    t0 = time.monotonic()
    with ThreadPoolExecutor(max_workers=len(sources)) as ex:
        results = list(ex.map(lambda f: f(), [make(n, s) for n, s in sources.items()]))
    discovery_wall = round(time.monotonic() - t0, 1)

    raw = {}
    for res in results:
        sname = res["source"]
        for r in res["records"]:
            raw[(sname, r["id"])] = r
        for axis, items in res["cov_axes"].items():
            for item, st in items.items():
                cur = coverage["axes"][axis].get(item)
                if cur is None or st["status"] == "success":   # any source covering the item counts
                    coverage["axes"][axis][item] = st
        coverage["sources"][sname] = res["status"]
        coverage["global_by_source"][sname] = res["global"]
        coverage["timing"][sname] = {"wall_s": res["wall_s"], "requests": res["requests"],
                                     "raw_hits": len(res["records"])}
        log("  %s: %s (%d requests, %ds, %d raw)"
            % (sname, res["status"], res["requests"], res["wall_s"], len(res["records"])))

    coverage["global"] = {"queries": global_qs,
                          "status": "success" if all(coverage["global_by_source"][s]["status"] == "success"
                                                     for s in sources) else "partial"}
    rbs = {}
    for r in raw.values():
        rbs[r["source"]] = rbs.get(r["source"], 0) + 1
    coverage["raw_by_source"] = rbs
    coverage["raw_hit_count"] = len(raw)
    coverage["search_window"] = {"start": since, "end": now_iso}
    coverage["timing"]["discovery_wall_s"] = discovery_wall
    coverage["finished_at"] = dt.datetime.utcnow().replace(microsecond=0).isoformat()

    write_json("%s/phase1/coverage.json" % run_dir, coverage)
    write_json("%s/phase1/raw_hits.json" % run_dir, list(raw.values()))
    return coverage


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="full")
    ap.add_argument("--run-dir", required=True)
    a = ap.parse_args()
    cov = run(a.mode, a.run_dir)
    log("discovery: sources=%s raw=%d wall=%ss"
        % (cov["sources"], cov["raw_hit_count"], cov["timing"]["discovery_wall_s"]))
