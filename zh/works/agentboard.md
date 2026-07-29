# AgentBoard (2024)

## Overview

AgentBoard 是一个针对多轮 LLM agent 的评估 benchmark，同时提供一个分析型评估面板。它的核心设计主张是：agent 评估不应收敛为一个二值成功率——性能应通过对已标注子目标（subgoal）的**细粒度进展率（fine-grained progress rate）**来衡量，且强调部分可观测（partially observable）的环境。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2401.13178>
- **Project:** <https://hkust-nlp.github.io/agentboard/>
- **Venue:** NeurIPS 2024 (oral)

## Summary

AgentBoard 论文认为大多数 agent benchmark 只关注最终任务结果，难以揭示 agent 是如何取得进展或如何失败的。该框架在四个任务家族之上提供了一个统一的评估设置，并附带一个分析面板，使性能可以在聚合成功率之外被切片查看。

## Tasks

1,013 个环境，分布在 9 种任务类型下。每个任务都附带子目标标注，用于计算进展率指标。

## Domains

Embodied AI、game agent、web agent 与 tool-use agent。环境为部分可观测、多轮交互。

## Evaluation

- **Progress rate（进展率）**：一段 trajectory 中已完成的已标注子目标比例。核心指标。
- **Success rate（成功率）**：作为与既往 benchmark 可比的粗粒度基线保留。
- **Grounding accuracy**：与进展率、成功率并行报告。
- **分析面板**：支持按任务家族与能力维度切片查看。

## Typical Duration

每个任务包含多轮交互；horizon 由子目标链而非固定步数预算界定。

## Main Contribution

面向多轮 LLM agent 的、基于子目标的细粒度进展指标；并配套一个把 trajectory 层级剖析——而非仅最终 success——视为一等评估输出的分析框架。

## Key Design Ideas

- 每个任务都标注一条子目标链。
- Progress rate 是对二值 success 的补充，而非替代。
- 部分可观测环境被视为默认设置，而非特例。
- 后处理式分析面板是交付物的一部分。

## Strengths

- 将 "取得了显著进展" 与 "完全失败" 区分开——这是二值 success 无法做到的。
- 在共享指标下覆盖四个任务家族（embodied、game、web、tool）。
- 公开的分析面板支持对比分析和诊断分析，而不仅是排行榜。

## Limitations

- Repository note: 子目标标注是一项人工的写作成本——将 benchmark 扩展到新任务家族需要人工做子目标分解。

## Related Works

- [T-Eval](./t-eval.md) — 同样在最终任务结果之下做了拆分，但沿的是 tool-use 能力子过程，而非任务子目标。
