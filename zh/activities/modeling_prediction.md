# 建模与预测

> [English](../../activities/modeling_prediction.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 构建或运用科学模型以预测量或行为的能力——预测与代理建模、预报、性质预测，以及以模型本身为核心产物的模型拟合。

## Scope

涵盖科学机器学习、性质回归与分类，以及学习用于预测的函数关系。与数据分析相区分（后者从观测数据得出结论）；二者仅在都被真正评估时才共现。仅在 ML 训练循环内部发生的优化不计入。

## Task Patterns

一类任务聚焦于**科学性质预测**——将分子或材料的结构映射到其性质。[LLM4Mat-Bench](../works/llm4mat-bench.md) 和 [MatText](../works/mattext.md) 都考察 LLM 能否从文本编码中预测晶体性质，二者得出了一致的结论：具备几何感知能力的专用模型依然占据主导地位。[FGBench](../works/fgbench.md) 将分子性质预测细化到官能团层面的推理，而 [AlchemyBench](../works/alchemybench.md) 和 [onePot-Bench](../works/onepot-bench.md) 则把预测范围扩展到合成配方以及反应/催化剂的结果，并以私有实验室数据作为评判依据。

第二类任务是**以优化模型指标为目标的 ML 工程**，要求 agent 迭代式地构建并训练模型。[MLAgentBench](../works/mlagentbench.md)、[MLE-bench](../works/mle-bench.md) 和 [MLE-Dojo](../works/mle-dojo.md) 把 ML 研究/工程构建成在 Kaggle 风格任务上不断改进指标的交互式循环；[DSBench](../works/dsbench.md) 在分析任务之外还加入了数据建模任务；[BioXArena](../works/bioxarena.md) 则在固定算力预算下，把完整的训练与提交流程应用于生物医学 ML。

第三类任务是**以物理为基础的预测与模型拟合**，其中拟合出的模型本身就是核心产物。[gwBenchmarks](../works/gwbenchmarks.md) 要求给出高精度的波形代理模型和残余体拟合，[RealPDEBench](../works/realpdebench.md) 衡量科学 ML 在物理系统上的仿真到现实差距，[Stargazer](../works/stargazer.md) 为径向速度序列拟合 Keplerian 轨道模型，而 [DiscoverPhysics](../works/discoverphysics.md) 则要求推断并实现反事实模拟世界的物理定律。[Model Discovery Agent](../works/model-discovery-agent.md) 在这条线上再加 Bayesian model averaging 和 M-open hypothesis expansion，最后专门拿 agent 从没做过的 intervention 检验 world model。天文则把这一点收紧为在几乎简并的候选之间做模型*选择*：[VESTA / DAWN](../works/vesta-dawn.md) 在只有到 log-log 空间才分得开的恒星初始质量函数族上、以及在引力波啁啾上，为「作图—变换—重拟合」这一循环评分；[Mephisto](../works/mephisto.md) 搜索的是候选的 CIGALE 光谱能量分布模型，而不是一张固定的参数网格；[VLM 验证的发现研究](../works/enhancing-agentic-autonomous-scientific-discovery.md) 则把还原出正确的生成模型作为通过判据，同时由一个视觉 judge 去查看拟合出的曲线。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| MLAgentBench | 2023 | 迭代式改进某个 ML 模型的目标指标 | 13 个 ML 实验任务，可读写并执行代码，agentic | 超越起始代码基线；最佳 agent 平均 37.5% | [卡片](../works/mlagentbench.md) |
| DSBench | 2024 | 从数据文件出发的端到端预测性数据建模 | 540 个任务（74 个建模 + 466 个分析），多模态多表格 | 完成任务；最佳成绩解出 34.12% 的分析题 | [卡片](../works/dsbench.md) |
| LLM4Mat-Bench | 2024 | 从文本编码的晶体预测材料性质 | 静态回归/分类 | 1.9M 个结构、45 种性质、3 种模态 | [卡片](../works/llm4mat-bench.md) |
| MatText | 2024 | 从文本表示预测晶体性质 | 静态回归，9 种表示，参数量最高达 70B，2M 个结构 | 达到几何 GNN 基线水平；揭示几何盲区 | [卡片](../works/mattext.md) |
| MLE-bench | 2024 | 端到端 ML 工程以训练有竞争力的模型 | 75 个精选 Kaggle 竞赛，agentic，长时程 | Kaggle 奖牌门槛；o1-preview 在 16.9% 上获铜牌 | [卡片](../works/mle-bench.md) |
| AlchemyBench | 2025 | 预测完整的材料合成配方及结果 | 对 17,000 个专家验证配方的静态预测 | LLM-as-a-Judge 与专家评估的一致性 | [卡片](../works/alchemybench.md) |
| ChemEBench | 2025 | 预测分子性质与反应结果 | L2 层级：SMILES 转 IUPAC、分子命名、性质预测与反应预测 | 客观题准确率；14 个模型的排行榜 | [卡片](../works/chemebench.md) |
| FGBench | 2025 | 在官能团层面推理分子性质 | 625K 个问题（245 个官能团）；7K 精选 LLM 子集，静态 QA | 回归/分类准确率；LLM 表现吃力 | [卡片](../works/fgbench.md) |
| Mephisto | 2025 | 搜索物理 SED 模型以拟合星系测光 | 256 个星系；五个 agent 角色驱动 CIGALE，每个星系约 36 个状态 | 模型的卡方落在穷举网格的 1.2 倍以内；恒星质量精确到约 0.3 dex | [卡片](../works/mephisto.md) |
| MLE-Dojo | 2025 | 借助反馈迭代式构建并优化 ML 模型 | 200+ 个 Kaggle 挑战，Gym 风格交互，可用于 SFT/RL 训练 | 8 个 LLM 上的迭代改进与解答质量 | [卡片](../works/mle-dojo.md) |
| VLM-Verified Autonomous Discovery | 2025 | 判定生成某个数据集的函数模型 | 10 个任务；纯代码、文本反馈与视觉反馈三种回路对比 | 还原出正确底层模型的 pass@1（最佳 0.8） | [卡片](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| BioXArena | 2026 | 构建并训练生物医学预测模型 | 76 个端到端任务，9 个领域，2 小时单 GPU 预算 | 隐藏标签 0-1 评分；最佳 MLEvolve 0.666 | [卡片](../works/bioxarena.md) |
| Cognitive Agents for Bridge Inspection Prioritization | 2026 | 依据清册记录预测未来劣化，据此为桥梁排序 | 康涅狄格州 3,365 座桥梁，六个年度 NBI 数据版本，四种方法同台比较 | 以截至 2025 年观测到的持续劣化为准，计算 AUC 与平均精度 | [卡片](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) |
| DiscoverPhysics | 2026 | 推断并实现反事实世界的物理定律 | 22 个模拟 N-body 世界，迭代式实验提案 | 轨迹 MSE 加上按 rubric 评判的解释；最佳约 50% | [卡片](../works/discoverphysics.md) |
| Model Discovery Agent | 2026 | 发现并平均 mechanistic world model | 四组 interactive benchmark；LLM 提结构，Bayesian machinery 做 inference | Held-out interventional prediction 与 structural recovery 随实验预算的变化 | [卡片](../works/model-discovery-agent.md) |
| DSAgentBench | 2026 | 在数据科学工作流中构建预测模型 | 275 个真实环境任务，含一个建模阶段 | 确定性的模型性能验证 | [卡片](../works/dsagentbench.md) |
| gwBenchmarks | 2026 | 构建高精度代理模型并拟合残余体性质 | 8 个任务，基于超过 10^8 核时的 NR 级数据 | 通过外部评估器达到约 1e-4 的相对误差；agent 未能达标 | [卡片](../works/gwbenchmarks.md) |
| onepot-Bench 0 | 2026 | 预测反应结果并选择催化剂 | 三部分套件（cheminformatics、拒答、合成），私有实验室数据 | 对照私有实验真实值进行预测 | [卡片](../works/onepot-bench.md) |
| RealPDEBench | 2026 | 衔接真实与模拟物理的科学 ML 模型 | 5 个真实+配对模拟数据集，3 个任务，8 项指标，10 个基线 | 数据/物理指标；预训练可提升准确率 | [卡片](../works/realpdebench.md) |
| Stargazer | 2026 | 迭代式为 RV 序列拟合 Keplerian 轨道模型 | 120 个任务（100 个合成 3 个层级 + 20 个真实），REPL 反馈 | 逐项通过/未通过；Easy 80% 到 Hard 5.8%，真实数据 0% | [卡片](../works/stargazer.md) |
| VESTA / DAWN | 2026 | 对分布模型与时间序列模型提出假设、拟合并修正 | 400 个任务；工具箱在回合中逐步扩充，图件以视觉方式回读 | 拟合用 Jensen–Shannon 散度，时间序列用 ELPD-LOO | [卡片](../works/vesta-dawn.md) |
| AutoWorldModel-Bench | 2026 | 改进一个学习得到的世界模型对实体动力学的前向预测 | 八个游戏环境统一采用共享的结构化状态张量格式，感知被移除 | 留出集上 Position L1 与 Alive F1 在 1/10/20 三个时程上的组合，权重 0.1/0.2/0.7 | [卡片](../works/autoworldmodel-bench.md) |

## Related Works

- [DSAgentBench](../works/dsagentbench.md)
- [MLAgentBench](../works/mlagentbench.md)
- [DSBench](../works/dsbench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatText](../works/mattext.md)
- [MLE-bench](../works/mle-bench.md)
- [AlchemyBench](../works/alchemybench.md)
- [FGBench](../works/fgbench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [BioXArena](../works/bioxarena.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [Model Discovery Agent](../works/model-discovery-agent.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [RealPDEBench](../works/realpdebench.md)
- [Stargazer](../works/stargazer.md)
- [ChemEBench](../works/chemebench.md)
- [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md)
- [Mephisto](../works/mephisto.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
