# ChemX (2025)

> [English](../../works/chemx.md) | **简体中文**

## Overview

ChemX 评测 agent 系统在化学科学信息自动抽取上的表现：10 个人工整理、领域专家校验的数据集，覆盖纳米材料与小分子，用来对比 ChatGPT Agent 等文档抽取 agent 与化学专用抽取管线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.00795>
- **Dataset:** <https://huggingface.co/ai-chem>
- **Venue:** AI4Mat Workshop, NeurIPS 2025

## Summary

ChemX 瞄准化学数据整编的抽取瓶颈：把论文——连同其领域术语、复杂表格、示意图与依赖上下文的歧义——转成结构化记录。十个专家校验的数据集（含细胞毒性、纳米酶、共晶、恶唑烷酮等专题集）提供真值。论文评测了包括 ChatGPT Agent 与化学专用数据抽取 agent 在内的多种 agent 式抽取器，另设一个可精细控制文档预处理的单 agent 方案与 GPT-5 级静态基线对照，结论是所有系统都面临持续存在的挑战。

## Tasks

从科学文献中做结构化化学数据抽取，对照 10 个覆盖纳米材料与小分子的精编数据集；agent 式文档处理，非实验室交互。

## Domains

化学与材料科学——纳米材料（纳米酶、纳米磁性材料）与小分子数据集，发表于 NeurIPS 的材料发现 workshop。

## Evaluation

- 以领域专家校验的记录为准绳评测抽取质量。
- **报告。** 所有参评系统都面临持续挑战：领域术语、复杂的表格与示意图表示、依赖上下文的歧义。定量数字为 TODO(reference)——摘要未载明。

## Typical Duration

以整篇科学论文为单位的抽取回合。

## Main Contribution

为化学领域的信息抽取提供专家校验的 agent 级真值——测量的正是「文献规模的化学数据库能否由机器建成」的那个决定性环节。

## Key Design Ideas

- 十个独立数据集把评估铺到真正异质的化学记录类型上。
- 每个数据集都经专家校验，抽取错误因此可归因于系统而非标签。
- agent 管线与受控的单 agent 预处理对照，分离出「agent 化」在哪里起作用。

## Strengths

- 覆盖了实践中关键却少有 benchmark 的「文献到数据库」环节。
- 数据集公开在机构 HuggingFace 主页上。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方数据主页编写（2026 年 8 月）；此外的细节有待全文校验。据 arXiv Comments，发表场所是 NeurIPS 2025 的 AI4Mat workshop，而非 Datasets and Benchmarks 主赛道。

## Related Works

- [MetaSyn](./metasyn.md) — 同样以文献为根基，评估从已发表论文中抽取结构化证据。
- [MaCBench](./macbench.md) — 同样是化学/材料数据抽取，在视觉-语言感知层面检验。
- [SciExplore](./sciexplore.md) — 同样是结构化的科学信息获取，覆盖更广的学科。
