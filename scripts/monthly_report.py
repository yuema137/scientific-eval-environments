#!/usr/bin/env python3
"""Prepare, generate, index, and validate bilingual monthly reports.

A report is keyed by the month in which cards first reached main. The cards'
First appeared stamps remain the authority for public-release chronology.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime" / "monthly-report"
AGENTS = ROOT / "automation" / "monthly_report" / "agents"
os.environ.setdefault("TZ", "America/Los_Angeles")
if hasattr(time, "tzset"):
    time.tzset()
STAMP = re.compile(
    r"^> \*\*First appeared:\*\* (\d{4}-\d{2}-\d{2}) · "
    r"\*\*Source:\*\* \[([^]]+)\]\((https?://[^)]+)\)$", re.M)


def _run(cmd, check=True):
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=check)


def _month(value=None):
    if value:
        if not re.fullmatch(r"\d{4}-(?:0[1-9]|1[0-2])", value):
            raise ValueError("month must be YYYY-MM")
        return value
    today = dt.datetime.now().date().replace(day=1)
    previous = today - dt.timedelta(days=1)
    return previous.strftime("%Y-%m")


def _section(text, heading):
    match = re.search(r"^##\s+" + re.escape(heading) + r"\s*\n(.*?)(?=^##\s|\Z)",
                      text, re.S | re.M)
    return match.group(1).strip() if match else ""


def _axis(text, heading, folder):
    block = _section(text, heading)
    out = []
    for label, slug in re.findall(r"\[([^]]+)\]\(\.\./%s/([^)]+)\.md\)" % folder, block):
        out.append({"name": label, "slug": slug, "url": "../%s/%s.md" % (folder, slug)})
    return out


def _main_additions(month):
    commits = _run(["git", "rev-list", "--first-parent", "HEAD"]).stdout.splitlines()
    paths = set()
    for commit in commits:
        raw_date = _run(["git", "show", "-s", "--format=%cI", commit]).stdout.strip()
        local_month = dt.datetime.fromisoformat(raw_date).astimezone().strftime("%Y-%m")
        if local_month != month:
            continue
        parent = _run(["git", "rev-parse", "%s^" % commit], check=False)
        if parent.returncode:
            continue
        changed = _run(["git", "diff", "--name-status", parent.stdout.strip(), commit]).stdout
        for line in changed.splitlines():
            parts = line.split("\t")
            if len(parts) == 2 and parts[0] == "A" and re.fullmatch(r"works/[^/]+\.md", parts[1]):
                if parts[1] != "works/README.md":
                    paths.add(parts[1])
    return sorted(paths)


def build_manifest(month, basis="main-addition"):
    works = []
    if basis == "first-appearance":
        paths = sorted(str(path.relative_to(ROOT)) for path in (ROOT / "works").glob("*.md")
                       if path.name != "README.md" and STAMP.search(path.read_text()) and
                       STAMP.search(path.read_text()).group(1)[:7] == month)
    else:
        paths = _main_additions(month)
    for rel in paths:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text()
        title_match = re.search(r"^#\s+(.+?)(?:\s+\(\d{4}\))?\s*$", text, re.M)
        stamp = STAMP.search(text)
        if not title_match or not stamp:
            raise RuntimeError("missing title or First appeared stamp: %s" % rel)
        first = stamp.group(1)
        works.append({
            "slug": path.stem,
            "title": title_match.group(1),
            "card_url": "../works/%s.md" % path.stem,
            "first_appeared": first,
            "first_appeared_source": {"label": stamp.group(2), "url": stamp.group(3)},
            "added_as": "New release" if first[:7] == month else "Backfill",
            "topics": _axis(text, "Topics", "topics"),
            "domains": _axis(text, "Domains", "domains"),
            "overview": _section(text, "Overview"),
            "summary": _section(text, "Summary"),
            "limitations": _section(text, "Limitations"),
        })
    manifest = {
        "month": month,
        "basis": basis,
        "month_label": dt.date(int(month[:4]), int(month[5:]), 1).strftime("%B %Y"),
        "works_count": len(works),
        "new_release_count": sum(w["added_as"] == "New release" for w in works),
        "backfill_count": sum(w["added_as"] == "Backfill" for w in works),
        "works": works,
    }
    RUNTIME.mkdir(parents=True, exist_ok=True)
    target = RUNTIME / (month + ".json")
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest, target


def _worker(agent, prompt, max_turns=35):
    system = (AGENTS / (agent + ".md")).read_text()
    cmd = [
        "claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns),
        "--permission-mode", "dontAsk", "--allowedTools", "Read,Write,Edit",
        "--model", os.environ.get("MONTHLY_REPORT_MODEL", "claude-opus-4-8"),
        "--append-system-prompt", system,
    ]
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=60 * 30)
    if proc.returncode:
        raise RuntimeError("%s failed: %s" % (agent, (proc.stderr or "")[-500:]))
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("%s returned invalid JSON" % agent) from exc
    if result.get("result") is None:
        raise RuntimeError("%s returned no result" % agent)


def _report_paths(month):
    return ROOT / "monthly" / (month + ".md"), ROOT / "zh" / "monthly" / (month + ".md")


def _update_indexes():
    months = sorted((p.stem for p in (ROOT / "monthly").glob("????-??.md")), reverse=True)
    en_rows = ["- [%s](./%s.md)" % (m, m) for m in months] or ["No monthly reports yet."]
    zh_rows = ["- [%s](./%s.md)" % (m, m) for m in months] or ["目前还没有月报。"]
    for path, rows in ((ROOT / "monthly" / "README.md", en_rows),
                       (ROOT / "zh" / "monthly" / "README.md", zh_rows)):
        text = path.read_text()
        text = re.sub(r"(?s)(<!-- MONTHLY_REPORTS_START -->).*?(<!-- MONTHLY_REPORTS_END -->)",
                      r"\1\n" + "\n".join(rows) + r"\n\2", text)
        path.write_text(text)


def generate(month, force=False, basis="main-addition", review=True):
    manifest, manifest_path = build_manifest(month, basis)
    if not manifest["works"]:
        raise RuntimeError("no cards first reached main during %s" % month)
    en, zh = _report_paths(month)
    if not force and (en.exists() or zh.exists()):
        raise RuntimeError("report already exists; pass --force to regenerate")
    prompt = ("Read %s and the referenced English cards. Write the canonical report to %s. "
              "The manifest is the complete inclusion list; do not add or omit works." %
              (manifest_path.relative_to(ROOT), en.relative_to(ROOT)))
    _worker("monthly-report-writer", prompt)
    if not en.exists():
        raise RuntimeError("English writer did not create %s" % en)
    prompt = ("Translate %s into %s. Read referenced cards only when needed to preserve technical "
              "meaning. Preserve every link target and complete-index row." %
              (en.relative_to(ROOT), zh.relative_to(ROOT)))
    _worker("monthly-report-translator", prompt)
    if not zh.exists():
        raise RuntimeError("translator did not create %s" % zh)
    if review:
        prompt = ("Review and revise %s in place. Use %s as the factual source. Preserve all links, "
                  "numbers, taxonomy membership, and complete-index rows." %
                  (zh.relative_to(ROOT), en.relative_to(ROOT)))
        _worker("monthly-report-chinese-reviewer", prompt, max_turns=8)
    # Relative links must move up one additional directory from zh/monthly/.
    zh_text = zh.read_text()
    for folder in ("works", "topics", "domains", "activities"):
        zh_text = zh_text.replace("](../%s/" % folder, "](../../%s/" % folder)
    zh.write_text(zh_text)
    _update_indexes()
    errors = validate(month, manifest)
    if errors:
        raise RuntimeError("monthly report validation failed:\n- " + "\n- ".join(errors))
    return en, zh


def bootstrap(start="2024-01", end=None, force=False, workers=4):
    end = end or _month()
    months = []
    year, number = map(int, start.split("-"))
    while "%04d-%02d" % (year, number) <= end:
        current = "%04d-%02d" % (year, number)
        manifest, _ = build_manifest(current, "first-appearance")
        if manifest["works"]:
            months.append(current)
        number += 1
        if number == 13:
            year, number = year + 1, 1

    def run_one(report_month):
        en, zh = _report_paths(report_month)
        if en.exists() and zh.exists():
            zh_text = zh.read_text()
            for folder in ("works", "topics", "domains", "activities"):
                zh_text = zh_text.replace("](../%s/" % folder, "](../../%s/" % folder)
            zh.write_text(zh_text)
            if not validate(report_month, build_manifest(report_month, "first-appearance")[0]):
                return report_month
        en.unlink(missing_ok=True) if hasattr(en, "unlink") else None
        zh.unlink(missing_ok=True) if hasattr(zh, "unlink") else None
        generate(report_month, force=True, basis="first-appearance", review=False)
        return report_month

    completed = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(run_one, report_month): report_month for report_month in months}
        for future in as_completed(futures):
            completed.append(future.result())
            print("bootstrapped %s (%d/%d)" %
                  (futures[future], len(completed), len(months)), flush=True)
    _update_indexes()
    return sorted(completed)


def _table_records(text, chinese=False):
    block = _section(text, "本月完整索引" if chinese else "Complete Monthly Index")
    prefix = r"\.\./\.\./works/" if chinese else r"\.\./works/"
    records = {}
    row_count = 0
    for line in block.splitlines():
        match = re.match(r"^\|\s*\[([^]]+)\]\(" + prefix +
                         r"([a-z0-9-]+)\.md\)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+)\|", line)
        if match:
            row_count += 1
            records[match.group(2)] = {"title": match.group(1), "date": match.group(3),
                                       "status": match.group(4).strip()}
    return records, row_count


def _broken_links(path, text):
    broken = []
    for target in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", text):
        if target.startswith(("http://", "https://")):
            continue
        if not (path.parent / target).resolve().exists():
            broken.append(target)
    return broken


def validate(month, manifest=None):
    en_path, zh_path = _report_paths(month)
    errors = []
    if not en_path.exists() or not zh_path.exists():
        return ["missing English or Chinese report for %s" % month]
    en, zh = en_path.read_text(), zh_path.read_text()
    if manifest is None:
        basis = "first-appearance" if "**Coverage:** First appearances" in en else "main-addition"
        manifest = build_manifest(month, basis)[0]
    required_en = ("Month at a Glance", "What Changed This Month", "Complete Monthly Index")
    required_zh = ("本月概览", "这个月到底变了什么", "本月完整索引")
    for heading in required_en:
        if not _section(en, heading):
            errors.append("English report missing non-empty %s" % heading)
    for heading in required_zh:
        if not _section(zh, heading):
            errors.append("Chinese report missing non-empty %s" % heading)
    expected = {w["slug"]: w for w in manifest["works"]}
    en_rows, en_count = _table_records(en)
    zh_rows, zh_count = _table_records(zh, chinese=True)
    for label, rows, row_count in (("English", en_rows, en_count),
                                   ("Chinese", zh_rows, zh_count)):
        if row_count != len(expected):
            errors.append("%s complete index must contain each manifest work exactly once; found %d rows for %d works" %
                          (label, row_count, len(expected)))
        if set(rows) != set(expected):
            errors.append("%s complete index differs from manifest: missing=%s extra=%s" %
                          (label, sorted(set(expected) - set(rows)), sorted(set(rows) - set(expected))))
            continue
        for slug, work in expected.items():
            if rows[slug]["date"] != work["first_appeared"]:
                errors.append("%s date mismatch for %s" % (label, slug))
            wanted = ("当月新发布" if work["added_as"] == "New release" else "历史补录") if label == "Chinese" else work["added_as"]
            if rows[slug]["status"] != wanted:
                errors.append("%s release/backfill mismatch for %s" % (label, slug))
    if set(en_rows) != set(zh_rows):
        errors.append("English and Chinese report work sets differ")
    if "——" in zh:
        errors.append("Chinese report contains a prohibited em dash")
    prohibited = ("老铁", "嘎嘎", "嘎哈")
    for word in prohibited:
        if word in zh:
            errors.append("Chinese report contains prohibited dialect performance: %s" % word)
    for path, text in ((en_path, en), (zh_path, zh)):
        broken = _broken_links(path, text)
        if broken:
            errors.append("%s has broken Markdown links: %s" % (path.relative_to(ROOT), broken))
    return errors


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "generate", "bootstrap", "validate", "validate-all", "index"):
        command = sub.add_parser(name)
        if name not in ("index", "validate-all", "bootstrap"):
            command.add_argument("--month")
            command.add_argument("--basis", choices=("main-addition", "first-appearance"),
                                 default="main-addition")
        if name == "generate":
            command.add_argument("--force", action="store_true")
        if name == "bootstrap":
            command.add_argument("--start", default="2024-01")
            command.add_argument("--end")
            command.add_argument("--workers", type=int, default=4)
            command.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if args.command == "index":
        _update_indexes()
        print("monthly indexes updated")
        return 0
    if args.command == "validate-all":
        months = sorted(p.stem for p in (ROOT / "monthly").glob("????-??.md"))
        all_errors = []
        for report_month in months:
            all_errors.extend("%s: %s" % (report_month, error)
                              for error in validate(report_month))
        if all_errors:
            print("monthly-report: FAIL\n" + "\n".join("- " + e for e in all_errors))
            return 1
        print("monthly-report: PASS (%d reports)" % len(months))
        return 0
    if args.command == "bootstrap":
        months = bootstrap(args.start, args.end, args.force, args.workers)
        print("bootstrapped %d monthly reports" % len(months))
        return 0
    month = _month(args.month)
    if args.command == "prepare":
        manifest, path = build_manifest(month, args.basis)
        print("prepared %s with %d works at %s" %
              (month, manifest["works_count"], path.relative_to(ROOT)))
        return 0
    if args.command == "generate":
        en, zh = generate(month, args.force, args.basis)
        print("generated %s and %s" % (en.relative_to(ROOT), zh.relative_to(ROOT)))
        return 0
    errors = validate(month)
    if errors:
        print("monthly-report: FAIL\n" + "\n".join("- " + e for e in errors))
        return 1
    print("monthly-report: PASS (%s)" % month)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as exc:
        print("monthly-report: ERROR: %s" % exc, file=sys.stderr)
        raise SystemExit(2)
