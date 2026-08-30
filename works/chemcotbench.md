# ChemCoTBench (2025)

> **English** | [简体中文](../zh/works/chemcotbench.md)

> **First appeared:** 2025-05-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.21318)

## Overview

ChemCoTBench moves chemical evaluation beyond QA by framing molecular transformations as modular chemical operations — addition, deletion, substitution — so that problem-solving becomes a transparent, step-by-step workflow: 1,495 samples across 22 tasks in molecular property optimization and chemical reaction prediction.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.21318>
- **Code:** <https://github.com/IDEA-XL/ChemCoTBench/>
- **Dataset:** <https://huggingface.co/datasets/OpenMol/ChemCoTBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

Published as "Beyond Chemical QA: Evaluating LLM's Chemical Reasoning with Modular Chemical Operations", ChemCoTBench decomposes chemistry problems into explicit operation sequences over molecules, making the reasoning chain itself evaluable rather than only the final answer. The benchmark contains 1,495 samples across 22 chemical tasks centered on molecular property optimization and reaction prediction, ships a reasoning taxonomy and baseline evaluations, and is paired with ChemCoTDataset, a 22,000-instance chain-of-thought training set.

## Tasks

1,495 benchmark samples across 22 chemical tasks (per the paper's full text) in two families — molecular property optimization and chemical reaction prediction — posed as step-by-step modular-operation workflows; static reasoning, not interactive.

## Domains

Chemistry — molecular optimization and reaction prediction, with drug design and reaction engineering as the stated application areas.

## Evaluation

- Structured evaluation over annotated operation workflows, with a reasoning taxonomy and baseline evaluations; step-level structure makes intermediate reasoning checkable.
- **Reported.** No headline numbers in the abstract; roughly 20 models across reasoning, general, and biomolecular-specialized categories are evaluated per the full text.

## Typical Duration

Single-episode step-by-step reasoning; no environment interaction.

## Main Contribution

Recasting chemical problem-solving as sequences of modular operations, which turns opaque end-to-end predictions into workflows whose intermediate steps can be evaluated.

## Key Design Ideas

- Operations (add/delete/substitute) are the unit of reasoning, mirroring how chemists actually edit molecules.
- A reasoning taxonomy separates failure at the operation level from failure at the plan level.
- The paired ChemCoTDataset (22K instances) makes the format trainable, not just testable.

## Strengths

- Step-wise evaluability addresses the core weakness of answer-only chemical QA.
- Verified NeurIPS Datasets and Benchmarks acceptance with public code and data.

## Limitations

- Repository note: card compiled from the arXiv abstract, full text, and official repositories (August 2026); the task and sample counts come from the paper's full text, not the abstract.

## Related Works

- [ChemEval](./chemeval.md) — Also structures chemical evaluation beyond flat QA, via capability levels rather than operations.
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — Also evaluates molecule editing and optimization, from open-domain natural-language instructions.
- [FukuyamaBench](./fukuyamabench.md) — Also step-structured reaction reasoning, at the level of elementary mechanisms.
