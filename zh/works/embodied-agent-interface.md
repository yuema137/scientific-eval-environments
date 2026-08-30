# Embodied Agent Interface (2024)

> [English](../../works/embodied-agent-interface.md) | **简体中文**

> **首次公开：** 2024-10-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.07166)

## Overview

Embodied Agent Interface（EAI）把 LLM 的具身决策评测分解为四个模块——目标解释、子目标分解、动作排序、状态转移建模——在 VirtualHome 与 BEHAVIOR 中对照模拟器状态逐一评分，并配有细粒度的错误分类法。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2410.07166>
- **Code:** <https://github.com/embodied-agent-eval/embodied-agent-eval>
- **Project:** <https://embodied-agent-interface.github.io/>
- **Dataset:** <https://huggingface.co/datasets/Inevitablevalor/EmbodiedAgentInterface>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks Track (oral), 2024

## Summary

EAI 不满足于只看具身 agent 的最终任务成败，而是把 LLM 可能承担的每个决策模块的接口标准化，分别评估：解释目标、分解子目标、排序动作、建模状态转移。错误被拆成类型——幻觉错误、affordance 错误与多种规划错误——使失败能定位到具体模块与具体原因。据官方项目页，评测覆盖 VirtualHome（26 个任务类别、338 条指令）与 BEHAVIOR（100 个任务类别），在 338 条轨迹上评估了 18 个 LLM。

## Tasks

在 VirtualHome 与 BEHAVIOR 任务上做模块级评估：LLM 的每个模块输出对照模拟器状态检查，而非跑完整的自由 agent 循环；338 条轨迹、约 4,420 步（官方项目页）。

## Domains

具身家居模拟——不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 按模块的细粒度指标，配类型化错误分类：幻觉错误、affordance 错误与多种规划错误，全部对照模拟器状态检查。
- **报告。** 摘要未给出头条数字；据项目页评估了 18 个 LLM。

## Typical Duration

对已记录任务轨迹的逐模块查询；非自由运行的回合。

## Main Contribution

给端到端具身评分提供了按能力分解的替代方案：一个标准化接口，把「agent 失败了」变成「哪个模块、哪类错误」。

## Key Design Ideas

- 四模块分解对应多数 LLM 具身系统的实际架构，分数可直接迁移到系统设计。
- 类型化错误（幻觉 vs affordance vs 规划）把知识性失败与接地性失败分开。
- 模拟器状态检查让模块判分保持客观，无需 LLM judge。

## Strengths

- 经核实的 oral 发表与完整公开材料；模块化具身 LLM 评估的事实参考。
- 错误分类法可迁移到任何具身管线，不限于所用的两个模拟器。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；规模数字出自项目页而非摘要。
- 按模块分解而非闭环：模块之间的相互作用不在测量范围内。

## Related Works

- [LoTa-Bench](./lota-bench.md) — 同样评估 LLM 具身规划，以执行后的目标达成度端到端判分。
- [TRAJDEBUG](./trajdebug.md) — 同样对 agent 轨迹做类型化错误分析，面向工具使用与编码 agent。
- [EmbodiedBench](./embodiedbench.md) — 同样按能力分解的具身评估，面向视觉驱动的 MLLM agent。
