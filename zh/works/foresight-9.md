# FORESIGHT-9 (2026)

> [English](../../works/foresight-9.md) | **简体中文**

> **首次公开：** 2026-08-29 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.29372)

## Overview

FORESIGHT-9 在反事实市场路径上测试自适应交易 agent，并核对内部研究状态与实际执行是否一致。否则，即使最终收益很高，系统原本的自适应机制也可能早已停止工作。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

N/A — 评估金融决策系统，未分配规范分类中的科学研究活动。

## Links

- **论文：** [FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents](https://arxiv.org/abs/2608.29372)，2026 年预印本。
- **全文与产物说明：** <https://arxiv.org/html/2608.29372v1>

## Summary

九条情景路径从 2026 年 7 月 15 日分叉。带固定随机种子的生成器保持预先声明的情景端点，时间限制则确保 agent 只能看到当前模拟日期已经开放的观测。实验组合两个 agent 框架和两个模型，共运行 36 次。固定等权策略胜过其中 31 次 agent 运行。

## Tasks

Agent 观察共享数据面板、维护因子、提出投资组合并执行配置。环境统一观测、交易约束、成本和时间规则，同时保留各系统自己的适应过程。

## Domains

金融市场与投资组合配置。Repository note: 当前科学／工程领域分类没有对应页面，因此通过评测 Topic 收录。

## Evaluation

结果指标包括净资产价值、回撤和 Sharpe 比率。过程记录分别跟踪存活因子库、系统声明的决策状态和实际持仓。某次高收益运行的存活因子已全部消失，但仍声称使用因子组合，实际执行的却是等权回退策略。因此，诊断要检查收益是否来自预期的自适应行为，不能只看组合有没有升值。

## Typical Duration

路径延伸至 2035 年 12 月 31 日，从共同信息边界之后计算约有 2,468 个模拟交易日。这是模拟跨度，不是实际耗时；论文未指定统一的单次运行时长。

## Main Contribution

在受控条件下同时测试跨情景稳健性，以及自适应状态和实际执行的一致性。

## Key Design Ideas

- 保留情景配置与随机种子，使路径可以确定性重建。
- 在每个模拟日期强制执行信息边界。
- 在相同情景和执行规则下，将 agent 与简单策略比较。

## Strengths

- 给出具体案例，说明过程记录如何改变对高收益结果的解释。
- 区分运行服务中的事件与模拟市场时间。

## Limitations

- 每个配置、每个情景只有一个随机种子，无法区分所有运行差异来源。
- 情景不是从经过校准的预测分布中采样，也没有独立人类专家验证。
- 规则要求仅做多且满仓，不测试做空和现金择时。
- Repository note: 论文描述了发布的产物，但本次核查没有找到可单独验证的官方下载地址。

## Related Works

- [Beyond Final Scores](./beyond-final-scores.md)
- [The Replay Gap](./the-replay-gap.md)
