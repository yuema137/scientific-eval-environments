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

DeepResearch-Bench comprises 650 tasks in three subsets: **TRACE-Core** (500 tasks, average complexity C(q) = 3.5, ~20% embedding "information traps"), **TRACE-Robustness** (100 tasks, C(q) = 4.2, all with traps), and **TRACE-Scaffolding** (50 tasks, C(q) = 5.8, 40% with traps). Complexity is a continuous scalar C(q) from a formalism-driven synthesis procedure, not a set of discrete tiers.

## Domains

Deep-research agent tasks: web search, evidence collection, retrieval, reasoning, report generation.

- **Hierarchical Trajectory Utility U(H).** Final-answer accuracy is a hard multiplicative gate on a product of efficiency and cognitive quality — U(H) = 𝟙(answer correct) · E(H)^ω_E · C(H)^ω_C — so a wrong answer zeros the whole utility.
  - **Process Efficiency E(H)** rewards solving more complex tasks while dividing by a trajectory-cost functional, including a *Redundant Exploration Penalty* that down-weights consecutive uninformative actions in proportion to the cosine similarity of successive observation embeddings.
  - **Cognitive Quality C(H) = β·G_E + (1−β)·R_R** combines **Evidence Grounding** G_E — the geometric mean of per-claim NLI entailment probabilities, so a single ungrounded claim collapses the score — and **Reasoning Robustness** R_R — an exponential decay in the number of steps needed to recover after a planted information trap.
  - The geometric-mean design is deliberate: "the research process is only as strong as its weakest link."
- **Scaffolded Capability Assessment.** Formalizing Vygotsky's Zone of Proximal Development, it reveals the first λ-fraction of an oracle solution trajectory and reports **λ_min** — the minimum hint fraction in [0, 1] at which expected success crosses a threshold θ_succ (≈0.9). Lower λ_min means more intrinsic capability.
- **Reported "high-score illusion."** DeepSeek-V3.1-671B posts the highest Pass@1 (65.8%) but the lowest trajectory utility (0.65) among top models, while Gemini-2.5-pro reaches Pass@1 75.4% / utility 0.88. Scaffolding λ̄_min: AgentFounder-30B 0.22, DeepSeek-V3.1 0.35, ReAct baseline 0.51.

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

- Repository note: The utility function relies on model components — an NLI model for evidence grounding and a judgment function for final-answer accuracy — so scores inherit those judges' reliability.

## Related Works

- [FinTrace](./fintrace.md) — Also multi-dimensional trajectory evaluation, in finance rather than deep research.
- [AgentBoard](./agentboard.md) — Trajectory evaluation via subgoal progress rate rather than a hierarchical utility function.
