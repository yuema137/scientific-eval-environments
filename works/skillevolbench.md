# SkillEvolBench (2026)

> **English** | [简体中文](../zh/works/skillevolbench.md)

## Overview

SkillEvolBench is a diagnostic benchmark for the step from experience reuse to skill formation: whether an LLM agent can distil its own episodic trajectories into reusable procedural skills that still work when the skill library is frozen and the tasks shift.

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2605.24117>
- **Project:** <https://skillevolbench.github.io/>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

The benchmark separates two phases. In acquisition, the agent solves learning tasks and updates an external skill library from compacted execution artifacts paired with verifier feedback. In deployment, the library is frozen and the agent may read but not modify it, facing held-out tasks that probe context shift, adversarial shortcuts, and composition. Four conditions — no-skill, raw-trajectory reuse, self-generated skills, and a curated-start seed library — are compared so that procedural abstraction can be separated from base capability, from prior curated knowledge, and from direct reuse of episodic traces. Across ten model configurations and three agent harnesses the paper reports that agents adapt locally but rarely form robust reusable skills, and that raw-trajectory reuse frequently outperforms the distilled skills derived from those same trajectories.

## Tasks

180 tasks across six real-world agent environments: code debugging and modification, tool and API orchestration, data processing and structured query, document parsing and transformation, research and information synthesis, and communication and scheduling. Tasks are organised into role-conditioned task families that share a latent procedure — five families per environment, six tasks per family (three acquisition tasks: canonical, enriched, variant; three frozen deployment tasks: context-shift, adversarial, composition). The skill library follows the SKILL.md convention with optional bundled resources under `scripts/`, `references/`, and `assets/`; a Tier-3 ablation makes resource bundling mandatory.

## Domains

General-purpose agent environments (software, tooling, data, documents, information synthesis, communication). No canonical science or engineering domain is targeted; the evaluated object is procedural skill formation, not a scientific task.

## Evaluation

- Per-phase success rates: LSR (acquisition/learning), RSR (replay of the same tasks under a frozen library), and ESR (frozen deployment evaluation).
- ESR is decomposed by deployment axis into CSSR (context shift), ARSR (adversarial shortcuts), and CompSR (composition).
- Every skill condition is reported as a delta against the no-skill and raw-trajectory controls, so that gains attributable to abstraction are distinguished from gains attributable to having any memory at all.
- **Reported.** Self-generated skill conditions can lift acquisition and replay while showing negative deltas on frozen deployment; per-model leaderboard values are TODO(reference).

## Typical Duration

No step or token cap is reported. Cost per attempted task is reported in USD on a log scale; curated variants average **+$0.077** and Tier-3 ablations **+$0.119** per attempted task relative to their baselines.

## Main Contribution

A controlled testbed that isolates *procedural abstraction* as the measured quantity, by pairing a frozen-library deployment phase with raw-trajectory and curated-start controls — turning "did the agent learn a skill?" into a difference between conditions rather than an aggregate score.

## Key Design Ideas

- Freezing the skill library at deployment time, so that measured gains cannot come from continued in-task adaptation.
- Role-conditioned task families with a shared latent procedure, which gives abstraction something specific to recover.
- A raw-trajectory control: the same episodic evidence supplied undistilled, which turns out to be a strong baseline.
- Three deployment axes (context shift, adversarial shortcuts, composition) that test different failure modes of a written skill.
- Capacity and cost ablations testing whether writing more skills or bundling larger resource libraries helps.

## Strengths

- The control design makes a negative result interpretable: distillation can be shown to lose information relative to the traces it summarises.
- Runs across three independent agent harnesses, so conclusions are not tied to one skill-library implementation.
- Reports monetary cost alongside success, exposing that extra skill writing buys coverage at a price.

## Limitations

- The paper's own diagnosis is that current abstraction procedures are lossy and that usefulness depends on the base model's ability to interpret and apply written skills; it does not propose a fix.
- Environments are general agent workflows; the benchmark says nothing about whether procedural abstraction behaves the same way on scientific or engineering tasks.
- Repository note: card compiled from the arXiv abstract and the v1 full text (August 2026); specific per-model success rates are left as TODO(reference) pending direct table validation.

## Related Works

- [Skill-Use](./skill-use.md) — Evaluates the use of pre-authored skills; SkillEvolBench evaluates whether the agent can write them in the first place.
- [SkillSV](./skillsv.md) — Values the internal units of an existing skill, complementary to measuring whether a skill was worth writing.
- [GATE](./gate.md) — Also concerns constructing reusable capability artifacts from experience, via a hierarchical tool graph rather than a written skill library.
- [HarnessOpt-Bench](./harnessopt-bench.md) — Also scores an agent's ability to improve its own surrounding artifact, at the harness level rather than the skill level.
- [AgentBoard](./agentboard.md) — Shares the commitment to progress-level rather than terminal-only signal in multi-step agent tasks.
