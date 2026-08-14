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

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [Aviary](../works/aviary.md)
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [SciAgentArena](../works/sciagentarena.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MDArena](../works/mdarena.md)
- [SciCode](../works/scicode.md)
- [GenoTEX](../works/genotex.md)
- [BixBench](../works/bixbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SpatialBench](../works/spatialbench.md)
- [BAISBench](../works/baisbench.md)
- [BioXArena](../works/bioxarena.md)
- [BioProBench](../works/bioprobench.md)
- [SciGym](../works/scigym.md)
- [LAB-Bench](../works/lab-bench.md)
- [LABBench2](../works/labbench2.md)
- [BioKGBench](../works/biokgbench.md)
- [ScienceBoard](../works/scienceboard.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
