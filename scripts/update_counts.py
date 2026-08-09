#!/usr/bin/env python3
"""Derive every reader-facing count from the reverse indexes and rewrite the
index tables, so the counts can never drift from the cards.

Sources of truth (never hand-edit the derived numbers):
  * activity counts   <- each work card's `## Activities` block
  * topic counts      <- each work card's `## Topics` block
  * domain counts     <- each domain page's `## Related Works` list
  * card / page totals <- the files on disk

Usage:
  python scripts/update_counts.py           # rewrite counts in place
  python scripts/update_counts.py --check    # exit 1 if any count is stale (CI)

Run from the repository root.
"""
import re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def cards():
    return [p for p in glob.glob("works/*.md") if not p.endswith("README.md")]

def block(text, heading):
    m = re.search(r'^## ' + heading + r'\s*\n(.*?)(?=^## |\Z)', text, re.S | re.M)
    return m.group(1) if m else ""

def compute():
    counts = {}                     # key filename (no .md) -> count
    act = {}
    top = {}
    for p in cards():
        t = open(p).read()
        for slug in re.findall(r'\]\(\.\./activities/([a-z0-9_]+)\.md\)', block(t, "Activities")):
            act[slug] = act.get(slug, 0) + 1
        for f in re.findall(r'\]\(\.\./topics/([a-z0-9_]+)\.md\)', block(t, "Topics")):
            top[f] = top.get(f, 0) + 1
    dom = {}
    for p in glob.glob("domains/*.md"):
        if p.endswith("README.md"):
            continue
        key = os.path.basename(p)[:-3]
        rw = block(open(p).read(), "Related Works")
        dom[key] = len(re.findall(r'\]\(\.\./works/[a-z0-9\-]+\.md\)', rw))
    counts.update(act); counts.update(top); counts.update(dom)
    totals = {
        "cards": len(cards()),
        "topics": len(glob.glob("topics/*.md")) - 1,
        "domains": len(glob.glob("domains/*.md")) - 1,
        "activities": len(glob.glob("activities/*.md")) - 1,
        "memberships": sum(act.values()),
    }
    return counts, totals

def set_row_counts(text, counts):
    """Replace the trailing `| <int> |` of any table row whose row contains a
    markdown link to a known <key>.md, with counts[key]."""
    out = []
    for ln in text.split("\n"):
        if ln.startswith("| ") and re.search(r'\|\s*\d+\s*\|\s*$', ln):
            m = re.search(r'\]\((?:\.{1,2}/)?(?:[a-z_]+/)?([a-z0-9_\-]+)\.md\)', ln)
            if m and m.group(1) in counts:
                ln = re.sub(r'\|\s*\d+\s*\|(\s*)$', '| %d |\\1' % counts[m.group(1)], ln)
        out.append(ln)
    return "\n".join(out)

def apply_all(check):
    counts, T = compute()
    orig = {}   # path -> text as on disk
    work = {}   # path -> text after transforms applied so far

    def stage(path, fn):
        if path not in orig:
            orig[path] = work[path] = open(path).read()
        work[path] = fn(work[path])

    # 1. count tables (activities, domains, topics indexes; root READMEs)
    for path in ["activities/README.md", "zh/activities/README.md",
                 "domains/README.md", "zh/domains/README.md",
                 "topics/README.md", "zh/topics/README.md",
                 "README.md", "zh/README.md"]:
        stage(path, lambda s: set_row_counts(s, counts))

    # 2. membership totals on the activity indexes
    stage("activities/README.md",
          lambda s: re.sub(r'\b\d+ activity memberships', "%d activity memberships" % T["memberships"], s))
    stage("zh/activities/README.md",
          lambda s: re.sub(r'了\s*\d+\s*条活动归属', "了 %d 条活动归属" % T["memberships"], s))

    # 3. structural summary lines in the two root READMEs
    stage("README.md", lambda s: re.sub(
        r'\*\*\d+ work cards\*\*, \*\*\d+ topic pages\*\*, \*\*\d+ domain pages\*\*, and \*\*\d+ activity pages\*\*',
        "**%d work cards**, **%d topic pages**, **%d domain pages**, and **%d activity pages**"
        % (T["cards"], T["topics"], T["domains"], T["activities"]), s))
    stage("zh/README.md", lambda s: re.sub(
        r'\*\*\d+ 张卡片\*\*、\*\*\d+ 个 topic 页\*\*、\*\*\d+ 个 domain 页\*\*、\*\*\d+ 个 activity 页\*\*',
        "**%d 张卡片**、**%d 个 topic 页**、**%d 个 domain 页**、**%d 个 activity 页**"
        % (T["cards"], T["topics"], T["domains"], T["activities"]), s))

    edits = {p: work[p] for p in work if work[p] != orig[p]}
    if check:
        if edits:
            print("STALE counts in %d file(s):" % len(edits))
            for p in sorted(edits):
                print("  -", p)
            print("Run: python scripts/update_counts.py")
            return 1
        print("counts up to date")
        return 0
    for p, new in edits.items():
        open(p, "w").write(new)
    print("updated %d file(s)%s" % (len(edits), (": " + ", ".join(sorted(edits))) if edits else " (all already current)"))
    print("totals:", T)
    return 0

if __name__ == "__main__":
    sys.exit(apply_all("--check" in sys.argv))
