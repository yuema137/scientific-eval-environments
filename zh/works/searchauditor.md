# SearchAuditor (2026)

> [English](../../works/searchauditor.md) | **简体中文**

> **首次公开：** 2026-08-05 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.05212)

## Overview

SearchAuditor 是对长 horizon 搜索 agent 的失败做定位、归因与修复的多视角审计框架，随之发布 SearchAuditBench——1,243 条专家标注的失败轨迹，采集自八个开源权重模型在五个 deep-search benchmark 上的运行。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.05212>
- **Venue:** arXiv preprint, 2026

## Summary

SearchAuditBench 的失败轨迹平均 73.1 条消息、65.1K token；每条都由专家标注关键错误步骤、搜索特有的根因，以及带评分 rubric 的参考修复。SearchAuditor 通过证据锚定的多视角裁决来定位与归因失败并提出修复，应用修复可提升 agent 的恢复表现。

## Tasks

SearchAuditBench：1,243 条失败轨迹（平均 73.1 条消息、65.1K token），来自八个开源权重模型在五个 deep-search benchmark 上的运行；每条附专家标注的关键错误步骤、搜索特有根因与带评分 rubric 的参考修复。

## Domains

长 horizon deep-search agent 轨迹。

## Evaluation

- 端到端度量审计质量：关键步骤定位、根因归因、对照参考 rubric 的修复。
- **报告。** 最强基线的端到端通过率仅 26.6%；SearchAuditor 配 GPT-5.5 等前沿模型达到 32.3%；应用其修复可改善 agent 恢复。

## Typical Duration

对长失败搜索轨迹（平均 65.1K token）的事后审计。

## Main Contribution

把搜索 agent 的失败分析变成有 benchmark、有专家锚定的任务——定位、归因、修复——而不是靠非正式的调试经验。

## Key Design Ideas

- 专家标注固定了关键步骤与根因，审计者可对照真值计分。
- 根因是搜索特有的，而非泛化的错误标签。
- 带 rubric 的参考修复使修复环节（而不仅是诊断）可评分。

## Strengths

- 覆盖多模型、多 benchmark 的大规模、高成本真实失败语料。
- 端到端通过率表明任务远未解决（最佳 32.3%）。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [TRAJDEBUG](./trajdebug.md) — 同样在标注失败轨迹中归因关键失败，但面向 tool-use 与编码而非 deep search。
- [TELBench](./telbench.md) — 同样对 deep-research 轨迹做专家切分与错误定位，粒度为 span 级。
- [Who&When Pro](./who-and-when-pro.md) — 同样为失败归因打分，但失败由构造而非自然产生。
