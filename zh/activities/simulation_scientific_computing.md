# 模拟与科学计算

> [English](../../activities/simulation_scientific_computing.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 以计算方式求解科学系统的能力——构建、配置、执行、调试数值模拟与科学计算任务，或对其加以推理。

## Scope

涵盖 PDE 与有限元求解、分子动力学、蒙特卡罗、DFT、多物理场模拟器，以及模拟器/数字孪生的构建。若 benchmark 只是在内部使用模拟器而 agent 并未实质参与模拟本身，则不归入此类。

## Task Patterns

有一大类工作将科学计算构建为 **PDE 求解器代码生成**任务，其中被评分的产物是求解器本身，而非求解得到的场。[CodePDE](../works/codepde.md) 确立了对 LLM 生成的数值求解器进行评估的各个维度；[PDEAgent-Bench](../works/pdeagent-bench.md) 将其扩展到横跨三个 FEM 库（DOLFINx、Firedrake、deal.II）的 645 个实例，并采用可执行性、准确性、效率逐级递进的阶梯式评估；[CFDLLMBench](../works/cfdllmbench.md) 则加入了一个三层 CFD 套件，将 PDE 求解的 Python 代码与研究生水平的知识以及 OpenFOAM 操作结合起来。[FEM-Bench](../works/fem-bench.md) 以课程级的粒度对有限元代码生成进行考察，而 [MooseBench](../works/moosebench.md) 通过确定性地重建 MOOSE 输入文件所编码的 PDE，揭示了理解与生成之间的差距，从而捕捉那些能运行却求解了错误物理的模拟。

另一大类工作则**端到端地驱动真实的领域模拟器**，把专业软件本身当作评估界面。[FEABench](../works/feabench.md) 通过 API 操作 COMSOL Multiphysics；[SimBench](../works/simbench.md) 在多轮对话中构建 Chrono 数字孪生；[VASPBench](../works/vaspbench.md) 在闭环中规划、运行并修复 VASP DFT 计算；[StructureClaw](../works/structureclaw.md) 驱动以 OpenSees 为后端的结构分析工作台；[PowerAgentBench-SS](../works/poweragentbench-ss.md) 让 agent 调用电网模拟器进行 N-2 故障筛查。[HydroAgent](../works/hydroagent.md) 对运行中的 CREST 水文模型进行迭代率定，[SimulCost](../works/simulcost.md) 则在 13 个物理模拟器上对成本感知的参数调优进行基准测试。

第三大类是**化工流程模拟建模（flowsheeting）**，被评分的产物是一个真正能够收敛的过程模拟。[Simona](../works/simona.md) 以模拟收敛率（Simulation Convergence Rate）衡量把书面工艺描述转化为流程图的效果；[CRAFTS](../works/crafts.md) 构建可执行的 IDAES/Pyomo 模型，且必须先通过一道道确定性的晋级门槛——自由度闭合、初始化、求解器终止状态；[CeProBench](../works/ceprobench.md) 的 Parameter 维度则把候选操作参数放进 Aspen Plus 里实际运行，由热力学可行性而非文本相似度来决定得分。

第四大类工作聚焦于借助专门的模拟工具链**端到端复现已发表的研究**：[AutoMat](../works/automat.md) 复现计算材料科学的结论（DFT、MD、位错动力学）；[Collider-Bench](../works/collider-bench.md) 通过公开的 MadGraph/Pythia/Delphes 工具栈重现 LHC 上的搜寻；[QMP-Bench](../works/qmp-bench.md) 覆盖端到端的量子多体模拟；[MDArena](../works/mdarena.md) 则把真实的分子动力学工作流打包成容器化任务。[Terminal-Bench Science](../works/terminal-bench-science.md) 将容器化的科学计算工作流推广到五个自然科学领域。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| SimBench | 2024 | 面向 Chrono 多物理场模拟器的多轮数字孪生生成 | 102 个任务 / 34 个系统，33+ 个 LLM，3000+ 轮对话 | 在预定义规则下由 LLM 评判打分，并引入人类参与 | [卡片](../works/simbench.md) |
| CFDLLMBench | 2025 | 三层 CFD：知识、PDE Python 求解器、OpenFOAM 算例 | 240 个任务（90 道 MCQ、24 个代码、126 个 OpenFOAM 算例） | 可执行性、相对误差、数值收敛性 | [卡片](../works/cfdllmbench.md) |
| CodePDE | 2025 | 带迭代优化的 LLM 生成 PDE 数值求解器 | 代表性 PDE 问题（数量 TODO） | 在代表性 PDE 问题上的求解器准确性 | [卡片](../works/codepde.md) |
| FEABench | 2025 | 通过 API 驱动 COMSOL Multiphysics 求解 FEA 问题 | 自然语言描述的多物理场问题，agent 式 API 循环（数量 TODO） | 答案正确；88% 的 API 调用可执行率 | [卡片](../works/feabench.md) |
| FEM-Bench | 2025 | FEM/计算力学的函数编写以及单元测试编写 | 33 个函数任务 + 测试赛道，每个 5 次尝试 | 客观验证；联合成功率 | [卡片](../works/fem-bench.md) |
| AutoDFT / VASPBench | 2026 | 自主的 VASP DFT 计算，规划-运行-修复闭环 | 横跨 9 种 DFT 计算类型的 34 个任务 | 94.1% 任务成功率；可靠的性质预测 | [卡片](../works/vaspbench.md) |
| AutoMat | 2026 | 在 HPC 上端到端复现计算材料学的结论 | 85 条由领域专家甄选的结论，三种复现类型 | 支持或推翻结论的证据；54.1% 成功率 | [卡片](../works/automat.md) |
| CeProBench | 2026 | 在 Aspen Plus 中实际执行的操作参数闭环调优 | 20 个高保真 Aspen Plus 文件，91 个可调参数，65 个目标 | 经 Aspen 验证的可行性；收率/纯度/成本与收敛迭代次数 | [卡片](../works/ceprobench.md) |
| Collider-Bench | 2026 | 通过公开模拟工具栈重现 LHC 上的 SUSY 搜寻 | 来自四项 CMS 搜寻的 10 个模拟任务 | 直方图与隐藏产额的吻合度；LLM 溯源评判 | [卡片](../works/collider-bench.md) |
| CRAFTS | 2026 | 从需求描述与 PFD 出发构建可执行的 IDAES/Pyomo 过程模拟模型 | OpenIDAES-450，82 个冻结的留出算例，确定性的 IDAES/Pyomo 门槛检查 | Workflow Success 91.5%，外加设备/物流/连接的宏平均 F1 | [卡片](../works/crafts.md) |
| HydroAgent | 2026 | 率定运行中的 CREST 水文模型，重模拟循环 | 4 个留出的水文站（329-40,792 km2），从 20 轮中取最优 | 相对人类专家参考的 Nash-Sutcliffe 效率系数 | [卡片](../works/hydroagent.md) |
| MDArena | 2026 | 真实的分子动力学研究工作流 | 50 个容器化任务，29 个系统，14 种协议 | 严格成功率外加过程级部分得分 | [卡片](../works/mdarena.md) |
| MooseBench | 2026 | 带 PDE 真值的 MOOSE 多物理场输入文件生成 | 220 个算例，每个都带有预期的 PDE 契约 | 通过确定性 PDE 重建得到的意图保真度分数 | [卡片](../works/moosebench.md) |
| PDEAgent-Bench | 2026 | 面向三个 FEM 库的 PDE 求解器代码生成 | 645 个实例，6 个类别，11 个族（DOLFINx/Firedrake/deal.II） | 分阶段的可执行性、准确性、效率检查 | [卡片](../works/pdeagent-bench.md) |
| PowerAgentBench-SS | 2026 | 通过模拟器调用进行 agent 式稳态电网研究 | IEEE 39-bus 变体，DC 热稳定 N-2 故障搜索 | 隐藏评估器重新计算有效性；多指标打分 | [卡片](../works/poweragentbench-ss.md) |
| QMP-Bench | 2026 | 端到端的量子多体模拟复现 | 来自 21 种高影响力期刊的 100 个研究任务 | 编码正确性外加物理有效性 | [卡片](../works/qmp-bench.md) |
| Simona | 2026 | 把书面工艺描述转化为能够收敛的模拟流程图 | 1,000 段专家撰写的工艺描述；通过 HTTP API 驱动模拟器 | 模拟收敛率（80.3%）与设计耗时 | [卡片](../works/simona.md) |
| SimulCost | 2026 | 成本感知的物理模拟参数调优 | 2,947 个单轮任务 + 1,931 个多轮任务，13 个模拟器 | 在模拟时间/资源预算约束下的性能 | [卡片](../works/simulcost.md) |
| StructureClaw | 2026 | 操作带求解器后端的结构工程工作台 | 150 个场景：标准、交互式、多模态重建 | 相对冻结参考的模型匹配 + 数值一致性 | [卡片](../works/structureclaw.md) |
| Terminal-Bench Science | 2026 | 容器化的自然科学计算工作流 | 横跨 5 个领域的 8 个任务（目标 100+） | 基于 pytest 的确定性程序化验证 | [卡片](../works/terminal-bench-science.md) |

## Related Works

- [SimBench](../works/simbench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [CodePDE](../works/codepde.md)
- [FEABench](../works/feabench.md)
- [FEM-Bench](../works/fem-bench.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [AutoMat](../works/automat.md)
- [Collider-Bench](../works/collider-bench.md)
- [HydroAgent](../works/hydroagent.md)
- [MDArena](../works/mdarena.md)
- [MooseBench](../works/moosebench.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [QMP-Bench](../works/qmp-bench.md)
- [SimulCost](../works/simulcost.md)
- [StructureClaw](../works/structureclaw.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [CeProBench](../works/ceprobench.md)
- [CRAFTS](../works/crafts.md)
- [Simona](../works/simona.md)
