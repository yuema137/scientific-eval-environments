# Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering (2025)

> [English](../../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) | **简体中文**

> **首次公开：** 2025-10-24 · **来源：** [官方出版记录](https://doi.org/10.3390/data10110169)

## Overview

一份已正式发表的数据集与验证方案：GPT-4o 对钢筋混凝土框架的结构分析问题作答两遍——一遍是纯语言模型裸答，一遍是作为工具型 agent 通过 Model Context Protocol (MCP) 服务器驱动 OpenSeesPy——两组答案都以相对误差对照人工搭建的 ETABS 参考模型计分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://doi.org/10.3390/data10110169>
- **Code:** <https://doi.org/10.17632/gh9sbjzz5z.2>（Mendeley Data，`LLMS_MCP`，CC BY 4.0）
- **Venue:** *Data* (MDPI), Vol. 10, Issue 11, Article 169，2025 年 10 月 24 日

## Summary

论文公开了一次结构分析对照实验的完整记录：四榀钢筋混凝土建筑框架各自由 GPT-4o 在两种配置下分析——无辅助裸答，以及作为工具型 agent 通过 Model Context Protocol 服务器驱动 OpenSeesPy——同时还有一份人工编写的 OpenSees 模型，以及一份提供 ground truth 的商业 ETABS 模型。全部提示词、交互过程、输出与误差指标均以开放许可发布。作者陈述的目的，是把概率性的语言生成与确定性的数值计算分开，并记录在涉及安全的工作流里每种配置究竟能被信任到什么程度。

## Tasks

四个算例（A–D），每个都是一榀三维钢筋混凝土建筑框架，各由一条按五段式「CIDI」模板（Context、Instructions、Details、Tasks、Intent）写成的结构化提示词定义。算例 A 为 2 层对称框架，两个方向跨度均为 4.0 m；算例 B 为 3 层非对称框架，跨度可变；算例 C 为 5 层对称框架，跨度 4.0 m；算例 D 为 5 层非对称框架，跨度可变。这些框架按厄瓜多尔 NEC-15 与美国 ASCE 7-22 规范设计。每个算例都在四个计算组下各分析一遍——GPT 单独作答、GPT+MCP、人工编写的 OpenSees，以及 ETABS——合计 16 次分析。未通过校验的输出会记录在案，并从精选数据集中剔除。

## Domains

土木与结构工程。受评目标是钢筋混凝土建筑框架的静力与地震响应——层间位移角、最大位移、基底剪力与基本周期——并对照设计规范要求核算，属结构工程的分析任务，而非一般意义上的工具操作。不设共同领域：语言模型与 MCP 这套机制只是手段，并非受评对象。

## Evaluation

每次分析都报告 X、Y 两个方向的层间位移角（无量纲比值）、最大位移（m）、基底剪力（kN）与结构周期（s）。正确性以对照 ETABS 参考模型的相对误差计分，即 `|X_model − X_ETABS| / X_ETABS × 100%`，逐项施加于每个报告量。报告结果：GPT 裸答配置的相对误差约在 230–270%，离散度很大；GPT+MCP 与人工 OpenSees 则都保持在 1.427% 以下。

## Typical Duration

每次 GPT+MCP 分析端到端耗时 6–12 秒；作者报告人工走 ETABS 路线约需 12–15 分钟。

## Main Contribution

作者贡献了一份精选、以开放许可发布的数据集，完整记录了从自然语言到求解器的全部交互过程，并附上判断其优劣所需的误差指标；他们把这套做法定位为一种可复现的方法论——通过把概率性语言生成与确定性数值计算分开，将生成式 AI 接入涉及安全的结构工程工作流。

## Key Design Ideas

- 以 Model Context Protocol 作桥梁：一个 FastAPI 服务器把模型的自然语言输出转成结构化的 JSON 模式，再驱动 OpenSeesPy 3.8.x（OpenSees 3.7.1）。
- 刻意保留纯 LLM 这一对照条件，使数据集测得的是「把模型接到求解器上」带来的效果，而不只是接好之后那条管线的精度。
- ground truth 来自独立的商业软件（ETABS 20.3.0），而不是 agent 所驱动的同一个求解器。
- 四个算例共用一套固定的提示词模板，算例之间的差异因此来自结构本身，而非提示词工程。
- 四榀框架跨越两种层数、兼有对称与非对称的平面布置，并按两套不同的抗震规范设计。

## Strengths

- ground truth 来自独立的商业软件包（ETABS），而非 agent 驱动的同一求解器，参照系因此不构成循环论证。
- 纯 LLM 对照条件得以保留而非弃用，正因如此，约 230–270% 与低于 1.427% 之间的误差落差才能解读为求解器接地带来的效果。
- 公开发布的材料采用开放许可，含提示词、交互过程、输出与误差指标，这套比较可以重算，而不必只凭信任。
- 精度之外同时报告运行时间（6–12 秒对人工路线的 12–15 分钟），把成本作为明确的第二个维度。
- 四个算例共用固定的提示词模板，把结构难度与提示词工程分离开。

## Limitations

- 规模很小：四榀框架、四条提示词、共 16 次分析，且全部属于同一种结构类型（钢筋混凝土抗弯框架），所考察的结构行为范围因此有限。
- 只跑了一个语言模型（GPT-4o），就已发布的内容而言，数据集不支持跨模型比较。
- 只对最终结果计分；未定义任何轨迹级、中间步骤级或工具调用级的评分。
- 论文本身没有局限性或使用者注意事项一节。
- Repository note: 已发表的摘要称数据集包含「150+ prompts」，而正文说明四个算例各由一条 CIDI 式提示词定义、总计 16 次分析。本卡片以正文为准。
- Repository note: 这是一篇配套于另一项研究的数据描述论文，而非为公开排行榜式使用而设计的 benchmark 套件；把它当评测集复用是可行的，但并非作者陈述的定位。

## Related Works

- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — 同样把 LLM 生成的 OpenSeesPy 分析对照参考结构解答计分。
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — 同一套 OpenSeesPy 代码生成设定，落在 2D 框架上并做重复试验。
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — 同样在相同的结构问题上比较纯 LLM 与带求解器的 agent。
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — 3D 框架分析，对照商业软件（SAP2000）的 ground truth 计分。
