# ML-Bench (2023)

> [English](../../works/ml-bench.md) | **简体中文**

## Overview

ML-Bench 在仓库级代码上评测 LLM 与 agent 的机器学习任务：18 个 GitHub 仓库上的 9,641 个样例，分为 ML-LLM-Bench（在仓库上下文中据任务描述生成代码）与 ML-Agent-Bench（在 Linux 沙箱中自主端到端执行任务）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.09835>
- **Code:** <https://github.com/gersteinlab/ML-bench>
- **Project:** <https://ml-bench.github.io/>
- **Venue:** arXiv preprint (cs.CL), 2023

## Summary

ML-Bench 衡量模型能否使用真实 ML 仓库，而不只是写孤立片段：18 个 GitHub 仓库上的 9,641 个样例，分两条赛道。ML-LLM-Bench 是静态文本到代码——给定任务描述与仓库上下文（含检索或 oracle 配置），LLM 生成可运行代码，以 Pass@5 评分。ML-Agent-Bench 是 agent 化的——自主 agent 在 Linux 沙箱（集成 OpenDevin）中端到端执行任务，以成功率评分。GPT-4o 在 LLM 赛道 Pass@5 超过 50%，在 agent 赛道成功率达 76.47%。

## Tasks

18 个 GitHub 仓库上的 9,641 个仓库级 ML 任务，分两条赛道：ML-LLM-Bench（带仓库上下文的静态文本到代码）与 ML-Agent-Bench（Linux 沙箱中的自主端到端执行）。

## Domains

AI 与机器学习研究——仓库级 ML 代码：使用真实 ML 代码库完成任务。

## Evaluation

- LLM 代码生成赛道用 Pass@5；agent 执行赛道用成功率。
- **报告。** GPT-4o：ML-LLM-Bench 上 Pass@5 超过 50%，ML-Agent-Bench 上成功率 76.47%。

## Typical Duration

单次生成（LLM 赛道）或多步沙箱执行回合（agent 赛道）。

## Main Contribution

把仓库级上下文引入 ML 任务评估——在同一批真实代码库上，把文本到代码能力与自主端到端执行分开。

## Key Design Ideas

- 仓库上下文考察模型能否导航并使用真实 ML 代码，而非只是回忆 API。
- LLM/agent 双赛道把代码生成与自主执行分开。
- 检索与 oracle 配置调节给模型多少上下文。

## Strengths

- 规模大（9,641 样例），在真实 ML 仓库上双赛道设计。
- 仓库与项目页公开，两条赛道均发布。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息。

## Related Works

- [ResearchCodeBench](./researchcodebench.md) — 同样是「据描述实现 ML」，考把近期论文贡献翻译成代码。
- [SUPER](./super.md) — 同样是执行研究仓库中的任务，聚焦搭建与复现。
- [MLAgentBench](./mlagentbench.md) — 同样是 agent 化 ML 任务，考「提升指标」的实验。
