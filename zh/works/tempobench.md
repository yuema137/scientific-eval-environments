# TempoBench (2025)

> [English](../../works/tempobench.md) | **简体中文**

## Overview

一个可形式化验证的时序 benchmark，隔离出对执行轨迹的*反事实因果归因*，检验 LLM 能否识别哪些输入是某个观测输出的必要条件，而不只是把系统向前模拟一遍。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A —— 针对合成 Mealy 机迹的抽象反事实因果归因推理诊断；是一项推理能力探针，而非科学/研究活动。

## Links

- **Paper:** https://arxiv.org/abs/2510.27544
- **Venue:** arXiv preprint（2025；cs.AI, cs.FL）

## Summary

TempoBench 由合成的确定性 Mealy 机构建，给出一个无限可扩展的、基于轨迹的因果推理问题语料，其复杂度可控、因果标签可证明正确。它分离两种能力：对执行迹的前向*模拟*，以及识别某个观测输出的*最小必要原因*。作者报告：前沿模型能准确地把系统向前模拟，但被问及哪些输入是某个观测输出的必要条件时表现骤降——他们把这一差距命名为 SIM/MIN gap——常把「可能的输入」混同为「必要的原因」。论文还报告，在 TempoBench 数据上微调开源模型可在外部因果 benchmark 上带来有针对性的增益，同时保持通用、数学与代码性能。

## Tasks

问题由合成的确定性 **Mealy 机**生成，得到一个无限可扩展、复杂度可控、因果标签可证明正确的语料。该 benchmark 在一条执行轨迹上定义两类任务：

- **前向模拟（SIM）** —— 给定一台机器与一个输入序列，产出执行迹（逐步：读入的输入、产生的输出、结果状态）。
- **最小必要原因（MIN）** —— 识别对某个给定观测输出而言必要的最小输入条件集合，这需要对备选输入做反事实推理。

确切的语料规模、按难度的划分与复杂度参数（状态数、迹长度）：`TODO(reference)`。

## Domains

N/A —— 该 benchmark 由抽象的确定性 Mealy 机构建，用作合成因果推理问题；它不评估某个科学或工程领域。作者以下游因果推断任务（如调试、根因分析与任务规划）作为动机。

## Evaluation

对照由底层 Mealy 机计算出的、可证明正确的标签做确定性、可形式化验证的评分：模拟迹逐步检查，最小必要原因答案对照由反事实归因导出的因果集合检查（对候选输入条件取反，并检验在机器动力学下输出是否改变）。报告的头条结果：前沿模型在前向模拟上达到 **96% 的逐步准确率**，而被问及哪些输入是某个观测输出的必要条件时跌至 **32%**——即 **SIM/MIN gap**。模型列表与按模型细分：`TODO(reference)`。

## Typical Duration

`TODO(reference)` —— 每问题的轨迹长度与 token 预算未从一手来源核实。

## Main Contribution

作为首个隔离出对执行轨迹之反事实因果归因的可形式化验证时序 benchmark 提出，并用它表明：当被要求做因果推理时，LLM 会成体系地退回到暴力的、基于模拟的推理——这由 SIM/MIN gap 量化——从而确立识别最小必要原因是一种与前向模拟不同的能力。

## Key Design Ideas

- 以**合成确定性 Mealy 机**作为问题生成器，给出无限可扩展、复杂度可控的语料。
- **可证明正确的因果标签**直接由机器计算，使因果归因对照真值而非某个 judge 检查。
- **SIM 与 MIN 分离** —— 前向迹模拟与最小必要原因识别作为不同任务评估，隔离出反事实归因。
- **SIM/MIN gap 作为诊断**：从前向模拟准确率到最小原因准确率的下降，暴露出对模拟而非因果理解的依赖。
- **经微调迁移** —— 在 TempoBench 数据上训练据报告能在外部因果 benchmark 上改进开源模型，同时保持通用、数学与代码性能。

## Strengths

- 真值因果标签由形式化模型计算，避免依赖人类或 LLM judge（据论文）。
- 该生成式构造被描述为无限可扩展、复杂度可控，因而难度可调、语料可扩（据论文）。
- 干净地分离前向模拟与反事实归因，隔离出一个具体的推理失败模式（据论文）。

## Limitations

- 报告的最小必要原因准确率即便对前沿模型也很低（约 32%），表明反事实因果归因在很大程度上仍未解决（据论文）。
- Repository note: 问题是抽象的 Mealy 机轨迹；与真实世界调试、根因分析与任务规划的联系是作者陈述的动机，而非一个被评估的设定。
- Repository note: 若干结构性数量（语料规模、受评模型列表、按模型与按难度的数字）在本轮无法从一手来源核实，标记为 `TODO(reference)`。

## Related Works

- [Long-Horizon Agent Trajectory Attribution](./long-horizon-agent-trajectory-attribution.md) —— 同样把观测结果归因于轨迹中负有责任的成分，但作用于 LLM-agent 轨迹而非形式化 Mealy 机执行迹。
- [ProcessBench](./processbench.md) —— 另一个「对推理做归因」的 benchmark，定位静态解答中最早出错的步骤，而非某个输出的最小必要原因。
