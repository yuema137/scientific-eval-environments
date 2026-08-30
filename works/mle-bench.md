# MLE-bench (2024)

> **English** | [简体中文](../zh/works/mle-bench.md)

> **First appeared:** 2024-10-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2410.07095)

## Overview

MLE-bench evaluates machine-learning agents on machine-learning engineering: 75 ML-engineering competitions curated from Kaggle, where agents train models, prepare datasets, and run experiments to produce submissions graded against real Kaggle leaderboards — with OpenAI's o1-preview (AIDE scaffolding) reaching at least bronze-medal level on 16.9% of competitions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07095>
- **Code:** <https://github.com/openai/mle-bench/>
- **Venue:** ICLR 2025

## Summary

MLE-bench (from OpenAI) measures whether agents can do the end-to-end work of a machine-learning engineer. It curates 75 ML-engineering competitions from Kaggle, each with real datasets, and establishes human baselines from Kaggle's public leaderboards, grading agent submissions against Kaggle medal thresholds (bronze/silver/gold). Agents run inside open-source scaffolds (e.g., AIDE) and must train models, prepare data, and iterate on experiments. The headline: OpenAI's o1-preview with AIDE scaffolding reaches at least a Kaggle bronze medal on 16.9% of competitions; the paper also studies resource scaling and pre-training contamination.

## Tasks

75 curated Kaggle ML-engineering competitions; the agent performs end-to-end ML engineering (data preparation, model training, experimentation) and submits a solution graded against the competition leaderboard. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — machine-learning engineering: building and training models to compete on real Kaggle tasks.

## Evaluation

- Kaggle-leaderboard human baselines and medal thresholds (bronze/silver/gold) per competition; resource-scaling and contamination analyses.
- **Reported.** OpenAI o1-preview with AIDE scaffolding reaches at least bronze-medal level on 16.9% of competitions.

## Typical Duration

Long-horizon end-to-end episodes per competition (multi-step data prep, training, and iteration).

## Main Contribution

The reference benchmark for autonomous ML engineering — grounding agent capability in real Kaggle competitions with medal-level human baselines rather than synthetic tasks.

## Key Design Ideas

- Kaggle leaderboards supply authentic, quantitative human baselines and medal thresholds.
- Offline curation of 75 competitions makes the suite reproducible and gradable.
- Explicit contamination and resource-scaling studies pre-empt the obvious confounds.

## Strengths

- Real competitions with medal-anchored scoring; open-sourced by OpenAI and widely adopted (e.g., as a substrate for MLE-Dojo and AIDE).
- The 16.9%-bronze result is a clear, citable capability marker for ML-engineering agents.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); arXiv Comments state "ICLR version" (ICLR 2025); the exact count of evaluated models is not in the abstract.

## Related Works

- [MLE-Dojo](./mle-dojo.md) — Builds an interactive Gym-style environment reusing MLE-bench competitions among 200+ Kaggle challenges.
- [MLAgentBench](./mlagentbench.md) — Also evaluates agents on ML experimentation, on 13 improve-the-metric tasks.
- [DSBench](./dsbench.md) — Also agentic data-science evaluation, on analysis and modeling tasks.
