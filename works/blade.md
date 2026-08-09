# BLADE (2024)

> **English** | [简体中文](../zh/works/blade.md)

## Overview

BLADE benchmarks language-model agents for data-driven science: 12 datasets paired with research questions drawn from scientific literature, with ground truth from independent analyses by expert data scientists, evaluating whether agents can integrate domain knowledge, statistics, and data understanding in open-ended analysis.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2408.09667>
- **Code:** <https://github.com/behavioral-data/BLADE>
- **Project:** <https://blade-bench.github.io/>
- **Venue:** EMNLP 2024 (Findings)

## Summary

BLADE evaluates the judgment that data-driven science requires: given 12 datasets and research questions from the scientific literature, agents interacting with the data must select conceptual constructs, transformations, and statistical models to answer open-ended questions. Ground truth comes from independent analyses by expert data scientists, and BLADE's automatic evaluation grades the multifaceted analytical decisions agents make. The finding is nuanced: agents that interact with the underlying data show improved but still non-optimal diversity in their analytical choices compared to base language models.

## Tasks

12 datasets with research questions from the scientific literature; agents perform open-ended data analysis (choosing constructs, transformations, statistical models), evaluated against expert ground-truth analyses.

## Domains

AI & Machine Learning Research — data-driven scientific analysis: statistically and conceptually grounded open-ended analysis.

## Evaluation

- Automatic multifaceted evaluation of analytical decisions against independent expert analyses (with diversity measures).
- **Reported.** Data-interacting agents show improved but non-optimal diversity in analytical decision-making versus base LMs; no single headline accuracy in the abstract.

## Typical Duration

Open-ended analysis episodes per dataset/research question.

## Main Contribution

Grading the analytical judgment of data-science agents — which constructs, transformations, and models they choose — against expert analyses, rather than a single numeric answer.

## Key Design Ideas

- Expert independent analyses as ground truth capture the space of defensible choices.
- Multifaceted evaluation grades decision quality and diversity, not just a final number.
- Data-interacting agents vs. base LMs isolates the value of engaging the data.

## Strengths

- Evaluates open-ended analytical judgment, the crux of real data-driven science.
- Venue-verified with a public repository and project site.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the abstract states 12 datasets while the repository lists additional named datasets — treat 12 as the paper's figure. "Findings" is a repository qualifier.

## Related Works

- [DSBench](./dsbench.md) — Also data-science agent evaluation, on analysis and modeling tasks.
- [DA-Code](./da-code.md) — Also data-science agents, focused on executable code generation.
- [MLR-Bench](./mlr-bench.md) — Also open-ended ML research evaluation, at the full-pipeline scale.
