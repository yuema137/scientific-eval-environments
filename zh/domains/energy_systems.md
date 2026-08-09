# Energy Systems

> [English](../../domains/energy_systems.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

能源系统工程：电力、可再生能源与能源研究。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Energy 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| PowerAgentBench-SS | 2026 | 开展电力系统稳态研究：在电网算例上做预想故障筛选并提出满足约束的缓解措施。 | IEEE 39 节点系统运行点变体上的 agentic 工具调用研究，配基于直流潮流的 N-2 热稳定越限搜索试点，受验证预算约束。 | 隐藏评估器重算物理有效性；多种 recall、false-safe 罚分、severity regret、动作成本与工具使用效率。 | [→](../works/poweragentbench-ss.md) |
| ElecBench | 2024 | 在稳定性、安全性与经济约束下对电网运行与调度进行推理。 | 跨通用知识与专业业务场景的电力调度评估；8 个 LLM。 | 六项指标（事实性、逻辑性、稳定性、安全性、公平性、表达性）/ 24 个子指标。 | [→](../works/elecbench.md) |

## Related Works

- [ResearchClawBench](../works/researchclawbench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [ElecBench](../works/elecbench.md)
