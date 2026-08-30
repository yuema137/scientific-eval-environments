# EEE-Bench (2024)

> [English](../../works/eee-bench.md) | **简体中文**

> **首次公开：** 2024-11-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2411.01492)

## Overview

EEE-Bench 是一个综合的多模态电气与电子工程 benchmark：2,860 个精选问题，横跨 10 个核心子领域（模拟电路、控制系统等），要求在专业指令之外读懂抽象电路、系统框图等复杂图像——17 个 LLM 与 LMM 的平均成绩仅 19.48%–46.78%。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.01492>
- **Venue:** CVPR 2025

## Summary

EEE-Bench 衡量多模态基础模型能否求解真实的电气工程问题——答案取决于读懂电路或系统框图，而不只是文本。其 2,860 个精选问题横跨 10 个核心 EE 子领域——模拟电路、控制系统等，每题把复杂图像（抽象电路、系统框图）与专业指令配对。对 17 个开源与闭源 LLM/LMM 的评测暴露出明显不足，平均成绩在 19.48% 到 46.78% 之间；论文指出一种「偷懒（laziness）」失败模式：模型依赖文本、忽视问题真正依赖的视觉上下文。

## Tasks

横跨 10 个子领域（模拟电路、控制系统、信号、数字等）的 2,860 个多模态 EE 问题；静态问题求解，需图文联合理解。

## Domains

电气工程——横跨 10 个 EE 子领域的宽多模态覆盖，以真实电路与系统框图影像为依据。

## Evaluation

- 17 个 LLM/LMM 上跨子领域的准确率，配细粒度分析与「偷懒」（文本压过视觉）发现。
- **报告。** 平均成绩在 19.48% 到 46.78% 之间，表明当前基础模型在 EE 上明显不足。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

按子领域覆盖最广的多模态 EE benchmark——以及「偷懒」诊断，表明模型系统性地未充分利用 EE 问题所依赖的电路与框图影像。

## Key Design Ideas

- 十子领域跨度使其能代表 EE，而非单一小众。
- 真实电路/框图影像迫使真正的视觉理解，而非读图注。
- 「偷懒」分析点名了一种具体、普遍的多模态失败模式。

## Strengths

- 发表信息经核实（CVPR 2025），模型覆盖广（17 个）、EE 范围宽。
- 19–47% 的区间给出多模态 EE 的清晰能力标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；CVPR 2025 经 Comments 确认。arXiv 页面无法核实官方代码/项目 URL。

## Related Works

- [MMCircuitEval](./mmcircuiteval.md) — 同样是多模态 EE/电路问答，按设计阶段与电路类型组织。
- [AnalogXpert](./analogxpert.md) — 同样覆盖模拟设计，为 agent 化综合任务而非问答。
- [MatSciBench](./matscibench.md) — 同样是多模态工程/科学推理 benchmark，在材料领域。
