# 优化与工程设计

> [English](../../activities/optimization_engineering_design.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 在科学或工程目标与约束下，搜索配置、参数、材料、结构或设计方案的能力。

## Scope

涵盖参数与控制器调优、工程与逆向设计、材料与分子设计，以及仿真引导的设计空间搜索。不因底层 ML 模型经由优化训练而归入此类——优化必须是受评的 agent 任务本身。

## Task Patterns

一大类任务聚焦于**电子与硬件设计**。模拟电路方面的工作由 [AnalogCoder](../works/analogcoder.md)（面向模拟电路、无需训练的代码生成 agent）和 [AnalogXpert](../works/analogxpert.md)（基于 SPICE、通过模块选择与连接实现拓扑综合）覆盖。数字与硬件代码设计涵盖 [CVDP](../works/cvdp.md)（全面的 RTL 设计、验证与调试）和 [HLS-Eval](../works/hls-eval.md)（自然语言到 HLS 的生成与优化改写）。与之相邻的工程控制与电网工作包括 [ControlAgent / ControlEval](../works/controleval.md)（面向稳定性/性能指标迭代调节控制器）和 [PowerAgentBench-SS](../works/poweragentbench-ss.md)（电网稳态故障筛查与缓解）。

第二大类是**分子与药物设计**，其指令或目标往往对应多种有效结构：[TOMG-Bench](../works/tomg-bench.md)（开放域分子编辑、优化与定制化生成）和 [SMDD-Bench](../works/smdd-bench.md)（面向蛋白靶点、带预算约束的多轮小分子药物设计）。[Aviary](../works/aviary.md) 提供了蛋白质工程与分子克隆环境，[SciAgentArena](../works/sciagentarena.md) 则在多个生物医学领域纳入了优化与药物发现类任务。

第三大类是**仿真引导的参数调优，以及在仿真器反馈下的迭代式工程设计**：[HydroAgent](../works/hydroagent.md)（校准业务化水文模型以最大化 NSE）、[SimulCost](../works/simulcost.md)（在多种物理仿真器上进行成本感知的参数调优）、[Frontier-Eng](../works/frontier-eng.md)（在工业级仿真器奖励与交互预算下的迭代式生成式设计）以及 [RE-Bench](../works/re-bench.md)（对照参考解的开放式 ML 研究工程优化）。

第四大类是**化工过程设计与装置运行决策**，其设计空间是一张流程图或一个操作点，而非控制器或分子。[Simona](../works/simona.md) 让 agent 挑选单元操作并调整其配置，直到流程图能够收敛；[CeProBench](../works/ceprobench.md) 的 Parameter 维度则在 Aspen Plus 中围绕收率、纯度与成本目标细化操作参数。另有两项工作把决策从设计阶段移到运行阶段，且方案只有经外部验证器放行才算可行：[容错控制教程环境](../works/ctrl-alt-recover.md)要求在注入装置故障后给出一个恢复模式或一组三元设定点，[AAE 框架](../works/aae-framework.md)则通过遍历装置的 P&ID 拓扑来评判所提出的控制动作。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AnalogCoder | 2024 | 无需训练的 LLM agent 通过 Python 代码设计模拟电路 | 模拟电路设计，自我纠错流程（24 项任务） | 成功设计电路；24 项中完成 20 项，优于 GPT-4o 的 15 项 | [卡片](../works/analogcoder.md) |
| AnalogXpert | 2024 | 通过模块选择与连接进行模拟拓扑综合 | SPICE 代码拓扑综合（30 个真实 + 2,000 个合成） | 合成 40% / 真实 23% 成功率，优于 GPT-4o 的 3% | [卡片](../works/analogxpert.md) |
| Aviary | 2024 | 面向克隆与蛋白质工程的科学 agent 环境 | 以语言为依托的 POMDP 环境（SeqQA、蛋白质稳定性、40 个蛋白质） | 达到或超越前沿 agent 与人类专家 | [卡片](../works/aviary.md) |
| ControlAgent / ControlEval | 2024 | 多 agent LLM 迭代调节控制器参数 | 覆盖多种系统类型的 500 项控制系统设计任务 | 在满足调节时间/相位裕度指标上取得高成功率 | [卡片](../works/controleval.md) |
| RE-Bench | 2024 | agent 优化 ML 研究工程代码与内核 | 7 个开放式 ML 研发环境，2/8/32 小时预算 | 对照参考解与人类专家的得分 | [卡片](../works/re-bench.md) |
| Speak-to-Structure / TOMG-Bench | 2024 | 自然语言驱动的开放域分子生成 | MolEdit/MolOpt/MolCustom，每个子任务 5,000 个样本 | 满足指令的有效分子（一对多） | [卡片](../works/tomg-bench.md) |
| CVDP | 2025 | Verilog 的 RTL 设计、验证与调试 | 783 个问题，13 个类别，含 agentic 与非 agentic | 生成任务的 Pass@1（SOTA <=34%） | [卡片](../works/cvdp.md) |
| HLS-Eval | 2025 | LLM 生成并优化可综合的 HLS 代码 | 94 个 HLS 设计，NL 到代码及优化改写 | 在 Vitis HLS 上可解析/可编译/可运行/可综合（pass@k） | [卡片](../works/hls-eval.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | 提出装置控制动作，并对照 P&ID 拓扑加以校验 | 5 个过程装置场景（其中 3 个取自 Tennessee Eastman），B0-B3 上下文阶梯，N=50 次运行 | 结构上可行的动作；在 43 个注入方案上的验证器召回率 | [卡片](../works/aae-framework.md) |
| Autonomous Fault-Tolerant Control Tutorial | 2026 | 在注入装置故障后选择恢复模式并调整设定点 | 两个可执行环境（混合模块、CSTR），支持按类型注入故障 | 经验证器认可的恢复动作；未报告参考分数 | [卡片](../works/ctrl-alt-recover.md) |
| CeProBench | 2026 | 过程操作参数的闭环优化 | 20 个 Aspen Plus 参数文件，91 个可调参数，65 个目标 | 收率/纯度/成本、Effective Score 与 Comprehensive Score、收敛迭代次数 | [卡片](../works/ceprobench.md) |
| EnergyBridge | 2026 | 生成约束感知的居民需求响应方案 | 基于 EnergyPlus 模型的 VPP 工作流（天津、柏林） | 授权率加容量承诺可靠性 | [卡片](../works/energybridge.md) |
| Frontier-Eng | 2026 | 在仿真器反馈下的迭代式生成式设计 | 47 项任务，5 个工程类别，预算受限 | 在硬可行性约束下的连续奖励 | [卡片](../works/frontier-eng.md) |
| HydroAgent | 2026 | agent 校准业务化 CREST 水文模型 | 4 个留出水文站（329-40,792 km2），20 轮取最优 | 对照人类专家参考的 Nash-Sutcliffe Efficiency | [卡片](../works/hydroagent.md) |
| PDAgent-Bench | 2026 | 约束下的 VLSI 物理设计优化 | 全流程实现加任务级问题；Innovus/ICC2/OpenROAD EDA | 时序收敛与 DRC 无违规布局；pass@1/5 | [卡片](../works/pdagent-bench.md) |
| PowerAgentBench-SS | 2026 | agent 筛查故障并提出电网缓解方案 | 验证预算下的 IEEE 39-bus DC 热稳定 N-2 搜索 | 隐藏评估器召回率、严重度后悔值、残余违规 | [卡片](../works/poweragentbench-ss.md) |
| SciAgentArena | 2026 | 涵盖优化与设计的生物医学研究任务 | 横跨五个生物医学领域、逐步验证的 200 项任务 | 在数据/优化/发现/有效性维度上逐步验证 | [卡片](../works/sciagentarena.md) |
| Simona | 2026 | 设计流程图拓扑并调整单元操作的配置 | 1,000 段专家撰写的工艺描述；通过 HTTP API 驱动仿真器 | 仿真收敛率（80.3%）与设计耗时 | [卡片](../works/simona.md) |
| SimulCost | 2026 | 物理仿真的成本感知参数调优 | 2,947 个单轮 + 1,931 个多轮任务，13 个仿真器 | 在仿真时间/资源预算下的调优质量 | [卡片](../works/simulcost.md) |
| SMDD-Bench | 2026 | 带预算约束的多轮小分子药物设计 | 502 个可解实例，102 个靶点，五种任务类型 | oracle 调用限制下的求解率（GPT-5.4: 40.2%） | [卡片](../works/smdd-bench.md) |

## Related Works

- [PDAgent-Bench](../works/pdagent-bench.md)
- [EnergyBridge](../works/energybridge.md)
- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [Aviary](../works/aviary.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [RE-Bench](../works/re-bench.md)
- [Speak-to-Structure / TOMG-Bench](../works/tomg-bench.md)
- [CVDP](../works/cvdp.md)
- [HLS-Eval](../works/hls-eval.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [HydroAgent](../works/hydroagent.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [SciAgentArena](../works/sciagentarena.md)
- [SimulCost](../works/simulcost.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [CeProBench](../works/ceprobench.md)
- [Simona](../works/simona.md)
