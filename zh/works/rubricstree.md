# RubricsTree (2026)

> [English](../../works/rubricstree.md) | **简体中文**

## Overview

RubricsTree 是面向开放式个人健康 agent 的评估框架。它不再依赖单一的整体式 LLM judge，而是改用一套由专家策划的分层 rubric 分类法——100 余条原子化、临床上可核验的布尔型 rubric——并通过一个感知上下文的自适应路由器，为每条查询只激活相关的那部分 rubric。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 面向消费级健康助手的评估方法学；被评估的任务本身并非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.18203>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

LLM 个人健康 agent 要真正进入临床，卡在一个评估瓶颈上：医生标注可靠却无法规模化，LLM-as-a-judge 能规模化却主观、不稳定，有时还与临床判断相悖。RubricsTree 由一位资深医生主导，以人在环中的迭代流程整理出一套分层 rubric 分类法——一张有向无环图，自宏观能力层经中间子领域，向下收敛到原子化的布尔型叶节点 rubric——整理过程参考了约 4,000 条真实用户查询。评估时，自适应路由器只为当前查询激活相关且自动加权的 rubric 子集。该框架一方面通过与专家小组的元评估得到验证，另一方面也在下游以指令、反馈和训练奖励三种用法接受检验。

## Tasks

N/A — 这是一套评判框架，而非任务套件。元评估使用一份内部数据集，含 532 条真实用户查询，覆盖四类场景（Medical Explanation、Health Data、Advice/Action Plan、Symptoms）并施加受控扰动；下游优化在 HealthBench-Hard 子集（362 条面向用户的查询）上测量，强化学习训练则使用 HealthBench-Consensus。分类法的整理取材于约 4,000 条真实的个人健康 agent 用户查询。

## Domains

Medicine & Health — 面向消费者与临床的健康问答，以用户健康数据与可穿戴传感器指标为依据，rubric 由医生主导的专家小组撰写并验证。rubric 覆盖的场景包括医学解释、健康数据解读、建议与行动规划，以及症状处理。

## Evaluation

- **原子化的布尔型 rubric。** 100 余条临床上可核验的叶节点 rubric 组织在一张分层 DAG 中，自宏观能力层向下直至原子叶节点；每一条都是布尔判定，而非分级的主观意见。
- **自适应路由与自动加权。** 感知上下文的路由器只激活与查询相关的 rubric 子集，权重自动分配，从而在规模化时保住吞吐量。
- **对照专家的元评估。** 与专家小组（1 位资深医生加 5 位健康专家；整理阶段的小组则是 1 位主导医生加 8 位健康研究者）的一致性以 ICC₃ 与 Cohen's κ 测量，另有 oracle 扰动测试，检查那些结合上下文看已经劣化的回答是否确实会被扣分。
- **报告。** RubricsTree 的总体 ICC₃ 为 0.876、Cohen's κ 为 0.787，而基于原则的 baseline 分别为 0.291 与 0.431。作为结构化指令、文本反馈或训练奖励使用时，它在 Gemini、GPT 与 Qwen 系列上带来 HealthBench 至多约 66% 的相对提升；基于 RL 的训练增益报告为 +66.7%（Qwen 0.6B）、+55.3%（Qwen 1.7B）与 +40.3%（Qwen 4B）。

## Typical Duration

N/A — 这是逐条回答打分的评判框架；论文以评估吞吐量为由引入自适应路由，但未报告单条查询的 wall-clock 时间或 token 预算。

## Main Contribution

一套与专家对齐、分层分解的 rubric 分类法，让开放式健康 agent 评估同时具备可审计性与可扩展性；分类法本身也被设计为在人在环中的整理流程下持续演进，而不是在论文发表时定型。

## Key Design Ideas

- 评估自顶向下分解，从宏观能力一直细到原子化的布尔叶节点，因此任一分数都能追溯到具体的、临床上可核查的判断。
- rubric 在构造上就是布尔且原子的——正是这一点让医生逐节点核验成为可能。
- 逐查询路由只激活相关 rubric，以放弃穷举打分换取吞吐量，但并不因此舍弃完整的分类法。
- 同一套 rubric 承担三种角色——judge、文本反馈、RL 奖励——于是评估质量的检验标准变成：它能否改进被它评分的系统。
- 元评估特意纳入被有意劣化的回答，检验 judge 是否会扣专家会扣的分，而不只是把好答案排出高下。

## Strengths

- 与专家的一致性以标准信度统计量（ICC₃、Cohen's κ）对照医生主导的小组测得，而非仅作断言。
- 下游优化结果提供了一项外部检验，说明 rubric 信号确实携带可用信息。
- 分类法的整理立足于大量真实用户查询，而非合成场景。

## Limitations

- 代码与 rubric 称将在正式发表后放出；那份 532 条查询的内部评估集因含专有临床内容无法公开，故只报告聚合统计量。
- 分类法的确切深度以及逐层的类别构成均未披露，为 TODO(reference)。
- rubric 的整理与评估小组都取自作者自己的专家网络，因此对齐是拿撰写 rubric 的同一传统来衡量的。
- Repository note: 被评估的对象是健康助手的回答而非 agent 轨迹，因此该框架的分层分解落在 judge 一侧；逐步骤或逐 tool call 的打分不在协议范围内。

## Related Works

- [MedHELM](./medhelm.md) — 同样把由临床医生验证的医疗工作分类法与 LLM-jury 方法结合，并显式测量其与临床医生评分的一致性。
- [SkillCoach](./skillcoach.md) — 同样在验证门控下从真实 rollout 中构建并演进 rubric，但针对的是 agent 的过程质量而非临床内容。
- [AgentClinic](./agentclinic.md) — 同样在开放式交互中评估健康 agent，而非用固定的选择题。
- [MedAgentBench](./medagentbench.md) — 同样面向健康 agent 评估，走的是可执行临床任务而非 rubric 评判的路线。
