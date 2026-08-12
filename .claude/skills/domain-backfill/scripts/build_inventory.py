#!/usr/bin/env python3
"""Phase-2 inventory builder for a domain backfill.

Merges the discovery agents' outputs, deduplicates candidates, checks each against
the existing card corpus, and partitions the survivors into deep-review batches.

Usage:
    python3 build_inventory.py <scratch_dir> [--repo PATH] [--batch-size 5]

Reads  <scratch_dir>/discovery_*.json   (JSON arrays of candidate records)
Writes <scratch_dir>/inventory_frozen.json
       <scratch_dir>/batch_NN.json
       <scratch_dir>/batch_manifest.json

Candidate records are free-form dicts; these keys are used when present:
    title, authors, year, source, url, repo_url_if_obvious,
    one_line_why_relevant, matched_query_family, note
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import OrderedDict, Counter

ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5})")
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def identity(rec):
    """Best available identity key: arXiv > DOI > repo URL > normalized title."""
    blob = " ".join(str(rec.get(k) or "") for k in ("url", "source", "note", "arxiv", "doi"))
    m = ARXIV_RE.search(blob)
    if m:
        return "ax:" + m.group(1)
    m = DOI_RE.search(blob)
    if m:
        return "doi:" + m.group(0).rstrip(".").lower()
    repo = rec.get("repo_url_if_obvious") or ""
    if "github.com/" in repo:
        return "gh:" + repo.split("github.com/", 1)[1].strip("/").lower()
    return "t:" + norm_title(rec.get("title"))


def existing_index(repo):
    """Identity fingerprints of every committed card, for repo-wide dedup."""
    ids, titles = set(), {}
    for p in glob.glob(os.path.join(repo, "works", "*.md")):
        slug = os.path.basename(p)[:-3]
        if slug == "README":
            continue
        txt = open(p, encoding="utf-8").read()
        for m in ARXIV_RE.finditer(txt):
            ids.add("ax:" + m.group(1))
        for m in DOI_RE.finditer(txt):
            ids.add("doi:" + m.group(0).rstrip(".").lower())
        head = txt.split("\n", 1)[0].lstrip("# ").strip()
        head = re.sub(r"\s*\(\d{4}\)\s*$", "", head)
        titles[norm_title(head)] = slug
        titles[norm_title(slug.replace("-", " "))] = slug
    return ids, titles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scratch")
    ap.add_argument("--repo", default="/home/yuema137/scientific-eval-environments")
    ap.add_argument("--batch-size", type=int, default=5)
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.scratch, "discovery_*.json")))
    if not files:
        print("no discovery_*.json in %s" % a.scratch)
        return 1

    merged = OrderedDict()
    per_file = {}
    for f in files:
        try:
            recs = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("  WARN unreadable %s: %s" % (os.path.basename(f), e))
            continue
        per_file[os.path.basename(f)] = len(recs)
        for r in recs:
            if not isinstance(r, dict) or not r.get("title"):
                continue
            k = identity(r)
            if k in merged:
                merged[k].setdefault("src", []).append(os.path.basename(f))
                # keep the richer record
                if len(str(r)) > len(str(merged[k].get("_rec"))):
                    merged[k]["_rec"] = r
            else:
                merged[k] = {"key": k, "_rec": r, "src": [os.path.basename(f)]}

    print("=== DISCOVERY INPUTS ===")
    for f, n in per_file.items():
        print("  %-28s %d" % (f, n))
    raw = sum(per_file.values())
    print("  raw records: %d  ->  unique candidates: %d" % (raw, len(merged)))

    ids, titles = existing_index(a.repo)
    inventory = []
    counts = Counter()
    for k, v in merged.items():
        r = v["_rec"]
        status = "NEW"
        match = None
        if k in ids:
            status, match = "ALREADY_INDEXED", "identity"
        else:
            nt = norm_title(r.get("title"))
            if nt in titles:
                status, match = "ALREADY_INDEXED", titles[nt]
        counts[status] += 1
        inventory.append({
            "key": k,
            "title": r.get("title"),
            "authors": r.get("authors"),
            "year": r.get("year"),
            "url": r.get("url"),
            "repo": r.get("repo_url_if_obvious"),
            "why": r.get("one_line_why_relevant"),
            "family": r.get("matched_query_family"),
            "note": r.get("note"),
            "src": sorted(set(v["src"])),
            "status": status,
            "existing_match": match,
        })

    print("\n=== REPO-WIDE DEDUP ===")
    for s, n in counts.most_common():
        print("  %-18s %d" % (s, n))
    for c in inventory:
        if c["status"] == "ALREADY_INDEXED":
            print("     already indexed: %s  (%s)" % (c["title"][:60], c["existing_match"]))

    todo = [c for c in inventory if c["status"] == "NEW"]
    batches = [todo[i:i + a.batch_size] for i in range(0, len(todo), a.batch_size)]
    manifest = []
    for i, b in enumerate(batches):
        p = os.path.join(a.scratch, "batch_%02d.json" % i)
        json.dump(b, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        manifest.append({"batch": i, "n": len(b), "file": p,
                         "titles": [c["title"][:60] for c in b]})

    json.dump(inventory, open(os.path.join(a.scratch, "inventory_frozen.json"), "w",
                              encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(manifest, open(os.path.join(a.scratch, "batch_manifest.json"), "w",
                             encoding="utf-8"), indent=1, ensure_ascii=False)

    print("\n=== BATCHES ===")
    print("  %d candidates -> %d batches of <=%d" % (len(todo), len(batches), a.batch_size))
    print("\nwrote inventory_frozen.json and %d batch files" % len(batches))
    return 0


if __name__ == "__main__":
    sys.exit(main())
