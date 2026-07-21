# CATP-LLM / OpenCATP (2024)

## Overview

CATP-LLM（Cost-Aware Tool Planning with LLMs）是一个让 LLM 在考虑工具执行成本的前提下进行工具规划的框架，并伴随 OpenCATP——被称为首个面向 cost-aware planning 的数据集（11,100 个评估样本）。本仓库为其 cost-aware *评估*贡献（OpenCATP）而收录它；论文的头号贡献——CATP-LLM 规划方法——是与本仓库评估焦点相邻的 agent 规划工作（见 Limitations 中的 repository note）。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.16313>
- **Venue:** ICCV 2025

## Summary

CATP-LLM 主张：以往的 LLM 工具规划工作忽视了工具执行成本（如执行时间），从而产生昂贵的计划，其成本超过其任务性能收益。它提出一套面向 cost-aware 工具规划的连贯设计：一种 tool planning language，让 LLM 生成多分支、非顺序的计划以实现高效的并发工具执行；以及一种 cost-aware 离线强化学习算法，微调 LLM 以优化性能–成本权衡。为在缺乏公开成本相关数据集的情况下支持评估，它引入 OpenCATP——首个面向 cost-aware planning 的数据集，包含来自多样任务的 11,100 个评估样本。

## Tasks

OpenCATP 包含来自多样任务的 11,100 个评估样本，其中被调度的工具包括视觉模型等外部模型。任务分类与各类别计数：TODO(reference)——摘要未说明。

## Domains

使用外部工具（如视觉模型）的 LLM 工具规划。OpenCATP 覆盖的具体任务领域：TODO(reference)。

## Evaluation

- 衡量工具计划的性能–成本权衡，将工具执行成本（如执行时间）作为一等量对待，而非忽略。
- 具体指标定义与验证方式：TODO(reference)——摘要未详述。

## Typical Duration

TODO(reference)：摘要未说明单任务时长或 token 预算。

## Main Contribution

论文陈述的贡献是 CATP-LLM——被称为首个赋能 LLM 进行 cost-aware 工具规划的连贯框架——以及 OpenCATP——被称为首个面向 cost-aware planning 的数据集。在本仓库中，其在范围内的贡献是作为 resource-aware 评估数据集的 OpenCATP。

## Key Design Ideas

- 工具执行成本（如执行时间）是规划考量，而非事后统计。
- Tool planning language 支持多分支、非顺序的计划，实现并发工具执行与成本降低。
- Cost-aware 离线 RL 算法微调 LLM 以优化性能–成本权衡。
- OpenCATP 提供专门的数据集（11,100 样本），在此前公开领域缺失的情况下评估 cost-aware planning。

## Strengths

- 引入面向 cost-aware planning 的公开数据集（OpenCATP），弥补以往工具使用数据集忽略的维度。
- 将性能与成本联合考量，而非仅优化任务成功率。
- 非顺序规划的表述使评估与并发、降本的工具执行相一致。

## Limitations

- Repository note: 论文的主要贡献是一个工具规划*方法*（tool planning language 加 cost-aware 离线 RL 微调算法）——属于 agent 规划 / 训练工作，位于本仓库以评估为核心的范围之外。此处为其 cost-aware 评估数据集 OpenCATP 而收录；方法本身不是收录理由。
- Repository note: OpenCATP 的任务分类、指标定义与验证方式在摘要中未说明，上文以 `TODO(reference)` 标注，待从论文或已发布数据集核实。

## Related Works

- [CostBench](./costbench.md) — 同样将 tool-use 成本作为一等量，但作为聚焦动态重规划的 benchmark，而非与规划方法配对的数据集。
- [SimulCost](./simulcost.md) — 同样 cost-aware，将 tool-use 成本扩展到物理仿真时间与实验资源。
