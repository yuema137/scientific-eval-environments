# MMCircuitEval (2025)

> [English](../../works/mmcircuiteval.md) | **简体中文**

## Overview

MMCircuitEval 是评测 LLM 的首个以电路为中心的多模态 benchmark：3,614 个精选问答对，横跨数字与模拟电路、覆盖关键 EDA 阶段——从通用知识与规格到前端与后端设计——取自教科书、题库、数据手册与真实文档。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.19525>
- **Code:** <https://github.com/cure-lab/MMCircuitEval>
- **Venue:** ICCAD 2025

## Summary

MMCircuitEval 沿设计流程组织电路评估：其 3,614 个问答对横跨数字与模拟电路、覆盖从通用知识与规格到前端与后端设计的 EDA 阶段，取自教科书、技术题库、数据手册与真实文档。问题带图像输入，形式包括选择题、填空题与开放题，按设计阶段、电路类型、所测能力（知识、理解、推理、计算）与难度分类。评测揭示当前模型间存在显著性能差距，尤其在后端设计与复杂计算上。

## Tasks

横跨数字与模拟电路及 EDA 阶段的 3,614 个多模态问答对；选择题、填空题、开放题形式的静态多模态问答。

## Domains

电气工程——横跨 EDA 阶段的数字与模拟电路知识与设计，含多模态（图像 + 文本）输入。

## Evaluation

- 按设计阶段、电路类型、所测能力（知识/理解/推理/计算）与难度分类的准确率。
- **报告。** 现有 LLM 间存在显著性能差距，尤其在后端设计与复杂计算上。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

首个沿 EDA 设计流程结构化的多模态电路 benchmark——定位模型能力在何处下滑（后端设计、复杂计算），而非只报一个总分。

## Key Design Ideas

- 按 EDA 阶段组织，把能力映射到真实设计管线上。
- 能力分类法（知识/理解/推理/计算）把失败类型分开。
- 混合题型与难度分级给出分级、可诊断的图景。

## Strengths

- 发表信息经核实（ICCAD 2025），公开发布，兼含数字与模拟。
- 阶段级与能力级拆分使结果对电路 LLM 构建者可落地。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、Comments 与官方仓库编写（2026 年 8 月）；参评模型数量摘要未载明。

## Related Works

- [EEE-Bench](./eee-bench.md) — 同样是多模态 EE 评估，横跨 10 个子领域而非 EDA 阶段。
- [AnalogCoder](./analogcoder.md) — 同样聚焦模拟电路，为 agent 化设计任务而非问答。
- [CVDP](./cvdp.md) — 同样是跨流程的电路设计评估，在 RTL 而非多模态问答。
