# PDEBench (2022)

> **English** | [简体中文](../zh/works/pdebench.md)

## Overview

PDEBench is the canonical benchmark suite for scientific machine learning on time-dependent PDEs: ready-to-use datasets across advection, Burgers, reaction-diffusion, diffusion-sorption, Darcy flow, shallow-water, and compressible/incompressible Navier–Stokes equations, with forward and inverse tasks and baselines including FNO, U-Net, and PINNs. It evaluates scientific ML surrogates, not LLM agents (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2210.07182>
- **Code:** <https://github.com/pdebench/PDEBench>
- **Dataset:** <https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/darus-2986>
- **Venue:** NeurIPS 2022 Datasets and Benchmarks

## Summary

PDEBench broadened SciML evaluation beyond a handful of toy equations: a much wider range of PDEs with much larger ready-to-use datasets, including multiple simulation runs across varied initial conditions, boundary conditions, and PDE parameters (per the official repository: 1D advection, Burgers, reaction-diffusion, diffusion-sorption; 2D diffusion-reaction, Darcy flow, shallow-water, incompressible Navier–Stokes; compressible Navier–Stokes). Models are compared against both classical numerical simulations and ML baselines under newly proposed evaluation metrics, with an extensible API for new tasks.

## Tasks

Forward and inverse learning tasks over time-dependent PDE simulation datasets spanning the nine equation families above; non-LLM surrogate training and evaluation.

## Domains

Computational physics: canonical PDE families from advection and Burgers through shallow-water and Navier–Stokes flows.

## Evaluation

- Comparison against classical numerical simulations and ML baselines (FNO, U-Net, PINN, gradient-based inverse methods) under the suite's proposed metrics; metric definitions are TODO(reference).
- **Reported.** The abstract states no numeric headline; the suite's role is standardized comparison.

## Typical Duration

N/A — offline surrogate training and evaluation over fixed datasets; not an agent setting.

## Main Contribution

The reference evaluation substrate for PDE surrogate learning — the suite later LLM-solver benchmarks (and this repository's RealPDEBench-class cards) define themselves against.

## Key Design Ideas

- Parameter, initial-condition, and boundary-condition variation is built into the datasets rather than left to users.
- Forward and inverse tasks live in one suite with a common API.
- Baselines plus pretrained models make comparisons reproducible out of the box.

## Strengths

- Canonical status: the shared vocabulary of PDE-surrogate evaluation.
- Extensible, permissively licensed data and code.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: PDEBench evaluates scientific ML surrogate models, not LLM agents; it is documented as the canonical PDE-suite reference point that agentic solver-generation benchmarks build on.

## Related Works

- [RealPDEBench](./realpdebench.md) — The real-world-data successor pairing measurements with simulations under the same caveat class.
- [CodePDE](./codepde.md) — Draws on PDEBench problem families for LLM solver-generation evaluation.
- [The Well](./the-well.md) — The large-scale, multi-domain sibling collection of physics simulation data.
