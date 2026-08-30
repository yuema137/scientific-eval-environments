# MobileJudgeBench (2026)

> [English](../../works/mobilejudgebench.md) | **简体中文**

## Overview

MobileJudgeBench 用 931 条人工标注的 mobile-agent trajectory 检验自动 evaluator。这些数据来自六个 benchmark、四种 agent model、289 个任务和 68 个 app。

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 面向通用 mobile-agent trajectory 的 evaluator-validation benchmark。

## Links

- **Paper:** <https://arxiv.org/abs/2608.11434>
- **Venue:** arXiv preprint (2026)

## Summary

Benchmark 将六种 judge 方法与五种 LLM backbone 组合，以人工成功标签为 ground truth。它既报告 trajectory 分类指标，也检查这些指标能否预测两种下游用途：复现人类给出的 agent 排名，以及为 on-policy training 提供 reward。简单的截图采样 baseline 不输专门设计的复杂 pipeline；最佳配置准确率为 90.9%，balanced accuracy 与 agent 排名 fidelity 的 Spearman ρ 为 0.87。

## Tasks

931 条 trajectory 来自 SPA-Bench、AndroidWorld、AndroidLab、AndroidArena、A3 和 B-MoCA，共覆盖 289 个任务与 68 个 app。每条 trajectory 包含四种 mobile-agent model 之一产生的截图和动作。

## Domains

Mobile GUI agent 与 app 交互，不属于规范化科学或工程 domain。

## Evaluation

相对于人工 success label 报告 accuracy、balanced accuracy、precision、recall 与 F1，并计算 agent-level 排名相关和成功率估计误差。每条 trajectory 由九位标注者中的二至四人独立标注，成对一致率为 88.4%。Meta-correlation 与下游 RL 实验进一步检查这些指标是否能预测实际 judge utility。

## Typical Duration

离线评价已有 trajectory，不为 judge 规定环境执行预算。

## Main Contribution

不仅测 judge 与人类是否一致，还检验 judge 指标能否预测可靠的 agent 比较和有用的训练 reward。

## Key Design Ideas

- 数据横跨六个 benchmark、多种 agent 和 68 个 app。
- 将 judge method 与 backbone 视为两个独立变量。
- 把离线指标同排名 fidelity 和 on-policy training 结果连接起来。
- 用 precision 与 recall 分析保守型和宽松型失败。

## Strengths

- 每条 trajectory 都有外部人工参考。
- 下游验证检查 judge 指标在 benchmark 之外是否有用。
- 简单 baseline 能直接暴露复杂 pipeline 是否真的带来可靠性。

## Limitations

- 数据只覆盖 mobile GUI agent。
- 二元 success 无法表达部分完成和过程质量。
- On-policy 验证只覆盖一种训练设置，不能代表所有 reward model。

## Related Works

- [AgentRewardBench](./agentrewardbench.md)
- [Plan-RewardBench](./plan-rewardbench.md)
- [SkillTV-Bench](./skilltv-bench.md)
