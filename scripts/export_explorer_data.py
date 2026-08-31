#!/usr/bin/env python3
"""Export repository Markdown into a JSON dataset for the static explorer.

Markdown files remain the only ground truth. The explorer is a render layer
generated from cards, topic/domain/activity indexes, and monthly reports.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "works"
ZH_WORKS = ROOT / "zh" / "works"
TOPICS = ROOT / "topics"
DOMAINS = ROOT / "domains"
ACTIVITIES = ROOT / "activities"
MONTHLY = ROOT / "monthly"
DOCUMENT_FOLDERS = ("topics", "domains", "activities", "monthly", "works")

SECTION_RE = re.compile(r"^##\s+(.+?)\s*\n(.*?)(?=^##\s|\Z)", re.M | re.S)
TITLE_RE = re.compile(r"^#\s+(.+?)\s+\((\d{4})\)\s*$", re.M)
STAMP_RE = re.compile(
    r"^> \*\*First appeared:\*\* (\d{4}-\d{2}-\d{2}) · "
    r"\*\*Source:\*\* \[([^]]+)\]\((https?://[^)]+)\)$",
    re.M,
)
AXIS_LINK_RE = re.compile(r"\[([^]]+)\]\(\.\./([a-z_]+)/([^)]+)\.md\)")
MONTHLY_COVERAGE_RE = re.compile(r"^> \*\*Coverage:\*\* (.+)$", re.M)
MONTHLY_ROW_RE = re.compile(r"^\|\s*\[([^]]+)\]\(\.\./works/([a-z0-9-]+)\.md\)\s*\|", re.M)
LINK_LINE_RE = re.compile(r"^- \*\*([^*]+):\*\*\s*(.+?)\s*$", re.M)
URL_RE = re.compile(r"https?://[^\s>)]+")
DOMAIN_WORK_RE = re.compile(r"\((?:\.\./)?\.\./works/([a-z0-9-]+)\.md\)")
ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)
OPENREVIEW_ID_RE = re.compile(r"openreview\.net/forum\?id=([A-Za-z0-9_-]+)", re.I)
HF_ID_RE = re.compile(r"huggingface\.co/(?:papers|datasets|spaces)/([^)\s>/]+(?:/[^)\s>/]+)?)", re.I)
GITHUB_REPO_RE = re.compile(r"github\.com/([^)\s>]+/[^)\s>/]+)", re.I)


def _document_url(source_path: str, language: str = "en") -> str:
    path = Path(source_path)
    if path.suffix != ".md":
        raise ValueError(f"Document source must be Markdown: {source_path}")
    return f"./documents/{language}/{path.with_suffix('.json').as_posix()}"


def _document_links(source_path: str) -> dict[str, str]:
    return {
        "url": _document_url(source_path, "en"),
        "zh_url": _document_url(source_path, "zh"),
    }


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _sections(text: str) -> dict[str, str]:
    return {heading.strip(): body.strip() for heading, body in SECTION_RE.findall(text)}


def _first_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text.strip()):
        plain = block.strip()
        if plain and not plain.startswith(("|", "-", ">")):
            return " ".join(line.strip() for line in plain.splitlines())
    return ""


def _links(block: str) -> list[dict[str, str]]:
    out = []
    for label, raw in LINK_LINE_RE.findall(block):
        url_match = URL_RE.search(raw)
        if url_match:
            out.append({"label": label.strip(), "url": url_match.group(0)})
    return out


def _monthly_first_appearance_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(MONTHLY.glob("????-??.md")):
        month = path.stem
        text = _read(path)
        for _, slug in MONTHLY_ROW_RE.findall(text):
            mapping.setdefault(slug, f"{month}-01")
    return mapping


def _infer_first_appeared(path: Path, text: str, sections: dict[str, str], monthly_map: dict[str, str]) -> tuple[str, dict[str, str]]:
    stamp_match = STAMP_RE.search(text)
    if stamp_match:
        return stamp_match.group(1), {
            "label": stamp_match.group(2),
            "url": stamp_match.group(3),
        }

    links_block = sections.get("Links", "")
    arxiv_match = ARXIV_ID_RE.search(links_block) or ARXIV_ID_RE.search(text)
    if arxiv_match:
        arxiv_id = arxiv_match.group(1)
        yy = int(arxiv_id[:2])
        year = 2000 + yy
        month = arxiv_id[2:4]
        return f"{year:04d}-{month}-01", {
            "label": "arXiv (month inferred from identifier)",
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        }

    openreview_match = OPENREVIEW_ID_RE.search(links_block)
    if openreview_match:
        forum_id = openreview_match.group(1)
        fallback = monthly_map.get(path.stem, f"{TITLE_RE.search(text).group(2)}-01-01")
        return fallback, {
            "label": "OpenReview (date inferred from repository chronology)",
            "url": f"https://openreview.net/forum?id={forum_id}",
        }

    github_match = GITHUB_REPO_RE.search(links_block)
    if github_match:
        repo = github_match.group(1)
        fallback = monthly_map.get(path.stem, f"{TITLE_RE.search(text).group(2)}-01-01")
        return fallback, {
            "label": "GitHub (date inferred from repository chronology)",
            "url": f"https://github.com/{repo}",
        }

    hf_match = HF_ID_RE.search(links_block)
    if hf_match:
        target = hf_match.group(1)
        fallback = monthly_map.get(path.stem, f"{TITLE_RE.search(text).group(2)}-01-01")
        return fallback, {
            "label": "Hugging Face (date inferred from repository chronology)",
            "url": f"https://huggingface.co/{target}",
        }

    fallback = monthly_map.get(path.stem)
    if fallback:
        return fallback, {
            "label": "Repository monthly archive (month fallback)",
            "url": _document_url(f"monthly/{fallback[:7]}.md"),
        }

    title_match = TITLE_RE.search(text)
    year = title_match.group(2) if title_match else "1900"
    return f"{year}-01-01", {
        "label": "Card year fallback",
        "url": _document_url(f"works/{path.name}"),
    }


def _localized_axis_title(folder: str, slug: str, fallback: str) -> str:
    path = ROOT / "zh" / folder / f"{slug}.md"
    if not path.exists():
        return fallback
    match = re.search(r"^#\s+(.+?)\s*$", _read(path), re.M)
    return match.group(1).strip() if match else fallback


def _axis(block: str) -> list[dict[str, str]]:
    out = []
    for name, folder, slug in AXIS_LINK_RE.findall(block):
        out.append({
            "name": name,
            "zh_name": _localized_axis_title(folder, slug, name),
            "slug": slug,
            **_document_links(f"{folder}/{slug}.md"),
        })
    return out


def _card(path: Path, monthly_map: dict[str, str]) -> dict:
    text = _read(path)
    zh_path = ZH_WORKS / path.name
    zh_text = _read(zh_path) if zh_path.exists() else ""
    sections = _sections(text)
    zh_sections = _sections(zh_text) if zh_text else {}
    title_match = TITLE_RE.search(text)
    if not title_match:
        raise ValueError(f"Missing title in {path}")
    title, year = title_match.groups()
    first_appeared, source = _infer_first_appeared(path, text, sections, monthly_map)
    return {
        "slug": path.stem,
        "title": title,
        "year": int(year),
        "card_url": _document_url(f"works/{path.name}"),
        "zh_card_url": _document_url(f"works/{path.name}", "zh"),
        "first_appeared": first_appeared,
        "first_appeared_source": source,
        "overview": sections.get("Overview", ""),
        "summary": sections.get("Summary", ""),
        "domains_text": sections.get("Domains", ""),
        "topics": _axis(sections.get("Topics", "")),
        "activities": _axis(sections.get("Activities", "")),
        "links": _links(sections.get("Links", "")),
        "zh": {
            "overview": zh_sections.get("Overview", ""),
            "summary": zh_sections.get("Summary", ""),
        },
    }


def _index_pages(directory: Path) -> list[dict[str, str | int]]:
    items = []
    for path in sorted(directory.glob("*.md")):
        if path.name == "README.md":
            continue
        text = _read(path)
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        title = title_match.group(1).strip() if title_match else path.stem.replace("_", " ").title()
        related = len(re.findall(r"\((?:\.\./)?\.\./works/[a-z0-9-]+\.md\)", text))
        items.append({
            "name": title,
            "slug": path.stem,
            **_document_links(f"{directory.name}/{path.name}"),
            "count": related,
        })
    return items


def _domain_membership() -> dict[str, list[dict[str, str]]]:
    by_work: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(DOMAINS.glob("*.md")):
        if path.name == "README.md":
            continue
        text = _read(path)
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        domain_name = title_match.group(1).strip() if title_match else path.stem.replace("_", " ").title()
        zh_domain_name = _localized_axis_title("domains", path.stem, domain_name)
        for slug in sorted(set(DOMAIN_WORK_RE.findall(text))):
            by_work[slug].append({
                "name": domain_name,
                "zh_name": zh_domain_name,
                "slug": path.stem,
                **_document_links(f"domains/{path.name}"),
            })
    return dict(by_work)


def _monthly_reports() -> list[dict]:
    reports = []
    for path in sorted(MONTHLY.glob("????-??.md")):
        text = _read(path)
        zh_path = ROOT / "zh" / "monthly" / path.name
        zh_text = _read(zh_path) if zh_path.exists() else ""
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
        sections = _sections(text)
        zh_title_match = re.search(r"^#\s+(.+?)\s*$", zh_text, re.M) if zh_text else None
        zh_sections = _sections(zh_text) if zh_text else {}
        coverage_match = MONTHLY_COVERAGE_RE.search(text)
        reports.append({
            "month": path.stem,
            "title": title_match.group(1).strip() if title_match else path.stem,
            "zh_title": zh_title_match.group(1).strip() if zh_title_match else path.stem,
            **_document_links(f"monthly/{path.name}"),
            "coverage": coverage_match.group(1).strip() if coverage_match else "",
            "summary": _first_paragraph(sections.get("Month at a Glance", "")),
            "zh_summary": _first_paragraph(zh_sections.get("本月概览", "")),
            "works_count": len(MONTHLY_ROW_RE.findall(text)),
        })
    reports.sort(key=lambda item: item["month"], reverse=True)
    return reports


def build_dataset(root: Path = ROOT) -> dict:
    _ = root
    cards = []
    domain_map = _domain_membership()
    monthly_map = _monthly_first_appearance_map()
    for path in sorted(WORKS.glob("*.md")):
        if path.name == "README.md":
            continue
        card = _card(path, monthly_map)
        card["domains"] = domain_map.get(card["slug"], [])
        card["first_appeared_month"] = card["first_appeared"][:7]
        cards.append(card)

    topic_counts = Counter()
    activity_counts = Counter()
    domain_counts = Counter()
    monthly_counts = Counter()
    for card in cards:
        for topic in card["topics"]:
            topic_counts[(topic["slug"], topic["name"], topic["url"])] += 1
        for activity in card["activities"]:
            activity_counts[(activity["slug"], activity["name"], activity["url"])] += 1
        for domain in card["domains"]:
            domain_counts[(domain["slug"], domain["name"], domain["url"])] += 1
        monthly_counts[card["first_appeared_month"]] += 1

    topics = sorted(
        ({"slug": slug, "name": name, "zh_name": _localized_axis_title("topics", slug, name),
          "url": url, "zh_url": _document_url(f"topics/{slug}.md", "zh"), "count": count}
         for (slug, name, url), count in topic_counts.items()),
        key=lambda item: (-item["count"], item["name"]),
    )
    activities = sorted(
        ({"slug": slug, "name": name, "zh_name": _localized_axis_title("activities", slug, name),
          "url": url, "zh_url": _document_url(f"activities/{slug}.md", "zh"), "count": count}
         for (slug, name, url), count in activity_counts.items()),
        key=lambda item: (-item["count"], item["name"]),
    )
    domains = sorted(
        ({"slug": slug, "name": name, "zh_name": _localized_axis_title("domains", slug, name),
          "url": url, "zh_url": _document_url(f"domains/{slug}.md", "zh"), "count": count}
         for (slug, name, url), count in domain_counts.items()),
        key=lambda item: (-item["count"], item["name"]),
    )

    timeline = [
        {"month": month, "count": count}
        for month, count in sorted(monthly_counts.items())
    ]
    monthly_reports = _monthly_reports()
    latest = max((card["first_appeared"] for card in cards), default=None)
    earliest = min((card["first_appeared"] for card in cards), default=None)
    works_by_first_appeared = sorted(cards, key=lambda item: item["title"].casefold())
    works_by_first_appeared.sort(key=lambda item: item["first_appeared"], reverse=True)

    documents = {}
    source_paths = ["README.md"]
    for folder in DOCUMENT_FOLDERS:
        source_paths.extend(
            f"{folder}/{path.name}"
            for path in sorted((ROOT / folder).glob("*.md"))
        )
    for source_path in source_paths:
        documents[source_path] = _document_links(source_path)

    return {
        "ground_truth": {
            "markdown": True,
            "note": "This dataset is generated from repository Markdown. The explorer is a render layer only.",
        },
        "stats": {
            "works": len(cards),
            "topics": len(list(TOPICS.glob("*.md"))) - 1,
            "domains": len(list(DOMAINS.glob("*.md"))) - 1,
            "activities": len(list(ACTIVITIES.glob("*.md"))) - 1,
            "monthly_reports": len(monthly_reports),
            "first_appeared_earliest": earliest,
            "first_appeared_latest": latest,
        },
        "topics": topics,
        "domains": domains,
        "activities": activities,
        "monthly_reports": monthly_reports,
        "timeline": timeline,
        "documents": documents,
        "works": works_by_first_appeared,
    }


def write_dataset(data: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_documents(output_dir: Path, root: Path = ROOT) -> None:
    """Wrap every rendered Markdown document in JSON for self-contained hosting."""
    source_paths = ["README.md"]
    for folder in DOCUMENT_FOLDERS:
        source_paths.extend(
            f"{folder}/{path.name}"
            for path in sorted((root / folder).glob("*.md"))
        )

    for source_path in source_paths:
        for language in ("en", "zh"):
            input_path = root / source_path if language == "en" else root / "zh" / source_path
            if not input_path.exists():
                raise FileNotFoundError(f"Missing {language} document mirror: {input_path}")
            document_url = _document_url(source_path, language)
            output_path = output_dir / (document_url[2:] if document_url.startswith("./") else document_url)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "language": language,
                "source_path": source_path,
                "markdown": _read(input_path),
            }
            output_path.write_text(
                json.dumps(payload, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="site/data/index.json")
    parser.add_argument(
        "--documents-output",
        default="site",
        help="Site root where self-contained document JSON files are written.",
    )
    args = parser.parse_args()
    write_dataset(build_dataset(ROOT), ROOT / args.output)
    write_documents(ROOT / args.documents_output, ROOT)


if __name__ == "__main__":
    main()
