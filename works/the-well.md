# The Well (2024)

> **English** | [简体中文](../zh/works/the-well.md)

## Overview

The Well is a large-scale collection of diverse physics simulations for machine learning: 15 TB of data across 16 datasets spanning biological systems, fluid dynamics, acoustic scattering, and magneto-hydrodynamic simulations of extra-galactic fluids and supernova explosions, with a unified PyTorch interface for training and evaluating surrogate models. It serves scientific ML surrogates, not LLM agents (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.00568>
- **Code:** <https://github.com/PolymathicAI/the_well>
- **Project:** <https://polymathic-ai.org/the_well/>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks

## Summary

Surrogate progress is bottlenecked by data breadth: models tuned on one physics regime routinely fail on the next. The Well answers with volume and diversity — 15 TB over 16 simulation datasets curated with domain experts, from active matter and viscoelastic instabilities to astrophysical MHD — behind one PyTorch interface with example baselines, so a single training/evaluation loop can sweep physics regimes that previously required bespoke pipelines.

## Tasks

Surrogate training and evaluation over 16 spatiotemporal physics-simulation datasets (15 TB) through a unified interface; non-LLM setting.

## Domains

Diverse simulated physics: fluid dynamics, acoustic scattering, magneto-hydrodynamics of extra-galactic fluids and supernovae, and biological systems.

## Evaluation

- Baseline training and evaluation through the unified PyTorch library; metric definitions are TODO(reference).
- **Reported.** The abstract's claim is the resource itself: 15 TB across 16 expert-curated datasets.

## Typical Duration

N/A — offline surrogate training and evaluation; not an agent setting.

## Main Contribution

Physics-simulation data at foundation-model scale and diversity, making cross-regime generalization of surrogates a testable claim rather than an aspiration.

## Key Design Ideas

- Sixteen heterogeneous physics regimes under one interface expose regime-transfer failures.
- Domain-expert curation keeps each dataset physically meaningful, not just voluminous.
- Uniform access removes the engineering excuse for narrow evaluation.

## Strengths

- The largest and most diverse open physics-simulation collection documented here.
- NeurIPS D&B pedigree and active maintenance by Polymathic AI.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The full 16-dataset enumeration is on the project documentation site.
- Repository note: The Well serves scientific ML surrogate models, not LLM agents; it is documented as a canonical data substrate that agent-relevant PDE benchmarks and this repository's surrogate-caveat cards reference.

## Related Works

- [PDEBench](./pdebench.md) — The canonical structured-PDE predecessor suite.
- [RealPDEBench](./realpdebench.md) — Complements simulated diversity with paired real-world measurements.
- [gwBenchmarks](./gwbenchmarks.md) — Uses the same class of expensive simulation data (numerical relativity) for agent stress-testing.
