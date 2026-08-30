# Agent Skill Evaluation and Evolution: Frameworks and Benchmarks (2026)

> [English](../../works/agent-skill-evaluation-survey.md) | **简体中文**

> **首次公开：** 2026-06-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.11435)

## Overview

这篇综述关注 skill 建成之后如何评估、如何演化：把相关文献归入四种 skill 演化范式与六类以 skill 为中心的 benchmark，并指出 benchmark 覆盖上的结构性空缺。

## Topics

- [Survey](../topics/survey.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 综述，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.11435>
- **Code:** <https://github.com/Cassie07/AgentSkill_Survey>
- **Venue:** arXiv preprint, 2026

## Summary

综述的核心论点是：这一领域正从孤立的 skill 创建，转向自动化、由评估驱动的 skill 演化；而当 skill 库规模变大，严格的评估就成了保证其效用、质量与安全的手段。它沿两条轴线梳理「基础性 skill 创建」之外的图景——skill 建成之后如何改进，以及如何度量 skill——最后给出若干开放方向，指向可泛化、高效且安全性可验证的 skill 生态。

## Tasks

N/A — 综述，不贡献任务套件。

## Domains

通用 LLM-agent 的 skill 生态；不针对任何科学或工程领域。

## Evaluation

N/A — 综述，不贡献评分协议。不过它确实按 benchmark 类别分析了已有协议，比较各自的覆盖面、取舍与指标丰富度。

## Typical Duration

N/A — 综述。

## Main Contribution

为 skill 创建之后的生命周期画出一张结构化地图：把演化范式分为四类，把以 skill 为中心的 benchmark 分为六类，两套分类合起来用于定位当前 benchmark 在测量内容上的结构性空缺。

## Key Design Ideas

- 演化范式按*所消费信号的粒度*区分：执行反馈（单次运行、步骤级信号，如运行时错误与错误输出）、轨迹蒸馏（多次运行、序列级模式）、压缩与增广（skill 库层面的结构），以及强化学习（任务级奖励）。
- benchmark 按测量对象而非按领域归类：skill 效用、skill 生成、skill 检索与路由、skill 安全审计、软件工程，以及真实环境。
- 对 benchmark 的分析围绕覆盖空缺与指标丰富度展开，而不是排行榜式的横向比较。
- 开放方向归为三组：多模态 skill、轨迹数据蒸馏，以及 agent skill 安全。

## Strengths

- 把 skill *生成* benchmark 与 skill *效用* benchmark 区分开——这恰是多数单个 benchmark 混为一谈的地方。
- 为一个快速演进的 benchmark 家族提供了可引用的索引，其中检索/路由与安全审计两条线尤其容易被漏掉。
- 配套仓库给出一份可持续更新的参考文献清单。

## Limitations

- 综述没有说明自己覆盖了多少篇论文或多少个 benchmark，其覆盖面的说法无法从正文中核实。
- 类别边界是描述性的；综述并未检验这六类 benchmark 在实践中是否真的可分。
- Repository note: 卡片依据 arXiv 摘要与 v1 全文编写（2026 年 8 月）。它索引的若干 benchmark 尚未收入本仓库，是后续补录的候选。

## Related Works

- [Skill-Use](./skill-use.md) — 属于综述所指认的 skill 效用类 benchmark，是其中一个实例。
- [SkillEvolBench](./skillevolbench.md) — 综述指认的轨迹蒸馏演化范式的一个实例，以 benchmark 的形式呈现。
- [SkillAudit](./skillaudit.md) — skill 安全审计类的一个实例。
- [SkillSV](./skillsv.md) — 与压缩与增广范式相关，通过为 skill 单元估值来指导剪枝。
- [Agent Evaluation Survey](./agent-evaluation-survey.md) — 更宽泛的 LLM-agent 评估综述，skill 评估是其中一个切面。
