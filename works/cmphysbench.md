# CMPhysBench (2025)

> **English** | [简体中文](../zh/works/cmphysbench.md)

> **First appeared:** 2025-08-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2508.18124)

## Overview

CMPhysBench is a benchmark of more than 520 meticulously curated graduate-level calculation problems in condensed matter physics, scored with Scalable Expression Edit Distance (SEED), a fine-grained non-binary partial-credit measure over solution expressions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.18124>
- **Code:** <https://github.com/CMPhysBench/CMPhysBench>
- **Venue:** arXiv preprint (cs.LG, cs.AI), 2025

## Summary

CMPhysBench targets condensed matter physics — magnetism, superconductivity, strongly correlated systems, and foundational theoretical frameworks — with calculation-based problems that require the model to generate a comprehensive solution independently rather than select an answer. Its SEED score assigns partial credit by expression similarity, complementing binary accuracy.

## Tasks

More than 520 graduate-level, calculation-based problems curated across condensed matter subfields including magnetism, superconductivity, and strongly correlated systems; each requires independently generating a full solution.

## Domains

Condensed matter physics: magnetism, superconductivity, strongly correlated systems, and foundational theoretical frameworks.

## Evaluation

- **SEED (Scalable Expression Edit Distance)** provides fine-grained, non-binary partial credit over solution expressions.
- **Accuracy** as the percentage of correct solutions.
- **Reported.** Even the best model, Grok-4, reaches only a 36 average SEED score and 28% accuracy.

## Typical Duration

Single-problem derivations; not an interactive agent setting.

## Main Contribution

Brings graduate-level condensed matter physics under quantitative evaluation with a partial-credit expression metric, exposing a large capability gap even for frontier models.

## Key Design Ideas

- Calculation problems demand generated derivations, not multiple-choice recognition.
- SEED's expression-level edit distance grades how close a wrong derivation is, where binary accuracy sees nothing.
- Code and dataset are publicly released.

## Strengths

- Scale (520+ problems) at graduate level within one coherent field.
- Partial credit makes model differences below the all-or-nothing threshold visible.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — Also condensed-matter evaluation, at expert-researcher level with 50 machine-graded problems.
- [PRBench](./prbench.md) — Also physics evaluation beyond exams, via end-to-end reproduction of published research.
- [CFDLLMBench](./cfdllmbench.md) — Also pairs a knowledge tier with partial-credit grading in a physical-simulation field.
