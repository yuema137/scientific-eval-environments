# EnergyBridge (2026)

> **English** | [简体中文](../zh/works/energybridge.md)

> **First appeared:** 2026-08-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.08691)

## Overview

EnergyBridge is a benchmark and agent framework for residential virtual power plants (VPPs) that couples capacity reporting, household authorization, and physical execution, pairing region-specific EnergyPlus building-energy environments with an LLM-based User Participation Simulator.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.08691
- **Code:** https://github.com/Agentic-Intelligence-Lab/EnergyBridge
- **Venue:** arXiv preprint (submitted 9 August 2026)

## Summary

Residential VPPs can provide grid flexibility by shifting household demand, but physical flexibility becomes dependable capacity only when residents authorize a plan and the promised response is actually delivered. Existing benchmarks evaluate control but omit event-specific authorization. EnergyBridge connects capacity reporting, household authorization, and physical execution in a single workflow (VPP request → capacity report → household-specific plan → simulated consent → controller or fallback execution → EnergyPlus measurement → audit). It combines region-specific EnergyPlus environments for Tianjin and Berlin with an LLM-based User Participation Simulator, and releases human data and code for reproducible human-centered grid-flexibility research.

## Tasks

The main evaluation runs 50 seven-day simulations spanning five fixed households, two regions (Tianjin and Berlin), and five methods, yielding 350 household-day episodes; one 18:00–19:00 demand-response event per household-day gives 70 matched contexts per method. A separate capacity-reporting audit uses held-out events with June delivery records forming each method's retrieval memory and July events forming the query cohort (70 held-out events per method; the repository describes 840 one-day simulations across seven configured July event days). Human validation collected 584 complete consented responses across six personas, producing 1,752 paired respondent–method judgments (584 respondents × 3 methods each).

## Domains

Energy systems / residential demand response and grid flexibility (household energy management for virtual power plants). Building-energy modeling of HVAC, EV charging, an electric water heater, washer, dryer, and dishwasher, together with non-controllable base load.

## Evaluation

Physical outcomes are metered from EnergyPlus (EnergyPlus 24.1.0). Reported metrics include: simulated gate-acceptance (authorization) rate `A = N_accepted / N_events`; event-window (VPP-window) energy; and capacity-commitment reliability `F_m = P(accepted ∩ {0.8 ≤ C_actual / Ĉ ≤ 1.2})`, which combines acceptance with within-tolerance delivery accuracy. Household authorization is decided by the LLM-based User Participation Simulator, which encodes six behavioral dimensions (`p = (p_schedule, p_comfort, p_task, p_price, p_control, p_grid)`) with the prompt frozen before validation. Against 584 persona- and event-matched human role-play judgments, the simulator preserves method acceptance ordering (EnergyBridge, then HEMA, then MPC) with a 5.3-percentage-point mean absolute acceptance error (abstract); for EnergyBridge specifically the LLM–human acceptance gap is 5.1 points (LLM 77.1% vs. human 72.1%, Table 2).

## Typical Duration

Environments are simulated at six zone timesteps per hour (10-minute resolution). The main evaluation uses seven-day simulations with one 18:00–19:00 event window per household-day; MPC uses a one-hour planning horizon (six steps) and Rule+MILP a 30-minute grid. Per-episode wall-clock time and token budgets are not stated.

## Main Contribution

The authors frame EnergyBridge as an end-to-end benchmark for human-authorized physical agents that evaluates whether an agent can transform physical flexibility potential into household-authorized and verifiable grid resources, rather than only generating feasible control schedules. It contributes human-grounded evaluation (released benchmark environments, human evaluation data, physical models, and baseline implementations) and an agent design combining household grounding, constraint-aware plan generation, consent-gated execution, and personalized capacity reporting.

## Key Design Ideas

- Couples three stages — capacity reporting, household authorization, and physical execution — into one benchmarked workflow, adding event-specific authorization that prior control benchmarks omit.
- Region-specific EnergyPlus building models: Tianjin and Berlin instantiate separate residential envelopes following GB 50176-2016 and DIN 4108-4:2020-11 respectively, with Tianjin using a CSWD typical-year EPW and a normalized time-of-use tariff, and Berlin using hourly 2025 station observations and hourly 2025 price traces.
- LLM-based User Participation Simulator over six behavioral dimensions, validated against human role-play so acceptance rankings can substitute for costly human trials.
- Capacity-commitment reliability metric that credits a method only when a plan is both accepted and delivered within a ±20% tolerance band.

## Strengths

- Human-grounded: acceptance judgments are validated against 584 consented human role-play responses (1,752 paired judgments), and the simulator preserves method ordering (paper).
- Physically grounded outcomes metered from EnergyPlus rather than from surrogate models, across two regulatory/climate regions (paper).
- Releases human data, physical models, and baseline implementations for reproducibility (paper, repository).

## Limitations

- Human validation is anchored on a single frozen Tianjin event and six personas; the abstract's 5.3-point mean absolute acceptance error quantifies remaining simulator–human disagreement (paper).
- Repository note: authorization is decided by an LLM simulator rather than by live residents, so reported acceptance and reliability figures inherit the simulator's calibration limits.
- Repository note: the paper's per-method event counts (e.g., 70 matched contexts / 350 episodes) and the repository's simulation counts (50 seven-day and 840 one-day simulations) describe the same study at different granularities; readers should consult both sources for exact configuration.

## Related Works

- TODO(reference) — related energy-systems / demand-response or building-control evaluation environments once indexed.
