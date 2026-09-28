# EvoHarnessBench (2026)

> [English](../../works/evoharnessbench.md) | **简体中文**

> **首次公开：** 2026-09-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.04280)

## Overview

EvoHarnessBench 检查可用 harness 扩大后，agent 是否还能解决以前的任务。它逐步增加工具、技能或专家 agent，同时保持已引入的任务不变，分别观察旧能力保留和新能力适应。

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 基于企业流程和软件工具任务评测通用 harness，不对应专门的科学研究流程。

## Links

- **论文：** [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280)，2026 年预印本。
- **全文：** <https://arxiv.org/html/2609.04280v1>
- **官方项目与评测说明：** <https://mas-orchestra.salesforceresearch.ai/evoharness/>

## Summary

基准从 EnterpriseOps-Gym 和 Agents' Last Exam 构造 17 条演化序列，每条有三至六个阶段。802 个不同任务形成 1,510 个按评测轴展开的样例，后者不是不同任务的数量。部署评测不在阶段间保留经验；适应评测允许从独立适应集学到的产物持续保留。

## Tasks

只有当所需能力全部可用、且至少有一项能力刚被引入时，任务才会进入对应阶段。后续阶段提供累积的全部 harness，包括不相关能力。评测者在更大的 harness 下重测旧任务，同时测试新任务。整个序列涵盖 520 个工具、42 项隐藏参考技能和 62 个专家 agent。

## Domains

通用企业流程和异构软件工具环境。Repository note: 此处没有确认具体科学领域的任务子集，因此通过评测 Topic 组织，不分配兜底领域。

## Evaluation

验证器检查数据库状态、文件内容等任务结果。按阶段和任务批次记录的表现矩阵，同时保留新任务准确率和旧任务表现。后向迁移比较旧批次初次引入时与最终阶段的成绩；前向迁移比较当阶段适应前后在新批次上的成绩。Token、工具调用和延迟反映运行成本。分析还区分是否选对能力与是否成功使用能力。

## Typical Duration

每条序列有三至六个 harness 阶段。论文报告运行成本指标，没有给出适用于所有任务的统一时长。

## Main Contribution

提供一种评测流程，检查即使模型权重不变，harness 变化是否仍会造成已有能力下降。

## Key Design Ideas

- 能力集合单调扩大，旧任务保持不变。
- 分开适应集和留出评测集。
- 分别报告旧能力保留与新任务适应，不只看总准确率。

## Strengths

- 部署对照将 harness 扩大的影响与累积经验的影响分开。
- 用验证器检查结果，同时记录开销。

## Limitations

- 能力只增加，不测试移除或修改。
- 任务和验证器来自两个已有环境。
- Repository note: 收录依据是 harness 与技能评测；其中的专家 agent 评测轴不意味着本仓库扩大到一般多 agent 系统研究。

## Related Works

- [HarnessOpt-Bench](./harnessopt-bench.md)
- [Skill-Use](./skill-use.md)
