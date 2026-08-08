# CMPhysBench (2025)

> [English](../../works/cmphysbench.md) | **简体中文**

## Overview

CMPhysBench 是凝聚态物理领域的 benchmark，含 520 余道精心整理的研究生水平计算题，用 Scalable Expression Edit Distance（SEED）——一种对解答表达式的细粒度、非二元部分得分——进行评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.18124>
- **Code:** <https://github.com/CMPhysBench/CMPhysBench>
- **Venue:** arXiv preprint (cs.LG, cs.AI), 2025

## Summary

CMPhysBench 面向凝聚态物理——磁学、超导、强关联体系与基础理论框架——的计算型问题，要求模型独立生成完整解答而非选出答案。其 SEED 分数按表达式相似度给出部分得分，与二元准确率互补。

## Tasks

520 余道研究生水平的计算型问题，覆盖磁学、超导、强关联体系等凝聚态子领域；每题要求独立生成完整解答。

## Domains

凝聚态物理：磁学、超导、强关联体系与基础理论框架。

## Evaluation

- **SEED（Scalable Expression Edit Distance）**对解答表达式给出细粒度、非二元的部分得分。
- **准确率**为正确解答的百分比。
- **报告。** 即便最佳模型 Grok-4 也仅达到平均 SEED 36 分与 28% 准确率。

## Typical Duration

单题推导；非交互式 agent 设定。

## Main Contribution

用表达式级部分得分指标把研究生水平的凝聚态物理纳入定量评估，揭示前沿模型仍存在的巨大能力缺口。

## Key Design Ideas

- 计算题要求生成推导，而非选择题式的识别。
- SEED 的表达式编辑距离衡量错误推导“差多远”——二元准确率对此视而不见。
- 代码与数据集公开发布。

## Strengths

- 单一领域内研究生水平的规模（520+ 题）。
- 部分得分使全对/全错阈值之下的模型差异可见。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — 同样是凝聚态评估，但为专家研究者水平的 50 道机器判分问题。
- [PRBench](./prbench.md) — 同样是超越考试的物理评估，通过端到端复现已发表研究。
- [CFDLLMBench](./cfdllmbench.md) — 同样在一个物理仿真领域把知识层与部分得分判分配对。
