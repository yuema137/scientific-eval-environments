# ReplicationBench (2025)

> [English](../../works/replicationbench.md) | **简体中文**

## Overview

ReplicationBench 是追问「AI agent 能否复现天体物理研究论文」的评估框架：每篇论文被拆成若干任务，要求 agent 复现其核心贡献——实验设置、推导、数据分析与代码库——且每个任务都与论文原作者共同开发。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.24591>
- **Code:** <https://github.com/Christine8888/replicationbench-release>
- **Venue:** arXiv preprint (cs.CL, astro-ph.IM), 2025

## Summary

ReplicationBench 把论文复现作为天体物理（一门数据驱动的科学）中 agent 评估的基本单元。agent 在计算沙箱中完成任务，每个任务瞄准一项关键科学结果；由于任务与原作者共同开发，忠实性（是否遵循原方法）与正确性（结果的技术准确性）都能客观打分。数据集含 111 个复现任务，覆盖 20 篇研究论文（据官方仓库）。即便表现最好的语言模型，得分也不足 20%。

## Tasks

111 个天体物理复现任务，覆盖 20 篇研究论文（官方仓库），每个任务瞄准一项关键科学结果，覆盖实验设置、推导、数据分析与代码库；在计算沙箱中运行。

## Domains

天体物理研究工作流，作为数据驱动科学的试验场。

## Evaluation

- 每任务双轴客观评分：对原方法的**忠实性**与结果的**正确性**，由作者共同开发的任务定义所支撑。
- **报告。** 表现最好的语言模型得分也不足 20%。

## Typical Duration

每任务为沙箱中的多步复现工作流；预算为 TODO(reference)。

## Main Contribution

让论文原作者共同定义「怎样才算复现」，以此作为天体物理 agent 评估的真值，并把「忠于方法」与「结果正确」分为两条轴。

## Key Design Ideas

- 任务由原作者共同开发，「什么算复现成功」由做出这项工作的人说了算。
- 忠实性与正确性分开打分，而不是折叠成一个数。
- 轨迹分析定位 agent 工作流在何处失败。

## Strengths

- 原作者的深度参与，让复现真值具有罕见的权威性。
- 20% 以下的上限记录了真实研究工作流上的巨大提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [PRBench](./prbench.md) — 同样是物理领域的端到端论文复现，带专家撰写的加权评分标准。
- [EXP-Bench](./exp-bench.md) — 同样端到端复现已发表实验，面向 AI 研究论文。
- [Stargazer](./stargazer.md) — 同样在真实天体物理分析上评估 agent，用档案系外行星系统。
