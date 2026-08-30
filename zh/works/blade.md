# BLADE (2024)

> [English](../../works/blade.md) | **简体中文**

> **首次公开：** 2024-08-19 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2408.09667)

## Overview

BLADE 为数据驱动科学评测语言模型 agent：12 个数据集配来自科学文献的研究问题，真值取自专家数据科学家的独立分析，考察 agent 能否在开放式分析中整合领域知识、统计学与数据理解。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2408.09667>
- **Code:** <https://github.com/behavioral-data/BLADE>
- **Project:** <https://blade-bench.github.io/>
- **Venue:** EMNLP 2024（Findings）

## Summary

BLADE 评测数据驱动科学所需的判断力：给定 12 个数据集与来自科学文献的研究问题，与数据交互的 agent 须选择概念构念、变换与统计模型来回答开放式问题。真值来自专家数据科学家的独立分析，BLADE 的自动评估为 agent 所做的多方面分析决策评分。结论颇有分寸：与底层数据交互的 agent 相比基座语言模型，在分析选择的多样性上有所改善但仍不理想。

## Tasks

12 个数据集配来自科学文献的研究问题；agent 做开放式数据分析（选择构念、变换、统计模型），对照专家真值分析评估。

## Domains

AI 与机器学习研究——数据驱动的科学分析：统计与概念上有根基的开放式分析。

## Evaluation

- 对分析决策的自动多方面评估，对照独立专家分析（含多样性度量）。
- **报告。** 与数据交互的 agent 相比基座 LM 多样性有所改善但不理想；摘要无单一头条准确率。

## Typical Duration

每个数据集/研究问题一段开放式分析回合。

## Main Contribution

为数据科学 agent 的分析判断评分——它们选择哪些构念、变换与模型——对照专家分析，而非单一数值答案。

## Key Design Ideas

- 专家独立分析作为真值，涵盖各种站得住的选择空间。
- 多方面评估为决策质量与多样性评分，而非只看最终数字。
- 「与数据交互的 agent vs 基座 LM」隔离出真正接触数据的价值。

## Strengths

- 评估开放式分析判断，正是真实数据驱动科学的核心。
- 发表信息经核实，仓库与项目页公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；摘要称 12 个数据集，而仓库列出更多具名数据集——以论文的 12 为准。「Findings」为仓库限定词。

## Related Works

- [DSBench](./dsbench.md) — 同样是数据科学 agent 评估，考分析与建模任务。
- [DA-Code](./da-code.md) — 同样是数据科学 agent，聚焦可执行代码生成。
- [MLR-Bench](./mlr-bench.md) — 同样是开放式 ML 研究评估，在全流程尺度。
