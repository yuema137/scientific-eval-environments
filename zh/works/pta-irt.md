# PTA-IRT (2026)

> [English](../../works/pta-irt.md) | **简体中文**

> **首次公开：** 2026-08-29 · **来源：** [官方代码与数据发布提交](https://github.com/DeepSoftwareAnalytics/PTA-IRT/commit/b38263b72f3c4a52fcc8fe478e1eae385ba423a6)

## Overview

PTA-IRT 只让软件 agent 执行一小部分任务，就估计它在整套基准上的成绩。传统项目反应模型主要使用成功或失败记录；PTA-IRT 在校准时加入历史执行轨迹，利用 agent 怎样解决问题的信息。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 面向一般软件问题修复的评测方法，不对应特定科学研究流程。

## Links

- **论文：** [Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation](https://arxiv.org/abs/2609.01603)，2026 年 9 月 1 日预印本。
- **全文：** <https://arxiv.org/html/2609.01603v1>
- **代码与数据：** <https://github.com/DeepSoftwareAnalytics/PTA-IRT>

## Summary

方法先将历史轨迹转换成摘要，再学习任务难度和区分能力，按难度分层挑选信息量较高的题目，并训练教师与学生估计器。新 agent 只需运行选中的任务，估计器据此预测其余任务的表现。

## Tasks

实验使用 SWE-bench Lite（300 题）、Verified（500 题）、Full（2,294 题）和 Pro（730 题）。这些版本有重叠，不能当成四组互不相交的题目。对应的 agent／模型集合分别有 35、70、14 和 14 个成员。留出的 agent 产生校准任务结果，再由估计器转成全套分数和排名。

## Domains

软件与系统工程，具体是代码仓库级的问题修复。工作贡献是现有任务上的评测估计器，并非新的科学编程任务集。

## Evaluation

四折交叉验证分开历史模型和留出模型。平均绝对误差衡量分数估计偏差，Kendall tau 和 Spearman rho 衡量预测排名与全套实测排名的一致性。在 10% 校准比例下，论文报告平均 MAE 为 0.041、tau 为 0.888、rho 为 0.973。消融包括去除轨迹条件、改变选题方法，以及破坏或丢弃摘要。给新 agent 评分时，无需取得它在整套任务上的轨迹。

## Typical Duration

没有统一实际运行时长。主实验执行 10% 的基准题目用于校准；Lite 上测试了 5–25% 的比例。历史轨迹收集和模型生成摘要仍有离线成本。

## Main Contribution

利用轨迹信息选择评测子集并估计分数，同时控制新 agent 的任务执行量。

## Key Design Ideas

- 将历史过程证据作为训练阶段可用的额外信息。
- 按难度层次平衡信息量驱动的选题。
- 分别验证分数与排名的恢复程度，不把它们混同于任务本身的成功率。

## Strengths

- 在四个基准版本上验证，并报告组件消融。
- 明确区分离线已有信息与新 agent 实际提供的观测。

## Limitations

- 需要历史结果和可用执行轨迹。
- Full 和 Pro 的 agent 集合远小于 Lite 和 Verified。
- Repository note: 预测分数不等于未执行任务的实测通过率；这些结果也不能证明方法能迁移到不相关的科学工作流。

## Related Works

- [SWE-bench](./swe-bench.md)
- [The Replay Gap](./the-replay-gap.md)
