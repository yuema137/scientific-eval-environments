# What Process Evaluation of Coding Agents Actually Measures (2026)

> [English](../../works/coding-agent-process-evaluation-levels.md) | **简体中文**

> **首次公开：** 2026-08-24 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.22960)

## Overview

对 coding agent 做过程评估时，通常是让一个 judge（往往是读完整条 trace 的 LLM）指出哪一步起了关键作用。这篇论文认为，这样的判断把三个问题混在了一起：agent 下一步大概会做什么（action 层面）、整次运行是否仍有不确定性或还能挽回（task 层面），以及某一步是否在因果上改变了结果（step 层面）。论文给每个层面配了单独的估计方法，其中 SCAE 是一个基于 replay 的估计器，专门估计 step 层面的因果量。作者用这些估计器分析 coding agent 的 trace，检验现有的过程信号到底在追踪什么。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — 这是针对 coding agent trajectory 的过程评估方法学，任务是通用软件中的文件定位（SWE-bench Verified），不评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.22960>

## Summary

作者把 agent 的执行过程建模为一个结构因果模型（SCM）：每个动作由 policy 加上外生的 Gumbel 解码噪声采样得到，环境返回一个观测，最后把输出的文件集合与 gold 集合比对打分。在三个假设下（上下文可观测、解码噪声是外生的、环境可以 replay），一个前缀的价值可以这样估计：从这个前缀出发让 agent 多次 replay，再把结果取平均；一步的贡献就是相邻两个前缀价值之差。当 agent 的下一步几乎是确定的，replay 无法让这一步发生变化，SCAE 就换上一个替代动作，真实执行它，再 replay 后续过程。把这些估计器用在文件定位 trace 上，结果显示：下一步动作主要跟着执行过程中的信息来源走；不确定性集中在 task 层面；而 full-trace judge 一旦能看到下游结果，就会把责任往后面的步骤推。

## Tasks

499 个从 SWE-bench Verified 派生的文件定位 episode，涉及 12 个仓库（django 最多）。每个 episode 包含一个 issue、一个仓库快照、一条 agent trajectory，以及需要定位的 gold 文件集合。Trajectory 由 Codex CLI 在只读 sandbox 中运行生成，后端为 gpt-5.5-0424-global。Action 层面的分析使用 488 个 episode 中的 7,616 个决策点；step 归因分析使用 38 个实例上的 190 个前缀。

## Domains

软件工程：在开源 Python 仓库中定位与某个 GitHub issue 相关的文件。

## Evaluation

- **结果变量。** SCM 中用的是「是否包含 gold 文件集合」；主实验用的是对 gold 文件的 recall。作者报告，在干预下 recall 会发生变化的实例占 98.6%，而二元成功只有 73.2%。
- **Step 贡献（SCAE）。** 从前缀 τ<sub>1:t</sub> 出发 replay m = 8 条后续，把结果取平均得到 v̂<sub>t</sub>；step 效应为 Δ̂<sub>t</sub> = v̂<sub>t</sub> − v̂<sub>t−1</sub>，所有 step 效应加起来等于 Y − E[Y | q, G]。在 (tool, target object) 分桶上用 4 到 6 次 replay 做熵探测，据此决定用观察式 replay 还是替代动作干预。工具输出从不伪造。
- **Trace。** 在某个 episode 里，如果从第 t 步之前的前缀出发，replay 平均能找回 40% 的 gold 文件，而从第 t 步之后的前缀出发平均能找回 55%，那么第 t 步记 +0.15。论文报告，190 个通过干预估计的效应在 q = 0.10 的 BH-FDR 校正后没有一个显著，所以没有任何单个 step 能被确认。
- **Action 层面。** 用 top-k 准确率、NLL、校准度和有效候选数评估下一步动作预测。一个以信息来源为依据的预测器（直接看上一次工具输出）在首次访问决策上 top-3 准确率为 0.326，而加强版代码图预测器只有 0.058。
- **Task 层面。** 实例身份解释了 replay 残差方差中 ICC = 0.640 的部分，置换零分布对应值为 0.196；action 模型的熵和 replay 方差没有对应关系（ρ = −0.088）。
- **Judge 审计。** 固定 judge 模型和 rubric，只改变是否让 judge 看到下游步骤：在 70 个 episode 中有 59 个，judge 的判定在能看到下游时落到了更靠后的步骤上。Full-trace judge 选中触及 gold 文件的步骤的比例为 0.900，baseline 为 0.413。测试的 judge 有 gpt-5.5、qwen3.6-plus 和 qwen3-coder-plus。

## Typical Duration

用于归因的 1,901 条 replay 后续共耗时 12.7 小时。本卡片所读的正文中没有说明每个 episode 的 agent 步数。TODO(reference)

## Main Contribution

一个测量框架，在 coding agent 的过程评估中把 action 层面的预测、task 层面的不确定性和 step 层面的因果归因分开处理；其中 SCAE 通过 replay 来估计以前缀为条件的 step 效应。作者的结论是：现有过程评估测到的往往是语义相关性，而不是经过确认的因果贡献。

## Key Design Ideas

- 把 step 层面的目标定义为一个以前缀为条件的因果量，这样 step 的功劳有一个不依赖任何 judge 的定义。
- 在可 replay 的环境里真实地重放 agent 来估计前缀价值，而不是让模型去预测结果。
- 只有当解码熵太低、replay 无法让动作发生变化时，才改用真实的替代动作。
- 审计 judge 时只改变它能看到的信息（是否包含下游步骤），从而把对撞偏差（collider bias）和 judge 本身的质量区分开。

## Strengths

- 每个结论都配有零分布或 baseline（置换零分布、随机一致率、代码图预测器）以及置信区间。
- 使用前先检查前提条件：在 100 个动作、每个重复执行 3 次的测试中，环境的可 replay 率为 1.00；没有任何 rollout 触发上下文压缩。
- Judge 审计在三个 judge 模型上重复进行，其中包括一个专门面向代码的模型。

## Limitations

- 只研究了文件定位，结论能否推广到 coding agent 的其他行为还不好说。
- 在可行的 replay 预算下，step 层面的归因统计功效不足：190 个干预估计在 FDR 校正后没有一个显著，所以没有哪个 episode 的关键步骤能被确认。
- 价值只在选定的前缀上估计，所以算出来的 step 贡献其实是对一段步骤的近似，而不是逐步的精确值。
- 解码噪声是否外生、替代动作能否迁移，都无法完全从 trace 中验证；替代动作分支估计的是扰动后 policy 下的效应。
- 三方面的不确定性分解只在一个合成过程上得到验证，而且 agent 操作的对象中只有 46.2% 能对应到依赖图节点上。
- Repository note: arXiv 页面和本卡片所读的论文正文中都没有看到代码或数据链接。

## Related Works

- [SWE-bench](./swe-bench.md) — 文件定位 episode 所用 issue 的来源。
- [AgentProcessBench](./agentprocessbench.md) — 用人工的有效性标签给 step 打分；本文追问的正是这类 step 判断是否反映了因果贡献。
- [Who&When Pro](./who-and-when-pro.md) — 同样要找出对结果负责的那一步，但用的是构造时就确定的失败标签，而不是 replay 估计。
- [Long-Horizon Agent Trajectory Attribution](./long-horizon-agent-trajectory-attribution.md) — 同样把结果归因到 agent trajectory 的某些部分，但归因对象是 trajectory 的组成部分，而不是通过 replay 估计的 step 效应。
