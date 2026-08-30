# PHYSICS (2025)

> [English](../../works/physics-benchmark.md) | **简体中文**

> **首次公开：** 2025-03-26 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2503.21821)

## Overview

PHYSICS 是大学水平物理解题的综合 benchmark：1,297 道专家标注的问题，覆盖六大核心领域——经典力学、量子力学、热力学与统计力学、电磁学、原子物理与光学——并配有稳健的自动评估系统。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.21821>
- **Venue:** Findings of ACL 2025

## Summary

PHYSICS 的每道题都需要高等物理知识与数学推理，其自动评估系统为答案提供精确可靠的校验。对领先基础模型的评估揭示了明显的局限——受评中最先进的模型 o3-mini 也只达到 59.9% 的准确率。论文在分数之外配有全面的错误分析、多种提示策略的探索，以及基于 RAG 的知识增强，以指出改进应从何处入手。

## Tasks

1,297 道专家标注的大学水平问题，覆盖物理六大核心领域；静态解题。

## Domains

大学水平物理：经典力学、量子力学、热力学与统计力学、电磁学、原子物理与光学。

## Evaluation

- 稳健的自动评估系统，提供精确可靠的答案校验。
- **报告。** 受评中最先进的模型 o3-mini 仅达 59.9% 准确率。

## Typical Duration

单题解题；非交互式 agent 设定。

## Main Contribution

覆盖大学课程广度、配可靠自动校验的物理评估，并通过错误分析、提示变体与 RAG 增强诊断出物理解题究竟败在哪里。

## Key Design Ideas

- 六大核心领域使覆盖面代表完整物理课程，而非单一子领域。
- 自动校验是专门工程化的可靠系统，而非交给通用 judge。
- 失败分析与知识增强是贡献的一部分，而非事后补充。

## Strengths

- 覆盖本科核心课程、上千道题规模的专家标注。
- 前沿推理模型不足 60% 的上限记录了明确的提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [UGPhysics](./ugphysics.md) — 同样是本科广度的物理评估并配自动判分流水线，双语且规模更大。
- [PhysGym](./physgym.md) — 同样是物理评估，但走向交互式发现而非静态解题。
- [CMPhysBench](./cmphysbench.md) — 同样锚定课程的物理问题，为单一子领域的研究生水平并带部分得分。
