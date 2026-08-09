# SimulCost (2026)

> [English](../../works/simulcost.md) | **简体中文**

## Overview

SimulCost 是面向 LLM agent 在物理仿真参数调优上的 cost-aware benchmark。它显式纳入 tool-use 成本——仿真时间与实验资源——超越"仅计 token 成本"的资源感知评估视角。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.20253>

## Summary

SimulCost 指出：科学 agent 评估长期聚焦 token 成本，而忽略了 tool-use 成本（仿真时间、实验资源）。本 benchmark 提供跨 13 个物理仿真器的参数调优任务，支持单轮与多轮两种设定，并直接与传统方法在预算约束下对比。

## Tasks

2,947 个单轮任务 + 1,931 个多轮任务，覆盖 13 个仿真器。

## Domains

物理仿真参数调优，跨 13 个仿真器。

## Evaluation

- 预算约束下的成功率。
- 区分单轮与多轮设定。
- 报告：frontier LLM 初始成功率为 46–65%，在严格精度要求下下降到 35–55%；在多轮场景下，LLM agent 相较传统方法落后 1.5–2.5×。

## Typical Duration

多轮参数调优工作流；摘要未给出每任务时长。

## Main Contribution

在物理仿真参数调优这一场景下引入 cost-sensitive 评估，显式建模 token 之外的 tool-use 资源成本。

## Key Design Ideas

- 成本模型超越 token，纳入仿真时间与实验资源成本。
- 跨 13 个仿真器的广度。
- 单轮与多轮设定分开报告。
- 与传统（非 LLM）方法直接对比。

## Strengths

- 显式建模 tool-use 成本——token-only 框架无法捕获的关键成本被纳入。
- 与传统方法的直接对比提供了强 baseline。
- 大规模任务集（2,947 + 1,931）。

## Limitations

- Repository note: 限定于物理仿真——成本模型能否迁移至其他科学工作流未被评估。

## Related Works

- [CostBench](./costbench.md) — 同样把成本作为一等目标，但在 travel-planning 场景下的 tool use，而非科学仿真。
