# scBench (2026)

> [English](../../works/scbench.md) | **简体中文**

> **首次公开：** 2026-02-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.09063)

## Overview

scBench 评估 AI agent 的单细胞 RNA-seq 分析能力：394 个可验证问题，横跨六种测序平台与七类任务，每个问题把「某个分析步骤开始前一刻」的实验数据快照交给 agent，并以确定性判分器检验关键生物学结果是否被复原。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.09063>
- **Venue:** arXiv preprint (q-bio.GN, cs.AI), 2026

## Summary

scBench 在真实 scRNA-seq 数据上隔离单个分析步骤：agent 拿到某步骤开始前的数据，须完成该步分析并复原已知的生物学结果，由确定性判分器打分。在八个前沿模型上，准确率介于 29–53%，且模型-任务与模型-平台交互效应显著——平台选择对准确率的影响不亚于模型选择，在文档较少的技术上会掉 40 个百分点以上。该 benchmark 与 SpatialBench 互补，覆盖单细胞领域两大主流模态。

## Tasks

394 个可验证的 scRNA-seq 分析问题，横跨六种测序平台、七类任务，均从步骤前数据快照出发。

## Domains

覆盖六种测序平台的单细胞 RNA 测序分析。

## Evaluation

- 确定性判分器检验关键生物学结果的复原；指标为准确率。
- **报告。** 八个前沿模型的准确率为 29–53%；平台选择与模型选择同等重要，在文档较少的技术上跌幅超过 40 个百分点。

## Typical Duration

真实数据集上的单步分析回合。

## Main Contribution

对真实单细胞分析做确定性、基于快照的判分，揭示 agent 能力是模型-平台组合的属性，而不只是模型的属性。

## Key Design Ideas

- 步骤前快照的设计精确锁定每个问题测量的是哪项分析能力。
- 确定性判分在一个充满「看似合理的错误分析」的领域里消除了 judge 噪声。
- 平台多样性把工具文档覆盖度变成被测变量。

## Strengths

- 在真实（而非合成）数据上做到规模化的可验证性（394 个问题）。
- 平台效应（40+ 个百分点）的发现对部署有直接指导意义。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。论文的 arXiv 页面上无可验证的代码发布。

## Related Works

- [SpatialBench](./spatialbench.md) — 同一「快照 + 确定性判分」设计的空间模态姊妹篇。
- [scBench-Long](./scbench-long.md) — 长 horizon 扩展：从近原始数据复原已发表结论。
- [HeurekaBench](./heurekabench.md) — 同样是单细胞 agent 评估，用对照已发表发现评判的开放式问题。
