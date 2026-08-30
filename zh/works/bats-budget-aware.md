# BATS / Budget Tracker (2025)

> [English](../../works/bats-budget-aware.md) | **简体中文**

> **首次公开：** 2025-11-21 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2511.17006)

## Overview

一项研究：当工具增强型 agent 在明确的工具调用预算下做 scaling 时会发生什么。出发点是一个反常现象——单纯把预算调高并不管用，因为 agent 根本不知道自己还剩多少。工作贡献了一套把 token 与工具消耗折算到同一尺度的统一计价指标、一个把剩余预算显式告诉 agent 的轻量插件 Budget Tracker，以及一个据此调整规划与验证策略的框架 BATS。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 面向网页搜索、对话与编码 agent 的预算约束研究，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2511.17006>
- **Code:** <https://github.com/google-research/budget-aware-agent>
- **Venue:** 已被 COLM 2026 接收。arXiv v1 为 2025 年 11 月，v2 为 2026 年 8 月。

## Summary

工具增强型 agent 的测试期 scaling 与单纯扩推理 token 不同：一次工具调用是对环境施加的动作，而不只是多想一会儿。论文的起点是一个反面观察——只把工具调用预算调高，性能并不会跟着涨，因为 agent 始终不知道自己还剩多少，很快就见顶。由此引出两项干预。Budget Tracker 是一个插件，在每一轮迭代开始时把各工具已用与剩余的预算注入 agent 的上下文，并附上一份说明不同预算档位下该怎么做的策略指引；它刻意做得极简，而论文的大部分增益恰恰来自它。BATS 在这份「预算意识」之上再加两件事：规划模块维护一棵树状清单，其广度与深度随剩余预算调整；验证模块在 agent 提出候选答案后逐条约束地反向核查，并根据预算状态决定 CONTINUE、PIVOT 还是 SUCCESS，转向时把已有轨迹压缩成摘要。为了让这些比较站得住脚，作者把 token 与工具调用统一到同一种计价上，据此画出成本—性能的 scaling 曲线，而不是在固定预算下比准确率。

## Tasks

主评测对象是网页搜索 agent：**BrowseComp（1,266 道网页浏览题）**、**BrowseComp-ZH（289 题）**，以及 **HLE-Search（从 Humanity's Last Exam 中精选的 200 题子集）**。附录把研究扩展到对话 agent 的 **τ²-bench 零售子集（114 个任务）** 与编码 agent 的 **SWE-bench Verified（500 个任务）**。

工具调用预算是自变量，按每种工具取 **10、30、50、100** 四档；τ²-bench 用 10、30、50 的全局预算，SWE-bench Verified 用 50、60、70。

## Domains

不指派任何规范领域。受评场景是网页浏览、零售对话与软件问题修复；HLE-Search 虽取自 Humanity's Last Exam，但论文没有给出这 200 题子集的学科构成，因此没有哪个切片既可辨识又有明确规模。本工作的贡献是一套成本度量与预算意识方法学，而不是科学或工程任务集。

## Evaluation

统一计价指标为 **`C_unified(x, π) = c_token(x, π) + Σᵢ cᵢ(x, π)·Pᵢ`**——token 按各厂商官方价计费，每种工具的调用次数则按 **搜索 API 调用与网页浏览动作统一每次 0.001 美元** 计价。正是有了单一计价，论文才能画出成本—性能 scaling 曲线、并就 Pareto 前沿展开讨论，而不是在名义上相等的工具预算下比准确率。

骨干模型为 **Gemini-2.5-Flash**、**Gemini-2.5-Pro**（thinking 预算设为 1024 token）与 **Claude-Sonnet-4**，附录另加 Gemini-3-Flash-Preview。

已报告的结果：在 **BrowseComp、预算为 100 时，BATS 达到 24.6% 准确率，而 ReAct 为 12.6%**。更锋利的是效率那一组——**仅用 Budget Tracker、预算为 10 时即达到 12.8%，追平 ReAct 在预算 100 下的 12.6%**，同时**少用 40.4% 的搜索调用、19.9% 的浏览调用，总成本降低 31.3%**。论文报告 BATS 在各预算档上都优于并行多数投票基线，且能在相当或更低的成本下取得更高准确率。

## Typical Duration

预算本身就是被评估的变量，而非一项固定设置：每种工具 10–100 次调用，成本以上述「token 加工具」的统一计价衡量。论文不施加墙钟预算。`TODO(reference)` — 每任务的绝对墙钟时间与 token 总量未列表。

## Main Contribution

为工具增强型 agent 确立了一种把 token 与工具调用一并计价的单一货币，并据此完成了作者所称的首个针对预算约束 agent 的系统性研究——外加一个发现：主要收益并非来自更聪明的搜索策略，而仅仅来自把「还剩多少预算」告诉 agent。

## Key Design Ideas

- 统一计价是使一切成立的前提：没有单一货币，「多调几次工具」与「多花些 token」之间无法折算，scaling 曲线也就画不出来。
- Budget Tracker 刻意做得极简——注入一行已用/剩余，外加一份策略指引——因而成为一次干净的检验：单靠「知情」本身能解释多少增益。
- 预算条件被接在两个不同的决策点上：规划要铺多宽多深，以及在给出候选答案后是 CONTINUE、PIVOT 还是 SUCCESS。
- 转向时把轨迹压缩成摘要而非丢弃，因此改变方向不会连带把已花掉的预算也一并作废。
- 报告的是 scaling **曲线**而非单点准确率，预算意识的效应因而表现为斜率变化，而不只是某一点上的提升。
- 附录把结论延伸到对话与编码 agent，用以检验这一发现是否只属于网页搜索。

## Strengths

- 头条发现是对该领域默认假设——预算越多性能越好——的一个反面结果，而论文把它放在最前面讲。
- 效率那组对比（用十分之一的预算追平基线准确率）比「同等预算下提高准确率」是更强的论断形式。
- 成本指标被明确写出，连每次调用的价格也一并给出，因此换一套定价即可重算。
- 最简单的干预被如实报告为增益的主要来源，而不是被埋在更复杂的框架之下。
- 代码在 Google Research 的仓库下公开，工作本身也经过 COLM 2026 的同行评审。
- 三个骨干模型、三类 benchmark，附录另有两种 agent 场景。

## Limitations

- 每次调用 0.001 美元是一个假定的均价，而非实测成本；关于 Pareto 前沿的结论对它敏感，而真实的搜索 API 与浏览开销并不相同。
- 成本只涵盖 token 与工具调用。墙钟时间、GPU 时间与显存——恰恰是科学与工程类 agent 工作中占大头的那几种货币——都未建模。
- 作者指出 HLE-Search 的题目通常更短、可核查的细节更少，这限制了验证模块在那里能起的作用。
- 每任务的绝对墙钟与 token 总量未列表（上文记为 `TODO(reference)`）。
- 预算意识由提示词注入实现，因此该机制的可靠性取决于模型的指令遵循程度，并非由 harness 强制保证。
- Repository note: 主要产物是一个方法加一套成本指标，而非任务集。本卡片收录它，依据是那套指标与那项系统性成本—性能研究属于评估方法学贡献；BATS 框架本身则是一个系统。
- Repository note: 这里的预算是**给定**的约束、要求 agent 遵守，而不是**预测**出来的量。论文并不在动作执行前估计它会花多少，而这正是 topic 页上 profile 方向所指的缺口。

## Related Works

- [CATP-LLM](./catp-llm.md) — 成本感知的工具规划，把工具执行成本与性能一并权衡，学的是规划策略，而非确立一套成本计价。
- [CostBench](./costbench.md) — 把预算感知做成 benchmark，成本直接计入分数，并报告静态与动态之间的稳健性落差。
- [R³-Bench](./r3-bench.md) — 在题组之间分配共用预算，并对照由模型自身响应曲线构造的 oracle 校准。
- [AI Research Preference Models](./ai-research-preference-models.md) — 预测式的对应物：不是告诉 agent 还剩多少预算，而是在动作执行前预测某个候选要花多少。
- [SimulCost](./simulcost.md) — 科学场景下的成本感知评估，货币是仿真算力而非工具调用。
