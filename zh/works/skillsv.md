# SkillSV (2026)

> [English](../../works/skillsv.md) | **简体中文**

## Overview

SkillSV（结构感知的 agent skill Shapley 估值）是把 credit 分配到 skill 内部单元的归因框架——将 skill 编译为单元、依赖与层级，从而只评估合法的反事实 skill。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.04562>
- **Venue:** arXiv preprint, 2026

## Summary

SkillSV 通过在 skill 的编译结构上做 Shapley 估值来回答“一个 skill 值多少、价值由哪些部分承载”。成对删除与长度中性填充把内容价值与上下文成本分开。在四个 agentic benchmark 上按忠实性、可操作性与解释质量评估，该框架恢复了单元间交互、保持了整体 skill 增益，并指导安全的剪枝与压缩。

## Tasks

N/A——归因方法，非任务套件。在四个 agentic benchmark 上评估；具体是哪四个为 TODO(reference)。

## Domains

作为结构化工件的 agent skill；无单一科学领域。

## Evaluation

- 在四个 agentic benchmark 上评估估值的忠实性、可操作性与解释质量。
- **报告。** SkillSV 恢复单元间交互、保持整体 skill 增益，并指导安全剪枝与压缩；更多数字为 TODO(reference)。

## Typical Duration

N/A——对已完成评估的事后估值。

## Main Contribution

把结构感知的 Shapley credit 引入 agent skill 内部，使 skill 的价值可以定位到具体单元，而非对整体一言以蔽之。

## Key Design Ideas

- 把 skill 编译为单元/依赖/层级，使反事实仅限于合法 skill，有别于朴素消融。
- 成对删除配长度中性填充，控制上下文长度混淆。
- 估值的检验标准是能否在不损失 skill 增益的前提下指导剪枝。

## Strengths

- 使 skill 库可审计：哪些单元配得上其上下文成本。
- 显式分离内容价值与上下文成本。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- 摘要未报告数值结果；benchmark 名单与量级为 TODO(reference)。

## Related Works

- [Skill-Use](./skill-use.md) — 同样把 skill 作为一等评估对象，但为 agent 对 skill 的使用打分，而非为其内部估值。
- [GATE](./gate.md) — 同样分析结构化的 skill/工具工件，但采用基于图的工具演化而非 credit 估值。
- [QVal](./qval.md) — 同样对 credit 信号本身做元评估，但面向步骤级监督而非 skill 单元。
