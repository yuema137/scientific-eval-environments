# 数据分析与统计推断

> [English](../../activities/data_analysis_statistical_inference.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 从数据中提炼科学结论的能力——预处理、探索性与统计分析、估计、假设检验、拟合、不确定性量化与结果解读。

## Scope

涵盖生物信息学与组学分析、对科学数据集的统计推断，以及以数据分析为核心科学活动的结构化分析流程。不因 benchmark 只是计算评测统计量而归入此类；与建模与预测相区分——后者的核心交付物是预测模型，而非从观测数据得出的结论。

## Task Patterns

有一大类任务聚焦于**单细胞与组学数据分析**。[BAISBench](../works/baisbench.md)、[scBench](../works/scbench.md)、[scBench-Long](../works/scbench-long.md) 和 [SpatialBench](../works/spatialbench.md) 考察 agent 从单细胞或空间转录组数据中还原生物学结论的能力，评分方式大多基于确定性的快照比对。[BixBench](../works/bixbench.md) 和 [HeurekaBench](../works/heurekabench.md) 把已发表的 notebook 分析改写成开放式的探索性任务；而 [GenoTEX](../works/genotex.md)、[BioAgent Bench](../works/bioagent-bench.md) 和 [GeneBench-Pro](../works/genebench-pro.md) 则覆盖了基因表达流程、RNA-seq/variant-calling 工作流，以及以仿真为基础的多阶段基因组统计。[MedAgentGym](../works/medagentgym.md) 和 [SciAgentArena](../works/sciagentarena.md) 进一步将其延伸到生物医学数据科学和跨尺度的生物医学研究。

第二类任务涵盖**通用数据科学以及文档密集型的分析**。[BLADE](../works/blade.md)、[DA-Code](../works/da-code.md)、[DSBench](../works/dsbench.md) 和 [ScienceAgentBench](../works/scienceagentbench.md) 以专家或源自论文的标准答案为基准，考察开放式的数据整理、分析和统计建模；[AstaBench](../works/astabench.md) 则把数据分析作为一个类别，纳入了更大的研究套件之中。[LongDA](../works/longda.md) 把在美国联邦调查数据的长文档中检索定位作为核心瓶颈，而 [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) 通过对生产环境 API 的结构化工具调用来测试环境地理空间分析。

第三类任务把分析刻画为**预算受限的测量与基于物理的拟合**：[Gravity-Bench-v1](../works/gravity-bench.md)、[MaD Physics](../works/mad-physics.md)、[SciGym](../works/scigym.md) 和 [Stargazer](../works/stargazer.md) 要求 agent 在成本预算约束下规划数据采集，并从采集或仿真得到的数据中推断规律、机制或轨道模型。[Model Discovery Agent](../works/model-discovery-agent.md) 把这层 inference machinery 明着拆出来：每来一个 designed experiment，就更新 model structure、parameter 和 latent dynamics 三层 Bayesian uncertainty。[EXP-Bench](../works/exp-bench.md) 则把这一思路扩展到端到端的 AI 研究实验。

天文学贡献了一类独特的任务：**面向观测档案与巡天数据流的分析**。其中一条脉络直接从人类审核者看到的仪器产物出发，去甄别或分类巡天探测：[AstroAlertBench](../works/astroalertbench.md) 把 ZTF 警报的 broker 元数据与 science/reference/difference 图像配在一起，[Spec-o3 / SpecVI-Bench](../works/spec-o3.md) 则要求 agent 在给出稀有天体判定之前，先把 LAMOST 光谱中选定的波段区间重新绘出来看。另一条脉络借助领域中成熟的分析代码，从档案星表反推物理量——[Mephisto](../works/mephisto.md) 为 256 个 COSMOS2020 星系搜索 CIGALE 光谱能量分布模型，并以穷举网格结果为参照；[gammapyGPT](../works/gammapygpt.md) 对 Gammapy 给出的流量与谱指数做数值校验；[Plausible but Wrong](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) 按参数还原程度为超新星、转动曲线、系外行星与引力透镜分析打分；[Einstein Telescope 的 agent 对比研究](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) 则在模拟探测器应变上跑完整的匹配滤波搜索。[AstroVisBench](../works/astrovisbench.md) 与 [Imaging-101](../works/imaging-101.md) 位于同一类中偏代码的一端，而 [VESTA / DAWN](../works/vesta-dawn.md) 把「作图—变换—重拟合」这一循环单独拎出来，放在天体物理的函数族上考察。

最后一类任务处理**神经科学与行为信号分析**：[BrainBench (EEG)](../works/brainbench-eeg.md) 评估以指令为条件的 EEG 分析与报告，[Rodent-Bench](../works/rodent-bench.md) 则测试对长时程啮齿动物行为视频的多模态标注。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| BLADE | 2024 | 依据分析决策评分的开放式数据驱动科学分析 | 12 个数据集，配有来自文献的研究问题 | 匹配专家数据科学家的标准答案分析 | [卡片](../works/blade.md) |
| DA-Code | 2024 | 智能体式的数据科学代码生成 | 在 Docker 沙箱中进行数据整理/分析任务 | 执行验证的准确率（最佳 LLM 30.5%） | [卡片](../works/da-code.md) |
| DSBench | 2024 | 在真实多模态任务上的数据分析与建模 | 540 个任务（466 个分析 + 74 个建模），多表 | 完成任务（最佳 agent 分析 34.12%） | [卡片](../works/dsbench.md) |
| GenoTEX | 2024 | 基因-性状关联的基因表达分析 | 覆盖 911 个数据集的 1,384 个问题，完整流程 | 匹配生物信息学家整理的参考代码/结果 | [卡片](../works/genotex.md) |
| ScienceAgentBench | 2024 | 单项数据驱动的科学工作流任务 | 来自 44 篇论文、四个学科的 102 个任务 | 自包含的 Python 程序，按执行评分 | [卡片](../works/scienceagentbench.md) |
| AstaBench | 2025 | 涵盖数据分析的整体性科学研究 | 横跨 11 个 benchmark 的 2,400+ 个问题 | 相对标准化基线的成本受控评分 | [卡片](../works/astabench.md) |
| AstroVisBench | 2025 | 源自 notebook 的天文专有数据处理工作流 | 来自 110 份 notebook 的 432 个处理 + 432 个可视化任务 | 变量召回分数，加上由 VLM 评判的图正确性（最佳 15.7% 无差错） | [卡片](../works/astrovisbench.md) |
| BAISBench | 2025 | 组学驱动的单细胞生物学发现 | 15 个数据集标注 + 193 道发现类 MCQ | 正确的细胞类型与研究结论，对比人类基线 | [卡片](../works/baisbench.md) |
| BixBench | 2025 | 探索性的计算生物学数据分析 | 50+ 个场景，约 300 个问题，Jupyter 容器 | 开放式答案/选择题的正确率（前沿约 17%） | [卡片](../works/bixbench.md) |
| CASCADE / SciSkillBench | 2025 | 材料科学与化学数据的检索、分析与处理 | 116 个任务中的 76 个数据类任务，两档说明详细程度，每种配置重复 3 次 | 在容差内自动比对标准答案（GPT-5 下 DeepSolver 总体 93.26%） | [卡片](../works/cascade.md) |
| EXP-Bench | 2025 | 端到端的 AI 研究实验 | 来自 51 篇论文的 461 个任务，12,737 个子任务 | 设计/实现/执行/分析（完整完成 0.5%） | [卡片](../works/exp-bench.md) |
| gammapyGPT | 2025 | 借 Gammapy 库做伽马射线观测分析 | 4 个基于真实观测数据的任务，精简过的执行环境 | 观测数量、流量与谱指数的精确匹配或容差匹配 | [卡片](../works/gammapygpt.md) |
| Gravity-Bench-v1 | 2025 | 预算受限的观测与引力物理推断 | 仿真的二体系统，含 OOD 变体 | 相对参考解刻画隐藏的物理规律 | [卡片](../works/gravity-bench.md) |
| HiSciBench | 2025 | 从给定数据集与研究问题出发的数据驱动发现 | L5.1：74 个实例，需自行编写并运行 Python 分析 | 对照逐任务判据的执行式成功率 | [卡片](../works/hiscibench.md) |
| LLM-IOAA | 2025 | 面向曲线图、光谱与巡天图像的奥赛数据分析 | 取自 2022–2025 年 IOAA 试卷的 8 道数据分析题 | 按官方评分标准分步给分（GPT-5 88.5%） | [卡片](../works/llm-ioaa.md) |
| MedAgentGym | 2025 | 以代码为核心的生物医学数据科学推理 | 72,413 个实例，129 个类别，沙箱化 | 可验证的标准答案通过；亦可用于 RL 训练 | [卡片](../works/medagentgym.md) |
| Mephisto | 2025 | 从多波段测光推断星系物理性质 | 256 个 COSMOS2020 星系外加 31 个 JWST 小红点；CIGALE 树搜索 | 拟合的卡方低于穷举网格基线的 1.2 倍 | [卡片](../works/mephisto.md) |
| SciGym | 2025 | 针对隐藏 SBML 系统的迭代式实验设计 | 评估 137 个小型系统，发布 350 个 | 提交假设的机制并对比真实系统 | [卡片](../works/scigym.md) |
| SpatialBench | 2025 | 基于数据快照的空间生物学分析 | 146 个问题，五种技术，七个类别 | 确定性地还原关键生物学结果 | [卡片](../works/spatialbench.md) |
| VLM-Verified Autonomous Discovery | 2025 | 还原给定数据集背后的底层模型 | 10 个任务：功率谱、谱线、振子、流行病学 | 判出正确模型的 pass@1（加入 VLM 反馈后为 0.7–0.8） | [卡片](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| AstroAlertBench | 2026 | 依据 broker 元数据与差异图像甄别巡天警报 | 1,500 条真实 ZTF 警报，每类 300 条，三个分别评分的阶段 | 端到端五分类准确率（最佳 60.60%），人类集成为 30.67% | [卡片](../works/astroalertbench.md) |
| BioAgent Bench | 2026 | 端到端的生物信息学流程执行 | RNA-seq/variant-calling/宏基因组学，扰动探针 | LLM 评分的输出产物与步骤推理 | [卡片](../works/bioagent-bench.md) |
| BrainBench | 2026 | 以指令为条件的 EEG 理解与分析 | 四个子集，17 个数据集，CodeAct/智能体式 | 在各输出维度上有科学依据的报告 | [卡片](../works/brainbench-eeg.md) |
| DSAgentBench | 2026 | 自动化完整的数据科学分析工作流 | 275 个任务，运行于真实计算机环境（notebook、终端、浏览器、数据库） | 对分析正确性的确定性检查（最佳 56.7%） | [卡片](../works/dsagentbench.md) |
| Einstein Telescope Agentic AI Comparison | 2026 | 端到端执行一次匹配滤波引力波搜索 | 一份七阶段规格说明，两个 agent，两轮运行，同一硬件 | 探测效率与恢复的 SNR，外加逐项计数的过程偏离 | [卡片](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| Fisher-R1 / P-Bench | 2026 | 选择检验、计算 p 值、得出有效推断 | 425 个假设检验任务；经济学、生物学、医学 | 拒绝/不拒绝匹配加 p 值接近度（Raw/Strict） | [卡片](../works/fisher-r1.md) |
| GeneBench-Pro | 2026 | 多阶段的统计基因组学分析 | 129 个基于仿真数据生成过程的问题 | 对决策相关数值的二元通过判定（最佳 28.7%） | [卡片](../works/genebench-pro.md) |
| GeoNatureAgent Benchmark | 2026 | 通过工具调用进行的环境地理空间分析 | 93 个任务，18 个类别，可自托管 API | 预期的工具调用与必含答案（最佳 60.8%） | [卡片](../works/geonatureagent-benchmark.md) |
| HeurekaBench | 2026 | 针对已发表研究的探索性端到端研究 | 来自 41 项洞见的 50 个开放题 + 50 道 MCQ，单细胞 | 数据驱动的答案，对比已报告的发现进行验证 | [卡片](../works/heurekabench.md) |
| Imaging-101 | 2026 | 借逆问题求解器从间接测量中恢复信号 | 57 个以论文为依据的任务，六个领域，四阶段的标准流水线 | 对照逐任务阈值的 NCC 与 NRMSE（端到端最佳 17/57） | [卡片](../works/imaging-101.md) |
| LongDA | 2026 | 文档密集型的调查数据分析 | 505 个查询，17 项美国调查，约 263k-token 文档 | 通过可执行代码给出数值/列表答案 | [卡片](../works/longda.md) |
| MaD Physics | 2026 | 预算受限的测量与物理定律推断 | 三个仿真环境，含改变物理规律的变体 | 推断规律以预测系统未来状态 | [卡片](../works/mad-physics.md) |
| Model Discovery Agent | 2026 | 对 mechanistic model 做 sequential Bayesian inference | 四组 discovery 任务上的 SMC³：结构、参数、latent state 三层 | 每次实验后的 held-out predictive loss 与 deterministic structural recovery | [卡片](../works/model-discovery-agent.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | 果蝇数据的行为分类与统计比较 | 9 任务的果蝇光遗传学流程；约 47 GB 数据 | 各阶段输出对照专家标注（如 Mann–Whitney U） | [卡片](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| Plausible but Wrong | 2026 | 对公开档案天文星表的分析 | 4 个研究任务：超新星、转动曲线、系外行星、引力透镜 | Parameter Recovery Score，外加物理合理性评级 | [卡片](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| Rodent-Bench | 2026 | 多模态的啮齿动物行为视频标注 | 长录像（10-35 分钟），多种范式 | 时间分割/分类（逐秒准确率、F1） | [卡片](../works/rodent-bench.md) |
| scBench | 2026 | 从快照出发的单步 scRNA-seq 分析 | 394 个问题，六个平台，七个类别 | 确定性地还原关键生物学结果（29-53%） | [卡片](../works/scbench.md) |
| scBench-Long | 2026 | 从接近原始数据出发的长时程单细胞发现 | 21 项评估，不规定方法 | 还原研究结论，确定性评分（25.4%） | [卡片](../works/scbench-long.md) |
| SciAgentArena | 2026 | 跨尺度的真实生物医学研究 | 约 200 个任务，五个领域，分步验证 | 分步验证的数据分析/发现/有效性 | [卡片](../works/sciagentarena.md) |
| SciVisAgentBench | 2026 | 面向洞见的科学数据分析与可视化 | 108 个专家案例，七个科学领域；多平台工具 | 以结果为中心的图像指标加确定性验证器 | [卡片](../works/scivisagentbench.md) |
| Spec-o3 / SpecVI-Bench | 2026 | 查看巡天光谱以甄别稀有天体候选体 | 5 个任务，LAMOST 测试光谱 1,122 条正样本 / 5,632 条负样本 | 宏平均准确率与正类 F1（Spec-o3-7B 88.7% / 76.5%） | [卡片](../works/spec-o3.md) |
| Stargazer | 2026 | 迭代式、基于物理的 RV 模型拟合 | 120 个任务（100 个合成 + 20 个真实档案） | 按标准逐项通过的 Keplerian 拟合（Easy 80%，真实 0%） | [卡片](../works/stargazer.md) |
| TS-Skill | 2026 | 信号层面的时间序列分析：尺度选择、定位、跨区间整合 | 覆盖七种 skill 组合的 3,000 道 QA；25 个按领域设定的合成类别 | 按单 skill 与按组合报告准确率（无工具时 SK3 不高于 0.259 的随机基线） | [卡片](../works/ts-skill.md) |
| VESTA / DAWN | 2026 | 带残差检视的迭代式分布与时间序列拟合 | 400 个实例，含恒星 IMF 与引力波啁啾切分 | 对照真值的 Jensen–Shannon 散度与 ELPD-LOO | [卡片](../works/vesta-dawn.md) |

## Related Works

- [DSAgentBench](../works/dsagentbench.md)
- [Model Discovery Agent](../works/model-discovery-agent.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [BrainBench](../works/brainbench-eeg.md)
- [Imaging-101](../works/imaging-101.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [scBench-Long](../works/scbench-long.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [SciAgentArena](../works/sciagentarena.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [TS-Skill](../works/ts-skill.md)
- [MaD Physics](../works/mad-physics.md)
- [AstroAlertBench](../works/astroalertbench.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [Stargazer](../works/stargazer.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [scBench](../works/scbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [Spec-o3](../works/spec-o3.md)
- [LongDA](../works/longda.md)
- [HeurekaBench](../works/heurekabench.md)
- [CASCADE](../works/cascade.md)
- [HiSciBench](../works/hiscibench.md)
- [SpatialBench](../works/spatialbench.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [AstaBench](../works/astabench.md)
- [Mephisto](../works/mephisto.md)
- [LLM-IOAA](../works/llm-ioaa.md)
- [gammapyGPT](../works/gammapygpt.md)
- [SciGym](../works/scigym.md)
- [MedAgentGym](../works/medagentgym.md)
- [EXP-Bench](../works/exp-bench.md)
- [AstroVisBench](../works/astrovisbench.md)
- [BAISBench](../works/baisbench.md)
- [BixBench](../works/bixbench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [DA-Code](../works/da-code.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [DSBench](../works/dsbench.md)
- [BLADE](../works/blade.md)
- [GenoTEX](../works/genotex.md)
