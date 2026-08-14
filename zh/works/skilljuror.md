# SkillJuror (2026)

> [English](../../works/skilljuror.md) | **简体中文**

## Overview

SkillJuror 是一套评估框架，把*一个 agent skill 如何组织*与*它说了什么*分离开来：在任务知识保持不变的前提下，比较 Progressive Disclosure 布局（一个精简的根文件，按需指向各项支撑资源）与归一化的扁平基线。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 通用的 agent skill 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.11543>
- **Venue:** arXiv preprint, 2026

## Summary

Agent Skill 在推理时为 LLM agent 供给程序性知识，但只报告任务成功率的 benchmark 无法把一个 skill 的内容与它的组织方式分开。SkillJuror 构造同一 skill 的语义受控变体，跑成对的多次试验评估，并检视轨迹证据，从而使任何测得的差异都能归到布局上，而不是知识上。把该框架用到一项 82 任务的 SkillsBench 研究上可以看到：Progressive Disclosure 先改变的是运行时行为，之后才改变聚合结果。

## Tasks

一项在 SkillsBench 上的 82 任务研究，每个任务都在语义受控的 skill 变体下运行（Progressive Disclosure 对归一化的扁平基线），采用成对的多次试验配置，合计 410 组配对试验。变体的构造流程使底层任务知识保持不变，只让组织方式有差别。

## Domains

作为结构化工件的 Agent Skill，服务于通用 LLM agent；论文未把任务限定到某个科学或工程领域，因此不指派任何规范领域。

## Evaluation

- **轨迹级行为指标。** 每条轨迹触及的不同 skill 资源数，以及每条轨迹的有效采纳事件数。
- **结果指标。** 配对试验中通过验证器的试验数。
- **报告。** 在 Progressive Disclosure 下，每条轨迹触及的不同 skill 资源数从 1.18 升到 3.85，有效采纳事件数从 1.33 升到 3.92；相对归一化的扁平基线，它在 410 组配对试验中多带来 17 组通过验证器的试验（+4.1%）。
- 论文报告收益因任务而异：当支撑资源能指导实现、检查或修复时，Progressive Disclosure 有帮助；而当成败取决于精确的输出约定、数值阈值或长链条的工件生成流水线时，它的作用较弱。

## Typical Duration

TODO(reference) — 摘要报告了试验次数，但未给出单任务的 wall-clock 或 token 预算。

## Main Contribution

一套针对 skill *写法范式*的受控评估协议，表明 skill 的组织方式不只是呈现形式：它会切实改变 agent 检索并运用程序性知识的方式，而结果层面的增益则取决于所暴露的资源是否可操作。

## Key Design Ideas

- 语义受控的 skill 变体让任务知识保持恒定，布局成为唯一被操纵的因素。
- 成对的多次试验评估把试验在变体之间一一配对，而不是比较聚合的排行榜。
- 把轨迹证据（触及的资源、采纳事件）当作主信号，聚合成功率则退为滞后的次级指标。

## Strengths

- 把内容与组织分开，而多数 skill benchmark 恰恰把二者混为一谈。
- 报告的是过程层面的效应，即便端任务成功率还没动，这些效应也看得见。
- 明确给出了所研究布局不起作用的边界条件。

## Limitations

- 只比较两种布局（Progressive Disclosure 与归一化的扁平基线），而非遍历组织范式的空间。
- 建立在单一宿主 benchmark 上（SkillsBench，82 个任务），该效应能否跨 harness 与任务族推广尚未验证。
- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [Skill-Use](./skill-use.md) — 同样把 skill 作为一等评估对象，但为 agent 对 skill 的使用打分，而非为 skill 的布局打分。
- [SkillSV](./skillsv.md) — 同样针对 skill 的内部结构，但为其单元估值，而非比较组织范式。
- [SkillTV-Bench](./skilltv-bench.md) — 同样在 skill 增强的设定下评估，落在评判者一侧而非执行的 agent。
- [Harness-Bench](./harness-bench.md) — 同样表明脚手架的选择（而不只是模型）会实质改变测得的能力。
