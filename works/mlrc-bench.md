# MLRC-Bench (2025)

> **English** | [简体中文](../zh/works/mlrc-bench.md)

## Overview

MLRC-Bench asks whether language agents can solve machine-learning research challenges: a curated suite of 7 competition tasks where agents must propose and implement novel research methods, scored objectively by how much of the gap between a provided baseline and top human participants they close — where the best agent closes only 9.3%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.09702>
- **Code:** <https://huggingface.co/spaces/launch/MLRC_Bench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

MLRC-Bench measures the hard part of ML research — proposing and implementing genuinely novel methods, not just running known pipelines. Its 7 competition tasks are scored by an objective metric (rather than an LLM judge): the fraction of the gap between a provided baseline and top human-participant scores that the agent closes. Even the best-performing agent (gemini-exp-1206 under the MLAB scaffold) closes only 9.3% of that gap, exposing how far agents remain from competitive ML research.

## Tasks

7 ML research-competition tasks; the agent proposes and implements novel research methods under a scaffold, submitting solutions scored against baseline and top-human references.

## Domains

AI & Machine Learning Research — ML research competitions: proposing and implementing novel methods to beat baselines toward human-competitive performance.

## Evaluation

- Objective gap-closed metric: fraction of the baseline-to-top-human gap the agent's solution closes (no LLM-as-judge).
- **Reported.** Best agent (gemini-exp-1206 under MLAB) closes only 9.3% of the baseline-to-human gap.

## Typical Duration

Long-horizon episodes: propose, implement, and iterate on a research method per task.

## Main Contribution

An objectively scored, human-anchored benchmark for novel-method ML research — measuring method innovation against competitive human baselines rather than task completion.

## Key Design Ideas

- Gap-closed scoring anchors difficulty to top human participants, not an arbitrary threshold.
- Objective metrics avoid the unreliability of LLM-as-judge for research quality.
- Requiring novel methods (not just implementation) targets research, not engineering.

## Strengths

- Venue-verified (NeurIPS 2025 D&B) with a public leaderboard.
- The 9.3%-gap result is a stark, citable measure of the research-capability frontier.

## Limitations

- Repository note: card compiled from the arXiv abstract and Comments (August 2026); the suite is small (7 tasks), and results depend on the agent scaffold (e.g., MLAB).

## Related Works

- [MLR-Bench](./mlr-bench.md) — Also open-ended ML research evaluation, across a full idea-to-paper pipeline with an LLM judge.
- [RE-Bench](./re-bench.md) — Also human-anchored ML R&D evaluation, against expert time budgets.
- [MLGym](./mlgym.md) — Also open-ended AI-research tasks, in a Gym environment.
