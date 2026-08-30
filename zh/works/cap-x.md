# CaP-X (2026)

> [English](../../works/cap-x.md) | **简体中文**

> **首次公开：** 2026-03-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2603.22435)

## Overview

CaP-X 评测并改进面向机器人操作的编码 agent：agent 通过合成并执行「组合感知与控制原语」的程序来控制机器人，在 CaP-Bench 中按抽象、交互与感知接地的层级评估——12 个前沿模型的表现随人工设计的抽象而提升、随这些先验被移除而下降。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 能力探针，agent 本身并不执行科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2603.22435>
- **Project:** <https://capgym.github.io>
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

CaP-X 把 Code-as-Policies 范式打包成一个可测量的框架，含四部分：CaP-Gym（交互环境）、CaP-Bench（benchmark），以及两个方法——免训练的 CaP-Agent0 与带可验证奖励的 CaP-RL。Benchmark 核心含 7 个操作任务（从举方块到双臂交接），并扩展 30 个 LIBERO-PRO 与 2 个 BEHAVIOR 任务，置于 187 任务的 CaP-Gym 套件内（正文）。编码 agent 以多轮方式工作，配结构化执行反馈与视觉差分。在 12 个模型上，一致的趋势是对设计者脚手架的依赖：人工设计的抽象层被逐层剥去，成功率随之下降。人类专家在底层原语层级上单轮平均成功率 88.5%；配套方法在模拟与真实 Franka Panda、AgiBot G1 平台上于若干任务恢复到人类级可靠性。

## Tasks

交互式代码合成回合：agent 编写调用感知/控制原语的 Python 程序、执行并据反馈修订；benchmark 评估在模拟中（Robosuite、LIBERO-PRO、BEHAVIOR），每个任务、每个抽象层级 100 次试验；配套方法另在真实机器人上运行。

## Domains

机器人学——经由 agent 编写程序的机器人操作控制，在模拟中评测，并将配套方法迁移到物理 Franka Panda 与 AgiBot G1 平台。

## Evaluation

- 每个任务、每个抽象层级 100 次试验的成功率；零样本 pass@1；在相同环境下与人类专家手写程序对照（人类在底层原语层级平均 88.5%）。
- **报告。** 表现随人工设计的抽象而提升、随先验被移除而下降（摘要）；项目页：前沿模型零样本 >30%；CaP-RL 把 Qwen2.5-Coder 从 20% 抬到 72%。

## Typical Duration

每个操作任务一段「合成-执行-修订」的多轮回合。

## Main Contribution

测量编码 agent 控制机器人时对脚手架的依赖：分层级的抽象量化了当前「LLM 能控制机器人」有多少建立在人工设计的原语之上。

## Key Design Ideas

- 抽象分层级把设计者先验变成实验变量，而非隐藏常量。
- 结构化执行反馈与视觉差分给 agent 以机器人专家会有的可观测性。
- 人类专家手写程序在相同条件下锚定上限。

## Strengths

- 分层级设计得到的是关于脚手架的因果式结论，而非仅一张排行榜。
- 覆盖 12 个当前前沿与开源模型，并把配套方法迁移到真实机器人。

## Limitations

- Repository note: 卡片依据 arXiv 摘要、正文与官方项目页编写（2026 年 8 月）；无法核实发表信息（HTML 显示 ICML 排版，表明是投稿而非录用）。Benchmark 与方法是并列贡献；任务数出自正文。代码仓库的确切 URL 无法从已获取来源核实。

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — 同样让 LLM 产出可执行的机器人行为，走对话与路径点而非程序。
- [ManipBench](./manipbench.md) — 同样考底层操作能力，以静态推理而非执行代码来测量。
- [BadRobot](./badrobot.md) — 同样评估 Code-as-Policies 式的具身栈，只是对抗性地。
