# SkillLens (2026)

> **English** | [简体中文](../zh/works/skilllens.md)

> **First appeared:** 2026-05-08 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.08386)

## Overview

SkillLens is a skill-reuse method that represents an agent's skills at four granularities (policies, strategies, procedures, primitives) and decides, unit by unit, which level to reuse, break down, or rewrite for a new task. Flat skill libraries force a choice between injecting a whole skill, which can bring irrelevant context, and rewriting it entirely, which costs tokens. SkillLens has an LLM verifier walk the skill graph and accept compatible sub-skills, rewrite only mismatched units, and periodically edits the verifier's routing rules using failure reports scored against a correctness-minus-cost objective. Its evaluation compares accuracy and token/time cost against rewrite-all and parent-only adaptation on MuLocbench and ALFWorld.

## Topics


- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities


N/A — Skill-reuse method evaluated on general repository bug localization and text-based embodied tasks; no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2605.08386>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

For a new query, SkillLens retrieves skill seeds by embedding similarity, expands them with a degree-corrected random walk with restart, and partitions candidates into fully compatible, partially relevant, and mismatched tiers. For each partially relevant unit, the verifier (GPT-5-mini) emits one action: accept (keep the unit and stop), decompose (push its children for evaluation), rewrite (have the writer adapt the unit locally), or skip. During evolution, each task with correctness M < 1 produces a gap report (error type, retrieved skills, traversal path, routing actions, rewritten units); the writer proposes single edits to the verifier's textual registry, and the candidate maximizing J(𝒮) = E[M − C] (correctness minus normalized cost) is committed. The paper's cost guarantee assumes that mismatches between a skill and a task are sparse.

## Tasks

N/A as a benchmark — SkillLens is a skill-reuse method evaluated on:

- **MuLocbench** — repository bug localization at file, module, and function granularity; 36 training and 10 test repositories (issue counts TODO(reference)).
- **ALFWorld** — text-based embodied tasks, at most 50 steps per episode; training split used for evolution and validation, valid-seen split for testing (split sizes TODO(reference)).

The skill library is initialized from antigravity-awesome-skills. Agent and writer: Codex GPT-5.2; verifier: GPT-5-mini; retrieval embedding: text-embedding-3-small.

## Domains

Software engineering (repository bug localization) and text-based embodied household tasks.

## Evaluation

- **Inside the loop.** Evolution tasks are scored with the benchmark metric M ∈ [0, 1]; failures generate gap reports, and registry edits are chosen by J = E[M − C]. Appendix A.4 describes a 7:3 evolution/validation split with the best validated version used for one final test run; Algorithm 2 selects by J on the evolution set.
- **MuLocbench.** Accuracy, Recall, and Precision at @1/@3/@5/@10, at file, module, and function level. Reported Acc@1 against the no-skill (Vanilla) agent: file 61.13 vs 58.87, module 59.26 vs 55.56, function 43.68 vs 37.37 (+6.31 pp). A parent-only adaptation variant scores higher at file (61.51) and function (45.79) level.
- **ALFWorld.** Episode success rate: SkillLens 51.31 vs Vanilla 45.00, AutoSkill 47.14, EvoSkill 47.14.
- **Cost comparison (MuLocbench).** Rewrite-all: 6,161.83 s, 115.51M tokens; parent-only: 5,257.82 s, 78.35M tokens; SkillLens: 4,718.54 s, 16.41M tokens.
- **Library-size scaling.** As the initial skill ratio rises from 25% to 100%, retrieval time rises from 18.28 to 58.72 minutes and main-agent tokens from 3.17M to 3.89M.

## Typical Duration

ALFWorld episodes are capped at 50 steps. On MuLocbench, the full SkillLens run takes 4,718.54 s and 16.41M tokens in the reported cost comparison.

## Main Contribution

The authors propose organizing skills as a four-layer graph and adapting them at mixed granularity under a verifier that routes each unit, with a theoretical argument that mixed-granularity adaptation has sublinear cost under sparse mismatch and that the evolutionary registry update monotonically improves the validation objective until a local optimum.

## Key Design Ideas

- Four-layer skill hierarchy: policies, strategies, procedures, primitives.
- Retrieval tiers from calibrated degree-corrected random-walk scores, so only partially relevant skills pay for verifier traversal.
- Four per-unit routing actions (accept, decompose, rewrite, skip) instead of a single whole-skill decision.
- The evolved object is a textual verifier registry, edited with single operators (Add, Del, Upd, Mrg) and kept with a fallback to the current version.
- The objective subtracts normalized cost from correctness, so evolution trades accuracy against adaptation cost.

## Strengths

- Compares three adaptation granularities (rewrite-all, parent-only, mixed) on both accuracy and token/time cost.
- Reports accuracy at three localization granularities, showing where the method does and does not lead.
- States its theoretical assumptions alongside the propositions.

## Limitations

- Two task families, both English-centric; multimodal, multilingual, and safety-critical settings are untested.
- Results depend on the initial skill library and on the verifier's routing; noisy skills can trigger unnecessary decomposition or rewriting, and the four-level ontology may not fit every domain.
- One agent/writer model family, one verifier, and one embedder.
- Verifier calls and registry maintenance add overhead relative to a no-skill agent; long-run library growth is not studied.
- The verifier's decision criteria and prompt are not specified, and the weighting of cost against correctness in J is not stated.
- Repository note: results are single runs without variance or significance tests, and the appendix and Algorithm 2 describe the validation-based selection differently. Card compiled from the arXiv abstract and v2 HTML full text (November 2026).

## Related Works

- [Break It Down, Pass It On](./break-it-down-pass-it-on.md) — Also shows that the granularity at which skills are reused changes whether they help.
- [SkillSV](./skillsv.md) — Also works on units inside a skill, valuing them rather than routing them.
- [SkillShapley](./skillshapley.md) — Attributes credit to steps inside a skill, a finer-grained view of which skill parts matter.
- [GATE](./gate.md) — Also builds a hierarchical structure over reusable agent capabilities, as a tool graph rather than a skill graph.
