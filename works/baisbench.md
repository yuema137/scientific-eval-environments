# BAISBench (2025)

> **English** | [简体中文](../zh/works/baisbench.md)

## Overview

BAISBench benchmarks AI scientists on omics-data-driven biological discovery through two tasks: cell type annotation across 15 expert-labeled single-cell datasets, and scientific discovery via 193 multiple-choice questions derived from the biological conclusions of 41 published single-cell studies — with a human baseline from six graduate-level bioinformaticians.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.08341>
- **Code:** <https://github.com/EperLuo/BAISBench>
- **Dataset:** <https://huggingface.co/datasets/EperLuo/BaisBench>
- **Venue:** arXiv preprint (cs.AI, cs.MA, q-bio.GN), 2025

## Summary

BAISBench holds AI scientists to what real studies concluded: systems analyze the actual single-cell transcriptomic datasets behind 41 published studies and must both annotate cell types (scored against a hierarchical cell-type tree per the official repository) and answer discovery questions whose answers are the studies' reported conclusions. Six graduate-level bioinformaticians provide the human reference. Evaluated AI scientists fall short of fully autonomous biological discovery.

## Tasks

Two tasks over real single-cell data: cell type annotation on 15 expert-labeled datasets, and 193 discovery multiple-choice questions derived from 41 published studies.

## Domains

Single-cell transcriptomics and omics-driven biological discovery.

## Evaluation

- Annotation scored against expert labels using a hierarchical cell-type tree (official repository); discovery scored by MCQ correctness against published conclusions.
- **Reported.** Current AI scientists fall short of fully autonomous biological discovery; the human baseline comes from six graduate-level bioinformaticians.

## Typical Duration

Dataset-level analysis episodes; not an interactive environment.

## Main Contribution

Evaluates the "AI scientist" claim against the two things a discovery must get right in single-cell biology — correct cell identities and the study's actual conclusions — with a measured human reference.

## Key Design Ideas

- Discovery questions are anchored to published conclusions, so the target is real science rather than plausible analysis.
- The hierarchical cell-type tree grades annotation at the right granularity instead of exact-string matching.
- A same-task human baseline makes "falls short" a measured statement.

## Strengths

- Direct human-expert comparison on identical tasks.
- Data-driven: systems must work from the datasets, not from the papers.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [scBench-Long](./scbench-long.md) — Also recovers published single-cell conclusions from data, with deterministic long-horizon grading.
- [HeurekaBench](./heurekabench.md) — Also derives discovery questions from published single-cell studies, judged open-endedly.
- [SciAgentArena](./sciagentarena.md) — Also biomedical discovery-task evaluation with expert-designed verification.
