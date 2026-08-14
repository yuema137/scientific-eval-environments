# VESTA / DAWN (2026)

> [English](../../works/vesta-dawn.md) | **简体中文**

## Overview

VESTA 是一个视觉语言 agent，用一套在 episode 中动态扩充的工具箱做迭代式统计模型拟合；随之提出的 DAWN 是一个含 400 个实例的 benchmark，任务为分布拟合与时间序列建模，其中最难的两个划分取自真实的天体物理建模问题——恒星初始质量函数与引力波啁啾信号。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.00384
- **Code:** https://github.com/wrudman/VESTA

## Summary

论文认为，当前模型做不好科学家拟合模型时真正在跑的那个迭代循环——作图、猜一个函数形式、拟合、检查残差、再修改——于是给 agent 配了一套会在 episode 过程中不断扩充的工具箱，涵盖数据变换、假设驱动的可视化和统计检验。为衡量这一循环上的进展，作者提出 DAWN（Dataset for Automated Workflows and Numerical Modeling），它把合成的 easy 与 hard 划分与取自真实天体物理函数族的天文划分配在一起，使难度来自真实科学模型的形态，而不是靠加噪声堆出来。DAWN 与 agent 并列，被作为第一等的贡献呈现。

## Tasks

共 400 个实例：200 个分布拟合任务与 200 个时间序列任务，各分三档。分布拟合含 50 个 easy 实例（单一分布）、100 个 hard 实例（两个分布的混合），以及一个 50 实例的天文划分，主题为恒星初始质量函数。时间序列含 50 个 easy 实例（线性趋势加基本季节性）、100 个 hard 实例（复杂动力学与非标准周期性），以及一个 50 实例的天文划分，主题为引力波啁啾。初始质量函数任务覆盖五种函数形式——Salpeter（单一幂律）、Kroupa（三段折线幂律）、Chabrier（对数正态过渡到幂律），以及两个自由形式变体——论文指出，它们只有在 log-log 空间中才在视觉上可区分。啁啾任务建模持续升高的频率，复杂变体另加幅度衰减包络以刻画 inspiral-ringdown 行为。实例由合成生成，参数从各档、各函数族的取值范围内均匀采样；每个分布拟合数据集含 600–1,500 个点，每个时间序列数据集含 600 个观测。

## Domains

DAWN 最难的两个划分属天文学：恢复正确的初始质量函数族及其参数是恒星族群建模问题，而拟合带 inspiral-ringdown 包络的啁啾则是引力波源建模问题。其余划分是领域中立的统计建模，因此这项工作同时落在统计推断方法学轴（Mathematics）上。天文数据是由天体物理函数族模拟生成的，并非取自巡天档案，但那两个划分上受评的目标确实是天体物理模型恢复的结果。

## Evaluation

分布拟合任务以拟合分布与真值分布之间的 Jensen-Shannon 散度计分——对称、取值有界于 [0,1]、越低越好。时间序列任务以留一交叉验证下的期望对数预测密度（ELPD-LOO）计分，并用滑动窗口采样来控制计算开销。评估了三个 backbone：GPT-5.4-mini、Claude Sonnet 4.6 与 Kimi K2.5。

## Typical Duration

`TODO(reference)` — 在为本卡片核验的材料中，论文未报告每任务的步数上限、wall-clock 时间或 token 预算。

## Main Contribution

作者自述的贡献有两方面：一个为视觉语言模型配备动态扩充统计工具箱、用于迭代式且以可视化为依据的模型拟合的 agent 框架；以及 DAWN benchmark，其提出目的被明确表述为「支持在当前方法失效的困难模型拟合问题上取得进展」。

## Key Design Ideas

- 工具箱在 episode 过程中扩充，而非一份固定的工具清单，让 agent 自己构造下一步所需的变换或检验。
- 把可视化当作证据通道：agent 生成假设驱动的图，再把图作为视觉输入读回来——这正是必须用视觉语言 backbone 的原因。
- 难度分档把合成的 easy 与 hard 案例同真实科学划分分开，使领域难度与统计难度分别可测。
- 天文划分选取的函数族在线性空间中近乎简并，只有做对了变换才分得开，从而直接考察「作图—变换—重拟合」这一循环。
- 采用恰当评分规则类指标（Jensen-Shannon 散度、ELPD-LOO）而非通过 / 不通过的精确匹配，使部分正确的拟合也能拿到相应的部分分数。

## Strengths

- benchmark 是一项具名且可独立成立的贡献，带明确的评分协议，而不是 agent 论文的评估附录。
- 连续的、分布层面的指标奖励确实更好的拟合，而不是奖励答案的精确匹配。
- 天文划分用的是真实天体物理函数族，而不是把一个通用数据集贴上科学标签。
- 在同一协议下评估了来自不同厂商的多个 backbone。

## Limitations

- DAWN 的全部实例都由已知参数范围合成生成，ground truth 因构造而存在，因此该 benchmark 并未考察面对真实巡天或探测器数据及其自身系统误差时的拟合能力。
- 只评估了三个 backbone，所报告排名的普适性因此受限。
- 天文部分只覆盖两个函数族（初始质量函数与啁啾），并未覆盖天文推断的广度。
- Repository note: 论文未报告每个 episode 的算力或步数预算，因此迭代式 agent 与单次作答 baseline 的结果无法在同等成本下比较。

## Related Works

- [Stargazer](./stargazer.md) — 最接近的天文 agent 邻居，评估的是天文研究分析而非统计模型拟合。
- [gwBenchmarks](./gwbenchmarks.md) — 引力波 agent 评估，与 DAWN 的啁啾划分有重叠。
- [BLADE](./blade.md) — 评估 agent 的数据分析决策，是相近的分析循环场景。
- [ScienceAgentBench](./scienceagentbench.md) — 数据驱动的科学 agent 任务，以可执行输出计分。
