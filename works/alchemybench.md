# AlchemyBench (2025)

> **English** | [简体中文](../zh/works/alchemybench.md)

> **First appeared:** 2025-02-23 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2502.16457)

## Overview

AlchemyBench is an end-to-end benchmark for LLM-driven materials synthesis, built on 17,000 expert-verified synthesis recipes from open-access literature: models predict raw materials and equipment, generate the synthesis procedure, and forecast characterization outcomes, graded by an expert-level LLM-as-a-Judge framework.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.16457>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

Published as "Towards Fully-Automated Materials Discovery via Large-Scale Synthesis Dataset and Expert-Level LLM-as-a-Judge," AlchemyBench turns 17,000 expert-verified synthesis recipes into an end-to-end prediction benchmark. Given a target, a model predicts the raw materials and equipment, generates the synthesis procedure, and forecasts characterization outcomes. Because free-form recipes resist exact-match scoring, the benchmark ships an LLM-as-a-Judge evaluation framework that the authors report is in strong statistical agreement with expert assessments.

## Tasks

End-to-end synthesis prediction over 17,000 expert-verified recipes: raw-materials and equipment prediction, synthesis-procedure generation, and characterization-outcome forecasting; static prediction, not interactive.

## Domains

Materials science — inorganic materials synthesis planning, from precursor and equipment selection through procedure and expected characterization.

## Evaluation

- LLM-as-a-Judge scoring of free-form predictions, reported to be in strong statistical agreement with expert assessments.
- **Reported.** No numeric headline in the abstract; the contribution is the dataset plus the validated judge framework.

## Typical Duration

Single-episode end-to-end synthesis predictions; no interactive setting.

## Main Contribution

A synthesis-planning benchmark at recipe scale with a judge validated against experts — making free-form synthesis prediction gradable where exact match cannot work.

## Key Design Ideas

- Recipe-scale expert-verified data grounds the task in real synthesis practice.
- Splitting the task into materials/equipment, procedure, and characterization gives partial credit structure.
- An expert-agreement-validated LLM judge handles the open-ended outputs.

## Strengths

- Large expert-verified recipe corpus underpinning an end-to-end task.
- The judge's reported expert agreement addresses the core scoring problem for synthesis.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); the paper is under review with no formal venue, and no code/dataset URL is verifiable from the arXiv page. The benchmark relies on an LLM-as-a-Judge; its expert agreement is reported qualitatively.

## Related Works

- [ChemCensor / CREED](./chemcensor.md) — Also synthesis-adjacent evaluation (retrosynthesis) where many valid answers defeat exact match.
- [AutoDFT / VASPBench](./vaspbench.md) — Also materials-workflow evaluation, on the computational rather than synthesis side.
- [Materials Hypothesis Generation](./materials-hypothesis.md) — Also LLM-driven materials discovery, at the hypothesis rather than synthesis stage.
