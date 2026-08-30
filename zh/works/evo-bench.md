# Evo-Bench (2026)

> [English](../../works/evo-bench.md) | **简体中文**

> **首次公开：** 2026-08-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.09096)

## Overview

Evo-Bench 是一个 benchmark，评估语言模型自主改进自身 agent harness 的内在能力——harness 即那套可编辑的脚手架，管控着模型如何推理、如何与工具交互——覆盖 Search、Office 与 General 三类 agent 领域。

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent harness 自我改进 benchmark，覆盖 Search/Office/General 场景；未评估任何科学或工程任务。

## Links

- **Paper:** https://arxiv.org/abs/2608.09096
- **Venue:** arXiv preprint (2026)

## Summary

Evo-Bench 针对的是"harness 演化"：模型并不去求解某个固定任务，而是反复编辑一套操作性 harness——它控制着策略如何与任务交互——并按演化后的 harness 使下游性能提升多少来计分。该 benchmark 由一条 harness 引导的流水线构建：先筛出真正对 harness 质量敏感的任务，再用敏感度感知的分层划分把它们分成验证集与评估集，从而将"改进 harness 的技能"与基座模型强弱、任务特定过拟合区分开来。模型出发的种子 harness 是一个极简的 CodeAct 循环，仅有 shell 执行与作答完成两项能力。任务取自横跨三个领域的五个源 benchmark：Search、Office 与 General。

## Tasks

共 608 个任务，划分为 160 个任务的验证集（每个源 benchmark 32 个）与 448 个任务的评估集。评估集包含 128 个 BrowseComp、128 个 HLE、64 个 GDPval、64 个 APEX-Agents 与 64 个 Claw-Eval 任务。五个源 benchmark 映射到三个领域：Search（BrowseComp、HLE）、Office（GDPval、APEX-Agents）与 General（Claw-Eval）。

构建（harness 引导框架）：
- **阶段 1 — 辅助 harness 生成。** 用 320 个辅助任务（128 search、128 office、64 general）以四个前沿模型独立运行 harness 演化，再经多样性感知的挑选得到 12 个有代表性的 harness。
- **阶段 2 — harness 引导的任务筛选。** 2,329 个候选任务在这 12 个辅助 harness 下评估；每个任务的"harness 敏感度"定义为任务级得分与整体 harness 质量之间的相关性。敏感度非正的任务被过滤掉，分层挑选则保持难度分布。

## Domains

该 benchmark 覆盖三类 agent 领域——Search（网页浏览 / 信息检索）、Office（文档与工作流任务）与 General。这些都是通用型 agent 场景，未评估任何具体的自然科学或工程学科。Repository note: 由于受评领域是 Search / Office / General 类 agent 任务而非某个科学或工程学科，此处不指派任何标准科学或工程 domain。

## Evaluation

每个模型充当"演化器"，反复编辑自身 harness；所得 harness 应用于留出的评估集并计分。报告指标包括 **Overall Score**（评估集上的性能）、各领域分数（Search、Office、General），以及 **Anytime Validation Score**——定义为在演化预算内平均的"迄今最佳"验证性能。演化后的 harness 与人工设计的（"Artificial Harness"）基线及 CodeAct 种子基线作比较。

主要结果（总体分）：最强模型达到 46.3（较其种子提升 +16.6），第二名达到 45.8（+16.1），人工设计基线为 47.5，CodeAct 种子基线为 29.7。共评估九个前沿与开放权重模型：GPT-5.6 Sol、Claude Opus 4.8、GLM-5.2、Qwen3.7-Max、Minimax-M3、Deepseek V4 Pro、Kimi K2.7 Code（前沿），以及 Qwen3.6-27b、Gemma-4-31B（开放权重）。Repository note: 模型名称字符串按一手来源所报转录，此处未作独立核实。

## Typical Duration

每次 harness 演化运行受限于 20 次迭代、1,000 个演化器步与 48 小时。演化过程中的策略 rollout 上限为 300 步、一小时。

## Main Contribution

作者提出 Evo-Bench，称其为首个专门评估模型内在 harness 演化能力的 benchmark，并配以一套 harness 引导的构建框架（辅助任务演化加敏感度感知的分层划分），意在将 harness 改进技能与基座模型强弱、任务特定过拟合区分开来。

## Key Design Ideas

- 将评估框定于 **harness 自我改进**，而非静态任务求解：受评的产物是模型编辑出的 harness，从极简的 CodeAct 种子出发。
- **harness 敏感度过滤**只保留得分与整体 harness 质量相关的任务，使测得的增益反映 harness 变化而非原始能力。
- **敏感度感知的分层划分**将任务分入验证集与评估集，以支撑跨集泛化并抑制过拟合。
- **Anytime Validation Score** 刻画演化预算内的"迄今最佳"轨迹，而不仅是最终 harness。
- 有界的演化预算（20 次迭代 / 1,000 步 / 48 小时）配以受限的策略 rollout（300 步 / 1 小时）。

## Strengths

- 通过构建流水线与敏感度过滤，将某项具体能力（harness 改进）与基座模型强弱分离开来。
- 覆盖三个不同的 agent 领域与五个源 benchmark，兼评前沿与开放权重模型。
- 报告轨迹感知的行为（anytime 验证、早期饱和等时间异常），而非只给最终分数。

## Limitations

- 作者报告，自主演化在需要高度特定处理工作流的 Office 任务上表现吃力，并指出早期饱和等时间异常。
- 演化后的 harness 总体上逼近但未超过人工设计基线（最佳 46.3 对 47.5）。
- Repository note: 若干评估数值与模型名称字符串取自对一手来源的自动化抽取；任务数的算术内部自洽（32×5 = 160；128+128+64+64+64 = 448；160+448 = 608），但个别结果值在引用前应对照论文重新核实。

## Related Works

- [UniClawBench](./uniclawbench.md) — Claw-Eval 是 Evo-Bench General 领域的源 benchmark 之一，出自同一条 Claw 评估线。
- [GAIA](./gaia.md) — 另一个横跨浏览与工具使用的通用型长 horizon agent benchmark。
- [Frontier-Eng](./frontier-eng.md) — 同样将 horizon 框定为固定预算下的迭代式"提出-评估"优化轨迹。
