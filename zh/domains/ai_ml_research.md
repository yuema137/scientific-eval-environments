# AI & Machine Learning Research

> [English](../../domains/ai_ml_research.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为被研究科学的 AI 与机器学习：复现、重发现与扩展已发表的 AI 研究。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| EXP-Bench | 2025 | 完成来自有影响力 AI 论文的完整研究实验——提出假设、设计并实现流程、执行、得出结论——覆盖计算机视觉、NLP 与强化学习。 | 461 个任务，来自 51 篇 NeurIPS 2024 与 ICLR 2024 论文，分解为 12,737 个可单独评分的子任务，每个任务给定研究问题与不完整起始代码。 | 设计、实现（对照真值 git diff）与结论由 LLM judge 评分，另有容器化执行验证器；All·E✓ 要求四项全对（最佳报告值 0.5%）。 | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | 在只给高层研究问题的条件下，重新发现近期高影响力 ML 研究中已确立、可验证的发现——LLM 行为实证研究，外加 CV 与神经网络分析扩展。 | 40 个完整执行的任务，构建自逐论文的研究问题树（根问题 → 子问题 → 叶实验）；全部轻量计算（单块 80GB A100 上 ≤24 小时）。 | 把 agent 结论与真值发现各自拆为原子主张后做语义蕴含匹配，计主张级 precision/recall/F1；judge 与人类对照验证 F1 达 0.89。 | [→](../works/fire-bench.md) |
| AIRS-Bench | 2026 | 语言建模与时间序列预测（连同数学与生物信息学）中的前沿研究任务，覆盖完整研究生命周期，不提供基线代码。 | 20 个任务；agent 以 CSV 提交留出测试集上的预测。 | 基于执行、只看结果：任务专属评估脚本计分；SOTA 归一化分数，接近上限处用 'march of nines' 变换。 | [→](../works/airs-bench.md) |
| AstaBench | 2025 | 以计算机科学为主的整体科研能力：文献理解、代码与执行、数据分析、端到端发现；许多问题来自真实用户对已部署 Asta agent 的请求。 | 11 个 benchmark 共 2,400+ 个问题，配标准可复现工具环境与逐 benchmark 的语料日期截止；已为 57 个 agent 计分。 | 各 benchmark 自有指标（F1、recall@30、精确匹配、LLM 评判的 rubric 与假设匹配），随时间不变的美元成本核算与分数–成本 Pareto 前沿一并报告。 | [→](../works/astabench.md) |

## Related Works

- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
