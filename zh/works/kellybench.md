# KellyBench (2026)

> [English](../../works/kellybench.md) | **简体中文**

## Overview

KellyBench 是评估非平稳市场中长 horizon 序贯决策的环境：agent 置身于 2023–24 赛季英超联赛的逐轮推进模拟中，要在体育博彩市场上最大化长期本金增长。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.27865>
- **Project:** <https://openreward.ai/GeneralReasoning/KellyBench>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

KellyBench 瞄准的是「程序性 benchmark 正在饱和」与「真实部署是长 horizon、非平稳、目标开放的环境」之间的落差。agent 获得详尽的历史数据——高阶统计、首发阵容、公开赔率——要想成功，就得构建机器学习模型、在公开市场中找到优势，并随环境变化不断调整。在五个种子上，所有受评前沿模型平均都在亏钱：最好的平均回报为 −8%，破产在各个种子上都很常见。人类专家评分标准另行评判策略的精细程度；Claude Opus 4.6 得 26.5%，远低于人类基线。

## Tasks

一整个赛季（2023–24 英超）的序贯博彩决策模拟，环境持续演变，共五个种子；agent 持续管理本金，而非解决离散任务。

## Domains

作为序贯决策环境的体育博彩市场；无科学或工程领域。

## Evaluation

- 长期本金增长（五个种子上的平均回报），另配人类专家评分标准评判策略的精细程度。
- **报告。** 所有受评前沿模型平均亏损；最佳为 −8% 回报，破产在各个种子上都很常见；Claude Opus 4.6 的策略精细度评分为 26.5%。

## Typical Duration

每次运行为一整个模拟赛季的序贯决策。

## Main Contribution

一个以「活下来」本身为指标的开放式、非平稳 horizon——暴露出在程序性 benchmark 上饱和的模型仍不会跨时间管理风险。

## Key Design Ideas

- 本金动态使风险管理（而非准确率）成为硬约束：破产是吸收态。
- 非平稳性迫使持续调整，而非一套固定策略。
- 货币结果与精细度评分标准配对，把运气带来的回报与稳健的策略分开。

## Strengths

- 少见的真正开放式目标（增长），且自然真值毫不留情。
- 所有前沿模型平均为负回报，记录了任务套件看不见的能力断崖。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [Gaia2](./gaia2.md) — 同样把时间动态变成受评能力，环境按自己的时钟推进。
- [FinTrace](./fintrace.md) — 同样是长 horizon 金融决策，对工具使用给出轨迹级指标。
- [CostBench](./costbench.md) — 同样评估经济决策质量，在动态定价的规划条件下。
