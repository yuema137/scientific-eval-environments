# EmbodiedEval (2025)

> [English](../../works/embodiedeval.md) | **简体中文**

> **首次公开：** 2025-01-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2501.11858)

## Overview

EmbodiedEval 在一个交互式 3D 模拟框架中把多模态 LLM 当作具身 agent 来评测：125 个多样 3D 场景中的 328 个任务，横跨导航、物体交互、社交互动、属性问答与空间问答五个类别。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2501.11858>
- **Code:** <https://github.com/thunlp/EmbodiedEval>
- **Project:** <https://embodiedeval.github.io>
- **Venue:** arXiv preprint (cs.CV), 2025

## Summary

EmbodiedEval 要的是一个交互框架内的能力广度：不押注单一任务族，而是让 328 个任务在 125 个场景中混合移动、操作式的物体交互、社交情境下的行为，以及两类必须「动起来才能回答」的问答。MLLM 在实时 3D 模拟器中作为交互式 agent 运行，论文报告其与人类水平存在显著差距。

## Tasks

125 个 3D 场景中的 328 个交互式任务，分五类（导航、物体交互、社交互动、属性问答、空间问答）；MLLM 是完整的 agent。仅模拟。

## Domains

多样 3D 场景中的具身模拟——不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 统一的模拟-评估框架按类别计任务完成度；人类基线评测代码随仓库发布。
- **报告。** MLLM 与人类水平差距显著；数值为 TODO(reference)——摘要未载明。

## Typical Duration

实时模拟中的多步交互回合。

## Main Contribution

把类别广度本身作为要点：在同一个交互框架里，导航、交互、社交行为与具身问答对同一个模型直接可比。

## Key Design Ideas

- 具身问答类任务迫使模型「行动以感知」，而非从初始画面作答。
- 125 个场景把场景多样性推到与任务多样性同等重要。
- 统一框架消除了任务类别之间的跨 benchmark 干扰因素。

## Strengths

- 按场景与类别覆盖计，最宽的交互式 MLLM 具身评估之一。
- 公开材料完整，含人类基线工具。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；这些来源无法核实任何发表信息，数值结果有待全文校验。
- 仅模拟；无物理机器人平台。

## Related Works

- [EmbodiedBench](./embodiedbench.md) — 同样是交互式 MLLM 具身评估，按能力而非类别组织。
- [PhysBench](./physbench.md) — 同样探测 MLLM 具身 agent 依赖的感知一侧，以静态物理理解问答呈现。
- [PARTNR](./partnr.md) — 同样是基于模拟器的具身评估，规模在协作层面。
