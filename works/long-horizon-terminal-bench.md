# Long-Horizon-Terminal-Bench (2026)

> **English** | [简体中文](../zh/works/long-horizon-terminal-bench.md)

## Overview

Long-Horizon-Terminal-Bench extends Terminal-Bench to substantially longer execution horizons. It uses fine-grained graded subtasks to enable dense intermediate rewards and partial credit rather than binary end-task pass/fail.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.08964>

## Summary

The benchmark evaluates agents on long-horizon terminal tasks with a graded-subtask reward structure. Instead of relying on binary end-task success, tasks are decomposed into scored subtasks so that partial progress can be measured under configurable reward thresholds.

## Tasks

46 long-horizon tasks spanning nine categories, including experiment reproduction, software engineering, multimodal analysis, interactive games, and scientific computing.

## Domains

Terminal-based long-horizon workflows across scientific computing, software engineering, multimodal analysis, and interactive games.

## Evaluation

- Fine-grained graded subtasks provide dense intermediate rewards.
- Partial credit under configurable reward thresholds.
- Reported: the strongest tested model achieves 15.2% pass@1 at a partial-reward threshold of 0.95, and 10.9% at the perfect-reward threshold of 1.0.

## Typical Duration

Long-horizon: hundreds of agent steps and extended interactions.

## Main Contribution

A dense reward-based grading scheme for long-horizon terminal tasks that moves evaluation from binary pass/fail toward partial credit.

## Key Design Ideas

- Subtask decomposition with graded rewards.
- Dense intermediate signal for partial progress.
- Threshold-based aggregation (0.95 partial-reward, 1.0 perfect-reward).

## Strengths

- Explicitly measures partial progress, reducing pass/fail brittleness on long-horizon tasks.
- Cross-category breadth (nine task categories) under a shared reward scheme.

## Limitations

- Repository note: Terminal-based execution — does not evaluate embodied, GUI-only, or physical-world capabilities.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Sibling extension of Terminal-Bench, but scoped to natural-science workflows.
- [Agents' Last Exam](./agents-last-exam.md) — Also long-horizon, but grounded in the occupational taxonomy rather than the terminal environment.
