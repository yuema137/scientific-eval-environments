# FORESIGHT-9 (2026)

> **English** | [简体中文](../zh/works/foresight-9.md)

> **First appeared:** 2026-08-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.29372)

## Overview

FORESIGHT-9 tests adaptive trading agents on counterfactual market paths and checks whether their internal research state agrees with actual execution. A high final return can otherwise hide an adaptive mechanism that has stopped operating.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

N/A — financial decision-system evaluation; no canonical scientific research activity is assigned.

## Links

- **Paper:** [FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents](https://arxiv.org/abs/2608.29372), 2026 preprint.
- **Full text and artifact descriptions:** <https://arxiv.org/html/2608.29372v1>

## Summary

Nine scenario paths branch from July 15, 2026. A seeded generator preserves declared scenario endpoints, while a time gate reveals only observations available on the current simulated date. The study evaluates two agent frameworks with two model backbones, giving 36 runs. A fixed equal-weight policy beats 31 of those runs.

## Tasks

Agents observe a shared panel, maintain factors, propose portfolios, and execute allocations across each path. The environment standardizes observations, trading constraints, costs, and timing while preserving each system's adaptation procedure.

## Domains

Financial markets and portfolio allocation. Repository note: this domain has no canonical science/engineering domain page; the work is indexed through its evaluation topics.

## Evaluation

Outcome metrics include net asset value, drawdown, and Sharpe ratio. Process records separately track the live factor library, declared decision state, and executed holdings. One high-return run loses its live factors while continuing to declare an ensemble and executing an equal-weight fallback. The diagnostic comparison therefore asks whether gains came from the intended adaptive behavior, not just whether the portfolio appreciated.

## Typical Duration

Paths extend to December 31, 2035, approximately 2,468 simulated trading days after the shared boundary. This is simulated horizon, not wall-clock runtime; no standard per-run wall-clock duration is specified.

## Main Contribution

A controlled test of cross-scenario robustness and consistency between adaptive state and execution.

## Key Design Ideas

- Keep scenario manifests and seeds sufficient for deterministic path regeneration.
- Enforce an explicit information boundary at every simulated date.
- Compare agent outcomes with a simple policy under the same scenario and execution contract.

## Strengths

- Provides a concrete case where process telemetry changes the interpretation of a favorable outcome.
- Separates operational events from simulated market time.

## Limitations

- One seed per configuration and scenario cannot separate all sources of run variance.
- Scenarios are not samples from a calibrated forecast distribution and lack independent human expert validation.
- The contract is long-only and fully invested; it does not test short selling or cash timing.
- Repository note: the paper describes released artifacts, but this review did not locate a separately verifiable official download URL.

## Related Works

- [Beyond Final Scores](./beyond-final-scores.md)
- [The Replay Gap](./the-replay-gap.md)
