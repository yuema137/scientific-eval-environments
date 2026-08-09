# Gravity-Bench-v1 (2025)

> **English** | [简体中文](../zh/works/gravity-bench.md)

## Overview

Gravity-Bench-v1 is an agentic benchmark on gravitational-physics discovery: the agent observes a simulated two-body gravitational system, plans data collection within an experimental budget, and analyzes the data to uncover concealed physics — including out-of-distribution modified physics that cannot be answered from memorized textbook knowledge.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.18411>
- **Code:** <https://github.com/NolanKoblischke/GravityBench>
- **Dataset:** <https://huggingface.co/datasets/GravityBench/GravityBench>
- **Project:** <https://gravitybench.github.io/>
- **Venue:** ICML 2025

## Summary

Each task simulates a binary system with rigorous gravitational-dynamics ground truth. The agent decides which observations to take under a budget (up to 100 data points per run, per the official project page), then reasons over the collected data to characterize the system's physics. The benchmark admits an open-ended space of solutions, and reference solutions calibrate AI performance against human expertise. Tasks include out-of-distribution physics variants, so success requires discovery rather than recall.

## Tasks

Interactive observation-planning-and-analysis episodes over simulated two-body gravitational systems, including out-of-distribution modified-physics variants; observations are drawn under a fixed experimental budget. Exact task counts are TODO(reference).

## Domains

Gravitational physics and dynamics of simulated binary systems (astrophysics-flavored, categorized under astro-ph.IM).

## Evaluation

- Answers checked against reference solutions derived from rigorous gravitational-dynamics simulations, calibrated against human expertise.
- **Reported (official project page).** The top model, o4-mini-high, reaches 74% with full data access, dropping to 49% under the observation budget.

## Typical Duration

Budgeted interactive episodes; up to 100 observations per run per the official project page.

## Main Contribution

Makes budgeted experimental design part of what a physics-discovery benchmark measures, and uses out-of-distribution physics to separate discovery from recall.

## Key Design Ideas

- The observation budget turns data collection into a planned, costed decision rather than free input.
- Out-of-distribution modified physics defeats memorization by construction.
- Reference solutions calibrate open-ended answers against human expert performance.

## Strengths

- The full-access-versus-budget gap (74% vs. 49% for the top model) isolates the cost of having to plan observations.
- Open-ended solution space at an upper-undergraduate technical level that still challenges baseline agents.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [MaD Physics](./mad-physics.md) — Also prices observations under a per-trial budget for discovering altered physical laws.
- [NewtonBench](./newtonbench.md) — Also evaluates law discovery under counterfactually shifted physics, via symbolic-equivalence scoring.
- [DiscoverPhysics](./discoverphysics.md) — Also has agents run experiments in simulated worlds whose physics deviates from our own.
