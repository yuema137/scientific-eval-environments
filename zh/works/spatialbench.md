# SpatialBench (2025)

> [English](../../works/spatialbench.md) | **简体中文**

## Overview

SpatialBench 追问 agent 能否分析真实世界的空间生物学数据：146 个可验证问题，横跨五种空间技术与七类任务，从步骤前数据快照出发、以确定性判分检验关键生物学结果的复原。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.21907>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

SpatialBench 把「快照 + 确定性判分」设计应用到空间转录组：agent 拿到分析步骤开始前一刻的实验数据，须复原已知的生物学结果。基础模型准确率偏低——各模型家族在 20–38% 之间——模型-任务与模型-平台交互效应显著；论文进一步主张 harness 设计（工具、提示、控制流、执行环境）有很大的实证影响，应作为一等对象加以评估与改进。

## Tasks

146 个可验证的空间生物学分析问题，横跨五种空间技术与七类任务，均从步骤前数据快照出发。

## Domains

覆盖五种技术的空间转录组与空间生物学；scBench 在单细胞侧的姊妹篇。

## Evaluation

- 确定性判分器检验关键生物学结果的复原；指标为准确率。
- **报告。** 各模型家族的基础模型准确率为 20–38%，模型-任务与模型-平台交互效应显著；harness 设计的实证影响很大。

## Typical Duration

真实空间数据集上的单步分析回合。

## Main Contribution

把可验证的 agent 评估扩展到空间生物学，并把 harness 提升为一等评估对象，而非实现细节。

## Key Design Ideas

- 与 scBench 相同的快照设计，让单细胞两大模态可比。
- 在真实（而非合成）数据集上做确定性判分。
- 实测 harness 变化的影响，呼应「能力是模型-harness 组合的属性」。

## Strengths

- 覆盖五种工具成熟度差异显著的空间技术。
- harness 效应的发现给实践者一根模型选择之外的可用杠杆。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [scBench](./scbench.md) — 覆盖另一主流单细胞模态的 scRNA-seq 姊妹篇。
- [scBench-Long](./scbench-long.md) — 该 benchmark 家族的长 horizon 扩展。
- [Harness-Bench](./harness-bench.md) — 同样把 harness 作为研究变量，面向通用 agent 工作流。
