import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest


SPEC = importlib.util.spec_from_file_location(
    "monthly_report", Path(__file__).parents[1] / "scripts" / "monthly_report.py")
monthly = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(monthly)


def _git(root, *args, env=None):
    merged = os.environ.copy()
    if env:
        merged.update(env)
    subprocess.run(["git"] + list(args), cwd=root, env=merged, check=True,
                   capture_output=True, text=True)


def _fixture_repo(tmp_path, monkeypatch):
    root = tmp_path
    for folder in ("works", "zh/works", "topics", "domains", "monthly", "zh/monthly"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "fixture@example.com")
    _git(root, "config", "user.name", "Fixture")
    (root / "README.md").write_text("fixture\n")
    _git(root, "add", "README.md")
    base_env = {"GIT_AUTHOR_DATE": "2026-07-31T12:00:00-07:00",
                "GIT_COMMITTER_DATE": "2026-07-31T12:00:00-07:00"}
    _git(root, "commit", "-qm", "base", env=base_env)
    card = """# Fixture Work (2024)

> **English** | [简体中文](../zh/works/fixture-work.md)

> **First appeared:** 2024-02-03 · **Source:** [Official record](https://example.com/work)

## Overview
One concrete overview.

## Topics
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities
N/A — fixture.

## Summary
One concrete summary.

## Domains
- [Biology](../domains/biology.md)

## Limitations
One boundary.
"""
    (root / "works" / "fixture-work.md").write_text(card)
    (root / "zh" / "works" / "fixture-work.md").write_text("mirror\n")
    (root / "topics" / "planning_decision_evaluation.md").write_text("topic\n")
    (root / "domains" / "biology.md").write_text("domain\n")
    (root / "monthly" / "README.md").write_text(
        "# Monthly Reports\n\n<!-- MONTHLY_ARCHIVE_OVERVIEW_START -->\n<!-- MONTHLY_ARCHIVE_OVERVIEW_END -->\n\n"
        "<!-- MONTHLY_REPORTS_START -->\n<!-- MONTHLY_REPORTS_END -->\n"
    )
    (root / "zh" / "monthly" / "README.md").write_text(
        "# 月度报告\n\n<!-- MONTHLY_ARCHIVE_OVERVIEW_START -->\n<!-- MONTHLY_ARCHIVE_OVERVIEW_END -->\n\n"
        "<!-- MONTHLY_REPORTS_START -->\n<!-- MONTHLY_REPORTS_END -->\n"
    )
    _git(root, "add", ".")
    add_env = {"GIT_AUTHOR_DATE": "2026-08-10T12:00:00-07:00",
               "GIT_COMMITTER_DATE": "2026-08-10T12:00:00-07:00"}
    _git(root, "commit", "-qm", "add fixture", env=add_env)
    monkeypatch.setattr(monthly, "ROOT", root)
    monkeypatch.setattr(monthly, "RUNTIME", root / "runtime" / "monthly-report")
    return root


def test_manifest_uses_main_addition_month_and_preserves_first_appearance(tmp_path, monkeypatch):
    _fixture_repo(tmp_path, monkeypatch)
    manifest, _ = monthly.build_manifest("2026-08")
    assert manifest["works_count"] == 1
    work = manifest["works"][0]
    assert work["slug"] == "fixture-work"
    assert work["first_appeared"] == "2024-02-03"
    assert work["added_as"] == "Backfill"
    assert work["topics"][0]["slug"] == "planning_decision_evaluation"
    assert work["domains"][0]["slug"] == "biology"


def test_main_addition_manifest_does_not_repeat_prior_backfill(tmp_path, monkeypatch):
    root = _fixture_repo(tmp_path, monkeypatch)
    (root / "monthly" / "2026-07.md").write_text(
        "# July 2026 Monthly Report\n\n## Complete Monthly Index\n\n"
        "| Work | First appeared | Added as | Topics | Domains |\n"
        "|---|---|---|---|---|\n"
        "| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | — | — |\n"
    )
    manifest, _ = monthly.build_manifest("2026-08")
    assert manifest["works_count"] == 0


def test_validate_requires_complete_bilingual_index(tmp_path, monkeypatch):
    root = _fixture_repo(tmp_path, monkeypatch)
    manifest, _ = monthly.build_manifest("2026-08")
    en = """# August 2026 Monthly Report

> **English** | [简体中文](../zh/monthly/2026-08.md)

## Month at a Glance
One work.

## What Changed This Month
See [Fixture Work](../works/fixture-work.md), [Planning](../topics/planning_decision_evaluation.md), and [Biology](../domains/biology.md).

## Complete Monthly Index

| Work | First appeared | Added as | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
"""
    zh = """# 2026 年 8 月月报

> [English](../../monthly/2026-08.md) | **简体中文**

## 本月概览
本月补录一项工作。

## 这个月到底变了什么
先看 [Fixture Work](../../works/fixture-work.md)，再看 [Planning](../../topics/planning_decision_evaluation.md) 和 [Biology](../../domains/biology.md)。

## 本月完整索引

| Work | 首次公开 | 加入类型 | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../../works/fixture-work.md) | 2024-02-03 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
"""
    (root / "monthly" / "2026-08.md").write_text(en)
    (root / "zh" / "monthly" / "2026-08.md").write_text(zh)
    assert monthly.validate("2026-08", manifest) == []
    (root / "zh" / "monthly" / "2026-08.md").write_text(zh.replace("历史补录", "当月新发布"))
    errors = monthly.validate("2026-08", manifest)
    assert any("release/backfill mismatch" in error for error in errors)


@pytest.mark.parametrize("value", ["2026-00", "2026-13", "Aug-2026", "2026-8"])
def test_month_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        monthly._month(value)


def test_generate_force_refresh_overwrites_existing_month(tmp_path, monkeypatch):
    root = _fixture_repo(tmp_path, monkeypatch)
    en_path = root / "monthly" / "2026-08.md"
    zh_path = root / "zh" / "monthly" / "2026-08.md"
    en_path.write_text("old english\n")
    zh_path.write_text("old chinese\n")

    def fake_worker(agent, prompt, max_turns=35):
        if agent == "monthly-report-writer":
            en_path.write_text("""# August 2026 Monthly Report

> **English** | [简体中文](../zh/monthly/2026-08.md)

> **Coverage:** Cards added to main during 2026-08

## Month at a Glance
August 2026 changes one thing.

## What Changed This Month
See [Fixture Work](../works/fixture-work.md), [Planning](../topics/planning_decision_evaluation.md), and [Biology](../domains/biology.md).

## Complete Monthly Index

| Work | First appeared | Added as | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
""")
            return
        if agent == "monthly-report-translator":
            zh_path.write_text("""# 2026 年 8 月月报

> [English](../../monthly/2026-08.md) | **简体中文**

> **覆盖范围：** 2026-08 加入 main 的 cards

## 本月概览
2026 年 8 月有一个变化。

## 这个月到底变了什么
先看 [Fixture Work](../../works/fixture-work.md)，再看 [Planning](../../topics/planning_decision_evaluation.md) 和 [Biology](../../domains/biology.md)。

## 本月完整索引

| Work | 首次公开 | 加入类型 | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../../works/fixture-work.md) | 2024-02-03 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
""")
            return
        if agent in ("monthly-report-adversarial-reviewer", "monthly-report-chinese-reviewer"):
            return
        raise AssertionError(agent)

    monkeypatch.setattr(monthly, "_worker", fake_worker)

    with pytest.raises(RuntimeError):
        monthly.generate("2026-08", force=False)
    monthly.generate("2026-08", force=True)
    assert "old english" not in en_path.read_text()
    assert "old chinese" not in zh_path.read_text()
    assert "Fixture Work" in en_path.read_text()


def test_validate_catches_enumeration_mismatch(tmp_path, monkeypatch):
    root = _fixture_repo(tmp_path, monkeypatch)
    manifest, _ = monthly.build_manifest("2026-08")
    en = """# August 2026 Monthly Report

> **English** | [简体中文](../zh/monthly/2026-08.md)

## Month at a Glance
This month splits into three clear lines.

## What Changed This Month

### [Planning](../topics/planning_decision_evaluation.md)

This month has three clear lines. First, [Fixture Work](../works/fixture-work.md) changes planning evidence. Second, it sharpens verification.

## Complete Monthly Index

| Work | First appeared | Added as | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
"""
    zh = """# 2026 年 8 月月报

> [English](../../monthly/2026-08.md) | **简体中文**

## 本月概览
这个月能分成三条线。

## 这个月到底变了什么

### [Planning](../../topics/planning_decision_evaluation.md)

这个月至少能分成三种路数。第一种，是 [Fixture Work](../../works/fixture-work.md)。第二种，是验证更硬。

## 本月完整索引

| Work | 首次公开 | 加入类型 | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../../works/fixture-work.md) | 2024-02-03 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
"""
    (root / "monthly" / "2026-08.md").write_text(en)
    (root / "zh" / "monthly" / "2026-08.md").write_text(zh)
    errors = monthly.validate("2026-08", manifest)
    assert any("English enumeration mismatch" in error for error in errors)
    assert any("Chinese enumeration mismatch" in error for error in errors)


def test_validate_all_catches_cross_month_duplicate(tmp_path, monkeypatch, capsys):
    root = _fixture_repo(tmp_path, monkeypatch)
    card2 = """# Second Work (2025)

> **English** | [简体中文](../zh/works/second-work.md)

> **First appeared:** 2025-01-05 · **Source:** [Official record](https://example.com/second)

## Overview
Second overview.

## Topics
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities
N/A — fixture.

## Summary
Second summary.

## Domains
- [Biology](../domains/biology.md)

## Limitations
Second boundary.
"""
    (root / "works" / "second-work.md").write_text(card2)
    (root / "zh" / "works" / "second-work.md").write_text("mirror\n")
    _git(root, "add", ".")
    add_env = {"GIT_AUTHOR_DATE": "2026-08-12T12:00:00-07:00",
               "GIT_COMMITTER_DATE": "2026-08-12T12:00:00-07:00"}
    _git(root, "commit", "-qm", "add second fixture", env=add_env)

    month1 = """# January 2025 Monthly Report

> **English** | [简体中文](../zh/monthly/2025-01.md)

## Month at a Glance
January 2025 changes one thing.

## What Changed This Month
See [Fixture Work](../works/fixture-work.md).

## Complete Monthly Index

| Work | First appeared | Added as | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
"""
    month1_zh = """# 2025 年 1 月月报

> [English](../../monthly/2025-01.md) | **简体中文**

## 本月概览
2025 年 1 月有一个变化。

## 这个月到底变了什么
先看 [Fixture Work](../../works/fixture-work.md)。

## 本月完整索引

| Work | 首次公开 | 加入类型 | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../../works/fixture-work.md) | 2024-02-03 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
"""
    month2 = """# August 2026 Monthly Report

> **English** | [简体中文](../zh/monthly/2026-08.md)

## Month at a Glance
August 2026 changes one thing.

## What Changed This Month
See [Fixture Work](../works/fixture-work.md) and [Second Work](../works/second-work.md).

## Complete Monthly Index

| Work | First appeared | Added as | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../works/fixture-work.md) | 2024-02-03 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
| [Second Work](../works/second-work.md) | 2025-01-05 | Backfill | [Planning](../topics/planning_decision_evaluation.md) | [Biology](../domains/biology.md) |
"""
    month2_zh = """# 2026 年 8 月月报

> [English](../../monthly/2026-08.md) | **简体中文**

## 本月概览
2026 年 8 月有一个变化。

## 这个月到底变了什么
先看 [Fixture Work](../../works/fixture-work.md) 和 [Second Work](../../works/second-work.md)。

## 本月完整索引

| Work | 首次公开 | 加入类型 | Topics | Domains |
|---|---|---|---|---|
| [Fixture Work](../../works/fixture-work.md) | 2024-02-03 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
| [Second Work](../../works/second-work.md) | 2025-01-05 | 历史补录 | [Planning](../../topics/planning_decision_evaluation.md) | [Biology](../../domains/biology.md) |
"""
    (root / "monthly" / "2025-01.md").write_text(month1)
    (root / "zh" / "monthly" / "2025-01.md").write_text(month1_zh)
    (root / "monthly" / "2026-08.md").write_text(month2)
    (root / "zh" / "monthly" / "2026-08.md").write_text(month2_zh)

    monkeypatch.setattr(sys, "argv", ["monthly_report.py", "validate-all"])
    assert monthly.main() == 1
    out = capsys.readouterr().out
    assert "work fixture-work also appears in 2025-01" in out
