# AgentBoard (2024)

## Overview

AgentBoard is a multi-turn LLM-agent evaluation benchmark paired with an analytical dashboard. Its central design commitment is that agent evaluation should not collapse to a binary success rate: performance is instead measured by a *fine-grained progress rate* over annotated subgoals in partially observable environments.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- Skill Hierarchy *(topic page pending)*

## Links

- **Paper:** <https://arxiv.org/abs/2401.13178>
- **Project:** <https://hkust-nlp.github.io/agentboard/>
- **Venue:** NeurIPS 2024 (oral)

## Summary

AgentBoard argues that most agent benchmarks reward only the final task outcome and therefore reveal little about how an agent fails or progresses. The framework provides a unified evaluation setup across four task families and augments it with an analytical dashboard for slicing performance beyond aggregate success rate.

## Tasks

1,013 environments across 9 task types. Every task carries annotated subgoals used by the progress-rate metric.

## Domains

Embodied AI, game agents, web agents, and tool-use agents. Environments are partially observable and multi-turn.

## Evaluation

- **Progress rate**: fraction of annotated subgoals completed within a trajectory. Primary metric.
- **Success rate**: retained as a coarse baseline for comparability with prior benchmarks.
- **Grounding accuracy**: measured alongside progress and success.
- **Analytical dashboard**: supports filtering by task family and capability dimension.

## Typical Duration

Multi-turn interactions per task; horizon is defined by the subgoal chain rather than by a fixed step budget.

## Main Contribution

A fine-grained, subgoal-based progress metric for multi-turn LLM agents, together with an analytical framework that treats trajectory-level dissection — not just final success — as a first-class evaluation output.

## Key Design Ideas

- Every task is annotated with a chain of subgoals.
- Progress rate complements, rather than replaces, binary success.
- Partially observable environments are treated as the default, not the exception.
- Post-hoc analysis via a dedicated dashboard is part of the deliverable.

## Strengths

- Distinguishes "made significant progress" from "failed entirely," which binary success cannot.
- Cross-family breadth (embodied, game, web, tool) under a shared metric.
- Public dashboard supports comparative and diagnostic analysis rather than only leaderboard ranking.

## Limitations

- Repository note: Subgoal annotation is a manual authoring cost — extending the benchmark to new task families requires human decomposition.

## Related Works

- [T-Eval](./t-eval.md) — Also decomposes evaluation below end-task success, but along tool-use capability subprocesses rather than task subgoals.
