# MLGym (2025)

> [English](../../works/mlgym.md) | **简体中文**

> **首次公开：** 2025-02-20 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2502.14499)

## Overview

MLGym 是首个面向 AI 研究任务的 Gym 环境——支持对「训练 agent」做强化学习研究——配套 MLGym-Bench，一个含 13 个横跨计算机视觉、NLP、强化学习与博弈论的开放式 AI 研究任务的 benchmark。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.14499>
- **Code:** <https://github.com/facebookresearch/MLGym>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

出自 Meta GenAI 与 UCSB，MLGym 提供首个面向机器学习研究任务的 Gym 环境，使得可以用强化学习在研究工作上训练 agent。其 benchmark MLGym-Bench 含 13 个横跨 CV、NLP、RL 与博弈论的开放式 AI 研究任务，演练完整研究循环：生成想法与假设、创建并处理数据、实现 ML 方法、训练模型、运行实验、分析结果、迭代。评估 Claude-3.5-Sonnet、Llama-3.1-405B、GPT-4o、o1-preview 与 Gemini-1.5-Pro，论文发现前沿模型能在给定基线上改进——通常靠找更好的超参——但不产生新颖的假设、算法、架构或实质性提升。

## Tasks

13 个开放式 AI 研究任务（MLGym-Bench），横跨 CV、NLP、RL 与博弈论；agent 在 MLGym 环境中跑完整研究循环。交互式 agent 化、长 horizon；支持 agent 的 RL 训练。

## Domains

AI 与机器学习研究——横跨 CV、NLP、RL 与博弈论的开放式 AI 研究，在可训练的 Gym 环境中。

## Evaluation

- 五个前沿模型在 13 个 MLGym-Bench 任务上的表现，在 Gym 环境内。
- **报告。** 前沿模型能在基线上改进（多靠超参），但不产生新颖假设、算法、架构或实质性提升。

## Typical Duration

每个任务一段长 horizon 研究循环回合；该环境也支持 RL 训练。

## Main Contribution

首个面向 AI 研究任务的 Gym 环境——把 ML 研究变成可 RL 训练的设定——配一个 13 任务 benchmark，表明前沿 agent 会调参却不创新。

## Key Design Ideas

- Gym 接口把 AI 研究变成可 RL 训练的环境，而非仅测试集。
- 13 个任务横跨四个子领域，防止 benchmark 过拟合单一领域。
- 演练完整研究循环，暴露「会调参不创新」的上限。

## Strengths

- 支持对「训练 AI 研究 agent」做 RL 研究，出自 Meta，公开发布。
- 「能改进基线但不创新」的发现干净地界定了当前能力。

## Limitations

- Repository note: 该论文既贡献 MLGym 框架/环境，也贡献 MLGym-Bench benchmark；本卡片以 benchmark 为中心。arXiv 元数据无发表信息。

## Related Works

- [MLE-Dojo](./mle-dojo.md) — 同样是面向 ML 工程 agent 的 Gym 环境，聚焦 Kaggle 挑战。
- [RE-Bench](./re-bench.md) — 同样是开放式 AI R&D 任务，对照人类专家评测。
- [MLR-Bench](./mlr-bench.md) — 同样是全流程 ML 研究自动化，由自动评审评分。
