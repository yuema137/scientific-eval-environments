# PhysRSI-eval (2026)

> [English](../../works/physrsi-eval.md) | **简体中文**

> **首次公开：** 2026-10-19 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.26848)

## Overview

PhysRSI-eval 测的是物理层面的递归自我改进：一个控制仿真双臂机器人的 LLM agent，在尝试失败后修改自己的代码、工具、技能和笔记，能不能把一项操作任务越做越好。18 个 RoboDojo 任务每个先做一次首次尝试，再给最多 17 轮改进，每轮都是一次完整的物理尝试。结果按五个维度打分：首次尝试表现、提升的效率、成功、预算，以及从失败中改进的程度。论文随后把每个维度和公开基准分数做关联，并用消融实验检验持久工作区里到底是哪些内容带来了改进。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 通用机器人操作基准；被评测的 agent 做的是双臂操作，不属于科学或研究活动。

## Links

- **Paper:** [Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848)，2026 年技术报告（Galbot Team）。
- **Full text:** <https://arxiv.org/html/2610.26848v1>
- **Code:** <https://github.com/PhysRSI-Eval/PhysRSI-Eval-code>（Apache-2.0 许可的评测循环参考实现，带 Codex 客户端；README 说明它只覆盖 18 个任务中的 4 个，来自泛化实验）
- **Project:** <https://physrsi-eval.github.io/>
- **Venue:** arXiv 预印本（cs.RO，2026）

## Summary

K0 轮是上下文内尝试：agent 使用共享的机器人工具，没有工作区，每个任务跑三次。从 K1 到 K17，agent 每轮基于一个持久工作区做一次物理尝试，工作区里有策略代码、工具、技能和笔记。每轮结束后它会拿到原生分数、成功标记和失败原因，然后在机器人动作被禁用的情况下修改工作区。一条改进链在第一次原生判定成功时停止。机器人动作是目标位姿调用，每次平移不超过 5 cm、旋转不超过 0.35 rad，执行 1–5 个控制步，返回一份状态 JSON 和三张相机图像。GPT 系列在 Codex CLI 中运行，Claude 系列在 Claude Code 中运行。

## Tasks

18 个来自 RoboDojo 的双臂操作任务，按官方成功率划成六个难度层（D1–D6），每层取三个，覆盖 RoboDojo 的五个类别（Precision、Long-Horizon、Memory、Open、Generalization）。例子有 `insert_key`、`pour_liquid_into_cup`、`push_T`、`play_Xylophone` 和 `organize_table`。每轮 300–1300 步，频率 25 Hz。主评测使用 layout 0、seed 0，每个任务一条改进链。论文没有说明 RoboDojo 一共有多少个任务。

## Domains

机器人学：RoboDojo 仿真中的双臂操作，由 agent 编写的策略代码下发末端执行器目标位姿来控制。论文没有报告实体机器人实验。

## Evaluation

- **维度：** A1 First-Attempt Performance 是 K0 的平均分。A2 Efficiency 是第 1 轮到第 H−1 轮的平均提升相对最终提升的比例。A3 Success 是从首次达到 90% 提升的那一轮开始，之后各轮部分得分的平均值。A4 Budget 是已解决任务上物理预算未用部分的平均比例，不计时间、token 和金钱。A5 Improvement 是 K1 失败、之后被解决的任务所占比例。总分是 A1–A5 等权平均值乘以 100。
- **评分：** 每个任务用 RoboDojo 原生评分器，给出 [0, 1] 之间的分数，以及带分级部分得分的成功判据。论文没有提到 LLM 或 VLM 评审。
- **系统：** GPT-6 Astra、GPT-6.1 Sol、GPT-6 Sol、GPT-5.6 Sol、Claude Opus 5.5 和 Claude Sonnet 5.5 跑全部 18 个任务；Gemini 4 跑 10 个任务，每个任务只有一次 K0，不参与关联分析。
- **结果（Table 1，A1–A5）：** GPT-6 Astra 为 0.3676 / 0.8594 / 0.8509 / 0.8429 / 0.7500，到 K17 解决 15 个任务；GPT-5.6 Sol 为 0.0120 / 0.2247 / 0.1037 / 0.3013 / 0.0556，只解决 1 个。正文给出四个 GPT 系统的总分范围是 13.9–73.4。Claude Opus 5.5 解决 13 个任务，Claude Sonnet 5.5 解决 11 个。`insert_key`、`store_tools_in_toolbox` 和 `swap_blocks` 没有任何系统解决。
- **与公开基准的关联：** 17 个公开基准分数先换成排名，再归成 Spatial、Harness、Perception 和 Coding 四组。在六个系统上，Spatial 与 A1 的 Spearman ρ = 0.94，Perception 与 A3、A5 的 ρ = 0.94；Coding 在每个维度上都是 ρ ≤ 0.37。经过 Benjamini–Hochberg 校正后，最小的 q 是 0.11。论文把这些关联当作候选瓶颈（"Physical Barrel Hypothesis"），而不是因果上的必要条件。
- **工作区消融（GPT-6 Astra，六个任务，每个两条链）：** 后期轮次（K4–K6）的成功次数，完整循环是 15/36，去掉历史是 3/36，去掉评分器反馈是 5/36，去掉之前的图像是 12/36。
- **迁移：** 冻结的 K6 工作区在没有修改、没有反馈的情况下，放到没见过的布局上，60 次尝试成功 25 次。在三个首次运行的案例里，借用另一个任务的工作区能让第一次成功来得更早（例如 Cover Blocks，Sonnet 5.5，从 K9 提前到 K1）。

## Typical Duration

每轮最多 4,200 s 推理时间，修改工作区的窗口是 1,800 s（GPT 系列）或 600 s（Claude 系列），每个任务最多 17 轮改进。论文没有报告 token 数、美元成本和总墙钟时间。

## Main Contribution

定义了在固定交互预算下描述物理自我改进的五维画像，把首次尝试做得好和失败后能改进这两种能力分开。对持久工作区的消融实验说明了是哪些保留下来的信息推动了后期轮次的成功。

## Key Design Ideas

- 每一轮改进都算一次完整的物理尝试，并用原生评分器判定，所以衡量的是实际执行的行为，而不是改过的代码。
- 首次尝试、提升速度、最初失败任务的恢复分成不同维度，因为同一个系统在各维度上的排名可能不同。
- 把工作区冻结后搬到没见过的布局或其他任务上，检验学到的东西能不能迁移。

## Strengths

- 消融实验把历史、评分器反馈和之前的图像分别去掉；去掉历史时，成功次数从 15/36 降到 3/36。
- 迁移测试用冻结的工作区在没见过的布局上进行，与任务内的改进分开。
- 作者如实报告了关联分析的小样本限制，包括没有一个相关性能通过多重比较校正。

## Limitations

- 作者列出的局限包括：只有六个系统，每个任务只有一条改进链，能力分数没有独立验证。K0 的重复运行无法估计整条改进链之间的波动。
- 作者指出，Budget 和 Improvement 是在条件任务集上算的，不同系统的任务集不一样。
- 消融和冻结工作区测试只覆盖 GPT-6 Astra 和六个任务，跨任务迁移只有三个案例。
- GPT-6 Astra 在主运行中解决 15 个任务，在不带 "supplementary hints" 的运行中解决 13 个；论文没有说明这些提示是什么。
- 论文说 Gemini 4 跑到了 "through K20"，而主协议设定 H = 17，也没有说明它的画像用的是哪一轮。
- Repository note: 项目页把 A4 标为 "Stability"，列出的 A4 和 A5 数值也与论文 Table 1 不同（例如 GPT-6 Astra 为 0.8405 和 0.7349，论文是 0.8429 和 0.7500）；本卡片以论文为准。

## Related Works

- [RobotAgentBench](./robotagentbench.md) — 同样测试 coding agent 在机器人控制中的递归自我改进，那里是家务基准中的一种配置。
- [EmbodiedCLBench](./embodiedclbench.md) — 同样测量具身任务中从先前尝试里学习的能力，经验以上下文内轨迹或书面技能摘要的形式保留。
- [CaP-X](./cap-x.md) — coding agent 编写机器人控制程序，按抽象层级比较，而不是按改进轮次比较。
