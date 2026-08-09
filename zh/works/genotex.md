# GenoTEX (2024)

> [English](../../works/genotex.md) | **简体中文**

## Overview

GenoTEX 是自动化基因表达数据分析的 LLM agent benchmark：agent 按照计算基因组学的标准流程完成基因-性状关联问题的数据集选择、预处理与统计分析，评估对照生物信息学家的专家整理标注进行。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.15341>
- **Code:** <https://github.com/Liu-Hy/GenoTEX>
- **Venue:** arXiv preprint (cs.LG, cs.AI, q-bio.GN)；据官方仓库为 MLCB 2025 oral

## Summary

GenoTEX 为大量基因-性状关联问题配齐了由生物信息学家整理的参考分析代码与结果。据官方仓库，共 1,384 个基因-性状关联分析问题（132 个无条件、1,252 个条件性），覆盖 911 个数据集。论文另提出 GenoAgent——一组采用多步编程工作流并可灵活自我纠错的 LLM agent——作为基线；实验展示了 LLM 方法的潜力，错误分析则点明了尚存的挑战。

## Tasks

基因表达数据上的基因-性状关联分析问题——按计算基因组学标准完成数据集选择、预处理与统计分析；据官方仓库为 911 个数据集上的 1,384 个问题。

## Domains

计算基因组学与生物信息学：基因表达分析与基因-性状关联。

## Evaluation

- 将 agent 产出与生物信息学家的专家整理标注比较；benchmark 同时提供参考分析代码与结果。
- **报告。** 实验展示了 LLM 方法的潜力；错误分析点明挑战。具体数字为 TODO(reference)。

## Typical Duration

带自我纠错的多步编程分析流水线；预算为 TODO(reference)。

## Main Contribution

把基因组学 agent 评估锚定到一线生物信息学家的实际产出——专家整理的参考流水线与结果——而非合成标签。

## Key Design Ideas

- 评估单元是完整的分析流水线（选择 → 预处理 → 统计），而非单个问题。
- 专家参考代码使 agent 的分析可以逐步对照，而不只比最终答案。
- 条件性与无条件问题变体把直接关联与依赖上下文的分析分开。

## Strengths

- 基因组学分析上少见规模的专家整理真值（据仓库为 1,384 个问题、911 个数据集）。
- 遵循计算基因组学标准，分数反映领域实践。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: 论文的基线多 agent 方法 GenoAgent 属于 agent 实现，超出本仓库范围；本卡片记录其 benchmark。

## Related Works

- [BixBench](./bixbench.md) — 同样在真实计算生物学分析上评估 agent，用探索式 Jupyter 场景而非整理好的流水线。
- [GeneBench-Pro](./genebench-pro.md) — 同样是基因组学分析评估，构建于因果结构完全已知的构造性模拟数据。
- [ScienceAgentBench](./scienceagentbench.md) — 同样是专家验证、统一为可执行程序的数据分析任务，跨学科。
