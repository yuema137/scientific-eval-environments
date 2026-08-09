# MLAgentBench (2023)

> **English** | [简体中文](../zh/works/mlagentbench.md)

## Overview

MLAgentBench evaluates language agents on machine-learning experimentation: a suite of 13 tasks — from improving CIFAR-10 accuracy to recent research problems like BabyLM — where an agent reads and writes files, executes code, inspects outputs, and iterates to beat a starter-code baseline, with the best agent (Claude 3 Opus) at 37.5% average success.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.03302>
- **Code:** <https://github.com/snap-stanford/MLAgentBench>
- **Venue:** ICML 2024

## Summary

MLAgentBench frames ML research as an interactive agent task: given a task and starter code, a ReAct-style agent reads available files, runs experiments on a compute cluster, inspects outputs, and iterates to improve a target metric. Its 13 tasks range from well-established datasets (CIFAR-10) to recent research problems (BabyLM) and Kaggle challenges. Across Claude v1/v2.1/v3-Opus, GPT-4, GPT-4-turbo, Gemini-Pro, and Mixtral, the best agent (Claude 3 Opus) reaches 37.5% average success — with success ranging from 100% on older datasets to 0% on recent Kaggle challenges.

## Tasks

13 ML-experimentation tasks; the agent reads/writes files, executes code, and inspects outputs to improve a metric over a starter-code baseline. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — ML experimentation: iteratively improving model performance across established and recent research tasks.

## Evaluation

- Success rate (runs achieving >10% improvement over the starter-code baseline at the final step) and average improvement.
- **Reported.** Claude 3 Opus best at 37.5% average success; success ranges from 100% (older datasets) to 0% (recent Kaggle challenges).

## Typical Duration

Long-horizon episodes: repeated read-execute-inspect-iterate cycles per task.

## Main Contribution

An early, influential formulation of ML research as an interactive agent benchmark — improve-a-metric tasks graded by measured improvement over starter code.

## Key Design Ideas

- Improvement-over-baseline scoring rewards genuine experimental progress, not just completion.
- Spanning old datasets to recent Kaggle tasks exposes the recency/contamination gradient.
- ReAct-style file/code/output actions mirror how researchers actually iterate.

## Strengths

- A foundational ML-experimentation agent benchmark with a maintained public release.
- The 100%-to-0% recency spread cleanly illustrates memorization vs. genuine capability.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the ICML 2024 venue is not stated in arXiv Comments (confirmed separately via OpenReview).

## Related Works

- [MLE-bench](./mle-bench.md) — Also ML-engineering agent evaluation, on 75 Kaggle competitions with medal scoring.
- [RE-Bench](./re-bench.md) — Also open-ended ML R&D tasks, benchmarked against human experts under time budgets.
- [MLGym](./mlgym.md) — Also open-ended AI-research tasks, in a Gym environment across CV/NLP/RL.
