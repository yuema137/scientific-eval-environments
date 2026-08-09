# DSBench (2024)

> **English** | [简体中文](../zh/works/dsbench.md)

## Overview

DSBench asks how far data-science agents are from becoming data-science experts: 540 tasks — 466 data-analysis and 74 data-modeling — with long contexts, multimodal backgrounds, and multi-table data sourced from competition platforms and Kaggle, where the best agent solves only 34.12% of analysis tasks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.07703>
- **Code:** <https://github.com/LiqiangJing/DSBench>
- **Project:** <https://liqiangjing.github.io/dsbench.github.io/>
- **Venue:** ICLR 2025 (per the official repository; arXiv metadata carries no venue)

## Summary

DSBench brings realistic complexity to data-science-agent evaluation: 466 data-analysis and 74 data-modeling tasks (540 total) drawn from competition sources and Kaggle, with long textual contexts, images and tables, and multi-table data. Given a task instruction (possibly with images and tables) and data files, the agent must produce a solution that resolves the task. The results show a wide gap to expertise: the best agent solves only 34.12% of data-analysis tasks and shows a 34.74% relative performance gap on modeling.

## Tasks

540 data-science tasks (466 analysis + 74 modeling) with long contexts, multimodal backgrounds, and multi-table data; agents produce solutions from instructions and data files.

## Domains

AI & Machine Learning Research — data science: end-to-end data analysis and predictive modeling on realistic, multimodal tasks.

## Evaluation

- Task-solve rate for analysis; relative performance gap (RPG) for modeling.
- **Reported.** Best agent solves 34.12% of analysis tasks with a 34.74% relative performance gap on modeling.

## Typical Duration

Per-task solution episodes over multimodal, multi-table data.

## Main Contribution

A realistically hard data-science benchmark — long-context, multimodal, multi-table — that quantifies how far agents remain from expert-level analysis and modeling.

## Key Design Ideas

- Multimodal, multi-table tasks reflect real data-science messiness, not clean toy tables.
- Separating analysis from modeling isolates two distinct competences.
- The relative-performance-gap metric grades modeling against a meaningful reference.

## Strengths

- Larger and more realistic than earlier data-analysis QA sets, with a public release.
- The 34% ceiling is a clear, citable marker of the expertise gap.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the ICLR 2025 venue is a repository claim, not in arXiv metadata. Task provenance is described as competition sources and Kaggle (a "ModelOff"/"Eloquence" naming appears across sources).

## Related Works

- [DA-Code](./da-code.md) — Also agentic data-science evaluation, focused on code generation in a sandbox.
- [BLADE](./blade.md) — Also data-driven-science analysis, grounded in expert reference analyses.
- [MLE-bench](./mle-bench.md) — Also Kaggle-grounded agent evaluation, on ML engineering with medal scoring.
