# Resource-aware Evaluation

> [English](../../topics/resource_aware_evaluation.md) | **简体中文** · [← 全部 topics](./README.md)

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
- **给物理发现设观测预算。** [Gravity-Bench-v1](../works/gravity-bench.md) 限定 agent 对模拟二体引力系统可观测的次数，让实验设计本身进入评分范围；据官方项目页，最佳模型从全量数据下的 74% 跌到预算下的 49%。
- **把 oracle 调用作为分子设计中的定价资源。** [SMDD-Bench](../works/smdd-bench.md) 为 502 个保证有解的药物设计任务设定有限的 oracle 调用预算，探索必须规划而非穷举；最佳前沿模型仅解出 40.2%。
- **把诊断成本写上记分表。** [SDBench](../works/sdbench.md) 对 agent（与 21 位医生）的每次就诊与检查计费，守门人只应答被明确提出的询问，按准确率-成本前沿评分；改变编排方式比换模型更能移动这条前沿。
- **成本本身即任务。** [ChemCost](../works/chemcost.md) 不是给 agent 的开销设预算，而是让 agent 计算一个反应的成本——对照冻结价格快照，配无 judge 的精确真值与阶段级失败诊断。
- **作为在线控制信号的预算。** [BAGEN](../works/bagen.md) 让 agent 在每一轮预测剩余预算的上界与下界并标记不可行，把资源使用作为逐步的估计目标而非执行后的统计来评分。
- **把评估调用作为预算化的资源。** [VeRO / VeRO-Bench](../works/vero.md) 在硬性评估调用预算下 benchmark 优化其他 agent 的 coding agent：对目标 agent 的每次打分都经过门控评估器，扣减 n_E ≤ B 并阻断超额请求，对应昂贵查询下的黑盒优化设定；B ∈ {2, 4, 8, 16, 32} 的预算消融把预算效应与能力效应区分开。
- **迭代式设计优化上的交互预算。** [Frontier-Eng](../works/frontier-eng.md) 为每个真实工程任务的 propose-execute-evaluate 循环设置固定交互预算：agent 必须分配有限次数的仿真器交互，在连续奖励与硬性可行性约束下细化候选设计，使 benchmark 内在具备 resource-aware 属性。
- **把经济一致性作为测量对象。** [EcoAgent-Bench](../works/ecoagent-bench.md) 在 304 个任务上为每个动作定价并设定显式的单任务预算，同时把「该升级」与「该省钱」的任务成对分组，使一味花钱或一味省钱的单边策略无法得高分。Tool-API agent 的经济一致性至多 7.3%；预算从低到高扫过一遍，GPT-5.4 的升级率也只从 0% 升到 3%。
- **给 harness 优化设评估预算。** [HarnessOpt-Bench](../works/harnessopt-bench.md) 给优化器 LLM 一个种子 harness、评估反馈与固定的目标评估预算，在 TEE 审计的循环内运行，以留出测试集上相对种子的归一化增益评分；在 4 个任务、5 个优化器模型、111 次计分运行中，优化器模型之间拉开的差距大于它们借以行动的编码 harness 之间的差距。
- **把效率写进评分 rubric。** [MASSE](../works/masse.md) 既不给 agent 设预算，也不把成本单列出来报告：它的整体系统 benchmark MASEB 在 100 分里划出 20 分给「效率与鲁棒性」，而负责评阅一整份结构工程分析日志的 GPT-5 评审，会把总 token 用量与总运行时间与四项分数一并写进同一个 JSON 对象——于是一条又准又贵的流水线拿不到满分。论文随附的四个后端之间的成本/运行时权衡分析，读的也正是这同一批测量值。
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
| Frontier-Eng | 2026 | 仿真器交互（每任务固定预算） | 对 propose-execute-evaluate 循环的硬性上限 | 真实工程优化；47 个任务、5 个类别 | [→](../works/frontier-eng.md) |
| EcoAgent-Bench | 2026 | 显式单任务预算下的定价动作 | 一等目标——升级/省钱成对分组上的经济一致性 | 304 个源自 QA 的任务、5 个族；tool-API 与 workspace-CLI 两种设定 | [→](../works/ecoagent-bench.md) |
| HarnessOpt-Bench | 2026 | 目标评估调用（固定预算，TEE 计量） | 对优化-评估循环的强制硬约束 | Harness 优化；4 任务 × 5 个优化器 LLM，111 次计分运行 | [→](../works/harnessopt-bench.md) |
| Gravity-Bench-v1 | 2025 | 对模拟系统的观测（据官方项目页每次运行至多 100 次） | 对实验设计的强制预算；报告全量与预算下的差距 | 模拟双星上的引力物理发现 | [→](../works/gravity-bench.md) |
| SMDD-Bench | 2026 | oracle 调用（有限的单任务预算） | 对设计空间探索的强制硬约束 | 小分子药物设计；502 个有解任务、102 个靶点 | [→](../works/smdd-bench.md) |
| SDBench | 2025 | 就诊与诊断检查的费用 | 与准确率联合评分，构成准确率-成本前沿 | 带信息守门人的 304 个 NEJM-CPC 病例序贯诊断 | [→](../works/sdbench.md) |
| ChemCost | 2026 | 冻结价格快照中的供应商报价与可购包装 | 成本即任务本身——agent 对照精确真值计算反应成本 | 反应定价；1,427 个反应、230,775 条报价；含噪声注入下的鲁棒性评测 | [→](../works/chemcost.md) |
| MASSE | 2025 | 总 token 用量与总运行时间，由评审与质量分一并给出 | 计分项——「效率与鲁棒性」在 MASEB 的 100 分中占 20 分；同一批数字还支撑了四个后端之间的成本/运行时权衡分析 | 多智能体结构工程工作流；100 道经专家校验的题目，每道跑十次 | [→](../works/masse.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | 每次流程执行的墙钟运行时间与峰值内存；token 成本刻意未测，并被列为一项局限 | 只是报告出来的测度，而非预算——运行时间与内存与科学输出并列，两个 agent 之间「快」与「可审计」的取舍就从这里读出来 | 两个 agentic coding 系统在同一硬件上执行同一份引力波流程规格说明；共四次自主运行 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |

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
- [Frontier-Eng](../works/frontier-eng.md) — 固定仿真器交互预算下的迭代式工程优化。
- [EcoAgent-Bench](../works/ecoagent-bench.md) — 定价动作与显式预算下的经济决策，以经济一致性评分。
- [HarnessOpt-Bench](../works/harnessopt-bench.md) — LLM 在固定且经 TEE 审计的评估预算下优化 agent harness。
- [Gravity-Bench-v1](../works/gravity-bench.md) — 引力物理发现中预算受限的观测规划。
- [SMDD-Bench](../works/smdd-bench.md) — 有限 oracle 调用预算下、保证有解的药物设计。
- [SDBench](../works/sdbench.md) — 按准确率-成本前沿评分的序贯诊断。
- [ChemCost](../works/chemcost.md) — 把反应成本计算本身作为被测任务，配无 judge 的精确定价真值。
- [MASSE](../works/masse.md) — 在端到端结构工程工作流 benchmark 中，把 token 用量与运行时间作为 rubric 的一个计分项。
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) — 每一次自主流程运行都测量运行时间与峰值内存；两个 agent 产出的科学结果相同，速度与资源占用便成了它们之间的一条比较轴。

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. 指出 cost-efficiency 是当前 agent 评估中覆盖不足的维度。<https://arxiv.org/abs/2503.16416>
