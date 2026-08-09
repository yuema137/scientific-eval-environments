# MLAgentBench (2023)

> [English](../../works/mlagentbench.md) | **简体中文**

## Overview

MLAgentBench 在机器学习实验上评测语言 agent：一套 13 个任务——从提升 CIFAR-10 准确率到 BabyLM 等近期研究问题——agent 读写文件、执行代码、检查输出并迭代以超过起始代码基线，最强 agent（Claude 3 Opus）平均成功率 37.5%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.03302>
- **Code:** <https://github.com/snap-stanford/MLAgentBench>
- **Venue:** ICML 2024

## Summary

MLAgentBench 把 ML 研究框定为交互式 agent 任务：给定任务与起始代码，一个 ReAct 式 agent 读取可用文件、在计算集群上运行实验、检查输出并迭代以提升目标指标。其 13 个任务从成熟数据集（CIFAR-10）到近期研究问题（BabyLM）与 Kaggle 挑战。在 Claude v1/v2.1/v3-Opus、GPT-4、GPT-4-turbo、Gemini-Pro 与 Mixtral 上，最强 agent（Claude 3 Opus）平均成功率 37.5%——成功率从成熟数据集上的 100% 到近期 Kaggle 挑战上的 0% 不等。

## Tasks

13 个 ML 实验任务；agent 读写文件、执行代码、检查输出，以超过起始代码基线提升指标。交互式 agent 化、长 horizon。

## Domains

AI 与机器学习研究——ML 实验：在成熟与近期研究任务上迭代提升模型性能。

## Evaluation

- 成功率（最终步相对起始代码基线提升超过 10% 的运行）与平均提升。
- **报告。** Claude 3 Opus 最强、平均成功率 37.5%；成功率从 100%（成熟数据集）到 0%（近期 Kaggle 挑战）不等。

## Typical Duration

长 horizon 回合：每个任务反复「读取-执行-检查-迭代」。

## Main Contribution

把 ML 研究做成交互式 agent benchmark 的早期、有影响力的表述——「提升指标」任务，以相对起始代码的实测提升评分。

## Key Design Ideas

- 「相对基线的提升」评分奖励真实的实验进展，而非仅完成。
- 从旧数据集到近期 Kaggle 任务的跨度暴露了「新近性/污染」梯度。
- ReAct 式的文件/代码/输出动作对应研究者实际的迭代方式。

## Strengths

- 奠基性的 ML 实验 agent benchmark，公开材料持续维护。
- 100% 到 0% 的新近性落差干净地展示了记忆 vs 真实能力。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ICML 2024 发表信息未见于 arXiv Comments（经 OpenReview 单独确认）。

## Related Works

- [MLE-bench](./mle-bench.md) — 同样是 ML 工程 agent 评估，考 75 个带奖牌评分的 Kaggle 竞赛。
- [RE-Bench](./re-bench.md) — 同样是开放式 ML R&D 任务，在时间预算下与人类专家对照。
- [MLGym](./mlgym.md) — 同样是开放式 AI 研究任务，在跨 CV/NLP/RL 的 Gym 环境中。
