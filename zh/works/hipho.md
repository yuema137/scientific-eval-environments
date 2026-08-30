# HiPhO (2025)

> [English](../../works/hipho.md) | **简体中文**

> **首次公开：** 2025-09-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2509.07894)

## Overview

HiPhO 是高中物理奥赛 benchmark，汇编 2024–2025 年最新的 13 套国际与地区奥赛真题，用官方评分方案在答案与步骤两级判分，并按官方奖牌线把模型分数映射为金、银、铜牌，与人类选手直接比较。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.07894>
- **Code:** <https://github.com/SciYu/HiPhO>
- **Leaderboard:** <https://phyarena.github.io/>
- **Venue:** ICML 2026

## Summary

HiPhO 的独特承诺是与人对齐的评估：它不自创评分方案，而是采用赛事的官方评分方案，在答案级与步骤级做细粒度判分，与人类阅卷完全对齐，再按官方阈值授予奖牌。真题取最新的 2024–2025 赛季，污染压力低，且混合纯文本与图示两种模态。在 30 个最先进 (M)LLM 上：开源 MLLM 大多停留在铜牌线及以下；开源 LLM 进步明显、多次摘金；闭源推理 MLLM 拿到 6 到 12 枚金牌——但大多数模型距满分仍有显著差距。

## Tasks

2024–2025 年最新的 13 套高中物理奥赛真题（国际与地区赛事），混合纯文本与图示题；静态答题。

## Domains

高中奥赛物理；子领域构成随源试卷而定，未单独列出。

## Evaluation

- 官方评分方案在答案级与步骤级应用；按官方金/银/铜阈值授牌。
- **报告。** 30 个 (M)LLM 中：开源 MLLM 大多在铜牌及以下，开源 LLM 多次摘金，闭源推理 MLLM 获 6–12 金；大多数模型距满分仍远。

## Typical Duration

试卷式答题；非交互式 agent 设定。

## Main Contribution

完全按人类奥赛选手的方式给模型判分——官方评分标准、官方奖牌线——让人机比较可以直接成立，而不必事后拼凑对照。

## Key Design Ideas

- 官方评分方案让评分设计不经 benchmark 作者之手。
- 奖牌阈值把分数转换成物理学界早已理解的刻度。
- 只用最新赛季真题，防污染随每个竞赛周期自动更新。

## Strengths

- 与人类阅卷对齐的步骤级判分，而非二元的对错检查。
- 奖牌框架用人类校准的语言传达模型能力。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [PHYBench](./phybench.md) — 同样是奥赛难度物理并配区分度更高的指标，但用原创题而非官方真题。
- [SeePhys](./seephys.md) — 同样是混合模态的物理评估，跨度从初中到博士。
- [UGPhysics](./ugphysics.md) — 同样以人类考试为锚的物理评估，在本科广度上。
