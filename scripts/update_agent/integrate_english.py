"""Phase 3 deterministic integration step.

The axis workers only DECIDE assignments (JSON) and write comparison-table rows / synthesis prose.
This step then wires the two-way reverse index **deterministically from the assignment JSON**:
  * card-side `## Topics` and `## Activities` link blocks (replacing the `TODO(axis)` placeholders);
  * the matching `## Related Works` entries on each topic / activity page;
  * domain-page `## Related Works` entries (one-way; cards are never modified for the domain axis).
Deriving both sides from the same source guarantees the reverse index agrees exactly, so the hard
English gate cannot be tripped by a worker editing one side but not the other. Then counts refresh.
"""
import argparse
import os
import re
import subprocess

from common import taxonomy, read_json, log, REPO_ROOT
from related_works import sort_all


def _display(repo_root):
    tax = taxonomy(repo_root)
    return {axis: {f: t for t, f in tax.get(axis, {}).items()} for axis in ("topics", "activities")}


def _card_title(repo_root, slug):
    p = os.path.join(repo_root, "works", "%s.md" % slug)
    if os.path.exists(p):
        m = re.search(r"^#\s+(.*?)(?:\s*\((\d{4})\))?\s*$", open(p).read(), re.M)
        if m:
            return m.group(1).strip()
    return slug


def _set_block(text, heading, body):
    pat = re.compile(r"(^##\s+" + re.escape(heading) + r"\s*\n).*?(?=^##\s)", re.S | re.M)
    return pat.subn(r"\g<1>\n" + body.rstrip() + "\n\n", text, count=1)[0]


def _ensure_related(page_path, slug, title):
    """Idempotently ensure `- [title](../works/slug.md)` appears once in the page's Related Works
    SECTION. The presence check is scoped to that section — a comparison-table Card link elsewhere
    on the page must NOT suppress the Related Works entry (that mismatch fails the axis gate)."""
    if not os.path.exists(page_path):
        return
    t = open(page_path).read()
    line = "- [%s](../works/%s.md)\n" % (title, slug)
    link_re = r"\]\(\.\./works/%s\.md\)" % re.escape(slug)
    m = re.search(r"(^##\s+Related Works\s*\n)(.*?)(?=^##\s|\Z)", t, re.S | re.M)
    if m:
        if re.search(link_re, m.group(2)):
            return  # already listed IN the Related Works section
        t = t[:m.start(2)] + line + m.group(2) + t[m.end(2):]
    else:
        t = t.rstrip() + "\n\n## Related Works\n\n" + line
    open(page_path, "w").write(t)


def run(run_dir, repo_root=REPO_ROOT):
    disp = _display(repo_root)
    topic_a = _load(run_dir, "topic_assignments.json")
    dom_a = _load(run_dir, "domain_assignments.json")
    act_a = _load(run_dir, "activity_assignments.json")
    tmap = {a["slug"]: a.get("topics", []) for a in topic_a.get("assignments", [])}
    amap = {a["slug"]: a for a in act_a.get("assignments", [])}
    dmap = {a["slug"]: a.get("domains", []) for a in dom_a.get("assignments", [])}

    slugs = set(tmap) | set(amap) | set(dmap)
    for slug in slugs:
        path = os.path.join(repo_root, "works", "%s.md" % slug)
        if not os.path.exists(path):
            log("  ! integrate: card missing %s" % slug)
            continue
        title = _card_title(repo_root, slug)
        txt = open(path).read()

        # card-side Topics block + topic-page Related Works
        topics = tmap.get(slug, [])
        if topics:
            tbody = "\n".join("- [%s](../topics/%s.md)" % (disp["topics"].get(f, f), f) for f in topics)
            txt = _set_block(txt, "Topics", tbody)
        for f in topics:
            _ensure_related(os.path.join(repo_root, "topics", "%s.md" % f), slug, title)
            _ensure_related(os.path.join(repo_root, "zh", "topics", "%s.md" % f), slug, title)

        # card-side Activities block (or N/A) + activity-page Related Works
        arec = amap.get(slug, {})
        acts = arec.get("activities", [])
        if acts:
            abody = "\n".join("- [%s](../activities/%s.md)" % (disp["activities"].get(f, f), f) for f in acts)
        else:
            abody = "N/A — %s" % (arec.get("na_reason")
                                  or "no scientific or research activity is directly evaluated.")
        txt = _set_block(txt, "Activities", abody)
        for f in acts:
            _ensure_related(os.path.join(repo_root, "activities", "%s.md" % f), slug, title)
            _ensure_related(os.path.join(repo_root, "zh", "activities", "%s.md" % f), slug, title)

        open(path, "w").write(txt)

        # domain pages: one-way — page Related Works only, never the card
        for f in dmap.get(slug, []):
            _ensure_related(os.path.join(repo_root, "domains", "%s.md" % f), slug, title)
            _ensure_related(os.path.join(repo_root, "zh", "domains", "%s.md" % f), slug, title)

        log("  integrated %s (topics=%d activities=%d domains=%d)"
            % (slug, len(topics), len(acts), len(dmap.get(slug, []))))

    counts = os.path.join(repo_root, "scripts", "update_counts.py")
    sort_all(repo_root)
    if os.path.exists(counts):
        subprocess.run(["python3", counts], cwd=repo_root, check=False)
    return sorted(slugs)


def _load(run_dir, name):
    p = "%s/phase3/%s" % (run_dir, name)
    return read_json(p) if os.path.exists(p) else {"assignments": []}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--repo-root", default=REPO_ROOT)
    a = ap.parse_args()
    print(run(a.run_dir, a.repo_root))
