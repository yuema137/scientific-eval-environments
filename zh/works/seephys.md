# SeePhys (2025)

> [English](../../works/seephys.md) | **简体中文**

## Overview

SeePhys 是基于视觉的物理推理大规模多模态 benchmark，覆盖从初中到博士资格考试的问题，横跨 7 个基础物理领域与 21 类高度异质的图示，其中 75% 的问题不看图就无法作答。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.19099>
- **Code:** <https://github.com/SeePhys/seephys-project>
- **Dataset:** <https://huggingface.co/datasets/SeePhys/SeePhys>
- **Project:** <https://seephys.github.io/>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks

## Summary

SeePhys 追问「看见是否有助于思考」：题目在构造上就要求从图示中提取信息才能解——电路图、Feynman 图等 21 类图示——视觉不可或缺的比例达 75%。据官方项目页，共 2,000 道经严格校验的问题，分 8 个知识层级，43 个模型受评（23 个 MLLM 与 20 个 LLM）。即便最先进的视觉推理模型（如 Gemini 2.5 Pro、o4-mini），准确率也不足 60%。

## Tasks

从初中到博士资格考试水平的多模态物理问题，横跨 7 个领域、21 类图示；据官方项目页共 2,000 道经校验的问题；静态解题。

## Domains

覆盖 7 个基础领域的物理（摘要未逐一列出），图示类型包括电路图与 Feynman 图。

## Evaluation

- 视觉不可或缺的多模态解题准确率。
- **报告。** 最先进的视觉推理模型（如 Gemini 2.5 Pro、o4-mini）准确率不足 60%；官方页报告最佳 MLLM GPT-5 (high) 为 63.2%，人类专家为 86.5%。

## Typical Duration

单题多模态解题；非交互式 agent 设定。

## Main Contribution

让图示成为物理评估中绕不开的一环：75% 的题目视觉不可或缺，分数测量的是基于视觉信息的物理推理，而非纯文本捷径。

## Key Design Ideas

- 视觉不可或缺性在构造时强制成立，「盲」模型无法只靠语言得分。
- 21 类异质图示覆盖物理学实际使用的视觉词汇。
- 从初中到博士的跨度让一个 benchmark 自带难度阶梯。

## Strengths

- 严格的多模态性，且视觉不可或缺的比例被量化。
- 模型覆盖面广（官方页为 43 个），并有人类专家锚点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。7 个领域在这些来源中未逐一列出。

## Related Works

- [PHYBench](./phybench.md) — 同样是原创题物理评估，纯文本并配表达式距离指标。
- [UGPhysics](./ugphysics.md) — 同样是大范围物理解题，双语纯文本。
- [HiPhO](./hipho.md) — 同样混合文本与图示模态，在最新奥赛真题上用官方评分。
