# MLE-Dojo (2025)

> **English** | [简体中文](../zh/works/mle-dojo.md)

## Overview

MLE-Dojo is a Gym-style interactive environment for training, evaluating, and improving autonomous LLM agents on machine-learning engineering: 200+ real-world Kaggle challenges with structured feedback loops covering data processing, architecture search, hyperparameter tuning, and code debugging, evaluated across eight frontier LLMs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07782>
- **Code:** <https://github.com/MLE-Dojo/MLE-Dojo>
- **Project:** <https://mle-dojo.github.io/MLE-Dojo-page/>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

MLE-Dojo turns ML-engineering evaluation into an interactive gym: agents iteratively experiment, debug, and refine solutions through structured feedback, over 200+ real Kaggle challenges (68 from MLE-bench, 74 from DSBench, and 75 freshly scraped, per the repository). Beyond evaluation, the environment supports supervised fine-tuning and reinforcement learning of agents, positioning ML engineering as a trainable interactive task. Eight frontier LLMs are evaluated, with the environment measuring iterative improvement, long-horizon solution quality, and error-resolution efficiency.

## Tasks

200+ Kaggle-derived ML-engineering challenges in an interactive environment; agents iterate over data processing, architecture search, hyperparameter tuning, and debugging with structured feedback. Interactive-agentic and long-horizon; supports SFT/RL agent training.

## Domains

AI & Machine Learning Research — machine-learning engineering as an interactive, trainable environment.

## Evaluation

- Environment-measured iterative improvement, long-horizon solution quality, and error-resolution efficiency across eight frontier LLMs.
- **Reported.** Eight frontier LLMs evaluated; the contribution is the environment plus its measured axes rather than a single headline score.

## Typical Duration

Long-horizon interactive episodes with iterative experiment-and-debug loops per challenge.

## Main Contribution

A Gym-style environment that makes ML engineering both evaluable and trainable — closing the loop from benchmark to reinforcement learning of ML-engineering agents.

## Key Design Ideas

- Structured feedback loops turn one-shot submission into an interactive, improvable task.
- Pooling MLE-bench, DSBench, and fresh Kaggle challenges broadens coverage to 200+.
- SFT/RL support makes the same challenges a training environment, not just a test set.

## Strengths

- Interactive, training-capable environment rather than a static submission benchmark.
- Broad Kaggle coverage reusing established suites plus fresh challenges.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); this is an environment/framework as much as a benchmark, and per-model numeric results are in the paper body. No venue is stated in arXiv metadata.

## Related Works

- [MLE-bench](./mle-bench.md) — The Kaggle-competition benchmark whose competitions MLE-Dojo partly reuses.
- [MLGym](./mlgym.md) — Also a Gym environment for AI-research agents, spanning broader research tasks.
- [MLAgentBench](./mlagentbench.md) — Also iterative ML-experimentation evaluation, without the RL-training environment.
