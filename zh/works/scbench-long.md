# scBench-Long (2026)

> [English](../../works/scbench-long.md) | **简体中文**

## Overview

scBench-Long 是长 horizon 单细胞生物学的可验证 benchmark：21 项评估要求 agent 在不预设方法的前提下，从原始或近原始数据复原科学结论，涵盖黑色素瘤 CD8 T 细胞反应性、RNA+ATAC 调控推断、人-猴嵌合体发育、KRAS 驱动的肺肿瘤衰老与致死性 COVID-19 肺部病理。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.26563>
- **Venue:** arXiv preprint (q-bio.GN, cs.AI), 2026

## Summary

scBench 隔离单个分析步骤，scBench-Long 则要求走完全程：从近原始数据出发——整合元数据、实验检测方法背景与辅助证据——一路推到研究的实际科学结论，方法不作规定。候选结论经复现、评审后转换为受控答案词表，配确定性判分与轨迹评分标准。在 1,068 条完成的轨迹中，最强的模型-harness 组合也只通过 63 次运行中的 16 次（25.4%）。

## Tasks

21 项长 horizon 评估，覆盖配对 scRNA/TCR 测序、RNA 与染色质（ATAC）联合分析、跨物种转录组、单核 RNA-seq 与免疫组库数据；agent 从原始或近原始数据做到科学结论。

## Domains

长 horizon 单细胞生物学，横跨黑色素瘤 T 细胞生物学、发育生物学（人-猴嵌合体）、肺癌与 COVID-19 肺部病理。

## Evaluation

- 候选结论经复现、评审并转换为受控答案词表；确定性判分加轨迹评分标准。
- **报告。** 在 1,068 条完成轨迹中，最强模型-harness 组合通过 16/63 次运行（25.4%）。

## Typical Duration

从近原始数据出发的长 horizon 多步分析轨迹；预算为 TODO(reference)。

## Main Contribution

让端到端的生物学发现变得可验证：受控答案词表使确定性判分器能为 agent 沿任意路径得出的结论打分。

## Key Design Ideas

- 不预设方法——通往结论的路径是 agent 自己的问题，与真实分析一致。
- 受控答案词表调和了开放式发现与确定性判分。
- 轨迹评分标准在终点之外同时给过程打分。

## Strengths

- 以真实且事关重大的研究（癌症、COVID-19 病理）为真值。
- 最强组合 25.4% 的上限量化了距自主分析的距离。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [scBench](./scbench.md) — 同一确定性判分理念下的单步姊妹篇。
- [BAISBench](./baisbench.md) — 同样检验对已发表单细胞发现的复原，用标注与选择题加人类基线。
- [FIRE-Bench](./fire-bench.md) — 同样是对已发表发现的全流程再发现，在机器学习研究领域。
