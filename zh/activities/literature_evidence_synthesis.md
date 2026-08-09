# 文献检索与证据综合

> [English](../../activities/literature_evidence_synthesis.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 检索、获取并综合科学文献与证据的能力——定位相关论文、筛选研究、抽取结构化证据，并将多个来源整合为有依据的科学回答或综述。

## Scope

涵盖定向找论文、开放式文献收集、系统综述与元分析、以证据为依托的问答，以及以文献为依托的结构化数据抽取。若 agent 只是把某篇给定论文当作完成另一任务的说明来阅读，则不计入——文献/证据环节本身必须是受评能力。

## Task Patterns

这一活动最直接的体现是智能体的论文检索，其交付物是一组文献，而非一段书面回答。[AutoResearchBench](../works/autoresearchbench.md) 将其清晰地划分为两类：针对某篇已知论文的精确检索（Deep Research，600 条查询），以及对满足条件的所有论文进行开放式收集（Wide Research，400 条查询）；[ScholarQuest](../works/scholarquest.md) 则围绕四类研究意图组织 CS 论文的迭代式检索，并报告称即便是最优秀的智能体，召回率依然偏低。[AstaBench](../works/astabench.md) 以套件规模覆盖了同一领域，设有文献理解类别（PaperFindingBench、LitQA2 变体、表格生成），背后依托受日期限制的生产级检索工具；[SciExplore](../works/sciexplore.md) 则把检索安排成一条递进路径，从数据库导航、模糊检索、缺失引用补全，一直到跨来源综合。

第二类任务考察以证据为依托的问答以及对文献的多跳综合。[Aviary](../works/aviary.md) 贡献了 LitQA2/PaperQA 文献研究环境；[LAB-Bench](../works/lab-bench.md) 及其后续版本 [LABBench2](../works/labbench2.md) 都把文献记忆与推理嵌入到更广泛的生物学能力套件中，其中 LABBench2 通过将答案锚定在 PDF 和图像上，让任务重新贴近真实场景。[MedBrowseComp](../works/medbrowsecomp.md) 把多跳综合推向真实、碎片化的医学来源，考察的正是信息时效性与整合协调的能力；[DeepResearch Bench](../works/deepresearch-bench.md) 则通过其 RACE 和 FACT 框架，评估端到端的深度研究报告生成与引用锚定。[BioKGBench](../works/biokgbench.md) 把文献理解重新表述为可核验的行为——将论断核实与 KGQA 组合起来，用于在生物医学知识图谱中查找事实性错误。

第三类任务是以文献为依托的结构化抽取：把论文转化为结构化记录。[MatViX](../works/matvix.md) 从完整篇幅的材料学文章中抽取成分组成与性质曲线并生成 JSON（评分对象包括图中曲线，而不仅是实体）；[ChemX](../works/chemx.md) 则从涵盖纳米材料与小分子数据集的文档中完成经专家验证的化学信息抽取。[MetaSyn](../works/metasyn.md) 处于系统综述 / 元分析这一终点，要求智能体在 PI/ECO 协议下从含有干扰项的语料中筛选出符合条件的研究集合并加以综合。

边界情形：Aviary、LAB-Bench、LABBench2 和 AstaBench 都是多能力套件，其中只有文献、问答与抽取相关的组成部分才明确落在本活动范围内（序列、克隆、实验流程以及代码类子任务则不属于）。[MOOSE-Chem](../works/moose-chem.md) 在一个 3,000 篇论文的语料上进行灵感检索，但其目的是重新发现假说而非证据综合，因此它主要归入 Experiment Design & Scientific Discovery。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| Aviary | 2024 | 通过 PaperQA 环境从文献中回答研究问题 | LitQA2/PaperQA 环境，248 道题（49 道为留出集）；多步骤 | 给出有文献依据的正确答案 | [卡片](../works/aviary.md) |
| BioKGBench | 2024 | 核实论断并查询知识图谱以发现事实性错误 | SCV + KGQA（2,000+ 条）组合成 KGCheck（225 个实例） | 在生物医学知识图谱中定位事实性错误 | [卡片](../works/biokgbench.md) |
| LAB-Bench | 2024 | 文献记忆/推理并结合数据库访问问答 | 涵盖 8 个类别的选择题（2,400+ 道）；静态，工具使用可选 | 相对专家生物学家基线的准确率 | [卡片](../works/lab-bench.md) |
| MatViX | 2024 | 从全文材料学文章中抽取结构化数据 | 零样本多模态抽取，324 篇文章生成 1,688 条 JSON 记录 | 成分组成与性质曲线的还原保真度 | [卡片](../works/matvix.md) |
| MOOSE-Chem | 2024 | 检索灵感以重新发现化学假说 | 51 篇标注论文，基于 3,000 篇论文的灵感语料；智能体流水线 | 与标准答案相符的假说 | [卡片](../works/moose-chem.md) |
| AstaBench | 2025 | 文献理解：论文检索、问答、表格生成 | 2,400+ 题套件中的文献理解基准；受日期限制的工具 | 相对基线的成本受控得分 | [卡片](../works/astabench.md) |
| ChemX | 2025 | 从文档中抽取结构化化学数据 | 针对 10 个精选数据集的智能体文档抽取 | 相对专家验证真值的结构化记录 | [卡片](../works/chemx.md) |
| DeepResearch Bench | 2025 | 开展端到端深度研究并生成带引用的报告 | 100 个专家任务，22 个领域（50 英文/50 中文） | 报告质量（RACE）与引用锚定（FACT） | [卡片](../works/deepresearch-bench.md) |
| MedBrowseComp | 2025 | 从实时来源检索并综合多跳事实 | 1,000+ 道精选问题；深度研究与 computer-use | 给出经协调整合的最新正确答案 | [卡片](../works/medbrowsecomp.md) |
| AutoResearchBench | 2026 | 找到目标论文并收集所有符合条件的论文 | 1,000 条查询：Deep Research（600）+ Wide Research（400） | 定位到目标论文/完整的论文集合 | [卡片](../works/autoresearchbench.md) |
| LABBench2 | 2026 | 在真实产物情境下进行文献/专利/试验问答 | 涵盖 PDF、图像、文件的 1,900 个任务；静态测评框架 | 准确率（比 LAB-Bench 难 26-46%） | [卡片](../works/labbench2.md) |
| MetaSyn | 2026 | 筛选符合条件的研究并综合成系统综述 | 422 项专家元分析；含干扰项的 PubMed 语料 | 正确的符合条件研究集合与忠于协议的综合 | [卡片](../works/metasyn.md) |
| ScholarQuest | 2026 | 按研究意图进行迭代式学术论文检索 | 1,000+ 个 CS 主题，四类意图类别 | Recall@100/@All（最优 | [卡片](../works/scholarquest.md) |
| SciExplore | 2026 | 导航数据库并整合跨来源证据 | 103 个专家任务，四种递进类型，10+ 个学科 | 正确的检索、锚定与综合 | [卡片](../works/sciexplore.md) |

## Related Works

- [Aviary](../works/aviary.md)
- [BioKGBench](../works/biokgbench.md)
- [LAB-Bench](../works/lab-bench.md)
- [MatViX](../works/matvix.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [AstaBench](../works/astabench.md)
- [ChemX](../works/chemx.md)
- [DeepResearch Bench](../works/deepresearch-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [LABBench2](../works/labbench2.md)
- [MetaSyn](../works/metasyn.md)
- [ScholarQuest](../works/scholarquest.md)
- [SciExplore](../works/sciexplore.md)
