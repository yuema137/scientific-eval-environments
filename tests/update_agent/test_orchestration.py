"""Deterministic end-to-end orchestration test.

Drives the real five-phase orchestrator (fixture_e2e -> pipeline -> integrate -> validators ->
final gate) but STUBS the Claude worker calls with canned, faithful outputs. This proves the
control flow, phase gates, English integration, bilingual parity, independent review step, and
the smoke final-gate ("all phases pass -> would_open_pr, but no PR is created") WITHOUT a live
model or network — complementary to the live auth / fixture smokes that run on the GitHub runner.
"""
import os
import re

import pipeline
import fixture_e2e

CARD = """# {title}

> **English** | [简体中文](../zh/works/{slug}.md)

## Overview
{title} is a fixture benchmark used by the orchestration test.

## Topics
TODO(axis)

## Activities
TODO(axis)

## Links
- **Paper:** <https://arxiv.org/abs/0000.00000>

## Summary
A synthetic in-scope benchmark for exercising the pipeline.

## Tasks
120 fixture tasks over tokamak transport simulations.

## Domains
Physics — plasma-physics simulation.

## Evaluation
Numerical comparison against reference solutions.

## Typical Duration
Long-horizon.

## Main Contribution
A fixture contribution.

## Key Design Ideas
- fixture idea

## Strengths
- fixture strength

## Limitations
- Repository note: fixture card, not a real work.

## Related Works
- [Other](./other.md)
"""


def _append_related(path, line):
    t = open(path).read()
    t = re.sub(r"(## Related Works\s*\n)", r"\1" + line + "\n", t, count=1)
    open(path, "w").write(t)


def _stub_worker(agent, kind, prompt, cwd, max_turns, schema=None, model=None):
    if kind == "card":
        slug = re.search(r"works/([a-z0-9\-]+)\.md", prompt).group(1)
        cid = re.search(r"candidate_id:\s*(\S+)", prompt).group(1)
        open(os.path.join(cwd, "works", "%s.md" % slug), "w").write(
            CARD.format(title="FusionBench Fixture", slug=slug))
        return {"ok": True, "structured_output": {"candidate_id": cid, "decision": "accepted",
                "card_slug": slug, "card_title": "FusionBench Fixture"}}
    if kind == "axis":
        slug = re.search(r"slugs:\s*(\S+)", prompt).group(1)
        title = "FusionBench Fixture"
        if "topic" in agent:
            _append_related(os.path.join(cwd, "topics", "scientific_agents.md"),
                            "- [%s](../works/%s.md)" % (title, slug))
            _write(cwd, "runtime/phase3/topic_assignments.json",
                   {"assignments": [{"slug": slug, "topics": ["scientific_agents"]}],
                    "pages_edited": ["topics/scientific_agents.md"]})
        elif "domain" in agent:
            _append_related(os.path.join(cwd, "domains", "physics.md"),
                            "- [%s](../works/%s.md)" % (title, slug))
            _write(cwd, "runtime/phase3/domain_assignments.json",
                   {"assignments": [{"slug": slug, "domains": ["physics"]}],
                    "pages_edited": ["domains/physics.md"]})
        elif "activity" in agent:
            _append_related(os.path.join(cwd, "activities", "simulation_scientific_computing.md"),
                            "- [%s](../works/%s.md)" % (title, slug))
            _write(cwd, "runtime/phase3/activity_assignments.json",
                   {"assignments": [{"slug": slug, "activities": ["simulation_scientific_computing"],
                    "na_reason": None}], "pages_edited": ["activities/simulation_scientific_computing.md"]})
        return {"ok": True, "structured_output": {"status": "ok"}}
    if kind == "translate":
        written = []
        for en, zh in re.findall(r"(\S+\.md) -> (\S+\.md)", prompt):
            src = os.path.join(cwd, en)
            if not os.path.exists(src):
                continue
            t = open(src).read()
            tblock = _block(t, "Topics")
            ablock = _block(t, "Activities")
            zt = ("# FusionBench Fixture\n\n> [English](../../works/%s) | **简体中文**\n\n"
                  "## Topics\n%s\n\n## Activities\n%s\n" %
                  (os.path.basename(en), tblock, ablock))
            os.makedirs(os.path.dirname(os.path.join(cwd, zh)), exist_ok=True)
            open(os.path.join(cwd, zh), "w").write(zt)
            written.append(zh)
        return {"ok": True, "structured_output": {"status": "translated", "files_written": written}}
    if kind == "review":
        return {"ok": True, "structured_output": {"status": "reviewed", "files_reviewed": [],
                "files_edited": [], "changes": "no change needed"}}
    return {"ok": True, "structured_output": {}}


def _block(text, heading):
    m = re.search(r"^##\s+" + heading + r"\s*\n(.*?)(?=^##\s)", text, re.S | re.M)
    return (m.group(1).strip() if m else "").strip()


def _write(cwd, rel, obj):
    import json
    p = os.path.join(cwd, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, "w"), indent=2)


def test_card_slug_is_always_valid_kebab():
    import re
    cases = [
        ({"candidate_id": "x1", "title": "OR-Space: A Full-Lifecycle Workspace Benchmark for Agents",
          "source_records": [{"source": "arxiv"}]}, "or-space"),
        ({"candidate_id": "x2", "title": "facebookresearch/meta-agents-research-environments",
          "source_records": [{"source": "github"}]}, "meta-agents-research-environments"),
        ({"candidate_id": "x3", "title": "EpiBench: Can LLMs Understand Epitopes",
          "source_records": [{"source": "arxiv"}]}, "epibench"),
        # a title whose 50-char truncation lands on a hyphen must NOT yield a trailing hyphen
        ({"candidate_id": "x4", "title": ("word " * 12) + "benchmark",
          "source_records": [{"source": "arxiv"}]}, None),
        ({"candidate_id": "2508.01234", "title": "", "source_records": [{"source": "arxiv"}]}, None),
    ]
    kebab = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
    for c, expected in cases:
        s = pipeline._card_slug(c)
        assert kebab.match(s), "invalid slug %r for %r" % (s, c["title"])
        if expected:
            assert s == expected, (s, expected)


def test_phase5_handles_null_structured_output(tmp_path, monkeypatch):
    # reviewers run without a JSON schema, so run_worker returns structured_output=None.
    # Phase 5 aggregation must not crash on that (regression: live fixture-e2e caught this).
    monkeypatch.setattr(pipeline, "run_worker",
                        lambda *a, **k: {"ok": True, "structured_output": None, "result": ""})
    run_dir = str(tmp_path / "rt")
    os.makedirs(os.path.join(run_dir, "phase5"), exist_ok=True)
    ok, r = pipeline.phase5(run_dir, str(tmp_path), ["zh/works/x.md"], pipeline.config())
    assert ok is True and r["edited"] == 0


def test_full_five_phase_orchestration_stubbed(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline, "run_worker", _stub_worker)
    ws = str(tmp_path / "ws")
    art = str(tmp_path / "art")
    summary = fixture_e2e.run(ws, art)
    # every phase passed; the run WOULD open a PR, but smoke mode blocks it and no PR is created
    assert summary["all_phases_passed"] is True
    assert summary["would_open_pr"] is True
    assert summary["pr_creation_disabled_by_smoke_mode"] is True
    assert summary["failed_phase"] is None
    # the fixture card and its Chinese mirror both exist in the isolated workspace
    changed = set(summary["changed_files"])
    assert any(f.startswith("works/") for f in changed)
    assert any(f.startswith("zh/works/") for f in changed)
    # the phase-3 English axes were integrated onto the card (Topics + Activities filled)
    slug = [f for f in changed if f.startswith("works/")][0].split("/")[1][:-3]
    card = open(os.path.join(ws, "works", "%s.md" % slug)).read()
    assert "../topics/scientific_agents.md" in card
    assert "../activities/simulation_scientific_computing.md" in card
    assert "TODO(axis)" not in card


def test_integrator_builds_consistent_two_way_index_from_json(tmp_path):
    """Worker writes ONLY the assignment JSON (no Related Works edits). The deterministic
    integrator must produce a card<->page reverse index that passes validate_axes."""
    import json
    import integrate_english
    import validators
    from conftest import build_mini_repo
    root = build_mini_repo(str(tmp_path), [
        {"slug": "newcard", "title": "NewCard"},   # written with TODO(axis) below
        {"slug": "other", "title": "Other"}])
    # give the new card TODO(axis) placeholder blocks (as the card writer leaves them)
    p = os.path.join(root, "works", "newcard.md")
    t = open(p).read()
    t = re.sub(r"(## Topics\n).*?(\n## )", r"\1TODO(axis)\2", t, flags=re.S)
    t = re.sub(r"(## Activities\n).*?(\n## )", r"\1TODO(axis)\2", t, flags=re.S)
    open(p, "w").write(t)
    # empty target pages
    for axis, f in [("topics", "trajectory_evaluation"), ("activities", "simulation_scientific_computing")]:
        os.makedirs(os.path.join(root, axis), exist_ok=True)
        open(os.path.join(root, axis, f + ".md"), "w").write("# %s\n\n## Related Works\n\n" % f)
    rd = tmp_path / "rt" / "phase3"
    rd.mkdir(parents=True)
    (rd / "topic_assignments.json").write_text(json.dumps(
        {"assignments": [{"slug": "newcard", "topics": ["trajectory_evaluation"]}]}))
    (rd / "activity_assignments.json").write_text(json.dumps(
        {"assignments": [{"slug": "newcard", "activities": ["simulation_scientific_computing"],
                          "na_reason": None}]}))
    integrate_english.run(str(tmp_path / "rt"), root)
    card = open(p).read()
    assert "../topics/trajectory_evaluation.md" in card and "TODO(axis)" not in card
    assert "../activities/simulation_scientific_computing.md" in card
    ok, errs = validators.validate_axes(root)
    assert ok, errs
