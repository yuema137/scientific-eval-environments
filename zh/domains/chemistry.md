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
| Model Discovery Agent | 2026 | 在七个可控化学条件里选择最有信息量的组合，发现隐藏的 enzyme-kinetic rate law。 | ChemBench/ActiveSciBench-Chem 的 36 个 interactive task（12 类 mechanism × 3 个难度），2 个 seed，最多 60 次 designed experiment。 | 在 1,000 个新条件上计算 held-out reaction-rate error，再用 SymPy 检查发现的 rate law 是否和真值数学等价。 | [→](../works/model-discovery-agent.md) |
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
| ChemEBench | 2025 | 该 benchmark L2 层级上的分子化学：SMILES 转 IUPAC 命名、依文字描述给分子命名、分子性质预测与反应预测。 | 整套 benchmark 分三个递进层级，覆盖 15 个维度、101 个不同任务，L2 是其中一级；题目为静态单次作答，比较 14 个模型。 | 客观题计准确率；主观的简答与计算题按完整性与清晰度打 0–5 分，并逐步核查推理链。 | [→](../works/chemebench.md) |
| Imaging-101 | 2026 | 化学与材料计算成像——它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| SciVQR | 2026 | 化学中的多模态科学推理，六个顶层计分学科之一。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 按学科报告零样本准确率，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 贯穿各层级的化学：对化学论文做文献问答，外加由模型自行编写并执行 Python 分析代码的数据驱动发现。 | 8,735 个实例中化学占 1,116 个——200 个通用科学问答、886 个单语文献问答、10 个综述选题与 20 个数据驱动发现任务；18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性；发现层用基于执行的 Success Rate，生成的程序跑不起来即计零分。 | [→](../works/hiscibench.md) |
| MolClaw | 2026 | 药物分子的计算化学：基于 RDKit 描述符的性质筛选、结合亲和力比较、分子对接与虚拟筛选、官能团改造，以及朝 QED、LogP 与 LogS 目标做的理化性质优化。 | MolBench 分三层——筛选（50 道性质筛选、37 道结合亲和力、25 道对接）、优化（39 道官能团题，外加一项性质优化子任务，其题量为 `TODO(reference)`），以及三项端到端发现挑战，需要 8 到 50 次以上的连续工具调用；题目取自 CARA/ChEMBL、ACNet 与 ChemCoTBench。 | 性质筛选与结合亲和力比较用 Accuracy，对接筛选用 Hits@3，优化用操作准确率、性质变化量与成功率，端到端一层用任务专属的加权 rubric（rubric 权重与评审身份为 `TODO(reference)`）。 | [→](../works/molclaw.md) |
| CASCADE | 2025 | SciSkillBench 中的化学研究任务：检索、处理与分析化学数据，并借助专用化学工具包与仿真代码完成计算。 | 116 个材料科学与化学任务——76 个数据类、40 个计算类，再按说明详细程度分为 58 个点明关键函数的 Level 0 任务与 58 个只给出高层目标的 Level 1 任务；每种配置重复三次，共 16,008 次实验运行。 | 以结果为准的自动打分：在预设容差阈值内比对 agent 处理后的输出与标准答案，报告为成功率（GPT-5 下 DeepSolver 为 93.26%，Native 配置为 35.36%）。 | [→](../works/cascade.md) |
| OntoLearner | 2026 | 为化学——它的本体集合覆盖的 22 个领域之一，官方 hub 上另有一份化学数据集——构建本体结构：给术语定类型、恢复类型之间的 is-a 层级、抽取非分类关系。 | 覆盖 22 个领域的 180 个机器可读本体，为三项本体学习任务备好可直接接入流水线的 train/dev/test 切分；共评测 22 个检索模型与 12 个 LLM，设定是单次结构化预测而非 agentic 循环。 | 以归一化的成对与三元组匹配对照金标准本体结构计算 precision、recall 与 F1；卡片中逐领域、逐模型的分数为 `TODO(reference)`，因论文的结果章节无法获取。 | [→](../works/ontolearner.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的化学子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`ORG` 有机化学与反应机理 · `ANAL` 分析化学与波谱 · `SYN` 合成路线设计与逆合成 · `QC` 量子化学与电子结构 · `MD` 分子动力学与生物分子模拟 · `CHEMINF` 化学信息学与分子表示 · `MOLDES` 分子设计与生成 · `MED` 药物化学与药物发现 · `BIOCHEM` 生物化学与化学生物学 · `NANO` 纳米材料与材料化学 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

**两个分，不是一个。** 各列分成**覆盖面**——评测设置把什么纳入了考察——与**严谨度**——它报出来的东西有多可信。两者分开求和，因为它们方向相反：一个 benchmark 可以什么都考一点却什么都没验扎实，而一个刻意收窄的 benchmark 反而可能是本页最可信的。各行按 `Cov` 从高到低排，`Cov` 相同时比 `Rig`，仍相同则保持 Comparison 表原序。以覆盖面领先排序，是因为读者扫表时先问的就是这件事——*这个 benchmark 到底有没有把我关心的问题纳入考察*——`Rig` 随后回答它报出的东西能信到什么程度。

### 覆盖面（`Cov`，满分 7）

是非列，按稀缺程度排序——做到的工作越少排得越靠前，因此这一组的左侧就是该领域的薄弱处。几乎人人都满足的性质不设列：*是否编写并运行代码* 就是因此删去的。

- **Net** — 允许联网或实时外部检索；给定的固定语料库不算。
- **E2E** — 端到端研究：只给问题或目标，不提供源论文、参考实现或分步规范，整个研究过程由 agent 自己推进。
- **Cost** — 预算或资源成本被计入评分或明确定价，仅有步数上限不算。
- **MM** — 多模态内容是承重的，要么必须作为输入，要么作为产出物被打分。
- **Repro** — 以某项已发表结果为准，agent 需要复现或还原它。
- **Real** — 使用真实实验或观测数据，而非合成或仿真数据（数字孪生算仿真）。
- **Inter** — 交互式：agent 对环境、工具或仿真器多次动作，并根据反馈决定下一步。

### 严谨度（`Rig`，满分 13）

- **Human** — 有实测的人类专家基线或人类参考表现为整个量表定锚。若锚点只是一篇已发表结果或专家参考实现，而非实际跑出来的人类成绩，记 `◐`。
- **Rubric** — 专家撰写的 rubric 或官方评分标准，带具名维度或权重；连续型自动指标不算 rubric。
- **Contam** — 有刻意设计的机制让答案无法靠记忆得到：取材于训练截止之后、未发表或新撰写的题目、反事实改写、按需生成，或做过泄漏筛查。评测时把一篇已发表论文藏起来记 `◐`——藏起来并不能把它从预训练语料里去掉。
- **Verif** `0`–`3` — 这个分数要在多大程度上依赖对某个模型的信任。`0` 仅由 LLM judge 或 rubric 打分，且该判分器未经验证 · `1` judge/rubric 打分，且报告了与人类专家的一致性 · `2` 确定性校验与 judge/rubric 并用 · `3` 完全确定性——执行、测试、与参考解做数值比对、符号检查或证明内核，全程无 judge 介入。它取代了原先"有无确定性验证"的是非列：那一列 85% 的工作都满足，因而区分不出任何东西；做成阶梯后区分度很高。另有一个 `Judge` 列因与 `Verif` < 2 几乎等价而删去。
- **Scale** `0`–`3` — **本领域内**受评的条目数：`0` 少于 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 及以上 · `?` 原文未给出逐领域计数。它数的是条目而非工作量：30 个论文复现任务远比 3,000 道考试题费力，这一列看不见这一点。
- **Fail** `0`–`4` — 失败分析做到多深，因为"论文有失败分析"这句话的跨度太大——从一句话带过到专门设计的对照实验都算。`0` 除成绩外没有任何失败分析 · `1` 只有关于模型薄弱环节的叙述性评论，未给出类别 · `2` 有具名的错误类别或示例性案例分析，但没有计数或占比 · `3` 定量的失败刻画：带逐类计数或占比的分类体系，或能分离出特定失败条件的实测拆分 · `4` 在第 3 级之上，另有专门设计的对照实验或消融，用来检验失败*为何*发生。

### 怎么读这两个分

是非列按 `✔` 1 分、`◐` 0.5 分、`✘` 0 分、`?` 0 分计；分级列直接计其数值，`?` 计 0 分。`Domain` 不计分。

三点要留意。`?` 与 `✘` 的代价完全相同，所以两个分都是"该工作*可查证地*做到了多少"的下界，而不是对它的判决。两个分也都不是质量排名：`Cov` 高而 `Rig` 低，说的是这个 benchmark 什么都想够到却什么都没钉死；`Cov` 低而 `Rig` 高，说的是它把一件窄事量得很仔细——哪一种才是对的设计，完全取决于要回答什么问题。还有，`Cov` 描述的是*评测设置*而非科学本身：一份工作可以排在本表末尾，同时是它那个子领域最重要的论文。

跨领域套件的行按本领域的切片来写，与上面的 Comparison 表一致。
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| ScienceAgentBench | CHEMINF | ◐ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✔ | 2 | 1 | 2 | **7.5** |
| Imaging-101 | ANAL, NANO | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| PhySciBench | GEN | ◐ | ◐ | ◐ | ✔ | ✘ | ✔ | ✔ | **4.5** | ✘ | ✔ | ✘ | 2 | 2 | 1 | **6** |
| MolQuest | ANAL | ? | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| NatureBench | MOLDES | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 2 | 1 | 2 | **7** |
| MetaSyn | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 2 | ? | 3 | **6** |
| SciVisAgentBench | MD | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| SMDD-Bench | MED | ✘ | ✘ | ✔ | ◐ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 2 | 2 | **8** |
| MolClaw | MED, MOLDES | ✔ | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | **3** | ✘ | ✔ | ✘ | 2 | 2 | 2 | **7** |
| Science Edge Evaluation (SEE) | ANAL | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ◐ | 2 | ? | 4 | **6.5** |
| DrBencher | BIOCHEM | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 1 | 1 | **6** |
| CASCADE | CHEMINF, NANO | ✔ | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
| Model Discovery Agent | GEN | ✘ | ✔ | ✔ | ✘ | ✘ | ✘ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 1 | 4 | **8** |
| ChemCost | SYN | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | **2.5** | ✔ | ✘ | ✘ | 3 | 3 | 4 | **11** |
| ChemX | NANO, MED | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **2.5** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MDArena | MD, BIOCHEM | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ◐ | ✔ | ✘ | 2 | 1 | 2 | **6.5** |
| MOOSE-Chem | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✘ | **2.5** | ◐ | ◐ | ✔ | 1 | 1 | 2 | **6** |
| MaCBench | ANAL, NANO | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ◐ | 2 | ? | 4 | **6.5** |
| HiSciBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| MolLangBench | CHEMINF, MOLDES | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| ChemCensor / CREED | SYN | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ◐ | ✘ | ✔ | 3 | 3 | 2 | **9.5** |
| MolPuzzle | ANAL, ORG | ✘ | ✘ | ✘ | ✔ | ✘ | ? | ✘ | **1** | ✔ | ✘ | ✘ | 3 | 3 | 2 | **9** |
| SciVQR | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| AInsteinBench | QC, CHEMINF | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| onepot-Bench 0 | SYN, CHEMINF | ? | ✘ | ? | ? | ✘ | ✔ | ✘ | **1** | ? | ? | ✔ | 2 | ? | 0 | **3** |
| ChemBench | GEN | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0.5** | ✔ | ✘ | ◐ | 2 | 3 | 2 | **8.5** |
| FGBench | CHEMINF | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| MolecularIQ | CHEMINF | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| ChemIQ | ORG, ANAL | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 4 | **9.5** |
| ChemEval | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 2 | 2 | **8** |
| ChemCoTBench | MOLDES, ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| Speak-to-Structure (TOMG-Bench) | MOLDES | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
| FukuyamaBench | ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| QCBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 2 | 2 | **6.5** |
| SciCode | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | ? | 0 | **3.5** |
| ChemEBench | CHEMINF, ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ◐ | ✘ | 2 | ? | 0 | **2.5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note：`?` 表示来源没有把这一列说清楚，不是仓库推断它不存在。这个区别在 `Net` 和跨领域套件的逐领域 `Scale` 上尤其重要，因为论文经常只报总任务数。

## Related Works

- [Model Discovery Agent](../works/model-discovery-agent.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [MDArena](../works/mdarena.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [Imaging-101](../works/imaging-101.md)
- [OntoLearner](../works/ontolearner.md)
- [NatureBench](../works/naturebench.md)
- [PhySciBench](../works/physcibench.md)
- [MetaSyn](../works/metasyn.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [SciVQR](../works/scivqr.md)
- [ChemCost](../works/chemcost.md)
- [DrBencher](../works/drbencher.md)
- [MolClaw](../works/molclaw.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [MolQuest](../works/molquest.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MolecularIQ](../works/moleculariq.md)
- [CASCADE](../works/cascade.md)
- [HiSciBench](../works/hiscibench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [ChemX](../works/chemx.md)
- [QCBench](../works/qcbench.md)
- [FGBench](../works/fgbench.md)
- [ChemEBench](../works/chemebench.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [MolLangBench](../works/mollangbench.md)
- [ChemIQ](../works/chemiq.md)
- [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md)
- [MaCBench](../works/macbench.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [ChemEval](../works/chemeval.md)
- [SciCode](../works/scicode.md)
- [MolPuzzle](../works/molpuzzle.md)
- [ChemBench](../works/chembench.md)
