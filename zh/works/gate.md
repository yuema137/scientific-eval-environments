# GATE (2026)

> [English](../../works/gate.md) | **简体中文**

## Overview

GATE（Graph-based Adaptive Tool Evolution Across Diverse Tasks）是一个动态构造并演化"可复用工具的层级图"的框架，供 LLM 在跨任务场景下使用。本卡片为覆盖完整性而纳入，但请注意：**该论文的实际主题是面向 LLM 的 tool-making，而不是 agent 的 skill-hierarchy 评估**——维护者初始列表把它归为 Skill Hierarchy 是名称匹配上的表面误分类，非论文实际内容。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://aclanthology.org/2026.acl-long.87/>
- **Venue:** ACL 2026

## Summary

GATE 动态构造并演化一个可复用工具的层级图，供 LLM 在多种场景下使用。该层级图刻画跨领域的工具关系与复用模式，使工具构造能自适应于不同问题类型。评估在 Minecraft、TextCraft、DABench 与代码生成上进行。

## Tasks

非任务套件。下游评估在四个 benchmark 上进行：Minecraft、TextCraft、DABench 与代码生成。

## Domains

面向 LLM 的 tool-making / tool evolution。下游评估覆盖游戏（Minecraft、TextCraft）、数据分析（DABench）与代码生成。

## Evaluation

在四个下游 benchmark 上的性能；论文摘要报告相较既有方法的改进。

## Typical Duration

取决于下游 benchmark。

## Main Contribution

一个自适应框架，用来构造并演化 LLM 可跨任务复用的、层级化的工具图。

## Key Design Ideas

- 可复用工具的层级图作为主要抽象。
- 面向不同任务类型的自适应工具构造。
- 跨 benchmark 的适用性。

## Strengths

- 在异质下游 benchmark 上给出自适应的工具结构。
- 在四个下游 benchmark 上（按摘要）相较既有方法有所提升。

## Limitations

- Repository note: GATE 是一个 tool-making / tool-evolution 框架——尽管本卡片按维护者初始列表被放在 Skill Hierarchy 之下，论文的实际主题是**为 LLM 构造工具**，而不是**把 agent 能力分解为 subskill**。请以论文实际范围为准，避免由此得出关于 skill hierarchy 的结论。
- Repository note: 非任务套件；下游任务（Minecraft、TextCraft、DABench、代码生成）是基座。

## Related Works

- 本仓库中无与之直接可比的对象——GATE 是 tool-evolution 框架，而非 benchmark。相邻的、与 topic 实际吻合的 skill 分解 benchmark 请见 [Skill Hierarchy](../topics/skill_hierarchy.md)。
