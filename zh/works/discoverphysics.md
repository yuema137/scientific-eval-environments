# DiscoverPhysics (2026)

> [English](../../works/discoverphysics.md) | **简体中文**

## Overview

DiscoverPhysics 是考察「跳出框架的科学思维」的 agentic benchmark：agent 要发现一个物理刻意偏离现实的模拟世界的运动定律——屏蔽引力、隐藏粒子种类、修改的力定律——方式是提出多轮实验并分析原始轨迹数据。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.26087>
- **Code:** <https://github.com/SampsonML/DiscoverPhysics>
- **Venue:** arXiv preprint (stat.ML, cs.LG), 2026

## Summary

22 个世界均由 N 体模拟器按需生成，物理刻意非标准。agent 提出数轮实验、观察原始轨迹数据，最终同时提交对该世界物理的自然语言解释与所推断定律的 Python 实现。评分沿两条互补的轴进行：留出粒子上的轨迹 MSE，以及按专家撰写的评分标准由 LLM 评判的解释分（考察对世界的概念性理解）。在 11 个前沿模型上，最强 agent 也只通过一半的世界，且在必须揭示潜在结构的世界上持续失败；预测精度高并不保证解释质量高。

## Tasks

22 个反事实模拟世界（据官方仓库的世界类型，如修改引力、额外维度、类暗物质隐藏粒子），每个世界要求迭代提出实验、观察原始 N 体轨迹数据，并提交解释与定律的 Python 实现。

## Domains

经典力学与 N 体动力学，带天体物理色彩的反事实设定（修改引力、类暗物质粒子、宇宙膨胀类比）。

## Evaluation

- 留出粒子上的**轨迹 MSE**（预测保真度）。
- 按专家评分标准由 **LLM 评判的解释分**（概念性理解）。
- **报告。** 11 个前沿模型受评；最强 agent 只通过一半的世界，且在需要揭示潜在结构的世界上持续失败；开源模型显著落后于商业模型。

## Typical Duration

每个世界数轮实验；单世界预算为 TODO(reference)。

## Main Contribution

把「预测一个世界」与「理解一个世界」分开：轨迹保真度与按评分标准评判的解释分成对出现，暴露那些拟合了数据却没有揭示潜在物理的 agent。

## Key Design Ideas

- 刻意非标准的物理让背下来的定律不仅无用，而且误导。
- 同时要求自然语言解释与可执行 Python 代码，迫使「理解」用两种表征各陈述一遍。
- 世界由 N 体模拟器按需生成，评估天然抗污染。

## Strengths

- 直接测量科学发现中真正要紧的失败模式：预测得好、解释得错。
- 在潜在结构世界上的持续失败定位出一个具体的能力缺口。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [NewtonBench](./newtonbench.md) — 同样在模拟系统上做反事实定律发现，但以符号等价而非「预测 + 解释」成对判分。
- [Gravity-Bench-v1](./gravity-bench.md) — 同样是含分布外变体的引力物理发现，在观测预算之下。
- [MaD Physics](./mad-physics.md) — 同样通过预算受限的交互推断被改动的物理定律。
