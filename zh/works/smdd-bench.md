# SMDD-Bench (2026)

> [English](../../works/smdd-bench.md) | **简体中文**

## Overview

SMDD-Bench 追问 LLM 能否解决真实世界的小分子药物设计任务：502 个保证有解的实例、102 个不同蛋白靶点、五类任务——2D 药效团识别、相互作用位点发现、骨架跃迁、先导化合物优化与片段组装——以多轮、长 horizon 的 agentic benchmark 呈现。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.21740>
- **Leaderboard:** <http://smddbench.com>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

SMDD-Bench 要求扎实的化学与生物学推理、3D 直觉、专业工具使用，以及在有限 oracle 调用次数下的规划能力——oracle 预算让每次查询都是被消耗的资源，agent 必须规划探索而非穷举。每个实例都构造为保证有解，因此失败反映的是 agent 而不是任务。在七个前沿开源与闭源 LLM 上，即便表现最好的 GPT-5.4 也只解出 40.2% 的任务。

## Tasks

502 个保证有解的多轮药物设计任务实例，覆盖 102 个蛋白靶点，五类：2D 药效团识别、相互作用位点发现、骨架跃迁、先导化合物优化与片段组装。

## Domains

小分子药物设计：面向蛋白靶点的药物化学与计算化学——药效团、骨架、先导优化与片段组装。

## Evaluation

- 有限 oracle 调用预算下、保证有解实例上的解出率；oracle 与验证器实现细节为 TODO(reference)。
- **报告。** 七个前沿 LLM 受评；最佳的 GPT-5.4 仅解出 40.2%。

## Typical Duration

以 oracle 调用预算为界的多轮长 horizon 设计回合。

## Main Contribution

把药物设计构造成预算受限的搜索：保证有解加 oracle 调用上限，使成功与查询效率都能归因到 agent 的规划能力上。

## Key Design Ideas

- 保证有解的构造排除了「任务本来就不可能」的借口。
- oracle 调用预算给探索定价，把资源意识引入分子设计。
- 五类任务从感知（药效团）一路铺到合成级规划（片段组装）。

## Strengths

- 靶点多样性真实（102 个蛋白），且可解性可验证。
- 预算下 40.2% 的前沿上限记录了充足的提升空间。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。校验时排行榜网站不可访问，论文的 arXiv 页面上亦无可验证的代码发布。

## Related Works

- [MDArena](./mdarena.md) — 同样是分子层面的 agent 科学工作流，在模拟而非设计侧。
- [MaD Physics](./mad-physics.md) — 同样在单任务预算下为查询定价，面向物理定律发现。
- [SciAgentArena](./sciagentarena.md) — 其生物医学研究场景中同样包含计算药物发现任务。
