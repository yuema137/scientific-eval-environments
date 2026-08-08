# QCBench (2025)

> [English](../../works/qcbench.md) | **简体中文**

## Overview

QCBench 评估 LLM 的领域定量化学能力：350 个计算题覆盖 7 个化学子领域、分三档难度，题目结构上防住启发式捷径，必须做显式的分步数值推理。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.01670>
- **Code:** <https://github.com/jiaqingxie/QCBench>
- **Venue:** arXiv preprint (cs.AI), 2025（Comments 载明正在 Journal of Chemical Information and Modeling 修回）

## Summary

QCBench 瞄准语言流畅与科学计算之间的落差：350 个定量问题横跨分析化学、生物/有机化学、普通化学、无机化学、物理化学、高分子化学与量子化学，按易、中、难分档。题目的构造让模式匹配无从下手，必须真正完成数值计算。对 24 个 LLM 的评测显示，随任务复杂度上升，性能一致地下降。

## Tasks

350 个计算化学问题，覆盖 7 个子领域（分析、生物/有机、普通、无机、物理、高分子、量子化学）、三档难度；静态分步计算，不使用工具。

## Domains

化学——覆盖七个具名子领域的定量与计算化学。

## Evaluation

- 分步数值计算的分档准确率，支持按难度层级对计算短板做细粒度诊断。
- **报告。** 24 个参评 LLM 随任务复杂度上升表现一致下降。

## Typical Duration

单轮计算题；无交互式设定。

## Main Contribution

把「数值化学计算」剥离为独立测量的能力：抗捷径的题目构造，加上子领域 × 难度的网格，定位出计算在哪里失效。

## Key Design Ideas

- 题目结构保证不做计算就得不到答案。
- 七个子领域把「不懂化学」与「不会计算」两类失败分开。
- 难度分档把一个 benchmark 变成一条性能衰减曲线。

## Strengths

- 覆盖了结构类、问答类 benchmark 都绕开的定量化学广度。
- 24 个模型的评测规模，使「随难度衰减」这一结论获得了同类工作少见的覆盖面。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；此外的细节有待全文校验。arXiv Comments 中的 JCIM 状态是「修回」而非录用。

## Related Works

- [ChemIQ](./chemiq.md) — 同样是不借助工具、程序化判分的化学评估，考结构而非计算。
- [HARDMath](./hardmath.md) — 同样是防捷径设计的多步应用定量问题。
- [CMPhysBench](./cmphysbench.md) — 同样是研究生水平的物理科学计算题，带部分得分机制。
