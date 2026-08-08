# PaperBench (2025)

> **English** | [简体中文](../zh/works/paperbench.md)

## Overview

PaperBench evaluates whether AI agents can replicate state-of-the-art AI research: agents must replicate 20 ICML 2024 Spotlight and Oral papers from scratch — understanding the contributions, developing a codebase, and executing experiments — graded against author-co-developed hierarchical rubrics totaling 8,316 individually gradable tasks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.01848>
- **Code:** <https://github.com/openai/preparedness>
- **Venue:** arXiv preprint (cs.AI, cs.CL), 2025

## Summary

PaperBench makes replication objectively gradable by decomposing each paper into a hierarchical rubric of sub-tasks with clear grading criteria, co-developed with the paper's own authors. An LLM-based judge grades replication attempts against the rubrics at scale, and the judge itself is assessed on a separate judge benchmark. The best-performing tested agent, Claude 3.5 Sonnet (New) with open-source scaffolding, reaches an average replication score of 21.0%, and recruited top ML PhDs still outperform the models on the attempted subset.

## Tasks

Replication of 20 ICML 2024 Spotlight and Oral papers from scratch, decomposed into 8,316 individually gradable rubric tasks spanning comprehension, codebase development, and experiment execution.

## Domains

AI research (machine learning): replication of ICML 2024 papers.

## Evaluation

- Author-co-developed hierarchical rubrics; an LLM-based judge grades attempts, with the judge's own performance measured on a separate judge benchmark.
- **Reported.** Best tested agent, Claude 3.5 Sonnet (New) with open-source scaffolding, scores 21.0% on average; models do not yet outperform the ML-PhD human baseline.

## Typical Duration

From-scratch paper replication sessions including code development and experiment execution; budgets are TODO(reference).

## Main Contribution

Hierarchical, author-co-developed rubrics that turn "did the agent replicate the paper" into thousands of objectively gradable sub-judgments — with the grading judge itself benchmarked.

## Key Design Ideas

- Rubric co-development with the original authors fixes what counts as replication.
- Hierarchical decomposition yields partial credit at fine grain instead of a single replication bit.
- A separate judge benchmark makes the automated grader's reliability a measured quantity.

## Strengths

- 8,316 gradable nodes give unusually fine resolution on where replication fails.
- A concurrent expert-human baseline anchors the model scores.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [ReplicationBench](./replicationbench.md) — Also author-co-developed paper replication, for astrophysics rather than AI research.
- [PRBench](./prbench.md) — Also rubric-scored paper reproduction, in physics.
- [CORE-Bench](./core-bench.md) — Also targets reproducibility, from provided code and data rather than from scratch.
