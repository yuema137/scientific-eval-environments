# SkillTV-Bench (2026)

> **English** | [简体中文](../zh/works/skilltv-bench.md)

> **First appeared:** 2026-08-06 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.05573)

## Overview

SkillTV-Bench is a benchmark for skill-aware trajectory verification: it evaluates how well LLM-as-a-Judge and Agent-as-a-Judge methods verify agent executions that use skills. It comprises 681 real agent trajectories from 50 tasks across eleven domains, and is accompanied by SkillTV-Evolve, which externalizes verification knowledge as a reusable JudgeSkill.

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.05573>
- **Venue:** arXiv preprint, 2026

## Summary

SkillTV-Bench measures trajectory verification when agent executions are skill-augmented — a setting where the judge needs task-aware skill knowledge to verify correctly. SkillTV-Evolve runs an automated evolution loop over misjudged cases and distills the resulting verification knowledge into a reusable JudgeSkill, which raises the same agent judge's accuracy by 14.8 percentage points and lifts offline rollout-pool selection from 22.9% selected-trajectory success with one rollout to 45.5% with ten.

## Tasks

681 real agent trajectories drawn from 50 distinct tasks spanning eleven domains.

## Domains

Eleven domains; the abstract does not enumerate them.

## Evaluation

- Judge accuracy for LLM-as-a-Judge and Agent-as-a-Judge methods on skill-augmented executions.
- Offline rollout-pool selection: success rate of the judge-selected trajectory as the rollout pool grows.
- **Reported.** The refined JudgeSkill increases the same agent judge's accuracy by 14.8 percentage points, and selected-trajectory success rises from 22.9% (one rollout) to 45.5% (ten rollouts).

## Typical Duration

Post-hoc verification of completed agent trajectories.

## Main Contribution

Puts the judge, not the agent, on the bench for skill-augmented execution, and shows verification knowledge itself can be externalized as a reusable skill.

## Key Design Ideas

- Skill-augmented execution changes what a judge must know; the benchmark makes that knowledge requirement explicit.
- Misjudged cases drive an evolution loop whose product is a portable JudgeSkill rather than a fine-tuned model.
- Verification quality is also measured by its downstream effect on best-of-n trajectory selection.

## Strengths

- Real trajectories rather than synthetic verification puzzles.
- Quantifies the gap between judging plain and skill-augmented executions.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [AgentRewardBench](./agentrewardbench.md) — Also benchmarks trajectory judges against ground truth, for web agents without skill augmentation.
- [Plan-RewardBench](./plan-rewardbench.md) — Also scores the judge rather than the agent, via pairwise trajectory preference.
- [Skill-Use](./skill-use.md) — Also evaluates the skill-augmented setting, scoring the executing agent rather than the judge.
