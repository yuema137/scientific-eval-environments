# BrainBench (EEG) (2026)

> [English](../../works/brainbench-eeg.md) | **简体中文**

> **首次公开：** 2026-08-04 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.04156)

## Overview

BrainBench (EEG) 评测 LLM 的综合 EEG 理解：指令条件下的分析，覆盖四个子集——基础分析、睡眠评估、神经认知评估、生理整合——共 17 个数据集，系统须分析 EEG 记录并产出有科学依据的报告。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.04156>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

与更早那个「预测神经科学结果」的 BrainBench 不同，本 benchmark 瞄准 EEG 信号理解。给定一条指令与 EEG 记录（可含生理信号），系统须完成分析并产出有科学依据的报告，必要时还有产物。它覆盖四个子集——基础分析、睡眠评估、神经认知评估、生理整合——共 17 个数据集，并在两种执行范式下评估模型：以 CodeAct 做自主代码执行、以 BrainAgent 做结构化 agent 分析，累计逾 10 万次执行。输出沿数值、类别、集合、序列、语义与产物六个维度校验，结果在模型、子集、难度与范式之间差异显著。

## Tasks

覆盖四个子集、17 个数据集的指令条件 EEG 分析任务；系统分析记录并产出报告/产物，在自主代码执行（CodeAct）与 agent（BrainAgent）两种范式下进行。交互式/agent 化。确切的任务、实例与模型数量为 TODO(reference)——arXiv 摘要中未解析。

## Domains

神经科学与认知科学——脑电图分析：横跨基础、睡眠、神经认知与生理任务的信号处理、定量证据与科学解读。

## Evaluation

- 多维度校验：数值、类别、集合、序列、语义与产物检查，累计逾 10 万次执行。
- **报告。** 结果在模型、子集、难度与执行范式间差异显著；具体数字为 TODO(reference)。

## Typical Duration

每个 EEG 任务一段多步的 agent 分析回合（代码执行或结构化 agent 工作流）。

## Main Contribution

一个指令条件、基于执行的 EEG 理解 benchmark，覆盖从信号处理到科学解读的分析工作流，并评估自主代码与 agent 两种范式。

## Key Design Ideas

- 六种校验模式（数值……产物）为异质的 EEG 分析输出评分。
- 两种执行范式（CodeAct vs BrainAgent）在同一任务上比较不同自主风格。
- 四个具科学/临床意义的子集构成难度范围。

## Strengths

- 在一个专门模态上覆盖广（17 个数据集）、执行规模大（逾 10 万次）。
- 基于执行的校验，而非文本相似度评分。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；若干规模数字（任务、实例、模型数量）在 arXiv 页面为未解析的 LaTeX 宏，标为 TODO(reference)。代码与 benchmark 称「即将发布」，尚无 URL。
- Repository note: 名称冲突——本工作不同于已收录的 [BrainBench](./brainbench.md)（预测神经科学实验结果，2024）。

## Related Works

- [BrainBench](./brainbench.md) — 更早的、无关的 BrainBench：预测神经科学实验结果。
- [Rodent-Bench](./rodent-bench.md) — 同样是多模态神经科学数据分析，对象是啮齿类行为视频。
- [EnvTrace](./envtrace.md) — 同样是基于执行评估科学分析代码，走轨迹校验。
