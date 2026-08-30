# Agent Planning Benchmark (2026)

> **English** | [简体中文](../zh/works/agent-planning-benchmark.md)

> **First appeared:** 2026-06-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.04874)

## Overview

Agent Planning Benchmark (APB) is a planning-specific diagnostic benchmark with 4,209 multimodal cases across 22 domains and five settings, separating complete-plan generation from feedback-conditioned next-step planning and robustness to tool or task defects.

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — general multimodal and tool-use planning benchmark spanning heterogeneous non-research tasks.

## Links

- **Paper:** <https://arxiv.org/abs/2606.04874>
- **Code:** <https://github.com/Mikivishy/AgentPlanningBenchmark>
- **Venue:** arXiv preprint (2026)

## Summary

APB is motivated by the inability of end-to-end success rates to tell planning failures from execution failures. It evaluates holistic plans produced before execution, one- to three-step decisions conditioned on trajectory feedback, planning with extraneous tools, recovery when a critical tool is broken but a substitute exists, and refusal when constraints make a task unsolvable. Across 12 multimodal LLMs, the paper reports a consistent gap between feedback-conditioned step-wise planning and holistic planning, along with sensitivity to distractor tools and incomplete information.

## Tasks

4,209 cases assembled from FrameThinker, GAIA, GTA, OpenCUA, ToolBench, and other agent-task sources across 22 domains. The five settings comprise 1,109 holistic cases, step-wise planning cases derived from execution trajectories, 1,500 extraneous-tool cases, 300 broken-tool cases, and 400 unsolvable cases. Step-wise evaluation asks for the next one, two, or three actions from the current state and observed feedback; holistic evaluation asks for a complete tool-and-action plan without intermediate observations.

## Domains

Twenty-two heterogeneous multimodal and tool-use domains, including web, mobile, desktop, information, finance, visual, and general assistant tasks. The paper does not provide a per-case mapping suitable for conservative assignment to this repository's canonical science and engineering domains.

## Evaluation

APB reports binary Plan Correctness, Plan Grade on a six-level 0–1 scale, and an E1–E6 error taxonomy covering goal understanding, premature conclusion or incompleteness, constraint violation, logic, tool use, and hallucination. A reference-aware LLM-as-a-judge protocol applies the rubric; dataset construction combines rule checks, two-stage model validation, and human verification. The paper also validates APB-guided refinement on 200 ToolSandbox and 200 τ²-bench tasks to test whether improved plans transfer to downstream execution metrics.

## Typical Duration

Offline plan generation rather than full benchmark execution. Step-wise cases predict one to three upcoming actions from a trajectory prefix; holistic cases generate a complete plan in one pass. No common wall-clock budget is defined across the heterogeneous source tasks.

## Main Contribution

A planning-only diagnostic layer that evaluates global and local decision quality upstream of execution, with controlled robustness settings that expose tool-selection, recovery, and calibrated-refusal failures.

## Key Design Ideas

- Separate holistic planning from feedback-conditioned step-wise planning.
- Add semantically plausible but functionally irrelevant tools to test selective tool use.
- Replace a broken critical tool with a differently named alternative to test recovery.
- Construct contradictory, information-missing, tool-missing, and visually inaccessible tasks that should be rejected.
- Pair aggregate correctness with graded severity and named failure categories.

## Strengths

- The design directly targets the planning-versus-execution confound.
- Local and global planning are evaluated under distinct information conditions.
- Robustness variants turn tool noise, failure recovery, and infeasibility recognition into controlled test settings.
- Downstream validation checks whether diagnostic improvement can translate into execution improvement.

## Limitations

- Most plan scoring relies on an LLM judge, although construction and validation include rule-based and human checks.
- The benchmark aggregates tasks from heterogeneous sources, so domain-specific scientific validity is not its focus.
- Step-wise correctness requires a reasonable progressing action but does not measure whether it is optimal relative to all available alternatives.

## Related Works

- [PlanBench](./planbench.md) — provides solver-backed plan validity and optimality in formal domains.
- [NATURAL PLAN](./natural-plan.md) — isolates planning with full information but does not test feedback-conditioned next actions.
- [TravelPlanner](./travelplanner.md) — evaluates planning and execution jointly in a constrained tool environment.
- [Plan-RewardBench](./plan-rewardbench.md) — benchmarks evaluators that rank complete tool-use trajectories, including hard planning pairs.
