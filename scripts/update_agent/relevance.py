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
                                          cfg["claude"].get("scorer_max_turns", 6), schema=SCHEMA))

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


def admit(candidates, decisions, cap):
    """Ranked triage. Returns (admitted, report)."""
    by_id = {c["candidate_id"]: c for c in candidates}
    deep = [cid for cid, d in decisions.items() if d["decision"] == "deep_review"]
    uncertain = sorted([cid for cid, d in decisions.items() if d["decision"] == "uncertain"],
                       key=lambda cid: -decisions[cid]["confidence"])
    rejected = [cid for cid, d in decisions.items() if d["decision"] == "reject_low_relevance"]

    admitted_ids = list(deep)
    room = cap - len(admitted_ids)
    admitted_from_uncertain = uncertain[:room] if room > 0 else []
    admitted_ids += admitted_from_uncertain

    admitted = [by_id[cid] for cid in admitted_ids if cid in by_id]
    report = {
        "deep_review": len(deep),
        "uncertain_total": len(uncertain),
        "uncertain_admitted": len(admitted_from_uncertain),
        "rejected_low_relevance": len(rejected),
        "admitted": len(admitted),
        "cap": cap,
        "overflow": len(deep) > cap,   # deep_review alone exceeds cap -> Phase 2 will needs_attention
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
