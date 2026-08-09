# Materials Hypothesis Generation (2025)

> [English](../../works/materials-hypothesis.md) | **简体中文**

## Overview

本工作评测目标驱动、约束引导的 LLM agent 用于材料发现：给定研究目标与具体约束，agent 生成实现目标的假说，由一个可扩展的评估指标判分——该指标旨在模拟材料科学家会如何批判性地评判一个假说。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.13299>
- **Venue:** NAACL 2025

## Summary

论文题为「Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents」。这篇 NAACL 2025 工作把一个从近期期刊论文策划的数据集，与一个模拟材料科学家批判性评判的可扩展新指标配在一起。LLM agent 是目标驱动、约束引导的：在具体约束下为既定目标生成假说，指标则评判这些假说是否值得深入。它为一个真值本就开放的任务提供了评估路径。

## Tasks

在明确目标与约束下的假说生成，基于从近期期刊论文策划的数据集；由一个可扩展、模拟专家的指标判分。数据集规模为 TODO(reference)——摘要未载明。

## Domains

材料科学——面向材料发现与设计的假说生成，以近期已发表研究的目标与约束为依据。

## Evaluation

- 一个模拟材料科学家批判性评估的可扩展指标。
- **报告。** 摘要无数值头条；贡献是策划的数据集加评估指标。

## Typical Duration

每个目标/约束规格一段假说生成回合。

## Main Contribution

为 LLM 材料假说生成提供评估路径——一个策划的数据集与一个模拟专家的指标，让开放式的发现任务变得可测量。

## Key Design Ideas

- 明确的目标与约束使假说可对照规格检验。
- 可扩展指标模拟专家批判，而非要求精确参考答案。
- 从近期论文策划，使目标真实而当下。

## Strengths

- 发表信息经核实（NAACL 2025），瞄准发现中最难判分的阶段。
- 模拟专家的指标针对阻碍假说 benchmark 的开放性问题。

## Limitations

- Repository note: 该论文在数据集与指标之外还突出其目标驱动/约束引导的 agent 方法；本卡片以数据集与评估贡献为中心。数据集规模摘要未载明，仍为 TODO(reference)；arXiv 页面无法核实代码/数据集 URL。

## Related Works

- [AlchemyBench](./alchemybench.md) — 同样是 LLM 驱动的材料发现，处于合成规划而非假说阶段。
- [MOOSE-Chem](./moose-chem.md) — 同样是 LLM 科学假说重发现，在化学领域。
- [ResearchClawBench](./researchclawbench.md) — 同样是端到端的研究发现重构，其领域涵盖材料。
