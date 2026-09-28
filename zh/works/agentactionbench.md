# AgentActionBench (2026)

> [English](../../works/agentactionbench.md) | **简体中文**

> **首次公开：** 2026-04-19 · **来源：** [官方任务材料发布提交](https://github.com/KOU-199024/NLPCC-2026-Shared-Task-11/commit/4dabe5fdd22a28a24d72dc31d77ba3c2e11c0892)

## Overview

AgentActionBench 用实际操作记录评估论文复现。MCP Action Recorder 记录读取、写入和命令执行，让一个看似合理的最终代码仓库不能直接替代“实验确实执行过”的证据。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **论文：** [Overview of the NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction from Scientific Papers](https://arxiv.org/abs/2609.11117)，2026 年 9 月 10 日发布的共享任务介绍预印本。
- **全文：** <https://arxiv.org/html/2609.11117v1>
- **官方任务、数据与记录工具：** <https://github.com/KOU-199024/NLPCC-2026-Shared-Task-11>

## Summary

论文记录了 150 项复现任务，包括 120 篇 ML 论文和 30 篇 AI4Science 论文。其中 15 篇有人工 rubric，用于开发和验证评分标准；其余论文决定主要排行榜成绩。四月的仓库发布已包含任务说明、论文、rubric 和记录工具代码，九月论文则报告扩充后的基准及实验结果。

## Tasks

给定 PDF 或 Markdown 论文，agent 通过 Read、Write、Execute 工具构建并运行复现仓库，最后提交仓库和按时间排序的操作日志。评测分成五个阶段：阅读论文、编写计划、实现代码、执行命令和匹配结果。

## Domains

AI 与机器学习研究共 120 篇论文；另有天文学、生物、化学、环境科学、材料科学和医学的 AI4Science 论文，合计 30 篇。原文未报告这六个科学领域各自的数量。所有任务都以复现特定已发表实验为目标。

## Evaluation

ChatGPT-4o-mini 针对每条 rubric 读取论文与相关工具日志，判断通过或失败，再按该条的重要性权重计算复现分数。执行日志提供证据，但最后的 rubric 判断仍由模型作出。全套基准有超过 10,000 个条目。在人工子集上，自动 rubric 和人工 rubric 得到的分数之间，Pearson 相关系数为 0.93，Spearman 为 0.88。这里比较的是两种 rubric 来源，不是让人工独立判断每条 agent 操作。分阶段结果显示，执行命令和匹配结果明显弱于规划与代码实现。

## Typical Duration

论文报告实验使用两张 NVIDIA L40S GPU，但未给出统一的单任务实际时间预算。

## Main Contribution

把记录操作的执行环境与论文专用评分条目结合起来，评估完整复现过程。

## Key Design Ideas

- 为不同 rubric 阶段选取能够提供证据的工具日志。
- 用经过交叉审阅的人工子集检查自动生成的 rubric。
- 将开发用 rubric 与主要排行榜任务分开。

## Strengths

- 可以看出“写出代码”和“成功执行代码”之间的差距。
- 除常规 ML 论文外，还覆盖科学应用。

## Limitations

- Repository note: 两种 rubric 所得分数的相关性，不能证明每一条自动通过或失败判断都准确。
- 人工 rubric 子集较小，未报告人类实际复现实验的基线。
- 隐藏测试 rubric 并不能保证模型没见过已经发表的论文。

## Related Works

- [PaperBench](./paperbench.md)
- [Beyond Final Scores](./beyond-final-scores.md)
