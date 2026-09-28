# HarnessDev (2026)

> [English](../../works/harnessdev.md) | **简体中文**

> **首次公开：** 2026-09-01 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.01437)

## Overview

HarnessDev 检查模型能否构建可复用的 agent 执行软件，并根据反馈继续改进。模型提交的是 harness；评测先将它冻结，再让执行模型用它完成下游任务。

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2609.01437>
- **Full text:** <https://arxiv.org/html/2609.01437v1>
- **Project:** <https://self-developing-agents.github.io/>
- **Venue:** arXiv 预印本（2026）

## Summary

Creation 从一个能够运行、但没有解题策略的种子程序和 1–3 个开发样例开始。Evolution 从已创建的 harness 出发，开放指定任务的执行反馈。编写者与执行者分开后，同一份软件既可以搭配编写它的模型，也可以搭配统一的运行模型进行测试。

## Tasks

六个编写模型、四类任务、2,207 个不重复的下游实例：SWE-bench Pro public 731 题、Terminal-Bench 2.1 89 题、MLE-bench 75 题、EQ-Bench3 46 题、BrowseComp 1,266 题。Evolution 只测代码 harness，用 100 道 SWE-Pro 和 89 道 Terminal-Bench 题提供反馈，另有 630 道 SWE-Pro 题不向开发过程公开。反馈集来自这些基准，不额外计入总量。

## Domains

软件工程、机器学习实验、写作和信息检索。科学任务部分采用 MLE-bench 的模型训练竞赛及提交评分；其余任务类别不属于科学研究评测。

## Evaluation

- 冻结后的 harness 按下游基准原有指标评分，包括任务成功率、竞赛奖牌、写作 rubric 或检索准确率。
- Self-Eval 让编写模型执行；Unified-Eval 固定执行模型。Evolution 分开报告反馈集和隐藏集上的变化。
- 代码任务依据仓库 diff 或最终环境状态给分，不采信 harness 自报成功。论文审计源码及轨迹，在报告的运行中未发现通过禁止途径得分的情况。
- 报告执行模型 token 总量及每题均值，不计编写、修改 harness 的开发 token。
- 在 Self-Eval 下，生成的 harness 在写作上接近参考系统，在机器学习实验上超过参考系统，但在代码和检索上仍落后。连续修订的收益不稳定，换成未见任务或其他执行模型后，收益往往缩小。

## Typical Duration

MLE-bench 每题允许十小时，其中半小时留给评分器；Evolution 代码任务每题允许两小时。两者都有 500 步上限。

## Main Contribution

把可长期复用的 harness 的构建与维护本身作为评测目标。

## Key Design Ideas

不提供解题策略的种子、独立的编写与执行角色、冻结产物和隐藏下游检查，共同区分开发反馈与泛化能力。

## Strengths

保留可执行产物和轨迹，记录 token 成本，并检查换执行模型后改进是否仍然有效。

## Limitations

Evolution 只覆盖代码。效率指标不包含开发成本。人工编写的参考系统成绩部分来自已发布报告，并非统一设置下的本地重跑。留出任务是对开发过程隐藏，不代表模型预训练时从未见过。

## Related Works

- [Evo-Bench](./evo-bench.md) — 测试对统一种子 harness 的改进。
- [EvoHarnessBench](./evoharnessbench.md) — 在可用能力扩大时检查适应与保留。
- [MLE-bench](./mle-bench.md) — 提供机器学习竞赛任务。
