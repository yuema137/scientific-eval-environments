# TRACE (2026)

## Overview

TRACE (Trajectory-Aware Comprehensive Evaluation) is an evaluation framework for deep research agents that scores whole reasoning trajectories via a hierarchical utility function, and quantifies latent agent capability by measuring the minimum guidance required for success. It ships with DeepResearch-Bench, an accompanying benchmark with controllable task complexity.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.21230>
- **Venue:** WWW 2026

## Summary

TRACE argues that Pass@1-style evaluation creates a "high-score illusion" for deep research agents by ignoring reasoning quality and process efficiency. It introduces a two-component evaluation: a hierarchical trajectory utility function jointly scoring accuracy, efficiency, evidence grounding, and reasoning quality; and a scaffolded-capability assessment that quantifies the minimum guidance needed for successful completion. The paper also releases DeepResearch-Bench, an accompanying benchmark with controllable complexity levels.

## Tasks

DeepResearch-Bench with controllable task complexity levels. Exact task count: TODO(reference).

## Domains

Deep-research agent tasks: web search, evidence collection, retrieval, reasoning, report generation.

## Evaluation

- **Hierarchical Trajectory Utility Function** — joint score over accuracy, process efficiency, evidence grounding, and reasoning quality.
- **Scaffolded Capability Assessment** — quantifies latent agent capability by measuring the minimum guidance required for success.
- Framed as revealing trade-offs across accuracy / efficiency / robustness rather than a single Pass@1 number.

## Typical Duration

Long-horizon multi-step research workflows with repeated retrieval, reasoning, and synthesis.

## Main Contribution

Argues explicitly that trajectories should be first-class evaluation objects for deep-research agents and provides both a utility-function score and a scaffolded-capability protocol to operationalize that view.

## Key Design Ideas

- Trajectory as a first-class evaluation object, not a side output.
- Hierarchical utility function joins several quality dimensions in one score.
- Scaffolded-capability assessment measures the guidance an agent needs, rather than assuming Pass@1 is representative of capability.
- Controllable-complexity DeepResearch-Bench for calibrated stress testing.

## Strengths

- Separates capability from Pass@1 by measuring guidance dependence.
- Joint utility function surfaces trade-offs a single-metric leaderboard hides.
- Controllable complexity enables calibrated evaluation.

## Limitations

- Repository note: Hierarchical utility scoring relies on judges (model or human) for reasoning-quality and evidence-grounding components.

## Related Works

- [FinTrace](./fintrace.md) — Also multi-dimensional trajectory evaluation, in finance rather than deep research.
- [AgentBoard](./agentboard.md) — Trajectory evaluation via subgoal progress rate rather than a hierarchical utility function.
