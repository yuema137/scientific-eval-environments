#!/usr/bin/env python3
"""Backfill auditable first-appearance stamps and chronological work indexes."""
import argparse
import datetime as dt
import glob
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ATOM = {"a": "http://www.w3.org/2005/Atom"}
STAMP_EN = re.compile(r"^> \*\*First appeared:\*\* .*?$", re.M)
STAMP_ZH = re.compile(r"^> \*\*首次公开：\*\* .*?$", re.M)


def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "scientific-eval-environments/1.0"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.load(r)


def _normal_date(value):
    if not value:
        return None
    m = re.search(r"(20\d{2}|19\d{2})[-/](\d{1,2})[-/](\d{1,2})", str(value))
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None
    return None


def _doi_date(doi):
    try:
        msg = _get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""))["message"]
    except Exception:
        return None
    dates = []
    for key in ("published-online", "published-print", "published", "issued"):
        parts = ((msg.get(key) or {}).get("date-parts") or [])
        if parts and len(parts[0]) >= 3:
            try:
                dates.append(dt.date(*parts[0][:3]).isoformat())
            except ValueError:
                pass
    return min(dates) if dates else None


def _official_page_date(url):
    if url.lower().endswith(".pdf"):
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as r:
            html = r.read(1500000).decode("utf-8", "ignore")
    except Exception:
        return None
    patterns = (
        r'<meta[^>]+(?:name|property)=["\'](?:citation_publication_date|article:published_time|'
        r'DC\.date|date)["\'][^>]+content=["\']([^"\']+)',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:name|property)=["\']'
        r'(?:citation_publication_date|article:published_time|DC\.date|date)["\']',
        r'"datePublished"\s*:\s*"([^"]+)"',
    )
    dates = [_normal_date(v) for p in patterns for v in re.findall(p, html, re.I)]
    dates = [d for d in dates if d]
    return min(dates) if dates else None


def _github_date(repo):
    try:
        data = _get_json("https://api.github.com/repos/%s" % repo)
    except Exception:
        return None
    return _normal_date(data.get("created_at"))


def _arxiv_dates(cards):
    ids = sorted({aid for c in cards for aid in c["arxiv_ids"]})
    out = {}
    for start in range(0, len(ids), 75):
        batch = ids[start:start + 75]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "id_list": ",".join(batch), "start": 0, "max_results": len(batch)
        })
        with urllib.request.urlopen(url, timeout=90) as r:
            root = ET.fromstring(r.read())
        for entry in root.findall("a:entry", ATOM):
            raw = entry.findtext("a:id", default="", namespaces=ATOM)
            m = re.search(r"/(\d{4}\.\d{4,5})(?:v\d+)?$", raw)
            published = entry.findtext("a:published", default="", namespaces=ATOM)
            if m and published:
                out[m.group(1)] = published[:10]
        if start + 75 < len(ids):
            time.sleep(3)
    # The bulk endpoint occasionally omits an otherwise valid record. Recover
    # those records individually so an old paper cannot silently look new.
    for aid in set(ids) - set(out):
        try:
            url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": aid})
            with urllib.request.urlopen(url, timeout=90) as r:
                root = ET.fromstring(r.read())
            entry = root.find("a:entry", ATOM)
            published = entry.findtext("a:published", default="", namespaces=ATOM) if entry is not None else ""
            if published:
                out[aid] = published[:10]
        except Exception:
            pass
    return out


def _hf_date(paper_id):
    try:
        data = _get_json("https://huggingface.co/api/papers/%s" % paper_id)
    except Exception:
        return None
    for key in ("submittedAt", "publishedAt", "published_at", "date"):
        value = data.get(key)
        if value and re.match(r"^\d{4}-\d{2}-\d{2}", str(value)):
            return str(value)[:10]
    return None


def _openreview_date(forum_id):
    try:
        data = _get_json("https://api2.openreview.net/notes?forum=" +
                         urllib.parse.quote(forum_id))
    except Exception:
        return None
    millis = [n.get("cdate") or n.get("odate") for n in data.get("notes", [])]
    millis = [m for m in millis if isinstance(m, (int, float))]
    if not millis:
        return None
    return dt.datetime.fromtimestamp(min(millis) / 1000, dt.timezone.utc).date().isoformat()


def _repo_addition(path):
    result = subprocess.run([
        "git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", path
    ], cwd=ROOT, capture_output=True, text=True, check=True)
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("no addition commit for %s" % path)
    commit = subprocess.run([
        "git", "log", "--follow", "--diff-filter=A", "--format=%H", "--", path
    ], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()[-1]
    return lines[-1][:10], commit


def _links_block(text):
    match = re.search(r"^## Links\s*\n(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return match.group(1) if match else ""


def _cards():
    cards = []
    for path in sorted(glob.glob(os.path.join(ROOT, "works", "*.md"))):
        if os.path.basename(path) == "README.md":
            continue
        text = open(path).read()
        slug = os.path.basename(path)[:-3]
        zh_path = os.path.join(ROOT, "zh", "works", os.path.basename(path))
        zh_text = open(zh_path).read() if os.path.exists(zh_path) else ""
        existing = re.search(r"^> \*\*First appeared:\*\* (\d{4}-\d{2}-\d{2}) · "
                             r"\*\*Source:\*\* \[([^]]+)\]\((https?://[^)]+)\)$", text, re.M)
        existing_zh = re.search(r"^> \*\*首次公开：\*\* \d{4}-\d{2}-\d{2} · "
                                r"\*\*来源：\*\* \[([^]]+)\]\(https?://[^)]+\)$", zh_text, re.M)
        title = re.search(r"^#\s+(.+?)(?:\s+\(\d{4}\))?\s*$", text, re.M).group(1)
        cards.append({
            "path": os.path.relpath(path, ROOT), "slug": slug, "title": title,
            "existing": ((existing.group(1), existing.group(2), existing.group(3),
                          existing_zh.group(1)) if existing and existing_zh and
                         existing.group(2) != "Repository addition" else None),
            "arxiv_ids": sorted(set(re.findall(
                r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", text, re.I))),
            "hf_ids": sorted(set(re.findall(r"huggingface\.co/papers/([\w.\-]+)", text, re.I))),
            "openreview_ids": sorted(set(re.findall(
                r"openreview\.net/forum\?id=([\w\-]+)", text, re.I))),
            "dois": sorted(set(d.rstrip(".,;") for d in (
                re.findall(r"doi\.org/([^>\s]+)", text, re.I)
                + re.findall(r"(?<!doi\.org/)(10\.\d{4,9}/[^\s>)\]]+)", text, re.I)
            ))),
            "urls": sorted(set(re.findall(r"https?://[^\s>)\]]+", _links_block(text)))),
            "github_repos": sorted(set("%s/%s" % m for m in re.findall(
                r"github\.com/([^/\s>]+)/([^/\s>#)]+)", text, re.I)
                if "%s/%s" % m != "yuema137/scientific-eval-environments")),
        })
    return cards


def _choose(card, arxiv):
    candidates = []
    for aid in card["arxiv_ids"]:
        if aid in arxiv:
            candidates.append((arxiv[aid], "arXiv initial submission", "https://arxiv.org/abs/%s" % aid,
                               "arXiv 首次提交"))
    for paper_id in card["hf_ids"]:
        date = _hf_date(paper_id)
        if date:
            candidates.append((date, "Hugging Face submission", "https://huggingface.co/papers/%s" % paper_id,
                               "Hugging Face 首次提交"))
    for forum_id in card["openreview_ids"]:
        date = _openreview_date(forum_id)
        if date:
            candidates.append((date, "OpenReview first public note",
                               "https://openreview.net/forum?id=%s" % forum_id,
                               "OpenReview 首次公开"))
    if candidates:
        return min(candidates, key=lambda x: (x[0], x[1]))
    # Preserve a reviewed public record that the structured resolvers do not
    # understand. A later run must not replace web research with a repository
    # date merely because the source uses an unfamiliar page format.
    if card["existing"]:
        return card["existing"]
    for doi in card["dois"]:
        date = _doi_date(doi)
        if date:
            candidates.append((date, "Official publication record", "https://doi.org/%s" % doi,
                               "官方出版记录"))
    for url in card["urls"]:
        if "github.com/" in url or "doi.org/" in url:
            continue
        date = _official_page_date(url)
        if date:
            candidates.append((date, "Official publication page", url, "官方发布页"))
    if candidates:
        return min(candidates, key=lambda x: (x[0], x[1]))
    for repo in card["github_repos"]:
        date = _github_date(repo)
        if date:
            url = "https://github.com/%s" % repo
            candidates.append((date, "Official repository creation", url, "官方代码库创建"))
    if candidates:
        return min(candidates, key=lambda x: (x[0], x[1]))
    date, commit = _repo_addition(card["path"])
    url = "https://github.com/yuema137/scientific-eval-environments/commit/%s" % commit
    return date, "Repository addition", url, "首次加入本仓库"


def _stamp(text, line, pattern):
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    switcher = re.search(r"^> .*?(?:English|简体中文).*?$", text, re.M)
    if not switcher:
        raise RuntimeError("missing language switcher")
    return text[:switcher.end()] + "\n\n" + line + text[switcher.end():]


def _index(records, zh=False):
    records = sorted(records, key=lambda r: (r["date"], r["title"].casefold()), reverse=True)
    if zh:
        head = ("# 按首次公开时间浏览 Works\n\n"
                "> [English](../WORKS_BY_DATE.md) | **简体中文**\n\n"
                "默认按 `First appeared` 从新到旧排列；同一天的工作按标题稳定排序。"
                "日期是这项工作最早可被公众访问的时间，与是否正式出版无关；只有无法核验公开日期时，才使用 card 首次加入本仓库的 Git 日期。\n\n"
                "| 首次公开 | Work | 来源 |\n|---|---|---|\n")
        rows = ["| {date} | [{title}](./{slug}.md) | [{label}]({url}) |".format(
            date=r["date"], title=r["title"], slug="works/" + r["slug"], label=r["zh_label"], url=r["url"])
                for r in records]
    else:
        head = ("# Works by First Appearance\n\n"
                "> **English** | [简体中文](./zh/WORKS_BY_DATE.md)\n\n"
                "Sorted by `First appeared`, newest first; titles provide a stable tie-breaker within a day. "
                "The date is the earliest verifiable day when the work itself became publicly accessible, "
                "regardless of formal publication. The card's first Git addition is used only when no public "
                "date can be verified.\n\n"
                "| First appeared | Work | Source |\n|---|---|---|\n")
        rows = ["| {date} | [{title}](./works/{slug}.md) | [{label}]({url}) |".format(**r)
                for r in records]
    return head + "\n".join(rows) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--index-only", action="store_true",
                    help="regenerate indexes from existing card stamps without network access")
    args = ap.parse_args()
    cards = _cards()
    arxiv = {} if args.index_only else _arxiv_dates(cards)
    records, changed = [], []
    for card in cards:
        en_path = os.path.join(ROOT, card["path"])
        zh_path = os.path.join(ROOT, "zh", card["path"])
        en = open(en_path).read()
        zh = open(zh_path).read()
        if args.index_only:
            em = re.search(r"^> \*\*First appeared:\*\* (\d{4}-\d{2}-\d{2}) · "
                           r"\*\*Source:\*\* \[([^]]+)\]\((https?://[^)]+)\)$", en, re.M)
            zm = re.search(r"^> \*\*首次公开：\*\* \d{4}-\d{2}-\d{2} · "
                           r"\*\*来源：\*\* \[([^]]+)\]\(https?://[^)]+\)$", zh, re.M)
            if not em or not zm:
                raise RuntimeError("missing first-appearance stamp for %s" % card["slug"])
            date, label, url, zh_label = em.group(1), em.group(2), em.group(3), zm.group(1)
        else:
            date, label, url, zh_label = _choose(card, arxiv)
        record = dict(card, date=date, label=label, url=url, zh_label=zh_label)
        records.append(record)
        if args.index_only:
            continue
        en_new = _stamp(en, "> **First appeared:** %s · **Source:** [%s](%s)" %
                        (date, label, url), STAMP_EN)
        zh_new = _stamp(zh, "> **首次公开：** %s · **来源：** [%s](%s)" %
                        (date, zh_label, url), STAMP_ZH)
        for path, old, new in ((en_path, en, en_new), (zh_path, zh, zh_new)):
            if old != new:
                changed.append(os.path.relpath(path, ROOT))
                if not args.check:
                    open(path, "w").write(new)
    indexes = ((os.path.join(ROOT, "WORKS_BY_DATE.md"), _index(records)),
               (os.path.join(ROOT, "zh", "WORKS_BY_DATE.md"), _index(records, zh=True)))
    for path, new in indexes:
        old = open(path).read() if os.path.exists(path) else ""
        if old != new:
            changed.append(os.path.relpath(path, ROOT))
            if not args.check:
                open(path, "w").write(new)
    if args.check and changed:
        print("out of date: " + ", ".join(changed[:20]))
        return 1
    action = "checked" if args.check else ("indexed" if args.index_only else "stamped")
    print("%s %d cards; %d file(s) changed" % (action, len(cards), len(changed)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
