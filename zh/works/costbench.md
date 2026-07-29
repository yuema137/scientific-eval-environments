# CostBench (2025)

> [English](../../works/costbench.md) | **简体中文**

## Overview

CostBench 评估 LLM tool-use agent 是否能够以**成本最优（cost-optimal）**为目标进行规划，并在环境阻断最便宜路径时做出适应。成本在这里不是事后统计，而是 agent 被要求优化的对象。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.02734>

## Summary

CostBench 把 tool-use 规划构造为一个多轮的成本最小化问题。在一个旅行规划（travel-planning）场景下，同一个目标可通过多种原子工具与组合工具的序列达成，每种工具都带有可配置的成本。环境会注入阻断事件——工具失效、成本变化——迫使 agent 在同一成本目标下做 trajectory 中途的重规划。

## Tasks

多轮 travel-planning 场景。每个任务允许多种不同成本的工具序列。四类阻断事件会在 trajectory 期间扰动环境。

## Domains

Travel planning，作为动态 tool-use 的一个具体实例。

## Evaluation

- 在**静态**（无扰动）设定下，agent 能否找到成本最优解。
- 在**动态**（有阻断事件）设定下，agent 能否恢复成本最优解。
- 报告结果：主流模型在静态到动态条件之间性能下降约 40%。

## Typical Duration

多轮 tool-use trajectory，结构上要求反复的"规划 / 执行 / 重规划"循环。

## Main Contribution

将成本作为 LLM tool-use agent 的一等评估目标——而非附带指标——并通过 trajectory 中途的扰动来对成本感知规划做压力测试。

## Key Design Ideas

- 成本是目标函数，而非汇总统计量。
- 对原子工具与组合工具都提供多样、可配置的成本。
- 动态环境的四类阻断事件迫使 agent 重规划。
- 静态–动态差距直接量化了规划的鲁棒性。

## Strengths

- 将成本最优性与任务完成解耦——两者可以且确实会分离。
- 通过阻断事件提供显式的适应性压力测试。
- 即便在强模型上也能揭示约 40% 的静态–动态差距，信号清晰。

## Limitations

- Repository note: 单一领域实例——travel planning。对其他成本敏感领域的泛化未被直接评估。

## Related Works

更广的相关文献见 [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)。
