# Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows (2026)

> **English** | [简体中文](../zh/works/plausible-but-wrong-a-case-study-on-agentic-failur.md)

## Overview

An evaluation study of the CMBAgent multi-agent system across two workflow paradigms and eighteen astrophysical tasks, contributing an automated scoring protocol (execution, parameter accuracy, numerical accuracy) and a four-mode failure taxonomy whose central finding is silent incorrect computation — syntactically valid code that returns plausible but wrong physics with no error signal.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.25345>
- **Venue:** arXiv preprint (cs.AI, astro-ph.IM), 2026

## Summary

The paper asks not whether an astrophysics agent can succeed but how it fails when it does not, and whether the failure is visible. CMBAgent is run in two configurations — a One-Shot pass and a full Deep Research planning-and-control loop — over fourteen tool-grounded CAMB computation tasks and four research-driven analysis tasks on public astronomical datasets. Scoring is decomposed so that crashing, misconfiguring solver parameters, and computing the wrong numbers from correct-looking parameters are separated rather than collapsed into a single pass/fail. Providing domain-specific documentation context lifts the One-Shot composite score from near zero to 0.85, roughly a sixfold improvement, but the dominant residual failure mode is Mode C: execution succeeds, parameters look reasonable, and the numerical result is wrong. The authors position the work as a case study and reliability analysis rather than a new model or framework.

## Tasks

Eighteen astrophysical tasks in two groups. Fourteen structured CAMB computation tasks assess parameter configuration robustness, solver reliability and numerical accuracy, adapted from the CMBAgent benchmark repository and stratified by complexity (tasks 1–6 are single API calls; task 7 onward increases in complexity). Four research-driven tasks (T1–T4) use public archival data: Type Ia supernova fitting on Union2.1, NGC 3198 rotation-curve modelling on SPARC galaxy data, exoplanet mass–radius analysis from the NASA Exoplanet Archive, and SLACS strong-lensing analysis.

## Domains

Astronomy and astrophysics throughout: cosmological Boltzmann-solver computations with CAMB, supernova cosmology fitting, galaxy rotation-curve modelling, exoplanet population analysis, and strong gravitational lensing. Cosmology is the dominant slice; a Physics co-reading is defensible but the evaluated objectives are astronomical inference from observational catalogs and astronomy-specific solvers.

## Evaluation

- **Execution Success Rate (ESR).** Binary; output must contain at least two numeric columns and cover at least 95% of the reference x-range.
- **Parameter Accuracy Score (PAS).** Weighted mean relative error across CAMB solver parameters, with weights of 2.0, 1.5 and 1.0 assigned by physical importance.
- **Numerical Accuracy Score (NAS).** Weighted average of NRMSE (0.2), SMAPE (0.3) and Lin's concordance correlation coefficient (0.5).
- **Composite.** `Score = PAS × NAS` when execution succeeds. The headline One-Shot score of 0.85 is the product of PAS = 0.95 and NAS = 0.86; without domain context the score is approximately 0, roughly a sixfold gap.
- **Deep Research scoring** is manual, using a Parameter Recovery Score `PRS = max(0, 1 − |θ̂_p − θ*_p| / (3σ*_p))` plus a qualitative rating of physical plausibility and failure transparency (✓ / ∼ / ×).
- **Failure taxonomy**, four mutually exclusive modes: Mode A code failure (ESR = 0); Mode B wrong parameters (ESR = 1, PAS < 0.5); Mode C wrong computation (ESR = 1, PAS ≥ 0.5, NAS < 0.5); Mode D correct (ESR = 1, PAS ≥ 0.5, NAS ≥ 0.5).
- **Reported.** The base LLM fails at Mode A about 91% of the time. CMBAgent without documentation context lands in Mode C — wrong computation with no error signal — about 47% of the time. All four Deep Research tasks exhibited silent failures; on T2 (NGC 3198) all 5 of 5 trials returned PRS = 0.05 with unphysical concentration parameters.

## Typical Duration

Not reported as tokens, cost or measured wall-clock. Hardware for the Deep Research runs is specified (Dell Precision 5480, 32 GB RAM, 20 CPU threads) along with a target runtime of "within a few minutes" for MCMC steps.

## Main Contribution

A reliability-focused evaluation of an astrophysics agent system that separates crashing from silent numerical error, quantifies how much of the apparent competence comes from domain documentation in context, and shows that the dominant residual failure mode produces confident, physically inconsistent results with no visible error indicator.

## Key Design Ideas

- Multiplicative composite scoring (`PAS × NAS`) so that a run cannot look successful by getting the configuration right while computing the wrong physics.
- Physics-weighted parameter error, weighting solver parameters by their importance rather than treating all fields equally.
- Numerical accuracy built from three complementary agreement measures (NRMSE, SMAPE, Lin's CCC) rather than a single distance.
- A four-mode taxonomy defined by thresholds on the same scores, making failure classification reproducible instead of narrative.
- Paired workflow paradigms — One-Shot versus a full Planning & Control loop with critique and retry — as the controlled variable, testing whether orchestration removes silent failures.
- An ablation on domain-specific context (with and without CAMB documentation) isolating retrieval of API knowledge from scientific competence.

## Strengths

- Directly targets the failure class that matters most for scientific deployment: results that are wrong but carry no error signal.
- Scoring is decomposed and threshold-defined, so failure categories are derived from the metrics rather than assigned by hand.
- Tasks span both tool-grounded solver calls and open-ended analysis on real archival datasets, so the conclusions are not confined to a single API surface.
- The context ablation gives a concrete measure of how much of the system's performance depends on documentation being in the prompt.

## Limitations

- The study evaluates a single agent system (CMBAgent) with a single LLM backend (GPT-4o-mini) across configurations, so the failure rates cannot be read as properties of astrophysics agents in general.
- Deep Research scoring is manual and covers only four tasks, with a small number of trials per task.
- The fourteen CAMB tasks are adapted from the CMBAgent benchmark repository and no standalone task-set release with a permanent URL is stated, which limits reuse.
- Repository note: the authors explicitly frame the work as a case study rather than a benchmark; its durable contribution here is the scoring protocol and failure taxonomy, not a reusable task suite.
- Repository note: the composite score is multiplicative over two sub-scores computed on the same run, so a single mis-specified reference range can depress both terms at once.

## Related Works

- [ReplicationBench](./replicationbench.md) — Also evaluates agents on astrophysics research workflows against author-defined ground truth, but as a graded replication benchmark rather than a failure-mode study of one system.
- [Stargazer](./stargazer.md) — Also separates statistical fit quality from physical parameter recovery in an astronomy setting, and reports the same pattern of good-looking fits with wrong physics.
- [AstroVisBench](./astrovisbench.md) — Also scores astronomy scientific-computing outputs by inspecting the data products rather than the code text.
- [EnvTrace](./envtrace.md) — Also an execution-grounded evaluation that distinguishes superficially valid agent output from substantively correct behaviour.
