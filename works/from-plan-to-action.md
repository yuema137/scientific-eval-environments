# Evaluating Plan Compliance in Autonomous Programming Agents (2026)

> **English** | [简体中文](../zh/works/from-plan-to-action.md)

> **First appeared:** 2026-04-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2604.12147)

## Overview

A systematic empirical analysis of *plan compliance* in programming agents: whether coding agents that are instructed to follow a task-specific plan actually follow it, and how deviations relate to task success. The study analyzes SWE-agent trajectories across four LLMs and two SWE-bench suites under eight plan variations, and introduces metrics that quantify how faithfully an agent's trajectory adheres to the instructed plan. The paper was first posted as "From Plan to Action: How Well Do Agents Follow the Plan?" and later retitled "Evaluating Plan Compliance in Autonomous Programming Agents."

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


N/A — Plan-compliance evaluation methodology over coding-agent trajectories; measures adherence metrics, not an evaluated scientific/research task.

## Links

- **Paper:** <https://arxiv.org/abs/2604.12147>
- **Venue:** arXiv preprint (cs.SE), 2026 (submitted 13 April 2026; revised 7 August 2026)
- **Authors:** Shuyang Liu, Saman Dehghan, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand (University of Illinois Urbana–Champaign; IBM)

## Summary

Programming agents are commonly given a task-specific plan for guidance, but the extent to which they comply with such plans has not been measured. This work presents an extensive analysis of plan compliance in programming agents, examining 16,991 SWE-agent trajectories across four LLMs on SWE-bench Verified and SWE-bench Pro under eight plan settings. It reports that, without an explicit plan, agents fall back on internalized workflows that are often incomplete, overfit, or inconsistently applied; providing the standard plan improves issue resolution; periodic plan reminders can mitigate plan violations and improve task success; a subpar plan can hurt performance more than no plan at all; and inserting additional task-relevant phases early can degrade performance when they do not align with the model's internal problem-solving strategy. The authors attribute deviation in part to plan salience decaying as the trajectory history grows and to the agent's locally-conditioned, feedback-driven action selection.

## Tasks

Resolving real-world GitHub issues by editing a repository's codebase, run through the SWE-agent scaffold. The evaluated instances are drawn from SWE-bench Verified (all 500 instances) and SWE-bench Pro (266 Python instances). Each agent run is instructed with one of eight plan settings, and its resulting trajectory is scored for compliance with the instructed plan.

## Domains

Software engineering — resolving issues in real open-source software repositories via an autonomous coding agent.

## Evaluation

- **Testbed.** SWE-agent scaffold over four LLMs: GPT-5 mini, DeepSeek-V3, DeepSeek-R1, and Devstral-small. Benchmarks: SWE-bench Verified (500 instances) and SWE-bench Pro (266 Python instances).
- **Plan settings (eight).** (1) default/standard plan, (2) no plan, (3) plan with the reproduction phase removed, (4) plan with the validation phase removed, (5) plan augmented with regression-test phases, (6) plan augmented with a change-summarization phase, (7) step reordering, and (8) plan reminder (periodic re-injection of the plan).
- **Compliance metrics.** Plan Phase Compliance (PPC), Plan Order Compliance (POC), and Plan Phase Fidelity (PPF); an overall compliance score is reported as the geometric mean of the three components.
- **Outcome metric.** Issue-resolution success (SWE-bench-style patch verification against the repository's test suite), compared across plan settings.
- **Reported directions.** Providing the standard plan improves issue resolution relative to no plan; periodic plan reminders reduce plan violations and improve success; a subpar plan can reduce performance below the no-plan baseline; adding task-relevant early phases can degrade performance. Specific per-model success rates are TODO(reference).

## Typical Duration

TODO(reference) — the paper reports trajectory-level analysis but does not state a per-task wall-clock or step-count duration in the material reviewed.

## Main Contribution

An extensive, systematic measurement of plan compliance in programming agents — defining plan-compliance metrics (PPC, POC, PPF) and using 16,991 SWE-agent trajectories under eight plan variations to characterize when and why agents deviate from instructed plans and how compliance relates to task success.

## Key Design Ideas

- Decompose plan compliance into three measurable dimensions — phase coverage (PPC), phase ordering (POC), and per-phase fidelity (PPF) — aggregated by geometric mean.
- Vary the instructed plan along eight controlled settings (removal, augmentation, reordering, reminders, and a no-plan baseline) to isolate the effect of plan content and structure on both compliance and success.
- Run the same scaffold (SWE-agent) across four LLMs on two SWE-bench suites so that plan effects can be separated from model and benchmark effects.

## Strengths

- Large trajectory corpus (16,991 trajectories) spanning four LLMs, two benchmarks, and eight plan settings.
- Introduces explicit, decomposed metrics for plan adherence rather than measuring only end-task success.

## Limitations

- Scoped to the SWE-agent scaffold and to SWE-bench Verified / SWE-bench Pro issue-resolution tasks; generalization to other scaffolds or task types is not established by the study.
- Repository note: the first arXiv version reported a larger trajectory count (21,120) under the original title; the figures in this card follow the revised version (16,991 trajectories, eight plan settings). Per-model success rates and exact compliance scores were not captured here and are marked TODO(reference).

## Related Works

- [SWE-bench](./swe-bench.md)
