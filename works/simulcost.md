# SimulCost (2026)

> **English** | [简体中文](../zh/works/simulcost.md)

> **First appeared:** 2026-03-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2603.20253)

## Overview

SimulCost is a cost-aware benchmark for LLM agents on physics-simulation parameter tuning. It explicitly accounts for tool-use costs — simulation time and experimental resources — beyond the token-cost view of resource-aware evaluation.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.20253>

## Summary

SimulCost argues that scientific-agent evaluation has focused on token costs while ignoring tool-use costs such as simulation time and experimental resources. It provides a benchmark of parameter-tuning tasks across 13 physics simulators in both single-round and multi-round settings, and directly compares LLM agents against traditional methods under budget constraints.

## Tasks

2,947 single-round tasks and 1,931 multi-round tasks spanning 13 simulators.

## Domains

Physics-simulation parameter tuning across 13 simulators.

## Evaluation

- Success rate under budget constraints.
- Single-round vs. multi-round settings.
- Reported: frontier LLMs achieve 46–65% success initially, declining to 35–55% under strict accuracy requirements; LLM agents underperform traditional approaches by 1.5–2.5× in multi-round scenarios.

## Typical Duration

Multi-round parameter-tuning workflows; specific per-task duration not stated in the abstract.

## Main Contribution

Introduces cost-sensitive parameter tuning for physics simulations as a benchmark, explicitly accounting for tool-use resource costs beyond token spend.

## Key Design Ideas

- Cost model extends beyond tokens to simulation-time and experimental-resource costs.
- Multi-simulator breadth (13 simulators).
- Distinct single-round and multi-round settings.
- Direct comparison against traditional (non-LLM) approaches.

## Strengths

- Explicitly models tool-use costs, which token-only frameworks miss.
- Comparison against traditional methods provides a strong baseline reference.
- Large task suite (2,947 + 1,931).

## Limitations

- Repository note: Physics-simulation-specific — cost-model transfer to other scientific workflows is not evaluated.

## Related Works

- [CostBench](./costbench.md) — Also cost-aware evaluation with cost as a first-class objective, but in travel-planning tool use rather than scientific simulation.
