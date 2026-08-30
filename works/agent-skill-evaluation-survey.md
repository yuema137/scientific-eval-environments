# Agent Skill Evaluation and Evolution: Frameworks and Benchmarks (2026)

> **English** | [简体中文](../zh/works/agent-skill-evaluation-survey.md)

> **First appeared:** 2026-06-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.11435)

## Overview

A survey of how agent skills are evaluated and evolved once they exist, organising the literature into four skill-evolution paradigms and six categories of skill-centric benchmark, and identifying structural gaps in benchmark coverage.

## Topics

- [Survey](../topics/survey.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — survey; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.11435>
- **Code:** <https://github.com/Cassie07/AgentSkill_Survey>
- **Venue:** arXiv preprint, 2026

## Summary

The survey's thesis is that the field is shifting from isolated skill creation toward automated, evaluation-driven skill evolution, and that as skill libraries scale, rigorous evaluation becomes the mechanism for ensuring their utility, quality, and safety. It reviews the landscape beyond foundational skill creation along two axes: how skills are improved after creation, and how skills are measured. It closes with open directions for building skill ecosystems that are generalisable, efficient, and verifiably safe.

## Tasks

N/A — survey; it contributes no task suite.

## Domains

General LLM-agent skill ecosystems. No science or engineering domain is targeted.

## Evaluation

N/A — survey; it contributes no scoring protocol. It does, however, analyse existing protocols by benchmark category, comparing coverage, trade-offs, and metric richness.

## Typical Duration

N/A — survey.

## Main Contribution

A structured map of the post-creation skill lifecycle: a four-way taxonomy of evolution paradigms paired with a six-way taxonomy of skill-centric benchmarks, used to locate structural gaps in what current benchmarks measure.

## Key Design Ideas

- Evolution paradigms are separated by the *granularity of the signal they consume*: execution feedback (single-run, step-level signals such as runtime errors and incorrect outputs), trajectory distillation (multi-run, sequence-level patterns), compression and augmentation (library-level structure), and reinforcement learning (task-level rewards).
- Benchmarks are categorised by what they measure rather than by domain: skill utility, skill generation, skill retrieval and routing, skill safety auditing, software engineering, and real-world environments.
- Benchmark analysis is framed around coverage gaps and metric richness rather than leaderboard comparison.
- Open directions are grouped as multimodal skills, trajectory data distillation, and agent-skill security.

## Strengths

- Distinguishes skill *generation* benchmarks from skill *utility* benchmarks, which is the distinction most single benchmarks blur.
- Provides a citable index of a fast-moving benchmark family, including retrieval/routing and safety-auditing lines that are easy to miss.
- Companion repository gives an updatable reference list.

## Limitations

- The survey does not state how many papers or benchmarks it covers, so its coverage claim cannot be checked from the text.
- Category boundaries are descriptive; the survey does not evaluate whether the six benchmark categories are separable in practice.
- Repository note: card compiled from the arXiv abstract and the v1 full text (August 2026). Several benchmarks it indexes are not yet in this repository and are candidates for follow-up.

## Related Works

- [Skill-Use](./skill-use.md) — An instance of the skill-utility benchmark category the survey identifies.
- [SkillEvolBench](./skillevolbench.md) — An instance of the trajectory-distillation evolution paradigm the survey identifies, evaluated as a benchmark.
- [SkillAudit](./skillaudit.md) — An instance of the skill safety-auditing category.
- [SkillSV](./skillsv.md) — Relates to the compression-and-augmentation paradigm, valuing skill units to guide pruning.
- [Agent Evaluation Survey](./agent-evaluation-survey.md) — Broader survey of LLM-agent evaluation, of which skill evaluation is one slice.
