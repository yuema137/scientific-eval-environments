import importlib.util
import os
import subprocess
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
