# ReplicationBench (2025)

> **English** | [简体中文](../zh/works/replicationbench.md)

> **First appeared:** 2025-10-28 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.24591)

## Overview

ReplicationBench is an evaluation framework asking whether AI agents can replicate astrophysics research papers: each paper is split into tasks requiring agents to replicate its core contributions — experimental setup, derivations, data analysis, and codebase — with every task co-developed with the original paper authors.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.24591>
- **Code:** <https://github.com/Christine8888/replicationbench-release>
- **Venue:** arXiv preprint (cs.CL, astro-ph.IM), 2025

## Summary

ReplicationBench treats paper replication as the unit of evaluation in astrophysics, a data-driven science. Agents work in computational sandboxes on tasks that target a key scientific result each; because tasks are co-developed with the original authors, both faithfulness (adherence to original methods) and correctness (technical accuracy of results) can be objectively scored. The dataset comprises 111 replication tasks spanning 20 research papers (per the official repository). Even the best-performing language models score under 20%.

## Tasks

111 astrophysics replication tasks spanning 20 research papers (official repository), each targeting a key scientific result and covering experimental setup, derivations, data analysis, and codebase; run in computational sandboxes.

## Domains

Astrophysics research workflows, as a testbed for data-driven science.

## Evaluation

- Dual-axis objective scoring per task: **faithfulness** to the original methods and **correctness** of the technical results, enabled by author-co-developed task definitions.
- **Reported.** Even the best-performing language models score under 20%.

## Typical Duration

Sandboxed multi-step replication workflows per task; budgets are TODO(reference).

## Main Contribution

Makes author-co-developed replication the ground truth for agent evaluation in astrophysics, separating faithfulness to method from correctness of result.

## Key Design Ideas

- Original paper authors co-develop the tasks, so "what counts as replication" is set by the people who did the work.
- Faithfulness and correctness are scored as distinct axes rather than folded into one number.
- Trajectory analysis identifies where agent workflows break down.

## Strengths

- Author involvement gives unusually authoritative ground truth for replication.
- The sub-20% ceiling documents substantial headroom on real research workflows.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [PRBench](./prbench.md) — Also end-to-end paper reproduction in physics, with expert-written weighted rubrics.
- [EXP-Bench](./exp-bench.md) — Also replicates published experiments end to end, for AI-research papers.
- [Stargazer](./stargazer.md) — Also evaluates agents on real astrophysical analysis, via archival exoplanet systems.
