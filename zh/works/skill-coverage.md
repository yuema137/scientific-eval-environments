# Skill Coverage (2026)

> [English](../../works/skill-coverage.md) | **简体中文**

## Overview

Skill Coverage 是面向可复用 agent skill 的、基于轨迹的测试充分性指标：它把 skill 的自然语言指令编译成半结构化的行为约束，再逐条核对：agent 轨迹有没有覆盖到该约束，覆盖时观察到的行为又是通过还是失败。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — 面向通用 agent skill 的评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.20659>
- **Venue:** arXiv preprint, 2026

## Summary

任务的成败说不出一个可复用 skill 的哪些部分真正被用到了，也说不出用到时 agent 究竟有没有照相关指令去做。Skill Coverage 补的正是这一环：先把 skill 的行为约束抽取出来——即以半结构化形式写明「在什么条件下 agent 应当有什么行为」——再拿 agent 轨迹逐条比对，产出一个覆盖率数字，外加对已覆盖约束的 Pass/Fail 判定。用在 SkillsBench 上的结果显示，排行榜轨迹触及的约束远不到一半，而 Fail 判定的可操作性足以据以修补 skill，把原本失败的任务救回来。

## Tasks

N/A — 这是一套指标与分析框架，不是任务套件。其应用对象是已有的 SkillsBench 基准，以及该基准排行榜上的 agent 轨迹。

## Domains

面向通用 LLM agent、作为结构化工件的 agent skill；框架本身不限定于任何科学或工程领域，故不指派规范领域。

## Evaluation

- **约束抽取。** 把自然语言的 skill 指令转写为半结构化的行为约束，写明特定条件下 agent 应有的行为。
- **覆盖。** 对每条约束，判断 agent 轨迹是否覆盖到它。
- **判定。** 对已覆盖的约束，依据观察到的 agent 行为给出 Pass 或 Fail。
- **报告。** SkillsBench 排行榜上的 agent 轨迹，平均只覆盖所抽取 skill 行为约束的 38.66% 到 45.51%。若只把 agent 未能遵守的原有指令加重强调、其余一概不动，再重跑同一批任务，五个 agent–模型行上失败任务的平均挽回率为 16.0%。

## Typical Duration

N/A — 对既有基准运行所产生的轨迹做事后分析。

## Main Contribution

把软件测试中「测试充分性」的思路迁移到 agent skill 上：对一个 skill 所抽取行为约束的覆盖率，既衡量该 skill 是否得到了充分测试，也充当 skill 使用行为的细粒度诊断信号。

## Key Design Ideas

- 把 skill 指令编译成带条件作用域的半结构化约束，而不是当作自由文本去核对。
- 覆盖与正确分开记：一条约束可以未被覆盖、已覆盖且通过，或已覆盖且失败。
- 修补环节不增删任何 skill 内容，只加重 agent 本来就没遵守的那几条指令——这样 Fail 标签的诊断价值就与「补充了新知识」带来的收益区分开了。

## Strengths

- 能在单条指令的粒度上解释一个 skill 为什么有用、或为什么没用。
- 诊断价值由一次干预（任务挽回）证实，而非仅作断言。
- 约束级的 Fail 标签给 skill 作者一个具体的修改靶点。

## Limitations

- 从自然语言指令中抽取约束本身也是自动化步骤，其保真度决定了指标的上限。
- 只在单一宿主基准（SkillsBench）及其排行榜轨迹上验证过。
- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要提到有项目网站，但其 URL 为 TODO(reference)。

## Related Works

- [SkillSV](./skillsv.md) — 同样把 skill 拆成内部单元逐一评估，走的是 Shapley 估值而非轨迹覆盖。
- [Skill-Use](./skill-use.md) — 同样为 skill 的流程遵从打分，但按任务侧面而非按抽取出的约束划分。
- [SkillJuror](./skilljuror.md) — 同样从轨迹证据中读取 skill 的采纳情况，比较的是组织方式，而不是度量指令覆盖。
- [AgentBoard](./agentboard.md) — 同样以过程级的进度信号取代单一成功率，依据的是标注子目标而非 skill 约束。
