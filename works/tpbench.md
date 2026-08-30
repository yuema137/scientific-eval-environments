# TPBench (2025)

> **English** | [简体中文](../zh/works/tpbench.md)

> **First appeared:** 2025-02-19 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2502.15815)

## Overview

TPBench (Theoretical Physics Benchmark) is a dataset and study of AI reasoning in theoretical physics: 57 novel problems ranging from undergraduate to research level in high-energy theory and cosmology, built to be auto-verifiable and absent from public problem collections.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.15815>
- **Project:** <http://tpbench.org>
- **Venue:** Machine Learning: Science and Technology, 2025

## Summary

TPBench targets the gap between exam physics and the problems theorists actually work on: its 57 problems are novel — not drawn from public collections — and span undergraduate through research difficulty in high-energy theory and cosmology. The paper addresses the challenges of auto-verifiability and grading at this level and analyzes common failure modes of evaluated models (o3-mini, o1, DeepSeek-R1, GPT-4o, and Llama and Qwen variants). Research-level problems remain mostly unsolved, leading the authors to conclude current models are still of limited use to researchers.

## Tasks

57 novel theoretical-physics problems, undergraduate to research level, in high-energy theory and cosmology; static problem solving with auto-verifiable answers.

## Domains

Theoretical physics: high-energy theory and cosmology.

## Evaluation

- Auto-verifiable answer checking with grading tailored to theoretical-physics derivations; failure-mode analysis.
- **Reported.** Research-level problems are mostly unsolved by the evaluated models.

## Typical Duration

Single-problem theoretical derivations; not an interactive agent setting.

## Main Contribution

Extends auto-verifiable physics evaluation into genuinely novel theory problems at research difficulty, where contamination from public problem collections is ruled out by construction.

## Key Design Ideas

- Problems are authored to be novel, so performance cannot come from retrieval of known solutions.
- Difficulty is graded from undergraduate to research level within one coherent theory domain.
- Auto-verifiability is treated as a design problem for symbolic theory answers, not an afterthought.

## Strengths

- A difficulty ladder inside theoretical physics rather than a single difficulty tier.
- Failure-mode analysis accompanies the scores.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — Also researcher-level physics with machine grading, in condensed matter theory.
- [CritPt](./critpt.md) — Also research-level, contamination-proof physics challenges, across 11+ subfields.
- [UGPhysics](./ugphysics.md) — Also systematic physics problem evaluation, at undergraduate breadth with a rule-based/model judgment pipeline.
