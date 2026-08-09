"""Phase 1 — large-scale discovery (recall-oriented, metadata only).

Runs the source x axis-profile query matrix, records a coverage manifest proving the
search space was attempted, and emits deduplicated raw hits. Deep validation and
candidate filtering happen later (deduplicate.py -> Phase 2).
"""
import argparse
import datetime as dt
import time

from common import config, taxonomy, search_profiles, write_json, log
from sources import all_sources

# polite inter-request delays (seconds) per source in full mode
_DELAY = {"arxiv": 3.0, "github": 2.0, "openreview": 1.0}


def _since_iso(days):
    return (dt.datetime.utcnow() - dt.timedelta(days=days)).replace(microsecond=0).isoformat()


def _profile_queries(prof, axis, item):
    qs = (prof.get(axis) or {}).get(item)
    # every taxonomy item is guaranteed coverage: explicit profile, else a derived query
    return list(qs) if qs else ["%s LLM agent benchmark" % item]


def run(mode, run_dir, now_iso=None):
    cfg = config()
    tax = taxonomy()
    prof = search_profiles()
    sources = all_sources()

    smoke = mode == "discovery-smoke"
    lookback = cfg["smoke"]["lookback_days"] if smoke else cfg["lookback_days"]
    since = _since_iso(lookback)
    now_iso = now_iso or dt.datetime.utcnow().replace(microsecond=0).isoformat()

    # which axis items to cover
    axes_items = {}
    for axis in ("domains", "topics", "activities"):
        items = list(tax.get(axis, {}).keys())
        if smoke:
            sample = set(cfg["smoke"].get("sample_%s" % axis, []))
            items = [i for i in items if i in sample]
        axes_items[axis] = items

    global_qs = (prof.get("global") or [])
    if smoke:
        global_qs = global_qs[:2]     # keep the smoke tiny
    coverage = {
        "run_id": run_dir.rstrip("/").split("/")[-1],
        "mode": mode,
        "started_at": now_iso,
        "lookback_days": lookback,
        "sources": {},
        "axes": {a: {} for a in axes_items},
        "global": {},
    }
    raw = {}          # key (source,id) -> record (+ matched_profiles)
    source_ok = {n: True for n in sources}

    def do_search(src, query, tag, limit):
        try:
            recs = src.search(query, since, limit)
        except Exception as e:  # operational failure
            log("  ! %s query failed (%s): %s" % (src.name, tag, e))
            return None
        for r in recs:
            key = (r["source"], r["id"])
            if key not in raw:
                r = dict(r)
                r["matched_profiles"] = []
                r["discovered_at"] = now_iso
                raw[key] = r
            if tag not in raw[key]["matched_profiles"]:
                raw[key]["matched_profiles"].append(tag)
        return len(recs)

    for sname, src in sources.items():
        limit = cfg["smoke"]["per_source_limit"] if smoke else cfg["source_limits"][sname]
        delay = 0.0 if smoke else _DELAY.get(sname, 1.0)
        item_failures = 0
        item_total = 0
        # axis items
        for axis, items in axes_items.items():
            for item in items:
                item_total += 1
                attempted = 0
                ok = False
                for q in _profile_queries(prof, axis, item):
                    res = do_search(src, q, "%s: %s" % (axis[:-1].capitalize(), item), limit)
                    attempted += 1
                    if res is not None:
                        ok = True
                    if delay:
                        time.sleep(delay)
                coverage["axes"][axis][item] = {"queries_attempted": attempted,
                                                "status": "success" if ok else "failed"}
                if not ok:
                    item_failures += 1
        # global queries
        gattempted = 0
        gok = False
        for q in global_qs:
            res = do_search(src, q, "Global", limit)
            gattempted += 1
            if res is not None:
                gok = True
            if delay:
                time.sleep(delay)
        coverage.setdefault("global_by_source", {})[sname] = {
            "queries_attempted": gattempted, "status": "success" if gok else "failed"}
        # source status: fail if it could not complete a substantial portion
        frac_fail = (item_failures / item_total) if item_total else (0.0 if gok else 1.0)
        source_ok[sname] = frac_fail < 0.5 and (gok or not global_qs)
        coverage["sources"][sname] = "success" if source_ok[sname] else "failure"
        log("  %s: %s (%d items, %d failed, %d raw so far)"
            % (sname, coverage["sources"][sname], item_total, item_failures, len(raw)))

    coverage["global"] = {"queries": global_qs,
                          "status": "success" if all(
                              coverage["global_by_source"][s]["status"] == "success"
                              for s in sources) else "partial"}
    coverage["raw_hit_count"] = len(raw)
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
    log("discovery: sources=%s raw=%d" % (cov["sources"], cov["raw_hit_count"]))
