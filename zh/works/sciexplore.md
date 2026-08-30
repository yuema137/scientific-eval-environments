# SciExplore (2026)

> [English](../../works/sciexplore.md) | **简体中文**

> **首次公开：** 2026-07-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.20926)

## Overview

SciExplore 是评估自主 agent 科学信息获取能力的 benchmark，覆盖从数据库导航到跨源信息整合，含四类渐进任务、103 个专家整理的任务，横跨十余个科学学科。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.20926>
- **Venue:** arXiv preprint, 2026 (submitted to ACL 2026)

## Summary

SciExplore 通过四类渐进任务评估 LLM 与 agent 的科学信息获取与推理能力——科学数据库导航、表述模糊的文献检索、缺失参考文献补全、跨源结构化知识综合——考察从实体级推理、文档级识别到证据级 grounding 与领域级综合的能力谱。

## Tasks

103 个专家整理的任务，分四类：科学数据库导航、表述模糊的文献检索、缺失参考文献补全、跨源结构化知识综合，横跨十余个科学学科。

## Domains

十余个科学学科；摘要未逐一列出。

## Evaluation

- 在四类渐进任务上评估十余个最先进的 LLM 与自主 agent。
- **报告。** 存在明显的性能差距：随任务复杂度上升性能急剧下降，最难的结构化综合任务准确率极低。

## Typical Duration

跨科学数据库与文献的多步信息获取工作流；单任务预算为 TODO(reference)。

## Main Contribution

一个能力渐进式的科学信息获取 benchmark，把数据库导航、检索、证据 grounding 与跨源综合分开评估，而非混为一体。

## Key Design Ideas

- 四类任务构成从实体级推理到领域级综合的能力阶梯。
- 专家整理横跨十余个学科，而非单一领域测试台。

## Strengths

- 清晰定位科学信息获取随复杂度上升在何处失效。
- 最难层级（结构化综合）准确率极低，留有明确提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [AutoResearchBench](./autoresearchbench.md) — 同样把科学文献发现单独拿出评估，以精确匹配与集合 IoU 为 1,000 条查询打分。
- [AstaBench](./astabench.md) — 同样在更广的科研能力中评估文献理解，带成本受控的打分。
- [ScholarQuest](./scholarquest.md) — 同样评估 agent 式论文检索，在计算机科学主题上按分类法引导。
