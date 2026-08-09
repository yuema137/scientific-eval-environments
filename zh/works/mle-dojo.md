# MLE-Dojo (2025)

> [English](../../works/mle-dojo.md) | **简体中文**

## Overview

MLE-Dojo 是训练、评估并改进自主 LLM agent 做机器学习工程的 Gym 式交互环境：200+ 个真实 Kaggle 挑战，配结构化反馈循环，覆盖数据处理、架构搜索、超参调优与代码调试，在八个前沿 LLM 上评估。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07782>
- **Code:** <https://github.com/MLE-Dojo/MLE-Dojo>
- **Project:** <https://mle-dojo.github.io/MLE-Dojo-page/>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

MLE-Dojo 把 ML 工程评估变成交互式竞技场：agent 在 200+ 个真实 Kaggle 挑战（据仓库：68 个来自 MLE-bench、74 个来自 DSBench、75 个新抓取）上，通过结构化反馈迭代地实验、调试、精修。除了评估，该环境还支持对 agent 做监督微调与强化学习，把 ML 工程定位为可训练的交互式任务。评估覆盖八个前沿 LLM，环境测量迭代改进、长 horizon 解质量与错误修复效率。

## Tasks

交互环境中的 200+ 个 Kaggle 派生 ML 工程挑战；agent 借结构化反馈在数据处理、架构搜索、超参调优与调试上迭代。交互式 agent 化、长 horizon；支持 SFT/RL agent 训练。

## Domains

AI 与机器学习研究——作为交互式、可训练环境的机器学习工程。

## Evaluation

- 环境测量的迭代改进、长 horizon 解质量与错误修复效率，覆盖八个前沿 LLM。
- **报告。** 评估了八个前沿 LLM；贡献是环境及其测量维度，而非单一头条分数。

## Typical Duration

每个挑战一段长 horizon 交互回合，含迭代的实验-调试循环。

## Main Contribution

一个让 ML 工程既可评估又可训练的 Gym 式环境——闭合了从 benchmark 到 ML 工程 agent 强化学习的闭环。

## Key Design Ideas

- 结构化反馈循环把一次性提交变成可交互、可改进的任务。
- 汇集 MLE-bench、DSBench 与新 Kaggle 挑战，把覆盖扩展到 200+。
- SFT/RL 支持使同一批挑战成为训练环境而非仅测试集。

## Strengths

- 可交互、可训练的环境，而非静态提交 benchmark。
- 复用既有套件加新挑战，Kaggle 覆盖广。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；这既是环境/框架也是 benchmark，各模型数值结果在正文中。arXiv 元数据无发表信息。

## Related Works

- [MLE-bench](./mle-bench.md) — MLE-Dojo 部分复用其 Kaggle 竞赛的 benchmark。
- [MLGym](./mlgym.md) — 同样是面向 AI 研究 agent 的 Gym 环境，覆盖更广的研究任务。
- [MLAgentBench](./mlagentbench.md) — 同样是迭代式 ML 实验评估，但无 RL 训练环境。
