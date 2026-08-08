# BioXArena (2026)

> **English** | [简体中文](../zh/works/bioxarena.md)

## Overview

BioXArena benchmarks LLM agents on multi-modal biomedical machine-learning tasks: 76 end-to-end tasks across 9 domains — sequence modeling, single-cell analysis, structural biology, network biology, chemical biology, perturbation dynamics, phenotype-disease modeling, biomedical imaging, and text-integrated learning — run in a standardized 2-hour single-GPU environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.15766>
- **Code:** <https://github.com/mbzuai-ai4bio/BioXArena>
- **Dataset:** <https://huggingface.co/datasets/mbzuai-ai4bio/BioXArena-Data-Public>
- **Project:** <https://mbzuai-ai4bio.github.io/BioXArena-ProjectPage/>
- **Venue:** arXiv preprint (cs.CE), 2026

## Summary

BioXArena's agents must write executable code, train predictive models, and generate submissions for private test samples — full ML-engineering loops on biomedical data curated from primary sources. A unified evaluation framework scores submissions with hidden labels, held-out graders, and biology-aware metrics normalized to a 0–1 scale. Across 11 agent configurations, MLEvolve with Gemini-3.1-Pro achieves the highest average score of 0.666, followed by GPT-5.4 at 0.636, while no single agent consistently dominates across all domains.

## Tasks

76 end-to-end biomedical ML tasks across 9 domains; agents build and train models against private test samples within a standardized 2-hour, single-GPU budget.

## Domains

Nine biomedical domains: sequence modeling, single-cell analysis, structural biology, network biology, chemical biology, perturbation dynamics, phenotype-disease modeling, biomedical imaging, and text-integrated learning.

## Evaluation

- Hidden labels with held-out graders; biology-aware metrics normalized to 0–1.
- **Reported.** Best average score 0.666 (MLEvolve with Gemini-3.1-Pro), then 0.636 (GPT-5.4), across 11 agent configurations; no agent dominates all domains.

## Typical Duration

2-hour single-GPU episodes per task (standardized compute budget).

## Main Contribution

Standardized-compute, hidden-label evaluation of agents as biomedical ML engineers, with domain-normalized metrics that make nine heterogeneous biology areas comparable on one scale.

## Key Design Ideas

- Private test labels close the leakage channel that public biomedical datasets leave open.
- The fixed 2h/1-GPU budget makes efficiency part of the measured object.
- Biology-aware metrics keep scores meaningful per domain before normalization.

## Strengths

- Breadth across nine biomedical modalities under one protocol.
- The no-dominant-agent finding cautions against single-leaderboard readings.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [MedAgentGym](./medagentgym.md) — Also sandbox-executed biomedical coding at scale, oriented to verifiable per-task ground truth.
- [AIRS-Bench](./airs-bench.md) — Also end-to-end ML-research tasks with outcome-only execution scoring.
- [AstaBench](./astabench.md) — Also standardized-environment scientific evaluation with cost accounting.
