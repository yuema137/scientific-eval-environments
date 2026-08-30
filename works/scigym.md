# SciGym (2025)

> **English** | [简体中文](../zh/works/scigym.md)

> **First appeared:** 2025-07-02 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2507.02083)

## Overview

SciGym measures the scientific capabilities of language models with a systems-biology dry lab: agents iteratively design experiments and analyze the resulting simulated data on biological systems encoded in the Systems Biology Markup Language (SBML), submitting hypothesized mechanisms against hidden ground-truth systems.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.02083>
- **Code:** <https://github.com/h4duan/SciGym>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

SciGym addresses the cost problem of evaluating open-ended experimentation: wet labs are too expensive to run at benchmark scale, so it substitutes a dry lab that simulates data from hidden SBML-encoded biological systems. Agents choose experiments sequentially, observe simulated results, and submit SBML-format hypotheses, with error-checking and configurable resubmission rounds (per the official repository). Six frontier LLMs are evaluated on 137 small systems, with 350 systems released in total; all models' performance declines significantly as system complexity increases.

## Tasks

Iterative experiment-design-and-analysis episodes over hidden SBML biological systems: 137 small systems evaluated, 350 released (137 small + 213 large per the official repository).

## Domains

Systems biology: mechanistic models of biological systems encoded in SBML.

## Evaluation

- Agent-recovered models compared against hidden ground-truth SBML systems; detailed metric definitions are TODO(reference).
- **Reported.** Six frontier LLMs evaluated; all models' performance declines significantly as system complexity increases.

## Typical Duration

Sequential experiment-design episodes up to an iteration limit (per the official repository).

## Main Contribution

An affordable stand-in for open-ended experimental science: simulated biology that preserves the iterate-experiment-analyze loop wet labs make prohibitively expensive to benchmark.

## Key Design Ideas

- Hidden SBML systems give experiment design a formal, checkable target.
- Sequential interaction makes experiment choice — not just analysis — the evaluated skill.
- A complexity gradient (small to large systems) builds the difficulty ladder into the corpus.

## Strengths

- Open-ended discovery with machine-checkable ground truth.
- The complexity-driven decline localizes where iterative scientific reasoning breaks down.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. Circulating venue-acceptance claims are not verifiable from those sources.

## Related Works

- [MaD Physics](./mad-physics.md) — Also budget-conscious interactive experimentation on simulated systems, in physics.
- [DiscoverPhysics](./discoverphysics.md) — Also iterative experiment design against hidden mechanisms, with paired prediction/explanation scoring.
- [Aviary](./aviary.md) — Also biology-focused interactive environments (cloning, protein engineering) with terminal rewards.
