# Scientific Agent Benchmarks

> [English](../../topics/scientific_agents.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

Scientific agent benchmark 是在真实科学研究或实践中提取任务的 AI agent 评估——计算工作流、参数调优、文献 grounding 的问题，或对已发表结果的复现。它们与通用 agent benchmark 的区别在于任务来源（真实科学工作）和正确性标准（对已发表或专家定义结果的匹配）。

## Motivation

科学工作具有通用 agent benchmark 建模不足的若干特征：中间评估可能开销昂贵（仿真、实验）、任务通常长 horizon、正确性有时需要参照已发表或专家标准而非合成 ground truth、工作流涉及需要领域知识才能正确串联的异构工具。给科学 agent 打分需要在评估中显式关注这些特征——因此值得作为独立 topic。

## Existing Approaches

- **可执行的科学工作流。** [Terminal-Bench Science](../works/terminal-bench-science.md) 在容器中用 pytest 确定性验证 AI agent 在自然科学计算工作流上的表现，覆盖五个科学领域。
- **以出版物 SOTA 锚定难度。** [NatureBench](../works/naturebench.md) 从 Nature-family 论文蒸馏 90 个任务，追问 coding agent 是否能达到已发表 SOTA——揭示了显著缺口：最强 agent 仅在 17.8% 的任务上超越已发表 SOTA（匹敌 47.8%）。
- **专家验证、基于执行的任务。** [ScienceAgentBench](../works/scienceagentbench.md) 从四个学科的 44 篇同行评审论文中提取 102 个任务，邀请九位领域专家验证，并将每个任务的输出统一为自包含的 Python 程序，按程序、执行结果与成本打分。它坚持在宣称端到端自动化之前先评估单个工作流任务，并报告了偏低的最佳 agent 求解率（独立 32.4%，含专家知识 34.3%）。
- **端到端研究生命周期。** [AIRS-Bench](../works/airs-bench.md) 提供 20 个 frontier 研究科学任务，不提供 baseline 代码，要求 agent 在语言建模、数学、生物信息学、时间序列预测中从零构造工作流。
- **跨尺度的真实研究场景。** [SciAgentArena](../works/sciagentarena.md) 在 agent-agnostic 环境中提供约 200 个来自真实世界科学研究场景、带逐步验证的任务，报告 agent 能处理结构化数据分析工作流，但在新颖洞见、自主探索与开放式问题上表现挣扎。
- **科学环境的 gymnasium。** [Aviary](../works/aviary.md) 提供一个可扩展的 language-agent 环境 gymnasium，其中三个为科学环境（分子克隆、科学文献研究、蛋白质工程）；其环境是可复用的评估面，尽管论文的头号贡献是训练框架而非评估贡献。
- **Cost-aware 科学仿真。** [SimulCost](../works/simulcost.md) 把 cost-aware 评估扩展到覆盖 13 个仿真器的物理仿真参数调优，显式建模仿真时间与实验资源成本。
- **医生共同验证的医疗评估。** [MedHELM](../works/medhelm.md) 把 Stanford CRFM 的 HELM 扩展到医疗任务：121 任务、由医生共同验证的分类体系；跨 35 benchmark 聚合；LLM-jury 方法与医生一致性（ICC = 0.47）被显式测量。
- **生成而非编写的 benchmark。** [HeurekaBench](../works/heurekabench.md) 贡献了一条半自动流水线，从已发表研究及其代码仓库中派生开放式研究问题，并将候选答案与这些研究已报告的发现比对验证。其单细胞实例含 50 道开放题与 50 道选择题，构建自 13 篇论文中的 41 条洞见；最强的现有 agent 在开放题正确性上为 5 分制的 2.34 分。
- **以模拟为根基的判分有效性。** [GeneBench-Pro](../works/genebench-pro.md) 把 129 个多阶段基因组学与定量生物学问题构建在人工模拟的数据生成过程而非真实数据集之上，从而使失败可归因于科学判断失误，而非归因于若干同样站得住脚的分析选择之一。每个问题内含 3 至 13 个相互依赖的决策点，仅以对决策相关数值的二元通过与否判分；所测得的最佳配置为 28.7%。
- **溯源审计下的已发表分析复现。** [Collider-Bench](../works/collider-bench.md) 要求 agent 仅凭公开论文与开源仿真软件复现 LHC 分析，用连续的直方图保真度对照隐藏参考产额为 10 个 CMS 搜索任务打分，并由 LLM judge 审计执行轨迹；在 364 次受评运行中 6% 的提交被标记为伪造，且平均而言没有 agent 能可靠胜过物理学家在环的解法。
- **反事实定律发现。** [NewtonBench](../works/newtonbench.md) 让 agent 对模拟物理系统运行实验，以复原 12 条经典物理定律的反事实偏移版本，用 LLM 判定的符号等价性为其 324 个任务打分。
- **计算材料科学中的主张级复现。** [AutoMat](../works/automat.md) 将 85 条由专家整理的计算材料科学论文主张打包为可运行的 HPC 任务，报告最佳 coding-agent 设定达到 54.1% 成功率，而当工作流必须仅凭论文正文复原时成功率接近零。
- **对接实时地理空间 API 的结构化工具调用。** [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) 针对一个开放、可自托管、服务于西班牙与葡萄牙三项指标的 API 运行 93 个环境分析任务，以机制性检查（不用 LLM judge）为每个案例打分，并把能力与单案例成本作为正交维度报告；最佳模型达到 60.8% ± 0.8%，而近似值比较类任务对每个模型都是 0%。
- **已发表 AI 实验的端到端复现。** [EXP-Bench](../works/exp-bench.md) 从 51 篇 NeurIPS 2024 与 ICLR 2024 论文中整理出 461 个任务，要求 agent 设计、实现、执行并得出完整实验结论；最佳 agent 配置仅能以可执行形式完成 0.5% 的实验。
- **全流程洞见再发现。** [FIRE-Bench](../works/fire-bench.md) 只给 agent 一个来自已发表机器学习研究的高层研究问题，并以对照该研究记录发现的主张级 F1 为其结论打分；最强的受评 agent Claude Code（Sonnet-4）在 30 任务核心集上达到 46.7。
- **隐藏论文再发现。** [ResearchClawBench](../works/researchclawbench.md) 将 40 个任务各自 grounding 在一篇真实已发表论文上，而该论文在评测期间保持隐藏，由 GPT-5.1 按 0–100 的 RADS 刻度、对照专家整理的加权评分标准为 agent 研究报告打分。
- **仿真驱动的模型拟合。** [Stargazer](../works/stargazer.md) 在带有逐准则物理一致性反馈的迭代式径向速度模型拟合上评估 agent；跨三个难度层级与 20 个真实档案系统，没有一个受评前沿 agent 能通过任何一个真实任务。
- **以论文复现为评估单元。** [PRBench](../works/prbench.md) 要求 agent 端到端复现已发表物理论文——30 个跨 11 个子领域的专家整理任务，其上最佳 agent OpenAI Codex（GPT-5.3-Codex）得分 34%，端到端回调成功率为零。
- **整体、成本受控的研究套件。** [AstaBench](../works/astabench.md) 聚合 11 个 benchmark、2,400+ 个问题，覆盖文献理解、代码与执行、数据分析、端到端发现，在标准工具下以时间不变的美元成本核算为 57 个 agent 打分。
- **以文献发现为评估目标。** [AutoResearchBench](../works/autoresearchbench.md) 用 1,000 条查询把自主研究中的文献查找环节单独拿出来评估，分两类任务——Deep Research（通过渐进式多步探查追踪一篇目标论文）与 Wide Research（全面收集满足给定条件的所有论文）——并报告最强模型分别仅达到 9.39% accuracy 与 9.31% IoU，尽管它们已基本攻克 BrowseComp 等通用 agentic browsing benchmark。
- **在真实仪器上物理执行。** [AFMBench](../works/afmbench.md) 要求 agent 在一台真正的原子力显微镜而非仿真器上完成 100 个经整理的任务，并报告材料科学问答能力并不迁移：Claude-3.5-Sonnet 的错误率达 51.6%，而最佳模型的总体任务完成率为 65%，在文档记录与分析合并时则跌至 23.3%。
- **单一仿真学科内的分层评估。** [CFDLLMBench](../works/cfdllmbench.md) 把领域固定在计算流体力学，转而改变能力的深度：90 道研究生水平题、24 个 PDE 求解器编程题、126 个 OpenFOAM 算例；物理准确性由相对参考解的归一化误差、以及解在网格与时间步细化下是否收敛来评判。分数从知识层的 92% 一路跌到求解器编程的约 14%，以及 OpenFOAM Basic / Advanced 两档的 34% / 25%。
- **仿真器反馈下的迭代式生成优化。** [Frontier-Eng](../works/frontier-eng.md) 把真实工程评估构造成 propose-execute-evaluate 循环：47 个任务横跨 5 个工程类别，工业级仿真器在硬性可行性约束下返回连续奖励，agent 在固定交互预算内修订。论文在 8 个 frontier LLM 上报告改进频率与改进幅度的双 power-law 衰减，并发现在受约束工程问题上深度比广度更重要。
- **机器判分的专家级理论。** [CMT-Benchmark](../works/cmt-benchmark.md) 收录 50 道由专家研究者按其自身研究水平编写的凝聚态理论问题——单题推导，而非交互式 agent 设定——对照专家提供的真值程序化判分，包括对非对易算符做正规排序后的符号比较。最佳模型 GPT-5 解出 30%；50 道题中有 18 道在全部 17 个受评模型上无一解出。
- **研究生水平推导的部分得分。** [CMPhysBench](../works/cmphysbench.md) 整理了 520 余道要求独立生成完整解答的研究生水平凝聚态物理计算题，用 SEED（Scalable Expression Edit Distance）——一种对解答表达式的细粒度、非二元部分得分——来评分；即便最佳模型 Grok-4 也仅达到平均 SEED 36 分与 28% 准确率。
- **容器化的分子动力学工作流。** [MDArena](../works/mdarena.md) 把源自在研项目的 50 个任务——轨迹分析、体系搭建、自由能计算与增强采样，覆盖 29 个分子体系与 14 种研究方案——打包进容器，以 Strict-Pass@1 为主指标并辅以过程级部分得分；最佳配置 Codex GPT-5.5（extra-high reasoning）解出 48%。
- **协议忠实的证据综合。** [MetaSyn](../works/metasyn.md) 把 422 个任务锚定到取自 34,000 余篇 Nature Portfolio 文章的专家 meta 分析：给定带结构化入选标准（PI/ECO）的研究问题，agent 要在掺入不合格干扰文献的共享 PubMed 文献库中找出原综述作者实际纳入的研究，分阶段评估则定位系统在综述流程中的薄弱环节。
- **物理科学的 deep research。** [PhySciBench](../works/physcibench.md) 整理了 200 道专家出题、物理与化学各半的问题，组织为呼应真实科研工作流的六类任务，针对现有 deep-research 系统的三类缺陷——推理链脆弱、跨步骤知识迁移有限、缺少基于物理的自我验证；Gemini Deep Research 基线的准确率为 33.5%。
- **按研究意图组织的文献搜索。** [ScholarQuest](../works/scholarquest.md) 按四类研究意图——方法导向、设定锚定、比较导向、范围受控——组织 agentic 论文搜索，覆盖 1,000 余个计算机科学主题；agentic 方法胜过单次检索基线，但最佳 agent 的 Recall@100 也仅有 0.314。
- **渐进式的信息获取分层。** [SciExplore](../works/sciexplore.md) 用四类渐进任务——科学数据库导航、表述模糊的文献检索、缺失参考文献补全、跨源结构化知识综合——评估科学信息获取能力：103 个专家整理的任务，覆盖十余个学科；任务复杂度一升高，表现便急剧下滑。
- **物理系统预测的真实世界数据。** [RealPDEBench](../works/realpdebench.md) 把五个真实测量数据集与同一批复杂物理系统的数值模拟配对，在三类任务与八项数据/物理导向指标下，把 sim-to-real 差距本身变成测量对象。其评估对象是科学 ML 代理模型而非 LLM agent——收录于此是因为其评估方法学；在十个基线上的实验显示模拟与真实数据差异显著，而用模拟数据预训练能稳定提升精度与收敛速度。
- **预算受限的引力发现。** [Gravity-Bench-v1](../works/gravity-bench.md) 让 agent 在实验预算内规划对模拟二体引力系统的观测，再分析数据以揭示被隐藏的——有时是分布外的——物理；据官方项目页，最佳模型从全量数据下的 74% 跌到预算下的 49%。
- **先验受控的物理发现。** [PhysGym](../works/physgym.md) 把 97 个交互式物理发现问题布置在四个受控的先验层级下，把「agent 发现了什么」与「agent 被告知了什么」分开；据官方仓库，先验逐级撤去时 o4-mini 从 62.89% 跌至 31%。
- **反事实世界的定律发现。** [DiscoverPhysics](../works/discoverphysics.md) 让 agent 在 22 个物理刻意偏离现实的模拟世界中做实验，并同时提交解释与定律的 Python 实现，以留出粒子上的轨迹 MSE 加按评分标准的 LLM 解释分评判；最强 agent 也只通过一半的世界。
- **操作专业 FEA 软件。** [FEABench](../works/feabench.md) 让 LLM agent 通过 API 驱动 COMSOL Multiphysics 端到端求解多物理场问题；最佳策略生成的 API 调用有 88% 可执行。
- **量子多体复现。** [QMP-Bench](../works/qmp-bench.md) 从 21 种高影响力期刊提取 100 个研究级端到端量子多体模拟任务，由编程验证器与科学验证器成对验证。
- **以精度为参照的引力波任务。** [gwBenchmarks](../works/gwbenchmarks.md) 在八个底层数据超过 10⁸ 核时的引力波任务上压力测试 12 个 coding agent，并因 agent 会伪造或只做部分评估而改用外部框架计分；较难任务上所有 agent 距 ≲10⁻⁴ 的领域要求差 1–2 个数量级。
- **原作者共同开发的论文复现。** [ReplicationBench](../works/replicationbench.md) 把天体物理论文拆成 111 个与原作者共同开发的复现任务（官方仓库），把对方法的忠实与结果的正确分开打分；最好的模型得分也不足 20%。
- **紧随期刊的研究任务。** [PRL-Bench](../works/prl-bench.md) 从 2025 年 8 月后的 Physical Review Letters 论文中派生 100 个经专家验证的长 horizon 研究任务，覆盖五个子领域，以新近性防污染；六个前沿 LLM 中最高总分不到 50（满分 100）。
- **轨迹对齐的仪器控制。** [EnvTrace](../works/envtrace.md) 让 LLM 生成的同步辐射光束线控制代码在数字孪生上执行、再对齐执行轨迹来评估——对于「意义即物理行为」的代码，这是语义层面的正确性检验；30 余个 LLM 受评。
- **Agent benchmark 能泛化多远？** [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md) 在 53 个显微术 benchmark 测试与 105 种 agent 配置上共运行 1,949 次，发现用这些结果训练的代理模型无法可靠预测未见任务上的表现。
- **未发表的研究级挑战。** [CritPt](../works/critpt.md) 由 50 余位物理学家在 11 个以上子领域创作 71 个未发表、防猜测的研究挑战（分解为 190 个检查点任务），由针对物理定制的流水线自动判分；最佳基础模型 5.7%，配编码工具约 10%。
- **全新理论问题。** [TPBench](../works/tpbench.md) 给出 57 道全新、可自动验证的理论物理问题，从本科到研究级，覆盖高能理论与宇宙学；研究级问题大多未被受评模型解出。
- **科学家整理的科研代码。** [SciCode](../works/scicode.md) 把 80 个真实科研编码问题分解为 338 个子问题，横跨 16 个自然科学子领域；受评模型中最好的在最接近真实的设定下只解出 4.6% 的主问题。
- **内核校验的形式化物理。** [Lean4Physics](../works/lean4physics.md) 贡献 LeanPhysBench——200 条经同行评审的 Lean4 物理命题——外加 PhysLib 基础库；最佳成绩为专业证明器 16%、Claude Sonnet 4 35%，PhysLib 平均带来 +11.75%。
- **防记忆的方程发现。** [LLM-SRBench](../works/llm-srbench.md) 构建 239 个方程发现问题：或把已知物理模型变换到陌生表征，或直接合成发现型问题；最好的系统符号准确率仅 31.5%。
- **本科广度的解题评估。** [UGPhysics](../works/ugphysics.md) 覆盖 5,520 道经泄漏筛查的双语问题、13 个科目，由 MARJ 流水线判分；31 个 LLM 中最高 49.8%。
- **原创题加连续指标。** [PHYBench](../works/phybench.md) 原创 500 道从高中到奥赛的问题，用表达式编辑距离为符号答案评分；Gemini 2.5 Pro 为 36.9%，人类专家为 61.9%。
- **视觉不可或缺的物理。** [SeePhys](../works/seephys.md) 让 75% 的题目不看图无法作答，横跨 21 类图示、从初中到博士；顶级视觉推理模型准确率不足 60%。
- **官方奥赛评分。** [HiPhO](../works/hipho.md) 用官方评分方案与奖牌线在 13 套最新高中物理奥赛真题上评判 30 个 (M)LLM；闭源推理 MLLM 获 6–12 金，但大多数模型距满分仍远。
- **前沿学术参照点。** [Humanity's Last Exam](../works/hle.md) 由全球领域专家在数十个学科上出 2,500 道位于人类知识前沿的题目——抗检索、可自动判分、并测量校准度。它是通用学术 benchmark 而非 agent benchmark，是研究级科学 benchmark 用来定位自身难度的天花板。
- **大学课程广度的解题评估。** [PHYSICS](../works/physics-benchmark.md) 整理 1,297 道专家标注的大学水平问题，覆盖物理六大核心领域，配稳健的自动评估系统；受评中最先进的 o3-mini 也只有 59.9%。
- **按评分标准分解的 AI 论文复现。** [PaperBench](../works/paperbench.md) 让 agent 从零复现 20 篇 ICML 2024 Spotlight 与 Oral 论文，由 LLM judge 对照与作者共同开发的层级式评分标准（共 8,316 个判分节点）打分——judge 本身也被单独评测；最佳 agent 得 21.0%，ML 博士仍然领先。
- **基于自带代码与数据的可复现性。** [CORE-Bench](../works/core-bench.md) 把计算可复现性单独隔离出来——用 90 篇论文自己的代码与数据重跑其结果，跨三个学科、270 个任务；最好的基线 agent 在最难档上仅 21%。
- **专家锚定的基因组学流水线。** [GenoTEX](../works/genotex.md) 在基因-性状关联分析上评估 agent——数据集选择、预处理、统计——对照生物信息学家整理的参考流水线（据官方仓库为 911 个数据集上的 1,384 个问题）。
- **真实 notebook 的生物信息学场景。** [BixBench](../works/bixbench.md) 把 50 余个已发表分析改成开放式探索 agent 任务并容器化执行；前沿模型开放式作答仅 17%，选择题不比随机好。
- **带扰动鲁棒性的流水线评估。** [BioAgent Bench](../works/bioagent-bench.md) 基于输出产物为端到端生物信息学流水线（RNA-seq、变异检测、宏基因组）判分，并用损坏输入、诱饵文件与提示膨胀施压；流水线搭对不保证步骤级推理可靠。
- **规模化的沙箱生物医学编码。** [MedAgentGym](../works/medagentgym.md) 在可执行沙箱中运行 72,413 个可验证编码任务实例（129 类、12 个真实生物医学场景），评测 29 个 LLM（并兼作 RL 训练环境）。
- **确定性判分的单细胞分析。** [scBench](../works/scbench.md) 把六个平台上真实 scRNA-seq 数据的步骤前快照交给 agent，以确定性判分检验其是否复原出关键生物学结果；准确率 29–53%，平台选择与模型选择同等重要。
- **长 horizon 的单细胞发现。** [scBench-Long](../works/scbench-long.md) 要求 agent 在不预设方法的前提下从近原始数据复原已发表结论，以受控答案词表判分；最强模型-harness 组合通过率 25.4%。
- **把 harness 当变量的空间生物学。** [SpatialBench](../works/spatialbench.md) 把同一确定性快照设计用于五种空间技术（基础模型 20–38%），并主张 harness 设计应作为一等对象评估。
- **配人类基线的 AI-scientist 任务。** [BAISBench](../works/baisbench.md) 在 15 个专家标注数据集上为细胞类型注释评分，并在派生自 41 项已发表研究的 193 道发现类选择题上评分，与六位研究生水平生物信息学家对照。
- **Agent 作为生物医学 ML 工程师。** [BioXArena](../works/bioxarena.md) 在标准化 2 小时/单 GPU 预算与隐藏标签下运行 9 个生物医学领域的 76 个端到端 ML 任务；11 种配置中最佳平均 0.666，无一全面占优。
- **语料规模的协议推理。** [BioProBench](../works/bioprobench.md) 把 22,413 份湿实验协议扩展为 523,784 个实例、五类任务；凡需深度推理、定量精确或安全意识处，模型表现骤降。
- **系统生物学干实验。** [SciGym](../works/scigym.md) 让 agent 在隐藏的 SBML 系统上迭代设计实验并提交机制假设；表现随系统复杂度显著下降。
- **面向研究实践的生物学问答。** [LAB-Bench](../works/lab-bench.md) 用 2,400 余道题测生物学研究的日常动作——文献、图表、数据库、协议、序列、克隆——配人类专家基线。
- **真实化加固的后继。** [LABBench2](../works/labbench2.md) 让同样的能力面对真实 PDF、图片与数据文件；恢复真实情境让模型付出 26–46 个百分点。
- **预算受限的分子设计。** [SMDD-Bench](../works/smdd-bench.md) 在有限 oracle 调用预算下布置 502 个保证有解的多轮药物设计任务（102 个蛋白靶点）；GPT-5.4 仅解出 40.2%。
- **知识图谱审计。** [BioKGBench](../works/biokgbench.md) 把主张验证与 KGQA 组合成 agentic 的 KGCheck 任务——深入盘查生物医学知识图谱找出事实错误——并在生产级数据库中揪出 90 余处真实错误。
- **实时来源的医学 deep research。** [MedBrowseComp](../works/medbrowsecomp.md) 在 1,000 余道医生整理的问题上要求跨实时试验注册库、监管记录、专利与费用数据做多跳综合。
- **序贯临床接诊。** [AgentClinic](../works/agentclinic.md) 把医学问答改成有主持的医患交互，带工具并对多种认知与隐性偏倚建模；准确率跌到静态问答的十分之一以下。
- **FHIR 虚拟 EHR。** [MedAgentBench](../works/medagentbench.md) 在 100 位真实感患者档案上、通过生产级医疗 API 运行 300 个医生撰写的任务；最佳模型 69.67%。
- **计费的序贯诊断。** [SDBench](../works/sdbench.md) 把 304 个 NEJM-CPC 病例改成守门人中介的接诊，按准确率-成本前沿评分，配 21 位医生、平均 20% 准确率的基线。
- **预测实验结果。** [BrainBench](../works/brainbench.md) 用困惑度检验模型能否分辨真实与改动结果的神经科学摘要；LLM 超过人类专家且信心有校准——静态 benchmark，因其预报式评估方法学收录。
- **把求解器当作生成物。** [CodePDE](../works/codepde.md) 把 PDE 求解构造成 LLM 代码生成，在代表性 PDE 问题上评估推理、调试、自我改进与测试时扩展——「LLM 写求解器」范式的奠基性评估。
- **分级把关的求解器生成。** [PDEAgent-Bench](../works/pdeagent-bench.md) 布置 645 个「PDE 到求解器」实例（11 个 PDE 族、三个 FEM 库），依次检查可执行性 → 精度 → 效率；一旦强制精度与效率，通过率大幅下滑。
- **能跑但物理错了。** [MooseBench](../works/moosebench.md) 提供 220 个带 PDE 级真值的多物理场算例；其 Intent Fidelity Score 重构所编码的 PDE，显示只修执行错误时 39–40% 的算例保持「能跑但错」。
- **从对话生成数字孪生。** [SimBench](../works/simbench.md) 在 Chrono 多物理场仿真器的多轮数字孪生生成上比较 33 个以上面向仿真的 LLM，由带规则与人在环指导的 LLM judge 打分。
- **在科学代码库上评测 coding agent。** [AInsteinBench](../works/ainsteinbench.md) 从六个生产级科学代码库（量子化学到数值相对论与流体力学）的维护者 PR 派生任务，在可执行环境中做测试驱动验证。
- **「工件像样」不等于「端到端做对」。** [StructureClaw](../works/structureclaw.md) 在 150 个结构工程场景上对照冻结的参考求解器响应；通用执行有 87.0% 通过模型工件检查，端到端成功率却只有 22.0%。
- **对齐课程难度的 FEM 编码。** [FEM-Bench](../works/fem-bench.md) 在 33 个研究生课程级计算力学任务上验证函数与单元测试编写，各尝试五次；最佳模型 26/33 个任务五次全成。
- **先澄清，再计算。** [SciConvBench](../works/sciconvbench.md) 为不适定仿真请求的多轮消歧与矛盾消解打分，覆盖流体力学、固体力学、材料科学与 PDE；最佳模型在流体力学消歧上仅解决 52.7%。
- **从意图到 PDE 控制。** [PDE-Controller](../works/pde-controller.md) 评估热/波动方程系统控制的自动形式化（自然语言到信号时序逻辑）、推理与程序合成，配人工案例加 200 万合成样本。
- **把近似当作受测技能。** [HARDMath](../works/hardmath.md) 自动生成经数值真值验证的研究生渐近分析问题；GPT-4 少样本思维链下仅 43.8%。
- **被重算的电网研究。** [PowerAgentBench-SS](../works/poweragentbench-ss.md) 让 agent 做电力系统故障研究，报告由隐藏评估器重新推导，false-safe 罚分与 severity regret 让没有依据的「一切正常」付出代价。
- **率定业务化预报模型。** [HydroAgent](../works/hydroagent.md) 以 Nash–Sutcliffe 效率评测九个前沿 agent 对 NWS 业务化 CREST 水文模型的率定；仅一个模型在一个测站达到人类专家参照。

## Comparison

| Benchmark | Year | 任务来源 | 科学范围 | 验证方式 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 领域专家编写 | Life / Physical / Earth / Math / Engineering Sciences | 容器内 pytest 确定性验证 | [→](../works/terminal-bench-science.md) |
| NatureBench | 2026 | 从 Nature-family 论文蒸馏 | 跨学科（Nature 编辑范围） | 与已发表 SOTA 比较 | [→](../works/naturebench.md) |
| ScienceAgentBench | 2024 | 从 44 篇同行评审论文提取（专家验证） | 数据驱动发现（四个学科） | 执行统一的 Python 程序；程序 / 结果 / 成本指标 | [→](../works/scienceagentbench.md) |
| AIRS-Bench | 2026 | Frontier 研究科学任务 | LM / 数学 / 生物信息学 / 时间序列 | 端到端研究生命周期评分 | [→](../works/airs-bench.md) |
| SciAgentArena | 2026 | 约 200 个真实研究场景任务 | 生物医学：5 个领域（分子 → 群体） | 按领域的逐步验证（执行 + 专家标准） | [→](../works/sciagentarena.md) |
| Aviary | 2024 | 五环境 gymnasium（3 个科学） | 分子生物学（克隆 / 蛋白质）+ 文献 | POMDP 环境中的各环境任务成功率 | [→](../works/aviary.md) |
| SimulCost | 2026 | 覆盖 13 个仿真器的参数调优 | 物理仿真 | 预算下成功率；与传统方法对比 | [→](../works/simulcost.md) |
| MedHELM | 2025 | 医生共同设计的分类（29 位医生） | 医疗 / 临床 | LLM-jury（与医生 ICC = 0.47）；跨 35 benchmark 聚合 | [→](../works/medhelm.md) |
| HeurekaBench | 2026 | 基于已发表研究及其代码仓库的半自动流水线 | 单细胞生物学（流水线被主张为领域无关） | G-Eval LLM judge（GPT-4o，1–5 分）对照已发表发现 | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | 人工模拟的数据生成过程 | 基因组学 / 定量生物学 / 转化医学 | 在校准容差下与可复原目标作二元匹配 | [→](../works/genebench-pro.md) |
| Collider-Bench | 2026 | 源自四项已发表 CMS 超对称搜索（先由专家解出） | 实验粒子物理（LHC recasting） | 对照隐藏参考产额的相对 L²（τ = 0.33 通过阈值）；LLM 溯源 judge | [→](../works/collider-bench.md) |
| NewtonBench | 2025 | 12 条经典物理定律的 108 个反事实偏移，各置于 3 种模拟系统 | 物理中的交互式科学定律发现 | LLM 判定的符号等价加 RMSLE 数据保真度 | [→](../works/newtonbench.md) |
| AutoMat | 2026 | 由材料科学专家从近期论文整理的 85 条主张 | 计算材料科学（统计/ML、DFT、MD、DDD） | artifact-grounded LLM 评估 agent 对照隐藏专家复现步骤打 1–5 分；成功为至少 4 分 | [→](../works/automat.md) |
| GeoNatureAgent Benchmark | 2026 | 针对可自托管地理空间 API、以领域专家 ground truth 指定的任务 | 环境地理空间分析（西班牙 / 葡萄牙） | 自动化工具调用 / 关键词 / 数值容差检查；无 LLM-as-judge | [→](../works/geonatureagent-benchmark.md) |
| EXP-Bench | 2025 | 从 51 篇 NeurIPS 2024 / ICLR 2024 论文及其代码提取的 461 个任务 | 端到端 AI 研究实验：设计、实现、执行、结论 | 对设计 / 实现 / 结论的 LLM-judge 评分加容器化执行验证 | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | 30 篇 ICLR、ICML、NeurIPS 2024–2025 实证 LLM 分析论文各一任务，加 10 任务跨域扩展 | 全流程：从高层研究问题到规划 → 编码 → 执行 → 结论 | 固定 gpt-5.2 蕴含 judge 对照真值发现的主张级 precision、recall、F1 | [→](../works/fire-bench.md) |
| ResearchClawBench | 2026 | 从真实已发表论文专家整理的 40 个任务，目标论文隐藏 | 10 个领域：天文、化学、地球、能源、信息、生命、材料、数学、神经科学、物理 | GPT-5.1 对照加权多模态评分标准为报告打分（RADS，0–100） | [→](../works/researchclawbench.md) |
| Stargazer | 2026 | 100 个种子模拟器任务 + 20 个匿名化档案系统（NASA 系外行星档案、VizieR） | 天体物理：径向速度时间序列上的系外行星模型拟合 | 四项联合通过/失败准则（残差 RMS、ΔBIC、参数匹配、行星数） | [→](../works/stargazer.md) |
| PRBench | 2026 | 由北京大学 20 多个课题组整理并复现的已发表物理论文 | 30 个任务，跨 11 个物理子领域 | 加权四维评分标准，由 green agent 对照专家 ground truth 打分；端到端回调率 | [→](../works/prbench.md) |
| AstaBench | 2025 | 作者自建 + 改编数据集，多来自 Asta 用户请求 | 全流程：文献、代码、数据分析、端到端发现（CS 加权） | LLM-judge 评分标准 + 程序化打分，带成本核算 | [→](../works/astabench.md) |
| AFMBench | 2025 | 100 个专家整理的任务，沿工具数、agent 数、复杂度与功能领域分层 | 材料的扫描探针显微术 | 在 Nanosurf DriveAFM 上物理执行；按领域的完成率加一套命名的错误分类 | [→](../works/afmbench.md) |
| AutoResearchBench | 2026 | 1,000 条查询，由基于论文全文与引用图的 full-text-first 人机协同流水线构建 | 科学文献发现（八个核心 CS 领域） | 对照已验证答案集的精确匹配 accuracy（Deep Research）与集合级 IoU（Wide Research） | [→](../works/autoresearchbench.md) |
| Frontier-Eng | 2026 | 47 个真实工程任务，横跨 5 个工程类别 | 真实工程（工业级仿真器） | 硬性可行性约束下的连续仿真器奖励；固定交互预算 | [→](../works/frontier-eng.md) |
| CFDLLMBench | 2025 | 90 道专家撰写的题目、24 个 PDE 编程题、126 个 OpenFOAM 算例（110 个由 tutorial 派生 + 16 个手工设计） | 计算流体力学 | 执行 + 相对参考解的归一化误差 + 网格/时间步细化下的收敛性 | [→](../works/cfdllmbench.md) |
| CMT-Benchmark | 2025 | 由专家研究者按其自身工作水平编写的 50 道问题 | 凝聚态理论：量子多体与经典统计力学 | 对照专家真值的程序化检验；非对易算符经正规排序做符号比较 | [→](../works/cmt-benchmark.md) |
| CMPhysBench | 2025 | 520 余道精心整理的研究生水平计算题 | 凝聚态物理：磁学、超导、强关联体系 | SEED 表达式编辑距离（部分得分）加二元准确率 | [→](../works/cmphysbench.md) |
| MDArena | 2026 | 源自在研项目的 50 个容器化任务 | 分子动力学：29 个分子体系、14 种研究方案 | Strict-Pass@1，辅以 correctness 与过程奖励的部分得分 | [→](../works/mdarena.md) |
| MetaSyn | 2026 | 取自 34,000+ 篇 Nature Portfolio 文章的 422 个专家 meta 分析 | 系统综述，主题横跨物理、化学、心理学与医学 | 对照原综述作者纳入集的研究识别；分阶段流程评估 | [→](../works/metasyn.md) |
| PhySciBench | 2026 | 200 道专家整理的 deep-research 问题 | 物理科学：物理与化学，六类任务 | 基于准确率比较模型与 agent 系统 | [→](../works/physcibench.md) |
| ScholarQuest | 2026 | 由 1,000+ 个计算机科学主题按四种研究意图构造的查询 | 计算机科学文献搜索 | 对照真值论文集的 Recall@100 与 Recall@All | [→](../works/scholarquest.md) |
| SciExplore | 2026 | 103 个专家整理的任务，分四类渐进任务 | 覆盖 10+ 学科的科学信息获取 | 从数据库导航到结构化综合的分层准确率 | [→](../works/sciexplore.md) |
| RealPDEBench | 2026 | 5 个真实测量数据集，配成对数值模拟 | 复杂物理系统（流固耦合、圆柱/翼型绕流、燃烧）；科学 ML 模型而非 LLM agent | 3 类真实-模拟对比任务上的 8 项数据/物理导向指标；10 个基线 | [→](../works/realpdebench.md) |
| Gravity-Bench-v1 | 2025 | 含分布外物理的模拟二体系统 | 观测预算下的引力物理发现 | 对照严格动力学模拟的参考解，与人类专家对标 | [→](../works/gravity-bench.md) |
| PhysGym | 2025 | 取自 PHYBench 的 97 个问题，以交互模拟运行 | 四个受控先验层级下的物理发现 | 假设准确性与模型保真度的标准化协议 | [→](../works/physgym.md) |
| DiscoverPhysics | 2026 | 按需生成的 22 个反事实 N 体世界 | 刻意非标准物理中的运动定律 | 留出粒子上的轨迹 MSE + 按评分标准的 LLM 解释分 | [→](../works/discoverphysics.md) |
| FEABench | 2025 | 经 COMSOL Multiphysics API 求解的多物理场问题 | 有限元多物理场仿真 | 对生成 API 调用与计算答案的评估；可执行率指标 | [→](../works/feabench.md) |
| QMP-Bench | 2026 | 提取自 21 种高影响力期刊的 100 个任务 | 量子多体模拟 | 编程验证器加基于物理原理的科学验证器 | [→](../works/qmp-bench.md) |
| gwBenchmarks | 2026 | 8 个任务，底层数据代表 10⁸+ 核时计算 | ≲10⁻⁴ 相对误差要求下的引力波天文学 | 外部预定义评估框架，配单任务物理指标 | [→](../works/gwbenchmarks.md) |
| ReplicationBench | 2025 | 与原作者共同开发的 20 篇论文 111 个任务 | 天体物理论文复现 | 逐任务客观评分：忠实性与正确性 | [→](../works/replicationbench.md) |
| PRL-Bench | 2026 | 100 篇 2025 年 8 月后的 PRL 论文，专家验证 | 五个子领域的前沿物理研究 | 客观可验证的结果；0–100 制评分 | [→](../works/prl-bench.md) |
| EnvTrace | 2025 | 同步辐射装置的光束线控制代码生成 | 实验物理的仪器控制 | 对照数字孪生的执行轨迹对齐 | [→](../works/envtrace.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | 53 个显微术测试 × 105 种 agent 配置 | 自主显微术 / 材料表征 | 带轨迹日志的 benchmark 测试；时延、成本与失败模式比较 | [→](../works/agentic-microscopy-benchmarks.md) |
| CritPt | 2025 | 50 余位物理学家的 71 个未发表挑战 + 190 个检查点 | 11+ 子领域的研究入门级物理 | 防猜测、可机器验证的答案；定制自动判分 | [→](../works/critpt.md) |
| TPBench | 2025 | 57 道全新问题，从本科到研究级 | 理论物理：高能理论与宇宙学 | 可自动验证的答案与定制判分 | [→](../works/tpbench.md) |
| SciCode | 2024 | 科学家整理的 80 个主问题 / 338 个子问题 | 16 个自然科学子领域（数学、物理、化学、生物、材料） | 对照科学家标注的金标准解与测试执行 | [→](../works/scicode.md) |
| Lean4Physics | 2025 | 200 条经同行评审的 Lean4 命题，取材教材与竞赛 | 作为形式化定理证明的大学物理 | Lean4 内核证明检查；无 judge 介入 | [→](../works/lean4physics.md) |
| LLM-SRBench | 2025 | 239 个问题，分 LSR-Transform 与 LSR-Synth 两类 | 横跨四个领域的科学方程发现 | 对照真值方程的符号准确率 | [→](../works/llm-srbench.md) |
| UGPhysics | 2025 | 5,520 道经泄漏筛查的双语本科问题 | 13 个科目的本科物理 | MARJ 模型辅助规则判分 | [→](../works/ugphysics.md) |
| PHYBench | 2025 | 500 道原创问题，从高中到奥赛 | 以符号答案作答的物理解题 | 表达式编辑距离（EED）加准确率；人类专家基线 | [→](../works/phybench.md) |
| SeePhys | 2025 | 2,000 道经校验的问题（官方页），从初中到博士 | 视觉不可或缺的物理：7 个领域、21 类图示 | 多模态解题准确率 | [→](../works/seephys.md) |
| HiPhO | 2025 | 13 套最新（2024–25）国际与地区奥赛真题 | 混合模态的高中奥赛物理 | 官方评分方案的答案级与步骤级判分；奖牌线 | [→](../works/hipho.md) |
| Humanity's Last Exam | 2025 | 全球领域专家出的 2,500 道题 | 数十个学科的前沿学术知识；非 agent 专属 | 对无歧义答案自动判分；准确率与校准度 | [→](../works/hle.md) |
| PHYSICS | 2025 | 1,297 道专家标注的大学水平问题 | 大学物理：六大核心领域 | 稳健的自动评估系统 | [→](../works/physics-benchmark.md) |
| PaperBench | 2025 | 20 篇 ICML 2024 Spotlight/Oral 论文，与作者共同开发评分标准 | AI 研究复现；8,316 个可判分节点 | LLM judge 对照层级式评分标准打分，judge 本身被单独评测 | [→](../works/paperbench.md) |
| CORE-Bench | 2024 | 90 篇论文自带代码与数据的 270 个任务 | 计算可复现性：计算机科学、社会科学、医学 | 重现结果的准确率（可并行评估系统校验） | [→](../works/core-bench.md) |
| GenoTEX | 2024 | 专家整理的基因-性状关联流水线（据官方仓库 1,384 个问题 / 911 个数据集） | 计算基因组学与生物信息学 | 对照生物信息学家整理的参考分析 | [→](../works/genotex.md) |
| BixBench | 2025 | 来自已发表分析的 50+ 场景、约 300 个开放式问题 | 计算生物学数据分析 | LLM 判分的开放作答 + 精确匹配选择题，容器化执行 | [→](../works/bixbench.md) |
| BioAgent Bench | 2026 | 人工整理的端到端流水线（RNA-seq、变异检测、宏基因组） | 生物信息学工作流 | LLM 判分器基于输出产物；扰动鲁棒性套件 | [→](../works/bioagent-bench.md) |
| MedAgentGym | 2025 | 12 个真实生物医学场景的 72,413 个实例 / 129 类 | 生物医学数据科学编码 | 可执行沙箱中的可验证真值 | [→](../works/medagentgym.md) |
| scBench | 2026 | 394 个可验证问题，六平台、七类 | 单细胞 RNA-seq 分析 | 生物学结果复原的确定性判分 | [→](../works/scbench.md) |
| scBench-Long | 2026 | 从原始或近原始数据出发的 21 项评估，方法不作规定 | 长 horizon 单细胞生物学 | 受控答案词表；确定性判分加轨迹评分标准 | [→](../works/scbench-long.md) |
| SpatialBench | 2025 | 146 个可验证问题，五种空间技术 | 空间转录组分析 | 生物学结果复原的确定性判分 | [→](../works/spatialbench.md) |
| BAISBench | 2025 | 15 个专家标注数据集 + 派生自 41 项研究的 193 道选择题 | 单细胞组学发现 | 层级化细胞类型树的注释评分 + 对照已发表结论的选择题 | [→](../works/baisbench.md) |
| BioXArena | 2026 | 9 个生物医学领域的 76 个端到端 ML 任务 | 多模态生物医学机器学习 | 隐藏标签、留出判分器、0–1 生物学感知指标；2 小时/单 GPU 预算 | [→](../works/bioxarena.md) |
| BioProBench | 2025 | 22,413 份人工撰写协议的 523,784 个实例 | 湿实验协议的理解与推理 | 按任务的指标，含步骤召回/精确率与 Kendall's tau | [→](../works/bioprobench.md) |
| SciGym | 2025 | 137 个受评（共发布 350 个）隐藏 SBML 系统 | 系统生物学实验设计 | 复原模型对照隐藏真值系统 | [→](../works/scigym.md) |
| LAB-Bench | 2024 | 8 类 2,400+ 道选择题，含 ProtocolQA 与 CloningScenarios | 生物学研究实践 | 对照人类专家基线的选择题评分 | [→](../works/lab-bench.md) |
| LABBench2 | 2026 | 约 1,900 个任务，基于真实 PDF、图片与数据文件 | 加固后的生物学研究实践 | 经发布的评估 harness 计算的准确率；较 LAB-Bench 为 −26% 至 −46% | [→](../works/labbench2.md) |
| SMDD-Bench | 2026 | 102 个蛋白靶点上 502 个保证有解的任务 | 小分子药物设计 | 有限 oracle 调用预算下的解出率 | [→](../works/smdd-bench.md) |
| BioKGBench | 2024 | 2,000+ 原子实例 + 225 个标注 KGCheck 实例 | 生物医学知识图谱 | 主张验证、KGQA 与 agentic 错误定位 | [→](../works/biokgbench.md) |
| MedBrowseComp | 2025 | 1,000+ 道医生整理的多跳问题 | 实时医学知识库 | 实时检索下对照标准答案检验 | [→](../works/medbrowsecomp.md) |
| AgentClinic | 2024 | 模拟接诊，九个专科、七种语言 | 作为序贯决策的临床诊断 | 有主持的多 agent 对话下的诊断准确率，含偏差扰动 | [→](../works/agentclinic.md) |
| MedAgentBench | 2025 | 100 位患者档案上 300 个医生撰写的任务 | FHIR 虚拟 EHR 操作 | 对照参考解的程序化成功率检验 | [→](../works/medagentbench.md) |
| SDBench | 2025 | 304 个 NEJM-CPC 病例的守门人中介接诊 | 带成本的序贯临床诊断 | 诊断准确率与就诊、检查费用成对报告 | [→](../works/sdbench.md) |
| BrainBench | 2024 | 200 对原始/改动的神经科学摘要（官方数据集） | 神经科学结果预测 | 二选一强制选择；LLM 用困惑度，人类专家附信心评级 | [→](../works/brainbench.md) |
| CodePDE | 2025 | 以求解器生成任务呈现的代表性 PDE 问题 | LLM 编写的数值 PDE 求解器 | 生成求解器对照参考解的精度；推理/调试/改进/扩展评估轴 | [→](../works/codepde.md) |
| PDEAgent-Bench | 2026 | 645 个实例，6 个数学类别、11 个 PDE 族、3 个 FEM 库 | 有限元求解器生成 | 分级检查：可执行性 → 数值精度 → 效率，按算例设定目标 | [→](../works/pdeagent-bench.md) |
| MooseBench | 2026 | 220 个带 PDE 级真值的 MOOSE 多物理场算例 | 多物理场模拟代码生成 | 经确定性 PDE 重构的 Intent Fidelity Score | [→](../works/moosebench.md) |
| SimBench | 2024 | 34 个物理系统上 102 个演示任务（官方仓库） | Chrono 仿真器的数字孪生生成 | 带预定义规则与人在环指导的 LLM judge 评分 | [→](../works/simbench.md) |
| AInsteinBench | 2025 | 6 个生产级科学仓库的维护者 PR 任务 | 科学软件工程（量子化学到流体力学） | 可执行环境中的测试驱动验证 | [→](../works/ainsteinbench.md) |
| StructureClaw | 2026 | 150 个受控场景：标准、交互、多模态重构 | 结构工程工作流 | 严格模型匹配 + 与冻结参考求解器响应的数值一致（E2E Success） | [→](../works/structureclaw.md) |
| FEM-Bench | 2025 | 33 个研究生课程任务，函数与单元测试两赛道，各五次尝试 | 计算力学代码生成 | 客观验证；Average Joint Success Rate | [→](../works/fem-bench.md) |
| SciConvBench | 2026 | 四个计算科学领域的不适定仿真请求 | 任务表述的多轮澄清 | 评分标准框架：澄清行为、对话共识建立、最终规格保真度 | [→](../works/sciconvbench.md) |
| PDE-Controller | 2025 | 人工案例 + 200 万合成样本（热/波动方程控制） | 经 STL 自动形式化的 PDE 控制 | 推理、自动形式化与程序合成指标；效用增益 | [→](../works/pde-controller.md) |
| HARDMath | 2024 | 自动生成的渐近分析问题；366 题 mini 测试集 | 研究生应用数学（近似技术） | 对照经数值验证真值的准确率 | [→](../works/hardmath.md) |
| PowerAgentBench-SS | 2026 | IEEE 39 节点系统变体；基于直流潮流的 N-2 热稳定越限搜索试点 | 电力系统稳态 agent 研究 | 隐藏评估器重算物理有效性；多种 recall、false-safe 罚分、severity regret | [→](../works/poweragentbench-ss.md) |
| HydroAgent | 2026 | 在 4 个留出测站上率定业务化 CREST 模型 | agent 的水文模型率定 | 对照人类专家参照的 Nash–Sutcliffe 效率 | [→](../works/hydroagent.md) |

## Open Questions

- **正确性的参照标准。** 科学任务允许多种合理的参照标准——已发表 SOTA（NatureBench）、专家分类（MedHELM）、可执行验证（Terminal-Bench Science）、与传统方法对比（SimulCost）。跨 benchmark 比较时，哪一种应成为标准？
- **发现 vs. 复现。** NatureBench 明确区分「匹敌 SOTA」与「真正的方法论创新」。评分指标该如何操作化「发现」？
- **成本作为评估维度。** 科学工作流有真实 tool-use 成本（仿真时间、实验资源）。scientific-agent topic 是否应像 SimulCost 那样把成本作为强制维度？
- **广度 vs. 深度。** 跨学科 benchmark（NatureBench、AIRS-Bench、MedHELM）给出广度；单仿真器 / 单领域 benchmark 给出深度。哪一种更适合作为主要评估面？
- **Judge 可靠性。** MedHELM 报告的 LLM-jury 与医生一致性为 ICC = 0.47。这是否是其他使用 LLM-judge 评分的科学领域 benchmark 应报告的下限？多少才算充分？

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [NatureBench](../works/naturebench.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SciAgentArena](../works/sciagentarena.md)
- [Aviary](../works/aviary.md)
- [AIRS-Bench](../works/airs-bench.md)
- [SimulCost](../works/simulcost.md)
- [MedHELM](../works/medhelm.md)
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [Collider-Bench](../works/collider-bench.md)
- [NewtonBench](../works/newtonbench.md)
- [AutoMat](../works/automat.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Stargazer](../works/stargazer.md)
- [PRBench](../works/prbench.md)
- [AstaBench](../works/astabench.md)
- [AFMBench](../works/afmbench.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CMPhysBench](../works/cmphysbench.md)
- [MDArena](../works/mdarena.md)
- [MetaSyn](../works/metasyn.md)
- [PhySciBench](../works/physcibench.md)
- [ScholarQuest](../works/scholarquest.md)
- [SciExplore](../works/sciexplore.md)
- [RealPDEBench](../works/realpdebench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [PhysGym](../works/physgym.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FEABench](../works/feabench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [ReplicationBench](../works/replicationbench.md)
- [PRL-Bench](../works/prl-bench.md)
- [EnvTrace](../works/envtrace.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [CritPt](../works/critpt.md)
- [TPBench](../works/tpbench.md)
- [SciCode](../works/scicode.md)
- [Lean4Physics](../works/lean4physics.md)
- [LLM-SRBench](../works/llm-srbench.md)
- [UGPhysics](../works/ugphysics.md)
- [PHYBench](../works/phybench.md)
- [SeePhys](../works/seephys.md)
- [HiPhO](../works/hipho.md)
- [Humanity's Last Exam](../works/hle.md)
- [PHYSICS](../works/physics-benchmark.md)
- [PaperBench](../works/paperbench.md)
- [CORE-Bench](../works/core-bench.md)
- [GenoTEX](../works/genotex.md)
- [BixBench](../works/bixbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SpatialBench](../works/spatialbench.md)
- [BAISBench](../works/baisbench.md)
- [BioXArena](../works/bioxarena.md)
- [BioProBench](../works/bioprobench.md)
- [SciGym](../works/scigym.md)
- [LAB-Bench](../works/lab-bench.md)
- [LABBench2](../works/labbench2.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [BioKGBench](../works/biokgbench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AgentClinic](../works/agentclinic.md)
- [MedAgentBench](../works/medagentbench.md)
- [SDBench](../works/sdbench.md)
- [BrainBench](../works/brainbench.md)
- [CodePDE](../works/codepde.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [MooseBench](../works/moosebench.md)
- [SimBench](../works/simbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [StructureClaw](../works/structureclaw.md)
- [FEM-Bench](../works/fem-bench.md)
- [SciConvBench](../works/sciconvbench.md)
- [PDE-Controller](../works/pde-controller.md)
- [HARDMath](../works/hardmath.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [HydroAgent](../works/hydroagent.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
