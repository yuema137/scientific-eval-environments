# Fisher-R1 / P-Bench (2026)

> [English](../../works/fisher-r1.md) | **简体中文**

## Overview

一个由 425 道贴近真实的假设检验任务组成的 benchmark（P-Bench），以及一个训练来做统计上有效之假设检验的开放权重 LLM agent（Fisher-R1）；评估 agent 是否选对了合适的统计方法、算出正确的 p 值，并得出有效的拒绝/不拒绝结论。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.07437>
- **Code:** <https://github.com/jmu27/FisherR1>
- **Venue:** arXiv preprint（2026-08-07 提交）

## Summary

该工作针对这样一种失败模式：LLM agent 正确执行了统计分析，却得出了错误的推断结论——例如报告一个在数据所依赖的假设下并不成立的 p 值。为衡量这一点，作者构建了 P-Bench，一个由 425 道开放式假设检验任务组成的 benchmark，覆盖经济学、生物学与医学；每个任务只给出一个科学假设与一份数据集，要求 agent 选择统计方法、计算 p 值并得出结论。作者还提出 Fisher-R1，一个开放权重 agent，先经监督微调、再在带已验证统计奖励的合成假设检验任务上做强化学习。据报告，在 P-Bench 上 Fisher-R1-14B 相对其骨干模型有所提升，并优于包括 GPT-5.4 与 DeepSeek-V4-Pro 在内的专有与开源基线。

## Tasks

425 道开放式假设检验任务，分为 Easy（203 道）与 Hard（222 道）两档。每个任务都源自领域专家最初开展的一次真实科学分析，并经三阶段流水线构建：(1) 在洁净机器上复现参考分析并记录执行日志；(2) 过滤掉无法复现的分析，并把每条保留的论断锚定到执行日志；(3) 生成一个自包含的可执行任务，配一份结构化的答案键。数据来源：经济学取自顶级期刊的同行评审论文（数据在 Harvard Dataverse）；生物学取自同行评审论文（数据在 cBioPortal）；医学/生物统计取自 Vanderbilt Biostatistics 的教学材料（数据集通过 R 包分发）。任务同时覆盖随机实验与观察性研究。摘要与所抽取文本均未给出各领域的任务数量分布——TODO(reference)。

## Domains

经济学、生物学与医学。

## Evaluation

每个标准 p 值、检验统计量与决策都从一次已记录的、对规范参考代码的运行中读出。报告两项指标：**Raw**——agent 最终的拒绝/不拒绝决策是否与标准决策一致；以及 **Strict**——Raw ∧ |z(p̂) − z(p*)| < 0.5，额外要求所报告 p 值在 0.5 个 z 分数单位内接近标准值。p 值经单调、无分布的映射 z(p) = Φ⁻¹(1 − p/2) 在 z 空间中比较。成功以 pass@1（三次独立运行的均值 ± 标准差）与 pass@3（三次试验中任一成功即算成功）报告。

## Typical Duration

未说明。训练超参数报告最大回复长度 4096 token、最大提示长度 2048 token，但未报告单任务的轨迹长度或墙钟预算——TODO(reference)。

## Main Contribution

作者陈述的贡献是：(1) P-Bench，一个评估 agent 所报告 p 值在数据所依赖假设下是否统计有效的 benchmark——作者认为既有 benchmark 未能捕捉这一失败模式；(2) Fisher-R1，一个在带已验证统计奖励的合成任务上用强化学习训练的开放权重 agent，据报告在单次试验成功率上相对 DeepSeek-V4-Pro 平均相对提升 21%，在最具挑战性的任务上提升至多 26%。

## Key Design Ideas

- 标准答案从对规范参考代码的已记录执行中读出，而非人工撰写，使答案键可验证。
- p 值在 z 空间中经 z(p) = Φ⁻¹(1 − p/2) 比较——这是一种单调、无分布的重新标注，用于公平地为 p 值接近程度打分。
- 两级评分（Raw 决策匹配；Strict 决策匹配外加 p 值接近程度），把正确结论与正确量级区分开。
- Fisher-R1 以 Qwen2.5-Coder-7B 与 14B 为骨干，先监督微调、再用 Decoupled Clip and Dynamic Sampling Policy Optimization（DAPO）做强化学习。
- 奖励 R(o) = I_valid(o)·(w_p·r_p(o) + w_c·r_c(o))，其中 w_p = 0.9、w_c = 0.1，p 值分量 r_p(o) = exp(−|min{z(p̂),5} − min{z(p*),5}|/σ)（σ = 1），并由有效性指示项门控。
- 合成训练语料含 8,642 个任务，由六个独立因子组合生成：统计方法、领域场景、样本量、效应量、提示风格与随机种子。

## Strengths

- 答案键与奖励都植根于对参考代码的已记录执行，给出可验证而非启发式的标准真值（论文）。
- 针对一个具体且被测量不足的失败模式——在分析正确执行的情况下仍得出推断无效的结论（论文）。
- 构建阶段的可复现性过滤剔除了无法在洁净机器上重新执行的分析（论文）。

## Limitations

- Repository note: 425 个任务在经济学、生物学与医学间的各领域分布，未在所查阅来源中说明。
- Repository note: 覆盖面仅限于三个领域（经济学、生物学、医学）的假设检验/p 值任务，未涉及其他形式的统计推断或科学分析。
- Repository note: 所报告的对比增益是相对一组固定的同期基线（如 GPT-5.4、DeepSeek-V4-Pro），反映的是这些模型在评估时的水平。

## Related Works

- TODO(reference) —— 面向科学 agent 数据分析与统计推断的相关 benchmark。
