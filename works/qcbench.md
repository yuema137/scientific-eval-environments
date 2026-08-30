# QCBench (2025)

> **English** | [简体中文](../zh/works/qcbench.md)

> **First appeared:** 2025-08-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2508.01670)

## Overview

QCBench evaluates LLMs on domain-specific quantitative chemistry: 350 computational problems across 7 chemistry subfields in three difficulty tiers, structured to prevent heuristic shortcuts and demand explicit step-by-step numerical reasoning.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.01670>
- **Code:** <https://github.com/jiaqingxie/QCBench>
- **Venue:** arXiv preprint (cs.AI), 2025 (Comments state a revision at the Journal of Chemical Information and Modeling)

## Summary

QCBench targets the gap between language fluency and scientific computation: 350 quantitative problems spanning analytical, bio/organic, general, inorganic, physical, polymer, and quantum chemistry, tiered as easy, medium, and difficult. Problems are constructed so heuristic pattern-matching fails and explicit numerical work is required. Evaluations of 24 LLMs show consistent performance degradation as task complexity increases.

## Tasks

350 computational chemistry problems across 7 subfields (analytical, bio/organic, general, inorganic, physical, polymer, quantum chemistry) in three difficulty tiers; static step-by-step calculation, no tools.

## Domains

Chemistry — quantitative and computational chemistry across seven named subfields.

## Evaluation

- Tiered accuracy on stepwise numerical calculation, supporting fine-grained diagnosis of computational weaknesses across difficulty levels.
- **Reported.** Consistent performance degradation with increasing task complexity across 24 evaluated LLMs.

## Typical Duration

Single-turn calculation problems; no interactive setting.

## Main Contribution

Isolating numerical chemical computation as its own measured capability, with shortcut-resistant construction and a subfield × difficulty grid that locates where calculation breaks down.

## Key Design Ideas

- Problems are structured so the answer cannot be reached without doing the calculation.
- Seven subfields separate "knows the chemistry" failures from "cannot compute" failures.
- Difficulty tiers turn one benchmark into a degradation curve.

## Strengths

- Covers quantitative chemistry breadth that structure- and QA-centric benchmarks skip.
- 24-model evaluation gives the degradation finding unusual coverage.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); details beyond those sources await full-paper validation. The JCIM status in arXiv Comments is "revision", not acceptance.

## Related Works

- [ChemIQ](./chemiq.md) — Also tool-free chemistry evaluation with programmatic checking, on structure rather than calculation.
- [HARDMath](./hardmath.md) — Also multi-step applied quantitative problems designed against shortcut solutions.
- [CMPhysBench](./cmphysbench.md) — Also graduate-level calculation problems in a physical science, with partial-credit scoring.
