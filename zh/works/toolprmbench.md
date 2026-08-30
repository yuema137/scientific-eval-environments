# ToolPRMBench (2026)

> [English](../../works/toolprmbench.md) | **简体中文**

> **首次公开：** 2026-01-18 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2601.12294)

## Overview

ToolPRMBench 是一个评估面向工具使用 agent 的 process reward model（PRM）的 benchmark，它把 agent trajectory 改写为 step 级样例，要求在正确动作与貌似合理的错误动作之间做出选择。它从四个 tool-use benchmark 中抽取 987 个这样的样例，并在 step 级判别准确率上对 17 个 LLM、通用 PRM 与工具专用 PRM 进行排名。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2601.12294>
- **Code:** <https://github.com/David-Li0406/ToolPRMBench>

## Summary

ToolPRMBench 针对工具使用场景下缺乏系统性 PRM 评估 benchmark 的问题，已有的 PRM benchmark 面向通用推理或 web agent，而非结构化的工具调用。它把 ToolTalk、GTA、BFCL 与 ToolSandbox 的 trajectory 转换为单决策 step 样例，每个样例包含交互历史、一个正确动作、一个貌似合理的错误动作以及可用工具 metadata，再通过三判官 LLM 验证流程进行过滤。在由此得到的排行榜上，ToolPRM-GRPO 以 78.6% 的平均准确率位居首位，其后是 Claude-4.5-haiku 的 75.1% 与 GPT-5 的 74.4%，而四个通用 PRM 落在 49.2–52.8% 区间。

## Tasks

按附录的细分统计共 987 个 step 级样例——BFCL 354 个、ToolSandbox 429 个、GTA 118 个、ToolTalk 86 个——每个样例都是交互历史、一个选中的正确动作、一个被拒绝的错误动作以及相应工具 metadata 构成的四元组。样例由两种互补策略生成：offline 采样把策略约束在 golden trajectory 前缀上并只对单个 step 重新采样，使错误保持在局部；online 采样让策略自由生成完整 trajectory，仅保留未通过源 benchmark 结果指标的 rollout，并由标注 LLM 定位第一个错误 step。已发布的划分为 542 训练 / 445 测试，其中 GTA 与 ToolTalk 不贡献训练样例。

## Domains

工具使用 agent 的交互，覆盖信息检索、多步推理与交互式工具执行，运行在 ToolTalk、GTA、BFCL 与 ToolSandbox 的 API 界面之上。

## Evaluation

- **强制二选一 step 准确率。** 每个样例给出交互历史、工具描述与两个候选动作，模型需指出其中正确的那一个；准确率为回答正确的样例占比。
- **分子集准确率与平均准确率。** 在 GTA、ToolTalk、BFCL 与 ToolSandbox 上分别报告分数，并给出四者的非加权平均。
- **面向 reward-guided search 的元评估。** 被评测模型在 GTA 与 BFCL 上作为 reward function 用于 n = 8 的 best-of-n 搜索，其 benchmark 准确率与由此带来的增益相关联；准确率低于 50% 的模型常常带来负增益。
- **成本分析。** 以每次调用的推理成本估计值对平均准确率作图，API 模型采用官方 API 定价，开源模型采用 Together.ai 定价。
- **报告结果（表 2）。** ToolPRM-GRPO 以 78.6% 的平均准确率领先，其后为 Claude-4.5-haiku 的 75.1%、GPT-5 的 74.4% 与 Gemini-2.5-flash 的 73.2%；最强的开源 LLM 是 Qwen3-14B 的 63.0%，四个通用 PRM 分布在 49.2–52.8%，且未报告人类表现 baseline。

## Typical Duration

每个样例是单个决策 step 上的判断，而非一次 agent rollout，因此没有给出每样例的 wall-clock、step 或 token 预算。未以 wall-clock 形式报告；论文转而报告每次调用的推理成本估计值。

## Main Contribution

一个用于系统性评估工具使用场景下 PRM 的大规模 benchmark，把取自四个 tool-use benchmark 的 step 级强制二选一样例，与覆盖 17 个 LLM、通用 PRM 及工具专用 PRM 的排行榜结合起来。

## Key Design Ideas

- step 级样例格式：交互历史、一个选中动作、一个被拒绝动作以及可用工具描述。
- 沿 golden trajectory 前缀的 offline 采样用于隔离单 step 错误，配合在失败 rollout 上的 online 采样以捕捉传播开来的多 step 失败。
- 由 GPT-5、Gemini-3-flash 与 Claude-4.5-haiku 构成的多 LLM 验证，保留一致通过的样例，丢弃一致否决的样例，并把投票分歧的样例交由人工验证。
- 四类模型并列评分：API 型 LLM、开源 LLM、通用 PRM，以及在该 benchmark 自身 BFCL 与 ToolSandbox 训练划分上训练出来的工具专用 PRM。

## Strengths

- 成对强制二选一的构造方式隔离出 step 级判别信号，而仅看结果的 benchmark 无法把它从最终任务成功中分离出来。
- 把 offline 与 online 采样分开，使注入的局部错误与自然传播的错误得以区分，PRM 的失效模式因此保持可读而不被聚合掉。
- 面向 best-of-n 搜索的元评估把 benchmark 准确率与下游搜索收益联系起来，其中包括准确率低于 50% 的判官会主动损害性能这一发现。

## Limitations

- Repository note: 正文给出 984 个样例总数，而附录的细分统计无论按四个子集还是按训练 / 测试两列汇总都是 987；本卡片采用附录数字，因为它是内部自洽的那一个。
- Repository note: 三个 ToolPRM 变体只在取自 BFCL 与 ToolSandbox 的 542 个样例上训练，因此它们在表 2 的四个子集分数中有两个属于 in-distribution，而其他所有被评测模型在四个子集上都是 out-of-distribution；论文对 in-distribution 与 out-of-distribution 的对比另行报告。

## Related Works

- [AgentBoard](./agentboard.md) — 同样在端到端任务成功之下对 agent 进展评分，但走的是在 agent 自身运行中穿过 subgoal 标注的路径，而不是检验一个外部 reward model 能否在单个 step 上挑出正确动作。
- [TRACE](./trace.md) — 同样评估 trajectory 而非最终答案，但对已完成的 trajectory 按质量维度打分，而不是对给单个 step 打分的判官本身做 benchmark。
