"""Phase 3 deterministic integration step.

Applies the two-way card-side metadata from the axis assignment files (Topics + Activities)
onto the new work cards, replacing the `TODO(axis)` placeholders the card writer left. The
Domain mapping is one-way and is NOT written to cards. Then refreshes derived counts.

Running this as a single deterministic step (rather than letting parallel axis workers edit
cards) prevents races on shared card files.
"""
import argparse
import os
import re
import subprocess

from common import taxonomy, read_json, log, REPO_ROOT


def _display(repo_root):
    tax = taxonomy(repo_root)
    inv = {}
    for axis in ("topics", "activities"):
        inv[axis] = {f: t for t, f in tax.get(axis, {}).items()}
    return inv


def _set_block(text, heading, body):
    """Replace the body of `## heading` (everything up to the next `## `) with `body`."""
    pat = re.compile(r"(^##\s+" + re.escape(heading) + r"\s*\n).*?(?=^##\s)", re.S | re.M)
    repl = r"\g<1>\n" + body.rstrip() + "\n\n"
    new, n = pat.subn(repl, text, count=1)
    return new if n else text


def run(run_dir, repo_root=REPO_ROOT):
    disp = _display(repo_root)
    topic_a = _load(run_dir, "topic_assignments.json")
    act_a = _load(run_dir, "activity_assignments.json")
    tmap = {a["slug"]: a.get("topics", []) for a in topic_a.get("assignments", [])}
    amap = {a["slug"]: a for a in act_a.get("assignments", [])}

    slugs = set(tmap) | set(amap)
    for slug in slugs:
        path = os.path.join(repo_root, "works", "%s.md" % slug)
        if not os.path.exists(path):
            log("  ! integrate: card missing %s" % slug)
            continue
        txt = open(path).read()
        # Topics block
        tbody = "\n".join("- [%s](../topics/%s.md)" % (disp["topics"].get(f, f), f)
                          for f in tmap.get(slug, []))
        if tbody:
            txt = _set_block(txt, "Topics", tbody)
        # Activities block (or N/A)
        arec = amap.get(slug, {})
        acts = arec.get("activities", [])
        if acts:
            abody = "\n".join("- [%s](../activities/%s.md)" % (disp["activities"].get(f, f), f)
                              for f in acts)
        else:
            abody = "N/A — %s" % (arec.get("na_reason") or "no scientific or research activity is directly evaluated.")
        txt = _set_block(txt, "Activities", abody)
        open(path, "w").write(txt)
        log("  integrated card-side axes for %s (topics=%d activities=%d)"
            % (slug, len(tmap.get(slug, [])), len(acts)))

    # refresh derived counts deterministically
    counts = os.path.join(repo_root, "scripts", "update_counts.py")
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
