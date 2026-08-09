# HydroAgent (2026)

> **English** | [简体中文](../zh/works/hydroagent.md)

## Overview

HydroAgent benchmarks nine frontier LLM agents on calibrating the operational CREST distributed hydrologic model — used by the U.S. National Weather Service for flash-flood forecasting — over four held-out gauges spanning 329–40,792 km², scored by Nash–Sutcliffe Efficiency against a human-expert reference. The paper's paired RL-trained agent is a method contribution (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.17792>
- **Venue:** arXiv preprint (cs.LG, physics.geo-ph), 2026

## Summary

Calibrating a distributed hydrologic model means reading hydrograph signatures and translating them into high-dimensional parameter adjustments, with online CREST simulations as feedback. Best-of-twenty-rounds NSE across nine frontier agents ranges from −0.16 (GPT-5.4) to 0.75 (Sonnet 4.6), and no model reaches the human-expert reference except Opus 4.7 on a single gauge. The paper then fine-tunes Qwen3-4B on 2,576 expert calibration trajectories with simulator-grounded RL (NSE as a verifiable reward), a training contribution outside this card's scope.

## Tasks

Iterative calibration of the operational CREST model on four held-out gauges (329–40,792 km²): interpret hydrograph behavior, adjust distributed parameters, and re-simulate; best-of-twenty rounds per gauge.

## Domains

Hydrology and Earth-system science: streamflow simulation and operational flash-flood forecasting infrastructure.

## Evaluation

- Nash–Sutcliffe Efficiency (NSE) on held-out gauges against a human-expert calibration reference; NSE doubles as the verifiable reward in the paired training work.
- **Reported.** Nine frontier agents span NSE −0.16 (GPT-5.4) to 0.75 (Sonnet 4.6); no model reaches the expert reference except Opus 4.7 on one gauge.

## Typical Duration

Iterative simulate-and-adjust calibration episodes, up to twenty rounds per gauge.

## Main Contribution

Puts frontier agents against an operational forecasting model with a professional yardstick — expert calibrators — and finds the gap is real: signature reading and parameter reasoning, not tooling, are the bottleneck.

## Key Design Ideas

- The target is a production model (CREST/NWS), so competence has direct operational meaning.
- NSE gives an unambiguous, simulation-verifiable score for every calibration attempt.
- Held-out gauges across three orders of magnitude in basin area test transfer, not memorized basins.

## Strengths

- Expert-reference comparison on genuinely operational infrastructure.
- The −0.16-to-0.75 spread shows model choice dominates in physical calibration tasks.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.
- Repository note: the HydroAgent RL fine-tuning (SFT on 2,576 expert trajectories + simulator-grounded GRPO) is a training contribution out of this repository's scope; the card documents the agent benchmark.

## Related Works

- [SimulCost](./simulcost.md) — Also simulation parameter tuning as the evaluated skill, with resource costs.
- [GeoNatureAgent Benchmark](./geonatureagent-benchmark.md) — Also environmental-domain agent evaluation with mechanistic checks.
- [Frontier-Eng](./frontier-eng.md) — Also iterative optimization against professional simulators under constraints.
