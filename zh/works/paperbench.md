# PaperBench (2025)

> [English](../../works/paperbench.md) | **简体中文**

> **首次公开：** 2025-04-02 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2504.01848)

## Overview

PaperBench 评估 AI agent 能否复现最前沿的 AI 研究：agent 需从零复现 20 篇 ICML 2024 Spotlight 与 Oral 论文——理解贡献、搭建代码库、执行实验——并对照与论文作者共同开发的层级式评分标准判分，可判分节点共 8,316 个。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.01848>
- **Code:** <https://github.com/openai/preparedness>
- **Venue:** arXiv preprint (cs.AI, cs.CL), 2025

## Summary

PaperBench 通过把每篇论文分解为带明确判分标准的层级式子任务，使「复现」可以客观打分——评分标准与论文作者共同开发。LLM judge 按标准大规模评判复现尝试，而 judge 本身也在一个单独的 judge benchmark 上被评估。受评中最好的 agent——配开源脚手架的 Claude 3.5 Sonnet (New)——平均复现分仅 21.0%；受邀的顶尖 ML 博士在所试子集上仍然胜过模型。

## Tasks

从零复现 20 篇 ICML 2024 Spotlight 与 Oral 论文，分解为 8,316 个可单独判分的评分节点，覆盖理解、代码库开发与实验执行。

## Domains

AI 研究（机器学习）：ICML 2024 论文的复现。

## Evaluation

- 与作者共同开发的层级式评分标准；LLM judge 按标准评分，其自身表现在单独的 judge benchmark 上测量。
- **报告。** 最好的受评 agent（配开源脚手架的 Claude 3.5 Sonnet (New)）平均 21.0%；模型尚未超过 ML 博士的人类基线。

## Typical Duration

从零开始的论文复现会话，含代码开发与实验执行；预算为 TODO(reference)。

## Main Contribution

与作者共同开发的层级式评分标准，把「agent 是否复现了论文」变成数千个可客观判分的子判断——连判分用的 judge 也被单独评测。

## Key Design Ideas

- 与原作者共同制定评分标准，确定「什么才算复现」。
- 层级分解在细粒度上给出部分得分，而非单一的复现与否。
- 单独的 judge benchmark 使自动评分器的可靠性成为一个被实际测量的量。

## Strengths

- 8,316 个判分节点为「复现败在哪里」提供了少见的分辨率。
- 同期的专家人类基线为模型分数提供锚点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [ReplicationBench](./replicationbench.md) — 同样是与作者共同开发的论文复现，面向天体物理而非 AI 研究。
- [PRBench](./prbench.md) — 同样按评分标准打分的论文复现，在物理领域。
- [CORE-Bench](./core-bench.md) — 同样面向可复现性，但基于论文提供的代码与数据而非从零开始。
