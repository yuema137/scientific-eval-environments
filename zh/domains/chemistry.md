# Chemistry

> [English](../../domains/chemistry.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

作为科学的化学，包括计算化学与分子设计。化学过程工程归属 Chemical Engineering。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| ScienceAgentBench | 2024 | 计算化学任务——其 102 个任务中的 20 个——提取自经同行评审的数据驱动发现工作流。 | 每个任务要求生成一个自包含的 Python 程序，复现真实论文中的分析。 | 有效执行加逐任务手写的成功检查器，对照专家标注参考（如指标阈值）；图形输出由 GPT-4o 评判。 | [→](../works/scienceagentbench.md) |
| NatureBench | 2026 | 达到 Nature 系列 Molecular Design 研究的已发表 SOTA——其 90 个任务中的 11 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的化学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Chemistry 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文产物的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| MDArena | 2026 | 运行真实的分子动力学计算化学工作流：轨迹分析、体系搭建、炼金术式（alchemical）自由能计算与增强采样。 | 源自在研项目的 50 个容器化任务，覆盖 29 个分子体系与 14 种研究方案。 | 以 Strict-Pass@1 为主指标，另以 correctness 与过程奖励指标为部分进展计分。 | [→](../works/mdarena.md) |
| PhySciBench | 2026 | 在物理与化学各半的题集中回答化学侧的专家 deep-research 问题，针对推理链脆弱、跨步骤知识迁移有限与缺少自我验证。 | 200 道专家整理的问题，物理与化学各半，组织为呼应真实科研工作流的六类任务。 | 基于准确率比较最先进模型与 agent 系统，并在准确率之外报告成本。 | [→](../works/physcibench.md) |
| MetaSyn | 2026 | 进行忠实于协议的系统综述与 meta 分析；化学是其 422 个专家整理 meta 分析所覆盖的主题之一。 | 多阶段系统综述工作流：在掺入不合格干扰文献的共享 PubMed 文献库中，依据带结构化 PI/ECO 标准的研究问题找出应纳入的研究。 | 对照原综述作者实际纳入的研究集做识别评估，并以分阶段评估定位 meta 分析流程中的失败环节。 | [→](../works/metasyn.md) |
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，化学是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的参考解与测试用例执行。 | [→](../works/scicode.md) |
| SMDD-Bench | 2026 | 面向蛋白靶点求解药物化学设计问题——2D 药效团识别、骨架跃迁、先导化合物优化、片段组装。 | 有限 oracle 调用预算下、102 个靶点上 502 个保证有解的多轮任务。 | 保证有解实例上的解出率；最佳前沿模型 40.2%。 | [→](../works/smdd-bench.md) |
| AInsteinBench | 2025 | 解决生产级科学仓库中的维护者 PR 任务；量子化学与化学信息学在其六个代码库之列。 | 可执行环境中的仓库级 coding agent 任务。 | 经专家评审整理的测试驱动验证。 | [→](../works/ainsteinbench.md) |
| ChemBench | 2024 | 以人类化学家的专业水平为对照，测量化学知识与推理。 | 2,700 多个策划问答对；不借助工具的静态问答。 | 自动化框架评分，配招募的化学家基线与置信度分析。 | [→](../works/chembench.md) |
| ChemEval | 2024 | 评估科研人员需要的化学能力，从文献理解到深入的化学知识。 | 42 个任务，覆盖 4 个递进层级与 12 个维度，数据来自开源与专家手工设计。 | 精选示例与提示下的零样本/少样本评估。 | [→](../works/chemeval.md) |
| ChemCoTBench | 2025 | 把分子性质优化与反应预测当作分步化学操作来求解。 | 1,495 个样本、22 个任务，以加/删/换的模块化工作流呈现。 | 在标注操作工作流上的结构化评估，配推理分类法。 | [→](../works/chemcotbench.md) |
| MolecularIQ | 2026 | 在分子图——决定分子性质的结构——上做推理。 | 符号可验证的结构推理任务；静态评估。 | 对照分子图的符号验证；失败可定位到结构类型。 | [→](../works/moleculariq.md) |
| ChemIQ | 2025 | 不借助工具回答有机化学核心问题，含 NMR 结构解析。 | 816 道构造式简答题，分 8 个类别。 | 无 judge 的程序化判分：精确匹配、OPSIN 解析 IUPAC、规范 SMILES。 | [→](../works/chemiq.md) |
| FGBench | 2025 | 把分子性质差异归因到具体官能团。 | 62.5 万个生成问题，覆盖 245 个官能团；7,000 个精选评测子集。 | 对照数据集标签的回归与分类评分。 | [→](../works/fgbench.md) |
| QCBench | 2025 | 完成横跨分析、生物/有机、普通、无机、物理、高分子与量子化学的定量计算。 | 7 个子领域、三档难度的 350 个问题，构造上防启发式捷径。 | 24 个 LLM 上分步数值计算的分档准确率。 | [→](../works/qcbench.md) |
| MolPuzzle | 2024 | 从 IR、MS、¹H-NMR、¹³C-NMR 谱图解析分子结构。 | 200 个实例分三阶段（理解、谱图解读、构建）；23,678 条样例。 | 最终结构精确匹配加各阶段得分，配人类基线。 | [→](../works/molpuzzle.md) |
| MolQuest | 2026 | 通过规划实验、整合异质谱图来解析结构。 | 实验步骤由模型自主发起的多轮交互回合。 | 最终结构准确率；SOTA 约 50%，多数模型低于 30%。 | [→](../works/molquest.md) |
| Speak-to-Structure (TOMG-Bench) | 2024 | 依据开放域自然语言指令生成、编辑与优化分子。 | 三族任务（MolEdit、MolOpt、MolCustom）；初版每子任务 5,000 个样本。 | 一对多的指令满足性检验，而非单参考匹配。 | [→](../works/tomg-bench.md) |
| MolLangBench | 2025 | 经由语言在字符串、图像与图上识别、编辑与生成分子结构。 | 三族任务；识别自动构造，编辑与生成由专家标注。 | 按任务计准确率；GPT-5 识别/编辑/生成分别 86.2%/85.5%/43.0%。 | [→](../works/mollangbench.md) |
| FukuyamaBench | 2026 | 为有机反应推导完整的基元步骤机理。 | 取自 Fukuyama《Advanced Organic Reaction Mechanism》的层级化机理推理问题。 | 完整路径精确匹配；已报告最好成绩 8.3%（微调 Qwen3-30B-A3B），对比 FlowER 的 5.1%。 | [→](../works/fukuyamabench.md) |
| ChemCensor / CREED | 2026 | 在多组前体皆化学合法的前提下评估单步逆合成。 | 基于合理性的 benchmark 框架，加数百万条经验证的反应记录。 | 以 ChemCensor 化学合理性指标取代精确匹配 Top-K。 | [→](../works/chemcensor.md) |
| MOOSE-Chem | 2024 | 重新发现近期高影响力化学论文的假说。 | 51 篇 2024 年 1 月后的论文，由化学博士标注；检索—组合—排序管线。 | 2024 年前知识截止控制下与标注真值假说的相似度。 | [→](../works/moose-chem.md) |
| ChemX | 2025 | 从纳米材料与小分子的科学文献中抽取结构化化学数据。 | 10 个人工整理、专家校验的数据集；agent 式文档抽取。 | 对照领域专家校验记录的抽取质量。 | [→](../works/chemx.md) |
| ChemCost | 2026 | 给化学反应定价：确定身份、检索报价、选择包装、计算成本。 | 冻结快照（2,261 种化学品、230,775 条供应商报价）上的 1,427 个可评估反应。 | 无 judge 的精确真值，配阶段级诊断；最强 agent 50.6% 落在 25% 相对误差内。 | [→](../works/chemcost.md) |
| onepot-Bench 0 | 2026 | 预测反应结果与催化剂选择，另测化学信息学素养与拒答行为。 | 私有三组件套件（ChemAbacus、SynthRefusal、SynthBench），基于实验室私有数据。 | 分组件对照私有实验真值评分。 | [→](../works/onepot-bench.md) |
| MaCBench | 2024 | 承担化学研究中的视觉工作：认读仪器、抽取数据、解读实验结果。 | 三个方面的多模态（图像 + 文本）任务；静态视觉-语言评估。 | 经 ChemBench 管线计准确率；抽取近乎完美，跨模态推断受限。 | [→](../works/macbench.md) |
| SciVisAgentBench | 2026 | 对化学数据做科学可视化与数据分析——化学是其七个应用领域之一——把自然语言意图转译为可执行的可视化操作，含分子动力学工具链。 | 108 个专家构造的 SciVis 案例，覆盖七个科学领域与 15 类可视化操作，经 CLI、MCP 服务器与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态流水线，结合 MLLM judge（报告为 Claude-Opus-4.6；与人工评分 Pearson 0.808）与确定性评估器——图像指标（PSNR、SSIM、LPIPS）、代码检查器与规则/逐案例验证器。 | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | 生物化学领域（归入 Chemistry）的网页浏览与计算交织问题——对化学实体做多跳识别，从 PubChem、ChEMBL、RCSB PDB 等来源检索定量属性，再做领域特定计算。 | 由知识图谱链条答案优先合成的问题，需多跳识别、定量属性检索与多步计算；覆盖五个领域（生物化学、地球物理、金融、安全、历史），生物化学是其一。 | 基于执行：金标准答案由对知识图谱数值执行参数化代码算得，在约 2% 相对容差内评分；两阶段难度级联；人工校验有效率 76%。 | [→](../works/drbencher.md) |
| Science Edge Evaluation (SEE) | 2026 | 对真实化学实验数据——谱图（IR、NMR、质谱）、X 射线衍射及相关测量——做证据受限的科学推理，而非概念回忆；化学是其三个学科之一。 | 1,116 道专家整理的多模态题目（公开 1,049 道），覆盖三个实验学科（化学、生物、材料科学）与 17 个子领域，采用选择题与数值填空格式；视觉智能体设定另加网页检索与代码解释器。 | 对照专家标准答案评分——选择题精确匹配，数值答案按专家容差——采用严格的二元 LLM-as-judge 协议（Gemini 3.1 Pro）；图像消融检查确认每题都需要其视觉输入。 | [→](../works/science-edge-evaluation.md) |

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MDArena](../works/mdarena.md)
- [PhySciBench](../works/physcibench.md)
- [MetaSyn](../works/metasyn.md)
- [SciCode](../works/scicode.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [ChemBench](../works/chembench.md)
- [ChemEval](../works/chemeval.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [MolecularIQ](../works/moleculariq.md)
- [ChemIQ](../works/chemiq.md)
- [FGBench](../works/fgbench.md)
- [QCBench](../works/qcbench.md)
- [MolPuzzle](../works/molpuzzle.md)
- [MolQuest](../works/molquest.md)
- [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md)
- [MolLangBench](../works/mollangbench.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [ChemX](../works/chemx.md)
- [ChemCost](../works/chemcost.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [MaCBench](../works/macbench.md)
