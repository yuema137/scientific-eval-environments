# SkillEvolBench (2026)

> [English](../../works/skillevolbench.md) | **简体中文**

> **首次公开：** 2026-05-22 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.24117)

## Overview

SkillEvolBench 是一套诊断性基准，针对的是从「经验复用」迈向「skill 形成」的那一步：LLM agent 能否把自己的情节式轨迹蒸馏成可复用的程序性 skill，并且在 skill 库被冻结、任务发生变化之后依然管用。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2605.24117>
- **Project:** <https://skillevolbench.github.io/>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

该基准把评估分成两个阶段。习得阶段，agent 解决学习任务，并用压缩后的执行工件配合验证器反馈去更新一个外部 skill 库。部署阶段，skill 库被冻结，agent 只能读不能改，面对的是考察上下文偏移、对抗性捷径与组合能力的留出任务。四种条件——无 skill、原始轨迹复用、自生成 skill，以及带精选种子库的起步——彼此对照，从而把程序性抽象与基础能力、与既有的人工精选知识、与情节轨迹的直接复用分离开来。论文在十种模型配置和三套 agent harness 上报告：agent 能做出局部适应，却很少形成稳健可复用的 skill；而且原始轨迹复用常常胜过从这同一批轨迹蒸馏出来的 skill。

## Tasks

180 个任务，分布在六个真实 agent 环境中：代码调试与修改、工具与 API 编排、数据处理与结构化查询、文档解析与转换、研究与信息综合、沟通与日程安排。任务组织为受角色约束的任务族，同族共享一条潜在流程——每个环境五个族，每族六个任务（三个习得任务：标准、加料、变体；三个冻结部署任务：上下文偏移、对抗、组合）。skill 库遵循 SKILL.md 约定，可选地在 `scripts/`、`references/`、`assets/` 下捆绑资源；Tier-3 消融把资源捆绑设为强制。

## Domains

通用 agent 环境（软件、工具、数据、文档、信息综合、沟通）。不针对任何规范的科学或工程领域；受评对象是程序性 skill 的形成，而非某项科学任务。

## Evaluation

- 分阶段的成功率：LSR（习得/学习）、RSR（在冻结库下重放同一批任务）、ESR（冻结部署下的评估）。
- ESR 再按部署轴分解为 CSSR（上下文偏移）、ARSR（对抗性捷径）与 CompSR（组合）。
- 每种 skill 条件都以相对无 skill 与原始轨迹两条对照的 delta 形式报告，从而把可归因于「抽象」的收益与仅仅「有记忆」带来的收益分开。
- **报告。** 自生成 skill 的条件可以抬高习得与重放的成绩，同时在冻结部署上呈现负 delta；逐模型的排行榜数值为 TODO(reference)。

## Typical Duration

未报告步数或 token 上限。每次尝试任务的成本以美元按对数尺度报告；相对各自基线，精选变体平均每次尝试任务 **+$0.077**，Tier-3 消融 **+$0.119**。

## Main Contribution

一个受控试验台，把「程序性抽象」单独隔离出来作为测量对象：冻结库的部署阶段配上原始轨迹对照与精选起步对照，把「agent 学到 skill 了吗」从一个聚合分数变成条件之间的差值。

## Key Design Ideas

- 部署时冻结 skill 库，使测得的收益不可能来自任务中的持续适应。
- 受角色约束、共享同一条潜在流程的任务族，让「抽象」有明确的东西可复原。
- 一条原始轨迹对照线：同样的情节证据不作蒸馏直接给出——结果证明这是一条很强的基线。
- 三条部署轴（上下文偏移、对抗性捷径、组合）分别考验一份成文 skill 的不同失效方式。
- 容量与成本消融，检验写更多 skill 或捆绑更大的资源库是否有用。

## Strengths

- 对照设计让一个负面结果变得可解读：可以证明蒸馏相对它所概括的轨迹是有信息损失的。
- 跨三套独立的 agent harness 运行，结论不绑死在某一种 skill 库实现上。
- 在报告成功率的同时报告金钱成本，暴露出多写 skill 换来的覆盖是要付费的。

## Limitations

- 论文自己的诊断是：当下的抽象流程有损，其有用与否取决于基础模型解读并运用成文 skill 的能力；论文并未提出解法。
- 环境都是通用 agent 工作流；程序性抽象在科学或工程任务上是否表现相同，该基准无从回答。
- Repository note: 卡片依据 arXiv 摘要与 v1 全文编写（2026 年 8 月）；逐模型的具体成功率留作 TODO(reference)，待直接核对表格。

## Related Works

- [Skill-Use](./skill-use.md) — 评估的是对预先写好的 skill 的使用；SkillEvolBench 评估的则是 agent 能否先把 skill 写出来。
- [SkillSV](./skillsv.md) — 为已有 skill 的内部单元估值，与「这个 skill 值不值得写」互为补充。
- [GATE](./gate.md) — 同样关心从经验中构建可复用的能力工件，走的是层级式工具图而非成文 skill 库。
- [HarnessOpt-Bench](./harnessopt-bench.md) — 同样为 agent 改进自身外围工件的能力打分，作用在 harness 层而非 skill 层。
- [AgentBoard](./agentboard.md) — 同样主张在多步 agent 任务中用过程级信号取代只看终局的信号。
