# PRL-Bench (2026)

> [English](../../works/prl-bench.md) | **简体中文**

## Overview

PRL-Bench（Physics Research by LLMs）是前沿物理研究能力的 benchmark，构建自 2025 年 8 月以来 Physical Review Letters 最新刊期的 100 篇精选论文并经领域专家验证，任务特征是面向探索的问题构造、长 horizon 工作流与客观可验证性。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.15411>
- **Dataset:** <https://huggingface.co/datasets/AdrianMiao/PRL_Bench>
- **Venue:** arXiv preprint (cs.LG, cs.AI, physics.data-an), 2026

## Summary

PRL-Bench 从最新的 PRL 论文中派生长 horizon、自主探索式的研究任务，覆盖五个理论与计算密集的子领域：天体物理、凝聚态物理、高能物理、量子信息与统计物理。只用 2025 年 8 月之后的论文使任务落在多数模型的训练截止之外。六个前沿 LLM 受评；表现仍然有限，最高总分不到 50（0–100 制）。

## Tasks

100 个研究任务，取材于 2025 年 8 月后的 Physical Review Letters 论文并经领域专家验证，覆盖五个子领域；任务强调面向探索的构造与长 horizon 工作流。

## Domains

前沿物理研究，横跨天体物理、凝聚态物理、高能物理、量子信息与统计物理。

## Evaluation

- 任务结果客观可验证并经专家验证；总体表现以 0–100 制分数报告。
- **报告。** 六个前沿 LLM 受评；最高总分不到 50。

## Typical Duration

每任务为长 horizon 研究工作流；预算为 TODO(reference)。

## Main Contribution

把一份旗舰物理期刊的最新进展变成可持续刷新的 benchmark，用「新近性」本身充当防污染机制。

## Key Design Ideas

- 只取模型训练截止之后的 PRL 刊期，任务在构建时即不可被记忆。
- 面向探索的任务构造瞄准研究行为，而非考试作答。
- 专家验证加客观可验证性，让研究级内容仍能机械判分。

## Strengths

- 基于新近性的防污染机制可随每期期刊持续刷新。
- 覆盖五个理论与计算密集的物理子领域。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- Repository note: PRL-Bench 与 [PRBench](./prbench.md) 是不同工作——团队不同、构造不同（100 个 PRL 派生任务 vs. 30 个专家整理的复现任务）；两者名称高度相近，极易混淆。

## Related Works

- [PRBench](./prbench.md) — 同样从物理论文派生评估；是对 30 篇专家整理论文的端到端复现，而非 100 个 PRL 派生研究任务。
- [CritPt](./critpt.md) — 同样是前沿研究级物理评估，用未发表、防猜测的挑战题。
- [ResearchClawBench](./researchclawbench.md) — 同样把任务锚定在模型接触不到的新近论文上，采用隐藏论文设计。
