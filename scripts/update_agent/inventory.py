"""Build an identity index of works already in the repository, for deduplication.

Stable identifiers, in priority order: arXiv ID, OpenReview ID, DOI, canonical
GitHub repo URL, normalized title.
"""
import os
import re
import glob

from common import REPO_ROOT, normalize_title, normalize_arxiv_id


def _norm_github(url):
    m = re.search(r"github\.com/([^/\s>]+)/([^/\s>#)]+)", url, re.I)
    if not m:
        return None
    owner, repo = m.group(1), re.sub(r"\.git$", "", m.group(2))
    return "github.com/%s/%s" % (owner.lower(), repo.lower())


def card_identity(path):
    text = open(path).read()
    slug = os.path.basename(path)[:-3]
    h1 = re.search(r"^#\s+(.*?)(?:\s*\((\d{4})\))?\s*$", text, re.M)
    title = h1.group(1).strip() if h1 else slug
    ident = {
        "slug": slug,
        "title": title,
        "title_norm": normalize_title(title),
        "arxiv": sorted(set(normalize_arxiv_id(m) for m in
                            re.findall(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", text, re.I))),
        "openreview": sorted(set(re.findall(r"openreview\.net/forum\?id=([\w\-]+)", text, re.I))),
        "doi": sorted(set(m.lower() for m in re.findall(r"\b(10\.\d{4,9}/[^\s>)\]]+)", text))),
        "github": sorted(set(g for g in (_norm_github(u) for u in
                             re.findall(r"https?://github\.com/[^\s>)\]]+", text)) if g)),
    }
    return ident


def build_index(repo_root=REPO_ROOT):
    cards = [p for p in glob.glob(os.path.join(repo_root, "works", "*.md"))
             if os.path.basename(p) != "README.md"]
    records = [card_identity(p) for p in cards]
    idx = {"arxiv": {}, "openreview": {}, "doi": {}, "github": {}, "title_norm": {}, "records": records}
    for r in records:
        for k in ("arxiv", "openreview", "doi", "github"):
            for v in r[k]:
                idx[k].setdefault(v, r["slug"])
        idx["title_norm"].setdefault(r["title_norm"], r["slug"])
    return idx


if __name__ == "__main__":
    import json
    import sys
    idx = build_index()
    summary = {k: len(idx[k]) for k in ("arxiv", "openreview", "doi", "github", "title_norm")}
    summary["cards"] = len(idx["records"])
    json.dump(summary, sys.stdout, indent=2)
    print()
