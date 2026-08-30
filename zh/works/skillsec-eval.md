# SkillSec-Eval (2026)

> [English](../../works/skillsec-eval.md) | **简体中文**

> **首次公开：** 2026-07-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.13987)

## Overview

SkillSec-Eval 是面向可复用 agent skill 的生命周期感知评估框架：它把 skill 生命周期拆成五个信任边界各异的阶段——仓库准入、语义检索、规划器选择、运行时执行与 skill 演化——并在一个含 327 个真实 skill 的仓库上逐阶段分别评估攻击与防御。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型 agent 安全评估框架；未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.13987>
- **Venue:** arXiv preprint (cs.CR), 2026

## Summary

可复用 skill 把 agent 能力打包起来以便共享与复用，但安全研究一直集中在 prompt injection 与运行时执行上，生命周期的其余环节无人审视。论文按每类攻击所突破的信任边界组织出一套威胁分类法，把它实例化为 SkillSec-Eval，并逐阶段开展实证研究，每个阶段都设攻击与防御两种条件。得到的是一份逐阶段的脆弱性画像，而非单一的聚合安全分数；它表明失效远在执行之前就已出现——在准入、检索与规划器选择环节。

## Tasks

benchmark 建立在一个企业规模的 skill 仓库之上：327 个良性 skill，分属 15 个 skill 簇，取自 SkillMCP 仓库并过滤掉重复与不完整的条目；这些簇覆盖基础设施管理、DevOps 自动化、软件工程、云运维、数据工程、数据库优化、安全与合规、生产力自动化以及项目管理。按能力聚簇的工作负载包含 440 条 benchmark 查询，横跨 15 个能力领域，那 327 个真实 skill 则提供了逼真的检索邻域。五个阶段各自实例化对应的生命周期攻击类别，每一类都配一个防御条件。

## Domains

面向通用型 LLM agent 的可复用 skill，取自一个企业 skill 仓库，其簇涵盖基础设施、DevOps、软件与数据工程以及业务自动化。被评估的对象是 skill 生命周期的安全性而非某个领域任务，因此不分配任何规范的科学或工程领域。

## Evaluation

- **逐阶段的攻击/防御对照。** 每个生命周期阶段都测量一个基线（无防御）条件与一个有防御条件，因此缓解效果是逐阶段报告而非汇总成一个数。
- **仓库准入。** 恶意准入率与误报率——混合式防御在 20.0% 误报率下准入 7.9% 的恶意 skill，而纯规则过滤器的恶意准入率为 52.9%。
- **语义检索。** 检索投毒的攻击成功率——关键词堆砌基线 46.59%、防御后 7.83%；Sybil 攻击基线 93.20%、防御后 26.59%。
- **规划器选择。** 伪造推荐基线 45.64%、防御后 8.72%；误导性描述基线 27.27%、防御后 0.00%。
- **运行时执行。** 基线攻击成功率 100%，所提防御将其降至 23%，并拦截 87% 的策略违规。
- **skill 演化。** 恶意更新检出率 92.5%，误报率 37.0%，更新接受率 63.0%。
- **实验设置。** 规划器 LLM 为 Gemini 1.5 Flash；语义检索使用 all-MiniLM-L6-v2 嵌入与 FAISS 索引。

## Typical Duration

N/A — 这是一套逐阶段的安全评估框架，而非长时程任务套件；论文未报告单条查询的 wall-clock 时间或 token 预算。

## Main Contribution

一套面向可复用 agent skill 的生命周期威胁分类法，按每类攻击所突破的信任边界来组织；配以模块化的评估框架与 benchmark，使安全性在每个生命周期阶段都可测量、可复现——并以实证确立：漏洞并不局限于运行时执行。

## Key Design Ideas

- 生命周期被拆成信任边界彼此独立的阶段，于是漏洞与防御可以分开分析，而不必端到端地混在一起。
- skill *演化*——对已准入 skill 的更新——被单列为一个攻击面，这是一次性审核覆盖不到的。
- 工作负载按能力聚簇，使检索邻域接近真实仓库，正是这一点让检索投毒攻击具有意义。
- 每项防御在报告检出率的同时也报告其误报代价，而不是只给检出率。

## Strengths

- 逐阶段报告给出的是 skill 层究竟在哪里失效的可解释画像，而非一个数字。
- 327 个 skill 的仓库与 440 条查询的工作负载来自真实的 skill 注册库，而非合成桩件。
- 防御与攻击在同一套框架中评估，因此缓解效果是被测出来的，而不只是被提出来的。

## Limitations

- 只用了一个规划器 LLM（Gemini 1.5 Flash），因此框架层面的结论与单一 backbone 的行为混杂在一起。
- 防御的误报率在一些环节偏高——准入 20.0%、skill 演化 37.0%——这限制了实际部署。
- 论文未给出任何代码或数据发布 URL，留作 TODO(reference)。
- Repository note: 本工作的候选元数据曾把它描述为综述；实则不然——论文的实质贡献是 SkillSec-Eval 框架、其 benchmark 以及一项攻击/防御实证研究。

## Related Works

- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](./agent-skill-evaluation-survey.md) — 综述的正是同一个 skill 评估层面，本工作则在其中贡献了一个生命周期专用框架。
- [SCR-Bench](./scr-bench.md) — 同样论证孤立式逐 skill 审核不足，但切入点是同一执行上下文内的组合，而非跨生命周期阶段。
- [HarmfulSkillBench](./harmfulskillbench.md) — 同样测量公开 skill 注册库的安全性，关注的是有害意图而非生命周期信任边界。
- [SkillAudit](./skillaudit.md) — 同样产出逐 skill 的多维报告，把效用与成本和安全性合在一起。
