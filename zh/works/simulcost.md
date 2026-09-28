# SimulCost (2026)

> [English](../../works/simulcost.md) | **简体中文**

> **首次公开：** 2026-03-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2603.20253)

## Overview

SimulCost 评测 LLM agent 能否以较低的模拟成本调好物理参数。除了模型 token 开销，它还计算调用模拟器所消耗的资源。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.20253>
- **Reviewed version:** <https://arxiv.org/html/2603.20253v4>（2026-08-17）

## Summary

Agent 需要选择满足精度要求的模拟参数，同时控制模拟器成本。SimulCost 把初始猜测和后续试错调整分开，与传统参数扫描比较。v4 将平台无关的解析成本，与生产级等离子体代码的实测耗时分开报告。

## Tasks

v4 在 11 个使用解析成本的模拟器上包含 2,643 个单轮、2,304 个多轮任务。第十二个模拟器 EPOCH 在两种设置下各有 273 题，按实测耗时另行报告。arXiv 修订说明指出，CGYRO 因案例搜索存在 bug 被移除。

## Domains

物理模拟参数调优，覆盖流体动力学、固体力学和等离子体物理。

## Evaluation

- 在预算约束和不同精度要求下比较成功率；区分单轮初始猜测与多轮调整。
- v4 报告单轮成功率为 45–62%，高精度要求下为 34–50%；多轮提高到 66–81%，但 agent 的成本为传统扫描的 1.5–2.7 倍，论文将其表述为更慢。
- 11 个模拟器的解析成本结果与 EPOCH 依赖硬件的实测耗时结果分开解释。

## Typical Duration

多轮参数调优工作流；摘要未给出每任务时长。

## Main Contribution

在物理仿真参数调优这一场景下引入 cost-sensitive 评估，显式建模 token 之外的 tool-use 资源成本。

## Key Design Ideas

- 对模拟器调用计费，不把 token 当成唯一资源。
- 将初始参数猜测与反馈驱动的调整分开测量。
- 在明确的精度要求下与传统扫描比较。
- 分别报告解析成本和实测耗时。

## Strengths

明确的模拟器成本和传统扫描基线，可以检查成功率提高是否同时消耗了更多计算。任务集覆盖数千个参数调优实例。

## Limitations

- Repository note: 本卡依据 v4；早期版本的任务数与成绩不能替代当前版本。
- Repository note: EPOCH 的实测耗时依赖测量平台，与另外 11 个模拟器的解析成本不同。
- Repository note: 该成本模型向物理模拟之外工作流的迁移尚未得到验证。

## Related Works

- [CostBench](./costbench.md) — 同样把成本作为一等目标，但在 travel-planning 场景下的 tool use，而非科学仿真。
