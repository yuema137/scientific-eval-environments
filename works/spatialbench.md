# SpatialBench (2025)

> **English** | [简体中文](../zh/works/spatialbench.md)

## Overview

SpatialBench asks whether agents can analyze real-world spatial biology data: 146 verifiable problems across five spatial technologies and seven task categories, graded deterministically on recovery of a key biological result from a pre-step data snapshot.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.21907>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

SpatialBench applies the snapshot-and-deterministic-grader design to spatial transcriptomics: agents receive experimental data immediately prior to an analysis step and must recover a known biological result. Base-model accuracy remains low — 20–38% across model families — with strong model-task and model-platform interactions, and the paper argues that harness design (tools, prompts, control flow, execution environment) has a large empirical effect and should be evaluated and improved as a first-class object.

## Tasks

146 verifiable spatial-biology analysis problems across five spatial technologies and seven task categories, each starting from a pre-step data snapshot.

## Domains

Spatial transcriptomics and spatial biology across five technologies; sibling of scBench on the single-cell side.

## Evaluation

- Deterministic grader evaluating recovery of a key biological result; accuracy as the metric.
- **Reported.** Base-model accuracy is 20–38% across model families, with strong model-task and model-platform interactions; harness design has a large empirical effect.

## Typical Duration

Single analysis-step episodes on real spatial datasets.

## Main Contribution

Extends verifiable agent evaluation to spatial biology and elevates the harness to a first-class evaluated object rather than an implementation detail.

## Key Design Ideas

- The same snapshot design as scBench keeps the two dominant single-cell modalities comparable.
- Deterministic grading over real datasets, not synthetic ones.
- Harness variation is measured, echoing that capability is a property of the model-harness pair.

## Strengths

- Covers five spatial technologies whose tooling maturity differs sharply.
- The harness-effect finding gives practitioners an actionable lever beyond model choice.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [scBench](./scbench.md) — The scRNA-seq sibling covering the other dominant single-cell modality.
- [scBench-Long](./scbench-long.md) — The long-horizon extension of this benchmark family.
- [Harness-Bench](./harness-bench.md) — Also treats the harness as the studied variable, for general agent workflows.
