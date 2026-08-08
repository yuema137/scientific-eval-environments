# RealPDEBench (2026)

> **English** | [简体中文](../zh/works/realpdebench.md)

## Overview

RealPDEBench is a benchmark for scientific machine learning that integrates real-world measurements with paired numerical simulations — presented as the first of its kind — comprising five datasets, three tasks, eight metrics, and ten baselines. Its subject is scientific ML models rather than LLM agents (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.01829>
- **Code:** <https://github.com/AI4Science-WestlakeU/RealPDEBench>
- **Dataset:** <https://huggingface.co/datasets/AI4Science-WestlakeU/RealPDEBench>
- **Project:** <https://realpdebench.github.io/>
- **Venue:** ICLR 2026 (oral)

## Summary

RealPDEBench targets a bottleneck in scientific ML for complex physical systems: models are overwhelmingly trained and validated on simulated data because real-world measurements are expensive, which limits evaluation and blocks research on sim-to-real transfer. The benchmark provides five real-world measured datasets with paired simulated datasets across different complex physical systems, defines three tasks that allow comparisons between real-world and simulated data, and scores models with eight metrics spanning data-oriented and physics-oriented measures. Experiments over ten baselines reveal significant discrepancies between simulated and real-world data, while pretraining with simulated data consistently improves both accuracy and convergence.

## Tasks

Five real-world measured datasets with paired numerical simulations — fluid–structure interaction, controlled cylinder, cylinder, foil, and combustion (per the official project page) — and three tasks enabling real-vs-simulated comparison and the development of methods that bridge the two.

## Domains

Complex physical systems: fluid–structure interaction, cylinder and foil flows, and combustion, with paired real-world measurements and numerical simulations.

## Evaluation

- Eight metrics spanning **data-oriented** measures (e.g., RMSE, relative L₂ per the official project page) and **physics-oriented** measures (e.g., Fourier error, kinetic energy).
- Ten baselines: state-of-the-art models, pretrained PDE foundation models, and a traditional method.
- **Reported.** Significant discrepancies between simulated and real-world data; pretraining with simulated data consistently improves both accuracy and convergence.

## Typical Duration

N/A — offline model training and evaluation over fixed datasets; not an interactive agent setting.

## Main Contribution

Makes the sim-to-real gap in scientific ML itself measurable, by pairing expensive real-world measurements with numerical simulations of the same physical systems under shared tasks and metrics.

## Key Design Ideas

- Every real-world dataset ships with a paired simulated dataset, so real-vs-simulated comparison is a designed-in capability rather than an afterthought.
- Physics-oriented metrics complement data-oriented ones, so physical plausibility is scored, not just pointwise error.
- The baseline pool deliberately spans pretrained PDE foundation models down to a traditional method, anchoring both ends of the method spectrum.

## Strengths

- Expensive real-world measurement data — the resource whose absence the paper identifies as the field's bottleneck — is the benchmark's core asset.
- The paired design directly supports sim-to-real transfer research rather than only documenting the gap.

## Limitations

- Repository note: card compiled from the arXiv abstract and the official project page (August 2026); details beyond those sources await full-paper validation.
- Repository note: RealPDEBench evaluates scientific ML surrogate models, not LLM agents; it is documented here for its evaluation methodology — paired real/simulated splits and physics-oriented metrics — which is directly relevant to how scientific agents are verified.

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — Also evaluates fluid-dynamics competence with physics-grounded verification, for LLM and coding agents rather than surrogate models.
- [SimulCost](./simulcost.md) — Also builds evaluation on physics simulators, adding cost-awareness rather than real-world measurements.
- [MaD Physics](./mad-physics.md) — Also evaluates prediction of physical-system evolution, in simulated environments where RealPDEBench contributes real measured data.
