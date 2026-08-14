# SLBench (2026)

> [English](../../works/slbench.md) | **简体中文**

## Overview

SLBench 是一套 86 个用例的可执行基准，考察 LLM agent 能否理清一个 agent skill 内部各条指令之间的逻辑关系——前置条件、约束、回退，以及配套框架 SkillLogic 编目的另外五种关系类型。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用 agent 的可靠性与安全探针，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.09016>
- **Venue:** arXiv preprint, 2026

## Summary

Agent skill 把可复用的流程、工具与领域工作流打包在一起，但能否安全执行下来，取决于 agent 是否守住各条指令彼此之间的依赖。SkillLogic 以一套八类关系的分类法分析 skill 文件中的逻辑关系，并据此编译出可执行测试；对 5000 多个公开 skill 的扫描发现，其中 70% 至少含有一条逻辑关系。SLBench 从中挑出高置信、高影响、可局部测试的关系，构成 86 个可执行用例，并评估了推理时脚手架 SLGuard 作为缓解手段。

## Tasks

86 个可执行用例：SkillLogic 扫描 5000 多个公开 skill，从中挖掘逻辑关系，再筛出高置信、高影响、可局部测试的那一批，据以构建用例。关系分类法共八类，例如前置条件规定哪些动作才有效，约束限定已允许的动作可以怎样执行，回退则规定失败后如何恢复。

## Domains

面向通用 LLM agent 的 agent skill，在编码 agent 的 harness 中运行；报告的失败后果属于软件与系统运维（隐私泄漏、不安全的配置改动、清理不彻底）。不指派规范的科学或工程领域。

## Evaluation

- **可执行测试**由每条逻辑关系导出，违规由执行判定，而不是交给 judge。
- **Unsafe rate** 为头条指标，按 harness 与骨干模型分别报告。
- **报告。** 在六个 LLM 骨干模型上评估 Codex 与 Claude Code，unsafe rate 最高达 70%，违规会导致隐私泄漏、不安全的配置改动和清理不彻底。人工审计把失败归到两处：agent 的能力缺口，以及 skill 文本本身不够显眼。轻量级推理时脚手架 SLGuard 在针对性用例上把违规减少了 63%。

## Typical Duration

TODO(reference) — 摘要未报告单个用例的墙钟时间或 token 预算。

## Main Contribution

把「遵循逻辑关系」确立为 skill 引导型 agent 的一项独立可靠性挑战——它与一般意义上的指令遵循可以分开——并同时给出了大规模挖掘此类关系的分类法，以及据此构建的可执行基准。

## Key Design Ideas

- 八类关系的分类法，把 skill 散文中隐含的依赖变成显式、可核查的结构。
- 用例按「可局部测试」筛选，因此每次违规都能孤立地由执行来验证。
- 先做生态扫描量化普遍程度（5000 多个公开 skill 中有 70% 至少带一条关系），再据此构建基准，为用例挑选提供依据。
- 人工审计把失败归到两个不同来源——agent 能力与 skill 文本的显著性——而不是一股脑算在模型头上。

## Strengths

- 可执行验证，而非判定式的遵从度评分。
- 基准的构建立足于真实公开 skill 生态中实测到的一项性质。
- 诊断之外还配了一个经过评估的缓解方案（SLGuard），不止步于失败率。

## Limitations

- 按构造只涵盖「可局部测试」的关系，违规要跨长时程才显现的那一类不在其列。
- 相对扫描过的 skill 总量，86 个用例只是很小的一套。
- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未逐一列出所评估的六个骨干模型，为 TODO(reference)。

## Related Works

- [Skill-Use](./skill-use.md) — 同样度量 agent 是否守住 skill 规定的流程与边界，但按任务侧面而非按逻辑关系类型划分。
- [SkillSV](./skillsv.md) — 同样把 skill 编译为单元与依赖，用于价值归因而非安全测试。
- [SkillJuror](./skilljuror.md) — 同样把 skill 的内部结构当作被操纵的变量，操纵的是组织方式而非逻辑依赖。
- [SafeAgentBench](./safeagentbench.md) — 同样用可执行检查为不安全的 agent 行为打分，但在具身任务中而非 skill 文件上。
