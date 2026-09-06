"""Repo-wide card sweeps and the Chinese-card conventions.

These are the checks a human PR gets: the daily updater validates only the slugs one run produced,
so nothing re-examines older cards. Every check here has a matching negative fixture — a check that
cannot fail is not a gate.
"""
import os
import subprocess
import sys

import pytest
from conftest import build_mini_repo

import validators


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
NO_URL_LINKS = "- **Paper:** the preprint is listed in the proceedings index."


def _required(root):
    """Template headings, read from the fixture's own works/README.md."""
    return validators._template_headings(root)


def _zh_card(root, slug, activities=("simulation_scientific_computing",),
             labels=None, headings=None):
    """Write a Chinese mirror carrying the English section headings.

    `labels` overrides the activity link text; `headings` overrides the section headings, which is
    how the negative fixtures inject translated or reordered sections.
    """
    heads = list(headings or _required(root))
    labels = labels or {}
    body = ["# %s (2025)\n" % slug,
            "> [English](../../works/%s.md) | **简体中文**\n" % slug,
            "> **首次公开：** 2025-01-02 · **来源：** "
            "[arXiv 首次提交](https://arxiv.org/abs/2401.00001)\n"]
    for h in heads:
        body.append("## %s\n" % h)
        if h.startswith("Activities") or h == "研究活动":
            body.append("\n".join("- [%s](../activities/%s.md)" % (labels.get(a, a), a)
                                  for a in activities) or "N/A — 方法学工作。")
        else:
            body.append("一段中文说明。")
        body.append("")
    path = os.path.join(root, "zh", "works", "%s.md" % slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write("\n".join(body))
    return path


def _zh_activity(root, slug, title):
    d = os.path.join(root, "zh", "activities")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "%s.md" % slug), "w").write(
        "# %s\n\n## 相关工作\n" % title)


def _zh_fixture(root, cards, labels=None, headings=None,
                activities=("simulation_scientific_computing",)):
    """A mini repo whose Chinese cards are rewritten under the caller's control."""
    build_mini_repo(root, cards)
    _zh_activity(root, "simulation_scientific_computing", "模拟与科学计算")
    _zh_activity(root, "modeling_prediction", "建模与预测")
    for c in cards:
        _zh_card(root, c["slug"], activities=activities, labels=labels, headings=headings)
    return root


# ------------------------------------------------------------ repo-wide enumeration
def test_all_card_slugs_enumerates_works_and_skips_readme(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "beta", "title": "Beta"},
                                           {"slug": "alpha", "title": "Alpha"}])
    assert validators.all_card_slugs(root) == ["alpha", "beta"]


def test_cards_all_catches_a_card_outside_the_run_slug_list(tmp_path):
    """The traxgen regression: a defect survives because no run ever names that slug again."""
    root = build_mini_repo(str(tmp_path), [
        {"slug": "fresh", "title": "Fresh"},
        {"slug": "historic", "title": "Historic", "links": NO_URL_LINKS},
    ])
    ok, _ = validators.validate_cards(root, ["fresh"])
    assert ok, "the per-run gate passes — that is exactly the blind spot"
    ok, errs = validators.validate_cards_all(root)
    assert not ok
    assert errs == ["historic: Links section has no URL"]


def test_bilingual_all_catches_a_missing_mirror_outside_the_run_slug_list(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "fresh", "title": "Fresh"},
        {"slug": "historic", "title": "Historic", "zh": False},
    ])
    ok, _ = validators.validate_bilingual(root, ["fresh"])
    assert ok
    ok, errs = validators.validate_bilingual_all(root)
    assert not ok and any("historic" in e for e in errs)


def test_cards_all_passes_on_a_clean_repo(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "alpha", "title": "Alpha"}])
    ok, errs = validators.validate_cards_all(root)
    assert ok, errs
    ok, errs = validators.validate_bilingual_all(root)
    assert ok, errs


# ------------------------------------------------------------ card section order
def test_card_sections_must_follow_template_order(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "alpha", "title": "Alpha"}])
    path = os.path.join(root, "works", "alpha.md")
    txt = open(path).read()
    strengths = txt.index("## Strengths")
    limits = txt.index("## Limitations")
    related = txt.index("## Related Works")
    swapped = txt[:strengths] + txt[limits:related] + txt[strengths:limits] + txt[related:]
    open(path, "w").write(swapped)
    ok, errs = validators.validate_cards_all(root)
    assert not ok
    assert errs == ["alpha: section '## Limitations' is out of template order "
                    "(the template has '## Strengths' here)"]


def test_card_order_check_stays_quiet_when_a_section_is_missing(tmp_path):
    """A missing section is reported once, as a missing section — not also as an order defect."""
    root = build_mini_repo(str(tmp_path), [{"slug": "alpha", "title": "Alpha"}])
    path = os.path.join(root, "works", "alpha.md")
    txt = open(path).read()
    open(path, "w").write(txt.replace("## Strengths", "## Strong Points"))
    ok, errs = validators.validate_cards_all(root)
    assert not ok
    assert errs == ["alpha: heading '## Strengths' appears 0 times (want 1)"]


# ------------------------------------------------------------ zh activity labels
def test_zh_activity_labels_accept_the_activity_page_h1(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "模拟与科学计算"})
    ok, errs = validators.validate_zh_activity_labels(root)
    assert ok, errs


@pytest.mark.parametrize("label", ["模拟与科学计算 ", "科学计算与模拟",
                                   "Simulation & Scientific Computing"])
def test_zh_activity_labels_reject_a_drifted_label(tmp_path, label):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": label})
    ok, errs = validators.validate_zh_activity_labels(root)
    if label.strip() == "模拟与科学计算":
        assert ok, "surrounding whitespace is not drift"
        return
    assert not ok
    assert errs == ["alpha: activity 'simulation_scientific_computing' labelled '%s', "
                    "canonical is '模拟与科学计算'" % label]


def test_zh_activity_labels_follow_the_page_when_the_page_is_renamed(tmp_path):
    """The canonical label is derived from the page, so renaming the page moves the target."""
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "模拟与科学计算"})
    _zh_activity(root, "simulation_scientific_computing", "仿真与科学计算")
    ok, errs = validators.validate_zh_activity_labels(root)
    assert not ok and "canonical is '仿真与科学计算'" in errs[0]


def test_zh_activity_labels_report_a_missing_activities_section(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}])
    heads = [h for h in _required(root) if h != "Activities"]
    _zh_card(root, "alpha", headings=heads)
    ok, errs = validators.validate_zh_activity_labels(root)
    assert not ok and errs == ["alpha: zh card has no '## Activities' section"]


# ------------------------------------------------------------ zh card headings
def test_zh_cards_with_english_headings_pass(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "模拟与科学计算"})
    ok, errs = validators.validate_zh_card_headings(root)
    assert ok, errs


def test_zh_cards_reject_translated_headings(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}])
    heads = ["概览" if h == "Overview" else "摘要" if h == "Summary" else h
             for h in _required(root)]
    _zh_card(root, "alpha", headings=heads)
    ok, errs = validators.validate_zh_card_headings(root)
    assert not ok
    assert errs == ["alpha: zh card uses Chinese section headings (## 概览, ## 摘要) — "
                    "zh cards keep the English headings"]


def test_zh_cards_reject_a_missing_english_heading(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}])
    _zh_card(root, "alpha", headings=[h for h in _required(root) if h != "Evaluation"])
    ok, errs = validators.validate_zh_card_headings(root)
    assert not ok
    assert errs == ["alpha: zh card heading '## Evaluation' appears 0 times (want 1)"]


def test_zh_cards_reject_out_of_order_sections(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}])
    heads = _required(root)
    i, j = heads.index("Strengths"), heads.index("Limitations")
    heads[i], heads[j] = heads[j], heads[i]
    _zh_card(root, "alpha", headings=heads)
    ok, errs = validators.validate_zh_card_headings(root)
    assert not ok
    assert errs == ["alpha: zh card section '## Limitations' is out of template order "
                    "(the template has '## Strengths' here)"]


def test_zh_heading_check_ignores_the_works_readme(tmp_path):
    """zh/works/README.md is documentation about cards, not a card; its headings stay Chinese."""
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "模拟与科学计算"})
    open(os.path.join(root, "zh", "works", "README.md"), "w").write(
        "# 卡片\n\n## 卡片模板\n\n说明。\n")
    ok, errs = validators.validate_zh_card_headings(root)
    assert ok, errs
    ok, errs = validators.validate_zh_activity_labels(root)
    assert ok, errs


# ------------------------------------------------------------ CLI wiring
@pytest.mark.parametrize("check", ["cards-all", "bilingual-all", "zh-activity-labels",
                                   "zh-headings"])
def test_cli_subcommand_runs_against_a_repo_root(tmp_path, check):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "模拟与科学计算"})
    p = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "update_agent",
                                                     "validators.py"), check,
                        "--repo-root", root],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert p.returncode == 0, p.stdout.decode()
    assert ("%s: PASS" % check) in p.stdout.decode()


def test_cli_subcommand_exits_nonzero_on_drift(tmp_path):
    root = _zh_fixture(str(tmp_path), [{"slug": "alpha", "title": "Alpha",
                                        "activities": ["simulation_scientific_computing"]}],
                       labels={"simulation_scientific_computing": "科学计算与模拟"})
    p = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "update_agent",
                                                     "validators.py"), "zh-activity-labels",
                        "--repo-root", root],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert p.returncode == 1
    assert "canonical is '模拟与科学计算'" in p.stdout.decode()
