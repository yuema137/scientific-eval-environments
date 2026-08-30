# ASIMOV (2025)

> [English](../../works/asimov.md) | **简体中文**

> **首次公开：** 2025-03-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2503.08663)

## Overview

ASIMOV Benchmark 评测作为机器人大脑的 VLM 的语义安全——判断情境的合意性与安全性、拒绝违反机器人宪法的动作——数据集大规模生成自真实视觉场景与医院伤害报告；配套方法自动生成并修订机器人宪法，最高对齐率达 84.3%。

## Topics

_无方法论轴主题——在 [Robotics](../domains/robotics.md) 领域（领域轴）下索引。_

## Activities

N/A — 评估的是 agent 的元属性（成本、安全性或鲁棒性），而非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2503.08663>
- **Code:** <https://github.com/asimov-benchmark/code/>
- **Project:** <https://asimov-benchmark.github.io>
- **Venue:** CoRL 2025（据官方项目页；arXiv 元数据未载明发表信息）

## Summary

这项由 Google DeepMind 发表、题为「Generating Robot Constitutions & Benchmarks for Semantic Safety」的工作瞄准机器人安全的语义层：不是避碰，而是机器人的大脑能否意识到某个动作是不合意的。ASIMOV 数据集把「不合意」锚定在现实上——真实视觉场景与医院的人身伤害报告——评估衡量模型判断与人类偏好之间的对齐。配套方法自动生成机器人宪法并加以修订（Constitutional AI 机制），最高对齐率达 84.3%，胜过无宪法与人工撰写宪法两种基线；论文还演示了一台机器人拒绝违反机器人宪法的动作。

## Tasks

静态安全判断评估：VLM 在以伤害报告与视觉场景为依据的数据上评判情境合意性与动作许可性。数据集规模为 TODO(reference)——摘要未载明。

## Domains

机器人学——对充当机器人大脑的 VLM 做语义安全评估，以真实伤害报告与视觉场景为依据；benchmark 本身是静态安全判断，而非机器人控制。

## Evaluation

- 在不同宪法条件下，模型判断与人类偏好（行为合意性与安全性）的对齐率。
- **报告。** 使用生成宪法时最高对齐率 84.3%，胜过无宪法与人工撰写宪法基线。

## Typical Duration

按条目的判断查询；benchmark 本身无回合式交互。

## Main Contribution

把机器人安全评估锚定在有据可查的人身伤害——伤害报告——之上，并表明机器生成、自我修订的宪法比人工撰写的规则更能对齐机器人的判断。

## Key Design Ideas

- 伤害报告把物理伤害的真实分布引入安全评估。
- 宪法使安全判据显式、可审计、可改进。
- 自动修订闭环：不对齐之处反馈回宪法修订。

## Strengths

- 在一个满是假想危险的领域里，罕见地以真实伤害为依据。
- 「生成宪法胜过人工撰写」的结果可直接用于已部署的机器人策略。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；论文标题为「Generating Robot Constitutions & Benchmarks for Semantic Safety」——ASIMOV 是 benchmark 工件之名。CoRL 2025 由项目页声明而非 arXiv 元数据；数据集规模摘要未载明。
- Benchmark 与宪法生成方法是并列贡献；使用生成宪法下的分数同时反映两者。

## Related Works

- [SafeAgentBench](./safeagentbench.md) — 同样是具身 agent 安全，以被执行的危险计划而非判断对齐来评估。
- [BadRobot](./badrobot.md) — 同样是机器人安全评估，对抗性地诱发 ASIMOV 要模型识别的那些危害。
- [PhysBench](./physbench.md) — 同样评估具身部署底下的世界理解层。
