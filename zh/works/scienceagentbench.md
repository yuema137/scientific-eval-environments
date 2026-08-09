# ScienceAgentBench (2024)

> [English](../../works/scienceagentbench.md) | **简体中文**

## Overview

ScienceAgentBench 是一个评估 language agent 在数据驱动科学发现工作流中单个任务的 benchmark。它从四个学科的 44 篇同行评审论文中提取 102 个任务，将每个任务的目标输出统一为一个自包含的 Python 程序，并对生成的程序、执行结果与成本进行评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.05080>
- **Venue:** ICLR 2025

## Summary

ScienceAgentBench 主张：在宣称端到端自动化科学发现之前，应在科学工作流中的单个任务上对 agent 进行严格评估。为确保科学真实性与现实相关性，它从四个学科的 44 篇同行评审论文中提取 102 个任务，并邀请九位领域专家进行验证。每个任务的目标输出被统一为一个自包含的 Python 程序文件，并用一组指标考察生成的程序、执行结果与成本。每个任务经过标注者与领域专家的多轮人工验证，benchmark 还提出两种策略以缓解数据污染问题。

## Tasks

从四个学科的 44 篇同行评审论文中精选 102 个任务——生物信息学、计算化学、地理信息科学、心理学与认知神经科学。各学科任务数（来自作者发布的数据集）：生物信息学 27、计算化学 20、地理信息科学 27、心理学与认知科学 28。每个任务的目标输出统一为一个自包含的 Python 程序文件。

## Domains

数据驱动的科学发现，跨四个学科：生物信息学、计算化学、地理信息科学、心理学与认知神经科学。

## Evaluation

对每个生成的独立程序用四个指标打分：

- **Valid Execution Rate (VER)** — 程序能否无错运行并以正确文件名保存输出（二元）。
- **Success Rate (SR)** — 输出是否满足任务特定的成功标准（如「测试集 ROC-AUC ≥ 0.77」、预测与答案匹配、可视化质量），以每个任务手写的可执行检查器实现；SR 以执行为前提（程序报错或保存错误则记 0）。图像输出由 GPT-4o 对照 gold 评判，取 3 次采样均值。
- **CodeBERTScore (CBS)** — 基于上下文 token embedding 的 F1，衡量与标注参考程序的相似度（当 SR = 1 时置为 1.0）。
- **API Cost** — 完成一个任务的平均花费（USD）。

另有一套专家 **rubric**（五个阶段：Data Loading、Data Processing、Modeling/Visualization、Output Formatting、Output Saving；归一化到 0–100）用于人工评估，作为对偏严格的结果指标的补充，但不属于自动 SR。任务另经多轮人工验证，并配两种策略缓解数据污染。

报告（每任务三次尝试）：最佳 agent（Claude-3.5-Sonnet + Self-Debug）独立求解 32.4%、含专家知识时 34.3%；o1-preview + Self-Debug 达 42.2%（API 成本为较便宜模型的 10 倍以上）。Self-Debug 比 OpenHands CodeAct 多解 10.8 个百分点（SR 21.6 → 32.4），成本却低 17 倍（每任务 $0.958 → $0.057）。

## Typical Duration

未以 wall-clock 报告；论文改报每任务 API 成本——如每任务 $0.017（Claude-3.5 direct prompting）至 $1.09（GPT-4o OpenHands CodeAct），o1-preview self-debug 为 $0.64–0.71。

## Main Contribution

一个经严格验证的数据驱动科学发现 benchmark：以真实论文中提取、专家验证的任务与统一的 Python 程序输出目标，评估 agent 在单个科学工作流任务上的能力，而非假定端到端自动化。

## Key Design Ideas

- 任务从真实同行评审论文中提取，并由领域专家验证以确保科学真实性。
- 统一的目标输出（自包含的 Python 程序）使异构科学任务可比较地打分。
- 四个自动指标（VER、SR（任务特定可执行标准）、CodeBERTScore、API 成本），并辅以五阶段专家 rubric 用于人工评估。
- 两种显式的数据污染缓解策略。
- 在五个开源与专有 LLM 上、三种 agent 框架下评估：direct prompting、OpenHands CodeAct 与 self-debug。

## Strengths

- 以出版物为基础、专家验证的任务，为科学发现评估提供生态效度。
- 统一的 Python 程序输出使得跨学科的、基于执行的可比较打分成为可能。
- 在报告准确率的同时报告成本，揭示推理时计算的权衡（o1-preview 以 >10 倍成本达到 42.2%）。
- 显式的数据污染缓解增强 benchmark 完整性。

## Limitations

- Repository note: 最佳 agent 求解率偏低（独立 32.4%，含专家知识 34.3%）表明该 benchmark 远未饱和——就 headroom 而言是优点，但超出通过/失败的单任务诊断信号并非其重点。
- Repository note: 范围是以 Python 程序表达的数据驱动发现；无法归约为程序产物的科学任务不在其范围内。

## Related Works

- [NatureBench](./naturebench.md) — 同样将科学任务锚定到同行评审论文，但以与已发表 SOTA 比较打分，而非执行统一的 Python 程序。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样采用基于执行的验证科学计算工作流，但用容器化 pytest 而非统一的 Python 程序输出。
- [AIRS-Bench](./airs-bench.md) — 同样面向研究科学任务，但评估端到端研究生命周期而非单个工作流任务。
