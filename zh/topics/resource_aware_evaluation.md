# Resource-aware Evaluation

## Definition

Resource-aware evaluation 把资源消耗——token、tool-call 费用、wall-clock 时间、计算资源、仿真时间或某种领域特定的成本单位——纳入 benchmark 所衡量的范围，而不仅作为事后统计。在其最强的形式下，某种资源（通常是成本）被作为 agent 必须与任务成功一起权衡的显式优化目标。

## Motivation

Agent 能力与资源消耗往往同向变化：更强的模型通常更贵；更长的 trajectory 通常能得到更好的答案。因此，孤立地评估能力等价于奖励"不惜代价解题"——这与科学或生产场景下的部署条件并不一致。

有两个划分维度：

- **资源作为额外报告的指标** vs. **资源作为显式目标**：前者在分析阶段浮现 trade-off；后者考察 agent 是否能在预算下**规划**。
- **仅 token 成本** vs. **tool-use 成本（仿真时间、实验资源）**：只看 token 成本会遗漏许多科学工作流的主要成本。

## Existing Approaches

- **在 tool use 中把成本作为一等目标。** [CostBench](../works/costbench.md) 把成本最小化本身设为任务，在 travel-planning 场景下具有可配置的原子/组合工具成本，并通过阻断事件迫使重规划。
- **Token 之外的 tool-use 成本，聚焦科学仿真。** [SimulCost](../works/simulcost.md) 把 cost-aware 评估扩展到物理仿真参数调优，显式建模仿真时间与实验资源成本，覆盖 13 个仿真器，并直接与传统方法对比。
- **成本–性能前沿式报告。** 另一些工作在 accuracy 之外同时报告 token 或 dollar 成本，用于在 Pareto 前沿上而非单一 accuracy 数字上做比较。这是分析时的资源意识，而非 benchmark 内部的资源意识。
- **交互预算作为资源约束。** [Frontier-Eng](../works/frontier-eng.md) 把 *propose-execute-evaluate 迭代次数*视为 47 个工程任务上的一等预算；论文的"深度 > 广度"发现——在受约束问题上深度更重要——本身就是关于"预算受限的 agent 应如何分配预算"的声明。

## Comparison

| Benchmark | Year | 资源单位 | 资源角色 | 场景 | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | 可配置的原子/组合工具成本 | 一等目标——为成本最优做规划 | 动态（阻断事件）；报告约 40% 静态→动态下降 | [→](../works/costbench.md) |
| SimulCost | 2026 | 仿真时间 + 实验资源 | 一等目标——预算下的参数调优 | 单轮与多轮；13 个仿真器 | [→](../works/simulcost.md) |
| Frontier-Eng | 2026 | 交互预算（propose-execute-evaluate 迭代数） | 有界预算塑形整个评估循环 | 工业级仿真器连续奖励 + 硬性可行性下的迭代优化 | [→](../works/frontier-eng.md) |

## Open Questions

- **不同场景下的资源规范化。** 一美元的 API 支出、一美元的 tool-call 费用、一秒的 wall-clock 或仿真时间并不直接可比。哪一种"资源货币"应作为跨 benchmark 比较的标准？或者它们本就无法完全统一？
- **静态 vs. 动态的鲁棒性。** CostBench 报告了显著的静态–动态下降。这一差距是当前模型的属性，还是仅是特定扰动分布的属性？领域是否应就一套标准扰动分布达成共识？
- **报告 vs. 优化。** 将资源作为一等目标的 benchmark 强制 agent 在预算下规划；仅报告资源使用的 benchmark 则没有。是否应显式区分这两类，以避免它们的数字被无声地拿去横向比较？
- **Token 成本 vs. tool-use 成本。** 聚合排行榜是否应仅报告 token（可移植、模型可比）还是也报告 tool-use 资源（在科学上有意义但依赖领域）？

## Related Works

- [CostBench](../works/costbench.md) — 动态 tool-use 条件下的成本最优规划。
- [SimulCost](../works/simulcost.md) — 覆盖 13 个仿真器的 cost-aware 物理仿真参数调优。
- [Frontier-Eng](../works/frontier-eng.md) — 固定交互预算下的迭代式工程优化。

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. 指出 cost-efficiency 是当前 agent 评估中覆盖不足的维度。<https://arxiv.org/abs/2503.16416>
