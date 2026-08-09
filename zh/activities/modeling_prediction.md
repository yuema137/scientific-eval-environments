# 建模与预测

> [English](../../activities/modeling_prediction.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 构建或运用科学模型以预测量或行为的能力——预测与代理建模、预报、性质预测，以及以模型本身为核心产物的模型拟合。

## Scope

涵盖科学机器学习、性质回归与分类，以及学习用于预测的函数关系。与数据分析相区分（后者从观测数据得出结论）；二者仅在都被真正评估时才共现。仅在 ML 训练循环内部发生的优化不计入。

## Task Patterns

一类任务聚焦于**科学性质预测**——将分子或材料的结构映射到其性质。[LLM4Mat-Bench](../works/llm4mat-bench.md) 和 [MatText](../works/mattext.md) 都考察 LLM 能否从文本编码中预测晶体性质，二者得出了一致的结论：具备几何感知能力的专用模型依然占据主导地位。[FGBench](../works/fgbench.md) 将分子性质预测细化到官能团层面的推理，而 [AlchemyBench](../works/alchemybench.md) 和 [onePot-Bench](../works/onepot-bench.md) 则把预测范围扩展到合成配方以及反应/催化剂的结果，并以私有实验室数据作为评判依据。

第二类任务是**以优化模型指标为目标的 ML 工程**，要求 agent 迭代式地构建并训练模型。[MLAgentBench](../works/mlagentbench.md)、[MLE-bench](../works/mle-bench.md) 和 [MLE-Dojo](../works/mle-dojo.md) 把 ML 研究/工程构建成在 Kaggle 风格任务上不断改进指标的交互式循环；[DSBench](../works/dsbench.md) 在分析任务之外还加入了数据建模任务；[BioXArena](../works/bioxarena.md) 则在固定算力预算下，把完整的训练与提交流程应用于生物医学 ML。

第三类任务是**以物理为基础的预测与模型拟合**，其中拟合出的模型本身就是核心产物。[gwBenchmarks](../works/gwbenchmarks.md) 要求给出高精度的波形代理模型和残余体拟合，[RealPDEBench](../works/realpdebench.md) 衡量科学 ML 在物理系统上的仿真到现实差距，[Stargazer](../works/stargazer.md) 为径向速度序列拟合 Keplerian 轨道模型，而 [DiscoverPhysics](../works/discoverphysics.md) 则要求推断并实现反事实模拟世界的物理定律。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| MLAgentBench | 2023 | 迭代式改进某个 ML 模型的目标指标 | 13 个 ML 实验任务，可读写并执行代码，agentic | 超越起始代码基线；最佳 agent 平均 37.5% | [卡片](../works/mlagentbench.md) |
| DSBench | 2024 | 从数据文件出发的端到端预测性数据建模 | 540 个任务（74 个建模 + 466 个分析），多模态多表格 | 完成任务；最佳成绩解出 34.12% 的分析题 | [卡片](../works/dsbench.md) |
| LLM4Mat-Bench | 2024 | 从文本编码的晶体预测材料性质 | 静态回归/分类，约 1.9M 个结构、45 种性质、3 种模态 | 相对 CGCNN 的准确率；微调模型胜过生成式 LLM | [卡片](../works/llm4mat-bench.md) |
| MatText | 2024 | 从文本表示预测晶体性质 | 静态回归，9 种表示，参数量最高达 70B，2M 个结构 | 达到几何 GNN 基线水平；揭示几何盲区 | [卡片](../works/mattext.md) |
| MLE-bench | 2024 | 端到端 ML 工程以训练有竞争力的模型 | 75 个精选 Kaggle 竞赛，agentic，长时程 | Kaggle 奖牌门槛；o1-preview 在 16.9% 上获铜牌 | [卡片](../works/mle-bench.md) |
| AlchemyBench | 2025 | 预测完整的材料合成配方及结果 | 对 17,000 个专家验证配方的静态预测 | LLM-as-a-Judge 与专家评估的一致性 | [卡片](../works/alchemybench.md) |
| FGBench | 2025 | 在官能团层面推理分子性质 | 625K 个问题（245 个官能团）；7K 精选 LLM 子集，静态 QA | 回归/分类准确率；LLM 表现吃力 | [卡片](../works/fgbench.md) |
| MLE-Dojo | 2025 | 借助反馈迭代式构建并优化 ML 模型 | 200+ 个 Kaggle 挑战，Gym 风格交互，可用于 SFT/RL 训练 | 8 个 LLM 上的迭代改进与解答质量 | [卡片](../works/mle-dojo.md) |
| BioXArena | 2026 | 构建并训练生物医学预测模型 | 76 个端到端任务，9 个领域，2 小时单 GPU 预算 | 隐藏标签 0-1 评分；最佳 MLEvolve 0.666 | [卡片](../works/bioxarena.md) |
| DiscoverPhysics | 2026 | 推断并实现反事实世界的物理定律 | 22 个模拟 N-body 世界，迭代式实验提案 | 轨迹 MSE 加上按 rubric 评判的解释；最佳约 50% | [卡片](../works/discoverphysics.md) |
| gwBenchmarks | 2026 | 构建高精度代理模型并拟合残余体性质 | 8 个任务，基于超过 10^8 核时的 NR 级数据 | 通过外部评估器达到约 1e-4 的相对误差；agent 未能达标 | [卡片](../works/gwbenchmarks.md) |
| onepot-Bench 0 | 2026 | 预测反应结果并选择催化剂 | 三部分套件（cheminformatics、拒答、合成），私有实验室数据 | 对照私有实验真实值进行预测 | [卡片](../works/onepot-bench.md) |
| RealPDEBench | 2026 | 衔接真实与模拟物理的科学 ML 模型 | 5 个真实+配对模拟数据集，3 个任务，8 项指标，10 个基线 | 数据/物理指标；预训练可提升准确率 | [卡片](../works/realpdebench.md) |
| Stargazer | 2026 | 迭代式为 RV 序列拟合 Keplerian 轨道模型 | 120 个任务（100 个合成 3 个层级 + 20 个真实），REPL 反馈 | 逐项通过/未通过；Easy 80% 到 Hard 5.8%，真实数据 0% | [卡片](../works/stargazer.md) |

## Related Works

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
- [gwBenchmarks](../works/gwbenchmarks.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [RealPDEBench](../works/realpdebench.md)
- [Stargazer](../works/stargazer.md)
