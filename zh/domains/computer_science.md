# Computer Science

> [English](../../domains/computer_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为被研究领域的计算机科学，不含 AI/ML 研究本身——AI 论文复现见 AI & Machine Learning Research，软件构建与验证见 Software & Systems Engineering。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| AutoResearchBench | 2026 | 覆盖八个核心 CS 领域的科学文献发现：通过渐进多步探查追踪一篇特定目标论文（Deep Research），或全面收集满足给定条件的所有论文（Wide Research）。 | 1,000 条查询——600 条 Deep Research + 400 条 Wide Research（平均每条 9.23 个有效答案）——由全文优先的人机流水线与基于引用的多跳扩展构建。 | 对照已验证目标论文的精确匹配准确率（Deep）；对照经严格审计、须 LLM 一致同意方可收录的答案集的集合级 IoU（Wide）。 | [→](../works/autoresearchbench.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Information 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [AutoResearchBench](../works/autoresearchbench.md)
- [ResearchClawBench](../works/researchclawbench.md)
