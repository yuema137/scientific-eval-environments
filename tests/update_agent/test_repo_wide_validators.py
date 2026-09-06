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


# ------------------------------------------------------------ domain capability matrices
MATRIX_COLUMNS = ["Work", "Domain", "Net", "E2E", "Cost", "MM", "Repro", "Real", "Inter", "Cov",
                  "Human", "Rubric", "Contam", "Verif", "Scale", "Fail", "Rig"]


def _matrix_page(root, domain, rows, folder="domains", columns=None):
    """Write a domain page whose Capability Matrix holds `rows` of (work, Cov, Rig).

    `columns` lets a test shift the header, which is how the by-name column lookup is exercised:
    the same rows read correctly under a header an index-based parser would misread.
    """
    columns = list(columns or MATRIX_COLUMNS)
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    for work, cov, rig in rows:
        cell = {"Work": work, "Domain": "GEN", "Cov": "**%s**" % cov, "Rig": "**%s**" % rig,
                "Verif": "3", "Scale": "2", "Fail": "4"}
        lines.append("| " + " | ".join(cell.get(c, "\u2714") for c in columns) + " |")
    d = os.path.join(root, folder)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "%s.md" % domain), "w").write(
        "# %s\n\n## Scope\n\nA field.\n\n## Capability Matrix\n\nA checklist view.\n\n%s\n\n"
        "## Related Works\n\n- none yet\n" % (domain, "\n".join(lines)))


def _matrix_fixture(tmp_path, rows, zh_rows="same", domain="physics", columns=None):
    """A mini repo carrying one domain page and, unless `zh_rows` is None, its Chinese mirror."""
    root = build_mini_repo(str(tmp_path), [{"slug": "alpha", "title": "Alpha"}])
    _matrix_page(root, domain, rows, columns=columns)
    if zh_rows is not None:
        _matrix_page(root, domain, rows if zh_rows == "same" else zh_rows,
                     folder=os.path.join("zh", "domains"), columns=columns)
    return root


def test_matrix_ordering_accepts_a_correctly_ranked_page(tmp_path):
    root = _matrix_fixture(tmp_path, [("High", "5.5", "7"), ("Mid", "5", "9"),
                                      ("Low", "5", "6.5"), ("Least", "0", "13")])
    ok, errs = validators.validate_matrix_ordering(root)
    assert ok, errs


def test_matrix_ordering_flags_a_rig_inversion_inside_equal_coverage(tmp_path):
    """The ai_ml_research defect: equal `Cov`, but the lower `Rig` row sits first."""
    root = _matrix_fixture(tmp_path, [("Curation-Bench", "5", "7"), ("PaperBench", "5", "7.5")],
                           zh_rows=None)
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["domains/physics.md: row 1 'Curation-Bench' (Cov 5, Rig 7) precedes "
                    "'PaperBench' (Cov 5, Rig 7.5)"]


def test_matrix_ordering_flags_a_coverage_inversion(tmp_path):
    root = _matrix_fixture(tmp_path, [("Narrow", "3", "11"), ("Broad", "5", "2")], zh_rows=None)
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["domains/physics.md: row 1 'Narrow' (Cov 3, Rig 11) precedes "
                    "'Broad' (Cov 5, Rig 2)"]


def test_matrix_ordering_reports_every_row_a_misplaced_row_jumped(tmp_path):
    """The chemistry defect: one row at the wrong rank inverts against each row above it."""
    root = _matrix_fixture(tmp_path, [("MolClaw", "3", "7"), ("DrBencher", "3", "6"),
                                      ("Model Discovery Agent", "3", "8")], zh_rows=None)
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == [
        "domains/physics.md: row 1 'MolClaw' (Cov 3, Rig 7) precedes "
        "'Model Discovery Agent' (Cov 3, Rig 8)",
        "domains/physics.md: row 2 'DrBencher' (Cov 3, Rig 6) precedes "
        "'Model Discovery Agent' (Cov 3, Rig 8)",
    ]


@pytest.mark.parametrize("order", [("Ay", "Bee"), ("Bee", "Ay")])
def test_matrix_ordering_allows_a_tie_on_both_scores_in_either_order(tmp_path, order):
    """Rows equal on `Cov` AND `Rig` keep Comparison-table order — a freedom, not a defect."""
    root = _matrix_fixture(tmp_path, [(order[0], "4", "6.5"), (order[1], "4", "6.5")])
    ok, errs = validators.validate_matrix_ordering(root)
    assert ok, errs


def test_matrix_ordering_reads_cov_and_rig_by_header_name(tmp_path):
    """A shifted header must not shift which numbers get compared."""
    columns = ["Work", "Notes"] + MATRIX_COLUMNS[1:]
    root = _matrix_fixture(tmp_path, [("First", "5", "7"), ("Second", "5", "7.5")],
                           zh_rows=None, columns=columns)
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["domains/physics.md: row 1 'First' (Cov 5, Rig 7) precedes "
                    "'Second' (Cov 5, Rig 7.5)"]


def test_matrix_ordering_flags_an_en_zh_row_order_mismatch(tmp_path):
    """Both pages are internally ordered; only the tie is resolved differently."""
    root = _matrix_fixture(tmp_path, [("Ay", "4", "6"), ("Bee", "4", "6")],
                           zh_rows=[("Bee", "4", "6"), ("Ay", "4", "6")])
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == [
        "zh/domains/physics.md: Capability Matrix row 1 is 'Bee', domains/physics.md has 'Ay'",
        "zh/domains/physics.md: Capability Matrix row 2 is 'Ay', domains/physics.md has 'Bee'",
    ]


def test_matrix_ordering_flags_an_en_zh_row_count_mismatch(tmp_path):
    root = _matrix_fixture(tmp_path, [("Ay", "4", "6"), ("Bee", "3", "6")],
                           zh_rows=[("Ay", "4", "6")])
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["zh/domains/physics.md: Capability Matrix has 1 rows, "
                    "domains/physics.md has 2"]


def test_matrix_ordering_flags_a_mirror_that_dropped_the_matrix(tmp_path):
    root = _matrix_fixture(tmp_path, [("Ay", "4", "6")], zh_rows=None)
    d = os.path.join(root, "zh", "domains")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "physics.md"), "w").write("# physics\n\n## Scope\n\n一个领域。\n")
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["zh/domains/physics.md: mirrors domains/physics.md but has no "
                    "Capability Matrix table"]


def test_matrix_ordering_skips_a_domain_page_with_no_matrix_yet(tmp_path):
    """The matrix rolls out domain by domain; a page without one is not yet a defect."""
    root = build_mini_repo(str(tmp_path), [{"slug": "alpha", "title": "Alpha"}])
    open(os.path.join(root, "domains", "physics.md"), "w").write(
        "# physics\n\n## Scope\n\nA field.\n\n## Related Works\n\n- none yet\n")
    ok, errs = validators.validate_matrix_ordering(root)
    assert ok, errs


def test_matrix_ordering_reports_an_unparseable_score_cell(tmp_path):
    root = _matrix_fixture(tmp_path, [("Ay", "4", "6"), ("Bee", "3", "n/a")], zh_rows=None)
    ok, errs = validators.validate_matrix_ordering(root)
    assert not ok
    assert errs == ["domains/physics.md: Capability Matrix row 2 'Bee' has a non-numeric "
                    "Rig cell '**n/a**'"]


def test_repository_capability_matrices_are_ordered():
    """The real pages, not a fixture: this is the check the two repaired pages must keep passing."""
    ok, errs = validators.validate_matrix_ordering(ROOT)
    assert ok, errs


# ------------------------------------------------------------ CLI wiring
@pytest.mark.parametrize("check", ["cards-all", "bilingual-all", "zh-activity-labels",
                                   "zh-headings", "matrix-ordering"])
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
