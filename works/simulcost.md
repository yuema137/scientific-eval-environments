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
- **Reviewed version:** <https://arxiv.org/html/2603.20253v4> (2026-08-17)

## Summary

An agent chooses simulation parameters to meet an accuracy target while limiting simulator cost. SimulCost compares its initial choice and subsequent trial-and-error adjustments with traditional parameter scanning. Version 4 separates platform-independent analytical costs from the wall-clock measurements of a production plasma code.

## Tasks

Version 4 contains 2,643 single-round and 2,304 multi-round tasks across 11 analytically costed simulators. A twelfth simulator, EPOCH, contributes 273 tasks in each setting and is reported separately using wall-clock cost. The arXiv revision notice says CGYRO was removed because of a case-search bug.

## Domains

Physics-simulation parameter tuning in fluid dynamics, solid mechanics, and plasma physics.

## Evaluation

- Compare success under budget constraints and multiple accuracy requirements, separately for single-round initial guesses and multi-round adjustment.
- Version 4 reports 45–62% single-round success, falling to 34–50% at high accuracy. Multi-round success reaches 66–81%, but agents require 1.5–2.7 times the cost of traditional scanning, expressed as slower performance in the paper.
- Keep the 11-simulator analytical-cost suite separate from EPOCH’s hardware-dependent wall-clock study.

## Typical Duration

Multi-round parameter-tuning workflows; specific per-task duration not stated in the abstract.

## Main Contribution

Introduces cost-sensitive parameter tuning for physics simulations as a benchmark, explicitly accounting for tool-use resource costs beyond token spend.

## Key Design Ideas

- Charge for simulator use rather than treating model tokens as the only resource.
- Separate an initial parameter guess from feedback-driven adjustment.
- Compare against traditional scanning at explicit accuracy requirements.
- Report analytical and measured wall-clock costs separately.

## Strengths

Explicit simulator costs and a traditional scanning baseline expose whether higher success also requires more computation. The benchmark covers thousands of parameter-tuning instances.

## Limitations

- Repository note: this card follows v4; counts and results from earlier revisions are not interchangeable with the current suite.
- Repository note: EPOCH wall-clock costs depend on the measurement platform, unlike the analytical costs of the other 11 simulators.
- Repository note: transfer of this cost model beyond physics-simulation workflows is not established.

## Related Works

- [CostBench](./costbench.md) — Also cost-aware evaluation with cost as a first-class objective, but in travel-planning tool use rather than scientific simulation.
