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
from sources import all_sources, first_submission_estimate

# polite inter-request delays (seconds) per source. Each source runs in its OWN thread, so these
# only rate-limit that one source; the three sources still overlap in wall time.
_DELAY = {"arxiv": 3.0, "github": 3.0, "openreview": 1.0, "huggingface": 1.0}


def _since_iso(days):
    return (dt.datetime.utcnow() - dt.timedelta(days=days)).replace(microsecond=0).isoformat()


def _profile_queries(prof, axis, item):
    qs = (prof.get(axis) or {}).get(item)
    return list(qs) if qs else ["%s LLM agent benchmark" % item]


def _search_source(sname, src, axes_items, global_qs, prof, since, limit, delay,
                   allowed_axes, per_item_cap, now_iso, until=None):
    """Deterministic per-source worker (runs in its own thread). Returns records + coverage + timing."""
    t0 = time.monotonic()
    records = {}
    cov_axes = {axis: {} for axis in axes_items}
    win_kw = {"until_iso": until} if until else {}         # adapters without an upper bound ignore it
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
                recs, n = src.search_many(qs, since, limit, **win_kw)
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
            recs, n = src.search_many(global_qs, since, limit, **win_kw)
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
        "warnings": src.warnings() if hasattr(src, "warnings") else [],
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


def _day_chunks(from_date, until_date, chunk_days):
    """Split the inclusive day range [from_date, until_date] (YYYY-MM-DD) into consecutive inclusive
    chunks of at most chunk_days days, oldest first."""
    a = dt.date.fromisoformat(from_date)
    b = dt.date.fromisoformat(until_date)
    step = max(1, int(chunk_days or 1))
    out = []
    while a <= b:
        e = min(b, a + dt.timedelta(days=step - 1))
        out.append((a.isoformat(), e.isoformat()))
        a = e + dt.timedelta(days=1)
    return out


def _is_revision(rec, since, grace_days):
    """True when an OAI record's first submission predates the window by more than grace_days, i.e.
    its only activity inside the window is a revision or metadata update. Unknown -> False (kept)."""
    first, basis = first_submission_estimate(rec.get("id", ""), rec.get("date", ""))
    if first is None:
        return False, None, basis
    cutoff = dt.date.fromisoformat(since[:10]) - dt.timedelta(days=grace_days)
    return first < cutoff, first.isoformat(), basis


def _harvest_chunks(src, chunks, max_pages, max_total_pages, delay):
    """Harvest each chunk with its own page budget, under an overall page budget. Returns
    (records_by_id, chunk_reports, requests). A chunk that hits its page cap, errors, or is skipped
    because the overall budget ran out is reported as such; nothing is truncated silently."""
    raw, reports, requests = {}, [], 0
    budget = max_total_pages
    for i, (a, b) in enumerate(chunks):
        rep = {"from": a, "until": b, "records": 0, "requests": 0, "status": "ok"}
        if budget is not None and budget <= 0:
            rep["status"] = "skipped_budget"
            reports.append(rep)
            continue
        mp = min(max_pages, budget) if budget is not None else max_pages
        try:
            recs, n, truncated = src.harvest(a, b, max_pages=mp, delay=delay)
            rep.update(records=len(recs), requests=n)
            if truncated:
                rep["status"] = "truncated"
            for r in recs:
                raw[r["id"]] = r
        except Exception as e:  # noqa: BLE001 - transport/parse failure for this chunk only
            rep.update(status="error", error=str(e)[:160], requests=1)
            n = 1
            log("  ! arxiv OAI harvest %s..%s failed: %s" % (a, b, e))
        requests += rep["requests"]
        if budget is not None:
            budget -= max(n, 1)
        reports.append(rep)
        if delay and i < len(chunks) - 1:
            time.sleep(delay)
    return raw, reports, requests


def _compact(rec):
    return {k: rec.get(k, "") for k in ("id", "title", "date", "datestamp", "categories")}


def _harvest_arxiv(sname, src, axes_items, global_qs, prof, since, until, allowed_axes,
                   max_pages, delay, now_stamp, chunk_days=1, max_total_pages=None,
                   revision_grace_days=30):
    """Deterministic arXiv collector: chunked OAI harvest -> revision filter -> local taxonomy
    match. Returns the same result shape as _search_source so downstream (raw merge, coverage,
    credibility) is unchanged, plus a `harvest` report and the two drop artifacts.

    The window is harvested in chunk_days-day chunks, each with its own max_pages budget, so one
    large window can no longer exhaust a single page cap part-way (2026-09/10: a 60-day harvest
    stopped at datestamp 09-18 and the rest of the window was never seen). max_total_pages bounds the
    whole run; an incomplete chunk keeps the source suspicious_empty, so the watermark holds."""
    t0 = time.monotonic()
    from_date, until_date = since[:10], until[:10]
    chunks = _day_chunks(from_date, until_date, chunk_days)
    raw, reports, requests = _harvest_chunks(src, chunks, max_pages, max_total_pages, delay)
    errors = [c for c in reports if c["status"] == "error"]
    canary_note = ""
    if not raw and not errors:                            # zero-storm: one bounded canary re-harvest
        log("  ! arxiv OAI returned 0 records for %s..%s -> canary re-harvest" % (from_date, until_date))
        raw2, reports2, req2 = _harvest_chunks(src, chunks, max_pages, max_total_pages, delay)
        requests += req2
        if raw2:
            raw, reports, canary_note = raw2, reports2, " (recovered on canary)"
        errors = [c for c in reports if c["status"] == "error"]

    # Classify every harvested record. Only the two relevant drop classes are kept as artifacts:
    # revisions that WOULD have matched (they used to take deep-review slots), and new-work records
    # the local gate rejected (compact, no abstract: the gate's recall can be audited from them).
    matched, revisions, unmatched = {}, [], []
    revisions_total = 0
    for rec in raw.values():
        is_rev, first, basis = _is_revision(rec, since, revision_grace_days)
        tags = _local_match(rec, prof, axes_items, allowed_axes)
        if is_rev:
            revisions_total += 1
            if tags:
                d = dict(_compact(rec), first_submitted_estimate=first, estimate_basis=basis,
                         updated=rec.get("updated", ""), matched_profiles=tags)
                revisions.append(d)
            continue
        if not tags:
            unmatched.append(_compact(rec))
            continue
        r = dict(rec)
        r["matched_profiles"] = tags
        r["discovered_at"] = now_stamp
        matched[rec["id"]] = r

    cov_axes = {axis: {} for axis in axes_items}
    transport_ok = len(errors) < len(chunks)              # at least one chunk was reachable
    for axis, items in axes_items.items():
        if allowed_axes is not None and axis not in allowed_axes:
            continue
        for item in items:                                # locally evaluated against every harvested record
            cov_axes[axis][item] = {"queries_attempted": 1,
                                    "status": "success" if transport_ok else "failed"}
    item_total = sum(len(v) for v in cov_axes.values())

    incomplete = [c for c in reports if c["status"] != "ok"]
    through = None                                        # last day of the complete prefix
    for c in reports:
        if c["status"] != "ok":
            break
        through = c["until"]
    if not transport_ok:
        status, detail = "failure", "OAI harvest transport error: %s" % (errors[0].get("error") or "")[:120]
    elif incomplete:
        kinds = {}
        for c in incomplete:
            kinds.setdefault(c["status"], []).append(c["from"])
        status = "suspicious_empty"
        detail = ("harvest incomplete -> coverage incomplete: %s; complete through %s"
                  % ("; ".join("%s %d chunk(s) from %s" % (k, len(v), v[0]) for k, v in sorted(kinds.items())),
                     through or "none"))
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
        "harvest": {"window": [from_date, until_date], "chunk_days": chunk_days,
                    "max_pages_per_chunk": max_pages, "max_total_pages": max_total_pages,
                    "chunks": reports, "complete_through": through,
                    "raw_harvested": len(raw), "revisions_dropped_total": revisions_total,
                    "revisions_dropped_matching": len(revisions),
                    "revision_grace_days": revision_grace_days,
                    "local_unmatched": len(unmatched), "matched": len(matched)},
        "revisions_dropped": revisions, "local_unmatched": unmatched,
    }


def _zero_hit_warning(res, since, until, min_window_days):
    """OpenReview canary: zero records across every query over a non-trivial window is reported
    (visible, non-blocking). OpenReview is relevance-ranked with no server-side date window, so a
    short window can be legitimately empty; arXiv stays the primary recency source."""
    if res["status"] not in ("success", "degraded_success") or res["records"]:
        return None
    try:
        days = (dt.datetime.fromisoformat(until[:19]) - dt.datetime.fromisoformat(since[:19])).days
    except ValueError:
        return None
    if days < min_window_days:
        return None
    return ("0 records across %d request(s) for a %d-day window (relevance-ranked endpoint; recent "
            "submissions may sit below the scanned depth) -- check the source if this persists"
            % (res["requests"], days))


def run(mode, run_dir, now_iso=None, since_iso=None, until_iso=None, window_info=None):
    """`since_iso`/`until_iso` bound the window (until defaults to now). `window_info` is merged
    into coverage["search_window"] (basis, override flag, watermark seen at discovery time)."""
    cfg = config()
    tax = taxonomy()
    prof = search_profiles()
    sources = all_sources()

    smoke = mode == "discovery-smoke"
    lookback = cfg["smoke"]["lookback_days"] if smoke else cfg["lookback_days"]
    since = since_iso if (since_iso and not smoke) else _since_iso(lookback)
    now_iso = now_iso or dt.datetime.utcnow().replace(microsecond=0).isoformat()
    until = until_iso if (until_iso and not smoke) else now_iso

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
            oai = cfg.get("arxiv_oai", {})
            mp = 2 if smoke else oai.get("max_pages", 50)
            total = 4 if smoke else oai.get("max_total_pages", 300)
            d = 0.0 if smoke else _DELAY.get("arxiv", 3.0)
            return lambda: _harvest_arxiv(sname, src, axes_items, global_qs, prof, since, until,
                                          allowed, mp, d, now_iso,
                                          chunk_days=oai.get("chunk_days", 1), max_total_pages=total,
                                          revision_grace_days=oai.get("revision_grace_days", 30))
        delay = 0.0 if smoke else _DELAY.get(sname, 1.0)
        limit = cfg["smoke"]["per_source_limit"] if smoke else cfg["source_limits"][sname]
        cap = cfg.get("github_queries_per_item") if sname == "github" else None
        return lambda: _search_source(sname, src, axes_items, global_qs, prof, since, limit,
                                      delay, allowed, cap, now_iso, until)

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

    # Non-blocking coverage warnings: a source's own notes (e.g. HuggingFace days not fetched) and
    # the OpenReview zero-hit canary. They never change credibility; they make a gap visible.
    coverage["source_warnings"] = {}
    zero_days = cfg.get("openreview", {}).get("zero_hit_min_window_days", 3)
    for n in order:
        w = list(results[n].get("warnings") or [])
        if n == "openreview" and not smoke:
            z = _zero_hit_warning(results[n], since, until, zero_days)
            if z:
                w.append(z)
        if w:
            coverage["source_warnings"][n] = w
            for x in w:
                log("  ! %s warning: %s" % (n, x))

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
    coverage["search_window"] = dict(window_info or {}, start=since, end=until)
    if "arxiv" in results and results["arxiv"].get("harvest"):
        coverage["arxiv_harvest"] = results["arxiv"]["harvest"]
    coverage["timing"]["discovery_wall_s"] = discovery_wall
    coverage["finished_at"] = dt.datetime.utcnow().replace(microsecond=0).isoformat()

    write_json("%s/phase1/coverage.json" % run_dir, coverage)
    write_json("%s/phase1/raw_hits.json" % run_dir, list(raw.values()))
    if "arxiv" in results and results["arxiv"].get("harvest"):
        # Audit artifacts for the two arXiv drops that happen BEFORE raw_hits.json: revisions of old
        # papers that the local gate would have matched, and new-work records the gate rejected.
        write_json("%s/phase1/arxiv_revisions_dropped.json" % run_dir,
                   results["arxiv"].get("revisions_dropped", []))
        write_json("%s/phase1/arxiv_local_unmatched.json" % run_dir,
                   results["arxiv"].get("local_unmatched", []))
    return coverage


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="full")
    ap.add_argument("--run-dir", required=True)
    a = ap.parse_args()
    cov = run(a.mode, a.run_dir)
    log("discovery: sources=%s raw=%d wall=%ss"
        % (cov["sources"], cov["raw_hit_count"], cov["timing"]["discovery_wall_s"]))
