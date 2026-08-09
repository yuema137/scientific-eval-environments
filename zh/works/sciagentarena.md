# SciAgentArena (2026)

> [English](../../works/sciagentarena.md) | **简体中文**

## Overview

SciAgentArena 是一个系统性 benchmark，用于在跨尺度的真实世界科学研究场景中评估 AI agent。它在一个交互式、agent-agnostic 的环境中提供约 200 个带逐步验证的任务。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12736>
- **Project:** <https://sciagentarena.github.io/>

## Summary

论文题为 *Benchmarking AI Agents for Addressing Scientific Challenges Across Scales*，SciAgentArena 针对 AI agent 在真实研究场景中的实际能力仍不清楚这一问题。它提供一个交互式、agent-agnostic 的环境，含约 200 个从真实世界科学研究场景构造、跨多个领域的任务，采用逐步验证。它报告 agent 在结构化数据分析工作流上表现良好，但在新颖洞见、自主探索与开放式问题上表现挣扎，并编目了常见失败模式。

## Tasks

约 200 个带逐步验证的任务（论文未给出确切整数），构造自跨五个领域的真实生物医学研究场景——单细胞组学、空间组学、计算药物发现、电子健康档案（EHR）建模与遗传学——外加一个小规模的跨领域集（eQTL、靶点识别、合成致死）。任务分四类：Data Analysis、Optimization、Discovery、Validity。

## Domains

跨五个领域的生物医学研究（单细胞组学、空间组学、计算药物发现、EHR 建模、遗传学）。“across scales”指的是生物学层级——分子 → 细胞 → 组织 → 人体 → 基因组 / 群体——而非物理尺度。

## Evaluation

- **按领域异构的逐步验证——基于执行与专家标准，而非 LLM judge。** 没有统一的全局 0–1 尺度；打分各领域原生：遗传学（PRS/MR）用专家设计的二元（0/1）逐子任务标准（以通过数报告，如“全部 14 个子任务”）、EHR（T1–T4）用把响应解析为动作列表后对 ground-truth 双向子串匹配的动作级 F1，其余领域用任务原生指标（AUROC、Jaccard、相关系数）。单细胞组学同时按逐步与整条 pipeline 两种方式评分。
- **既有步骤级也有终局评分**，对代码输出做基于执行的对照（ground-truth / oracle）；药物发现分数为三次独立评估的均值，并给出逐任务标准误。
- **报告（18 个 agent，含 GPT-5.2、Gemini 3 Pro、Claude Sonnet 4.6 及专用 agent Biomni / STELLA / ToolUniverse）：** 如 hERG 预测 68.1 AUROC、差异表达检测 29.4 F1、空间可变基因检测 47.6 Jaccard、EHR FHIR 查询最高 F1 ≈ 0.91（STELLA）。agent 在结构化数据分析上强（读取 / 连接表格、计算描述符、运行标准 pipeline），但在优化（仅约 1–25% 能解多目标分子设计，且无一会预算 oracle 调用）、发现（许多在 OOD 任务上无法产出可运行代码）与有效性（倾向假设不可行任务可行，而非拒绝）上弱。最难：EHR 用药管理（所有 agent F1 < 0.32）。

## Typical Duration

未说明：论文未给出单任务的 wall-clock、步数或 token 预算。唯一类似预算的约束是领域特定的——药物发现优化将分子 oracle 调用上限设为 100。

## Main Contribution

一个系统性、agent-agnostic 的 benchmark，用于衡量 AI agent 在跨尺度真实科学研究场景上的进展，采用逐步验证，并显式说明 agent 当前在何处成功与失败。

## Key Design Ideas

- 跨多个尺度的真实世界科学研究场景。
- 逐步验证而非仅终态结果打分。
- agent-agnostic、交互式的环境，支持多样 agent。
- 显式的失败模式分析（新颖洞见、自主探索、开放式问题）。

## Strengths

- 逐步验证提供比仅终态成功更细粒度的信号。
- agent-agnostic 设计支持跨多样 agent 实现的比较。
- 报告具体的强弱项而非单一分数。

## Limitations

- Repository note: 论文称“约 200 个任务”，但从未给出确切总数或逐领域任务表——仅有工作流内部的子任务计数。由于各领域打分尺度不同（二元标准、F1 与原生指标），跨领域聚合并无统一指标。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 在数据驱动科学任务上的能力，但对统一的 Python 程序输出打分，而非跨尺度的逐步验证。
- [AIRS-Bench](./airs-bench.md) — 同样面向研究科学任务，评估端到端研究生命周期。
