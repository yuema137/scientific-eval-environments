# 数据分析与统计推断

> [English](../../activities/data_analysis_statistical_inference.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 从数据中提炼科学结论的能力——预处理、探索性与统计分析、估计、假设检验、拟合、不确定性量化与结果解读。

## Scope

涵盖生物信息学与组学分析、对科学数据集的统计推断，以及以数据分析为核心科学活动的结构化分析流程。不因 benchmark 只是计算评测统计量而归入此类；与建模与预测相区分——后者的核心交付物是预测模型，而非从观测数据得出的结论。

## Task Patterns

有一大类任务聚焦于**单细胞与组学数据分析**。[BAISBench](../works/baisbench.md)、[scBench](../works/scbench.md)、[scBench-Long](../works/scbench-long.md) 和 [SpatialBench](../works/spatialbench.md) 考察 agent 从单细胞或空间转录组数据中还原生物学结论的能力，评分方式大多基于确定性的快照比对。[BixBench](../works/bixbench.md) 和 [HeurekaBench](../works/heurekabench.md) 把已发表的 notebook 分析改写成开放式的探索性任务；而 [GenoTEX](../works/genotex.md)、[BioAgent Bench](../works/bioagent-bench.md) 和 [GeneBench-Pro](../works/genebench-pro.md) 则覆盖了基因表达流程、RNA-seq/variant-calling 工作流，以及以仿真为基础的多阶段基因组统计。[MedAgentGym](../works/medagentgym.md) 和 [SciAgentArena](../works/sciagentarena.md) 进一步将其延伸到生物医学数据科学和跨尺度的生物医学研究。

第二类任务涵盖**通用数据科学以及文档密集型的分析**。[BLADE](../works/blade.md)、[DA-Code](../works/da-code.md)、[DSBench](../works/dsbench.md) 和 [ScienceAgentBench](../works/scienceagentbench.md) 以专家或源自论文的标准答案为基准，考察开放式的数据整理、分析和统计建模；[AstaBench](../works/astabench.md) 则把数据分析作为一个类别，纳入了更大的研究套件之中。[LongDA](../works/longda.md) 把在美国联邦调查数据的长文档中检索定位作为核心瓶颈，而 [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) 通过对生产环境 API 的结构化工具调用来测试环境地理空间分析。

第三类任务把分析刻画为**预算受限的测量与基于物理的拟合**：[Gravity-Bench-v1](../works/gravity-bench.md)、[MaD Physics](../works/mad-physics.md)、[SciGym](../works/scigym.md) 和 [Stargazer](../works/stargazer.md) 要求 agent 在成本预算约束下规划数据采集，并从采集或仿真得到的数据中推断规律、机制或轨道模型。[EXP-Bench](../works/exp-bench.md) 则把这一思路扩展到端到端的 AI 研究实验。

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
| BAISBench | 2025 | 组学驱动的单细胞生物学发现 | 15 个数据集标注 + 193 道发现类 MCQ | 正确的细胞类型与研究结论，对比人类基线 | [卡片](../works/baisbench.md) |
| BixBench | 2025 | 探索性的计算生物学数据分析 | 50+ 个场景，约 300 个问题，Jupyter 容器 | 开放式答案/选择题的正确率（前沿约 17%） | [卡片](../works/bixbench.md) |
| EXP-Bench | 2025 | 端到端的 AI 研究实验 | 来自 51 篇论文的 461 个任务，12,737 个子任务 | 设计/实现/执行/分析（完整完成 0.5%） | [卡片](../works/exp-bench.md) |
| Gravity-Bench-v1 | 2025 | 预算受限的观测与引力物理推断 | 仿真的二体系统，含 OOD 变体 | 相对参考解刻画隐藏的物理规律 | [卡片](../works/gravity-bench.md) |
| MedAgentGym | 2025 | 以代码为核心的生物医学数据科学推理 | 72,413 个实例，129 个类别，沙箱化 | 可验证的标准答案通过；亦可用于 RL 训练 | [卡片](../works/medagentgym.md) |
| SciGym | 2025 | 针对隐藏 SBML 系统的迭代式实验设计 | 评估 137 个小型系统，发布 350 个 | 提交假设的机制并对比真实系统 | [卡片](../works/scigym.md) |
| SpatialBench | 2025 | 基于数据快照的空间生物学分析 | 146 个问题，五种技术，七个类别 | 确定性地还原关键生物学结果 | [卡片](../works/spatialbench.md) |
| BioAgent Bench | 2026 | 端到端的生物信息学流程执行 | RNA-seq/variant-calling/宏基因组学，扰动探针 | LLM 评分的输出产物与步骤推理 | [卡片](../works/bioagent-bench.md) |
| BrainBench | 2026 | 以指令为条件的 EEG 理解与分析 | 四个子集，17 个数据集，CodeAct/智能体式 | 在各输出维度上有科学依据的报告 | [卡片](../works/brainbench-eeg.md) |
| GeneBench-Pro | 2026 | 多阶段的统计基因组学分析 | 129 个基于仿真数据生成过程的问题 | 对决策相关数值的二元通过判定（最佳 28.7%） | [卡片](../works/genebench-pro.md) |
| GeoNatureAgent Benchmark | 2026 | 通过工具调用进行的环境地理空间分析 | 93 个任务，18 个类别，可自托管 API | 预期的工具调用与必含答案（最佳 60.8%） | [卡片](../works/geonatureagent-benchmark.md) |
| HeurekaBench | 2026 | 针对已发表研究的探索性端到端研究 | 来自 41 项洞见的 50 个开放题 + 50 道 MCQ，单细胞 | 数据驱动的答案，对比已报告的发现进行验证 | [卡片](../works/heurekabench.md) |
| LongDA | 2026 | 文档密集型的调查数据分析 | 505 个查询，17 项美国调查，约 263k-token 文档 | 通过可执行代码给出数值/列表答案 | [卡片](../works/longda.md) |
| MaD Physics | 2026 | 预算受限的测量与物理定律推断 | 三个仿真环境，含改变物理规律的变体 | 推断规律以预测系统未来状态 | [卡片](../works/mad-physics.md) |
| Rodent-Bench | 2026 | 多模态的啮齿动物行为视频标注 | 长录像（10-35 分钟），多种范式 | 时间分割/分类（逐秒准确率、F1） | [卡片](../works/rodent-bench.md) |
| scBench | 2026 | 从快照出发的单步 scRNA-seq 分析 | 394 个问题，六个平台，七个类别 | 确定性地还原关键生物学结果（29-53%） | [卡片](../works/scbench.md) |
| scBench-Long | 2026 | 从接近原始数据出发的长时程单细胞发现 | 21 项评估，不规定方法 | 还原研究结论，确定性评分（25.4%） | [卡片](../works/scbench-long.md) |
| SciAgentArena | 2026 | 跨尺度的真实生物医学研究 | 约 200 个任务，五个领域，分步验证 | 分步验证的数据分析/发现/有效性 | [卡片](../works/sciagentarena.md) |
| Stargazer | 2026 | 迭代式、基于物理的 RV 模型拟合 | 120 个任务（100 个合成 + 20 个真实档案） | 按标准逐项通过的 Keplerian 拟合（Easy 80%，真实 0%） | [卡片](../works/stargazer.md) |

## Related Works

- [BLADE](../works/blade.md)
- [DA-Code](../works/da-code.md)
- [DSBench](../works/dsbench.md)
- [GenoTEX](../works/genotex.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [AstaBench](../works/astabench.md)
- [BAISBench](../works/baisbench.md)
- [BixBench](../works/bixbench.md)
- [EXP-Bench](../works/exp-bench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [SciGym](../works/scigym.md)
- [SpatialBench](../works/spatialbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [BrainBench](../works/brainbench-eeg.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [HeurekaBench](../works/heurekabench.md)
- [LongDA](../works/longda.md)
- [MaD Physics](../works/mad-physics.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SciAgentArena](../works/sciagentarena.md)
- [Stargazer](../works/stargazer.md)
