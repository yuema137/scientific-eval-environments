"""Deterministic validators and phase gates for the Daily Update Agent.

Every function operates on an explicit repo_root so the same checks run against the real
repository AND against an isolated fixture workspace. Each returns (ok: bool, errors: list[str]).
"""
import argparse
import glob
import os
import re
import sys

from common import taxonomy, search_profiles, read_json, REPO_ROOT

# Real template residue that must never survive into a finished card. Bare words like TBD/TBA are
# NOT banned outright: they appear in legitimate prose ("the preprint lists the venue as TBD"). Only
# an actual unfilled template token, OR a metadata field whose entire value is TBD/TBA, is a defect.
# Word boundaries are load-bearing on the bare-word tokens. Without them `FILL[_ ]?ME` matches
# case-insensitively INSIDE ordinary English: "Task Fu-fillme-nt" -> "fillme". That false positive
# failed a production run on 2026-08-19 that had produced 24 valid cards with zero worker failures,
# because one card named its evaluation dimension "Task Fulfillment".
PLACEHOLDER = re.compile(r"(TODO\(card\)|\bFIXME\b|lorem\s+ipsum|<\s*placeholder\s*>|"
                         r"\{\{\s*[A-Z][A-Z0-9_ ]*\s*\}\}|\bFILL[_ ]?ME\b)", re.I)
# a bold field label whose value is ONLY TBD/TBA (e.g. "**Venue:** TBD") -> an unfilled field.
PLACEHOLDER_FIELD = re.compile(r"\*\*[^*\n]+:\*\*\s*(TBD|TBA)\b[\s.)\]]*$", re.I | re.M)


def _has_placeholder(txt):
    return bool(PLACEHOLDER.search(txt) or PLACEHOLDER_FIELD.search(txt))


# ---------------------------------------------------------------- profiles
def validate_profiles(repo_root=REPO_ROOT):
    errs = []
    tax = taxonomy(repo_root)
    prof = search_profiles(repo_root)
    for axis in ("domains", "topics", "activities"):
        for item in tax.get(axis, {}):
            entry = (prof.get(axis) or {}).get(item)
            if not entry:
                errs.append("%s: taxonomy item '%s' has no search profile" % (axis, item))
    if not prof.get("global"):
        errs.append("global: no catch-all queries defined")
    return (not errs, errs)


# ---------------------------------------------------------------- discovery
def validate_discovery(run_dir, mandatory=("arxiv", "openreview", "github")):
    # `huggingface` is deliberately NOT mandatory. It is a supplementary community-curated feed
    # whose daily endpoint legitimately returns empty on weekends and holidays, and arXiv remains
    # the primary recency source — so a HuggingFace outage must not block a run that arXiv,
    # OpenReview and GitHub covered. Its per-source status is still recorded in coverage.json, and
    # the strict cross-source axis-completeness check below still applies to it.
    errs = []
    cov = read_json("%s/phase1/coverage.json" % run_dir)
    # A source may be `degraded_success` (reachable, mandatory coverage complete, only a supplemental
    # query — e.g. the broad global catch-all — failed transiently). That does not block discovery.
    # Only a real `failure` (source broadly unavailable / substantial mandatory failures) does.
    # `suspicious_empty` (a zero-storm that a canary could not resolve) does NOT fail discovery — the
    # run proceeds as an operationally-green (usually empty) no-op. Credibility is enforced separately:
    # coverage["discovery_credible"] is false, so the watermark is not advanced past the silent outage.
    ok_source = ("success", "degraded_success", "suspicious_empty")
    for s in mandatory:
        st = cov.get("sources", {}).get(s)
        if st not in ok_source:
            errs.append("source %s not success/degraded_success: %s" % (s, st))
    # Cross-source completeness stays STRICT: an axis item is covered if ANY source succeeded for it
    # (see discover.run). If some item lost coverage from every source, block the run regardless of
    # per-source health — this is what guarantees a degraded source never silently drops a taxonomy item.
    for axis, items in cov.get("axes", {}).items():
        for item, rec in items.items():
            if rec.get("status") != "success":
                errs.append("axis %s/%s coverage not success" % (axis, item))
    cands = read_json("%s/phase1/candidates.json" % run_dir)
    if not isinstance(cands, list):
        errs.append("candidates.json is not a list")
    else:
        for c in cands:
            for f in ("candidate_id", "title", "source_records"):
                if f not in c:
                    errs.append("candidate missing field %s: %r" % (f, c.get("candidate_id")))
    return (not errs, errs)


# ---------------------------------------------------------------- cards
def _template_headings(repo_root):
    txt = open(os.path.join(repo_root, "works", "README.md")).read()
    m = re.search(r"```markdown\n(.*?)```", txt, re.S)
    block = m.group(1) if m else ""
    return [h.strip() for h in re.findall(r"^##\s+(.*)$", block, re.M)]


def _section(txt, heading):
    m = re.search(r"^##\s+" + re.escape(heading) + r"\s*\n(.*?)(?=^##\s|\Z)", txt, re.S | re.M)
    return m.group(1) if m else None


def _first_appeared(txt, chinese=False):
    label = "首次公开" if chinese else "First appeared"
    pattern = (r"^>\s+\*\*" + re.escape(label) +
               r"(?:：|:)\*\*\s+(\d{4}-\d{2}-\d{2})\s+·\s+\*\*(?:来源|Source)(?:：|:)\*\*\s+"
               r"\[[^\]]+\]\((https?://[^)]+)\)\s*$")
    matches = re.findall(pattern, txt, re.M)
    return matches[0] if len(matches) == 1 else None


def validate_cards(repo_root, slugs):
    errs = []
    required = _template_headings(repo_root)
    for slug in slugs:
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
            errs.append("%s: filename not kebab-case" % slug)
        path = os.path.join(repo_root, "works", "%s.md" % slug)
        if not os.path.exists(path):
            errs.append("%s: card file missing" % slug)
            continue
        txt = open(path).read()
        for h in required:
            n = len(re.findall(r"^##\s+" + re.escape(h) + r"\s*$", txt, re.M))
            if n != 1:
                errs.append("%s: heading '## %s' appears %d times (want 1)" % (slug, h, n))
        if _has_placeholder(txt):
            errs.append("%s: contains a placeholder token" % slug)
        if not _first_appeared(txt):
            errs.append("%s: missing or invalid sourced First appeared stamp" % slug)
        links = _section(txt, "Links") or ""
        if not re.search(r"https?://", links):
            errs.append("%s: Links section has no URL" % slug)
        acts = _section(txt, "Activities") or ""
        if not acts.strip():
            errs.append("%s: empty Activities block" % slug)
    return (not errs, errs)


# ---------------------------------------------------------------- axes (reverse index)
def _card_axis_links(txt, axis):
    blk = _section(txt, "Topics" if axis == "topics" else "Activities") or ""
    return set(re.findall(r"\]\(\.\./%s/([a-z0-9_]+)\.md\)" % axis, blk))


def validate_axes(repo_root):
    errs = []
    tax = taxonomy(repo_root)
    valid = {a: set(tax.get(a, {}).values()) for a in ("topics", "activities", "domains")}
    cards = [p for p in glob.glob(os.path.join(repo_root, "works", "*.md"))
             if os.path.basename(p) != "README.md"]
    card_axis = {"topics": {}, "activities": {}}
    for p in cards:
        slug = os.path.basename(p)[:-3]
        txt = open(p).read()
        for axis in ("topics", "activities"):
            links = _card_axis_links(txt, axis)
            for f in links:
                if valid[axis] and f not in valid[axis]:
                    errs.append("%s: unknown %s label '%s'" % (slug, axis[:-1], f))
            card_axis[axis][slug] = links
    # two-way for topics & activities: page Related Works <-> card block
    for axis in ("topics", "activities"):
        if not valid[axis]:
            continue
        for page in valid[axis]:
            pp = os.path.join(repo_root, axis, "%s.md" % page)
            if not os.path.exists(pp):
                continue
            rw = _section(open(pp).read(), "Related Works") or ""
            page_slugs = re.findall(r"\]\(\.\./works/([a-z0-9\-]+)\.md\)", rw)
            if len(page_slugs) != len(set(page_slugs)):
                errs.append("%s/%s: duplicate Related Works entry" % (axis, page))
            page_set = set(page_slugs)
            for s in page_set:
                if not os.path.exists(os.path.join(repo_root, "works", "%s.md" % s)):
                    errs.append("%s/%s: Related Works -> missing card %s" % (axis, page, s))
                if page not in card_axis[axis].get(s, set()):
                    errs.append("%s/%s: lists %s but its card omits the label" % (axis, page, s))
            for slug, links in card_axis[axis].items():
                if page in links and slug not in page_set:
                    errs.append("%s: card lists %s/%s but page omits it" % (slug, axis, page))
    # domains: one-way; every domain-page Related Works link resolves
    for page in valid["domains"]:
        pp = os.path.join(repo_root, "domains", "%s.md" % page)
        rw = _section(open(pp).read(), "Related Works") or ""
        for s in re.findall(r"\]\(\.\./works/([a-z0-9\-]+)\.md\)", rw):
            if not os.path.exists(os.path.join(repo_root, "works", "%s.md" % s)):
                errs.append("domains/%s: Related Works -> missing card %s" % (page, s))
    return (not errs, errs)


# ---------------------------------------------------------------- bilingual
def validate_bilingual(repo_root, slugs):
    errs = []
    for slug in slugs:
        en = os.path.join(repo_root, "works", "%s.md" % slug)
        zh = os.path.join(repo_root, "zh", "works", "%s.md" % slug)
        if not os.path.exists(zh):
            errs.append("%s: missing Chinese mirror" % slug)
            continue
        et, zt = open(en).read(), open(zh).read()
        for axis in ("topics", "activities"):
            if _card_axis_links(et, axis) != _card_axis_links(zt, axis):
                errs.append("%s: %s membership differs en/zh" % (slug, axis))
        # language switcher present on both
        if "简体中文" not in et:
            errs.append("%s: en card missing zh switcher" % slug)
        if "English" not in zt:
            errs.append("%s: zh card missing en switcher" % slug)
        ed, zd = _first_appeared(et), _first_appeared(zt, chinese=True)
        if not ed or not zd:
            errs.append("%s: missing or invalid first-appearance stamp in en/zh" % slug)
        elif ed != zd:
            errs.append("%s: first-appearance date or provenance URL differs en/zh" % slug)
    return (not errs, errs)


# ---------------------------------------------------------------- topic explanations
def validate_topic_explanations(repo_root=REPO_ROOT):
    """Require a readable entry section on every canonical topic and its mirror."""
    errs = []
    tax = taxonomy(repo_root)
    for topic_file in tax.get("topics", {}).values():
        paths = (
            (os.path.join(repo_root, "topics", "%s.md" % topic_file), "Start Here"),
            (os.path.join(repo_root, "zh", "topics", "%s.md" % topic_file),
             "先看它解决什么问题"),
        )
        for path, heading in paths:
            rel = os.path.relpath(path, repo_root)
            if not os.path.exists(path):
                errs.append("%s: topic page missing" % rel)
                continue
            txt = open(path).read()
            n = len(re.findall(r"^##\s+" + re.escape(heading) + r"\s*$", txt, re.M))
            if n != 1:
                errs.append("%s: heading '## %s' appears %d times (want 1)" %
                            (rel, heading, n))
    return (not errs, errs)


# ---------------------------------------------------------------- first appearance
def validate_first_appearance(repo_root=REPO_ROOT):
    errs = []
    cards = [p for p in glob.glob(os.path.join(repo_root, "works", "*.md"))
             if os.path.basename(p) != "README.md"]
    for en in cards:
        slug = os.path.basename(en)[:-3]
        zh = os.path.join(repo_root, "zh", "works", "%s.md" % slug)
        if not os.path.exists(zh):
            errs.append("%s: missing Chinese mirror" % slug)
            continue
        ed = _first_appeared(open(en).read())
        zd = _first_appeared(open(zh).read(), chinese=True)
        if not ed or not zd:
            errs.append("%s: missing or invalid sourced first-appearance stamp" % slug)
        elif ed != zd:
            errs.append("%s: first-appearance date or provenance URL differs en/zh" % slug)
    return (not errs, errs)


# ---------------------------------------------------------------- CLI
def _report(name, ok, errs):
    print("%s: %s" % (name, "PASS" if ok else "FAIL"))
    for e in errs[:40]:
        print("  -", e)
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("check", choices=["profiles", "discovery", "cards", "axes", "bilingual",
                                      "topic-explanations", "first-appearance"])
    ap.add_argument("--repo-root", default=REPO_ROOT)
    ap.add_argument("--run-dir")
    ap.add_argument("--slugs", default="")
    a = ap.parse_args()
    slugs = [s for s in a.slugs.split(",") if s]
    if a.check == "profiles":
        ok, e = validate_profiles(a.repo_root)
    elif a.check == "discovery":
        ok, e = validate_discovery(a.run_dir)
    elif a.check == "cards":
        ok, e = validate_cards(a.repo_root, slugs)
    elif a.check == "axes":
        ok, e = validate_axes(a.repo_root)
    elif a.check == "bilingual":
        ok, e = validate_bilingual(a.repo_root, slugs)
    elif a.check == "topic-explanations":
        ok, e = validate_topic_explanations(a.repo_root)
    elif a.check == "first-appearance":
        ok, e = validate_first_appearance(a.repo_root)
    sys.exit(_report(a.check, ok, e))


if __name__ == "__main__":
    main()
