# ATOM-Bench (2026)

> [English](../../works/atom-bench.md) | **简体中文**

> **首次公开：** 2026-06-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.16826)

## Overview

ATOM-Bench 是一个真实机器人 benchmark，把**原子**操作技能与由它们搭起来的**组合**任务分开，于是组合任务上的失败可以归因：要么是底层原子技能不过关，要么是组合复用本身真的失效了。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型机器人操作策略 benchmark；受评策略做的是桌面操作，而非某项科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.16826>
- **Project:** <https://flageval-baai.github.io/AtomBenchPage/>
- **Dataset:** <https://huggingface.co/AtomBench>
- **Venue:** arXiv preprint, June 2026

## Summary

通用操作策略越来越多地被当作机器人控制的基础模型来看待，但论文认为它们在真实世界中的泛化很难诊断：一个策略可能在演示过的任务上成功，底下细粒度的原子技能却仍然不行；也可能是无法把技能重新组合成新的任务结构。ATOM-Bench 把桌面操作分解为**运动原子**与**指令原子**，在成对的单臂与双臂机器人赛道上同时评估原子技能的习得与留出的组合泛化。策略先只在原子任务上微调，再同时在原子任务与留出的组合任务上评测，两项指标专门用来分开这两类失败源。作者同时公开演示数据与评测 rollout 数据，以支撑可复现的真实世界评估。

## Tasks

**30 个原子任务与 24 个留出的组合任务**，分布在成对的单臂与双臂机器人赛道上（单臂为 Franka Panda；双臂为 Agilex Cobot Magic，Mobile ALOHA 形制）。原子分类法分两族：

- **运动原子：** 抓放、重定向、推动、堆叠、倾倒、铰接物体开合。
- **指令原子：** 颜色、形状、大小、计数、排除、空间关系、目标位置。

组合任务把一个或多个运动原子与多个指令原子组合起来，并从微调中留出。原子微调采集了 **3,000 条人类遥操作演示**。`TODO(reference)` — 各赛道上 30 个原子任务在运动族与指令族之间的确切划分，论文有陈述，但此处未与第二来源比对确认。

## Domains

机器人学——在两个物理平台上做真实机器人桌面操作，所报告的结果全部来自物理 rollout，而非仿真。

## Evaluation

策略以任务成功率计分，另加由人类依任务完成谓词标注的逐原子 **Process Success Rate（PSR）**。两项派生指标用来分开失败源：

- **Atomic Score（AS）** — 某任务所需各原子的 PSR 均值，用来估计策略对该任务各组成要素的掌握程度。
- **Compositional Failure Share（CFS）** — 任务失败中无法用弱原子解释的那一份，按 `max(0, AS(X) − PSR(X)) / (1 − PSR(X))` 计算。CFS 高，说明失败来自组合，而非原子能力缺失。

评测对每个任务使用 10 个共享的物理测试种子，并以掩膜引导的物体摆放保证初始状态可复现。五个策略共完成 **2,700 次物理 rollout**：Pi0.5、Motus、LingBot-VLA、GROOT N1.6 与 SmolVLA——全都是视觉-语言-动作通用操作策略。

报告的头条结果：Pi0.5 最强，在 Franka 赛道的运动原子上成功率 46.2%、指令原子上 94.3%，但在留出的组合任务上只有 15.8%，尽管其 Atomic Score 达到 83.3%——原子上的强表现并不迁移到组合上。各策略中最难的运动原子是倾倒与铰接物体开合。

## Typical Duration

`TODO(reference)` — 所查来源报告了 rollout 次数（每任务 10 个种子、合计 2,700 次），但未给出单回合的 wall-clock 时间或时序长度。

## Main Contribution

一个真实世界 benchmark：把操作分解为运动原子与指令原子，把原子评测与留出的组合评测配成一对，并配两项诊断指标（Atomic Score 与 Compositional Failure Share），用来区分「原子技能弱导致的失败」与「组合复用能力有限导致的失败」。

## Key Design Ideas

- 把桌面操作分解为两族正交的原子——运动原子（手臂做什么）与指令原子（语言指定什么）——而不是一张扁平的任务清单。
- 只在原子任务上微调策略，使组合任务真正处于留出状态。
- 以人工标注的逐原子 Process Success Rate 作为聚合指标的基础，而不是只用二值的任务成功。
- Compositional Failure Share 作为显式的归因指标：它先把弱原子已经能预测的那部分失败减掉。
- 单臂与双臂两条赛道成对设置，结果按本体分别报告。
- 掩膜引导的物体摆放与共享的测试种子，让真实机器人评测可复现。
- 演示数据与评测 rollout 数据一并公开。

## Strengths

- 大规模真实机器人评测（2,700 次物理 rollout），而非仿真迁移（论文）。
- 直接把「总分混淆」问题变成可测：AS/CFS 这一对指标让人说得清组合任务*为什么*失败（论文）。
- 组合任务的留出由微调协议强制保证，而不是假定成立（论文）。
- 两种本体并行评测，单臂结果不会想当然地推广到双臂（论文）。

## Limitations

- 作者指出，该 benchmark 受制于真实机器人评测与逐策略微调的成本，且评测仍然费人力（过程成功要靠人工标注）。
- 覆盖面不含可变形物体操作、工具使用、移动操作与高度长时程的任务（论文）。
- `Repository note:` 原子分类法由 benchmark 设计者自行拟定；论文并未证明这些原子是桌面操作的极小或完备基底，因此 AS 的意义完全取决于所选的这套分解。
- `Repository note:` 所查来源未报告单回合时长与 token/算力预算。

## Related Works

- [VLA-Arena](./vla-arena.md) — 同样沿结构化难度轴评估 VLA 操作策略，但在仿真中而非真实硬件上。
- [ManipBench](./manipbench.md) — 用选择题探测 VLM 的底层操作推理，而非物理 rollout。
- [RoboFAC](./robofac.md) — 互补的失败归因视角：分析并纠正出错的操作 trajectory。
- [T-Eval](./t-eval.md) — 同样的分解立场（子过程分别计分而非只给一个总分），应用在工具使用上。
- [CFDLLMBench](./cfdllmbench.md) — 另一个层级为嵌套而非并列的 benchmark，因而呈现出天花板形状的能力画像。
