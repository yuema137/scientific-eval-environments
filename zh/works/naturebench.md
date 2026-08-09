# NatureBench (2026)

> [English](../../works/naturebench.md) | **简体中文**

## Overview

NatureBench 评估 AI coding agent 是否能匹敌 Nature-family 科学出版物的已发表 SOTA——被作者框定为一次从"复现"走向"方法论发现"的评估尝试。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.24530>

## Summary

NatureBench 从同行评审的 Nature-family 论文中蒸馏任务，追问 coding agent 是否能达到甚至超越已发表 SOTA。该 benchmark 同时考察跨学科的科学覆盖，以及要匹敌一份真实出版物结果所需的深度。

## Tasks

90 个从同行评审的 Nature-family 论文（2022–2025）中蒸馏出的任务，覆盖六个领域：Cellular Omics 31、Protein Biology 16、Biomedical Modeling 14、Physical Modeling 13、Molecular Design 11、Relational Reasoning 5。任务由一条经评审把关的 “NatureGym” 流水线从约 5,500 篇候选论文构造，并设有信息防火墙——只把目标算法的输入交给 agent，而不给出其操作或输出。

## Domains

从 Nature-family 论文蒸馏的六个领域：Cellular Omics、Protein Biology、Biomedical Modeling、Physical Modeling、Molecular Design、Relational Reasoning。

## Evaluation

- **SOTA 归一化的相对差距。** 每个实例指定一个主指标；得分 g = dir · (m − m_sota) / |m_sota|，其中 m 是 agent 的取值、m_sota 是论文报告的 SOTA、dir ∈ {+1, −1} 表示指标方向——使 g 无量纲且可跨所用的 81 种异构指标（AUROC、RMSE、Spearman ρ、ARI、F1……）比较。g ≥ 0 表示 agent 匹敌或超越已发表结果。任务分数对其各实例的 g 取平均（每任务平均 3.7 个主指标）；提交失败记 g = −1.0，并由 Claude Sonnet 4.6 judge 标记走捷径的运行。
- **在 90 个任务上的两个阈值率：** Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）。
- **报告：** 最强 agent Claude Opus 4.7 在严格禁用联网检索、跨三种 harness（Claude Code、Codex CLI、Gemini CLI）的协议下，仅在 17.8% 的任务上超越 SOTA（g > 0.1，≈16/90），在 47.8% 上匹敌（g ≥ 0，≈43/90）。
- 作者观察：agent 的成功往往来自将科学问题重构为常规的预测任务，而非真正的方法论创新。

## Typical Duration

每任务 4 小时 wall-clock 预算（评分时时钟暂停）。按任务分配算力：3 个仅 CPU 任务、70 个用单张 RTX 3090/4090、17 个最密集任务用单张 A800。

## Main Contribution

将 benchmark 难度锚定在顶级科学出版物的已发表 SOTA 上——提供一个与真实研究产出对齐的门槛，而非由人工挑选的玩具任务。

## Key Design Ideas

- 任务源自 Nature-family 出版物，给出一个真实的 SOTA 参照。
- 单个 benchmark 内的跨学科覆盖。
- 显式区分 "匹敌 SOTA" 与 "发现"。

## Strengths

- SOTA 锚点使难度直接与已发表科学结果绑定。
- 揭示了一个显著缺口（最强 agent 仅在 17.8% 的任务上超越 SOTA），且参照是硬指标。
- 作者观察揭示了一个独立的评估关注点（问题重构）。

## Limitations

- Repository note: 蒸馏自 Nature-family 出版物——覆盖会受该系列刊物编辑偏好塑形。

## Related Works

- [AIRS-Bench](./airs-bench.md) — 同样面向研究生命周期，但围绕自建任务集组织，而非以已发表 SOTA 为锚点。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样面向科学，但聚焦容器化可执行验证。
