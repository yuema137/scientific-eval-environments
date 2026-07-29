# AIRS-Bench (2026)

## Overview

AIRS-Bench (AI Research Science Benchmark) 是面向 LLM agent 的 frontier 研究科学任务套件，共 20 个任务，覆盖全研究生命周期，跨越语言建模、数学、生物信息学与时间序列预测——且不提供 baseline 代码。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.06855>

## Summary

AIRS-Bench 在完整研究生命周期上评估 agent 能力，而不是孤立的编码子任务。任务跨越四个科学领域，设置上不提供 baseline 代码，因此 agent 必须从零构造端到端的研究工作流。

## Tasks

20 个任务。

## Domains

语言建模、数学、生物信息学、时间序列预测。

## Evaluation

- **基于执行、只看结果。** 尽管任务以完整研究生命周期为框架，打分只针对最终产物：agent 提交测试集预测的 `.csv`，由每个任务的 `evaluate.py` 对照测试标签评分——无 LLM judge、无过程 rubric，也不提供 baseline 代码。
- **Normalized Score (NS)。** 逐任务地，NS = [φ(s) − φ(s_min)] / [φ(s_sota) − φ(s_min)]，其中 s_min 是所有 seed / agent 中观测到的最差分，s_sota 为文献 SOTA；0 = 最差、1 = 人类 SOTA、>1 = 超过 SOTA。“march of nines” 变换 φ(s) = −log₁₀|s − s_opt|（s_opt 为理论最优）对接近上限的提升做对数缩放，使其仍然可辨。
- **Valid Submission Rate (VSR)** — 产生可执行、可评分提交的运行比例。
- **Elo** — 对 agent 得分两两比较的 Bradley–Terry 评分。
- **报告：** 平均 normalized score ≈ 24.1%；平均有效提交率 ≈ 55.1%；仅约 1.58% 的提交超过 SOTA。按逐任务平均，agent 在 20 个任务中的 4 个上超过人类 SOTA（16 个未被超越），且人类 SOTA 在 Elo 上高于所有 agent。

## Typical Duration

每次运行历时 24 小时、使用一块 H-200 GPU，每个任务至少启动 10 次（“seed”）。作者将其归为高算力 benchmark（每任务 >1 小时）；部分任务被指出受算力或时间限制。

## Main Contribution

一个 frontier 研究科学 benchmark，去除 baseline 代码，要求 agent 在一个精简但多领域的任务集上从零构造端到端的研究工作流。

## Key Design Ideas

- 不提供 baseline 代码——agent 从零构造工作流。
- 覆盖完整研究生命周期，而不仅是建模或评估子任务。
- 在紧凑的 20 任务套件内实现多领域覆盖。
- Normalized Score 配合 “march of nines” 对数变换，使接近性能上限的提升仍然可辨；辅以 Valid Submission Rate 与 Elo。

## Strengths

- 去除 baseline 代码逼近真正的 agent 驱动研究设计。
- 紧凑但多领域，便于聚焦跨子领域的评估。

## Limitations

- Repository note: 20 个任务——相较典型 benchmark 是较小的任务池。
- Repository note: 尽管以完整研究生命周期为框架，打分只看结果（预测 `.csv` 对照留出标签）；构思与迭代改进过程未被直接评分。

## Related Works

- [NatureBench](./naturebench.md) — 同样面向研究科学，但锚定于 Nature-family 已发表 SOTA。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样面向科学工作流，但采用容器化可执行验证。
