"""Phase 1 — large-scale discovery (recall-oriented, metadata only).

The three public sources are searched CONCURRENTLY (one deterministic worker thread per source),
each preserving its own request spacing / rate limit. Within a source, synonym queries for one
taxonomy item are consolidated into a single request (search_many). Total discovery wall time is
therefore ~max(arXiv, OpenReview, GitHub), not their sum. This is deterministic API work — no
Claude here (relevance scoring happens after, in run_phase). Per-stage timing is recorded.
"""
import argparse
import datetime as dt
import re
import time
from concurrent.futures import ThreadPoolExecutor

from common import config, taxonomy, search_profiles, write_json, log
import prefilter
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
    failed_items = []

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
                failed_items.append("%s/%s" % (axis, item))
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

    # Tri-state source health (conservative, bounded tolerance).
    #   success          — every attempted query worked.
    #   degraded_success — the source is clearly reachable AND mandatory taxonomy coverage is
    #                      essentially complete, but a minority of queries failed transiently:
    #                        (a) all per-item queries succeeded and only the broad GLOBAL catch-all
    #                            failed  (the exact production case we must tolerate), OR
    #                        (b) a very small bounded number of per-item queries failed:
    #                            <= MAX_DEGRADED_ITEM_FAILS AND <= MAX_DEGRADED_ITEM_FRAC.
    #                      Discovery may proceed; the exact lost source-item coverage is recorded.
    #   failure          — failures exceed that bounded tolerance, or the source is broadly
    #                      unavailable (no item queries, or the only query — global — failed).
    # A single source degrading never silently drops a taxonomy item: validate_discovery's per-axis
    # check (merged across ALL sources) independently blocks the run if an item lost every source's
    # coverage. Source health and cross-source completeness are deliberately separate concerns.
    MAX_DEGRADED_ITEM_FAILS = 2
    MAX_DEGRADED_ITEM_FRAC = 0.10
    frac_fail = (item_failures / item_total) if item_total else 0.0
    lost = (" [lost: %s]" % ",".join(failed_items)) if failed_items else ""
    if item_total and item_failures == item_total:
        status, detail = "failure", "all %d item queries failed" % item_total
    elif item_failures == 0 and (gok or not global_qs):
        status, detail = "success", ""
    elif item_total == 0 and global_qs and not gok:
        status, detail = "failure", "no item queries and global query failed"
    elif item_failures <= MAX_DEGRADED_ITEM_FAILS and frac_fail <= MAX_DEGRADED_ITEM_FRAC:
        parts = []
        if item_failures:
            parts.append("%d/%d item queries failed%s" % (item_failures, item_total, lost))
        if global_qs and not gok:
            parts.append("global catch-all query failed")
        status, detail = "degraded_success", "; ".join(parts) or "supplemental query failed"
    else:
        status, detail = "failure", ("%d/%d item queries failed (exceeds degraded tolerance "
                                     "<=%d and <=%d%%)%s"
                                     % (item_failures, item_total, MAX_DEGRADED_ITEM_FAILS,
                                        int(MAX_DEGRADED_ITEM_FRAC * 100), lost))
    return {
        "source": sname, "records": list(records.values()), "cov_axes": cov_axes,
        "global": {"queries_attempted": gatt, "status": "success" if gok else "failed"},
        "status": status, "status_detail": detail,
        "requests": requests, "wall_s": round(time.monotonic() - t0, 1),
        "item_total": item_total, "item_failures": item_failures,
    }


# ---- arXiv OAI incremental harvest + local taxonomy matching --------------------------------
# Tokens too generic to distinguish a taxonomy item (they appear in nearly every eval paper). A
# profile query's DISTINCTIVE tokens (what's left) are what a harvested record must contain to be
# tagged with that item — e.g. "LLM agent physics benchmark" -> distinctive {physics}.
_GENERIC_TOKENS = {
    "llm", "llms", "agent", "agents", "agentic", "benchmark", "benchmarks", "evaluation",
    "evaluations", "evaluate", "evaluating", "eval", "ai", "scientific", "science", "sciences",
    "autonomous", "model", "models", "for", "the", "a", "an", "of", "on", "and", "to", "in",
    "with", "using", "based", "via", "problem", "solving", "task", "tasks", "reasoning",
}
# A harvested record is a candidate only if it names a CONCRETE benchmark/evaluation artifact
# (prefilter.EVAL_STRONG: benchmark/testbed/leaderboard/arena/gym/eval suite/environment) AND has an
# agent or LLM angle. This replaces the targeting the Search-API ranking used to provide — the OAI
# harvest sees every recent paper, so a bare "we evaluate our method on <science>" must NOT pass (that
# is the prefilter's loose EVAL+SCI floodgate). The downstream prefilter + relevance scorer decide last.
_LLM_SIGNAL = re.compile(r"\b(llm|llms|large language model|language model|foundation model|"
                         r"multimodal model|gpt[-\s]?\d|vision[-\s]language)\b", re.I)


def _distinctive(query):
    return [t for t in re.findall(r"[a-z0-9][a-z0-9\-]+", query.lower())
            if t not in _GENERIC_TOKENS and len(t) > 2]


def _local_match(rec, prof, axes_items, allowed_axes):
    """Return the matched_profiles tags for one harvested record (empty = drop). A record is kept
    when it names a concrete benchmark/eval artifact AND has an agent/LLM angle; axis tags are added
    when a profile's distinctive tokens are all present. Mirrors, locally, the old Search-API fan-out."""
    hay = " ".join([rec.get("title", ""), rec.get("abstract_or_description", ""),
                    rec.get("categories", "")]).lower()
    if not (prefilter.EVAL_STRONG.search(hay)
            and (prefilter.AGENT.search(hay) or _LLM_SIGNAL.search(hay))):
        return []
    tags = ["Global"]                                    # broad catch-all: concrete benchmark + agent/LLM
    for axis, items in axes_items.items():
        if allowed_axes is not None and axis not in allowed_axes:
            continue
        for item in items:
            for q in _profile_queries(prof, axis, item):
                dts = _distinctive(q)
                if dts and all(re.search(r"\b%s\b" % re.escape(t), hay) for t in dts):
                    tags.append("%s: %s" % (axis[:-1].capitalize(), item))
                    break
    return tags


def _harvest_arxiv(sname, src, axes_items, global_qs, prof, since, now_iso, allowed_axes,
                   max_pages, delay, now_stamp):
    """Deterministic arXiv collector: OAI harvest -> local taxonomy match. Returns the same result
    shape as _search_source so downstream (raw merge, coverage, credibility) is unchanged."""
    t0 = time.monotonic()
    from_date, until_date = since[:10], now_iso[:10]

    def _do():
        return src.harvest(from_date, until_date, max_pages=max_pages, delay=delay)

    raw, requests, truncated, transport_ok, err = [], 0, False, True, None
    try:
        raw, requests, truncated = _do()
    except Exception as e:  # noqa: BLE001 - transport/parse failure
        transport_ok, err = False, str(e)
        log("  ! arxiv OAI harvest failed: %s" % e)
    canary_note = ""
    if transport_ok and not raw:                          # zero-storm: one bounded canary re-harvest
        log("  ! arxiv OAI returned 0 records for %s..%s -> canary re-harvest" % (from_date, until_date))
        try:
            raw2, req2, truncated = _do()
            requests += req2
            if raw2:
                raw, canary_note = raw2, " (recovered on canary)"
        except Exception as e:  # noqa: BLE001
            log("  ! arxiv canary failed: %s" % e)

    matched = {}
    for rec in raw:
        tags = _local_match(rec, prof, axes_items, allowed_axes)
        if not tags:
            continue
        r = dict(rec)
        r["matched_profiles"] = tags
        r["discovered_at"] = now_stamp
        matched[rec["id"]] = r

    cov_axes = {axis: {} for axis in axes_items}
    for axis, items in axes_items.items():
        if allowed_axes is not None and axis not in allowed_axes:
            continue
        for item in items:                                # locally evaluated against every harvested record
            cov_axes[axis][item] = {"queries_attempted": 1,
                                    "status": "success" if transport_ok else "failed"}
    item_total = sum(len(v) for v in cov_axes.values())

    if not transport_ok:
        status, detail = "failure", "OAI harvest transport error: %s" % (err or "")[:120]
    elif truncated:
        status, detail = "suspicious_empty", "harvest truncated at max_pages -> coverage incomplete"
    elif not raw:
        status, detail = "suspicious_empty", ("OAI returned 0 records for %s..%s (canary also empty)"
                                              % (from_date, until_date))
    else:
        status, detail = "success", ""
    return {
        "source": sname, "records": list(matched.values()), "cov_axes": cov_axes,
        "global": {"queries_attempted": 1, "status": "success" if transport_ok else "failed"},
        "status": status, "status_detail": detail + canary_note, "requests": requests,
        "wall_s": round(time.monotonic() - t0, 1), "item_total": item_total, "item_failures": 0,
        "raw_harvested": len(raw),
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
                "global_by_source": {}, "source_status_detail": {}, "timing": {}}

    def make(sname, src):
        allowed = cfg.get("source_axes", {}).get(sname)
        if sname == "arxiv":                              # OAI incremental harvest + local matching
            mp = 2 if smoke else cfg.get("arxiv_oai", {}).get("max_pages", 50)
            d = 0.0 if smoke else _DELAY.get("arxiv", 3.0)
            return lambda: _harvest_arxiv(sname, src, axes_items, global_qs, prof, since, now_iso,
                                          allowed, mp, d, now_iso)
        delay = 0.0 if smoke else _DELAY.get(sname, 1.0)
        limit = cfg["smoke"]["per_source_limit"] if smoke else cfg["source_limits"][sname]
        cap = cfg.get("github_queries_per_item") if sname == "github" else None
        return lambda: _search_source(sname, src, axes_items, global_qs, prof, since, limit,
                                      delay, allowed, cap, now_iso)

    thunks = {n: make(n, s) for n, s in sources.items()}
    order = list(thunks)
    t0 = time.monotonic()
    with ThreadPoolExecutor(max_workers=len(sources)) as ex:
        results = dict(zip(order, ex.map(lambda n: thunks[n](), order)))
    discovery_wall = round(time.monotonic() - t0, 1)

    # Credibility: sources self-report `suspicious_empty` when their coverage is not trustworthy —
    # the arXiv OAI collector runs its own bounded zero-storm canary and flags an empty/truncated
    # harvest; a transport failure is `failure`. A run is credible only when no mandatory source is
    # suspicious_empty; on an incredible run the watermark is NOT advanced (watermark.should_advance),
    # so a silent outage never skips the interval it failed to ingest.
    coverage["suspicious_empty"] = [n for n in order if results[n]["status"] == "suspicious_empty"]
    coverage["discovery_credible"] = not coverage["suspicious_empty"]

    raw = {}
    for res in results.values():
        sname = res["source"]
        for r in res["records"]:
            raw[(sname, r["id"])] = r
        for axis, items in res["cov_axes"].items():
            for item, st in items.items():
                cur = coverage["axes"][axis].get(item)
                if cur is None or st["status"] == "success":   # any source covering the item counts
                    coverage["axes"][axis][item] = st
        coverage["sources"][sname] = res["status"]
        coverage["source_status_detail"][sname] = res.get("status_detail", "")
        coverage["global_by_source"][sname] = res["global"]
        coverage["timing"][sname] = {"wall_s": res["wall_s"], "requests": res["requests"],
                                     "raw_hits": len(res["records"])}
        log("  %s: %s%s (%d requests, %ds, %d raw)"
            % (sname, res["status"], (" [%s]" % res["status_detail"]) if res.get("status_detail") else "",
               res["requests"], res["wall_s"], len(res["records"])))

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
