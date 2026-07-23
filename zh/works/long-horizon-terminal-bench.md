# Long-Horizon-Terminal-Bench (2026)

## Overview

Long-Horizon-Terminal-Bench 将 Terminal-Bench 扩展到显著更长的执行 horizon。它使用细粒度分级子任务提供密集的中间奖励与部分得分，而不是仅采用二值的端到端 pass/fail。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.08964>

## Summary

该 benchmark 使用分级子任务奖励结构评估 agent 在长 horizon terminal 任务上的表现。任务被分解为可打分的子任务，可在可配置的奖励阈值下衡量部分进展。

## Tasks

46 个长 horizon 任务，涵盖 9 个类别，包括实验复现、软件工程、多模态分析、交互式游戏、科学计算。

## Domains

Terminal 场景下的长 horizon 工作流，覆盖科学计算、软件工程、多模态分析、交互式游戏。

## Evaluation

- 细粒度分级子任务提供密集中间奖励。
- 部分得分在可配置的奖励阈值下聚合。
- 报告：最强测试模型在 0.95 部分奖励阈值下取得 15.2% pass@1，在 1.0 完美奖励阈值下取得 10.9%。

## Typical Duration

长 horizon：数百步 agent 交互与延长的会话。

## Main Contribution

针对长 horizon terminal 任务的密集奖励评分方案，将评估从二值 pass/fail 推向部分得分。

## Key Design Ideas

- 子任务分解 + 分级奖励。
- 部分进展的密集中间信号。
- 基于阈值的聚合（0.95 部分奖励、1.0 完美奖励）。

## Strengths

- 显式衡量部分进展，降低长 horizon 任务上二值 pass/fail 的脆弱性。
- 在共享奖励方案下覆盖 9 个任务类别。

## Limitations

- Repository note: Terminal 执行环境——不评估具身、GUI-only 或物理世界能力。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Terminal-Bench 的姊妹扩展，面向自然科学工作流。
- [Agents' Last Exam](./agents-last-exam.md) — 也是长 horizon，但以职业分类为 grounding。
