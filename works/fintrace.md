# FinTrace (2026)

> **English** | [简体中文](../zh/works/fintrace.md)

> **First appeared:** 2026-04-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2604.10015)

## Overview

FinTrace is a holistic trajectory-level evaluation benchmark for LLM tool calling on long-horizon financial decision-making tasks. It scores nine metrics across four dimensions rather than only final-answer correctness.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2604.10015>

## Summary

FinTrace assesses how LLMs use external tools for financial decision-making. Instead of scoring only the final answer, it evaluates entire trajectories against nine metrics grouped into four dimensions: action correctness, execution efficiency, process quality, and output quality. The benchmark also releases a training corpus of annotated trajectories.

## Tasks

800 trajectories across 34 task categories.

## Domains

Financial decision-making with external tool use.

## Evaluation

Nine metrics across four dimensions:

- Action correctness
- Execution efficiency
- Process quality
- Output quality

Reported: across 13 tested models, all struggle with information utilization and final answer quality, exposing a gap between invoking the right tools and reasoning effectively over their outputs. The authors also release a training dataset of 8,196 annotated trajectories; fine-tuning yields measurable improvements but leaves end-to-end answer quality challenging.

## Typical Duration

Long-horizon financial workflows. Per-task duration not stated in the abstract.

## Main Contribution

A trajectory-level, four-dimensional evaluation framework for financial tool-use agents, paired with a large annotated training corpus.

## Key Design Ideas

- Trajectory-level evaluation across 9 metrics organized into 4 dimensions.
- Domain-specific grounding in financial decision-making.
- Companion training corpus of annotated trajectories.

## Strengths

- Multi-dimensional trajectory scoring surfaces which capability drives failure.
- Companion training set enables both evaluation and improvement work under a shared framework.
- Broad task-category coverage (34 categories) within finance.

## Limitations

- Repository note: Domain-scoped to finance — transfer of the multi-dimensional metric framework to other domains is not evaluated.

## Related Works

- [TRACE](./trace.md) — Also multi-dimensional trajectory evaluation, for deep-research agents rather than finance.
- [AgentBoard](./agentboard.md) — Trajectory evaluation via subgoal progress rate rather than multi-dimensional metrics.
