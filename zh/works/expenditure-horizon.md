# Expenditure Horizon (2026)

> [English](../../works/expenditure-horizon.md) | **简体中文**

> **首次公开：** 2026-07-21 · **来源：** [METR 研究报告](https://metr.org/blog/2026-07-21-expenditure-horizon/)

## Overview

Expenditure horizon 是 METR 提出的一个指标，衡量 agent 改进一个连续优化目标的能力。它不问 agent 有没有解出任务，而是把 agent 和人的进展放在同一条以美元计的坐标轴上：agent 的成本是 API token 加实验算力，人的成本是估算的工时乘以时薪。Expenditure horizon 就是这样一个预算点：花同样多的钱，agent 累积带来的改进恰好等于人类取得的改进；超过这个点，雇人更划算。报告用 NanoGPT speedrun 演示了这个指标。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Report:** [Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT](https://metr.org/blog/2026-07-21-expenditure-horizon/)，Tom Cunningham、Manish Shetty、Vincent Cheng、Nate Rush，METR，2026-07-21。
- **Task source:** NanoGPT speedrun，<https://github.com/KellerJordan/modded-nanogpt>
- **Related METR note:** <https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/>
- **Venue:** METR 研究报告（没有链接配套论文或代码发布）

## Summary

过去在开放式优化问题上评估 agent，通常只报告运行一段时间后的分数，但这说明不了同样的钱如果花在人身上，会不会走得更远。METR 构建了两条「投入回报」曲线。人类曲线来自 speedrun 的纪录历史：每条纪录所花的精力通过采访贡献者和 LLM judge 来估计，经过校准后按每小时 $150 折算成钱。Agent 曲线来自长时间的 agent 运行，agent 声称的每一次提升都要用重复运行重新验证。两条曲线的交点就是 expenditure horizon。在每次运行花费超过 $10K 之后，报告估计的 horizon 在 $0 到约 $3K 之间；这个结果对「人类每提升 1% 要花多少钱」这一假设很敏感。

## Tasks

只有一个优化任务：NanoGPT speedrun（modded-nanogpt），目标是在 8 块 H100 GPU 上，用尽量短的墙钟训练时间在 FineWeb 上把验证 loss 降到 3.28。纪录历史从 2024 年 5 月到 2026 年 4 月共 82 条。Agent 的运行从第 78 号纪录开始（2026 年 3 月，85.56 s）。Agent 只能修改 `solution.py`；负责计时的 `runner.py` 和根据返回的 logits 计算交叉熵的 `validate.py` 归 root 所有，受到保护。

Repository note: 报告称这个方法适用于有约束的优化问题，也可以用来概括 RE-Bench、MLE-bench 等现有的 AI R&D benchmark，但实际只测了 NanoGPT speedrun。

## Domains

AI 与机器学习研究：语言模型训练速度优化。

## Evaluation

- **定义：** Expenditure horizon 是「在相同预算下，对目标指标的改进等于人类所做改进时对应的美元数」。另一个相关量是 cost saving，即在改回雇人变得更划算之前，agent 能省下的花费；作者认为它更难估计。
- **人类回报曲线：** 聚焦第 19 到第 82 号纪录（2025 年 1 月以来）。作者就其中六条纪录采访了两位主要贡献者（总提速 9.8%，约 142 小时）；由 LLM judge（Opus-4.6）估计每个 PR 的工时；两种估计取几何平均，再乘以校正系数 α = 1.58（bootstrap 95% CI [1.07, 2.62]）。按每小时 $150 计算，每提升 1% 约需 $2,500，人类总投入约 $250,000。在第 19 号纪录附近的拐点之前，每 1% 只需约 $200。
- **Agent 回报曲线：** 每次运行最多 $10,000（API 加 GPU），持续 5 天，在 Modal 上使用 4 个 H100 节点（32 块 GPU），并提供可以并行跑实验的异步工具。Agent 可以随意给中间解打分，prompt 引导它先用少量运行探索，再用 n = 8 确认。声称的进展会重跑 40 次以上，每花 $500 就把排名前三的中间解重跑一遍；曲线以累计方式和按花费翻倍的方式展示，带 bootstrap ±1 SD 区间。
- **Trace：** agent 做了一处缩短训练时间的改动，先由受保护的 runner 计时，validator 根据 logits 检查 loss，再对这次提升做重新验证；把每个累计花费点上经重新验证的提速百分比，与按每 1% $2,500 计算的人类曲线比较。
- **结果：** 六次高花费运行。GPT-5 和 Opus-4.1 在重新验证后没有实质进展。另外四个模型的 horizon 为正，在 $600 到 $3.3K 之间。在中等假设下，Opus-4.8（经重新验证的提升约 1.5%）为 $3,300，GPT-5.5（提升约 1%）为 $2,300。在人类成本分别取容易 / 中等 / 困难（每 1% $1K / $2.5K / $10K）时，Opus-4.8 为 $120 / $3,300 / $14,400，GPT-5.5 为 $160 / $2,300 / $9,400。
- **可合并性：** 一位维护者判断约 70% 的 agent 想法可以合并；按提速份额计算，Opus-4.8 约 60%、GPT-5.5 约 50% 可合并。

## Typical Duration

每次 agent 运行最多 $10,000、5 天；实验约占 trajectory 成本的 70–90%。

## Main Contribution

一个以美元计价的指标，在同一个优化问题上比较 agent 和人类的投入回报，并用 NanoGPT speedrun 做了实证演示。

## Key Design Ideas

- 用同一个单位（美元）衡量 agent 和人类的投入，包括模型 API、GPU 算力和人工。
- 对 agent 声称的提升反复重新验证，因为原始 trajectory 会因噪声而高估进展。
- 人类投入从两个来源（采访和 LLM judge）估计，并用贡献者的事后估计来校准。
- 在容易、中等、困难三种人类成本假设下做敏感性分析。

## Strengths

- 连续评分能记录部分进展；在这类问题上，只看通过与否会把这些进展丢掉。
- 重新验证加上受保护的 runner 和 validator，可以防止由噪声带来或被篡改的提升；报告记录了发现的 reward hacking 和脆弱改动。
- 检查了污染问题：从第 12 号纪录开始的运行显示出对后续纪录的记忆，因此没有纳入主要结果。

## Limitations

- 作者表示 harness 可能效率不高，agent 的改动大多是超参数调整（用维护者的话说，"mostly fiddling with knobs"）。
- 人类投入的估计不确定：judge 估计的总量比贡献者自己的估计低约 37%，上游研究和协作也没有完全算进去。
- 结果对「人类每提升 1% 的成本」这一假设很敏感，而且方法假设 agent 的回报比人类的回报递减得更快。
- 只衡量了 agent 自主优化，没有衡量人机协作；第 78 号纪录里本身已经包含一些由 agent 产生的优化。
- 从第 78 号纪录开始的运行大多发生在模型的知识截止日期之后，Opus-4.8 可能是例外。
- Repository note: 每个模型只在一个任务上报告了一次运行，所以模型之间的差异没有配套的运行间方差；报告正文没有写出第六个模型的名字。

## Related Works

- [RE-Bench](./re-bench.md) — 同样在 ML research engineering 优化任务上、在相同预算下把 agent 和人类专家比较（预算以时间而不是美元计）；报告点名它是这个指标可以概括的 benchmark 之一。
- [MLE-bench](./mle-bench.md) — 报告点名的另一个可以用这个指标概括的 AI R&D benchmark。
