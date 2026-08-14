# 模拟与科学计算

> [English](../../activities/simulation_scientific_computing.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 以计算方式求解科学系统的能力——构建、配置、执行、调试数值模拟与科学计算任务，或对其加以推理。

## Scope

涵盖 PDE 与有限元求解、分子动力学、蒙特卡罗、DFT、多物理场模拟器，以及模拟器/数字孪生的构建。若 benchmark 只是在内部使用模拟器而 agent 并未实质参与模拟本身，则不归入此类。

## Task Patterns

有一大类工作将科学计算构建为 **PDE 求解器代码生成**任务，其中被评分的产物是求解器本身，而非求解得到的场。[CodePDE](../works/codepde.md) 确立了对 LLM 生成的数值求解器进行评估的各个维度；[PDEAgent-Bench](../works/pdeagent-bench.md) 将其扩展到横跨三个 FEM 库（DOLFINx、Firedrake、deal.II）的 645 个实例，并采用可执行性、准确性、效率逐级递进的阶梯式评估；[CFDLLMBench](../works/cfdllmbench.md) 则加入了一个三层 CFD 套件，将 PDE 求解的 Python 代码与研究生水平的知识以及 OpenFOAM 操作结合起来。[FEM-Bench](../works/fem-bench.md) 以课程级的粒度对有限元代码生成进行考察，而 [MooseBench](../works/moosebench.md) 通过确定性地重建 MOOSE 输入文件所编码的 PDE，揭示了理解与生成之间的差距，从而捕捉那些能运行却求解了错误物理的模拟。

另一大类工作则**端到端地驱动真实的领域模拟器**，把专业软件本身当作评估界面。[FEABench](../works/feabench.md) 通过 API 操作 COMSOL Multiphysics；[SimBench](../works/simbench.md) 在多轮对话中构建 Chrono 数字孪生；[VASPBench](../works/vaspbench.md) 在闭环中规划、运行并修复 VASP DFT 计算；[StructureClaw](../works/structureclaw.md) 驱动以 OpenSees 为后端的结构分析工作台；[PowerAgentBench-SS](../works/poweragentbench-ss.md) 让 agent 调用电网模拟器进行 N-2 故障筛查。[HydroAgent](../works/hydroagent.md) 对运行中的 CREST 水文模型进行迭代率定，[SimulCost](../works/simulcost.md) 则在 13 个物理模拟器上对成本感知的参数调优进行基准测试。

第三大类是**化工流程模拟建模（flowsheeting）**，被评分的产物是一份真正能够收敛的过程模拟。[Simona](../works/simona.md) 以模拟收敛率（Simulation Convergence Rate）衡量把书面工艺描述转化为流程图的效果；[CRAFTS](../works/crafts.md) 构建可执行的 IDAES/Pyomo 模型，且必须先通过一道道确定性的晋级关卡——自由度闭合、初始化、求解器终止状态；[CeProBench](../works/ceprobench.md) 的 Parameter 维度则把候选操作参数放进 Aspen Plus 里实际运行，由热力学可行性而非文本相似度来决定得分。

第四大类工作聚焦于借助专门的模拟工具链**端到端复现已发表的研究**：[AutoMat](../works/automat.md) 复现计算材料科学的结论（DFT、MD、位错动力学）；[Collider-Bench](../works/collider-bench.md) 通过公开的 MadGraph/Pythia/Delphes 工具栈重现 LHC 上的搜寻；[QMP-Bench](../works/qmp-bench.md) 覆盖端到端的量子多体模拟；[MDArena](../works/mdarena.md) 则把真实的分子动力学工作流打包成容器化任务。[Terminal-Bench Science](../works/terminal-bench-science.md) 将容器化的科学计算工作流推广到五个自然科学领域。

还有一条宇宙学脉络瞄准的是 **Boltzmann 求解器与结构形成代码**，受评的是求解器配置得如何，而不是一段量身写就的脚本。[CLASS 模型构建框架](../works/an-llm-driven-framework-for-cosmological-model-bui.md) 是其中最深入的一个——agent 要去改求解器自身的 C 源码来实现一个替代性暗能量模型，随后还得把它编译起来、算出功率谱，并让这些谱与 DESI、Planck、Pantheon+ 和 SH0ES 数据对照检验。[Plausible but Wrong](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) 走的是另一条路：把 CAMB 的配置与数值准确度作为两个相乘的独立项分别评分，从而把这样一种失败模式隔离出来——程序跑通了，求解器参数看着也合理，返回的物理却是错的，而且毫无报错信号。[SimAgents](../works/simagents.md) 处在同一工作流的最前端，要在代码用户手册所写的约束下，从已发表论文中重建 MP-Gadget 的配置，其中软件层面非法的参数类型与取值错误是分开计数的。

第五大类是**用土木工程求解器做结构分析**：一段自然语言的结构描述必须先变成求解器模型，再核对它算出的响应。这条脉络的结构复杂度逐级攀升——[可靠性与鲁棒性 agent 研究](../works/a-large-language-model-empowered-agent-for-reliabl.md)处理静定梁，[一套轻量的五 agent 系统](../works/a-lightweight-large-language-model-based-multi-age.md)转向多跨二维框架，[面向三维框架体系的 agentic 流水线](../works/agentic-large-language-models-for-automated-struct.md)则要求每一个受监测响应都落在人工搭建的 SAP2000 参考模型的 1% 以内。[Integrating LLMs for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md) 与[经 MCP 中介的静力分析数据集](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)分别借一套提示框架和一台工具服务器抵达同一个 OpenSeesPy 目标；[AutoBM](../works/autobm.md) 以基本周期校验所生成的建筑模型；[MASSE](../works/masse.md) 则把「建模并求解」这一步嵌进一整套咨询工作流中。另有两项工作把被模拟的对象移出了建筑框架：[Automating Structural Reliability Analysis](../works/automating-structural-reliability-analysis-with-a.md) 运行 FORM、蒙特卡罗与子集模拟来求构件可靠度，[LLM-EPANET](../works/llm-epanet.md) 则执行供水管网的水力与水质模拟。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| SimBench | 2024 | 面向 Chrono 多物理场模拟器的多轮数字孪生生成 | 102 个任务 / 34 个系统，33+ 个 LLM，3000+ 轮对话 | 在预定义规则下由 LLM 评判打分，并引入人类参与 | [卡片](../works/simbench.md) |
| Building Static Analysis with LLMs and MCP | 2025 | 通过 Model Context Protocol 服务器配置并运行 OpenSeesPy | 4 个钢筋混凝土框架，16 次分析，纯 GPT 与 GPT+MCP 对照 | 相对 ETABS 参考模型的相对误差（GPT+MCP 低于 1.427%） | [卡片](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) |
| CASCADE / SciSkillBench | 2025 | 为材料与化学任务运行仿真与专用计算工具包 | 116 个任务中的 40 个计算类任务；benchmark 运行时关闭记忆工具 | 在容差内自动比对标准答案（GPT-5 下 DeepSolver 总体 93.26%） | [卡片](../works/cascade.md) |
| CFDLLMBench | 2025 | 三层 CFD：知识、PDE Python 求解器、OpenFOAM 算例 | 240 个任务（90 道 MCQ、24 个代码、126 个 OpenFOAM 算例） | 可执行性、相对误差、数值收敛性 | [卡片](../works/cfdllmbench.md) |
| CodePDE | 2025 | 带迭代优化的 LLM 生成 PDE 数值求解器 | 代表性 PDE 问题（数量 TODO） | 在代表性 PDE 问题上的求解器准确性 | [卡片](../works/codepde.md) |
| Cosmological Model-Building with CLASS | 2025 | 为实现替代性宇宙学而改写 CLASS Boltzmann 求解器 | 容器化的 CLASS 3.3.0，三个顺序阶段，两个目标模型 | 能编译并算出可观测量；相对参考实现的最大相对偏差 | [卡片](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| FEABench | 2025 | 通过 API 驱动 COMSOL Multiphysics 求解 FEA 问题 | 自然语言描述的多物理场问题，agent 式 API 循环（数量 TODO） | 答案正确；88% 的 API 调用可执行率 | [卡片](../works/feabench.md) |
| FEM-Bench | 2025 | FEM/计算力学的函数编写以及单元测试编写 | 33 个函数任务 + 测试赛道，每个 5 次尝试 | 客观验证；联合成功率 | [卡片](../works/fem-bench.md) |
| Integrating LLMs for Automated Structural Analysis | 2025 | 由结构文字题驱动 OpenSeesPy 与 OpsVis | 20 道手工整理的二维框架题；三取优与五次运行的稳定性方案 | 变形与内力正确（GPT-4o 三取优 100%） | [卡片](../works/integrating-large-language-models-for-automated-st.md) |
| Lightweight Multi-Agent System for 2D Frame Analysis | 2025 | 为多跨二维框架构建 OpenSeesPy 有限元模型 | 20 道框架题，五个专职 agent，每题 10 次试验 | 正确生成模型的比例（多数题目超过 80%） | [卡片](../works/a-lightweight-large-language-model-based-multi-age.md) |
| LLM-EPANET | 2025 | 生成并执行 EPANET 供水管网模拟 | 3 个管网上的 69 条查询，5 个复杂度层级，沙箱内自调试循环 | 返回数值与手写参考脚本等价（56-81%） | [卡片](../works/llm-epanet.md) |
| MASSE | 2025 | 在结构咨询工作流内部构建并求解 OpenSeesPy 模型 | 100 道货架体系题目，4 套 rubric 评分基准，每题 10 次试验 | 由 GPT-5 judge 按 agent 角色给出的 rubric 得分（SAAB 最高 96.6） | [卡片](../works/masse.md) |
| SimAgents | 2025 | 从已发表论文中重建可执行的 MP-Gadget 配置 | 40 余项经标注的宇宙学模拟；参数集受手册约束 | 参数 micro-F1 为 98.67%，软件层面非法的 Type Error 单独计数 | [卡片](../works/simagents.md) |
| Agentic LLMs for 3D Frame Structural Analysis | 2026 | 生成不规则三维框架体系的可执行 SAP2000 模型 | 10 个不规则三维框架（开洞、退台、L/U/十字形平面），每个 10 次试验 | 全部受监测响应都落在人工搭建 SAP2000 模型的 1% 以内（平均 90%） | [卡片](../works/agentic-large-language-models-for-automated-struct.md) |
| AutoBM / BMEval | 2026 | 生成可执行的 OpenSeesPy 建筑模型，并以模态分析校验 | 128 项经专家验证的任务，沙箱执行，16 个模型 | Pass@k_strict：干净执行、周期落在容差内、给出合规结论 | [卡片](../works/autobm.md) |
| AutoDFT / VASPBench | 2026 | 自主的 VASP DFT 计算，规划-运行-修复闭环 | 横跨 9 种 DFT 计算类型的 34 个任务 | 94.1% 任务成功率；可靠的性质预测 | [卡片](../works/vaspbench.md) |
| AutoMat | 2026 | 在 HPC 上端到端复现计算材料学的结论 | 85 条由领域专家甄选的结论，三种复现类型 | 支持或推翻结论的证据；54.1% 成功率 | [卡片](../works/automat.md) |
| Automating Structural Reliability Analysis | 2026 | 生成并运行 FORM、蒙特卡罗与子集模拟求解器 | 20 道留出的可靠度题，配确定性的非 LLM 运行器 | 20 道题的可靠指标均与经验证求解器的参考值相差不超过 0.1 | [卡片](../works/automating-structural-reliability-analysis-with-a.md) |
| CeProBench | 2026 | 在 Aspen Plus 中实际执行的操作参数闭环调优 | 20 个高保真 Aspen Plus 文件，91 个可调参数，65 个目标 | 经 Aspen 验证的可行性；收率/纯度/成本与收敛迭代次数 | [卡片](../works/ceprobench.md) |
| Collider-Bench | 2026 | 通过公开模拟工具栈重现 LHC 上的 SUSY 搜寻 | 来自四项 CMS 搜寻的 10 个模拟任务 | 直方图与隐藏产额的吻合度；LLM 溯源评判 | [卡片](../works/collider-bench.md) |
| CRAFTS | 2026 | 从用户请求与 PFD 出发构建可执行的 IDAES/Pyomo 过程模拟模型 | OpenIDAES-450，82 个冻结的留出算例，确定性的 IDAES/Pyomo 晋级关卡 | Workflow Success 91.5%，外加单元/物流/连接的宏平均 F1 | [卡片](../works/crafts.md) |
| HydroAgent | 2026 | 率定运行中的 CREST 水文模型，重模拟循环 | 4 个留出的水文站（329-40,792 km2），从 20 轮中取最优 | 相对人类专家参考的 Nash-Sutcliffe 效率系数 | [卡片](../works/hydroagent.md) |
| LLM-Empowered Agent for Structural Analysis | 2026 | 生成并自动执行 OpenSeesPy 梁模型，配 OpsVis 绘图 | 8 道梁题外加 3 项扩展任务，每项运行 500 次 | 可靠性高于 0.990，鲁棒性高于 0.996 | [卡片](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| LQCDMaster | 2026 | 生成并运行 PyQUDA 格点 QCD 测量工作流 | 70 个任务：定域与非定域两点函数、介子与重子三点函数、Wilson 环 | 与专家参考实现在机器精度上一致（63/70 Matched） | [卡片](../works/lqcdmaster.md) |
| MDArena | 2026 | 真实的分子动力学研究工作流 | 50 个容器化任务，29 个系统，14 种协议 | 严格成功率外加过程级部分得分 | [卡片](../works/mdarena.md) |
| MolClaw / MolBench | 2026 | 跨 30 多个工具驱动对接、构象采样与分子性质计算 | 分三层；端到端挑战需 8 到 50 次以上的连续工具调用 | 各子任务的 Accuracy 与 Hits@3，外加加权的 E2E rubric（对接命中 0.80 对 0.56） | [卡片](../works/molclaw.md) |
| MooseBench | 2026 | 带 PDE 真值的 MOOSE 多物理场输入文件生成 | 220 个算例，每个都带有预期的 PDE 契约 | 通过确定性 PDE 重建得到的意图保真度分数 | [卡片](../works/moosebench.md) |
| PDEAgent-Bench | 2026 | 面向三个 FEM 库的 PDE 求解器代码生成 | 645 个实例，6 个类别，11 个族（DOLFINx/Firedrake/deal.II） | 分阶段的可执行性、准确性、效率检查 | [卡片](../works/pdeagent-bench.md) |
| Plausible but Wrong | 2026 | 配置并运行 CAMB Boltzmann 求解器计算 | 14 个按复杂度分层的 CAMB 任务；One-Shot 与 Deep Research 两种回路 | 参数准确度乘以数值准确度（带领域文档时为 0.85） | [卡片](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
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
- [Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [MASSE](../works/masse.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [AutoBM / BMEval](../works/autobm.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [SimAgents](../works/simagents.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [CASCADE](../works/cascade.md)
- [LQCDMaster](../works/lqcdmaster.md)
- [MolClaw](../works/molclaw.md)
