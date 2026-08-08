# FGBench (2025)

> **English** | [简体中文](../zh/works/fgbench.md)

## Overview

FGBench evaluates molecular property reasoning at functional-group granularity: 625K generated problems annotated with which of 245 functional groups drive a property difference, with a 7K curated subset used to benchmark state-of-the-art LLMs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.01055>
- **Code:** <https://github.com/xuanliugit/FGBench>
- **Dataset:** <https://huggingface.co/datasets/xuan-liu/FGBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

FGBench asks not just whether a model predicts a molecular property but whether it can reason about *why* — localized to functional groups. The dataset comprises 625K property-reasoning problems covering 245 functional groups in three settings: single functional-group impacts, multiple functional-group interactions, and direct molecular comparisons, spanning both regression and classification. Benchmarking on 7K curated problems shows current LLMs struggle with functional-group-level property reasoning.

## Tasks

625K molecular property-reasoning problems (245 functional groups; single-impact, interaction, and molecular-comparison settings); a curated 7K subset serves as the LLM benchmark. Static QA with regression and classification targets.

## Domains

Chemistry — structure–property relationships at functional-group level, motivated by molecular design and drug discovery.

## Evaluation

- Regression and classification scoring against dataset labels, with functional-group annotations enabling reasoning-level analysis.
- **Reported.** Current LLMs struggle with functional-group-level property reasoning; no single headline number in the abstract.

## Typical Duration

Single-turn problems; no interactive setting.

## Main Contribution

Shifting property-prediction evaluation from whole-molecule answers to functional-group-localized reasoning, with a data-generation framework that scales the format to 625K problems.

## Key Design Ideas

- Functional groups are the explanatory unit chemists actually use — the benchmark tests that vocabulary directly.
- Interaction problems separate additive reasoning from genuine multi-group understanding.
- A generation framework plus curated evaluation subset decouples training-scale data from benchmark quality.

## Strengths

- Fine-grained attribution: failures localize to specific groups and interaction types.
- Verified NeurIPS Datasets and Benchmarks acceptance with public code and data.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); metric details beyond regression/classification framing await full-paper validation.

## Related Works

- [MolecularIQ](./moleculariq.md) — Also structure-grounded chemical reasoning, verified symbolically on the molecular graph.
- [ChemCoTBench](./chemcotbench.md) — Also decomposes chemical reasoning into checkable units, at the operation level.
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — Also property-aware molecule tasks, in the generative direction.
