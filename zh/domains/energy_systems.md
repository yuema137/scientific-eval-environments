# Energy Systems

> [English](../../domains/energy_systems.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

能源系统工程：电力、可再生能源与能源研究。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Energy 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文产物的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| PowerAgentBench-SS | 2026 | 开展电力系统稳态研究：在电网算例上做预想故障筛选并提出满足约束的缓解措施。 | IEEE 39 节点系统运行点变体上的 agentic 工具调用研究，配基于直流潮流的 N-2 热稳定越限搜索试点，受验证预算约束。 | 隐藏评估器重算物理有效性；多种 recall、false-safe 罚分、severity regret、动作成本与工具使用效率。 | [→](../works/poweragentbench-ss.md) |
| ElecBench | 2024 | 在稳定性、安全性与经济约束下对电网运行与调度进行推理。 | 跨通用知识与专业业务场景的电力调度评估；8 个 LLM。 | 六项指标（事实性、逻辑性、稳定性、安全性、公平性、表达性）/ 24 个子指标。 | [→](../works/elecbench.md) |
| EnergyBridge | 2026 | 居民虚拟电厂运行与需求响应——通过耦合容量申报、住户授权与 HVAC/电动车/家电负荷转移的物理执行，把住户的物理灵活性转化为可靠、经授权的电网容量。 | 50 个七天 EnergyPlus 建筑能耗模拟，覆盖五户家庭、两个地区（天津、柏林）与五种方法（350 个户-日回合；每个含一次 18:00–19:00 需求响应事件），外加一项留出的容量申报审计；由 LLM 用户参与模拟器决定授权。 | 从 EnergyPlus 24.1.0 计量的物理结果——门控接受（授权）率、事件窗口能量与容量承诺可靠性（获接受 ∧ 交付落在承诺 ±20% 内）；授权模拟器对照 584 条人类角色扮演回应验证（接受率平均绝对误差 5.3 个百分点）。 | [→](../works/energybridge.md) |

## Related Works

- [EnergyBridge](../works/energybridge.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [ElecBench](../works/elecbench.md)
