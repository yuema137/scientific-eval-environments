import json
import os

import pytest
from conftest import build_mini_repo

import inventory
import deduplicate
import phase_state
import related_works
import validators


# ------------------------------------------------------------ inventory
def test_card_identity_extraction(tmp_path):
    c = tmp_path / "mle-bench.md"
    c.write_text("# MLE-bench (2025)\n\n## Links\n"
                 "- **Paper:** <https://arxiv.org/abs/2410.07095>\n"
                 "- **Code:** <https://github.com/openai/mle-bench>\n")
    ident = inventory.card_identity(str(c))
    assert ident["arxiv"] == ["2410.07095"]
    assert ident["github"] == ["github.com/openai/mle-bench"]
    assert ident["title_norm"] == "mle bench"


def test_title_normalization():
    from common import normalize_title
    assert normalize_title("MLE-Bench: A Test!") == normalize_title("mle bench a test")
    assert normalize_title("Agent-Bench") == "agent bench"


# ------------------------------------------------------------ dedup
def _raw(source, _id, url, title, abstract="agent benchmark evaluation"):
    return {"source": source, "id": _id, "url": url, "title": title,
            "abstract_or_description": abstract, "authors": [], "date": "",
            "matched_profiles": ["Global"], "discovered_at": ""}


def _run_dedup(tmp_path, raw, existing_repo=None):
    run = tmp_path / "run"
    (run / "phase1").mkdir(parents=True)
    (run / "phase1" / "raw_hits.json").write_text(json.dumps(raw))
    root = existing_repo or build_mini_repo(str(tmp_path / "repo"), [])
    deduplicate.run(str(run), repo_root=root)
    load = lambda n: json.loads((run / "phase1" / n).read_text())
    return load("candidates.json"), load("duplicate_matches.json"), load("rejected.json")


def test_dedup_exact_arxiv_duplicate(tmp_path):
    repo = build_mini_repo(str(tmp_path / "repo"),
                           [{"slug": "foo", "title": "Foo Bench",
                             "links": "- **Paper:** <https://arxiv.org/abs/2401.09999>"}])
    cands, dups, _ = _run_dedup(tmp_path, [_raw("arxiv", "2401.09999", "https://arxiv.org/abs/2401.09999", "Foo Bench")], repo)
    assert cands == []
    assert dups and dups[0]["match"]["kind"] == "arxiv"


def test_dedup_title_case_punctuation(tmp_path):
    repo = build_mini_repo(str(tmp_path / "repo"),
                           [{"slug": "foo", "title": "Foo Bench",
                             "links": "- **Paper:** <https://example.com>"}])
    cands, dups, _ = _run_dedup(tmp_path, [_raw("arxiv", "2401.11111", "https://arxiv.org/abs/2401.11111", "FOO-BENCH!!")], repo)
    assert cands == [] and dups  # matched by normalized title


def test_dedup_cross_source_merge(tmp_path):
    raw = [_raw("arxiv", "2402.00001", "https://arxiv.org/abs/2402.00001", "Cool Agent Benchmark"),
           _raw("github", "acme/cool", "https://github.com/acme/cool", "Cool Agent Benchmark")]
    cands, _, _ = _run_dedup(tmp_path, raw)
    assert len(cands) == 1
    assert {r["source"] for r in cands[0]["source_records"]} == {"arxiv", "github"}


def test_dedup_distinct_similar_titles_not_merged(tmp_path):
    raw = [_raw("arxiv", "2402.00002", "https://arxiv.org/abs/2402.00002", "Agent Benchmark for Physics"),
           _raw("arxiv", "2402.00003", "https://arxiv.org/abs/2402.00003", "Agent Benchmark for Chemistry")]
    cands, _, _ = _run_dedup(tmp_path, raw)
    assert len(cands) == 2


def test_dedup_out_of_scope_rejected(tmp_path):
    cands, _, rej = _run_dedup(tmp_path, [_raw("arxiv", "2402.00004", "https://arxiv.org/abs/2402.00004",
                                               "A Cookbook of Pasta Recipes", abstract="pasta food cooking")])
    assert cands == [] and rej


def test_dedup_pending_pr_awareness(tmp_path):
    pend = tmp_path / "pending.json"
    pend.write_text(json.dumps({"arxiv": {"2403.00001": "pending-slug"},
                                "openreview": {}, "doi": {}, "github": {}, "title_norm": {}}))
    run = tmp_path / "run"
    (run / "phase1").mkdir(parents=True)
    (run / "phase1" / "raw_hits.json").write_text(json.dumps(
        [_raw("arxiv", "2403.00001", "https://arxiv.org/abs/2403.00001", "Already Proposed Bench")]))
    repo = build_mini_repo(str(tmp_path / "repo"), [])
    deduplicate.run(str(run), str(pend), repo_root=repo)
    dups = json.loads((run / "phase1" / "duplicate_matches.json").read_text())
    assert dups and dups[0]["match"]["kind"] == "pending-pr"


# ------------------------------------------------------------ phase state / final gate
def test_gate_all_pass_ready():
    states = {p: "pass" for p in phase_state.REQUIRED_PHASES}
    g = phase_state.compute_gate(states, accepted_count=3)
    assert g["ready_for_pr"] is True and g["run_status"] == "success"


@pytest.mark.parametrize("bad", phase_state.REQUIRED_PHASES)
def test_gate_single_fail_blocks(bad):
    states = {p: "pass" for p in phase_state.REQUIRED_PHASES}
    states[bad] = "fail"
    g = phase_state.compute_gate(states, accepted_count=3)
    assert g["ready_for_pr"] is False and g["run_status"] == "fail"


def test_gate_empty_run_is_success_no_pr():
    states = {"discovery": "pass", "cards": "skipped", "english_axes": "skipped",
              "chinese_mirror": "skipped", "chinese_review": "skipped", "final_validation": "skipped"}
    g = phase_state.compute_gate(states, accepted_count=0)
    assert g["empty_run"] is True and g["ready_for_pr"] is False and g["run_status"] == "success"


def test_failure_injection_blocks_pr(tmp_path):
    # simulate Chinese parity gate FAIL after earlier phases passed
    for p in ["discovery", "cards", "english_axes"]:
        phase_state.write_phase_result(str(tmp_path), p, "pass")
    phase_state.write_phase_result(str(tmp_path), "chinese_mirror", "fail")
    phase_state.write_phase_result(str(tmp_path), "chinese_review", "skipped")
    phase_state.write_phase_result(str(tmp_path), "final_validation", "skipped")
    g = phase_state.run(str(tmp_path), accepted_count=2, smoke=False)
    assert g["ready_for_pr"] is False
    assert g["run_status"] == "fail"
    assert g["would_open_pr"] is False


def test_gate_smoke_never_opens_pr(tmp_path):
    for p in phase_state.REQUIRED_PHASES:
        phase_state.write_phase_result(str(tmp_path), p, "pass")
    g = phase_state.run(str(tmp_path), accepted_count=1, smoke=True)
    assert g["would_open_pr"] is True
    assert g["ready_for_pr"] is False
    assert g["pr_creation_disabled_by_smoke_mode"] is True


# ------------------------------------------------------------ profiles (real repo)
def test_profiles_cover_full_taxonomy():
    ok, errs = validators.validate_profiles()
    assert ok, errs


def test_topic_explanations_cover_full_taxonomy():
    ok, errs = validators.validate_topic_explanations()
    assert ok, errs


# ------------------------------------------------------------ axis validators (fixtures)
def test_axes_valid_mapping(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "a", "title": "A", "topics": ["trajectory_evaluation"], "activities": ["simulation_scientific_computing"]},
        {"slug": "other", "title": "Other"},
    ])
    ok, errs = validators.validate_axes(root)
    assert ok, errs


def test_axis_related_works_are_sorted_by_first_appeared(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "older", "title": "Older", "topics": ["trajectory_evaluation"]},
        {"slug": "zulu", "title": "Zulu", "topics": ["trajectory_evaluation"]},
        {"slug": "alpha", "title": "Alpha", "topics": ["trajectory_evaluation"]},
    ])
    for slug, date in (("older", "2024-01-01"), ("zulu", "2026-01-01"), ("alpha", "2026-01-01")):
        path = os.path.join(root, "works", "%s.md" % slug)
        text = open(path).read().replace("2025-01-02", date)
        open(path, "w").write(text)

    page = os.path.join(root, "topics", "trajectory_evaluation.md")
    zh_page = os.path.join(root, "zh", "topics", "trajectory_evaluation.md")
    open(zh_page, "w").write("# trajectory_evaluation\n\n## 相关工作\n\n"
                              "- [Older](../works/older.md)\n"
                              "- [Zulu](../works/zulu.md)\n"
                              "- [Alpha](../works/alpha.md)\n")
    assert related_works.sort_all(root) == [
        "topics/trajectory_evaluation.md",
        "zh/topics/trajectory_evaluation.md",
    ]
    text = open(page).read()
    assert text.index("../works/alpha.md") < text.index("../works/zulu.md") < text.index("../works/older.md")
    zh_text = open(zh_page).read()
    assert zh_text.index("../works/alpha.md") < zh_text.index("../works/zulu.md") < zh_text.index("../works/older.md")
    ok, errs = validators.validate_axes(root)
    assert ok, errs


def test_axis_validator_rejects_non_chronological_related_works(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "older", "title": "Older", "topics": ["trajectory_evaluation"]},
        {"slug": "newer", "title": "Newer", "topics": ["trajectory_evaluation"]},
    ])
    newer = os.path.join(root, "works", "newer.md")
    newer_text = open(newer).read().replace("2025-01-02", "2026-01-01")
    open(newer, "w").write(newer_text)
    ok, errs = validators.validate_axes(root)
    assert not ok
    assert any("not ordered by First appeared" in error for error in errs)


def test_topic_explanations_detect_missing_entry(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "a", "title": "A", "topics": ["trajectory_evaluation"]},
    ])
    tp = os.path.join(root, "zh", "topics", "trajectory_evaluation.md")
    open(tp, "w").write("# trajectory_evaluation\n")
    ok, errs = validators.validate_topic_explanations(root)
    assert not ok and any("先看它解决什么问题" in e for e in errs)


def test_axes_missing_reverse_mapping(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "a", "title": "A", "topics": ["trajectory_evaluation"]},
        {"slug": "other", "title": "Other"},
    ])
    # break the reverse index: remove 'a' from the topic page Related Works
    tp = os.path.join(root, "topics", "trajectory_evaluation.md")
    open(tp, "w").write("# trajectory_evaluation\n\n## Related Works\n\n")
    ok, errs = validators.validate_axes(root)
    assert not ok and any("omits" in e for e in errs)


def test_axes_duplicate_related_works(tmp_path):
    root = build_mini_repo(str(tmp_path), [
        {"slug": "a", "title": "A", "topics": ["trajectory_evaluation"]},
        {"slug": "other", "title": "Other"}])
    tp = os.path.join(root, "topics", "trajectory_evaluation.md")
    open(tp, "w").write("# t\n\n## Related Works\n\n- [A](../works/a.md)\n- [A](../works/a.md)\n")
    ok, errs = validators.validate_axes(root)
    assert not ok and any("duplicate" in e for e in errs)


def test_axes_broken_card_link(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "a", "title": "A", "topics": ["trajectory_evaluation"]},
                                           {"slug": "other", "title": "Other"}])
    tp = os.path.join(root, "topics", "trajectory_evaluation.md")
    open(tp, "w").write("# t\n\n## Related Works\n\n- [A](../works/a.md)\n- [Ghost](../works/ghost.md)\n")
    ok, errs = validators.validate_axes(root)
    assert not ok and any("missing card" in e for e in errs)


def test_cards_schema(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "good", "title": "Good",
                                            "activities": ["simulation_scientific_computing"]}])
    ok, errs = validators.validate_cards(root, ["good"])
    assert ok, errs
    # a real template placeholder token still fails the card
    bad = os.path.join(root, "works", "good.md")
    open(bad, "w").write(open(bad).read().replace("One line.", "TODO(card)"))
    ok, errs = validators.validate_cards(root, ["good"])
    assert not ok


def test_placeholder_prose_tbd_allowed_but_unfilled_field_and_tokens_flagged():
    # bare TBD/TBA in legitimate descriptive prose must NOT fail (regression: a real card said
    # "the preprint lists the venue as TBD" and was wrongly rejected)
    assert validators._has_placeholder("the preprint text lists the venue as TBD") is False
    assert validators._has_placeholder("we leave the extension as TBD for future work") is False
    assert validators._has_placeholder("## Activities\nN/A — evaluation methodology.") is False
    # an unfilled metadata field whose value is only TBD/TBA is still a defect
    assert validators._has_placeholder("- **Venue:** TBD") is True
    assert validators._has_placeholder("- **Year:** TBA") is True
    # genuine template tokens are still rejected anywhere
    for tok in ("TODO(card)", "FILL_ME", "<placeholder>", "{{PLACEHOLDER}}", "lorem ipsum"):
        assert validators._has_placeholder("Overview: %s" % tok) is True, tok


# ------------------------------------------------------------ bilingual
def test_bilingual_valid_pair(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "a", "title": "A",
                                            "activities": ["simulation_scientific_computing"]}])
    ok, errs = validators.validate_bilingual(root, ["a"])
    assert ok, errs


def test_bilingual_missing_mirror(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "a", "title": "A", "zh": False}])
    ok, errs = validators.validate_bilingual(root, ["a"])
    assert not ok and any("missing Chinese mirror" in e for e in errs)


def test_bilingual_membership_mismatch(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "a", "title": "A",
                                            "activities": ["simulation_scientific_computing"]}])
    zt = os.path.join(root, "zh", "works", "a.md")
    open(zt, "w").write(open(zt).read().replace(
        "- [simulation_scientific_computing](../activities/simulation_scientific_computing.md)",
        "N/A — evaluation methodology."))
    ok, errs = validators.validate_bilingual(root, ["a"])
    assert not ok and any("membership differs" in e for e in errs)


def test_bilingual_first_appearance_mismatch(tmp_path):
    root = build_mini_repo(str(tmp_path), [{"slug": "a", "title": "A"}])
    zt = os.path.join(root, "zh", "works", "a.md")
    text = open(zt).read().replace("2025-01-02", "2025-01-03")
    open(zt, "w").write(text)
    ok, errs = validators.validate_bilingual(root, ["a"])
    assert not ok and any("first-appearance date or provenance URL differs" in e for e in errs)


def test_first_appearance_covers_full_repository():
    ok, errs = validators.validate_first_appearance()
    assert ok, errs
