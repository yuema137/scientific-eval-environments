# Gravity-Bench-v1 (2025)

> [English](../../works/gravity-bench.md) | **简体中文**

## Overview

Gravity-Bench-v1 是引力物理发现的 agentic benchmark：agent 观测一个模拟二体引力系统，在实验预算内规划采集哪些数据，再通过数据分析揭示被隐藏的物理——包括无法靠背诵教科书知识回答的、分布外的修改物理。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.18411>
- **Code:** <https://github.com/NolanKoblischke/GravityBench>
- **Dataset:** <https://huggingface.co/datasets/GravityBench/GravityBench>
- **Project:** <https://gravitybench.github.io/>
- **Venue:** ICML 2025

## Summary

每个任务模拟一个双星系统，以严格的引力动力学模拟为真值。agent 在预算内决定采集哪些观测（据官方项目页，每次运行至多 100 个数据点），再基于所得数据推断系统的物理性质。该 benchmark 允许开放的解空间，并以参考解将 AI 表现与人类专家水平对标。任务包含分布外的物理变体，因此取得成功靠的是发现，而不是记忆。

## Tasks

在模拟二体引力系统上的交互式「观测规划 + 数据分析」回合，含分布外修改物理变体；观测在固定实验预算内进行。具体任务数为 TODO(reference)。

## Domains

模拟双星系统的引力物理与动力学（带天体物理色彩，归于 astro-ph.IM）。

## Evaluation

- 答案对照由严格引力动力学模拟导出的参考解检验，并与人类专家水平对标。
- **报告（官方项目页）。** 最佳模型 o4-mini-high 在可用全部数据时达到 74%，在观测预算下降至 49%。

## Typical Duration

预算受限的交互回合；据官方项目页，每次运行至多 100 次观测。

## Main Contribution

把有预算的实验设计纳入物理发现 benchmark 的测量范围，并用分布外物理把「发现」与「背诵」区分开。

## Key Design Ideas

- 观测预算使数据采集成为需要规划、有代价的决策，而非免费输入。
- 分布外的修改物理从构造上封死了记忆式作答。
- 参考解让开放式答案能对标人类专家表现。

## Strengths

- 全量数据与预算受限之间的差距（最佳模型 74% vs. 49%）单独度量了「必须规划观测」的代价。
- 解空间开放，技术难度在本科高年级水平，仍能难住基线 agent。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [MaD Physics](./mad-physics.md) — 同样在单次试验预算下为观测定价，以发现被改动的物理定律。
- [NewtonBench](./newtonbench.md) — 同样在反事实偏移的物理下评估定律发现，以符号等价性判分。
- [DiscoverPhysics](./discoverphysics.md) — 同样让 agent 在物理偏离现实的模拟世界中做实验。
