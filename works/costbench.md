# CostBench (2025)

> **English** | [简体中文](../zh/works/costbench.md)

## Overview

CostBench evaluates whether LLM tool-use agents can plan for **cost-optimality** and adapt when the environment blocks the cheapest path. Cost is not reported as a post-hoc statistic; it is the objective the agent is being asked to optimize.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — evaluates an agent meta-property (cost, safety, or robustness), not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2511.02734>

## Summary

CostBench frames tool-use planning as a multi-turn cost-minimization problem. In a travel-planning domain, the same goal is reachable via multiple sequences of atomic and composite tools with configurable costs. The environment then injects blocking events — tool failures and cost changes — that force the agent to replan mid-trajectory under the same cost objective.

## Tasks

Multi-turn travel-planning scenarios. Each task admits several tool sequences with different costs. Four categories of blocking events perturb the environment during a trajectory.

## Domains

Travel planning, as an instantiation of dynamic tool-use.

## Evaluation

- Whether the agent finds a cost-optimal solution in **static** settings (no perturbation).
- Whether the agent recovers cost-optimality in **dynamic** settings after blocking events.
- Reported result: leading models show roughly a 40% performance drop between static and dynamic conditions.

## Typical Duration

Multi-turn tool-use trajectories, structured for repeated plan / execute / replan cycles.

## Main Contribution

Introduces cost as a first-class evaluation objective — not a side metric — for LLM tool-use agents, and stress-tests the resulting cost-aware planning under mid-trajectory perturbations.

## Key Design Ideas

- Cost is the objective function, not a summary statistic.
- Diverse, customizable tool costs across atomic and composite tools.
- Dynamic environment with four categories of blocking events forces replanning.
- Static-vs-dynamic gap directly quantifies planning robustness.

## Strengths

- Separates cost-optimality from task completion — the two can and do diverge.
- Explicit adaptation stress test via blocking events.
- Surfaces a large (~40%) static-vs-dynamic gap even for strong models, giving a clear signal.

## Limitations

- Repository note: Single-domain instantiation — travel planning. Generalization to other cost-sensitive domains is not directly evaluated.

## Related Works

See [Resource-aware Evaluation](../topics/resource_aware_evaluation.md) for the broader landscape.
