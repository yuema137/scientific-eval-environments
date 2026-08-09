# MLE-bench (2024)

> [English](../../works/mle-bench.md) | **简体中文**

## Overview

MLE-bench 在机器学习工程上评测机器学习 agent：从 Kaggle 精选的 75 个 ML 工程竞赛，agent 须训练模型、准备数据、运行实验并产出提交，对照真实 Kaggle 排行榜评分——OpenAI 的 o1-preview（AIDE 脚手架）在 16.9% 的竞赛上达到至少铜牌水平。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07095>
- **Code:** <https://github.com/openai/mle-bench/>
- **Venue:** ICLR 2025

## Summary

MLE-bench（出自 OpenAI）衡量 agent 能否承担机器学习工程师的端到端工作。它从 Kaggle 精选 75 个 ML 工程竞赛，每个都有真实数据集，并以 Kaggle 公开排行榜建立人类基线，按 Kaggle 奖牌门槛（铜/银/金）为 agent 提交评分。agent 在开源脚手架（如 AIDE）中运行，须训练模型、准备数据、迭代实验。头条结果：OpenAI o1-preview 配 AIDE 脚手架在 16.9% 的竞赛上达到至少 Kaggle 铜牌；论文还研究了资源扩展与预训练污染。

## Tasks

75 个精选的 Kaggle ML 工程竞赛；agent 做端到端 ML 工程（数据准备、模型训练、实验），提交对照竞赛排行榜评分。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——机器学习工程：在真实 Kaggle 任务上构建并训练模型以参赛。

## Evaluation

- 每个竞赛的 Kaggle 排行榜人类基线与奖牌门槛（铜/银/金）；资源扩展与污染分析。
- **报告。** OpenAI o1-preview 配 AIDE 脚手架在 16.9% 的竞赛上达到至少铜牌水平。

## Typical Duration

每个竞赛一段长 horizon 端到端回合（多步数据准备、训练与迭代）。

## Main Contribution

自主 ML 工程的参照 benchmark——把 agent 能力锚定在带奖牌级人类基线的真实 Kaggle 竞赛上，而非合成任务。

## Key Design Ideas

- Kaggle 排行榜提供真实、定量的人类基线与奖牌门槛。
- 离线精选 75 个竞赛，使套件可复现、可评分。
- 显式的污染与资源扩展研究预先排除了明显混淆因素。

## Strengths

- 真实竞赛、按奖牌门槛评分；OpenAI 开源，被广泛采用（如作为 MLE-Dojo 与 AIDE 的底座）。
- 16.9% 铜牌是 ML 工程 agent 清晰、可引用的能力标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv Comments 载明「ICLR version」（ICLR 2025）；参评模型的确切数量摘要未载明。

## Related Works

- [MLE-Dojo](./mle-dojo.md) — 在 200+ Kaggle 挑战（部分复用 MLE-bench 竞赛）之上构建交互式 Gym 环境。
- [MLAgentBench](./mlagentbench.md) — 同样评测 agent 的 ML 实验，考 13 个「提升指标」任务。
- [DSBench](./dsbench.md) — 同样是 agent 式数据科学评估，考分析与建模任务。
