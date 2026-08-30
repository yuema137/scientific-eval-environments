# BAISBench (2025)

> [English](../../works/baisbench.md) | **简体中文**

> **首次公开：** 2025-05-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.08341)

## Overview

BAISBench 以两项任务评测「AI scientist」在组学数据驱动的生物学发现上的能力：在 15 个专家标注的单细胞数据集上做细胞类型注释，并回答 193 道由 41 项已发表单细胞研究的生物学结论派生的选择题——另配六位研究生水平生物信息学家的人类基线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.08341>
- **Code:** <https://github.com/EperLuo/BAISBench>
- **Dataset:** <https://huggingface.co/datasets/EperLuo/BaisBench>
- **Venue:** arXiv preprint (cs.AI, cs.MA, q-bio.GN), 2025

## Summary

BAISBench 用真实研究的结论来要求 AI scientist：系统须分析 41 项已发表研究背后的真实单细胞转录组数据，既要注释细胞类型（据官方仓库以层级化细胞类型树评分），又要回答以研究实际结论为答案的发现类问题。六位研究生水平的生物信息学家提供人类参照。受评的 AI scientist 距完全自主的生物学发现仍有差距。

## Tasks

真实单细胞数据上的两项任务：15 个专家标注数据集上的细胞类型注释，以及派生自 41 项已发表研究的 193 道发现类选择题。

## Domains

单细胞转录组与组学驱动的生物学发现。

## Evaluation

- 注释以层级化细胞类型树对照专家标签评分（官方仓库）；发现任务以对照已发表结论的选择题正确率评分。
- **报告。** 当前 AI scientist 距完全自主的生物学发现仍有差距；人类基线来自六位研究生水平的生物信息学家。

## Typical Duration

数据集级分析回合；非交互式环境。

## Main Contribution

用单细胞生物学中一项发现必须做对的两件事——细胞身份正确、研究结论复原——来检验「AI scientist」的说法，并配有实测的人类参照。

## Key Design Ideas

- 发现类问题锚定已发表结论，目标是真实的科学而非貌似合理的分析。
- 层级化细胞类型树在恰当的粒度上为注释评分，而非精确字符串匹配。
- 同任务的人类基线让「仍有差距」成为可测的陈述。

## Strengths

- 在完全相同的任务上直接与人类专家比较。
- 数据驱动：系统必须从数据集出发，而不是从论文出发。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [scBench-Long](./scbench-long.md) — 同样从数据复原已发表的单细胞结论，采用确定性的长 horizon 判分。
- [HeurekaBench](./heurekabench.md) — 同样从已发表单细胞研究派生发现类问题，以开放式方式评判。
- [SciAgentArena](./sciagentarena.md) — 同样是带专家设计验证的生物医学发现任务评估。
