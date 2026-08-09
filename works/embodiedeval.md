# EmbodiedEval (2025)

> **English** | [简体中文](../zh/works/embodiedeval.md)

## Overview

EmbodiedEval evaluates multimodal LLMs as embodied agents in an interactive 3D simulation framework: 328 distinct tasks within 125 varied 3D scenes, spanning navigation, object interaction, social interaction, attribute question answering, and spatial question answering.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2501.11858>
- **Code:** <https://github.com/thunlp/EmbodiedEval>
- **Project:** <https://embodiedeval.github.io>
- **Venue:** arXiv preprint (cs.CV), 2025

## Summary

EmbodiedEval targets breadth of embodied competence in one interactive framework: rather than a single task family, its 328 tasks across 125 scenes mix locomotion, manipulation-style object interaction, socially situated behavior, and two QA families that require acting to answer. MLLMs run as interactive agents in a real-time 3D simulator, and the paper reports a significant shortfall relative to human level.

## Tasks

328 interactive tasks in 125 3D scenes across five categories (navigation, object interaction, social interaction, attribute QA, spatial QA); the MLLM is the full agent. Simulation only.

## Domains

Embodied simulation across diverse 3D scenes — outside the repository's science/engineering domain axis; documented for its evaluation methodology.

## Evaluation

- Unified simulation-and-evaluation framework scoring task completion per category; human-baseline evaluation code ships with the repository.
- **Reported.** MLLMs show a significant shortfall compared to human level; numeric figures are TODO(reference) — not stated in the abstract.

## Typical Duration

Interactive multi-step episodes in real-time simulation.

## Main Contribution

Category breadth as the point: a single interactive framework where navigation, interaction, social behavior, and embodied QA are directly comparable for the same model.

## Key Design Ideas

- Embodied QA families force acting-to-perceive rather than answering from the initial frame.
- 125 scenes push scene diversity as hard as task diversity.
- One unified framework removes cross-benchmark confounds between task categories.

## Strengths

- Among the broadest interactive MLLM embodied evaluations by scene and category coverage.
- Full public stack including human-baseline tooling.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is verifiable from those sources, and numeric results await full-paper validation.
- Simulation-only; no physical robot platform.

## Related Works

- [EmbodiedBench](./embodiedbench.md) — Also interactive MLLM embodied evaluation, organized by capability rather than category.
- [PhysBench](./physbench.md) — Also probes the perception side MLLM embodied agents depend on, as static physical-understanding QA.
- [PARTNR](./partnr.md) — Also simulator-based embodied evaluation, at collaboration scale.
