# Frontier-Eng (2026)

> **English** | [简体中文](../zh/works/frontier-eng.md)

## Overview

Frontier-Eng is a benchmark for self-evolving agents on real-world engineering tasks, framed as **iterative generative optimization**: an agent proposes a candidate design, an industrial-grade simulator returns continuous reward under hard feasibility constraints, and the agent revises within a fixed interaction budget.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.12290>

## Summary

Frontier-Eng argues that binary pass/fail scoring does not capture how agents perform on constrained real-world engineering problems, where feasible-but-suboptimal solutions dominate and iterative refinement is the main capability under test. The benchmark structures each task as a propose-execute-evaluate loop: the agent generates a candidate artifact, an industrial-grade simulator returns continuous reward signals under hard feasibility constraints, and the agent revises within a fixed interaction budget.

## Tasks

47 tasks spanning 5 engineering categories.

## Domains

Real-world engineering, verified against industrial-grade simulators.

## Evaluation

- Iterative propose-execute-evaluate loop as the fundamental unit of evaluation.
- Industrial-grade simulators as verifiers.
- Continuous reward signal rather than binary pass/fail.
- Hard feasibility constraints enforced by the simulator.
- Fixed interaction budget per task.
- 8 frontier LLMs tested; GPT 5.4 exhibited the most robust performance; all models found the benchmark challenging.
- Reported analytical finding: **dual power-law decay** in improvement — improvement frequency decays as ~1/iteration and improvement magnitude also follows a power law across the optimization trajectory.
- Reported design finding: **depth matters more than breadth** for solving constrained engineering problems.

## Typical Duration

Iterative multi-step refinement per task, bounded by the fixed interaction budget.

## Main Contribution

Reframes engineering-agent evaluation from binary pass/fail to **iterative generative optimization under industrial-grade simulator feedback and a bounded interaction budget**, and empirically documents the shape of the improvement trajectory as dual power-law decay.

## Key Design Ideas

- Propose-execute-evaluate as the fundamental unit of evaluation, rather than one-shot generation.
- Industrial-grade simulators return continuous reward, so feasible-but-suboptimal solutions receive graded credit.
- Hard feasibility constraints coexist with continuous reward — the search space is bounded but the reward within it is dense.
- Fixed interaction budget makes the benchmark inherently resource-aware.
- Empirical characterization of the improvement trajectory (dual power-law decay) as part of the benchmark's headline result.

## Strengths

- Continuous reward under industrial-grade simulation captures a signal that binary pass/fail benchmarks discard.
- Bounded interaction budget makes reported scores reproducible without token-cost drift.
- Empirical power-law-decay claim gives follow-up work a concrete phenomenon to reproduce or refute.
- Depth-vs-breadth finding is a testable design claim for engineering agents.

## Limitations

- Repository note: 47 tasks across 5 categories — modest task pool relative to the "real-world engineering" domain coverage claim.
- Repository note: Reference is arXiv v2 (2026-04-27); no peer-reviewed venue is documented in the primary source at time of writing.

## Related Works

- [SimulCost](./simulcost.md) — Also uses domain simulators as verifiers and treats resource use as first-class; scoped to physics-simulation parameter tuning rather than open-ended engineering optimization.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also science / engineering with executable verification, but uses pytest checks in containers rather than industrial-grade simulator feedback inside an iterative loop.
- [CostBench](./costbench.md) — Also structures evaluation around iterative decisions under a bounded resource budget, but the resource is tool-call cost in a travel-planning domain rather than an interaction budget on engineering optimization.
