# Frontier-Eng (2026)

> [English](../../works/frontier-eng.md) | **简体中文**

> **首次公开：** 2026-04-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.12290)

## Overview

Frontier-Eng 是面向"自我进化 agent"的真实工程任务 benchmark，把评估构造成**迭代式生成优化**：agent 提出候选方案，工业级仿真器在硬性可行性约束下返回连续奖励，agent 在固定交互预算内修订。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.12290>

## Summary

Frontier-Eng 主张：二值 pass/fail 评分无法反映 agent 在受约束的真实工程任务上的表现——那里"可行但次优"的解占多数，迭代式细化才是真正被测的能力。该 benchmark 把每个任务组织为一个 propose-execute-evaluate 循环：agent 生成一个候选 artifact，工业级仿真器在硬性可行性约束下返回连续奖励信号，agent 在固定交互预算内修订。

## Tasks

47 个任务，横跨 5 个工程类别。

## Domains

真实工程任务，以工业级仿真器作为验证器。

## Evaluation

- 迭代式的 propose-execute-evaluate 循环作为基本评估单位。
- 工业级仿真器作为验证器。
- 连续奖励信号，而非二值 pass/fail。
- 仿真器强制硬性可行性约束。
- 每任务固定交互预算。
- 测试 8 个 frontier LLM；GPT 5.4 表现最稳健；所有模型都对该 benchmark 感到有挑战。
- 报告的分析发现：**双 power-law 衰减**——改进的**频率**近似按 ~1/iteration 衰减，改进的**幅度**也沿优化轨迹遵循 power law。
- 报告的设计发现：在受约束问题上，**深度比广度更重要**。

## Typical Duration

按固定交互预算的多步迭代细化。

## Main Contribution

把工程 agent 评估从二值 pass/fail 重构为**工业级仿真器反馈下、有界交互预算内的迭代式生成优化**，并对改进轨迹的形状给出双 power-law 衰减这一实证刻画。

## Key Design Ideas

- Propose-execute-evaluate 作为基本评估单位，而非一次性生成。
- 工业级仿真器返回连续奖励——"可行但次优"能得到分级得分。
- 硬性可行性约束与连续奖励并存——搜索空间被限定，但空间内的奖励是密集的。
- 固定交互预算使 benchmark 内在具备 resource-aware 属性。
- 对改进轨迹的实证刻画（双 power-law 衰减）作为 benchmark 头条结果的一部分。

## Strengths

- 工业级仿真下的连续奖励捕获了二值 pass/fail benchmark 丢弃的信号。
- 有界交互预算使得得分在无 token 成本漂移的情况下可复现。
- Power-law 衰减这一实证声明为后续工作提供了一个可复现或可反驳的具体现象。
- "深度 > 广度" 是工程 agent 的一个可检验的设计声明。

## Limitations

- Repository note: 47 任务、5 类别——相较 "真实工程" 的域覆盖声明，任务池规模较小。
- Repository note: 引用来源为 arXiv v2（2026-04-27）；截至撰稿一手来源尚无同行评审出处。

## Related Works

- [SimulCost](./simulcost.md) — 同样以域仿真器作为验证器、把资源使用视为一等；限定在物理仿真参数调优，而非开放式工程优化。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样面向科学 / 工程 + 可执行验证，但用容器内 pytest，而非工业级仿真器在迭代循环中的反馈。
- [CostBench](./costbench.md) — 同样把评估围绕有界资源预算下的迭代决策组织，但资源是 travel-planning 场景下的 tool-call 成本，而非工程优化上的交互预算。
