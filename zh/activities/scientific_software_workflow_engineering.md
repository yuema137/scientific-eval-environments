# 科学软件与工作流工程

> [English](../../activities/scientific_software_workflow_engineering.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 生产、修复、集成或执行科学与工程软件或工作流的能力——科学代码生成、数值算法实现、仓库工程、流水线构建，以及硬件描述与形式化规约代码。

## Scope

涵盖科学与工程软件/工作流产物（含 HDL/RTL、形式化模型、数值求解器与科学流水线），以软件正确性为评测核心。不含通用的应用或 Web 软件工程，也不含为完成另一活动而顺带编写的辅助脚本。

## Task Patterns

**HDL/RTL 生成与硬件验证。** 有一批工作聚焦于硬件描述与形式化硬件代码。[RTLLM](../works/rtllm.md) 和 [VerilogEval](../works/verilogeval.md) 根据自然语言生成设计/RTL Verilog，并通过仿真评分；[RTL-Repo](../works/rtl-repo.md) 将其扩展到仓库级的跨文件 Verilog 补全，[VHDL-Eval](../works/vhdl-eval.md) 扩展到 VHDL，[HLS-Eval](../works/hls-eval.md) 扩展到高层次综合。[CVDP](../works/cvdp.md) 将 RTL 生成、调试与验证整合到 783 道题目中。以验证为核心的工作则生成断言与测试平台：[AssertionBench](../works/assertionbench.md) 针对经形式化验证的标准答案生成 SystemVerilog 断言，[FVEval](../works/fveval.md) 将形式化验证拆解为 NL2SVA 与 Design2SVA 子任务，并由 Cadence Jasper 检查。

**PDE/数值求解器与仿真代码生成。** 许多工作要求 agent 编写数值代码或仿真输入文件。[CodePDE](../works/codepde.md)、[PDEAgent-Bench](../works/pdeagent-bench.md) 和 [PDE-Controller](../works/pde-controller.md) 面向 PDE 求解器；[FEM-Bench](../works/fem-bench.md) 和 [FEABench](../works/feabench.md) 覆盖有限元代码；[CFDLLMBench](../works/cfdllmbench.md) 横跨 CFD 知识、Python 求解器与 OpenFOAM 案例；[MooseBench](../works/moosebench.md) 从 MOOSE 输入文件中重建其所编码的 PDE；[SimBench](../works/simbench.md) 则构建 Chrono 数字孪生。[CRAFTS](../works/crafts.md) 把这一思路延伸到化工流程仿真建模：先产出带类型的中间表示，通过确定性的 IDAES/Pyomo 关卡校验后，才据此构建可执行模型。领域仿真工作流的执行体现在 [VASPBench](../works/vaspbench.md)、[MDArena](../works/mdarena.md) 和 [Collider-Bench](../works/collider-bench.md) 中。

**科学仓库工程与研究复现。** 这些工作让 agent 在真实代码库和论文上开展工作。[AInsteinBench](../works/ainsteinbench.md) 将 SWE-bench 的维护者 PR 范式移植到六个生产级科学仓库；[SUPER](../works/super.md) 和 [ML-Bench](../works/ml-bench.md) 考察真实研究仓库的搭建与运行。论文复现类工作包括 [PaperBench](../works/paperbench.md)、[EXP-Bench](../works/exp-bench.md)、[PRBench](../works/prbench.md)、[QMP-Bench](../works/qmp-bench.md)、[NatureBench](../works/naturebench.md) 和 [gwBenchmarks](../works/gwbenchmarks.md)。

**ML 研究代码实现与 ML 工程。** 一大批工作把 ML 研究/工程本身作为要编写的代码产物。[MLAgentBench](../works/mlagentbench.md)、[MLE-bench](../works/mle-bench.md)、[MLE-Dojo](../works/mle-dojo.md)、[MLRC-Bench](../works/mlrc-bench.md)、[RE-Bench](../works/re-bench.md) 和 [DevAI](../works/devai.md) 让 agent 训练模型、优化代码，或对照基线与排行榜提出新方法。[ResearchCodeBench](../works/researchcodebench.md) 实现近期论文中的新贡献，[SciCode](../works/scicode.md) 则覆盖由科学家精心编排的、横跨各自然科学子领域的研究编程。

**生物信息学/数据科学流水线与跨领域工作流。** 流水线构建与数据科学编程类工作包括 [GenoTEX](../works/genotex.md)、[BioAgent Bench](../works/bioagent-bench.md)、[MedAgentGym](../works/medagentgym.md)、[BioXArena](../works/bioxarena.md)、[DA-Code](../works/da-code.md)、[ScienceAgentBench](../works/scienceagentbench.md) 和 [MatTools](../works/mattools.md)（pymatgen）。形式化规约代码由 [SysMoBench](../works/sysmobench.md)（TLA+ 模型）代表。更广义的容器化科学计算测评框架有 [Terminal-Bench Science](../works/terminal-bench-science.md) 和结构工程工作台 [StructureClaw](../works/structureclaw.md)。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| ML-Bench | 2023 | 根据任务描述生成仓库级 ML 代码 | 覆盖 18 个 GitHub 仓库的 9,641 个任务；文本到代码 + Linux 沙箱 agent | Pass@5 / 自主执行成功率 | [卡片](../works/ml-bench.md) |
| MLAgentBench | 2023 | 编写提升指标的 ML 实验代码 | 13 个任务；ReAct agent 读写文件并运行实验 | 相对起始代码基线的实测提升 | [卡片](../works/mlagentbench.md) |
| RTLLM | 2023 | 根据自然语言生成设计 RTL（Verilog） | 29 个手工设计（v2.0：50 个）；静态生成 | 语法、功能与设计质量通过 | [卡片](../works/rtllm.md) |
| VerilogEval | 2023 | 根据题目/规格描述生成 Verilog RTL | 156 道 HDLBits 题目；静态生成 | 仿真校验的功能正确性（pass@k） | [卡片](../works/verilogeval.md) |
| AssertionBench | 2024 | 为硬件设计生成 SystemVerilog 断言 | 100 个 OpenCores Verilog 设计；静态生成 | 功能正确断言的占比 | [卡片](../works/assertionbench.md) |
| DA-Code | 2024 | 数据科学数据整理/分析代码 | Docker 沙箱中的 agentic 任务 | 基于执行的准确率（最佳 30.5%） | [卡片](../works/da-code.md) |
| DevAI / Agent-as-a-Judge | 2024 | 根据需求开展 AI/ML 开发项目 | 55 个任务、365 条层级化需求；agentic | 逐步的需求满足度（Agent-as-a-Judge） | [卡片](../works/devai.md) |
| FVEval | 2024 | 为验证生成 SystemVerilog 断言/测试平台 | 三个子任务（NL2SVA-Machine/Human、Design2SVA） | 形式化工具（Cadence Jasper）验证 | [卡片](../works/fveval.md) |
| GenoTEX | 2024 | 基因表达分析流水线代码 | 覆盖 911 个数据集的 1,384 个基因-性状问题；agentic | 与专家编排的参考流水线/结果相匹配 | [卡片](../works/genotex.md) |
| MLE-bench | 2024 | 端到端 ML 工程解决方案 | 75 个 Kaggle 竞赛；scaffold 中的 agent | 对照排行榜的 Kaggle 奖牌阈值 | [卡片](../works/mle-bench.md) |
| RE-Bench | 2024 | ML 研究工程代码/kernel | 7 个开放式环境；agent 对阵 61 位专家 | 在 2/8/32 小时预算下相对参考的得分 | [卡片](../works/re-bench.md) |
| RTL-Repo | 2024 | 仓库级 Verilog 补全 | 4,000+ 个带完整仓库上下文的样本；静态 | 编辑相似度 / 精确匹配 | [卡片](../works/rtl-repo.md) |
| SciCode | 2024 | 由科学家编排的研究代码 | 80 道主问题、338 道子问题、16 个子领域 | 对照参考解与测试用例通过 | [卡片](../works/scicode.md) |
| ScienceAgentBench | 2024 | 自包含的科学工作流 Python 程序 | 来自 44 篇论文、四个学科的 102 个任务 | 程序/执行结果的正确性与成本 | [卡片](../works/scienceagentbench.md) |
| SimBench | 2024 | Chrono 多物理场数字孪生代码 | 覆盖 34 个系统的 102 个任务；多轮 | 规则加人工指导下的 LLM-judge 评分 | [卡片](../works/simbench.md) |
| SUPER | 2024 | 搭建并运行研究仓库 | 45 个端到端 + 152 个子问题 + 602 个自动问题；agentic | 端到端成功率（最佳 16.3%） | [卡片](../works/super.md) |
| VHDL-Eval | 2024 | VHDL 代码生成 | 202 道带自校验测试平台的题目；静态 | 测试平台校验的功能正确性 | [卡片](../works/vhdl-eval.md) |
| AInsteinBench | 2025 | 科学仓库 PR 解决 | 6 个生产级科学仓库中的维护者 PR 任务；agentic | 可执行环境中的测试驱动验证 | [卡片](../works/ainsteinbench.md) |
| CFDLLMBench | 2025 | CFD 知识、Python 求解器、OpenFOAM 案例 | 三个层级（CFDQuery/Code/Foam）共 240 个任务 | 可执行性、数值误差、收敛性 | [卡片](../works/cfdllmbench.md) |
| CodePDE | 2025 | PDE 求解器代码生成 | 具代表性的 PDE 问题，配以迭代式改进 | 求解器在 PDE 问题上的数值精度 | [卡片](../works/codepde.md) |
| CVDP | 2025 | RTL 设计、调试与验证代码 | 783 个问题、13 个类别；agentic + 非 agentic | pass@1（代码生成最佳 <=34%） | [卡片](../works/cvdp.md) |
| EXP-Bench | 2025 | 端到端 AI 研究实验代码 | 来自 51 篇论文的 461 个任务，起始代码不完整 | 设计/实现/执行正确性（子任务） | [卡片](../works/exp-bench.md) |
| FEABench | 2025 | 通过 API 驱动 COMSOL 完成 FEA 求解 | 多物理场自然语言问题；agentic API 迭代 | 可执行的 API 调用 / 计算结果正确 | [卡片](../works/feabench.md) |
| FEM-Bench | 2025 | FEM 函数与单元测试 | 33 个函数编写任务 + 测试赛道；5 次尝试 | 客观验证 / 联合成功率 | [卡片](../works/fem-bench.md) |
| HLS-Eval | 2025 | 高层次综合代码与优化改动 | 94 个设计、两个任务；框架化测评 | 在 Vitis HLS 上解析/编译/运行/综合（pass@k） | [卡片](../works/hls-eval.md) |
| MatTools | 2025 | pymatgen 工具理解与 Python 代码 | 69,225 个 QA 对 + 49 个任务（138 个子任务）；执行 | 正确执行得出的材料性质答案 | [卡片](../works/mattools.md) |
| MedAgentGym | 2025 | 生物医学数据科学编程 | 72,413 个实例、129 个类别；带反馈的沙箱 | 可验证标准答案的成功（可 RL 训练） | [卡片](../works/medagentgym.md) |
| MLE-Dojo | 2025 | 交互式 gym 中的 ML 工程解决方案 | 200+ 个 Kaggle 挑战；结构化反馈循环 | 迭代改进 / 长时程质量 | [卡片](../works/mle-dojo.md) |
| MLRC-Bench | 2025 | 实现新颖的 ML 研究方法 | 7 个竞赛任务；scaffold 化 agent | 弥合基线到人类差距的比例（最佳 9.3%） | [卡片](../works/mlrc-bench.md) |
| PaperBench | 2025 | 从零复现 AI 论文 | 20 篇 ICML 论文、8,316 个 rubric 子任务；agentic | rubric 评分的复现得分（LLM judge） | [卡片](../works/paperbench.md) |
| PDE-Controller | 2025 | STL 自形式化 + PDE 控制程序 | 热/波系统；人工案例 + 200 万合成 | 推理/自形式化/综合指标；效用增益 | [卡片](../works/pde-controller.md) |
| ResearchCodeBench | 2025 | 将新颖 ML 论文贡献实现为代码 | 来自 20 篇近期论文的 212 个挑战；静态 | 正确的可执行实现（最佳 37.3%） | [卡片](../works/researchcodebench.md) |
| SysMoBench | 2025 | TLA+ 形式化系统模型 + TLC 配置 | 11 个并发/分布式产物，175-5,360 SLOC | 语法/运行时/一致性/不变量检查（自动化） | [卡片](../works/sysmobench.md) |
| AutoDFT / VASPBench | 2026 | 自主 DFT（VASP）工作流执行 | 34 个任务、9 种计算类型；闭环 agent | 任务级成功 + 性质精度（94.1%） | [卡片](../works/vaspbench.md) |
| BioAgent Bench | 2026 | 端到端生物信息学流水线 | 精选的 RNA-seq/变异检测/宏基因组；agentic | LLM 评分的流水线进展 + 结果有效性 | [卡片](../works/bioagent-bench.md) |
| BioXArena | 2026 | 多模态生物医学 ML 模型 | 76 个任务、9 个领域；2 小时单 GPU 环境 | 隐藏标签、具生物学意识的评分（0-1） | [卡片](../works/bioxarena.md) |
| Collider-Bench | 2026 | LHC 分析复现（仿真流水线） | 10 个 CMS SUSY 任务；容器化公开技术栈 | 直方图相对隐藏参考产额的保真度 | [卡片](../works/collider-bench.md) |
| CRAFTS | 2026 | 可执行的 IDAES/Pyomo 化工过程仿真模型 | OpenIDAES-450；82 个冻结的留出算例、带类型的中间表示、确定性关卡校验 | Workflow Success 91.5% + 单元/物流/连接的宏平均 F1 | [卡片](../works/crafts.md) |
| gwBenchmarks | 2026 | 引力波建模/代理模型代码 | 8 个高精度任务；>10^8 核时数据 | 外部框架在接近 1e-4 误差下的评分 | [卡片](../works/gwbenchmarks.md) |
| MDArena | 2026 | 分子动力学工作流代码 | 50 个容器化任务、29 个系统、14 种协议 | 严格成功率 + 过程部分得分 | [卡片](../works/mdarena.md) |
| MooseBench | 2026 | MOOSE 多物理场仿真输入文件 | 220 个带 PDE 级标准答案的案例 | 意图保真度得分（重建 PDE 匹配） | [卡片](../works/moosebench.md) |
| NatureBench | 2026 | 匹配已发表的 SOTA 科学代码 | 来自 Nature 系列论文、六个领域的 90 个任务 | 在信息防火墙下达到/超越已发表 SOTA | [卡片](../works/naturebench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | 用代码搭建一条神经科学数据到发现的流程 | 9 个计算任务（7 个阶段 + 端到端）；兼容 Harbor | 各阶段代码正确性，对照专家标注与遗留代码库 | [卡片](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| PDAgent-Bench | 2026 | 为 VLSI 物理设计生成 EDA 工具脚本 | 210 个脚本生成任务 + 闭环流程；Innovus/ICC2/OpenROAD | 经执行验证的脚本（pass@1/5） | [卡片](../works/pdagent-bench.md) |
| PDEAgent-Bench | 2026 | 面向 FEM 库的 PDE 求解器代码 | 645 个实例、6 个类别；DOLFINx/Firedrake/deal.II | 分阶段的可执行性、精度、效率 | [卡片](../works/pdeagent-bench.md) |
| PRBench | 2026 | 从论文复现物理研究 | 30 个专家精选任务、11 个子领域；沙箱 | 与出版结果的定量匹配（CSV rubric） | [卡片](../works/prbench.md) |
| QMP-Bench | 2026 | 量子多体仿真代码 | 来自 21 种期刊的 100 个端到端任务 | 编码正确性 + 物理有效性 | [卡片](../works/qmp-bench.md) |
| SciVisAgentBench | 2026 | 生成可执行的科学可视化代码 | 108 个案例；ParaView/napari/MD/拓扑，经 CLI/MCP/Python | 图像指标 + 代码检查器 + 基于规则的验证器 | [卡片](../works/scivisagentbench.md) |
| StructureClaw | 2026 | 结构工程工作流（建模到求解器再到校核） | 150 个场景；配备 OpenSees 的产物工作台 | 模型匹配 + 相对冻结参考的数值一致 | [卡片](../works/structureclaw.md) |
| Terminal-Bench Science | 2026 | 容器化科学计算工作流 | 5 个领域的 8 个任务（目标 100+）；agentic | pytest 确定性程序化验证 | [卡片](../works/terminal-bench-science.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [ML-Bench](../works/ml-bench.md)
- [MLAgentBench](../works/mlagentbench.md)
- [RTLLM](../works/rtllm.md)
- [VerilogEval](../works/verilogeval.md)
- [AssertionBench](../works/assertionbench.md)
- [DA-Code](../works/da-code.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [FVEval](../works/fveval.md)
- [GenoTEX](../works/genotex.md)
- [MLE-bench](../works/mle-bench.md)
- [RE-Bench](../works/re-bench.md)
- [RTL-Repo](../works/rtl-repo.md)
- [SciCode](../works/scicode.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SimBench](../works/simbench.md)
- [SUPER](../works/super.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [CodePDE](../works/codepde.md)
- [CVDP](../works/cvdp.md)
- [EXP-Bench](../works/exp-bench.md)
- [FEABench](../works/feabench.md)
- [FEM-Bench](../works/fem-bench.md)
- [HLS-Eval](../works/hls-eval.md)
- [MatTools](../works/mattools.md)
- [MedAgentGym](../works/medagentgym.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [PaperBench](../works/paperbench.md)
- [PDE-Controller](../works/pde-controller.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [SysMoBench](../works/sysmobench.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [BioXArena](../works/bioxarena.md)
- [Collider-Bench](../works/collider-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [MDArena](../works/mdarena.md)
- [MooseBench](../works/moosebench.md)
- [NatureBench](../works/naturebench.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [PRBench](../works/prbench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [StructureClaw](../works/structureclaw.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [CRAFTS](../works/crafts.md)
