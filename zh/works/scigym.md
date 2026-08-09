# SciGym (2025)

> [English](../../works/scigym.md) | **简体中文**

## Overview

SciGym 用一个系统生物学干实验（dry lab）来测量语言模型的科学能力：agent 在以 SBML（Systems Biology Markup Language）编码的生物系统上迭代地设计实验、分析模拟数据，并对照隐藏的真值系统提交机制假设。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.02083>
- **Code:** <https://github.com/h4duan/SciGym>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

SciGym 直面开放式实验评估的成本问题：湿实验太贵，无法以 benchmark 规模运行，于是用干实验代替——由隐藏的 SBML 编码生物系统生成模拟数据。agent 按序选择实验、观察模拟结果、以 SBML 格式提交假设，配错误检查与可配置的重提交轮次（据官方仓库）。六个前沿 LLM 在 137 个小型系统上受评，共发布 350 个系统；所有模型的表现都随系统复杂度上升而显著下降。

## Tasks

在隐藏 SBML 生物系统上的迭代「实验设计 + 分析」回合：137 个小型系统受评，共发布 350 个（据官方仓库为 137 小 + 213 大）。

## Domains

系统生物学：以 SBML 编码的生物系统机制模型。

## Evaluation

- agent 复原的模型与隐藏的真值 SBML 系统比较；详细指标定义为 TODO(reference)。
- **报告。** 六个前沿 LLM 受评；所有模型表现随系统复杂度上升显著下降。

## Typical Duration

有迭代次数上限的按序实验设计回合（据官方仓库）。

## Main Contribution

为开放式实验科学提供一个负担得起的替身：模拟生物学保留了「迭代-实验-分析」循环，而湿实验的成本让这个循环无法成为 benchmark。

## Key Design Ideas

- 隐藏的 SBML 系统给实验设计一个形式化、可检验的目标。
- 按序交互让「选择做什么实验」——而不只是分析——成为受评能力。
- 从小到大的复杂度梯度把难度阶梯内建于语料。

## Strengths

- 开放式发现配上机器可检验的真值。
- 随复杂度的下滑定位了迭代式科学推理从何处开始失效。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。流传的会议录用说法无法从这些来源证实。

## Related Works

- [MaD Physics](./mad-physics.md) — 同样是模拟系统上预算意识的交互实验，在物理领域。
- [DiscoverPhysics](./discoverphysics.md) — 同样对照隐藏机制做迭代实验设计，配「预测 + 解释」成对评分。
- [Aviary](./aviary.md) — 同样是生物学主题的交互环境（克隆、蛋白质工程），带终末奖励。
