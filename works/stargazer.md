# Stargazer (2026)

## Overview

Stargazer is a scalable benchmark environment for evaluating AI agents on dynamic, iterative, physics-grounded model-fitting tasks over radial-velocity (RV) time series. It comprises 120 tasks — 100 simulator-generated across three difficulty tiers plus 20 anonymized real archival systems — with built-in per-criterion feedback on every submission.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.15664>
- **Project:** <https://aips-uoft.github.io/Stargazer/>
- **Code:** <https://github.com/AIPS-UofT/Stargazer>

## Summary

Stargazer starts from the position that evaluating agents on research work requires dynamic benchmark environments with built-in feedback on scientifically grounded tasks. Agents iteratively fit Keplerian orbital models to RV time series through a Python REPL and a submission interface, and the evaluator returns per-criterion pass/fail diagnostics with optional hints after every submission. Across eight frontier agents, the best pass rates fall from 80.0% on the Easy tier (GPT-5.3-codex) to 5.8% on Hard (GPT-5.2) and 0.0% for every agent on the 20 real archival systems, with good statistical fits frequently coexisting with incorrect physical parameters. Increasing test-time compute yields only marginal gains, with excessive token usage often reflecting recursive failure loops rather than meaningful exploration.

## Tasks

120 tasks: 100 synthetic RV model-fitting tasks in three difficulty tiers — Easy (20), Medium (40), and Hard (40) — plus 20 real archival systems drawn from published datasets in the NASA Exoplanet Archive and VizieR, spanning one to seven planets. Synthetic scenarios range from high-SNR single-planet systems to multi-planet configurations requiring low-SNR analysis.

## Domains

Astrophysics: exoplanet system inference from radial-velocity time series.

## Evaluation

A task is solved only when all four evaluator criteria are satisfied simultaneously:

- **Residual quality (ok_rms).** The residual RMS of the submitted fit must be at most 1.5× the median measurement uncertainty of the series.
- **Model selection (ok_delta_bic).** The per-point ΔBIC of the proposed model against a weighted-mean constant null model must be positive.
- **Physical recovery (ok_match).** Proposed planets are matched to the ground truth via the Hungarian algorithm, and the resulting match score must be at least 0.8.
- **Planet count (ok_count).** The number of proposed planets must equal the true number.
- **Reported (Table 1).** Pass rates averaged over three independent runs: GPT-5.3-codex leads the eight evaluated agents on Easy at 80.0% against 95.0% for a classical Lomb-Scargle + Keplerian-fitting pipeline, GPT-5.2 leads Hard at 5.8%, and no agent — o3-mini, GPT-5-mini, GPT-5.2, Kimi-K2.5, Qwen-3.5-Plus, Gemini-3.1-Pro, Claude-Sonnet-4.6, GPT-5.3-codex — passes a single one of the 20 real archival tasks (0.0%).

## Typical Duration

Per-tier budgets: 200K tokens and 600 s wall-clock with 3 submission attempts on Easy, 450K tokens and 900 s with 5 attempts on Medium, and 900K tokens and 1,500 s with 10 attempts on Hard; an episode terminates when any limit is reached.

## Main Contribution

A scalable, simulation-driven environment for evaluating AI agents on iterative, physics-grounded model fitting, with per-criterion physical-consistency feedback and a design methodology the authors suggest generalizes to other model-fitting problems across scientific domains.

## Key Design Ideas

- Simulator-driven task generation: a single random seed controls orbital-parameter sampling, observation scheduling, noise injection, and N-body signal generation via Rebound.
- Interactive fit loop: a Python REPL for analysis code plus a `submit_action` interface, with per-criterion pass/fail diagnostics and optional hints returned after every submission.
- Success gated on physical consistency: statistical criteria (residual RMS, per-point ΔBIC) are required jointly with physical parameter recovery and correct planet count.
- Anonymized real-data subset: 20 archival systems with target and instrument identifiers removed, guarding against contamination from published solutions.

## Strengths

- Seeded, simulator-driven generation yields a scalable task pool with exact ground truth for every synthetic system.
- Per-criterion diagnostics separate statistical fit quality from physical parameter recovery, making the gap between the two directly measurable.
- Classical baselines (a Lomb-Scargle + Keplerian-fitting pipeline and nested sampling) anchor the difficulty scale against standard practice.

## Limitations

- Repository note: Single scientific substrate — all 120 tasks are radial-velocity model fitting, and the authors' suggestion that the simulation-driven design generalizes to other model-fitting domains is not demonstrated in the paper.
- Repository note: The four-criterion success rule awards no partial credit, and the classical baselines are not run on the 20 real archival tasks, so the agent–classical comparison covers only the synthetic tiers.

## Related Works

- [Aviary](./aviary.md) — Also an interactive environment suite for scientific agents with programmatic reward, but spanning five language-grounded environments across domains rather than a single physics model-fitting problem.
- [ScienceAgentBench](./scienceagentbench.md) — Also evaluates agents on data-driven scientific analysis, but scores standalone generated programs on static metrics rather than running an iterative fit loop with per-criterion feedback.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also executable scientific-agent tasks, but domain-expert-authored across five domains rather than simulator-generated within a single astrophysical setting.
