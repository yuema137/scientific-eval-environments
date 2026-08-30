# SkillJuror (2026)

> **English** | [简体中文](../zh/works/skilljuror.md)

> **First appeared:** 2026-06-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.11543)

## Overview

SkillJuror is an evaluation framework that isolates *how an agent Skill is organized* from *what it says*, comparing a Progressive Disclosure layout (a concise root file pointing to supporting resources on demand) against a normalized flat baseline while holding task knowledge fixed.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — general-purpose agent-skill evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.11543>
- **Venue:** arXiv preprint, 2026

## Summary

Agent Skills supply LLM agents with procedural knowledge at inference time, but benchmarks that report only task success cannot separate a Skill's content from its organization. SkillJuror constructs semantically controlled variants of the same Skill, runs matched multi-trial evaluations, and inspects trajectory evidence, so that any measured difference is attributable to the layout rather than to the knowledge. Applied to an 82-task SkillsBench study, the framework finds that Progressive Disclosure changes runtime behavior before it changes aggregate outcomes.

## Tasks

An 82-task study on SkillsBench, with each task run under semantically controlled Skill variants (Progressive Disclosure versus a normalized flat baseline) in matched multi-trial configurations totalling 410 matched trials. The variant construction procedure holds the underlying task knowledge fixed so that only organization differs.

## Domains

Agent Skills as structured artifacts for general-purpose LLM agents; the paper does not scope its tasks to a science or engineering field, so no canonical domain is assigned.

## Evaluation

- **Trajectory-level behavior metrics.** Distinct Skill resources touched per trajectory, and effective uptake events per trajectory.
- **Outcome metric.** Verifier-passing trials over matched trial pairs.
- **Reported.** Distinct Skill resources touched per trajectory rise from 1.18 to 3.85 and effective uptake events rise from 1.33 to 3.92 under Progressive Disclosure; it yields 17 additional verifier-passing trials out of 410 matched trials (+4.1%) over the normalized flat baseline.
- The benefit is reported as task-dependent: Progressive Disclosure helps when supporting resources guide implementation, checking, or repair, and is weaker when success hinges on exact output conventions, numerical thresholds, or long artifact-generation pipelines.

## Typical Duration

TODO(reference) — the abstract reports trial counts but no per-task wall-clock or token budget.

## Main Contribution

A controlled evaluation protocol for Skill *writing paradigms*, showing that Skill organization is not mere presentation: it measurably changes how agents search for and apply procedural knowledge, with outcome gains contingent on whether the exposed resources are actionable.

## Key Design Ideas

- Semantically controlled Skill variants hold task knowledge constant so layout is the only manipulated factor.
- Matched multi-trial evaluation pairs trials across variants rather than comparing aggregate leaderboards.
- Trajectory evidence (resources touched, uptake events) is treated as the primary signal, with aggregate success as a secondary, lagging indicator.

## Strengths

- Separates content from organization, a distinction most skill benchmarks conflate.
- Reports process-level effects that are visible even where end-task success is not yet moved.
- States the boundary conditions under which the studied layout does not help.

## Limitations

- Compares two layouts (Progressive Disclosure and a normalized flat baseline) rather than surveying a space of organizational paradigms.
- Built on a single host benchmark (SkillsBench, 82 tasks), so the generality of the effect across harnesses and task families is untested.
- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [Skill-Use](./skill-use.md) — Also treats skills as first-class evaluation objects, scoring the agent's use of a skill rather than the skill's layout.
- [SkillSV](./skillsv.md) — Also targets a skill's internal structure, valuing its units rather than comparing organizational paradigms.
- [SkillTV-Bench](./skilltv-bench.md) — Also evaluates in the skill-augmented setting, on the judge side rather than the executing agent.
- [Harness-Bench](./harness-bench.md) — Also shows that scaffolding choices, not just the model, materially change measured capability.
