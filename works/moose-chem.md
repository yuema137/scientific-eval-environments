# MOOSE-Chem (2024)

> **English** | [简体中文](../zh/works/moose-chem.md)

## Overview

MOOSE-Chem evaluates whether LLMs can rediscover unseen chemistry hypotheses: a benchmark of 51 high-impact chemistry papers published after January 2024, each manually annotated by PhD chemists with background, inspirations, and hypothesis, paired with an agentic framework that retrieves inspirations, composes hypotheses, and ranks them.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07076>
- **Code:** <https://github.com/ZonglinY/MOOSE-Chem>
- **Venue:** ICLR 2025

## Summary

MOOSE-Chem decomposes hypothesis discovery mathematically into three subtasks — retrieving inspirations, composing hypotheses with those inspirations, and ranking the results — and implements the decomposition as an agentic LLM framework. To test it without contamination, the benchmark uses 51 post-January-2024 high-impact chemistry papers (expert-annotated into background, inspirations, hypothesis) and an LLM whose knowledge cutoff precedes 2024. The framework rediscovers many hypotheses with high similarity to the ground truth, with surprisingly high accuracy on inspiration retrieval.

## Tasks

Rediscovery tasks over 51 expert-annotated chemistry papers: from a paper's background and an inspiration corpus (3,000 papers in the official release), regenerate the paper's hypothesis. Multi-stage agentic pipeline, not environment-interactive.

## Domains

Chemistry — hypothesis discovery across chemistry without restriction on subdomain, benchmarked on recent high-impact literature.

## Evaluation

- Similarity of rediscovered hypotheses to the annotated ground-truth hypothesis, with per-subtask assessment (retrieval, composition, ranking); contamination controlled via a pre-2024 knowledge cutoff.
- **Reported.** Many hypotheses rediscovered with high similarity to ground truth; surprisingly high accuracy on inspiration retrieval. Quantitative figures are TODO(reference) — not stated in the abstract.

## Typical Duration

Multi-stage pipeline episodes per paper (retrieve → compose → rank).

## Main Contribution

A contamination-controlled rediscovery protocol for scientific hypothesis generation: recent expert-annotated papers plus a knowledge-cutoff model make "could the machine have found this?" a measurable question.

## Key Design Ideas

- The background/inspirations/hypothesis annotation scheme turns discovery into a decomposable, gradable pipeline.
- Post-cutoff papers with a pre-cutoff model give a clean no-memorization guarantee.
- Ranking as an explicit subtask measures whether systems can recognize their own best hypotheses.

## Strengths

- PhD-chemist annotation of all 51 papers grounds the ground truth in expert judgment.
- The decomposition makes partial credit meaningful — retrieval, composition, and ranking fail independently.

## Limitations

- Repository note: the paper's primary contribution is the MOOSE-Chem agentic framework; the 51-paper benchmark was constructed to evaluate it. This card covers the benchmark; the framework is a paired method.
- Repository note: card compiled from the arXiv abstract and official repository (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [ResearchClawBench](./researchclawbench.md) — Also rediscovery of hidden published findings, end-to-end across ten domains.
- [HeurekaBench](./heurekabench.md) — Also evaluates regenerating published scientific findings, judged against the papers.
- [MolQuest](./molquest.md) — Also abductive chemical reasoning, at the structure-elucidation scale.
