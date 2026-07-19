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

面向完整研究生命周期的 agent 能力评估。摘要提到 baseline 参照来自人类表现。

## Typical Duration

TODO(reference): 摘要未给出每任务时长。

## Main Contribution

一个 frontier 研究科学 benchmark，去除 baseline 代码，要求 agent 在一个精简但多领域的任务集上从零构造端到端的研究工作流。

## Key Design Ideas

- 不提供 baseline 代码——agent 从零构造工作流。
- 覆盖完整研究生命周期，而不仅是建模或评估子任务。
- 在紧凑的 20 任务套件内实现多领域覆盖。

## Strengths

- 去除 baseline 代码逼近真正的 agent 驱动研究设计。
- 紧凑但多领域，便于聚焦跨子领域的评估。

## Limitations

- Repository note: 20 个任务——相较典型 benchmark 是较小的任务池。

## Related Works

- [NatureBench](./naturebench.md) — 同样面向研究科学，但锚定于 Nature-family 已发表 SOTA。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样面向科学工作流，但采用容器化可执行验证。
