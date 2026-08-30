# SkillLearnBench (2026)

> **English** | [简体中文](../zh/works/skilllearnbench.md)

## Overview

SkillLearnBench is a benchmark for continual skill-learning methods — approaches that generate agent skills automatically from an agent's own execution experience — scoring not only whether the task is solved but the quality of the generated skill itself.

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — general-purpose agent benchmark over real-world task categories; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2604.20087>
- **Code:** <https://github.com/cxcscmu/SkillLearnBench>
- **Venue:** COLM 2026

## Summary

Skills — customized instructions, workflows and tools — have become the standard way to extend LLM agents, but how to learn them automatically remains unresolved. SkillLearnBench evaluates continual learning methods that produce skills from agent experience, over skill-dependent tasks derived from a real-world skill taxonomy, at three levels: skill quality, execution trajectory, and task outcome. The evaluation covers one-shot generation, self-feedback and teacher-feedback refinement, and a skill-creator pipeline, and finds that while every method beats a no-skill baseline, none dominates across tasks and backbones.

## Tasks

The repository states the scope as "20 skill-dependent tasks · 15 sub-domains · 100 verified instances"; the paper describes them as 20 verified, skill-dependent tasks across 15 sub-domains derived from a real-world skill taxonomy. Tasks are selected so that success depends on holding the relevant skill, which is what makes the generated skill the object under test.

## Domains

Real-world agent task categories drawn from a skill taxonomy; the sub-domains are not enumerated as science or engineering fields in the abstract or repository summary, so no canonical domain is assigned.

## Evaluation

Three evaluation levels:

- **Task outcome** — pass rate.
- **Skill quality** — functional coverage, executability, and safety of the generated skill.
- **Trajectory quality** — key-point recall, execution order, and completeness.

Four continual-learning baselines are implemented: One-Shot (single-pass skill generation), Self-Feedback (iterative refinement via execution review), Teacher-Feedback (expert-guided improvement), and Skill Creator. The repository lists the evaluated backbones as "claude-haiku-4-5, claude-sonnet-4-6, and claude-opus-4-6; gemini-3.1-flash-lite-preview, gemini-3-flash-preview, and gemini-3.1-pro-preview".

**Reported.** All continual learning methods improve over the no-skill baseline, but consistent gains remain elusive: no method leads across all tasks and LLMs, and scaling to stronger LLMs does not reliably help. Continual learning improves tasks with clear, reusable workflows but struggles on open-ended tasks. Multiple iterations facilitate genuine improvement via external feedback, whereas self-feedback alone induces recursive drift.

## Typical Duration

TODO(reference) — the abstract reports no per-task wall-clock or token budget; continual-learning baselines are run over multiple iterations.

## Main Contribution

Presented by the authors as the first benchmark for evaluating continual skill learning methods, shifting the measured object from task success to the automatically generated skill artifact and the trajectory that produced it.

## Key Design Ideas

- Tasks are chosen to be *skill-dependent*, so a weak generated skill cannot be masked by a strong backbone solving the task unaided.
- Three-level scoring separates the quality of the induced artifact from the process and from the outcome.
- Skill quality is itself decomposed into functional coverage, executability, and safety rather than judged holistically.
- The baseline set spans the feedback spectrum — none, self, teacher, and a structured creator pipeline — isolating the contribution of the feedback source.

## Strengths

- Scores the induced skill directly, not merely the downstream task it enables.
- Distinguishes genuine iterative improvement from recursive drift under self-feedback, a failure mode invisible to outcome-only evaluation.
- Data and code are open-source.

## Limitations

- 20 tasks (100 verified instances) is a small suite for claims about method ranking across backbones.
- Backbone coverage is limited to two model families.
- Repository note: the benchmark's subject is skill *induction from experience* rather than the decomposition-and-per-subskill-scoring pattern that defines most of the Skill Hierarchy topic; it is filed there as the closest existing home for evaluation of skill artifacts.
- Repository note: card compiled from the arXiv abstract, metadata, and the official repository README (August 2026); numbers beyond those quoted await full-paper validation.

## Related Works

- [SkillSV](./skillsv.md) — Also evaluates the internal quality of a skill artifact, by attribution over a fixed skill rather than over generated ones.
- [Skill-Use](./skill-use.md) — Also uses skill-dependent executable tasks, to measure skill *use* rather than skill *generation*.
- [GATE](./gate.md) — Also concerns constructing reusable capability artifacts from agent activity, as a graph-based tool-evolution framework rather than a benchmark.
- [SkillJuror](./skilljuror.md) — Also evaluates properties of the skill artifact itself, for authored organization rather than automatic generation.
