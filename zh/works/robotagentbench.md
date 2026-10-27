# RobotAgentBench (2026)

> [English](../../works/robotagentbench.md) | **简体中文**

> **首次公开：** 2026-10-26 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.34649)

## Overview

RobotAgentBench（RAB）要回答的问题是：家用机器人能不能自己把事办成，而不只是会不会抓取和摆放物体。它在 Isaac Sim 里把一套真实住宅重建成 50 种家居布局，把单独运行的 VLA 和世界动作模型（WAM）策略，与在同一套规划、执行、验证框架下工作的 coding agent 放在一起测试。打分分两层：任务层看五种能力（操作、任务发现、情境推理、失败恢复、鲁棒性），场景层看四个把这些能力串起来的开放式场景。表现最好的配置在任务层平均得 48.5 分，开放式场景得 15.4 分；单独运行的策略最高只有 18.0 分。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 通用家用机器人基准；被评测的策略和 agent 做的是家务操作和导航，不属于科学或研究活动。

## Links

- **Paper:** [RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)，2026 年预印本（Aether AI、UC San Diego、UC Davis）。
- **Full text:** <https://arxiv.org/html/2610.34649v1>
- **Code:** <https://github.com/AetherLabsAI/RobotAgentBench>（评测代码采用 Apache-2.0；团队自制的资产和任务数据采用 CC BY 4.0）
- **Assets:** <https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-assets>
- **Training data:** <https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-TrainingData>
- **Model:** <https://huggingface.co/AetherLabs-AI/InternVLA-A1.5-RAB>
- **Project:** <https://aetherlabsai.github.io/RobotAgentBench/>
- **Venue:** arXiv 预印本（cs.RO，2026）

## Summary

环境由一条半自动的 real-to-sim 流程搭建。coding agent 按真实住宅的测量数据和照片检索或重建 3D 资产，人工审核视觉和物理上是否逼真，再把真实遥操作演示放回仿真里回放，用来校准几何形状和物理参数。机器人是带移动底盘的 AgiBot G1；基准不提供规划好的路线，也不提供自动导航动作。每个系统都拆成规划器、执行器、验证器三部分，每部分可以是基于代码（C）、学习得到的 VLA/WAM 策略（L）、两者混合（H），或者不存在（–）。单独运行的策略、完全基于代码的 coding agent（C/C/C）、各种混合配置，以及带递归自我改进（RSI）的 C/C/C 配置，都在同一批任务上评测。在 RSI 设置下，coding agent 根据执行反馈创建、改进并复用控制工具，共迭代十轮，有效的改进会保留下来。

## Tasks

基础是 90 个原子家务任务，比如推、拉、双臂配合和移动操作。它们组合成 18 个短程任务（例如 “Prepare coffee”“Wipe the table”）和 8 个长程任务（例如 “Prepare a meal”“Find and pack an item”）。任务层另有四个发现场景、四种情境推理设定（饮料、零食、垃圾和沙发物品的选择）、五种失败恢复变体（四种抓空、一种杯子倾倒），以及六种加入人为干预和光照变化的鲁棒性变体。场景层有四类开放式场景：准备晚饭、招待客人、准备出门和整理房间。每个任务或场景都在 30 个不同实例上评测。基准还提供一套 101.8 小时的仿真数据集用于训练策略：每个原子任务和短程任务 50 条演示，每个长程任务和开放式场景 10 条。

## Domains

机器人学：在仿真 AgiBot G1 上做家居移动操作，为长程和开放式家务目标做任务规划，自主导航，失败恢复，以及 VLA/WAM 策略评测。sim-to-real 对比在实体机器人上跑了一部分任务。

## Evaluation

- **任务层：** Discovery 是在接触次数预算内（N 个目标给 N+2 次接触）碰到的目标物体比例。Reasoning 只要碰到正确的目标就算分，不要求抓起来。Manipulation、Recovery 和 Robustness 用任务进度分，由各任务专用的评分规则根据当前物理状态计算。Average 是五项能力分的平均值。
- **场景层：** Open-Ended 是一个场景里所有任务检查点的最终进度分。Task Coverage、Task Progress、Recovery Rate 和 Stagnation 用来描述行为。仿真时间连续 120 s 没有进度提升时回合结束；每个回合最多 200 次模型响应，每次工具调用最多 600 个控制步。论文没有提到在打分中使用 LLM 或 VLM 评审。
- **系统：** 8 个 VLA（π0.5、Xiaomi Robotics-1、InternVLA-A1.5、MolmoAct2、LingBot-VLA2、HY-VLA、Galaxea G0.5、X-VLA），3 个 WAM（τ0、OpenWAM-Alpha、LingBot-VA），以及三个 coding agent：Codex（GPT-6 Astra，默认配置）、Claude Code（Opus 5.5）和 Antigravity CLI（Gemini 4 Argon）。
- **结果（Table 1，Average / Open-Ended）：** 单独运行的策略从 3.2 / 1.9（MolmoAct2）到 18.0 / 1.0（InternVLA-A1.5）。完全基于代码的 agent：Codex 31.0 / 8.4，Claude Code 33.3 / 9.2，Antigravity CLI 39.7 / 9.8。Codex 搭配 InternVLA-A1.5：–/L/C 23.3 / 3.7，C/L/– 26.4 / 9.1，C/H/C 48.5 / 15.4。Codex 的 C/C/C + RSI 在第十轮迭代时为 42.3 / 10.8。
- **行为（Table 2）：** InternVLA-A1.5 的 Stagnation 为 88.3，OpenWAM-Alpha 为 84.6，三个 coding agent 在 18.4–33.7 之间。加上 RSI 后，Codex 的 Recovery Rate 从 15.4 升到 38.9，Stagnation 从 33.7 降到 12.3。
- **问题构成（Appendix D.2）：** 在 coding agent 的开放式场景轨迹里，运动可行性问题和执行不到位合计占已识别问题的 82.1%，代码或接口错误占 15.3%。论文说明，这些比例描述的是问题的构成，不是总体错误率。
- **sim-to-real（Table 3）：** 在一组配对的任务和四个场景情境上，Average 从仿真到真实的变化是：InternVLA-A1.5 从 17.8 降到 13.5，OpenWAM-Alpha 从 8.5 降到 8.2，Codex 从 34.2 降到 31.9。项目页说排名保持不变。

## Typical Duration

仿真时间连续 120 s 没有进度、达到 200 次模型响应，或任务完成判定后，回合结束；一次工具调用最多执行 600 个控制步（约 30 s 仿真时间）。论文没有报告 token 数、美元成本和墙钟时间。

## Main Contribution

把单独运行的机器人策略和 coding agent 架构放到同一批家务任务上，并把任务发现、情境推理、恢复和鲁棒性与操作能力分开打分。再用规划器–执行器–验证器的记法，看清分数提升来自哪个部件。

## Key Design Ideas

- 给操作成功率看不出来的能力单独打分：能不能找到目标，能不能根据情境选对物体，能不能从人为制造的失败中恢复。
- 用规划器、执行器、验证器各自的类型描述每个系统，让单独策略、coding agent 和混合系统在同一个维度上比较。
- 让 coding agent 在十轮迭代中保留并改进自己的控制工具，以此测试 harness 层面的递归自我改进。

## Strengths

- 一张表在同样的五项能力和开放式场景上报告了全部 18 种配置。
- 规划器 × 执行器的组合、三个 coding agent 以及 RSI 各轮迭代都有直接对比（Figures 4–6）。
- 评测代码、资产、1,470 个保存好的初始配置、训练数据和一个微调过的策略都已公开。

## Limitations

- 作者指出，开放式场景里的可靠自主仍远未解决；开放式场景最高分只有 15.4。
- 50 种布局全部来自同一套真实住宅。
- sim-to-real 对比中，真实环境得分低于仿真，而且这项对比只覆盖部分任务和三个系统。
- Repository note: 论文没有报告重复运行、方差或置信区间。
- Repository note: 每个 coding agent 只搭配一个基座模型，所以三行 C/C/C 结果分不开 harness 和模型各自的影响。
- Repository note: 论文没有说明 coding agent 在评测时能否联网。

## Related Works

- [CaP-X](./cap-x.md) — 同样让 coding agent 编写机器人控制程序，也迁移到 AgiBot G1，但任务是桌面操作，按抽象层级比较。
- [RoboGraphBench](./compiling-and-benchmarking-task-state-horizons-for.md) — 长程家务规划，在规划层面打分，不由被测系统做物理执行。
- [PhysRSI-eval](./physrsi-eval.md) — 同样测 coding agent 的物理自我改进，在 RoboDojo 操作任务上最多迭代 17 轮。
