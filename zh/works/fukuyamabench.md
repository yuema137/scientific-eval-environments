# FukuyamaBench (2026)

> [English](../../works/fukuyamabench.md) | **简体中文**

## Overview

FukuyamaBench 是层级化反应机理推理的高难度 benchmark，题目取自 Fukuyama 的《Advanced Organic Reaction Mechanism》一书；它由一篇以训练为主的机理推理论文发布，该文微调的 Qwen3-30B-A3B 在 Set A 上达到 8.3% 的完整路径精确匹配，超过专用模型 FlowER 的 5.1%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.12771>
- **Venue:** arXiv preprint, 2026

## Summary

论文「Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models」先构建了大规模的反应机理推理训练数据集，再建立 FukuyamaBench 来严格评估层级化机理推理——推导完整的基元反应路径，而不只是预测产物。头条评估结果是：机理感知的微调让 Qwen3-30B-A3B 在 FukuyamaBench Set A 上达到 8.3% 的路径精确匹配，超过专用的 FlowER 模型（5.1%）——这些数字主要说明了这个 benchmark 有多难。

## Tasks

对有机反应逐步推导基元反应机理路径，题源为研究生水平的机理教科书；静态推理任务。各 Set 的规模为 TODO(reference)——摘要未载明。

## Domains

化学——有机反应机理：产物预测与逆合成底下的基元步骤路径推理。

## Evaluation

- 对推导出的机理做完整路径精确匹配。
- **报告。** 微调后的 Qwen3-30B-A3B：Set A 路径精确匹配 8.3%；专用 FlowER 模型：5.1%。

## Typical Duration

单回合的多步机理推导。

## Main Contribution

为「机理层面」（而非产物层面）的化学推理提供了评估靶标，其难度之高，使目前最好的系统十条路径也解不出一条。

## Key Design Ideas

- 取材高阶教科书，把难度锚定在专家训练材料上，而非抓取的反应数据。
- 完整路径精确匹配要求给出全部机理，堵死了「猜产物」的捷径。
- 层级结构把单步能力与全路径能力区分开。

## Strengths

- 探测产物预测类 benchmark 绕开的那一层化学理解——机理。
- 个位数的 SOTA 分数留下清晰可测的提升空间。

## Limitations

- Repository note: 该论文的头号贡献是训练数据集与机理感知微调；FukuyamaBench 是其评估侧的次要贡献，本卡片只覆盖 benchmark 本身。论文标题并非「FukuyamaBench」。
- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；论文 arXiv 页面上无法核实任何代码或数据集发布。

## Related Works

- [ChemCoTBench](./chemcotbench.md) — 同样是步骤结构化的反应推理，粒度在模块化分子操作层面。
- [ChemCensor / CREED](./chemcensor.md) — 同样重新思考反应类任务该怎么评，落在逆合成一侧。
- [QCBench](./qcbench.md) — 同样是防捷径、必须显式多步推演的化学问题。
