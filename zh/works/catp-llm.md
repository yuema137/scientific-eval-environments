# CATP-LLM / OpenCATP (2024)

> [English](../../works/catp-llm.md) | **简体中文**

> **首次公开：** 2024-11-25 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2411.16313)

## Overview

CATP-LLM（Cost-Aware Tool Planning with LLMs）是一个让 LLM 在考虑工具执行成本的前提下进行工具规划的框架，并伴随 OpenCATP——被称为首个面向 cost-aware planning 的数据集（11,100 个评估样本）。本仓库为其 cost-aware *评估*贡献（OpenCATP）而收录它；论文的头号贡献——CATP-LLM 规划方法——是与本仓库评估焦点相邻的 agent 规划工作（见 Limitations 中的 repository note）。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 评估的是 agent 的元属性（成本、安全性或鲁棒性），而非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2411.16313>
- **Venue:** ICCV 2025

## Summary

CATP-LLM 主张：以往的 LLM 工具规划工作忽视了工具执行成本（如执行时间），从而产生昂贵的计划，其成本超过其任务性能收益。它提出一套面向 cost-aware 工具规划的连贯设计：一种 tool planning language，让 LLM 生成多分支、非顺序的计划以实现高效的并发工具执行；以及一种 cost-aware 离线强化学习算法，微调 LLM 以优化性能–成本权衡。为在缺乏公开成本相关数据集的情况下支持评估，它引入 OpenCATP——首个面向 cost-aware planning 的数据集，包含来自多样任务的 11,100 个评估样本。

## Tasks

OpenCATP 由 111 个组合式任务构成——87 个 sequential（复用自 OpenAGI；69 训练 / 18 测试）与 24 个 non-sequential（12 训练 / 12 测试）——每个任务配 100 个输入样本，合计 11,100 个评估样本（实验中每任务随机采 40 个输入）。被调度的工具是外部专家模型（视觉与 NLP）。

## Domains

基于 OpenAGI 工具箱的组合式视觉 + NLP 工具使用——如目标检测、图像超分、上色、去模糊、去噪、分类与机器翻译，输出为图像和 / 或文本。

## Evaluation

- **Quality of Plan (QoP)** — 头号指标：QoP = α · P_task(p) − (1 − α) · C_price(p)，对两项做 min–max 归一化以统一量纲，默认 α = 0.5（性能与成本等权）。
- **Plan performance P_task** — 图像输出用 ViT Score（计划生成图与 gold 图的余弦相似度），文本输出用 BERT Score（文本余弦相似度）；多输出任务对各输出得分取平均。
- **Plan cost C_price** — 一个归一化的货币价格（USD），来自受 AWS Lambda 启发的定价模型，对工具执行时间与常驻 / 瞬时 CPU–GPU 内存计价；计划价格为各工具价格之和，并行分支取各分支执行时间的最大值。执行时间是价格的输入，而非指标本身。
- **报告：** 以 Llama2-7B 为 backbone，CATP-LLM 即超过 GPT-4，plan quality 整体提升 1.5–93.9%；sequential 规划上较 GPT-3.5 / GPT-4 提升 16.5–34.6% QoP，non-sequential 规划上性能提升 28.4–30.2%、执行价格降低 24.7–45.8%、执行时间降低 67.0–78.3%、QoP 提升 129.4–683.0%。

## Typical Duration

未说明：OpenCATP 定义了成本指标（基于执行时间的价格），但未设定单任务的时间、token 或成本预算上限。

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
- Repository note: OpenCATP 的任务是基于 OpenAGI 工具箱的组合式视觉 / NLP 流水线；其成本模型与 QoP 指标向其他工具生态的迁移尚未被评估。

## Related Works

- [CostBench](./costbench.md) — 同样将 tool-use 成本作为一等量，但作为聚焦动态重规划的 benchmark，而非与规划方法配对的数据集。
- [SimulCost](./simulcost.md) — 同样 cost-aware，将 tool-use 成本扩展到物理仿真时间与实验资源。
