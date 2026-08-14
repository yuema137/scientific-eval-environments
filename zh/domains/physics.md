# Physics

> [English](../../domains/physics.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

以物理定律、物理仿真或实验物理为基础的评估环境。粒子物理、核物理、量子物理与流体物理折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| MaD Physics | 2026 | 推断支配模拟系统的未知——有时被刻意改变的——物理定律，覆盖经典力学（D 维中的 N 粒子）、2D 不可压缩粘性流体与 2D 势箱中的两个量子粒子。 | 在三个模拟环境中交互实验；每次观测按保真度级别花费 2 / 5 / 10，受固定的单 trial 预算约束。 | 相对真实未来状态的预测误差：经典力学用归一化 RMSE，流体/量子用涡量/概率密度上的 L2 误差，在 33 个随机初始化上取平均。 | [→](../works/mad-physics.md) |
| NewtonBench | 2025 | 重新发现一条隐藏物理定律：对 12 条经典定律（万有引力、库仑、傅里叶、Snell 等）的表达式树做反事实变异得到。 | 324 个交互任务（108 条变异定律 × 3 个模型系统）；agent 通过 `run_experiment` 工具设计实验，以符号表达式提交定律。 | 与真值定律的二元符号等价（LLM judge；与人类专家一致率 98.3%），辅以所发现方程预测的 RMSLE。 | [→](../works/newtonbench.md) |
| PRBench | 2026 | 端到端复现已发表的物理研究——理解论文方法、从零实现算法、复现其定量结果——覆盖从 QCD 到凝聚态的 11 个子领域。 | 30 个专家整理的论文复现任务，来自 20 余个课题组，在沙箱执行环境中运行，输出标准化 CSV。 | 每任务由专家撰写的加权 rubric 评分（数据复现准确性权重 0.60）；端到端成功要求每个维度 >0.9——目前所有 agent 均为零。 | [→](../works/prbench.md) |
| Collider-Bench | 2026 | 复现 LHC 实验分析：通过公开仿真栈（MadGraph5、Pythia、Delphes）为 CMS 超对称搜索生成信号事例，并实现论文发表的事例筛选。 | 10 个 Simulation 任务，取自 13 TeV 下四项 CMS SUSY 搜索；agent 提交预测信号产额的分 bin 直方图、分析代码与方法报告。 | 与隐藏参考直方图的相对 L² 距离，通过阈值由 physicist-in-the-loop 基线设定；另有 LLM 溯源评判标记造假工作流。 | [→](../works/collider-bench.md) |
| SimulCost | 2026 | 在 13 个物理仿真器上调节仿真参数以达到目标物理结果，并计入仿真时间与实验资源成本。 | 2,947 个单轮与 1,931 个多轮参数调优任务。 | 预算约束下的成功率，并分层报告更严格的精度要求。 | [→](../works/simulcost.md) |
| NatureBench | 2026 | 达到 Nature 系列 Physical Modeling 研究的已发表 SOTA——其 90 个任务中的 13 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的物理任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Physics 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| CMT-Benchmark | 2025 | 求解专家研究者水平的凝聚态理论问题——量子多体系统与经典统计力学——横跨 Hartree-Fock、精确对角化、量子/变分蒙特卡洛、DMRG 与统计力学。 | 50 道由专家研究者按其自身工作水平编写的单题理论与计算推导；非交互式 agent 设定。 | 对照专家提供的真值做程序化检验，机器判分包括对非对易算符做正规排序后的符号处理。 | [→](../works/cmt-benchmark.md) |
| CMPhysBench | 2025 | 完成研究生水平的凝聚态物理计算，覆盖磁学、超导、强关联体系与基础理论框架。 | 520 余道精心整理的计算题，每题要求独立生成完整解答；单题推导，非交互式 agent 设定。 | 对解答表达式的 SEED（Scalable Expression Edit Distance）部分得分，加上以正确解答百分比计的准确率。 | [→](../works/cmphysbench.md) |
| PhySciBench | 2026 | 在物理与化学各半的题集中回答物理侧的专家 deep-research 问题，针对推理链脆弱、跨步骤知识迁移有限与缺少基于物理的自我验证。 | 200 道专家整理的问题，物理与化学各半，组织为呼应真实科研工作流的六类任务。 | 基于准确率比较最先进模型与 agent 系统，并在准确率之外报告成本。 | [→](../works/physcibench.md) |
| MetaSyn | 2026 | 进行忠实于协议的系统综述与 meta 分析；物理学是其 422 个专家整理 meta 分析所覆盖的主题之一。 | 多阶段系统综述工作流：在掺入不合格干扰文献的共享 PubMed 文献库中，依据带结构化 PI/ECO 标准的研究问题找出应纳入的研究。 | 对照原综述作者实际纳入的研究集做识别评估，并以分阶段评估定位 meta 分析流程中的失败环节。 | [→](../works/metasyn.md) |
| RealPDEBench | 2026 | 基于与数值模拟配对的真实测量数据，预测复杂物理系统——流固耦合、圆柱与翼型绕流、燃烧——的演化。 | 五个真实测量数据集配成对模拟数据集，三类真实-模拟对比任务；评估科学 ML 代理模型而非 LLM agent。 | 横跨数据导向与物理导向的八项指标，覆盖十个基线（含预训练 PDE 基础模型与一种传统方法）。 | [→](../works/realpdebench.md) |
| Gravity-Bench-v1 | 2025 | 通过有计划的观测，发现模拟二体引力系统中被隐藏的——有时是分布外的——物理。 | 实验预算下的交互式「观测规划 + 数据分析」回合（据官方项目页每次运行至多 100 次观测）。 | 对照严格引力动力学模拟导出的参考解检验答案，并与人类专家水平对标。 | [→](../works/gravity-bench.md) |
| PhysGym | 2025 | 通过探查交互式模拟发现底层物理定律，先验知识分四个受控层级提供。 | 97 个精选问题（取自 PHYBench），以有限实验预算下的逐步交互回合运行。 | 假设准确性与模型保真度的标准化协议与指标。 | [→](../works/physgym.md) |
| DiscoverPhysics | 2026 | 揭示物理刻意偏离现实的 N 体世界——修改引力、隐藏粒子种类——的运动定律。 | 按需生成的 22 个反事实世界；迭代提出实验，最终提交自然语言解释与定律的 Python 实现。 | 留出粒子上的轨迹 MSE，加按评分标准的 LLM 解释分。 | [→](../works/discoverphysics.md) |
| FEABench | 2025 | 通过 API 操作 COMSOL Multiphysics，用有限元分析端到端求解多物理场问题。 | 以自然语言给出问题描述；agentic 设定下对照软件反馈迭代 API 调用。 | 对生成 API 调用与计算答案的评估，API 调用可执行率为主要指标。 | [→](../works/feabench.md) |
| QMP-Bench | 2026 | 端到端复现已发表的量子多体模拟结果。 | 100 个研究级任务，提取自 21 种高影响力期刊。 | 编程验证器检验代码正确性，科学验证器检验基于物理原理的有效性。 | [→](../works/qmp-bench.md) |
| gwBenchmarks | 2026 | 完成高精度引力波科学：数值相对论波形代理模型、黑洞轨道动力学、并合遗迹拟合、模板库。 | 8 个任务，底层数据代表 10⁸ 核时以上的计算；12 个 coding agent 受评。 | 外部预定义评估框架配单任务物理指标（频域失配、相对误差），对照 ≲10⁻⁴ 的领域要求。 | [→](../works/gwbenchmarks.md) |
| PRL-Bench | 2026 | 完成从 2025 年 8 月后的 Physical Review Letters 论文派生的前沿物理研究任务，覆盖五个子领域。 | 100 个经专家验证、面向探索构造的长 horizon 研究任务。 | 客观可验证的结果，以 0–100 制评分。 | [→](../works/prl-bench.md) |
| EnvTrace | 2025 | 为同步辐射光束线生成控制代码——其正确性即随时间的物理行为。 | 在光束线控制逻辑数字孪生上评估代码生成；30 余个 LLM 受评。 | 执行轨迹对齐，产出多维度功能正确性分。 | [→](../works/envtrace.md) |
| CritPt | 2025 | 求解未发表的研究入门级物理挑战，覆盖从凝聚态到生物物理的 11 个以上子领域。 | 71 个复合挑战加 190 个检查点任务，由 50 余位活跃研究者创作，可选配编码工具。 | 防猜测、可机器验证的答案，由针对物理定制的自动判分流水线打分。 | [→](../works/critpt.md) |
| TPBench | 2025 | 求解高能理论与宇宙学中的全新理论物理问题，难度直至研究级。 | 57 道全新问题，从本科到研究级；单题推导。 | 可自动验证的答案，判分为理论推导定制。 | [→](../works/tpbench.md) |
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，物理是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的参考解与测试用例执行。 | [→](../works/scicode.md) |
| Lean4Physics | 2025 | 在 Lean4 中形式化证明大学物理命题。 | 200 条手工编写、经同行评审的命题，取材于大学教材与竞赛题，配 PhysLib 基础库。 | Lean4 内核证明检查——全程无 judge 介入。 | [→](../works/lean4physics.md) |
| UGPhysics | 2025 | 求解横跨 13 个科目、四种物理推理技能的本科物理问题。 | 5,520 道中英双语问题，七种答案类型，经严格泄漏筛查。 | 为物理答案正确性定制的 MARJ（模型辅助规则判分）流水线。 | [→](../works/ugphysics.md) |
| PHYBench | 2025 | 求解需要物理感知与多步骤、多条件推理的原创物理问题，难度直至奥赛。 | 500 道以符号表达式作答的原创问题；附实测人类专家基线。 | 作用于数学表达式的表达式编辑距离（EED）分数，加准确率。 | [→](../works/phybench.md) |
| SeePhys | 2025 | 求解图示不可或缺的物理问题——电路图、Feynman 图及其余 19 类图示。 | 2,000 道经校验的多模态问题（官方页），从初中到博士资格考试水平；75% 视觉不可或缺。 | 多模态解题准确率，以人类专家为锚点。 | [→](../works/seephys.md) |
| HiPhO | 2025 | 在竞赛级判分下作答最新的高中物理奥赛真题。 | 2024–2025 年的 13 套国际与地区真题，混合纯文本与图示题。 | 官方评分方案的答案级与步骤级判分；按官方阈值授牌。 | [→](../works/hipho.md) |
| PHYSICS | 2025 | 求解覆盖六大核心领域的大学水平物理问题：经典力学、量子力学、热力学与统计力学、电磁学、原子物理与光学。 | 1,297 道专家标注的问题；静态单题解题。 | 稳健的自动评估系统，提供精确可靠的答案校验。 | [→](../works/physics-benchmark.md) |
| CodePDE | 2025 | 为支配物理系统的代表性 PDE 问题生成数值求解器。 | 带迭代改进的求解器代码生成；评估推理、调试、自我改进与测试时扩展。 | 生成求解器对照参考解的精度。 | [→](../works/codepde.md) |
| PDEAgent-Bench | 2026 | 为横跨 6 个数学类别、11 个族的 PDE 生成有限元求解器。 | 645 个「规格到代码」实例，面向 DOLFINx、Firedrake 或 deal.II。 | 分级检查：可执行性、数值精度（规定网格上的参考解）与效率。 | [→](../works/pdeagent-bench.md) |
| MooseBench | 2026 | 生成求解预期 PDE 的多物理场模拟代码，而不只是能跑的代码。 | 220 个带 PDE 级数学真值的 MOOSE 算例。 | 经确定性重构（控制项、边界条件、初始条件、系数、时间格式）计算的 Intent Fidelity Score。 | [→](../works/moosebench.md) |
| SciConvBench | 2026 | 通过对话把不适定的计算科学请求——流体力学、固体力学、材料、PDE——变成适定规格。 | 多轮消歧与矛盾消解对话。 | 按评分标准为澄清行为、对话共识建立与最终规格保真度打分。 | [→](../works/sciconvbench.md) |
| AInsteinBench | 2025 | 解决生产级科学代码库（含数值相对论与流体力学）中的维护者 PR 任务。 | 六个科学仓库上的仓库级 coding agent 任务。 | 可执行环境中的测试驱动验证。 | [→](../works/ainsteinbench.md) |
| SciVisAgentBench | 2026 | 对物理数据做科学可视化与数据分析——其七个应用领域之一——把自然语言意图转成可执行的可视化操作（体渲染、场计算、洞见提炼）。 | 108 个专家精心制作的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，在 ParaView、napari 等平台上经 CLI、MCP 服务器与 Python API 运行。 | 多模态、以结果为中心的流水线，结合 MLLM 评判（报告为 Claude-Opus-4.6；与人类评分 Pearson 0.808）与确定性验证器——图像指标（PSNR、SSIM、LPIPS）、代码检查器与基于规则/case 专属的验证器。 | [→](../works/scivisagentbench.md) |
| An LLM-driven framework for cosmological model-building and exploration | 2025 | 在 CLASS Boltzmann 求解器内部实现暗能量场论——Thawing Quintessence 与 Early Dark Energy——再对照观测探索它们的参数空间。 | 在容器化的 CLASS 3.3.0 环境中，每个模型实例走三个顺序阶段（模型实现、计算可观测量、参数探索）；两个标准答案模型外加两次假设生成运行，只评测一种 agent 配置。 | 二元的执行里程碑；Ω_X 与物质功率谱相对标准参考实现的最大相对偏差；以及由 DESI、Planck、Pantheon+ 与 SH0ES 数据算出的似然/BIC、Hubble/M_B 张力与 CMB C_ℓ 自洽性奖励。 | [→](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope | 2026 | 搭建并运行一条匹配滤波引力波搜索流程：由原始应变做 Welch PSD 估计，用 IMRPhenomD 近似波形按 0.97 最小匹配度生成几何模板库，并恢复注入的双黑洞波形。 | 一份书面规格说明被自主执行四次——两个 agent（Claude Code、Codex）× 两档注入强度——在同一硬件上对模拟 Einstein Telescope E1 噪声中的 100 次 BBH 注入运行。 | 实测的流程输出——模板库规模、ρ = 8 以上的探测效率、恢复 SNR 的统计量、墙钟运行时间与峰值内存——与逐项计数的过程行为（重启、静默偏离、未经要求的优化）并列报告。 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SimAgents | 2025 | 从论文正文中还原一项已发表模拟所假定的宇宙学模型——物质、重子与暗能量密度、哈勃参数、σ8 与谱指数——并写成 MP-Gadget 能接受的形式。 | 来自 arXiv、ApJ 与 MNRAS 的 40 余项已发表模拟，逐项人工标注全部相关的参数/取值对；与 chain-of-thought 及 exchange-of-thought 基线对比。 | 对照人工标注计算参数级的精确率、召回率与 micro-F1；另按 Value / Type / Hallucination 的错误分类逐个模拟计数，人工评分与自动评分两种口径都有报告。 | [→](../works/simagents.md) |
| Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities | 2025 | 在生成的时间序列数据中区分阻尼型与啁啾型谐振子动力学。 | benchmark 的十项任务中有两项是振子动力学问题，每项都把作者生成的数据集与一段自然语言提示配对；对比三个 coding agent 与两个 judge 模型。 | 以系统能否判出正确底层模型的 pass@1 计分；视觉语言绘图 judge 只看产出的图（不给代码），依照由任务提示逐任务生成的 rubric 评分。 | [→](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| AI's Capability in Assisting Scientific Research I: Literature Review | 2026 | 为八个课题中属物理的那几个整理文献：脉冲星计时阵对广义相对论偏离的灵敏度、有质量 Yang–Mills 理论，以及激光烧蚀亚波长结构上的碎屑生成。 | 每个课题、每个系统各做一轮文献检索，至多 50 篇论文并归入四个类别；三个 AI 系统对每个课题各一位人类专家，共产出 701 条 AI 参考文献与 194 条人类参考文献。 | 与专家列表的重合只在标题与所归类别都吻合时才计入，相关性由该课题的领域专家判定；每条 AI 参考文献另经 DOI → 链接 → 标题检索的级联核验，判为完全正确 / 元数据不符 / 凭空编造。 | [→](../works/ai-assisting-research-i-literature-review.md) |
| AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation | 2026 | 为八个课题中属物理的两个——有质量 Yang–Mills 理论与激光烧蚀碎屑预测——撰写一页纸研究计划，写明方法、数据集、工具、时间安排与风险。 | 32 份一页纸计划书（8 份人类撰写，24 份来自三个 LLM），都依据同一份专家提供的任务说明与模板写成；六位评审每人都评了全部 32 份。 | 由四位教师或资深博后评审与两位前沿 LLM 评审做盲评，按 1–5 分 rubric 打分，涵盖表述与结构的清晰度、方法的适切性、资源与工具规划，以及可行性/时间安排/风险意识；每份计划书另做一次「人类还是 AI 撰写」的二元判断。 | [→](../works/ai-assisting-research-ii-project-planning.md) |
| Imaging-101 | 2026 | 物理计算成像——它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| SciVQR | 2026 | 物理中的多模态科学推理，六个顶层计分学科之一，也与数学并列为最难的两个。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 按学科报告零样本准确率，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 面向文献的物理工作：对来自 arXiv 的物理论文做解析、翻译、问答与综述生成。 | 8,735 个实例中物理占 2,306 个——200 个通用科学问答、357 个文献 OCR、357 个翻译、1,025 个单语文献问答、357 个跨语文献问答与 10 个综述选题；物理不贡献数据驱动发现类实例。18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性。 | [→](../works/hiscibench.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [MaD Physics](../works/mad-physics.md)
- [NewtonBench](../works/newtonbench.md)
- [PRBench](../works/prbench.md)
- [Collider-Bench](../works/collider-bench.md)
- [SimulCost](../works/simulcost.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CMPhysBench](../works/cmphysbench.md)
- [PhySciBench](../works/physcibench.md)
- [MetaSyn](../works/metasyn.md)
- [RealPDEBench](../works/realpdebench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [PhysGym](../works/physgym.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FEABench](../works/feabench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [PRL-Bench](../works/prl-bench.md)
- [EnvTrace](../works/envtrace.md)
- [CritPt](../works/critpt.md)
- [TPBench](../works/tpbench.md)
- [SciCode](../works/scicode.md)
- [Lean4Physics](../works/lean4physics.md)
- [UGPhysics](../works/ugphysics.md)
- [PHYBench](../works/phybench.md)
- [SeePhys](../works/seephys.md)
- [HiPhO](../works/hipho.md)
- [PHYSICS](../works/physics-benchmark.md)
- [CodePDE](../works/codepde.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [MooseBench](../works/moosebench.md)
- [SciConvBench](../works/sciconvbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [SimAgents](../works/simagents.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [AI's Capability in Assisting Scientific Research I: Literature Review](../works/ai-assisting-research-i-literature-review.md)
- [AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation](../works/ai-assisting-research-ii-project-planning.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
