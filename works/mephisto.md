# Mephisto (2025)

> **English** | [简体中文](../zh/works/mephisto.md)

> **First appeared:** 2025-10-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.08354)

## Overview

Mephisto is a multi-agent LLM framework that drives the CIGALE spectral-energy-distribution (SED) code to infer the physical properties of galaxies from multi-band photometry, iteratively refining physical models via tree search and a self-play-accumulated knowledge base. Alongside the system, the authors construct a 256-galaxy task set with an external quantitative pass criterion and run all seven LLM backbones over it, releasing code, catalogs and the knowledge base on Zenodo.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** https://arxiv.org/abs/2510.08354
- **Code:** https://zenodo.org/records/15589045 (DOI 10.5281/zenodo.15589045)
- **Venue:** arXiv preprint (October 2025); the arXiv comments field states the paper is submitted to an AAS journal. Its conference abstract, "Interpreting Multi-band Galaxy Observations with Large Language Model-Based Agents" (arXiv:2409.14807), was accepted at the NeurIPS (NIPS) ML4PS Workshop 2024 — the same work, not a separate one.

## Summary

Mephisto decomposes SED interpretation into cooperating agent roles — hypothesis reasoning, CIGALE execution, fit evaluation, knowledge extraction and knowledge validation — and searches over candidate physical models rather than over a fixed precomputed parameter grid. Each galaxy is analysed by expanding a search tree of model-refinement hypotheses (depth-first for exploitation, breadth-first for exploration), with the fit quality of executed CIGALE runs feeding back into the next round of reasoning; insights distilled from past interactions are validated by ablation and retained in a persistent knowledge base. The authors evaluate the framework on a deliberately constructed 256-galaxy sample from COSMOS2020, scored against an exhaustive 360-million-point CIGALE grid, and apply it to 31 JWST "Little Red Dot" objects from JADES. A cross-backbone study repeats the full 256-galaxy run with seven different LLMs and reports success rate against relative API cost.

## Tasks

Each task is one galaxy: given multi-band photometry, produce an SED model whose fit is competitive with an exhaustive grid search. The primary set contains **256 galaxies** drawn from the COSMOS2020 catalog with spectroscopic confirmation from surveys including PRIMUS, 3D-HST and SDSS. The sample is not a convenience selection — the authors fit a neural spline flow over a four-dimensional space (redshift, stellar mass, V-band dust attenuation, star-formation rate) and sample uniformly across it, so the set spans z = 0.1–5.7, M⋆ = 10⁶–10¹² M☉, A_V = 0–3 and SFR = 10⁻⁴–10⁴ M☉/yr. A second, harder application set consists of **31 JWST-discovered "Little Red Dot" galaxies** from JADES, for which no consensus physical interpretation exists. For the knowledge-base ablation the 256 galaxies are split into **208** used for knowledge accumulation and **48** held out as unseen test galaxies; the cross-backbone study uses all 256. The paper defines no difficulty tiers over the galaxies (its three-tier grouping is over LLM cost, not task difficulty).

## Domains

**Astronomy** — specifically extragalactic astronomy and galaxy astrophysics. The evaluated objective is an astronomical inference: recovering physical properties (stellar mass, star-formation rate, dust attenuation, redshift, AGN contribution) of real observed galaxies from multi-band photometry, using an astronomy-specific modelling code (CIGALE) and real survey data (COSMOS2020, JWST/JADES). No co-domain is assigned: the work contributes no general methodology benchmark and its software component is a thin wrapper around an existing astronomy code rather than a software-engineering evaluation.

## Evaluation

The pass criterion is external to the system and quantitative: Mephisto is judged to provide a reasonable interpretation of a galaxy if it produces **any** SED model whose fit satisfies **χ² < 1.2 × χ²_baseline**, where χ²_baseline comes from an exhaustive CIGALE grid search over **360 million grid points** spanning 10 physical parameters (a Brown et al. 2014-style library extended in redshift range and AGN fraction). Secondary agreement measures are reported rather than thresholded: solutions fall within ±20% of the exhaustive-search χ² values, and inferred stellar masses agree with the grid-search values to within about ±0.3 dex. The same criterion is reused for the cross-backbone comparison, over which most models reach **80–90%** success while the low-cost tier drops by more than 25 percentage points relative to GPT-4o. `TODO(reference)` — per-model numeric success rates are presented only graphically (Figure 10) and are not tabulated in the text, so the exact value for each of the seven backbones cannot be quoted. The Little Red Dot analysis is not scored by a formula; it is validated qualitatively against published human-expert analyses.

## Typical Duration

Roughly **36 reasoning steps (explored search states) per galaxy**, with **N_b = 4** refinement hypotheses generated at each step; the breadth-first runs on the Little Red Dots also cap explored states at 36. Each step executes a CIGALE grid of 10⁴–10⁶ points over 8–12 free parameters, so a full per-galaxy analysis evaluates about **1×10⁶ to 6×10⁶ models — approximately 1% of the 360-million-point baseline grid**. With GPT-4o as backbone the authors report about **200K tokens and roughly two dollars per galaxy** for a detailed analysis; mid-cost backbones run at about 1/10 and low-cost backbones at about 1/100 of that cost. No wall-clock time per galaxy is reported.

## Main Contribution

In the authors' framing, Mephisto is the first multi-agent LLM framework that emulates human-like scientific reasoning for interpreting multi-band galaxy observations: it interfaces with an established physical-modelling codebase, reasons deliberately through tree search, accumulates knowledge through self-play, and updates its own knowledge base. They position it against "black-box machine learning approaches in astronomy" as a transparent, human-aligned alternative that integrates with existing research practice, and as a step toward end-to-end AI-driven scientific workflows — a "research copilot for astronomers" rather than an evaluation suite.

## Key Design Ideas

- Five cooperating agent roles: a reasoning agent proposing model hypotheses, an execution agent running CIGALE, an evaluation agent assessing fit quality across photometric bands, a learning agent distilling insights from interaction histories, and a validation agent gating what enters the knowledge base.
- Search over *physical models* instead of a static parameter grid: each node is a model configuration, expanded with N_b = 4 candidate refinements, using depth-first search to exploit promising directions and breadth-first search to keep alternative physical explanations alive.
- The traditional method is the reference, not a competitor component: the exhaustive 360M-point CIGALE grid defines the χ² a solution must approach, so the agent is measured against established practice rather than against another agent.
- Self-play knowledge accumulation with ablation-gated retention: **72 knowledge entries** were distilled from interaction histories, and a candidate entry was kept only if runs with and without it showed demonstrable improvement.
- Reported memory/knowledge effects: temporal memory gives about 25% greater improvement by inference depth 3 (relative χ² of 0.52 with memory versus 0.67 without), and the external knowledge base reduces the failure rate by 11% on the 48 unseen test galaxies.
- Backbone sweep as a cost-performance study: the same 256-galaxy protocol is rerun across seven LLMs grouped into high-, mid- and low-cost tiers (GPT-4o; DeepSeek-V3, DeepSeek-R1, QwQ-32B, DeepSeek-R1-Distill-Llama-70B; DeepSeek-R1-Distill-Llama-8B, GLM-4-Air-250414), plotting success rate against relative cost.

## Strengths

- The pass criterion is anchored to an artifact outside the system — an exhaustive CIGALE grid search — so success is not defined by the agent's own output or by an LLM judge.
- The 256-galaxy set is deliberately constructed to cover the physical parameter space (flow-based uniform sampling in four properties) rather than assembled opportunistically, and it uses spectroscopically confirmed real observations.
- Resource accounting is unusually concrete for an astronomy agent paper: tokens and dollars per galaxy, relative cost tiers, and compute expressed as a fraction of the exhaustive baseline grid.
- The reusable material is public: the Zenodo record (CC-BY-4.0 / MIT, June 2025) ships the agent source, the COSMOS and Little Red Dot photometric catalogs, and the knowledge-base JSON.
- The Little Red Dot study exercises the framework on genuinely open science — the agent independently surfaces both competing interpretations (dust-obscured starburst versus obscured AGN host) reported in the literature.
- Knowledge-base claims are supported by controlled ablations (with/without memory, with/without knowledge, held-out galaxies) rather than asserted.

## Limitations

- Coverage is a single task family. Every scored task is CIGALE-based SED fitting of photometry; the framework is not exercised on spectra, imaging, time series, or any other astronomical inference, so the reported success rates do not generalise beyond this one workflow.
- Per-backbone success rates appear only in a figure and are never tabulated, so the seven-model comparison cannot be cited numerically (recorded above as `TODO(reference)`).
- Success is defined relative to the baseline grid, not to ground truth. The 360M-point grid encodes its own choices of model library, priors and parameter ranges; a galaxy where the grid itself fits poorly can still be "passed", and physical correctness is only spot-checked via stellar-mass agreement.
- The Little Red Dot results — the most scientifically interesting part — are validated by qualitative comparison with prior expert analyses, with no quantitative scoring protocol.
- The 256 galaxies carry no difficulty stratification, so the aggregate success rate cannot be decomposed into easy versus hard regimes of the parameter space.
- Repository note: the authors do not present this work as a benchmark. The words "benchmark" and "test suite" do not appear in the paper, Section III is titled "Results", and the framing throughout is a research copilot. This card treats the 256-galaxy set plus the χ² criterion as a reusable evaluation artifact; that reading is the repository's, not the authors'.
- Repository note: the seven-model study is a **backbone ablation within one framework**, not a comparison of independent agent systems. It measures how far Mephisto's scaffold can be run on cheaper LLMs, and says nothing about how other agent designs would perform on the same galaxies.
- Repository note: the reference point is a **traditional SED-fitting grid search**, not an agent baseline or a human baseline. No competing LLM agent is evaluated on the task set.
- Repository note: the release is a versioned Zenodo snapshot rather than a maintained evaluation harness — there is no runner, no leaderboard, and no held-out split published for external use.

## Related Works

- [Stargazer](./stargazer.md) — the closest analogue: iterative, physics-grounded model fitting on astronomical data (radial-velocity time series), but built explicitly as a benchmark environment with difficulty tiers and per-criterion feedback.
- [gammapyGPT](./gammapygpt.md) — an agent driving an established astronomy analysis code (Gammapy) whose numerical outputs are checked against expected values, the same "traditional code as executable environment and reference" pattern.
- [ReplicationBench](./replicationbench.md) — astrophysics evaluation where the reference is published expert work rather than a grid search, and tasks are co-developed with the original authors.
- [AstroVisBench](./astrovisbench.md) — astronomy workflow evaluation on the code-and-visualization side, complementary to Mephisto's model-inference side.
- [Gravity-Bench-v1](./gravity-bench.md) — physics-discovery evaluation where compute/observation budget is part of the scoring, comparable to Mephisto's cost-versus-success reporting.
- [SimulCost](./simulcost.md) — cost-aware evaluation of simulation parameter tuning with direct comparison against traditional methods, the same accuracy-per-compute framing.
