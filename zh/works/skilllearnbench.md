# SkillLearnBench (2026)

> [English](../../works/skilllearnbench.md) | **简体中文**

## Overview

SkillLearnBench 是面向持续 skill 学习方法的基准——这类方法从 agent 自身的执行经验中自动生成 agent skill——它不只看任务解没解出来，还给生成出来的 skill 本身的质量打分。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 面向真实任务品类的通用 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2604.20087>
- **Code:** <https://github.com/cxcscmu/SkillLearnBench>
- **Venue:** COLM 2026

## Summary

Skill——定制化的指令、工作流与工具——已成为扩展 LLM agent 的标准做法，但怎样自动学出这些 skill 仍无定论。SkillLearnBench 评估那些从 agent 经验中产出 skill 的持续学习方法，任务派生自真实世界的 skill 分类法，且必须依赖 skill 才能完成，并从三个层次打分：skill 质量、执行轨迹、任务结果。评估覆盖一次性生成、自反馈精炼、教师反馈精炼，以及一条 skill creator 流水线，结论是：每种方法都胜过无 skill 基线，但没有哪一种能在所有任务与骨干模型上通吃。

## Tasks

仓库把范围表述为 "20 skill-dependent tasks · 15 sub-domains · 100 verified instances"；论文的说法是 20 个经过校验、依赖 skill 的任务，分布在真实世界 skill 分类法派生出的 15 个子领域中。任务的挑选标准是「成败取决于是否掌握相关 skill」，正因如此，生成出的 skill 才成了真正的受测对象。

## Domains

取自某 skill 分类法的真实 agent 任务品类；摘要与仓库说明都没有把这些子领域列为科学或工程学科，故不指派规范领域。

## Evaluation

三个评估层次：

- **任务结果**——通过率。
- **skill 质量**——所生成 skill 的功能覆盖、可执行性与安全性。
- **轨迹质量**——关键点召回、执行顺序与完整度。

实现了四条持续学习基线：One-Shot（单趟生成 skill）、Self-Feedback（借执行复盘迭代精炼）、Teacher-Feedback（专家指导下改进）以及 Skill Creator。仓库列出的受评骨干模型为 "claude-haiku-4-5, claude-sonnet-4-6, and claude-opus-4-6; gemini-3.1-flash-lite-preview, gemini-3-flash-preview, and gemini-3.1-pro-preview"。

**报告。** 所有持续学习方法都优于无 skill 基线，但稳定的收益依然难求：没有哪种方法在所有任务和所有 LLM 上领先，换用更强的 LLM 也不保证有帮助。持续学习在工作流清晰、可复用的任务上有提升，在开放式任务上则吃力。多轮迭代配合外部反馈能带来真实改进，而单靠自反馈则会引发递归漂移。

## Typical Duration

TODO(reference) — 摘要未报告逐任务的墙钟时间或 token 预算；持续学习基线要跑多轮迭代。

## Main Contribution

作者将其定位为首个评估持续 skill 学习方法的基准，把测量对象从任务成功率，转移到自动生成的 skill 工件以及产出它的那条轨迹上。

## Key Design Ideas

- 任务特意选成「依赖 skill」的，这样强骨干模型即便能独立解题，也掩盖不了一个弱 skill。
- 三层打分把所诱导工件的质量、过程与结果三者分开。
- skill 质量本身再拆成功能覆盖、可执行性与安全性，而不是整体给一个笼统判断。
- 基线集合横跨反馈谱系——无反馈、自反馈、教师反馈，以及一条结构化的 creator 流水线——从而把反馈来源的贡献单独隔离出来。

## Strengths

- 直接给诱导出的 skill 打分，而不只看它带来的下游任务表现。
- 把真实的迭代改进与自反馈下的递归漂移区分开来，而后者是只看结果的评估看不见的失败模式。
- 数据与代码开源。

## Limitations

- 20 个任务（100 个校验实例）对于「跨骨干模型给方法排名」这类主张而言偏小。
- 骨干模型只覆盖两个模型家族。
- Repository note: 该基准的对象是「从经验中诱导 skill」，而非定义 Skill Hierarchy 主题大部分工作的「分解并逐 subskill 打分」范式；把它归入该主题，是因为在评估 skill 工件这件事上，那里是现有最贴近的归属。
- Repository note: 卡片依据 arXiv 摘要、元数据与官方仓库 README 编写（2026 年 8 月）；所引之外的数字有待全文校验。

## Related Works

- [SkillSV](./skillsv.md) — 同样评估 skill 工件的内部质量，但对固定 skill 做归因，而非面向生成出来的 skill。
- [Skill-Use](./skill-use.md) — 同样使用依赖 skill 的可执行任务，度量的是 skill 的「使用」而非「生成」。
- [GATE](./gate.md) — 同样关心从 agent 活动中构建可复用的能力工件，但它是基于图的工具演化框架而非基准。
- [SkillJuror](./skilljuror.md) — 同样评估 skill 工件自身的性质，针对的是人工编写的组织方式而非自动生成。
