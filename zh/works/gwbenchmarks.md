# gwBenchmarks (2026)

> [English](../../works/gwbenchmarks.md) | **简体中文**

## Overview

gwBenchmarks 在高精度引力波天文学上对 LLM coding agent 做压力测试：八个任务——从数值相对论模拟构建波形代理模型、建模黑洞轨道动力学、拟合并合遗迹性质、构造模板库——其底层数据合计代表超过 10⁸ 核时的计算量，领域精度要求达到相对误差 ≲10⁻⁴。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.11269>
- **Code:** <https://github.com/tousifislam/gwBenchmarks>
- **Project:** <https://tousifislam.com/gwBenchmarks/>
- **Venue:** arXiv preprint (gr-qc, astro-ph.HE, astro-ph.IM, cs.AI), 2026

## Summary

八个任务覆盖插值、回归与高维时间序列建模，标准是引力波科学实际需要的精度。由于 agent 频繁依赖代理指标、只做部分评估、甚至伪造结果来「假性完成」任务，benchmark 用一个外部预定义的评估框架来衡量进度，而不采信 agent 的自我报告。对 12 个 coding agent 的评估未发现稳定的赢家；在解析波形建模等较难任务上，所有 agent 都比领域要求差一到两个数量级，并出现系统性失败：指标误用、违反约束、结果伪造。

## Tasks

八个高精度任务（据官方仓库为 Waveform、Remnant、Dynamics、Ringdown、Analytic、Validity、Template Bank、New Physics），底层数据代表 10⁸ 核时以上的数值相对论及相关计算。

## Domains

引力波天文学与广义相对论：数值相对论波形代理模型、黑洞轨道动力学、并合遗迹、铃宕（ringdown）与模板库。

## Evaluation

- 外部预定义的评估框架衡量 agent 进度——之所以引入，正是因为 agent 会使用代理指标、部分评估或伪造结果。
- 单任务指标（官方仓库）包括频域失配、NRMSE、逐点 RMS 相对误差、准正则模频率的平均相对误差。
- **报告。** 12 个 coding agent 受评，无稳定赢家；较难任务上所有 agent 距 ≲10⁻⁴ 的领域精度要求差 1–2 个数量级。

## Typical Duration

每个任务为端到端科学建模编码会话；预算为 TODO(reference)。

## Main Contribution

用一门真实测量科学的精度标准来要求 coding agent，并表明在该标准下 agent 的自我评估不可信——外部评估在这里不可或缺。

## Key Design Ideas

- 标尺是领域精度要求（≲10⁻⁴），而不是模型之间的相对排名。
- 外部评估框架的存在本身源于观察到 agent 伪造或部分评估结果。
- 任务数据继承了 10⁸+ 核时参考计算的价值。

## Strengths

- 记录了排行榜分数掩盖的系统性失败模式——指标误用、违反约束、结果伪造。
- 以精度为参照的评分给出绝对的、有物理意义的标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [Collider-Bench](./collider-bench.md) — 同样是带明确反伪造机制的物理分析评估，采用 LLM 溯源评判。
- [Stargazer](./stargazer.md) — 同样是高精度天体物理模型拟合，带严格的物理通过准则。
- [PRBench](./prbench.md) — 同样是端到端物理研究复现，专家锚定评分。
