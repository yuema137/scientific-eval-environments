# LoTa-Bench (2024)

> [English](../../works/lota-bench.md) | **简体中文**

> **首次公开：** 2024-02-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2402.08178)

## Overview

LoTa-Bench 为具身 agent 的语言任务规划器提供全自动评测：LLM 生成的计划在模拟器中执行，按目标达成度判分，覆盖两组数据集-模拟器组合——AI2-THOR 上的 ALFRED 与 VirtualHome 上扩展的 Watch-And-Help。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2402.08178>
- **Code:** <https://github.com/lbaa2022/LLMTaskPlanning>
- **Venue:** ICLR 2024

## Summary

在 LoTa-Bench 之前，比较 LLM 任务规划器要靠人工审读计划。LoTa-Bench 补上了这一闭环：LLM 针对家政服务指令给出技能序列，模拟器执行，成功与否对照目标条件自动判定——从而可以在两套彼此独立的数据集-模拟器栈上，系统地扫过模型选择与提示词设计。

## Tasks

两组组合上的家政任务规划回合：AI2-THOR 中的 ALFRED 指令与 VirtualHome 中扩展的 Watch-And-Help 指令；LLM 在技能库上做规划，计划在模拟中执行。任务数量为 TODO(reference)——摘要未载明。

## Domains

具身家居模拟——不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 自动化的执行式判分：计划在模拟器中运行，按目标达成度评分，取代人工审读。
- **报告。** 摘要未给出头条数字；论文扫过多个 LLM 与提示词配置。

## Typical Duration

每条指令一个规划回合，在模拟中执行到底。

## Main Contribution

让 LLM 任务规划器的比较变得自动、可复现——用执行验证的 benchmark 取代此前的定性审读。

## Key Design Ideas

- 两套独立的模拟器栈防止结论被单一模拟器的特性绑架。
- 技能库上的规划把「语言到计划」一步与底层控制隔离。
- 自动目标检查让提示词/模型消融便宜到可以大规模去做。

## Strengths

- 执行式 LLM 规划器评估的早期标准，发表信息经核实。
- 双栈设计成为后续具身 benchmark 的模板。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；任务与模型数量有待全文校验。
- 仅模拟；无物理机器人平台。

## Related Works

- [Embodied Agent Interface](./embodied-agent-interface.md) — 同样评估 LLM 的具身决策，按模块分解并配错误分类法。
- [EmbodiedBench](./embodiedbench.md) — 同样是多环境具身评估，扩展到视觉驱动的 MLLM agent。
- [Robotouille](./robotouille.md) — 同样评估 LLM 规划，重点考异步重叠任务。
