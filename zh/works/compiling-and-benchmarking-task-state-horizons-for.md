# RoboGraphBench (2026)

> [English](../../works/compiling-and-benchmarking-task-state-horizons-for.md) | **简体中文**

> **首次公开：** 2026-08-08 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.08036)

## Overview

一个 benchmark 与任务编译器（RoboGraph），评估 agentic 基础模型作为长 horizon 具身任务的高层规划器，并以 *task-state horizon*（TSH，任务状态视界）刻画难度——即 agent 在一条轨迹上必须跟踪、维护、探索并更新的、与任务相关的状态转移的跨度。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用具身高层规划 benchmark（家居操作/导航）；评估的是通用机器人中的状态跟踪，而非某项科学/研究活动。

## Links

- **Paper:** https://arxiv.org/abs/2608.08036
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

该工作指出，现有长 horizon 机器人 benchmark 主要用动作序列长度与子任务复杂度刻画难度，却忽视了一个不同的挑战：agent 必须跟踪由其自身探索和环境动态共同诱导、且不断演变的、与任务相关的世界状态。作者把这一点形式化为 *task-state horizon*（TSH），并提出 RoboGraph——一个机器人任务编译器，它把空间与时间上的因果状态转移依赖（包括执行中因意外失败与干预而诱导的依赖）翻译成可执行的符号图。基于 RoboGraph，作者发布了一个含 588 个 episode、跨 84 个场景、覆盖不同 TSH 的 benchmark，并在语义（符号）与视觉两种闭环环境中评估 15 个 agentic 模型。

## Tasks

跨 84 个场景的 588 个家居操作与整理 episode，分为桌面设定（57 个场景的 399 个 episode）与室内导航设定（27 个场景的 189 个 episode）；报告的任务主题包括化妆品收纳、书桌整理、餐桌整理、食品打包与冰箱调料摆放。每个场景产生一个基线加六种干预条件（动作失败、状态回退、子目标回滚、错误移位、新增遮挡、新增物体），共得 588 个。RoboGraph 把每个任务编译成一张编码状态转移依赖的符号场景图；论文报告场景图平均含 18.4 个节点、21.8 条边、6.1 个被遮挡节点与 14.3 个子目标。

## Domains

Robotics — 面向机器人操作与室内导航的具身高层规划，在桌面与厨房仿真器中评估。

## Evaluation

统一的闭环评估 harness，每个 episode 最多 100 步；成功要求在步数预算内达成目标谓词并发出 "stop" 动作。使用两种环境模式：语义模式将场景图以文本观测呈现、不作视觉渲染；视觉模式对桌面任务用 RoboTwin 2.0 仿真器（三视角 RGB）、对室内厨房导航用 RoboCasa 仿真器。报告指标包括任务成功——Success Rate (SR) 与 Success weighted by Symbolic Action Length (SSAL)——五个状态管理指标，按维护（Action Executability Rate、Redundant Action Rate）、探索（State Exploration Gain、Action-Distance Reduction Rate）与更新（Intervention Recovery Rate）分组，另加恢复指标 F1@Recovery Detection 与 Accuracy@Recovery Grounding。

## Typical Duration

闭环 episode，每个最多 100 步。未报告每任务的 wall-clock 时间或 token 预算（`TODO(reference)`）。

## Main Contribution

引入 task-state horizon（TSH）作为一个区别于动作序列长度的长 horizon 难度轴，并给出 RoboGraph——一个把空间/时间因果状态转移依赖（包括由失败与干预诱导的依赖）转成可执行符号图的编译器，以及一个含 588 个 episode 的 benchmark，用于度量 agent 性能如何随 TSH 变化。

## Key Design Ideas

- **task-state horizon（TSH）** 分解为三个可度量维度：`H_maintain`（获取一条时间依赖事实与其最后一次使用之间的最大步数）、`H_explore`（暴露空间依赖事实所需的最大视野扩展动作数）与 `H_update`（在 oracle 解中被外生事件失效的事实数）。
- **RoboGraph 编译器** 把状态转移依赖翻译成可执行的符号图，使任务能以受控的 TSH 构建。
- **干预条件**——每个场景注入六种扰动（动作失败、状态回退、子目标回滚、错误移位、新增遮挡、新增物体），以诱导状态更新并测试恢复。
- **双环境模式**——纯符号（语义）模式与视觉闭环模式（桌面用 RoboTwin 2.0、室内用 RoboCasa），共用一套评估 harness。
- **状态管理指标套件**，将维护、探索与更新行为分开，另加显式的恢复检测与 grounding 指标。

## Strengths

- 隔离出长 horizon 难度的一个状态跟踪维度——它是基于动作长度的 benchmark 无法直接度量的——并以定量的 TSH 子度量将其可操作化。
- 在符号与视觉两种闭环设定下评估同一批任务，将规划/状态跟踪与感知分离。
- 系统性地注入失败与干预以探测恢复，并配专门的恢复检测与 grounding 指标。

## Limitations

- 任务为仿真中的家居操作与整理（RoboTwin 2.0、RoboCasa）；论文未报告真实机器人执行（`TODO(reference)`）。
- 撰写时未在一手来源中找到代码或项目 URL（`TODO(reference)`）。
- Repository note: 该 benchmark 评估的是基础模型的高层符号规划，而非底层机器人控制策略；结论关乎规划器的状态跟踪行为，而非端到端的机器人自主性。

## Related Works

- [CaP-X](./cap-x.md) — 同样评估前沿模型作为机器人规划器，在操作任务的符号/程序抽象之上工作。
- [VIKI-Bench](./viki-bench.md) — 在仿真场景中评估基础模型的具身多机器人规划 benchmark。
- [REFLECT / RoboFail](./robofail.md) — 同样聚焦机器人操作 episode 中的失败与纠正/恢复。
