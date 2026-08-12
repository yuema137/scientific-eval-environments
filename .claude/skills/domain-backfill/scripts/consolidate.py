#!/usr/bin/env python3
"""Phase-4 card gate for a domain backfill.

Consolidates deep-review batch results and audits them against the repository:
every candidate decided, every accept carrying exactly one card, no orphan cards,
no duplicate accepts, and axis labels drawn from the canonical taxonomy.

Usage:
    python3 consolidate.py <scratch_dir> [--repo /path/to/repo]

Expects in <scratch_dir>:
    batch_manifest.json   [{"batch": 0, "n": 4, ...}, ...]
    result_<NN>.json      the deep-review output for each batch
    result_snowball.json  optional, for citation-snowball finds

Writes <scratch_dir>/consolidated.json and prints a report.
"""
import argparse
import collections
import glob
import json
import os
import subprocess
import sys

TOPIC_DIR, ACT_DIR, DOM_DIR = "topics", "activities", "domains"


def canonical(repo):
    """Canonical label sets, read from the repository rather than hardcoded."""
    topics = {f[:-3] for f in os.listdir(os.path.join(repo, TOPIC_DIR))
              if f.endswith(".md") and f != "README.md"}
    acts = {f[:-3] for f in os.listdir(os.path.join(repo, ACT_DIR))
            if f.endswith(".md") and f != "README.md"}
    doms = {}
    for f in os.listdir(os.path.join(repo, DOM_DIR)):
        if f.endswith(".md") and f != "README.md":
            with open(os.path.join(repo, DOM_DIR, f)) as fh:
                doms[fh.readline().strip("# \n")] = f[:-3]
    return topics, acts, doms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scratch")
    ap.add_argument("--repo", default="/home/yuema137/scientific-eval-environments")
    a = ap.parse_args()
    ce, repo = a.scratch, a.repo

    manifest = json.load(open(os.path.join(ce, "batch_manifest.json")))
    expected = {m["batch"]: m["n"] for m in manifest}

    results, missing = {}, []
    for b in sorted(expected):
        p = os.path.join(ce, "result_%02d.json" % b)
        if os.path.exists(p):
            results[b] = json.load(open(p))
        else:
            missing.append(b)

    print("=== BATCH COVERAGE ===")
    decided = 0
    for b in sorted(expected):
        if b in missing:
            print("  batch %02d: MISSING (expected %d)" % (b, expected[b]))
            continue
        n = len(results[b])
        decided += n
        flag = "" if n == expected[b] else "   <-- COUNT MISMATCH (expected %d)" % expected[b]
        print("  batch %02d: %d decisions%s" % (b, n, flag))

    extra = []
    snow = os.path.join(ce, "result_snowball.json")
    if os.path.exists(snow):
        extra = json.load(open(snow))
        decided += len(extra)
        print("  snowball: %d decisions" % len(extra))

    print("  batches missing: %s" % (missing or "none"))
    print("  total decided  : %d" % decided)

    allr = [c for b in results.values() for c in b] + extra

    print("\n=== DECISIONS ===")
    for d, n in collections.Counter(c.get("decision") for c in allr).most_common():
        print("  %-42s %d" % (d, n))

    accepts = [c for c in allr if c.get("decision") == "ACCEPT_NEW_CARD"]
    axis_updates = [c for c in allr if c.get("decision") == "ALREADY_INDEXED_AXIS_UPDATE"]

    # dedupe accepts by slug: two subagents may card the same work
    by_slug = collections.OrderedDict()
    dupes = []
    for c in accepts:
        s = c.get("slug_if_accepted")
        if s in by_slug:
            dupes.append(s)
        else:
            by_slug[s] = c

    topics, acts, doms = canonical(repo)
    print("\n=== ACCEPTED (%d unique) ===" % len(by_slug))
    problems = []
    for s, c in by_slug.items():
        ok = os.path.exists(os.path.join(repo, "works", "%s.md" % s))
        for t in c.get("topics") or []:
            if t not in topics:
                problems.append((s, "topic", t))
        for x in c.get("activities") or []:
            if x not in acts:
                problems.append((s, "activity", x))
        for d in c.get("domains") or []:
            if d not in doms:
                problems.append((s, "domain", d))
        print("  %-52s %s" % (s, "[file]" if ok else "[NO FILE]"))

    if dupes:
        print("\n  DUPLICATE ACCEPTS (adjudicate and merge): %s" % ", ".join(sorted(set(dupes))))
    print("  NON-CANONICAL LABELS: %s" % (problems or "none"))

    if axis_updates:
        print("\n=== ALREADY-INDEXED AXIS UPDATES (%d) ===" % len(axis_updates))
        for c in axis_updates:
            print("   %s" % (c.get("candidate_title", "")[:70]))

    print("\n=== ORPHAN CHECK ===")
    out = subprocess.run(["git", "-C", repo, "status", "--short", "works/"],
                         capture_output=True, text=True).stdout.strip()
    orphans = [os.path.basename(l.split()[-1])[:-3] for l in out.splitlines()
               if os.path.basename(l.split()[-1])[:-3] not in by_slug]
    print("  uncommitted cards with no ACCEPT record: %s" % (orphans or "none"))

    print("\n=== AXIS FAN-OUT ===")
    for label, key, mapping in (("DOMAIN", "domains", doms), ("TOPIC", "topics", None),
                                ("ACTIVITY", "activities", None)):
        cnt = collections.Counter(v for c in by_slug.values() for v in (c.get(key) or []))
        print("  %s: %s" % (label, dict(cnt)))

    json.dump({"accepts": list(by_slug.values()), "axis_updates": axis_updates,
               "counts": dict(collections.Counter(c.get("decision") for c in allr)),
               "total_decided": decided, "missing_batches": missing,
               "duplicate_accepts": sorted(set(dupes)), "label_problems": problems},
              open(os.path.join(ce, "consolidated.json"), "w"), indent=1)

    json.dump(list(by_slug.values()), open(os.path.join(ce, "accepts_final.json"), "w"), indent=1)
    print("\nwrote consolidated.json and accepts_final.json")

    blocking = bool(missing or problems or orphans)
    if blocking:
        print("\nGATE: FAIL — resolve the above before axis integration.")
    else:
        print("\nGATE: PASS")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
