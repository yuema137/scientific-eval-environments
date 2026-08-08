# scBench (2026)

> **English** | [简体中文](../zh/works/scbench.md)

## Overview

scBench evaluates AI agents on single-cell RNA-seq analysis: 394 verifiable problems spanning six sequencing platforms and seven task categories, each handing the agent a snapshot of experimental data immediately prior to an analysis step and grading recovery of a key biological result deterministically.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.09063>
- **Venue:** arXiv preprint (q-bio.GN, cs.AI), 2026

## Summary

scBench isolates single analysis steps on real scRNA-seq data: the agent receives the data as it stood just before a step and must perform the analysis that recovers a known biological result, scored by a deterministic grader. Across eight frontier models, accuracy ranges from 29–53% with strong model-task and model-platform interactions — platform choice affects accuracy as much as model choice, with 40+ percentage-point drops on less-documented technologies. The benchmark complements SpatialBench to cover the two dominant single-cell modalities.

## Tasks

394 verifiable scRNA-seq analysis problems across six sequencing platforms and seven task categories, each starting from a pre-step data snapshot.

## Domains

Single-cell RNA sequencing analysis across six sequencing platforms.

## Evaluation

- Deterministic grader evaluating recovery of a key biological result; accuracy as the metric.
- **Reported.** Eight frontier models range from 29–53% accuracy; platform choice matters as much as model choice, with 40+ point drops on less-documented technologies.

## Typical Duration

Single analysis-step episodes on real datasets.

## Main Contribution

Deterministic, snapshot-based grading for real single-cell analysis, revealing that agent competence is a property of the model-platform pair rather than the model alone.

## Key Design Ideas

- The pre-step snapshot design pins down exactly which analysis capability each problem measures.
- Deterministic grading removes judge noise from a domain full of defensible-looking wrong analyses.
- Platform diversity turns tool-documentation coverage into a measured variable.

## Strengths

- Verifiability at scale (394 problems) on real, not synthetic, data.
- The platform-effect finding (40+ points) is directly actionable for deployment.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [SpatialBench](./spatialbench.md) — The sibling benchmark covering the spatial modality with the same snapshot-and-deterministic-grading design.
- [scBench-Long](./scbench-long.md) — The long-horizon extension: recover published conclusions from near-raw data.
- [HeurekaBench](./heurekabench.md) — Also single-cell agent evaluation, via open-ended questions judged against published findings.
