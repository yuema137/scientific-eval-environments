"""Phase-1 metadata relevance scoring + admission (the main precision improvement).

After deterministic prefilter + cross-source merge + existing-work dedup, a bounded Claude
scorer reads ONLY lightweight metadata and triages candidates into deep_review /
reject_low_relevance / uncertain. Admission is ranked triage — NOT silent truncation:

  * admitted = all deep_review candidates, plus uncertain candidates (highest confidence first)
    only while the queue stays within the deep-review safety budget;
  * if deep_review alone exceeds the cap, everything deep_review is kept so Phase 2's cap check
    fails the run as needs_attention (conservative — never truncates real positives silently);
  * a scorer OPERATIONAL failure marks candidates 'uncertain' (never a silent reject).
"""
import json
import re

from common import config, log
from run_claude_worker import run_worker, parallel

SCHEMA = {
    "type": "object",
    "properties": {"results": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "candidate_id": {"type": "string"},
            "decision": {"type": "string", "enum": ["deep_review", "reject_low_relevance", "uncertain"]},
            "confidence": {"type": "number"},
            "reason": {"type": "string"},
        },
        "required": ["candidate_id", "decision"],
    }}},
    "required": ["results"],
}


def _meta(c):
    srcs = ",".join(sorted({r["source"] for r in c.get("source_records", [])}))
    return {
        "candidate_id": c["candidate_id"],
        "title": c.get("title", ""),
        "abstract_or_description": (c.get("abstract_or_description") or "")[:1200],
        "authors": (c.get("authors") or [])[:8],
        "sources": srcs,
        "matched_profiles": c.get("matched_profiles", [])[:8],
    }


def score(candidates, cfg=None, batch_size=None, max_workers=None):
    """Return {candidate_id: {decision, confidence, reason, source}}.
    Operational failure -> 'uncertain' (fail-open on recall, never silent reject."""
    cfg = cfg or config()
    batch_size = batch_size or cfg.get("relevance", {}).get("batch_size", 12)
    max_workers = max_workers or cfg["limits"].get("max_relevance_workers", 4)
    batches = [candidates[i:i + batch_size] for i in range(0, len(candidates), batch_size)]

    def make(batch):
        payload = json.dumps([_meta(c) for c in batch], ensure_ascii=False)
        prompt = ("Triage these candidates (metadata only). Return the strict JSON object with one "
                  "result per candidate_id.\nCANDIDATES:\n" + payload)
        return lambda: (batch, run_worker("relevance-scorer", "score", prompt, ".",
                                          cfg["claude"].get("scorer_max_turns", 6), schema=SCHEMA,
                                          model=cfg["claude"].get("relevance_model")))

    results = parallel([make(b) for b in batches], max_workers)
    out = {}
    for item in results:
        if not item:
            continue
        batch, r = item
        decided = {}
        if r and r.get("ok"):
            so = r.get("structured_output") or _extract(r.get("result", ""))
            for row in ((so or {}).get("results") or []):
                cid = row.get("candidate_id")
                if cid:
                    decided[cid] = {"decision": row.get("decision", "uncertain"),
                                    "confidence": float(row.get("confidence") or 0.5),
                                    "reason": row.get("reason", ""), "source": "scorer"}
        for c in batch:
            cid = c["candidate_id"]
            out[cid] = decided.get(cid, {"decision": "uncertain", "confidence": 0.5,
                                         "reason": "scorer unavailable/omitted -> uncertain (fail-open)",
                                         "source": "fail_open"})
    return out


def _github_only(c):
    return {r["source"] for r in c.get("source_records", [])} == {"github"}


def _rank_key(cid, decisions):
    # deterministic, reproducible priority: confidence desc, then candidate_id asc (stable tie-break)
    return (-float(decisions[cid].get("confidence") or 0.0), cid)


def admit(candidates, decisions, cap):
    """Budgeted, ranked, source-aware admission. Returns (admitted, report).

    `cap` is a per-run PROCESSING BUDGET, not a completeness requirement: a credible discovery run
    may legitimately surface more metadata-plausible works than one run can deep-review. Priority:
    deep_review first (ranked by confidence), then paper-backed `uncertain` fills any remaining
    budget. A GitHub-only `uncertain` is never admitted (repo metadata carries far less signal than
    an abstract). Candidates that don't fit the budget are recorded as `deferred_by_budget` — this is
    an explicit bounded-coverage policy, NOT silent truncation and NOT a persistent backlog: deferred
    items are retained for observability / manual backfill only, never auto-processed later.
    """
    by_id = {c["candidate_id"]: c for c in candidates}
    deep = [cid for cid, d in decisions.items() if d["decision"] == "deep_review" and cid in by_id]
    uncertain = [cid for cid, d in decisions.items() if d["decision"] == "uncertain" and cid in by_id]
    rejected = [cid for cid, d in decisions.items() if d["decision"] == "reject_low_relevance"]

    deep_ranked = sorted(deep, key=lambda cid: _rank_key(cid, decisions))
    uncertain_admittable = sorted([cid for cid in uncertain if not _github_only(by_id[cid])],
                                  key=lambda cid: _rank_key(cid, decisions))
    gh_only_uncertain = [cid for cid in uncertain if _github_only(by_id[cid])]

    # fill the budget: highest-priority deep_review first, then paper-backed uncertain
    admitted_deep = deep_ranked[:cap]
    deferred_deep = deep_ranked[cap:]
    room = cap - len(admitted_deep)
    admitted_uncertain = uncertain_admittable[:room] if room > 0 else []
    deferred_uncertain = uncertain_admittable[room:] if room > 0 else list(uncertain_admittable)

    admitted_ids = admitted_deep + admitted_uncertain
    admitted = [by_id[cid] for cid in admitted_ids]

    def _defrow(cid):
        c = by_id[cid]
        return {"candidate_id": cid, "title": c.get("title", ""),
                "sources": sorted({r["source"] for r in c.get("source_records", [])}),
                "confidence": decisions[cid].get("confidence"),
                "decision": decisions[cid]["decision"],
                "matched_profiles": c.get("matched_profiles", []),
                "reason": "deferred_by_budget"}
    deferred = [_defrow(cid) for cid in (deferred_deep + deferred_uncertain)]

    report = {
        "deep_review": len(deep),
        "uncertain_total": len(uncertain),
        "uncertain_admitted": len(admitted_uncertain),
        "uncertain_github_only_excluded": len(gh_only_uncertain),
        "rejected_low_relevance": len(rejected),
        "admitted": len(admitted),
        "cap": cap,
        "deferred_by_budget": len(deferred),
        "deferred_candidates": deferred,
        "budget_exceeded": len(deep) > cap,   # deep_review alone exceeded the budget (reporting only)
    }
    return admitted, report


def _extract(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
