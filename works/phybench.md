# PHYBench (2025)

> **English** | [简体中文](../zh/works/phybench.md)

> **First appeared:** 2025-04-22 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2504.16074)

## Overview

PHYBench is a benchmark of 500 original physics problems, ranging from high school to Physics Olympiad difficulty, scored with the Expression Edit Distance (EED) Score — a continuous metric over mathematical expressions that the paper reports improves sample efficiency by 204% over binary scoring.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.16074>
- **Project:** <https://www.phybench.cn/>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks

## Summary

PHYBench evaluates physical perception and multi-step, multi-condition reasoning on problems written originally for the benchmark — a contamination control by construction. Its EED Score grades how close a wrong symbolic answer is instead of scoring all errors identically, and the paper reports the benchmark differentiates models where AIME 2024, OlympiadBench, and GPQA saturate. A human expert baseline anchors the scale: the best model, Gemini 2.5 Pro, reaches 36.9% accuracy against the experts' 61.9%.

## Tasks

500 original physics problems from high-school to Physics Olympiad difficulty; static text problem solving with symbolic answers.

## Domains

Physics problem solving across the high-school-to-Olympiad range; subfield composition is not stated in the abstract.

## Evaluation

- **Expression Edit Distance (EED) Score** over mathematical expressions, improving sample efficiency by a reported 204% over binary scoring; accuracy also reported.
- **Reported.** Best model Gemini 2.5 Pro at 36.9% accuracy versus 61.9% for human experts.

## Typical Duration

Single-problem solving; not an interactive agent setting.

## Main Contribution

Originality as contamination control plus a continuous expression metric, yielding a physics benchmark that still separates frontier models where standard suites saturate.

## Key Design Ideas

- All problems are written for the benchmark, so pretraining exposure is ruled out by construction.
- EED makes partial correctness of symbolic answers measurable.
- A measured human-expert baseline gives the scores an external anchor.

## Strengths

- Strong model separation with only 500 problems, credited to the continuous metric.
- The 25-point human-model gap quantifies remaining headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CMPhysBench](./cmphysbench.md) — Also grades physics answers by expression edit distance (SEED), at graduate level in condensed matter.
- [PhysGym](./physgym.md) — Builds its interactive discovery environments from PHYBench problems.
- [HiPhO](./hipho.md) — Also olympiad-difficulty physics, graded with official human marking schemes.
