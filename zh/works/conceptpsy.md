# ConceptPsy (2023)

> [English](../../works/conceptpsy.md) | **简体中文**

> **首次公开：** 2023-11-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2311.09861)

## Overview

ConceptPsy 是为「概念全面性」而建的心理学 benchmark 套件：12 个核心学科、1,383 个人工收集的概念，每道题都标注到章节，使得逐概念的表现——而非只有一个总分——得以显现。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.09861>
- **Venue:** arXiv preprint (cs.CL), 2023

## Summary

ConceptPsy 主张单一的心理学准确率数字会掩盖模型真正失手的地方，因此按概念组织评估：12 个核心学科、1,383 个人工收集的概念，每个概念的题目由 GPT-4 生成、经心理学家审阅，每道题都标注到章节。章节级准确率揭示出跨概念的显著表现差异——即便同一系列的模型也如此——这是总分会掩盖的。

## Tasks

覆盖 12 个核心学科、1,383 个概念的心理学题目，每题标注到章节；静态问答。题目总数为 TODO(reference)——摘要未载明。

## Domains

神经科学与认知科学——概念粒度上、覆盖 12 个核心学科的心理学知识。

## Evaluation

- 总体准确率加章节级（逐概念）准确率，覆盖广泛的 LLM。
- **报告。** 跨概念表现差异显著，即便在同一模型系列内；数值结果为 TODO(reference)。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

概念级的心理学评估——把每道题标注到章节，使逐概念的短板显现，而非被平均掉。

## Key Design Ideas

- 概念级标注把一个分数变成逐概念的画像。
- 人工收集 1,383 个概念，确保覆盖全面。
- 心理学家审阅生成题目，保障题目质量。

## Strengths

- 概念粒度使 benchmark 具诊断性，而不止于比较。
- 覆盖 12 个核心心理学学科，全面。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；论文在审（arXiv 无发表信息），题目总数未载明，arXiv 页面无法确认代码 URL。

## Related Works

- [CPsyExam](./cpsyexam.md) — 同样是中文心理学知识 benchmark，沿知识与案例分析两轴组织。
- [PsychCounsel-Bench](./psychcounsel-bench.md) — 同样是心理学知识评估，考咨询师认证题。
- [BrainBench](./brainbench.md) — 同样是神经科学/心理学领域 benchmark，考前瞻性结果预测。
