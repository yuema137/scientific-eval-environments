# Biology

> [English](../../domains/biology.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

从分子到群体尺度的生命科学评估。生物信息学、基因组学与单细胞生物学折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Aviary | 2024 | 分子克隆（DNA 构建体操作）与蛋白质工程：为真实蛋白提出稳定化突变；另含科学文献研究（LitQA2）。 | 带终末奖励的 POMDP 环境：SeqQA（500 训练 / 约 140 测试克隆问题）、Protein Stability（在 megascale 稳定性数据集的 40 个蛋白上提出突变）、LitQA2（248 题）。 | SeqQA / LitQA2 按选择题准确率计分；蛋白任务当且仅当所提突变的 Rosetta ΔΔG < 0（稳定化）记为通过。 | [→](../works/aviary.md) |
| HeurekaBench | 2026 | 回答开放式单细胞生物学研究问题——派生自 13 篇 Nature 与 Cell 论文中的 41 条已验证洞见——agent 需在原研究数据集上自主设计并执行多步分析。 | 50 道开放题 + 50 道选择题（Lite 子集：22 + 18，限 750 MB 以下数据集），由半自动的洞见到问题流水线产出。 | 真值是已发表的研究发现；开放题由 G-Eval GPT-4o judge 按原子事实重合度打 1–5 分，选择题按准确率。 | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | 基因组学、数量生物学与转化生物医学中的多阶段统计分析，每题含 3–13 个推断岔路，貌似合理的错误选择会改变下游答案。 | 129 个问题，构建于因果结构完全已知的构造性模拟数据生成过程之上，刻意避开教科书案例。 | 对照可恢复目标的二元评分，含精确匹配规则与数值容差；无部分得分；每个模型–问题对独立尝试 10 次。 | [→](../works/genebench-pro.md) |
| SciAgentArena | 2026 | 覆盖单细胞组学、空间组学、计算药物发现、EHR 建模与遗传学的真实生物医学研究场景。 | 约 200 个任务，分四类（Data Analysis、Optimization、Discovery、Validity），在交互式、agent 无关的环境中运行；Validity 类含刻意不可行的请求。 | 按领域的逐步验证——专家设计的二元标准、动作级 F1 与任务原生指标（AUROC、Jaccard、相关系数）——基于执行与专家标准，不用 LLM judge。 | [→](../works/sciagentarena.md) |
| ScienceAgentBench | 2024 | 生物信息学任务——其 102 个任务中的 27 个——提取自经同行评审的数据驱动发现工作流。 | 每个任务要求生成一个自包含的 Python 程序，复现真实论文中的分析。 | 有效执行加逐任务手写的成功检查器，对照专家标注参考；图形输出由 GPT-4o 评判。 | [→](../works/scienceagentbench.md) |
| NatureBench | 2026 | 达到 Nature 系列 Cellular Omics（31）与 Protein Biology（16）研究的已发表 SOTA——其 90 个任务中的 47 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| AIRS-Bench | 2026 | 其四个领域之一的生物信息学中的前沿研究任务，覆盖完整研究生命周期，不提供基线代码。 | 套件共 20 个任务；agent 以 CSV 提交留出测试集上的预测。 | 基于执行、只看结果：任务专属评估脚本计分；SOTA 归一化分数，接近上限处用 'march of nines' 变换。 | [→](../works/airs-bench.md) |
| AstaBench | 2025 | 其 11 个 benchmark 的科研套件中的生物学领域 benchmark——如 DiscoveryBench 的数据驱动发现——与以 CS 为主的文献、代码与发现任务并列。 | 11 个 benchmark 共 2,400+ 个问题，配标准、可复现的工具环境；已为 57 个 agent 计分。 | 各 benchmark 自有指标，从精确匹配到 LLM 评判的假设匹配，随时间不变的美元成本核算与分数–成本 Pareto 前沿一并报告。 | [→](../works/astabench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Life Sciences 分组下的生物学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Life 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文产物的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| MDArena | 2026 | 运行真实的生物分子模拟工作流——包括膜蛋白体系——覆盖轨迹分析、体系搭建、自由能计算与增强采样。 | 源自在研项目的 50 个容器化任务，覆盖 29 个分子体系与 14 种研究方案。 | 以 Strict-Pass@1 为主指标，另以 correctness 与过程奖励指标为部分进展计分。 | [→](../works/mdarena.md) |
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，生物学是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的参考解与测试用例执行。 | [→](../works/scicode.md) |
| GenoTEX | 2024 | 自动化基因表达分析以研究基因-性状关联：按计算基因组学标准完成数据集选择、预处理与统计分析。 | 911 个数据集上的 1,384 个分析问题（官方仓库）；带自我纠错的多步编程流水线。 | 对照生物信息学家整理的专家标注、参考代码与结果。 | [→](../works/genotex.md) |
| BixBench | 2025 | 完成取自真实已发表 notebook 分析的探索式计算生物学数据分析。 | 50+ 场景、约 300 个开放式问题（摘要口径；当前仓库为 205 个问题），以容器化执行的多步 agent 轨迹运行。 | LLM 判分的开放作答加精确匹配选择题；多副本多数投票。 | [→](../works/bixbench.md) |
| BioAgent Bench | 2026 | 完成端到端生物信息学流水线：RNA-seq、变异检测、宏基因组及相关工作流。 | 人工整理的流水线任务，从提示做到具体输出产物，跨多个 agent harness。 | LLM 判分器基于输出产物评进度与有效性；扰动鲁棒性套件（损坏输入、诱饵、提示膨胀）。 | [→](../works/bioagent-bench.md) |
| scBench | 2026 | 完成能复原已知生物学结果的单细胞 RNA-seq 分析步骤。 | 394 个可验证问题，横跨六种测序平台与七类任务，均从步骤前数据快照出发。 | 确定性判分器检验关键生物学结果的复原；准确率。 | [→](../works/scbench.md) |
| scBench-Long | 2026 | 在不预设方法的前提下，从原始或近原始数据复原真实单细胞研究已发表的科学结论。 | 21 项长 horizon 评估，覆盖 scRNA/TCR、RNA+ATAC、跨物种与免疫组库数据；1,068 条完成轨迹。 | 受控答案词表配确定性判分与轨迹评分标准。 | [→](../works/scbench-long.md) |
| SpatialBench | 2025 | 分析真实空间生物学数据以复原已知生物学结果。 | 146 个可验证问题，横跨五种空间技术与七类任务，从步骤前快照出发。 | 确定性判分器检验关键生物学结果的复原；准确率。 | [→](../works/spatialbench.md) |
| BAISBench | 2025 | 注释细胞类型，并回答锚定于已发表单细胞研究结论的发现类问题。 | 15 个专家标注的注释数据集加派生自 41 项研究的 193 道选择题；六位研究生水平生物信息学家的人类基线。 | 层级化细胞类型树的注释评分，加对照已发表结论的选择题正确率。 | [→](../works/baisbench.md) |
| BioXArena | 2026 | 在从序列建模到生物医学影像的九个领域上，对生物医学数据构建并训练预测模型。 | 标准化 2 小时单 GPU 环境中的 76 个端到端 ML 任务；agent 针对私有测试样本提交预测。 | 隐藏标签配留出判分器与归一化到 0–1 的生物学感知指标。 | [→](../works/bioxarena.md) |
| BioProBench | 2025 | 对生物湿实验协议做理解、排序、纠错、生成与推理。 | 22,413 份人工撰写协议的 523,784 个任务实例，五类任务；静态评估。 | 按任务的指标，含步骤召回/精确率、Kendall's tau、精确匹配与 BLEU。 | [→](../works/bioprobench.md) |
| SciGym | 2025 | 迭代设计实验以揭示隐藏系统生物学模型的机制。 | 在隐藏 SBML 系统上的按序实验设计回合；137 个受评，共发布 350 个。 | 复原模型对照隐藏的真值 SBML 系统。 | [→](../works/scigym.md) |
| LAB-Bench | 2024 | 考查生物学研究的实用能力：文献、图表、数据库、协议、DNA/蛋白质序列与克隆。 | 八类 / 30 个子任务的 2,400+ 道选择题；静态，可选配工具。 | 对照人类专家生物学研究者的选择题评分。 | [→](../works/lab-bench.md) |
| LABBench2 | 2026 | 同样的生物学研究能力，置于真实情境：PDF、图片与生物信息学文件。 | 近 1,900 个任务，子任务族经加固并新增专利、来源质量与临床试验。 | 经发布的评估 harness 计算的准确率；较 LAB-Bench 各模型下滑 −26% 至 −46%。 | [→](../works/labbench2.md) |
| BioKGBench | 2024 | 验证科学主张并深入盘查生物医学知识图谱以定位事实错误。 | 2,000+ 原子实例（主张验证、KGQA）加 225 个标注的 agentic KGCheck 实例，覆盖 UniProt、STRING、Reactome、DisGeNET。 | 原子任务正确率加 agent 级 KGCheck 评分；发现 90 余处真实数据库错误。 | [→](../works/biokgbench.md) |
| SciVisAgentBench | 2026 | 对生物学数据的科学可视化与数据分析——其七个应用领域之一——将自然语言意图转成可执行的可视化操作，含基于 napari 的生物影像工具。 | 108 个专家精制的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，经 CLI、MCP server 与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态流水线：将 MLLM judge（报告为 Claude-Opus-4.6；与人工评分 Pearson 0.808）与确定性评估器结合——图像指标（PSNR、SSIM、LPIPS）、代码检查器与基于规则/按案例的验证器。 | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | 生物化学领域（折并入 Biology）中"网页浏览加计算"交织的问题——多跳识别生物分子实体、从 UniProt、RCSB PDB、PubChem 等来源检索定量属性，再做领域特定计算。 | 答案优先的问题，由知识图谱链合成，需多跳识别、定量属性检索与多步计算；跨五个领域（生物化学、地球物理、金融、安全、历史），生物化学是其中之一。 | 基于执行：标准答案由在知识图谱取值上执行参数化代码算得，按约 2% 相对容差评分；两阶段难度级联；76% 经人工验证有效。 | [→](../works/drbencher.md) |
| Science Edge Evaluation (SEE) | 2026 | 对真实生物学实验数据的证据受限推理——生物活性测量、Cryo-EM 结构、Western blot 与凝胶电泳图像、以及显微成像——而非概念回忆；生物学是其三个学科之一。 | 1,116 道专家整理的多模态问题（1,049 道公开），横跨三个实验学科（化学、生物、材料科学）与 17 个子领域，含选择题与数值填空两种形式；视觉 agent 设定另加网页搜索与代码解释器。 | 对照专家真值评分——选择题精确匹配、数值答案按专家容差——在严格的二元 LLM-as-judge 协议（Gemini 3.1 Pro）下进行；图像消融检查确认每题都需要其视觉输入。 | [→](../works/science-edge-evaluation.md) |
| Fisher-R1 / P-Bench | 2026 | 在真实生物学数据集（取自数据存于 cBioPortal 的同行评审论文）上进行统计有效的假设检验——生物学是其三个领域之一——检验 agent 所报 p 值在数据假设下是否有效。 | 425 个开放式假设检验任务（Easy 203 / Hard 222），横跨经济学、生物与医学；每题只给一个假设与一个数据集，要求选择统计检验、计算 p 值并作出拒绝/不拒绝的结论。卡片未给出各领域计数。 | 标准答案的 p 值、检验统计量与决策取自对规范参考代码一次带日志运行的读数；按 Raw（决策匹配）与 Strict（决策加 p 值接近度在 0.5 个 z-score 单位内）计分，pass@1 与 pass@3。 | [→](../works/fisher-r1.md) |
| ScienceBoard | 2025 | 通过 UCSF ChimeraX 驱动的结构与分子生物学工作——它是承载各领域的六款专业软件之一。 | 单台 Ubuntu 虚拟机中 169 个人工整理的计算机使用任务：38 个纯 GUI、33 个纯 CLI、98 个 GUI+CLI 混合；逐软件任务数未公布。 | 通过支持精确匹配、区间判定与数值容差的模板，程序化检查关键中间输入/输出与虚拟机的最终状态；生物化学属得分最高的领域之一（GPT-5 最高 62.07%）。 | [→](../works/scienceboard.md) |
| Imaging-101 | 2026 | 生物计算成像——它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| SciVQR | 2026 | 生物学中的多模态科学推理，六个顶层计分学科之一。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 按学科报告零样本准确率，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 贯穿各层级的生物学：对 arXiv 生物学论文做文献解析、翻译与问答，外加由模型自行编写并执行 Python 分析代码的数据驱动发现。 | 8,735 个实例中生物学占 2,324 个——200 个通用科学问答、45 个文献 OCR、45 个翻译、1,952 个单语文献问答、45 个跨语文献问答、10 个综述选题与 27 个数据驱动发现任务；18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性；发现层用基于执行的 Success Rate，生成的程序跑不起来即计零分。 | [→](../works/hiscibench.md) |
| FlyAOC | 2026 | 端到端地策展果蝇（Drosophila melanogaster）基因注释：只给一个基因符号，agent 自行检索并阅读原始文献，产出以本体为依据的 Gene Ontology 功能条目、表达模式与历史同义词。 | 100 个 benchmark 基因，以开放式策展任务的形式提出，语料是一份固定的 16,898 篇全文论文集（论文称取自 PubMed Central，超过 1.4 亿词）；真值为 7,397 条 FlyBase 专家策展注释，分属三种注释类型。 | 对照 FlyBase 策展记录计算语义 recall@k——GO 与表达条目用 Gene Ontology 有向无环图上的 Wang 相似度（k = 20 与 k = 10），同义词用不区分大小写的精确匹配——以微平均 recall 为主指标。 | [→](../works/flyaoc.md) |
| Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes | 2026 | 为脊椎动物比较形态学产出 Entity-Quality 表型注释，把自由文本的性状-状态描述连接到 UBERON、PATO、BSPO 与 GO 本体中的条目。 | Dahdul 等（2018）的生物策展 Gold Standard——取自七项系统发育研究的 203 个性状（463 个性状状态），评分只限第 51–203 个性状（344 个状态）；五个前沿 LLM 作为 agentic 策展员，在一个自足工作区内运行，区内备有源 PDF、人类标注指南、各本体与一个校验脚本。 | 沿用原研究、未加改动的四项基于本体的语义相似度指标（SimJ、NIC、partial precision、partial recall），对照 Gold Standard 打分，并与三位受训人类生物策展员及 Semantic CharaParser 这一 NLP 基线比较。 | [→](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md) |
| BiomedSQL | 2025 | 围绕神经退行性疾病的 GWAS 汇总统计量、SMR 因果推断结果、等位基因频率与基因–通路关联，回答人类基因组学问题，其间还得自行补上问题从未言明的统计遗传学惯例——全基因组显著性阈值、效应方向。 | 68,000 组 question / SQL 查询 / answer 三元组，落在一个十张表的 BigQuery 数据库上（表的规模从几百行到 72.2M 行不等），由 40 条专家编写的种子查询套模板扩展而来；模型在一个有代表性的 546 题测试集上评分。 | 以 Execution Accuracy 为主指标（查询执行结果须与金标准执行结果完全一致），并列报告 Jaccard 部分得分与语法错误率；对照实测的两位生物医学分析师基线，其 EX 为 90.0%。 | [→](../works/biomedsql.md) |
| OntoLearner | 2026 | 为生物与生命科学——它的本体集合覆盖的 22 个领域之一——构建本体结构：给术语定类型、恢复类型之间的 is-a 层级、抽取非分类关系。 | 覆盖 22 个领域的 180 个机器可读本体，为三项本体学习任务备好可直接接入流水线的 train/dev/test 切分；共评测 22 个检索模型与 12 个 LLM，设定是单次结构化预测而非 agentic 循环。 | 以归一化的成对与三元组匹配对照金标准本体结构计算 precision、recall 与 F1；卡片中逐领域、逐模型的分数为 `TODO(reference)`，因论文的结果章节无法获取。 | [→](../works/ontolearner.md) |
| Apodex Discovery | 2026 | 腺相关病毒衣壳设计，涵盖活性预测、嗜性预测、结构预测与生成式设计。 | 20 个可执行环境之一，每个环境在固定的 episode 接口背后提供工具、数据、预算与隐藏验证器。 | 面向各项任务的实验适应度指标，对照已发表的最好水平——该系统在全部四项任务上都高出 7%。 | [→](../works/apodex-discovery.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的生物学子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`GENOM` 基因组学、遗传学与统计遗传学 · `SCB` 单细胞生物学与转录组 · `SPAT` 空间生物学与空间转录组 · `MOLB` 分子与细胞生物学、克隆与生物化学 · `PROT` 蛋白质科学与蛋白质工程 · `STRB` 结构生物学与生物大分子模拟 · `BIOINF` 生物信息学与计算生物学 · `SYSB` 系统生物学与机理建模 · `IMM` 免疫学 · `ECOEV` 生态、演化与个体生物学 · `DRUG` 药物发现与药理学 · `IMG` 生物成像与显微 · `PROTO` 湿实验方案与实验方法 · `CURA` 生物数据整编、本体与生物知识库 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

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
| Imaging-101 | IMG | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| AIRS-Bench | BIOINF | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 0 | 1 | **4.5** |
| FlyAOC | GENOM, CURA | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✘ | ✘ | 3 | 2 | 4 | **9.5** |
| scBench | SCB | ✔ | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **4.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| ScienceAgentBench | BIOINF | ✘ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✔ | ✔ | 2 | 1 | 2 | **7.5** |
| Apodex Discovery | PROT | ? | ◐ | ◐ | ✘ | ✔ | ✔ | ✔ | **4** | ◐ | ✔ | ◐ | 2 | 0 | 3 | **7** |
| AstaBench | GEN | ◐ | ✘ | ✔ | ✘ | ◐ | ✔ | ✔ | **4** | ✘ | ◐ | ◐ | 2 | ? | 2 | **5** |
| BioXArena | GEN | ✘ | ◐ | ✘ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 3 | 1 | 3 | **9** |
| SpatialBench | SPAT | ? | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| scBench-Long | SCB, IMM | ? | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✔ | ◐ | 2 | 1 | 3 | **7.5** |
| HeurekaBench | SCB | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | 2 | 3 | **7** |
| NatureBench | SCB, PROT | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 2 | 1 | 2 | **7** |
| Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes | ECOEV, CURA | ✘ | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| Fisher-R1 / P-Bench | GENOM | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| BixBench | BIOINF | ? | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | 2 | 1 | **5** |
| SciVisAgentBench | IMG | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| SciAgentArena | SCB, SPAT, GENOM, DRUG | ? | ◐ | ◐ | ✘ | ✘ | ✔ | ✔ | **3** | ◐ | ✔ | ✘ | 3 | 2 | 3 | **9.5** |
| GenoTEX | GENOM, BIOINF | ✘ | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | 3 | 2 | **9** |
| LABBench2 | GEN | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| ScienceBoard | STRB | ? | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | ? | 3 | **7** |
| Science Edge Evaluation (SEE) | STRB, IMG | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ✔ | 2 | ? | 3 | **6** |
| DrBencher | MOLB | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | ? | 1 | **5** |
| BioAgent Bench | BIOINF, GENOM | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ✘ | 0 | 0 | 3 | **3.5** |
| LAB-Bench | GEN | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2.5** | ✔ | ✘ | ✔ | 3 | 3 | 1 | **9** |
| Aviary | MOLB, PROT | ✘ | ✘ | ✔ | ✘ | ✘ | ◐ | ✔ | **2.5** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| MDArena | STRB | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✔ | ✘ | 2 | 1 | 3 | **7** |
| HiSciBench | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| SciGym | SYSB | ✘ | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| BioKGBench | CURA | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| BAISBench | SCB | ? | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| GeneBench-Pro | GENOM | ✘ | ◐ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| BiomedSQL | GENOM | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✔ | ✘ | ✘ | 2 | 2 | 4 | **9** |
| BioProBench | PROTO | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 3 | 3 | **9** |
| SciVQR | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| SciCode | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | CURA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [Apodex Discovery](../works/apodex-discovery.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [MDArena](../works/mdarena.md)
- [Imaging-101](../works/imaging-101.md)
- [OntoLearner](../works/ontolearner.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [scBench-Long](../works/scbench-long.md)
- [NatureBench](../works/naturebench.md)
- [SciAgentArena](../works/sciagentarena.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md)
- [BioXArena](../works/bioxarena.md)
- [SciVQR](../works/scivqr.md)
- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [FlyAOC](../works/flyaoc.md)
- [scBench](../works/scbench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [LABBench2](../works/labbench2.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [HeurekaBench](../works/heurekabench.md)
- [HiSciBench](../works/hiscibench.md)
- [SpatialBench](../works/spatialbench.md)
- [AstaBench](../works/astabench.md)
- [SciGym](../works/scigym.md)
- [ScienceBoard](../works/scienceboard.md)
- [BiomedSQL](../works/biomedsql.md)
- [BAISBench](../works/baisbench.md)
- [BioProBench](../works/bioprobench.md)
- [BixBench](../works/bixbench.md)
- [Aviary](../works/aviary.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SciCode](../works/scicode.md)
- [LAB-Bench](../works/lab-bench.md)
- [BioKGBench](../works/biokgbench.md)
- [GenoTEX](../works/genotex.md)
