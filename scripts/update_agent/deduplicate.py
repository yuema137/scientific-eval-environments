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


def _paper_ids_from_text(text):
    """Extract paper identifiers embedded in free text (e.g. a GitHub repo's description or
    homepage linking its arXiv paper) so the repo merges onto the paper candidate."""
    keys = set()
    for a in re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", text, re.I):
        keys.add(("arxiv", normalize_arxiv_id(a)))
    for a in re.findall(r"\barxiv[:\s]+(\d{4}\.\d{4,5})", text, re.I):
        keys.add(("arxiv", normalize_arxiv_id(a)))
    for o in re.findall(r"openreview\.net/forum\?id=([\w\-]+)", text, re.I):
        keys.add(("openreview", o))
    for d in re.findall(r"\b(10\.\d{4,9}/[^\s>)\]]+)", text):
        keys.add(("doi", d.lower()))
    return keys


def _ids(rec):
    """Return normalized identity keys for one raw record."""
    keys = set()
    if rec["source"] == "arxiv":
        a = normalize_arxiv_id(rec["id"])
        if a:
            keys.add(("arxiv", a))
    if rec["source"] == "openreview":
        keys.add(("openreview", rec["id"]))
    if rec["source"] == "huggingface":
        # HuggingFace daily-papers ids ARE arXiv ids, so the record merges with the arXiv record
        # for the same work rather than surfacing as a separate candidate.
        a = normalize_arxiv_id(rec["id"])
        if a:
            keys.add(("arxiv", a))
    if rec["source"] == "github":
        m = re.search(r"github\.com/([^/]+)/([^/#?]+)", rec["url"], re.I)
        if m:
            keys.add(("github", "github.com/%s/%s" % (m.group(1).lower(),
                     re.sub(r"\.git$", "", m.group(2).lower()))))
        # a repo that links its paper -> gains the paper's identifier keys
        keys |= _paper_ids_from_text(" ".join([rec.get("url", ""), rec.get("homepage", ""),
                                               rec.get("abstract_or_description", "")]))
    tn = normalize_title(rec["title"])
    if tn:
        keys.add(("title_norm", tn))
    return keys


def _merge_key(existing_keys, rec_keys):
    return bool(existing_keys & rec_keys)


def _author_lastnames(rec):
    out = set()
    for a in (rec.get("authors") or []):
        toks = re.sub(r"[^a-z\s]", "", str(a).lower()).split()
        if toks:
            out.add(toks[-1])
    return out


def _title_tokens(t):
    return set(w for w in re.sub(r"[^a-z0-9\s]", " ", (t or "").lower()).split() if len(w) > 2)


def _fuzzy_same_paper(a, b):
    """Cautious cross-record equivalence for PAPER records (arxiv/openreview): high title
    token-set overlap AND at least one shared author last name. Never merges on title alone."""
    _PAPERS = ("arxiv", "openreview", "huggingface")
    if a["source"] not in _PAPERS or b["source"] not in _PAPERS:
        return False
    ta, tb = _title_tokens(a.get("title")), _title_tokens(b.get("title"))
    if not ta or not tb:
        return False
    jac = len(ta & tb) / len(ta | tb)
    subtitle = ta <= tb or tb <= ta   # one title is a prefix/superset (subtitle difference)
    if jac < 0.85 and not subtitle:
        return False
    return bool(_author_lastnames(a) & _author_lastnames(b))


def run(run_dir, extra_inventory=None, repo_root=REPO_ROOT, raw_path=None):
    raw = read_json(raw_path or "%s/phase1/raw_hits.json" % run_dir)
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

    # second pass: cautious fuzzy merge of paper clusters (title+author), never title-only
    merged = True
    while merged:
        merged = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if any(_fuzzy_same_paper(ra, rb)
                       for ra in clusters[i]["records"] for rb in clusters[j]["records"]):
                    clusters[i]["keys"] |= clusters[j]["keys"]
                    clusters[i]["records"] += clusters[j]["records"]
                    clusters[i]["matched_profiles"] |= clusters[j]["matched_profiles"]
                    del clusters[j]
                    merged = True
                    break
            if merged:
                break

    candidates, duplicates, rejected = [], [], []
    for c in clusters:
        recs = c["records"]
        # choose a primary record: prefer arxiv > openreview > huggingface > github
        order = {"arxiv": 0, "openreview": 1, "huggingface": 2, "github": 3}
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
