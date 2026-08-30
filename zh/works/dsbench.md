# DSBench (2024)

> [English](../../works/dsbench.md) | **简体中文**

> **首次公开：** 2024-09-12 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2409.07703)

## Overview

DSBench 追问数据科学 agent 离数据科学专家还有多远：540 个任务——466 个数据分析、74 个数据建模——带长上下文、多模态背景与多表数据，取自竞赛平台与 Kaggle，最佳 agent 只解出 34.12% 的分析任务。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.07703>
- **Code:** <https://github.com/LiqiangJing/DSBench>
- **Project:** <https://liqiangjing.github.io/dsbench.github.io/>
- **Venue:** ICLR 2025（据官方仓库；arXiv 元数据无发表信息）

## Summary

DSBench 为数据科学 agent 评估带来真实的复杂度：466 个数据分析与 74 个数据建模任务（共 540 个），取自竞赛来源与 Kaggle，带长文本上下文、图像与表格、以及多表数据。给定任务指令（可能含图像与表格）与数据文件，agent 须产出解决任务的方案。结果显示与专家水平差距很大：最佳 agent 只解出 34.12% 的数据分析任务，建模上有 34.74% 的相对性能差距。

## Tasks

540 个数据科学任务（466 分析 + 74 建模），带长上下文、多模态背景与多表数据；agent 据指令与数据文件产出方案。

## Domains

AI 与机器学习研究——数据科学：在真实感、多模态任务上做端到端数据分析与预测建模。

## Evaluation

- 分析用任务解出率；建模用相对性能差距（RPG）。
- **报告。** 最佳 agent 解出 34.12% 的分析任务，建模相对性能差距 34.74%。

## Typical Duration

在多模态、多表数据上按任务的求解回合。

## Main Contribution

一个真实感偏难的数据科学 benchmark——长上下文、多模态、多表——量化 agent 离专家级分析与建模还有多远。

## Key Design Ideas

- 多模态、多表任务反映真实数据科学的杂乱，而非干净的玩具表。
- 把分析与建模分开，隔离两种不同能力。
- 相对性能差距指标对照有意义的参照为建模评分。

## Strengths

- 比早期数据分析问答集更大、更真实，公开发布。
- 34% 的上限是专家差距的清晰、可引用标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ICLR 2025 是仓库声明，arXiv 元数据未载明。任务来源描述为竞赛来源与 Kaggle（各来源中出现「ModelOff」/「Eloquence」命名）。

## Related Works

- [DA-Code](./da-code.md) — 同样是 agent 式数据科学评估，聚焦沙箱中的代码生成。
- [BLADE](./blade.md) — 同样是数据驱动科学分析，以专家参考分析为依据。
- [MLE-bench](./mle-bench.md) — 同样是以 Kaggle 为依据的 agent 评估，考带奖牌评分的 ML 工程。
