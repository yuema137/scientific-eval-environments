# PhysGym (2025)

> [English](../../works/physgym.md) | **简体中文**

> **首次公开：** 2025-07-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2507.15550)

## Overview

PhysGym 是面向 LLM agent 交互式物理发现的 benchmark 套件与模拟平台：agent 主动探查模拟环境、在约束下逐步采集数据、并就底层物理定律提出假设——其特色是对提供给 agent 的先验知识做精细控制。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.15550>
- **Code:** <https://github.com/principia-ai/PhysGym>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks（据官方仓库）

## Summary

PhysGym 的独特维度是先验知识控制：同一个发现问题可以在四个先验层级（据官方仓库为 L1–L4）下布置，从而把「agent 发现了什么」与「agent 被告知了什么」分开。套件含 97 个精选物理问题（据官方仓库，取自 PHYBench），以带有限实验预算的交互模拟形式运行，并提供评估假设准确性与模型保真度的标准化协议与指标。

## Tasks

97 个精选物理问题（官方仓库），以交互模拟回合布置：探查环境、在有限实验预算（据仓库为 100 次实验）下逐步采集数据、提交关于支配物理定律的假设，并在四个受控先验层级下进行。

## Domains

基于物理定律交互模拟的物理发现；问题取自 PHYBench 问题集。

## Evaluation

- 评估假设准确性与模型保真度的标准化协议与指标。
- **报告（官方仓库）。** 先验越少表现越差——例如 o4-mini 从 L1 的 62.89% 跌至 L4 的 31%。

## Typical Duration

受有限实验预算约束的逐步交互回合（据官方仓库为 100 次实验）。

## Main Contribution

把先验知识变成物理发现评估中可实验控制的变量，使「发现能力」能与「复述已给上下文」分开测量。

## Key Design Ideas

- 四个先验层级把「agent 被告知了多少」变成一条 benchmark 轴。
- 约束下的逐步数据采集使设定保持真正的交互性，而非一次性作答。
- 复用经过检验的 PHYBench 问题，让模拟环境锚定在已验证的问题集上。

## Strengths

- L1→L4 的性能衰减曲线量化了「表观能力中有多少由所给先验承载」。
- 平台化设计支持跨 agent、跨知识条件的受控比较。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [MaD Physics](./mad-physics.md) — 同样是预算约束下的交互式物理发现，观测按保真度定价。
- [DiscoverPhysics](./discoverphysics.md) — 同样是模拟世界中的 agentic 定律发现，物理被刻意设为非标准。
- [PHYBench](./phybench.md) — PhysGym 交互环境所依托的问题来源。
