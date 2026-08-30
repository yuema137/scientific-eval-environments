# ScholarQuest (2026)

> [English](../../works/scholarquest.md) | **简体中文**

> **首次公开：** 2026-06-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.20235)

## Overview

ScholarQuest 是面向开放文献环境中 agent 式学术论文检索的大规模、分类法引导的 benchmark，由 1,000 余个计算机科学主题与四类代表性研究意图构建。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.20235>
- **Venue:** arXiv preprint (cs.IR), 2026

## Summary

ScholarQuest 系统评估执行迭代式文献探索的 LLM 检索 agent。其四类研究意图——方法导向、设定锚定、比较导向、范围受控——建模了研究者实际的检索方式。Agent 式方法优于单次检索基线，但最佳 agent 也仅达到 0.314 Recall@100 与 0.355 Recall@All；论文进一步分析了检索效率、意图级稳健性与失败案例。

## Tasks

查询构建自 1,000 余个计算机科学主题，分四类研究意图：方法导向、设定锚定、比较导向、范围受控。具体查询数为 TODO(reference)。

## Domains

计算机科学文献（信息检索与 AI 为主）。

## Evaluation

- 对照真值论文集合的 **Recall@100 与 Recall@All**。
- 检索效率、意图级稳健性与失败案例分析。
- **报告。** 最佳 agent 仅达 0.314 Recall@100 与 0.355 Recall@All；agent 式方法优于单次基线，但提升空间仍然很大。

## Typical Duration

开放文献环境中的迭代式文献探索回合。

## Main Contribution

把研究意图分类法大规模应用于 agent 式论文检索，表明控制意图结构后，即使最强 agent 的召回率也依然很低。

## Key Design Ideas

- 意图分类法（方法 / 设定 / 比较 / 范围）取代无差别的“找论文”查询。
- 开放文献环境而非冻结语料。
- 两个截断点的召回率把排序质量与覆盖度分开。

## Strengths

- 规模（1,000+ 主题）与受控的意图结构兼得。
- 失败案例分析定位迭代探索在何处失效。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [AutoResearchBench](./autoresearchbench.md) — 同样考核 agent 式文献发现；ScholarQuest 按研究意图而非 deep/wide 任务类型组织查询。
- [SciExplore](./sciexplore.md) — 同样评估科学信息获取，但按能力渐进层级而非检索意图。
- [AstaBench](./astabench.md) — 其文献理解任务同样含论文查找，带成本受控的打分。
