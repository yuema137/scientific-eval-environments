# PhySciBench (2026)

> [English](../../works/physcibench.md) | **简体中文**

## Overview

PhySciBench 是物理科学领域的 deep-research benchmark：200 道专家整理的问题，物理与化学各半，分六个反映真实科学工作流的任务类别。配套的 DelveAgent 框架属于 agent 构建工作，与本仓库的评估重心相邻。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.18648>
- **Venue:** arXiv preprint (physics.comp-ph), 2026

## Summary

论文指出现有 deep-research 系统在物理科学问题上的三项缺陷——长推理链脆弱、跨步骤知识迁移有限、缺少以物理为根基的自我验证——并提出 PhySciBench 加以度量：200 道专家整理问题，物理与化学均衡，分六个任务类别。论文同时开发了 DelveAgent（自适应规划循环、双粒度记忆、层级式物理反思机制）。

## Tasks

200 道专家整理的问题，物理与化学均衡，组织为六个反映真实科学工作流的任务类别。

## Domains

物理科学：物理与化学。

## Evaluation

- 以准确率为核心，比较最先进的模型与 agent 系统。
- **报告。** Gemini Deep Research 基线准确率 33.5%；DelveAgent 最多提升 7.5 个百分点，推理成本约为最强基线的三分之一。

## Typical Duration

带长推理链的 deep-research 工作流；单题预算为 TODO(reference)。

## Main Contribution

一个专家整理的物理科学 deep-research benchmark，使推理链脆弱性、跨步骤知识迁移与物理自我验证成为可度量对象。

## Key Design Ideas

- 六个任务类别对应真实科学工作流，而非考试题型。
- 物理/化学均衡使 benchmark 不退化为单一领域。
- 对所提 agent 同时报告成本与准确率。

## Strengths

- 瞄准已诊断的失效画像（脆弱链条、迁移差、无物理自检），而非泛化的难度。
- 基线准确率 33.5%，留有大量提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- Repository note: 论文的第二项贡献 DelveAgent 属于 agent 实现，超出本仓库范围；本卡片记录其 benchmark。

## Related Works

- [PRBench](./prbench.md) — 同样是专家整理的物理评估，但通过端到端论文复现而非 deep-research 问题。
- [DeepResearch Bench](./deepresearch-bench.md) — 同样评估 deep-research 系统，但评分对象是通用需求的报告而非物理科学问题。
- [TRACE](./trace.md) — 同样评估 deep-research agent，但对整条轨迹而非最终答案打分。
