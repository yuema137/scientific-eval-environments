# MLGym (2025)

> **English** | [简体中文](../zh/works/mlgym.md)

## Overview

MLGym is the first Gym environment for AI-research tasks — enabling reinforcement-learning research on training agents — paired with MLGym-Bench, a benchmark of 13 diverse open-ended AI-research tasks across computer vision, NLP, reinforcement learning, and game theory.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.14499>
- **Code:** <https://github.com/facebookresearch/MLGym>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

From Meta GenAI and UCSB, MLGym provides the first Gym environment for machine-learning research tasks, making it possible to train agents with reinforcement learning on research work. Its benchmark, MLGym-Bench, holds 13 open-ended AI-research tasks spanning computer vision, NLP, reinforcement learning, and game theory, exercising the full research loop: generating ideas and hypotheses, creating and processing data, implementing ML methods, training models, running experiments, analyzing results, and iterating. Evaluating Claude-3.5-Sonnet, Llama-3.1-405B, GPT-4o, o1-preview, and Gemini-1.5-Pro, the paper finds frontier models can improve on given baselines — usually by finding better hyperparameters — but do not generate novel hypotheses, algorithms, architectures, or substantial improvements.

## Tasks

13 open-ended AI-research tasks (MLGym-Bench) across CV, NLP, RL, and game theory; agents run the full research loop inside the MLGym environment. Interactive-agentic and long-horizon; supports RL training of agents.

## Domains

AI & Machine Learning Research — open-ended AI research across CV, NLP, RL, and game theory, in a trainable Gym environment.

## Evaluation

- Task performance across the 13 MLGym-Bench tasks over five frontier models, within the Gym environment.
- **Reported.** Frontier models improve on baselines (mostly via hyperparameters) but do not produce novel hypotheses, algorithms, architectures, or substantial gains.

## Typical Duration

Long-horizon research-loop episodes per task; the environment also supports RL training.

## Main Contribution

The first Gym environment for AI-research tasks — turning ML research into a trainable RL setting — paired with a 13-task benchmark that shows frontier agents tune but do not innovate.

## Key Design Ideas

- A Gym interface makes AI research an RL-trainable environment, not just a test set.
- The 13 tasks span four subfields, keeping the benchmark from over-fitting one area.
- The full research loop is exercised, exposing the tune-not-innovate ceiling.

## Strengths

- Enables RL research on training AI-research agents, from Meta, with a public release.
- The "improve baselines but don't innovate" finding cleanly bounds current capability.

## Limitations

- Repository note: the paper contributes both the MLGym framework/environment and the MLGym-Bench benchmark; this card centers the benchmark. No venue is stated in arXiv metadata.

## Related Works

- [MLE-Dojo](./mle-dojo.md) — Also a Gym environment for ML-engineering agents, focused on Kaggle challenges.
- [RE-Bench](./re-bench.md) — Also open-ended AI R&D tasks, benchmarked against human experts.
- [MLR-Bench](./mlr-bench.md) — Also full-pipeline ML-research automation, judged by an automated reviewer.
