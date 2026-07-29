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
- **面向 cost-aware planning 的专用数据集。** [CATP-LLM / OpenCATP](../works/catp-llm.md) 贡献了 OpenCATP——被称为首个面向 cost-aware planning 的数据集（11,100 样本），其中工具执行成本（如执行时间）与任务性能联合打分。其配对的规划方法属于本仓库范围之外的 agent 构建工作；数据集才是此处记录的 resource-aware 评估贡献。
- **按保真度定价的测量预算。** [MaD Physics](../works/mad-physics.md) 对每次观测收取随其精度上升的成本，并对每个 trial 的总花费设上限，使 agent 必须在固定预算下分配测量，以推断一条未知的——有时被改动的——物理定律。
- **作为在线控制信号的预算。** [BAGEN](../works/bagen.md) 让 agent 在每一轮预测剩余预算的上界与下界并标记不可行，把资源使用作为逐步的估计目标而非执行后的统计来评分。
- **把评估调用作为预算化的资源。** [VeRO / VeRO-Bench](../works/vero.md) 在硬性评估调用预算下 benchmark 优化其他 agent 的 coding agent：对目标 agent 的每次打分都经过门控评估器，扣减 n_E ≤ B 并阻断超额请求，对应昂贵查询下的黑盒优化设定；B ∈ {2, 4, 8, 16, 32} 的预算消融把预算效应与能力效应区分开。
- **成本–性能前沿式报告。** 另一些工作在 accuracy 之外同时报告 token 或 dollar 成本，用于在 Pareto 前沿上而非单一 accuracy 数字上做比较。这是分析时的资源意识，而非 benchmark 内部的资源意识。

## Comparison

| Benchmark | Year | 资源单位 | 资源角色 | 场景 | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | 可配置的原子/组合工具成本 | 一等目标——为成本最优做规划 | 动态（阻断事件）；报告约 40% 静态→动态下降 | [→](../works/costbench.md) |
| SimulCost | 2026 | 仿真时间 + 实验资源 | 一等目标——预算下的参数调优 | 单轮与多轮；13 个仿真器 | [→](../works/simulcost.md) |
| CATP-LLM / OpenCATP | 2024 | 归一化工具价格（USD；执行时间 + 内存） | 通过 Quality of Plan 与性能联合报告（QoP = α·perf − (1−α)·cost） | 111 个工具规划任务 / 11,100 样本 | [→](../works/catp-llm.md) |
| MaD Physics | 2026 | 测量成本（按保真度定价的观测） | agent 分配的每个 trial 固定预算 | 模拟经典 / 流体 / 量子物理 | [→](../works/mad-physics.md) |
| BAGEN | 2026 | Token；时间 / 占用 / 成本 | 预测目标 + 提前停止目标 | 谜题 / 检索 / 编码 / 供应链 | [→](../works/bagen.md) |
| VeRO / VeRO-Bench | 2026 | 对目标 agent 的评估调用（门控预算 n_E ≤ B） | 强制硬约束——优化器须分配昂贵的评估 | 覆盖 5 个目标 agent 任务套件的 agent-harness 优化 | [→](../works/vero.md) |

## Open Questions

- **不同场景下的资源规范化。** 一美元的 API 支出、一美元的 tool-call 费用、一秒的 wall-clock 或仿真时间并不直接可比。哪一种"资源货币"应作为跨 benchmark 比较的标准？或者它们本就无法完全统一？
- **静态 vs. 动态的鲁棒性。** CostBench 报告了显著的静态–动态下降。这一差距是当前模型的属性，还是仅是特定扰动分布的属性？领域是否应就一套标准扰动分布达成共识？
- **报告 vs. 优化。** 将资源作为一等目标的 benchmark 强制 agent 在预算下规划；仅报告资源使用的 benchmark 则没有。是否应显式区分这两类，以避免它们的数字被无声地拿去横向比较？
- **Token 成本 vs. tool-use 成本。** 聚合排行榜是否应仅报告 token（可移植、模型可比）还是也报告 tool-use 资源（在科学上有意义但依赖领域）？

## Related Works

- [CostBench](../works/costbench.md) — 动态 tool-use 条件下的成本最优规划。
- [SimulCost](../works/simulcost.md) — 覆盖 13 个仿真器的 cost-aware 物理仿真参数调优。
- [CATP-LLM / OpenCATP](../works/catp-llm.md) — OpenCATP，面向 cost-aware 工具规划的数据集（11,100 样本）。
- [MaD Physics](../works/mad-physics.md) — 模拟物理中按保真度定价的测量预算；agent 在测量的质与量之间权衡以推断被改动的物理定律。
- [BAGEN](../works/bagen.md) — 跨 token 与多资源 agent 的渐进式预算区间预测与可训练的提前停止。
- [VeRO / VeRO-Bench](../works/vero.md) — 在门控评估调用预算下把 coding agent 作为 agent 优化器来 benchmark。

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. 指出 cost-efficiency 是当前 agent 评估中覆盖不足的维度。<https://arxiv.org/abs/2503.16416>
