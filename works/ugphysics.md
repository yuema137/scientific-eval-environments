# UGPhysics (2025)

> **English** | [简体中文](../zh/works/ugphysics.md)

> **First appeared:** 2025-02-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2502.00334)

## Overview

UGPhysics is a comprehensive benchmark for undergraduate physics reasoning: 5,520 problems in both English and Chinese, covering 13 subjects with seven answer types and four distinct physics reasoning skills, all rigorously screened for data leakage, and judged by the MARJ (Model-Assistant Rule-based Judgment) pipeline.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.00334>
- **Code:** <https://github.com/YangLabHKUST/UGPhysics>
- **Venue:** ICML 2025

## Summary

UGPhysics scales systematic physics evaluation to undergraduate breadth: 5,520 bilingual problems over 13 subjects, with answer-type diversity (seven types) that defeats format shortcuts and leakage screening that protects validity. Its MARJ pipeline combines rule-based checking with model assistance, tailored to physics answer correctness. Across 31 leading LLMs, the highest overall accuracy is 49.8% (OpenAI o1-mini) — evidence, the authors argue, that physics reasoning demands more than mathematical ability.

## Tasks

5,520 undergraduate-level physics problems in English and Chinese, spanning 13 subjects, seven answer types, and four physics reasoning skills; static problem solving.

## Domains

Undergraduate physics across 13 subjects; the abstract does not enumerate them.

## Evaluation

- **MARJ (Model-Assistant Rule-based Judgment)** pipeline tailored to physics answer correctness.
- **Reported.** 31 leading LLMs evaluated; highest overall accuracy 49.8% (OpenAI o1-mini).

## Typical Duration

Single-problem solving; not an interactive agent setting.

## Main Contribution

Undergraduate-breadth, bilingual physics evaluation with leakage screening and a physics-specific judgment pipeline, separating physics reasoning from mathematical ability.

## Key Design Ideas

- Seven answer types prevent scoring from collapsing into one gradable format.
- Bilingual construction doubles as a cross-lingual robustness probe.
- MARJ blends rules with model assistance where pure rules cannot parse physics answers.

## Strengths

- Scale and breadth (5,520 problems, 13 subjects) with explicit leakage screening.
- The sub-50% ceiling across 31 models quantifies the physics-beyond-math gap.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CMPhysBench](./cmphysbench.md) — Also large-scale physics problem evaluation with a tailored grading scheme, at graduate level in one subfield.
- [PHYBench](./phybench.md) — Also original physics problems with a custom expression metric, at olympiad difficulty.
- [SeePhys](./seephys.md) — Also broad physics evaluation, with vision-essential multimodal problems.
