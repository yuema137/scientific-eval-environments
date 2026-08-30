# EmbodiedBench (2025)

> [English](../../works/embodiedbench.md) | **简体中文**

> **首次公开：** 2025-02-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2502.09560)

## Overview

EmbodiedBench 大规模评测作为视觉驱动具身 agent 的多模态 LLM：1,128 个测试任务横跨四个环境，从高层家居语义任务到导航、操作等原子动作任务，组织为六个能力子集——最强模型 GPT-4o 平均也只得 28.9%。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2502.09560>
- **Project:** <https://embodiedbench.github.io>
- **Venue:** ICML 2025

## Summary

EmbodiedBench 纵贯具身能力的全部层级：EB-ALFRED 与 EB-Habitat 承担高层语义任务，EB-Navigation 与 EB-Manipulation 承担底层原子动作，另有六个精心策划的能力子集，考察常识推理、复杂指令理解、空间感知、视觉感知与长程规划。对 24 个主流闭源与开源 MLLM 的评测显示出一致的分裂：模型能应付高层任务，却在底层操作上举步维艰，GPT-4o 的平均分也被压在 28.9%。

## Tasks

四个环境中的 1,128 个交互式测试任务；MLLM 作为从指令到动作的完整视觉驱动 agent。仅模拟。

## Domains

具身家居模拟——不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 跨环境的任务成功率，加六个能力子集的拆分。
- **报告。** 24 个 MLLM 中最强的 GPT-4o 平均 28.9%；高层能力尚可、底层操作薄弱。

## Typical Duration

从高层家居任务到原子导航/操作步骤的交互式回合。

## Main Contribution

一次纵向贯通的测量，表明 MLLM 的具身能力头重脚轻——语义规划跑在了感知-动作落地的前面。

## Key Design Ideas

- 高层与原子动作环境同置一个 benchmark，可以定位系统在哪一层断裂。
- 能力子集是事先策划而非事后归类，六个维度可分别测量。
- 24 个模型的覆盖面让「高低分裂」成为群体结论而非个别模型的怪癖。

## Strengths

- 发布时规模最大的、发表信息经核实的 MLLM 具身评估，公开材料持续维护。
- 28.9% 的上限成为领域内被广泛引用的能力标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目页编写（2026 年 8 月）；环境实现细节有待全文校验。
- 仅模拟；无物理机器人平台。

## Related Works

- [LoTa-Bench](./lota-bench.md) — 同样是执行判分的具身规划评估，面向文本侧的 LLM 规划器。
- [EmbodiedEval](./embodiedeval.md) — 同样是交互式 MLLM 具身评估，铺开在 125 个多样 3D 场景上。
- [PARTNR](./partnr.md) — 同样是大规模具身评估，聚焦人机协作。
