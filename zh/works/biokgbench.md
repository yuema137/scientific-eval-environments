# BioKGBench (2024)

> [English](../../works/biokgbench.md) | **简体中文**

## Overview

BioKGBench 是面向生物医学 AI agent 的知识图谱核查 benchmark：两项原子任务——科学主张验证（SCV）与知识图谱问答（KGQA）——组合成 agentic 的 KGCheck 任务，agent 借助 KGQA 与领域 RAG 找出大规模生物医学知识图谱中的事实错误。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.00466>
- **Code:** <https://github.com/westlake-autolab/BioKGBench>
- **Venue:** arXiv preprint (cs.CL, cs.AI), 2024

## Summary

BioKGBench 把「读懂文献」变成可检验的行为：agent 能否验证科学主张、并把知识图谱问到足够深，以致发现图谱本身哪里错了？它为原子任务提供两千余个实例，为 agent 级的 KGCheck 任务提供 225 个高质量标注实例，覆盖 UniProt、STRING、Reactome、DisGeNET 等生物医学资源（据官方仓库）。最先进的 agent——无论通用还是生物医学专用——在该 benchmark 上或失败或表现不佳；论文的基线 agent（BKGAgent）在现有知识图谱数据库中发现了 90 余处事实错误。

## Tasks

两项原子任务（科学主张验证；KGQA）共 2,000 余个实例，外加 agentic 的 KGCheck 任务 225 个标注实例：交互式查询生物医学知识图谱以定位事实错误。

## Domains

覆盖蛋白质及其相互作用、通路、疾病、基因与组织的生物医学知识图谱（据官方仓库为 UniProt、STRING、Reactome、DisGeNET）。

## Evaluation

- 主张验证与 KGQA 的正确性；agent 级评分基于标注的 KGCheck 实例。详细指标定义为 TODO(reference)。
- **报告。** 最先进的 agent 或失败或表现不佳；在现有知识图谱数据库中发现 90 余处事实错误。

## Typical Duration

KGCheck 为交互式图谱查询回合；原子任务为单实例作答。

## Main Contribution

把知识库质量控制变成 agent benchmark——并以实效证明价值：在生产级生物医学数据库中揪出 90 余处真实错误。

## Key Design Ideas

- 原子任务（验证、查询）与其 agentic 组合（审计）分开评估。
- 评估对象是知识图谱本身，成功即产出科学价值（找到的错误），而不只是分数。
- 领域 RAG 把验证锚定在生物医学来源上，而非参数化记忆。

## Strengths

- 双层设计能定位失败是原子层面的还是组合层面的。
- 被发现的错误为该 benchmark 的真实性提供了少见的外部佐证。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: 论文的基线 agent BKGAgent 属于 agent 实现，超出本仓库范围；本卡片记录其 benchmark。

## Related Works

- [LAB-Bench](./lab-bench.md) — 同样评估生物学数据库导航，以选择题形式。
- [MetaSyn](./metasyn.md) — 同样评估对生物医学文献的证据忠实性，走系统综述路线。
- [MedBrowseComp](./medbrowsecomp.md) — 同样在实时生物医学知识库上做多跳事实综合。
