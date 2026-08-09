# AutoResearchBench (2026)

> [English](../../works/autoresearchbench.md) | **简体中文**

## Overview

AutoResearchBench 是一个面向自主科学文献发现（scientific literature discovery）的 benchmark，评估 AI agent 在两类任务上的能力：通过渐进式多步探查追踪一篇特定目标论文（Deep Research），以及全面收集满足给定条件的所有论文（Wide Research）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.25256>
- **Code:** <https://github.com/CherYou/AutoResearchBench>

## Summary

AutoResearchBench 聚焦自主研究中的文献查找环节——为研究问题探索已有知识，以及为验证假设、支撑论断获取证据。与此前的 agentic web-browsing benchmark 相比，论文从三个维度界定其特点：*research-oriented*（需要对科学概念的深入理解）、*literature-focused*（要求对细节信息的细粒度利用）、*open-ended*（符合条件的论文数量未知，因而全程需要审慎的推理与搜索）。论文认为这些特性使该 benchmark 即使对已基本攻克 BrowseComp 等通用 agentic browsing benchmark 的模型也极具挑战。

## Tasks

1,000 条查询，分为两类互补任务：**Deep Research**（600 条——通过渐进式多步探查定位一篇特定目标论文）与 **Wide Research**（400 条——收集满足给定条件的论文集合；平均每条查询 9.23 个有效答案，范围 2 到 34 篇）。任务由 full-text-first 的人机协同流水线构建：Deep Research 包括目标论文选择、全文约束挖掘与基于引用的多跳扩展、约束模糊化与剪枝、以及验证；Wide Research 包括面向领域的来源采集、结构抽象、查询精化、以及带严格审计的迭代扩展，论文入选需 LLM 一致同意。

## Domains

覆盖八个核心计算机科学领域的科学文献发现。

## Evaluation

- **Deep Research：** 精确匹配 accuracy——预测集合必须与 ground-truth 目标完全一致。
- **Wide Research：** 预测论文集合与 ground-truth 集合之间的 Intersection over Union（IoU），整体评估预测集合而不强加排序。
- 报告结果：最强的被评估模型在 Deep Research 上仅达到 9.39% accuracy，在 Wide Research 上仅达到 9.31% IoU，许多强基线低于 5%。

## Typical Duration

在学术检索与通用 web 检索后端上的多轮 agentic 搜索；每条查询的轮数因模型而异，平均可达数十轮。

## Main Contribution

一个专门面向自主科学文献发现的 benchmark，将定向论文查找（Deep Research）与开放式全面收集（Wide Research）分开评估，并公开发布数据集、评估流水线与代码。

## Key Design Ideas

- 两类互补任务拆分文献发现问题：精确定位一篇目标论文 vs. 穷尽式收集符合条件的集合。
- 构造上的开放性：符合条件的论文数量对 agent 未知，因此停止时机本身成为被评估的对象。
- Full-text-first 的任务构建从论文全文与引用图中挖掘约束，而不仅依赖标题与摘要。
- Wide Research 采用集合级 IoU 评分，直接评估全面性而非排序质量。

## Strengths

- 瞄准自主研究中承重的一环（文献发现），这是通用 web-browsing benchmark 覆盖不足的。
- 提升空间大：两类任务的最好报告成绩均低于 10%。
- 数据集、评估流水线与代码公开发布（Apache 2.0）。

## Limitations

- Repository note: 覆盖范围限于计算机科学文献；论文未评估其他科学领域的文献发现。
- Repository note: Wide Research 的 ground-truth 入选在构建阶段依赖 LLM 共识，因此答案集合的完备性继承这些 judge 的可靠性。

## Related Works

- [AstaBench](./astabench.md) — 同样评估文献相关的研究能力，但作为宽泛研究套件中的一个类别，而非专门的文献发现 benchmark。
- [GAIA](./gaia.md) — 通用助手式的浏览与工具使用问题，答案单一且无歧义；AutoResearchBench 以开放式、面向文献的搜索与这类通用 agentic browsing 相区别。
