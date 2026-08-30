# Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design (2026)

> [English](../../works/co-evolution-agentic-systems-survey.md) | **简体中文**

> **首次公开：** 2026-08-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.10299)

## Overview

一篇关于 agentic 系统中共同演化的综述——所谓共同演化，是自我演化的多组件形态，多个 agent 与它们所处的环境彼此施加适应压力。文章用一个递进的三阶段分类体系梳理文献，追踪系统如何一步步卸掉人为设计的约束，并专辟一节论述为什么评估这类系统比评估固定 agent 更难。

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — 一篇关于通用 agentic 系统自我演化方法的综述。它不评估任何 agent 在科学或研究活动上的表现。

## Links

- **Paper:** <https://arxiv.org/abs/2608.10299>
- **Venue:** arXiv 预印本（2026 年 8 月）。

## Summary

综述的起点是：单实体的自我演化受限于静态的学习语境——一个只面对固定任务与固定反馈去改进的 agent，迟早会把这个语境能教给它的东西学完。共同演化则让其他组件也动起来，从而移走这道天花板。三阶段分类体系按「还剩多少人为设计」排序。**Agent–Agent 共同演化**涵盖 agent 对动态同伴的适应，分为对抗压力（两两对抗与多源对抗）、协作适应（并行协作与角色分化协作），以及不断演化的 agent 组织。**Agent–Environment 共同演化**把这一回路延伸到环境本身，覆盖三个空间：任务空间（暴露与选择；自适应任务生成）、反馈空间（偏好驱动、结果驱动、一致性增强的反馈）与交互空间（可执行世界构建与基于模型的世界构建）。**Meta 共同演化**则追问演化机制本身能否被做成可演化的，分别从开放性与 meta 共同演化的前身两方面讨论。综述最后落在三类开放挑战上：评估、跨组件的规模化，以及如何让自主性不断提高的演化过程保持安全可控。

## Tasks

N/A — 综述，不贡献任务集。参考文献从 Hillis（1990）延伸到本文 2026 年 8 月的投稿；`TODO(reference)` — 综述未说明收录论文数量，也未给出明确的覆盖时间窗。

## Domains

不指派任何规范领域。主题是通用 agentic 系统的方法学；它讨论的 benchmark 集中在工具使用、网页浏览、软件工程、计算机操作与多 agent 交互，在本仓库的领域轴上都不属于科学或工程学科。

## Evaluation

作为评分协议是 N/A——但评估是综述点名的开放挑战之一，而它对这一点的处理正是本卡片收录于此的理由。作者指出现有 benchmark 主要衡量 agent 的最终能力，而评估共同演化「必须判定是否所有演化中的组件都在改进、它们的收益能否迁移到未见过的同伴与环境，以及每个组件对整体进展各贡献了多少」。

论文点名了三种特属于此场景的失效模式：**评判器被利用**、**对同伴过拟合**、**多样性坍缩**。建议的应对是把固定 benchmark 与过程级测试配合使用——具体包括**历史交叉对战、组件消融与留出评判器**。

综述以行文方式而非表格列举了它讨论的 benchmark：工具使用有 τ-Bench、ToolSandbox、PlanBench-XL、CostBench 与 AdaPlanBench；网页浏览有 WebArena 与 BrowseComp；软件工程有 SWE-Bench 与 SWE-Lancer；计算机操作有 AppWorld、OSWorld 与 Terminal-Bench；多 agent 交互有 SOTOPIA、AgentSense 与 MultiAgentBench。其中它只认定 **PostTrainBench** 一个具备演化感知能力——这正是综述用来说明「它所描述的评估缺口确实存在且基本无人填补」的证据。

## Typical Duration

N/A — 综述。

## Main Contribution

一个按「移除了多少人为设计结构」来排序自我演化研究的分类体系，把视野从单 agent 自我改进扩展到跨 agent、任务、反馈与交互空间的共同演化——并论证这类系统打破了静态 benchmark 的前提假设，同时给出一份「那么该改测什么」的具体清单。

## Key Design Ideas

- 分类体系的排序原则是「剩余人为设计的多少」，因此三个阶段构成的是递进而非并列——到了第三阶段，演化机制本身成为被演化的对象。
- Agent–Environment 共同演化按环境的**哪一部分**在动来拆分（任务、反馈，还是交互空间），把原本容易混作一谈的几条研究线索分了开来。
- 评估一节点出三种特属于共同演化系统的失效模式，而它们从构造上都是固定 benchmark 看不见的：可被利用的评判器、可被过拟合的同伴，以及会坍缩的多样性。
- 提出的对策是结构性的而非指标层面的——与历史对手交叉对战、组件消融、留出评判器——这与「问题出在评估设计而非分数」的判断相吻合。
- 统计既有 benchmark 中有几个具备演化感知能力（一个），把这道缺口量化了，而不是断言了事。

## Strengths

- 就一篇综述而言，评估部分的讨论异常具体，既点名失效模式，也点名能应对它们的具体测试设计。
- 在所讨论的十五个左右 benchmark 中只认定一个具备演化感知，这是一个可核查的论断，为文章的缺口论证提供了证据。
- 按「移除多少人为设计」排序，使分类体系具备原则而非仅有列表结构，新工作因而有确定的归位。
- 作者直接说明自己第三阶段的内容偏薄，而没有硬撑。
- 覆盖范围上溯至 Hillis（1990），把近期的 LLM agent 自我演化放进了更长的共同演化计算脉络中。

## Limitations

- 未说明收录论文数量或明确的覆盖时间窗，综述的完整性因而无从评估（上文记为 `TODO(reference)`）。
- 作者说明符合其第三阶段定义的工作有限，因此那部分讨论不得不大量借助单实体的 meta 演化作为前身，而非真正的 meta 共同演化。
- 安全、监控与人类监督只被当作愿望层面的要求来处理；作者说明自己并未发展出具体的防护手段或协议。
- 没有提到公开的论文清单或仓库，因此这篇综述并未作为一份持续维护的索引来经营。
- 所讨论的 benchmark 都是通用 agent benchmark，未涉及科学与工程领域的评估，因此综述的评估批评并未落在科学 agent 这支文献上。
- Repository note: 本卡片收录的理由是综述中的评估挑战一节。工作的主体是对自我演化**方法**的梳理，不在本仓库范围内。

## Related Works

- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](./agent-skill-evaluation-survey.md) — 最接近的邻居：同样梳理演化范式及为其打分的 benchmark，范围限定在 agent skill 而非整个系统。
- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — 通用 agent 评估的分类体系，覆盖的正是本综述认为被共同演化打破的静态 benchmark 场景。
- [Evaluation and Benchmarking of LLM Agents: A Survey](./agent-evaluation-benchmarking-survey.md) — 按目标与过程两个维度组织 agent 评估，与本综述在建议过程级测试时所诉诸的区分是同一个。
- [PACE-Bench](./pace-bench.md) — 专门评估环境变化之后的自演化 agent，正是本综述认为付之阙如的那种「变化下的适配」测量的一个实例。
