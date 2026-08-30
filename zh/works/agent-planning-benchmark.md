# Agent Planning Benchmark (2026)

> [English](../../works/agent-planning-benchmark.md) | **简体中文**

> **首次公开：** 2026-06-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.04874)

## Overview

Agent Planning Benchmark（APB）是一套规划专项诊断 benchmark，包含横跨 22 个领域、五种设置的 4,209 个多模态实例，把完整计划生成与基于反馈的下一步规划分开，并测试 agent 面对工具或任务缺陷时的稳健性。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — 横跨多类非研究任务的通用多模态与工具规划 benchmark。

## Links

- **Paper:** <https://arxiv.org/abs/2606.04874>
- **Code:** <https://github.com/Mikivishy/AgentPlanningBenchmark>
- **Venue:** arXiv preprint (2026)

## Summary

APB 的出发点是：端到端成功率无法判断失败源于规划还是执行。它分别评价执行前一次性给出的整体计划、依据 trajectory 反馈选择的一至三步动作、存在无关工具时的规划、关键工具损坏但有替代项时的恢复，以及约束导致任务无解时的拒绝。在 12 个多模态 LLM 上，论文观察到基于反馈的逐步规划与整体规划之间存在稳定差距，模型也容易受干扰工具和信息缺失影响。

## Tasks

4,209 个实例，来源包括 FrameThinker、GAIA、GTA、OpenCUA 和 ToolBench 等 agent 任务，覆盖 22 个领域。五种设置包括 1,109 个整体规划实例、从执行 trajectory 派生的逐步规划实例、1,500 个无关工具实例、300 个坏工具实例和 400 个不可解实例。逐步模式要求从当前状态和已有反馈预测未来一至三步；整体模式则在没有中间观察的情况下给出完整工具与动作计划。

## Domains

横跨 web、移动设备、桌面操作、信息、金融、视觉和通用助手等 22 类多模态与工具任务。论文没有给出足以支持保守映射的逐实例领域表，因此不归入本仓库的规范化科学与工程 domain。

## Evaluation

APB 报告二元 Plan Correctness、六档的 0–1 Plan Grade，以及 E1–E6 错误分类：目标理解、过早结束或任务不完整、约束违反、逻辑、工具使用和幻觉。评分采用参考计划辅助的 LLM-as-a-judge 协议；数据构建则结合规则检查、两阶段模型验证和人工核验。论文还在 200 个 ToolSandbox 与 200 个 τ²-bench 任务上检验 APB 引导的计划改进能否迁移到下游执行指标。

## Typical Duration

离线生成计划，不执行完整 benchmark 环境。逐步实例从 trajectory 前缀预测后续一至三步，整体实例一次生成完整计划。不同来源任务之间没有统一墙钟预算。

## Main Contribution

一层位于执行之前的规划专项诊断：分别评价全局与局部决策质量，并用受控稳健性设置揭示工具选择、失败恢复和合理拒绝方面的问题。

## Key Design Ideas

- 分开评估整体规划与基于反馈的逐步规划。
- 注入语义上看似相关、功能上无关的工具。
- 用名称不同但功能等价的替代工具替换损坏的关键工具。
- 构造约束冲突、信息缺失、工具缺失和视觉信息不可访问的应拒绝任务。
- 将总正确率与严重程度分级、命名错误类别结合。

## Strengths

- 设计直接针对规划与执行相互混淆的问题。
- 局部和全局规划在不同信息条件下分别测量。
- 稳健性变体把工具噪声、恢复和不可行性识别变成受控测试。
- 下游验证检查诊断指标的提升能否转成执行收益。

## Limitations

- 计划评分大多依赖 LLM judge，尽管构建和验证包含规则与人工检查。
- 任务来源异质，领域特有的科学正确性并非重点。
- 逐步正确性要求动作合理且推动目标，但不衡量它相对所有其他选择是否最优。

## Related Works

- [PlanBench](./planbench.md) — 在形式化领域中提供 solver 支撑的有效性与最优性检查。
- [NATURAL PLAN](./natural-plan.md) — 在信息齐全时隔离规划，但不测量基于反馈的下一步。
- [TravelPlanner](./travelplanner.md) — 在封闭工具环境中联合评估规划与执行。
- [Plan-RewardBench](./plan-rewardbench.md) — 评价对完整工具 trajectory 进行排序的 judge，其中包含困难规划偏好对。
