# KellyBench (2026)

> **English** | [简体中文](../zh/works/kellybench.md)

## Overview

KellyBench is an environment for evaluating long-horizon sequential decision-making in non-stationary markets: agents live through a sequential simulation of the 2023–24 English Premier League season and must maximize long-term bankroll growth in sports-betting markets.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2604.27865>
- **Project:** <https://openreward.ai/GeneralReasoning/KellyBench>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

KellyBench targets the gap between saturating procedural benchmarks and real deployments in long-horizon, non-stationary, open-ended environments. Agents receive detailed historical data — advanced statistics, lineups, public odds — and to succeed must build machine-learning models, identify edge in public markets, and adapt as the environment changes over a season. All evaluated frontier models lose money on average over five seeds: the best achieves −8% average return, with many models experiencing ruin. A human-expert rubric grades strategy sophistication; Claude Opus 4.6 scores 26.5%, far below human baselines.

## Tasks

A season-long sequential simulation (2023–24 English Premier League) of betting decisions under evolving conditions, run over five seeds; agents manage a bankroll continuously rather than solving discrete tasks.

## Domains

Sports-betting markets as a sequential decision environment; no science or engineering domain.

## Evaluation

- Long-term bankroll growth (average return across five seeds), plus a human-expert rubric grading strategy sophistication.
- **Reported.** Every frontier model evaluated loses money on average; best −8% return, with ruin common across seeds; Claude Opus 4.6 scores 26.5% on the strategy rubric.

## Typical Duration

A full simulated season of sequential decisions per run.

## Main Contribution

An open-ended, non-stationary horizon where survival itself is the metric — exposing that models which saturate procedural benchmarks cannot yet manage risk over time.

## Key Design Ideas

- Bankroll dynamics make risk management, not accuracy, the binding constraint (ruin is absorbing).
- Non-stationarity forces continual adaptation rather than a fixed strategy.
- Pairing monetary outcomes with a sophistication rubric separates lucky returns from sound strategy.

## Strengths

- A rare genuinely open-ended objective (growth) with an unforgiving natural ground truth.
- Negative average returns across all frontier models document a capability cliff invisible to task suites.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [Gaia2](./gaia2.md) — Also makes temporal dynamics a scored capability, via environments that advance on their own clock.
- [FinTrace](./fintrace.md) — Also long-horizon financial decision-making, with trajectory-level metrics over tool use.
- [CostBench](./costbench.md) — Also scores economic decision quality, under dynamically priced planning conditions.
