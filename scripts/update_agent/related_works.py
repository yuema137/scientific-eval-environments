"""Deterministic ordering for axis-page Related Works indexes."""

import glob
import os
import re


AXES = ("topics", "domains", "activities")
FIRST_APPEARED = re.compile(r"^>\s+\*\*First appeared:\*\*\s+(\d{4}-\d{2}-\d{2})\b", re.M)
TITLE = re.compile(r"^#\s+(.+?)(?:\s+\(\d{4}\))?\s*$", re.M)
RELATED_SECTION = re.compile(r"(^##\s+(?:Related Works|相关工作)\s*\n)(.*?)(?=^##\s|\Z)", re.S | re.M)
RELATED_LINK = re.compile(r"^- \[(.+?)\]\(\.\./works/([a-z0-9-]+)\.md\)(.*?)\s*$")


def card_order(repo_root):
    """Return slug -> (date, canonical title) from English work cards."""
    order = {}
    for path in glob.glob(os.path.join(repo_root, "works", "*.md")):
        if os.path.basename(path) == "README.md":
            continue
        text = open(path).read()
        date = FIRST_APPEARED.search(text)
        title = TITLE.search(text)
        if not date or not title:
            continue
        order[os.path.basename(path)[:-3]] = (date.group(1), title.group(1).strip())
    return order


def sorted_related_lines(body, order, page_path):
    lines = [line for line in body.splitlines() if line.strip()]
    if not lines:
        return []
    entries = []
    for line in lines:
        match = RELATED_LINK.match(line)
        if not match:
            raise ValueError("%s: Related Works must contain bare work-card links" % page_path)
        label, slug, suffix = match.groups()
        if slug not in order:
            raise ValueError("%s: no First appeared date for %s" % (page_path, slug))
        date, canonical_title = order[slug]
        entries.append((date, canonical_title.casefold(), label, slug, suffix))
    entries.sort(key=lambda item: item[1])
    entries.sort(key=lambda item: item[0], reverse=True)
    return ["- [%s](../works/%s.md)%s" % (label, slug, suffix)
            for _, _, label, slug, suffix in entries]


def expected_slug_order(slugs, order):
    expected = list(slugs)
    expected.sort(key=lambda slug: order[slug][1].casefold())
    expected.sort(key=lambda slug: order[slug][0], reverse=True)
    return expected


def sort_page(page_path, order, check=False):
    text = open(page_path).read()
    match = RELATED_SECTION.search(text)
    if not match:
        return False
    lines = sorted_related_lines(match.group(2), order, page_path)
    replacement = match.group(1).rstrip() + "\n\n" + "\n".join(lines) + ("\n" if lines else "")
    updated = text[:match.start()] + replacement + text[match.end():]
    if updated == text:
        return False
    if not check:
        open(page_path, "w").write(updated)
    return True


def sort_all(repo_root, check=False):
    order = card_order(repo_root)
    changed = []
    for prefix in ("", "zh"):
        for axis in AXES:
            folder = os.path.join(repo_root, prefix, axis) if prefix else os.path.join(repo_root, axis)
            for page_path in sorted(glob.glob(os.path.join(folder, "*.md"))):
                if os.path.basename(page_path) == "README.md":
                    continue
                if sort_page(page_path, order, check=check):
                    changed.append(os.path.relpath(page_path, repo_root))
    return changed
