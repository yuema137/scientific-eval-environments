"""Deduplicate raw discovery hits into a clean candidate queue.

  1. cross-source merge (arXiv + OpenReview + GitHub for the same work -> ONE candidate)
  2. drop works already in the repository (existing-work identity index)
  3. drop works already proposed on the open automated-update branch (pending index)
  4. light scope pre-filter (recall-oriented; Phase 2 does the real scope check)

Produces candidates.json, duplicate_matches.json, rejected.json.
"""
import argparse
import os
import re

from common import REPO_ROOT, normalize_title, normalize_arxiv_id, write_json, read_json, log
import inventory as inv

# obvious-irrelevance guard: a raw hit with none of these tokens anywhere is dropped.
_RELEVANT = re.compile(
    r"\b(agent|agentic|benchmark|evaluat|llm|language model|scientific|science|"
    r"research|reasoning|autonomous|trajector|reproduc)\w*", re.I)


def _ids(rec):
    """Return normalized identity keys for one raw record."""
    keys = set()
    if rec["source"] == "arxiv":
        a = normalize_arxiv_id(rec["id"])
        if a:
            keys.add(("arxiv", a))
    if rec["source"] == "openreview":
        keys.add(("openreview", rec["id"]))
    if rec["source"] == "github":
        m = re.search(r"github\.com/([^/]+)/([^/#?]+)", rec["url"], re.I)
        if m:
            keys.add(("github", "github.com/%s/%s" % (m.group(1).lower(),
                     re.sub(r"\.git$", "", m.group(2).lower()))))
    tn = normalize_title(rec["title"])
    if tn:
        keys.add(("title_norm", tn))
    return keys


def _merge_key(existing_keys, rec_keys):
    return bool(existing_keys & rec_keys)


def run(run_dir, extra_inventory=None, repo_root=REPO_ROOT):
    raw = read_json("%s/phase1/raw_hits.json" % run_dir)
    index = inv.build_index(repo_root)
    pending = read_json(extra_inventory) if extra_inventory and os.path.exists(extra_inventory) else \
        {"arxiv": {}, "openreview": {}, "doi": {}, "github": {}, "title_norm": {}}

    # ---- cross-source merge ----
    clusters = []  # list of {keys:set, records:[...], matched_profiles:set}
    for rec in raw:
        rk = _ids(rec)
        placed = False
        for c in clusters:
            if _merge_key(c["keys"], rk):
                c["keys"] |= rk
                c["records"].append(rec)
                c["matched_profiles"] |= set(rec.get("matched_profiles", []))
                placed = True
                break
        if not placed:
            clusters.append({"keys": set(rk), "records": [rec],
                             "matched_profiles": set(rec.get("matched_profiles", []))})

    candidates, duplicates, rejected = [], [], []
    for c in clusters:
        recs = c["records"]
        # choose a primary record: prefer arxiv > openreview > github
        order = {"arxiv": 0, "openreview": 1, "github": 2}
        recs_sorted = sorted(recs, key=lambda r: order.get(r["source"], 9))
        primary = recs_sorted[0]

        _PRIO = {"arxiv": 0, "openreview": 1, "doi": 2, "github": 3, "title_norm": 4}

        def _hit(ix):
            for kind, val in sorted(c["keys"], key=lambda kv: _PRIO.get(kv[0], 9)):
                if val in ix.get(kind, {}):
                    return {"kind": kind, "value": val, "slug": ix[kind][val]}
            return None

        dup = _hit(index)
        if dup:
            duplicates.append({"title": primary["title"], "match": dup,
                               "sources": [r["source"] for r in recs]})
            continue
        if _hit(pending):
            duplicates.append({"title": primary["title"], "match": {"kind": "pending-pr"},
                               "sources": [r["source"] for r in recs]})
            continue

        text = "%s %s" % (primary.get("title", ""), primary.get("abstract_or_description", ""))
        if not _RELEVANT.search(text):
            rejected.append({"title": primary["title"], "reason": "no in-scope token in metadata",
                             "sources": [r["source"] for r in recs]})
            continue

        cand_id = None
        for kind in ("arxiv", "openreview", "github"):
            for k, v in c["keys"]:
                if k == kind:
                    cand_id = v.replace("/", "_")
                    break
            if cand_id:
                break
        if not cand_id:
            cand_id = re.sub(r"[^a-z0-9]+", "-", normalize_title(primary["title"]))[:60]

        candidates.append({
            "candidate_id": cand_id,
            "title": primary["title"],
            "authors": primary.get("authors", []),
            "abstract_or_description": primary.get("abstract_or_description", ""),
            "source_records": [{"source": r["source"], "id": r["id"], "url": r["url"],
                                "date": r.get("date", "")} for r in recs_sorted],
            "matched_profiles": sorted(c["matched_profiles"]),
            "discovered_at": primary.get("discovered_at", ""),
        })

    candidates.sort(key=lambda x: x["candidate_id"])
    write_json("%s/phase1/candidates.json" % run_dir, candidates)
    write_json("%s/phase1/duplicate_matches.json" % run_dir, duplicates)
    write_json("%s/phase1/rejected.json" % run_dir, rejected)
    log("dedup: raw=%d clusters=%d candidates=%d duplicates=%d rejected=%d"
        % (len(raw), len(clusters), len(candidates), len(duplicates), len(rejected)))
    return {"raw": len(raw), "candidates": len(candidates),
            "duplicates": len(duplicates), "rejected": len(rejected)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--pending-index", default=None)
    ap.add_argument("--repo-root", default=REPO_ROOT)
    a = ap.parse_args()
    run(a.run_dir, a.pending_index, a.repo_root)
