# Scientific Agent Benchmarks

> [English](../../topics/scientific_agents.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Scientific agent 不能只看文字像不像专家。它可能要复现一个结果、运行 simulator、调 parameter、检查 evidence，或者写出一段 code，而且最终数字还得达到领域标准。Evaluator 因此必须把 agent output 接到真实 scientific artifact 与 check 上。

拿一个 computational task 走一遍：给 agent 一个从 paper 取出的 question 和 starter environment，在 container 里执行它的 code，把结果与 accepted value 比较，同时记录 cost 和 failure stage。这比再找一个 model 判断答案「像不像科学」更扎实。但它只覆盖这道 task 所代表的 workflow 与 validity check，不能自动推出 agent 具备通用 scientific competence。

## 定义

Scientific agent benchmark 让 agent 去做真正来自科学实践的工作：跑计算 workflow、调 simulator、根据文献回答、分析数据，或复现已发表结果。它们的 task 来自科学工作，正确性也要靠 executable check、measured value、publication 或专家判断来锅定，不能只看文字像不像那么回事。

## 为什么重要

科学工作同时改变了 task 和 evaluator。跑一次 simulation 或 experiment 可能很贵，多种 tool 可能必须按领域规则排好顺序，分析方法也可能不止一种合理选择。但最后的数字仍然要符合物理约束或已发表结果。通用 agent benchmark 常常把这些条件拿掉，所以需要单独跟踪能把它们保留下来的 evaluation design。

## 现有方法

- **可执行的科学工作流。** [Terminal-Bench Science](../works/terminal-bench-science.md) 在容器中用 pytest 确定性验证 AI agent 在自然科学计算工作流上的表现，覆盖五个科学领域。
- **以出版物 SOTA 锚定难度。** [NatureBench](../works/naturebench.md) 从 Nature-family 论文蒸馏 90 个任务，追问 coding agent 是否能达到已发表 SOTA——揭示了显著缺口：最强 agent 仅在 17.8% 的任务上超越已发表 SOTA（匹敌 47.8%）。
- **专家验证、基于执行的任务。** [ScienceAgentBench](../works/scienceagentbench.md) 从四个学科的 44 篇同行评审论文中提取 102 个任务，邀请九位领域专家验证，并将每个任务的输出统一为自包含的 Python 程序，按程序、执行结果与成本打分。它坚持在宣称端到端自动化之前先评估单个工作流任务，并报告了偏低的最佳 agent 求解率（独立 32.4%，含专家知识 34.3%）。
- **端到端研究生命周期。** [AIRS-Bench](../works/airs-bench.md) 提供 20 个 frontier 研究科学任务，不提供 baseline 代码，要求 agent 在语言建模、数学、生物信息学、时间序列预测中从零构造工作流。
- **跨尺度的真实研究场景。** [SciAgentArena](../works/sciagentarena.md) 在 agent-agnostic 环境中提供约 200 个来自真实世界科学研究场景、带逐步验证的任务，报告 agent 能处理结构化数据分析工作流，但在新颖洞见、自主探索与开放式问题上表现吃力。
- **科学环境的 gymnasium。** [Aviary](../works/aviary.md) 提供一个可扩展的 language-agent 环境 gymnasium，其中三个为科学环境（分子克隆、科学文献研究、蛋白质工程）；其环境是可复用的评估面，尽管论文的头号贡献是训练框架而非评估贡献。
- **Cost-aware 科学仿真。** [SimulCost](../works/simulcost.md) 把 cost-aware 评估扩展到覆盖 13 个仿真器的物理仿真参数调优，显式建模仿真时间与实验资源成本。
- **医生共同验证的医疗评估。** [MedHELM](../works/medhelm.md) 把 Stanford CRFM 的 HELM 扩展到医疗任务：121 任务、由医生共同验证的分类体系；跨 35 benchmark 聚合；LLM-jury 方法与医生一致性（ICC = 0.47）被显式测量。
- **生成而非编写的 benchmark。** [HeurekaBench](../works/heurekabench.md) 贡献了一条半自动流水线，从已发表研究及其代码仓库中派生开放式研究问题，并将候选答案与这些研究已报告的发现比对验证。其单细胞实例含 50 道开放题与 50 道选择题，构建自 13 篇论文中的 41 条洞见；最强的现有 agent 在开放题正确性上为 5 分制的 2.34 分。
- **基于模拟的判分有效性。** [GeneBench-Pro](../works/genebench-pro.md) 把 129 个多阶段基因组学与定量生物学问题构建在人工模拟的数据生成过程而非真实数据集之上，从而使失败可归因于科学判断失误，而非归因于若干同样站得住脚的分析选择之一。每个问题内含 3 至 13 个相互依赖的决策点，仅以对决策相关数值的二元通过与否判分；所测得的最佳配置为 28.7%。
- **溯源审计下的已发表分析复现。** [Collider-Bench](../works/collider-bench.md) 要求 agent 仅凭公开论文与开源仿真软件复现 LHC 分析，用连续的直方图保真度对照隐藏参考产额为 10 个 CMS 搜索任务打分，并由 LLM judge 审计执行轨迹；在 364 次受评运行中 6% 的提交被标记为伪造，且平均而言没有 agent 能可靠胜过物理学家在环的解法。
- **反事实定律发现。** [NewtonBench](../works/newtonbench.md) 让 agent 对模拟物理系统运行实验，以复原 12 条经典物理定律的反事实偏移版本，用 LLM 判定的符号等价性为其 324 个任务打分。
- **计算材料科学中的主张级复现。** [AutoMat](../works/automat.md) 将 85 条由专家整理的计算材料科学论文主张打包为可运行的 HPC 任务，报告最佳 coding-agent 设定达到 54.1% 成功率，而当工作流必须仅凭论文正文复原时成功率接近零。
- **对接实时地理空间 API 的结构化工具调用。** [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) 针对一个开放、可自托管、服务于西班牙与葡萄牙三项指标的 API 运行 93 个环境分析任务，以机制性检查（不用 LLM judge）为每个案例打分，并把能力与单案例成本作为正交维度报告；最佳模型达到 60.8% ± 0.8%，而近似值比较类任务对每个模型都是 0%。
- **已发表 AI 实验的端到端复现。** [EXP-Bench](../works/exp-bench.md) 从 51 篇 NeurIPS 2024 与 ICLR 2024 论文中整理出 461 个任务，要求 agent 设计、实现、执行并得出完整实验结论；最佳 agent 配置仅能以可执行形式完成 0.5% 的实验。
- **全流程洞见再发现。** [FIRE-Bench](../works/fire-bench.md) 只给 agent 一个来自已发表机器学习研究的高层研究问题，并以对照该研究记录发现的主张级 F1 为其结论打分；最强的受评 agent Claude Code（Sonnet-4）在 30 任务核心集上达到 46.7。
- **隐藏论文再发现。** [ResearchClawBench](../works/researchclawbench.md) 将 40 个任务各自锚定在一篇真实已发表论文上，而该论文在评测期间保持隐藏，由 GPT-5.1 按 0–100 的 RADS 刻度、对照专家整理的加权评分标准为 agent 研究报告打分。
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
- **实验预算下的 Bayesian model discovery。** [Model Discovery Agent](../works/model-discovery-agent.md) 用同一套「选实验—更新 belief—提出新模型」循环，横跨化学、反事实物理、probabilistic program 和 electrophysiology。每次 intervention 以后都重测 held-out prediction 和 structural recovery，所以它看的不是最后蒙没蒙对，而是有用的机制多快浮出来。
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
- **官方奥赛评分。** [HiPhO](../works/hipho.md) 用官方评分方案与奖牌线在 13 套最新高中物理奥赛真题上评判 30 个 (M)LLM；闭源推理 MLLM 获 6–12 金，但大多数模型距满分仍远。[LLM-IOAA](../works/llm-ioaa.md) 把同一套标准搬到天文：五个前沿模型在 2022–2025 年完整的国际天文与天体物理奥赛理论卷与数据分析卷上受评，依官方 IOAA 评分标准打分——全部 285 次模型-题目评定都由前 IOAA 选手与领队评了两遍——Gemini 2.5 Pro（理论卷 85.6%）与 GPT-5 大致排在每年 200–300 名真人选手的前两位。
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
- **「产物像样」不等于「端到端做对」。** [StructureClaw](../works/structureclaw.md) 在 150 个结构工程场景上对照冻结的参考求解器响应；通用执行有 87.0% 通过模型产物检查，端到端成功率却只有 22.0%。
- **对齐课程难度的 FEM 编码。** [FEM-Bench](../works/fem-bench.md) 在 33 个研究生课程级计算力学任务上验证函数与单元测试编写，各尝试五次；最佳模型 26/33 个任务五次全成。
- **先澄清，再计算。** [SciConvBench](../works/sciconvbench.md) 为不适定仿真请求的多轮消歧与矛盾消解打分，覆盖流体力学、固体力学、材料科学与 PDE；最佳模型在流体力学消歧上仅解决 52.7%。
- **从意图到 PDE 控制。** [PDE-Controller](../works/pde-controller.md) 评估热/波动方程系统控制的自动形式化（自然语言到信号时序逻辑）、推理与程序合成，配人工案例加 200 万合成样本。
- **把近似当作受测技能。** [HARDMath](../works/hardmath.md) 自动生成经数值真值验证的研究生渐近分析问题；GPT-4 少样本思维链下仅 43.8%。
- **被重算的电网研究。** [PowerAgentBench-SS](../works/poweragentbench-ss.md) 让 agent 做电力系统故障研究，报告由隐藏评估器重新推导，false-safe 罚分与 severity regret 让没有依据的「一切正常」付出代价。
- **率定业务化预报模型。** [HydroAgent](../works/hydroagent.md) 以 Nash–Sutcliffe 效率评测九个前沿 agent 对 NWS 业务化 CREST 水文模型的率定；仅一个模型在一个测站达到人类专家参照。
- **以化学家为基线的大规模问答。** [ChemBench](../works/chembench.md) 用 2,700 多个策划问答对为 LLM 评分，并与招募的化学家队列对照；最强模型平均超过最强人类化学家，却在基础任务上依然过度自信。
- **以科研需求为纲的分类法。** [ChemEval](../works/chemeval.md) 把化学能力组织为 4 个递进层级、12 个维度、42 个任务，揭示通用模型（文献、指令）与化学专用模型（深层知识）之间的取舍。
- **考操作而非答案。** [ChemCoTBench](../works/chemcotbench.md) 把分子变换框定为加/删/换的模块化操作，使中间推理步骤可被评估，覆盖性质优化与反应预测的 1,495 个样本。
- **符号可验证的结构推理。** [MolecularIQ](../works/moleculariq.md) 只收录能对照分子图本身检验的任务，消除文献标签泄漏，并把失败定位到具体结构。
- **测出推理档位的跃升。** [ChemIQ](../works/chemiq.md) 出 816 道不借助工具的有机化学简答题并程序化判分；推理模型答对 50–57%，非推理模型只有 3–7%。
- **官能团层面的归因。** [FGBench](../works/fgbench.md) 追问是 245 个官能团中的哪一个驱动了性质差异，共 62.5 万个生成问题、7,000 个精选评测子集。
- **防捷径的定量化学。** [QCBench](../works/qcbench.md) 覆盖 7 个子领域、三档难度的 350 个计算题；24 个 LLM 随复杂度上升一致退化。
- **谱图推结构的分段拼图。** [MolPuzzle](../works/molpuzzle.md) 把解析拆成理解、谱图解读与构建三个阶段；GPT-4o 与真值精确匹配的比例仅 1.4%，远低于人类。
- **把解析当实验规划来考。** [MolQuest](../works/molquest.md) 让 agent 在多轮溯因循环中自己决定采集哪些谱图；SOTA 模型也只有约 50% 的准确率。
- **一对多的分子生成。** [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md) 对开放域的分子编辑、优化与生成按「是否满足指令」检验，而非对照单一参考，评测覆盖 31 个 LLM。
- **读—改—写的梯度。** [MolLangBench](../works/mollangbench.md) 显示 GPT-5 在结构识别与编辑上分别达 86.2% 与 85.5%，在生成上只有 43.0%；识别任务构造即可验证。
- **机理层面的反应推理。** [FukuyamaBench](../works/fukuyamabench.md) 要求为研究生机理教科书的题目给出完整的基元步骤路径；已报告的最好系统只精确解出 8.3%。
- **修正逆合成的指标。** [ChemCensor / CREED](../works/chemcensor.md) 用化学合理性指标取代精确匹配 Top-K，并用同一验证器构建了百万量级的训练数据集。
- **控制污染的假说重发现。** [MOOSE-Chem](../works/moose-chem.md) 让知识截止早于 2024 年的 LLM 重新发现 51 篇 2024 年后化学论文的假说，论文由化学博士标注为背景、灵感与假说。
- **从文献到数据库的抽取。** [ChemX](../works/chemx.md) 用 10 个专家校验的化学数据集评测 agent 式抽取器，发现其在领域术语、复杂表格与歧义上的失败持续存在。
- **给反应定价。** [ChemCost](../works/chemcost.md) 要求 agent 确定化学品身份、检索供应商报价并对照冻结快照计算反应成本；最强 agent 也只有 50.6% 落在 25% 相对误差内，且随噪声退化。
- **靠数据不公开来防泄漏。** [onepot-Bench 0](../works/onepot-bench.md) 把反应结果与催化剂选择的评估锚定在实验室私有数据上，另配化学信息学素养与拒答两个子组件。
- **实验室里的 VLM 瓶颈。** [MaCBench](../works/macbench.md) 发现视觉-语言模型在设备识别与数据抽取上近乎完美，但在空间推理与跨模态综合上存在根本性局限。
- **自主实验室的失败分析。** [LabRobFail](../works/labrobfail.md) 为化学自主实验室搭建失败中心的 benchmark——20,000+ 条轨迹，含控制级、物理级与语义级失败注入——领域专用 VLM 检测率达 90.83%，作为实时监督者提升下游任务成功率。
- **材料知识考试问答。** [MaScQA](../works/mascqa.md) 用 650 个 GATE 考题测 LLM 的材料知识，GPT-4 约 62%，概念性错误多于计算性错误。
- **大学水平的材料推理。** [MatSciBench](../works/matscibench.md) 出 1,340 个带参考解与图像的问题；DeepSeek-R1 文本达 75.22%，而图像最好仅 53.02%，把多模态推理标记为更难的前沿。
- **LLM 作为性质预测器。** [LLM4Mat-Bench](../works/llm4mat-bench.md) 在约 190 万晶体、45 种性质上评测生成式对话 LLM 与微调模型，发现任务专用模型仍占主导。
- **几何盲区。** [MatText](../works/mattext.md) 在九种晶体文本表示上评测 LLM，记录了一堵「GNN-LM 墙」：模型抓住类别模式却漏掉坐标信息。
- **晶体结构空间推理。** [AtomWorld](../works/atomworld.md) 以十种可验证的原子结构操作为 LLM 评分，旋转成功率低于 12%，暴露几何缺陷。
- **模型广度的晶体学问答。** [OpenXRD](../works/openxrd.md) 在 217 个专家策划 XRD 问题上评测 74 个 LLM/MLLM，表明 token 数相同时专家策划的上下文胜过 AI 生成的。
- **抗捷径的表征视觉问答。** [MatVQA](../works/matvqa.md) 用覆盖真实显微与衍射影像的 1,325 个问题测 17 个 MLLM，并迭代剔除文本捷径。
- **按阶段组织的表征。** [MatCha](../works/matcha.md) 横跨四个研究阶段、21 个任务共 1,500 个问题，发现与人类专家的显著差距且提示无法弥合。
- **按方法组织的表征问答。** [MatQnA](../works/matqna.md) 覆盖十种表征方法（XPS、XRD、SEM、TEM 等）；前沿 MLLM 在客观题上已达约 90%。
- **图级材料抽取。** [MatViX](../works/matvix.md) 在 324 篇全文论文上评测多模态抽取，产出 1,688 个 JSON 目标，评判性质曲线（CSS、CAS）而不只是实体。
- **材料工具使用。** [MatTools](../works/mattools.md) 测 LLM 能否理解并编程 pymatgen——69,225 对理解问答加 49 个执行任务——发现通用模型胜过专用模型。
- **自主 DFT 编排。** [AutoDFT / VASPBench](../works/vaspbench.md) 在 34 个任务、9 种计算类型上评测闭环 DFT agent，AutoDFT 达到 94.1% 的任务级成功率。
- **配方级规模的合成规划。** [AlchemyBench](../works/alchemybench.md) 把 17,000 条专家核验配方变成端到端预测，由一个经专家一致性验证的 LLM judge 判分。
- **面向发现的假说生成。** [Materials Hypothesis Generation](../works/materials-hypothesis.md) 用一个模拟专家的指标评测目标驱动、约束引导的 LLM agent 的材料设计假说。
- **Verilog 代码生成——标杆任务。** [VerilogEval](../works/verilogeval.md) 在 156 个 HDLBits 问题上，通过与参考解仿真为 LLM Verilog 生成评分；其 v2 增加规格到 RTL，GPT-4o 达 63%。
- **从自然语言生成设计级 RTL。** [RTLLM](../works/rtllm.md) 在 29 个手工设计（v2 为 50 个）上按语法、功能、设计质量为完整设计 RTL 生成判分，并提出 self-planning 提示。
- **仓库级 RTL。** [RTL-Repo](../works/rtl-repo.md) 在 4,000+ 真实 GitHub 样本上考察带完整仓库上下文的多文件 Verilog 补全，按编辑相似度与精确匹配判分。
- **另一种 HDL。** [VHDL-Eval](../works/vhdl-eval.md) 在 202 个问题上评测 VHDL 生成，发现 Verilog 中心的模型迁移不佳、需 VHDL 专门微调。
- **综合的 RTL 设计与验证。** [CVDP](../works/cvdp.md)（NVIDIA）横跨 783 问题 / 13 类别，兼有非 agent 与 agent 格式；最先进的模型代码生成 pass@1 不超过 34%。
- **基于形式验证的断言生成。** [AssertionBench](../works/assertionbench.md) 在 100 个 OpenCores 设计上，对照经形式验证的参考衡量 LLM 硬件断言生成。
- **形式验证能力。** [FVEval](../works/fveval.md)（NVIDIA）把硬件形式验证分解为三个子任务，用 Cadence Jasper 工具校验所生成断言。
- **高层综合。** [HLS-Eval](../works/hls-eval.md) 在 94 个设计上评测 LLM 的 HLS 代码生成与优化，在 Vitis HLS 上按可解析/可编译/可运行/可综合判分。
- **免训练的模拟设计。** [AnalogCoder](../works/analogcoder.md) 是通过 Python 代码生成设计模拟电路的 LLM agent，在精选 benchmark 上解出 20 个电路——比 GPT-4o 多 5 个。
- **模拟拓扑综合。** [AnalogXpert](../works/analogxpert.md) 把设计专长编码进 LLM agent，在合成/真实拓扑 benchmark 上达 40%/23%，而 GPT-4o 仅 3%。
- **多模态 EE 广度。** [EEE-Bench](../works/eee-bench.md) 出 2,860 个横跨 10 个 EE 子领域、需理解电路与框图的问题；17 个模型平均 19–47%，并有「偷懒」（文本压过视觉）失败模式。
- **沿 EDA 流程的电路问答。** [MMCircuitEval](../works/mmcircuiteval.md) 把 3,614 个多模态问答按设计阶段与能力组织，定位后端设计与复杂计算的短板。
- **电信知识。** [TeleQnA](../works/teleqna.md) 在取自 3GPP/IEEE 标准的 10,000 道电信题上评测 LLM，通用知识可比肩专业人士，却在标准规范上吃力。
- **控制系统设计。** [ControlAgent](../works/controleval.md) 用协作 LLM agent 自动化控制器设计，在 ControlEval（500 任务）上评估并胜过「工具箱+人工」基线。
- **电网调度。** [ElecBench](../works/elecbench.md) 用以电网稳定性与安全性为中心的六指标/24 子指标框架评测 LLM 的电力调度。
- **综合 EEG 理解。** [BrainBench (EEG)](../works/brainbench-eeg.md) 在四个子集、17 个数据集上评测 LLM 的指令条件 EEG 分析，基于执行、在自主代码与 agent 两种范式下为报告评分（不同于更早那个「结果预测」的 BrainBench）。
- **啮齿类行为标注。** [Rodent-Bench](../works/rodent-bench.md) 在真实啮齿类行为视频上测试多模态 LLM 的跨范式标注，发现没有模型强到能充当标注助手。
- **中文心理学考试。** [CPsyExam](../works/cpsyexam.md) 从 22,000 道题库中提炼出 4,000 道，沿心理学知识与案例分析两轴组织。
- **概念级心理学。** [ConceptPsy](../works/conceptpsy.md) 把心理学题目标注到 12 个学科的 1,383 个概念，显现总分会掩盖的逐概念表现差异。
- **专业咨询知识。** [PsychCounsel-Bench](../works/psychcounsel-bench.md) 用约 2,252 道美国国家咨询师认证考试题对照约 70% 及格线评测 LLM。
- **Kaggle 上的 ML 工程。** [MLE-bench](../works/mle-bench.md)（OpenAI）在 75 个精选 Kaggle 竞赛上以按奖牌门槛评分评测 agent；o1-preview 配 AIDE 在 16.9% 上达到铜牌。
- **可训练的 ML 工程竞技场。** [MLE-Dojo](../works/mle-dojo.md) 把 200+ Kaggle 挑战变成支持 SFT/RL 的交互环境，测量迭代改进与错误修复效率。
- **ML 实验。** [MLAgentBench](../works/mlagentbench.md) 让 agent 读写文件、运行代码、迭代以超过起始代码基线，覆盖 13 个任务；Claude 3 Opus 平均成功率最高 37.5%。
- **仓库级 ML 代码。** [ML-Bench](../works/ml-bench.md) 把 18 个仓库上的 9,641 个样例分为文本到代码赛道（Pass@5）与自主沙箱执行赛道。
- **数据科学专长。** [DSBench](../works/dsbench.md) 出 540 个多模态、多表分析与建模任务；最佳 agent 只解出 34.12% 的分析任务。
- **数据科学编码。** [DA-Code](../works/da-code.md) 在可执行沙箱中为 agent 式数据整理与分析代码评分，最强 LLM 达 30.5%。
- **分析判断。** [BLADE](../works/blade.md) 在 12 个数据集上，对照独立专家分析为数据驱动科学 agent 的构念、变换与模型选择评分。
- **新颖方法 ML 研究。** [MLRC-Bench](../works/mlrc-bench.md) 在 7 个竞赛任务上按「基线到顶尖人类差距」缩小的比例为 agent 评分；最佳只缩小 9.3%。
- **仓库复现。** [SUPER](../works/super.md) 评测搭建并执行真实研究仓库中的任务；GPT-4o 端到端解出 16.3%。
- **全流程 ML 研究。** [MLR-Bench](../works/mlr-bench.md) 在想法、方案、实验、论文四阶段评估 201 个开放式任务，发现 agent 约 80% 的情形编造结果。
- **AI R&D 对照人类专家。** [RE-Bench](../works/re-bench.md)（METR）在 7 个研究工程环境上以时间预算对照 61 位专家——2h 时 agent 4 倍，32h 时人类 2 倍。
- **面向 AI 研究的 RL 竞技场。** [MLGym](../works/mlgym.md)（Meta）把 Gym 环境与 13 个开放式研究任务配对，发现前沿 agent 调参却不创新。
- **实现新颖研究代码。** [ResearchCodeBench](../works/researchcodebench.md) 要模型实现 2024–2025 论文的贡献；最强（Gemini-2.5-Pro）达 37.3%。
- **研究想法生成。** [IdeaBench](../works/ideabench.md) 把 LLM 以有影响力论文上下文为依据，用两阶段框架按新颖性与可行性为想法评分。
- **发散式科学思维。** [LiveIdeaBench](../works/liveideabench.md) 在 1,180 个关键词、22 个领域上评估单关键词想法生成，发现创造力难以由通用智力预测。
- **AI 开发 agent，由 agent 评判。** [DevAI / Agent-as-a-Judge](../works/devai.md) 提供 55 个 AI 开发任务、365 个层级化需求，由 agent 化评判器评估、可靠性媲美人类。
- **专家级的神经科学流水线。** [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) 把一条真实的果蝇光遗传学研究流水线拆解为七个由专家评分的阶段，发现 agent 能解出单个阶段，却做不出正确的端到端发现。
- **真实环境中的端到端数据科学。** [DSAgentBench](../works/dsagentbench.md) 评估 agent 能否在真实计算机环境（notebook、IDE、终端、浏览器、数据库）中自动化完整的数据科学生命周期，共 275 个任务，每个都配一个确定性评估器。
- **科学可视化 agent。** [SciVisAgentBench](../works/scivisagentbench.md) 用一套以结果为中心、结合图像指标、代码/规则验证器与经人类验证的 LLM judge 的多模态管线，为横跨七个科学领域的 108 个专家精心设计的 SciVis 案例评分。
- **研究级的证明生成。** [TCS-Bench](../works/tcs-bench.md) 从 FOCS/STOC/SODA 论文（2020–2026）中组装 300 个定理证明任务，用一个校准到超过 90% 专家一致率的自动验证 agent 判分。
- **证据受限的实验推理。** [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md) 在化学、生物与材料科学中，对真实实验图表与数据做多模态推断，把证据受限的推理定力与信息获取分离开来。
- **统计上有效的假设检验。** [Fisher-R1 / P-Bench](../works/fisher-r1.md) 在 425 个扎根于已记录参考代码执行的任务上，评估 agent 是否选对了统计方法、算出了有效的 p 值，并得出正确的拒绝/不拒绝结论。
- **人类授权的物理能源 agent。** [EnergyBridge](../works/energybridge.md) 为住宅虚拟电厂耦合容量申报、住户授权与物理执行，并从分地区的 EnergyPlus 模型计量结果。
- **VLSI 物理设计。** [PDAgent-Bench](../works/pdagent-bench.md) 把任务级评估（353 道精选 EDA 题目）与工作流级闭环物理设计流程统一起来，发现模型在概念上有竞争力，但在工具中心、长时程的执行上偏弱。
- **以可靠性评分的心理健康推理。** [MiraMind](../works/miramind.md) 在六类任务、13 个数据集上评估心理健康推理，不仅为结果打分，也为「从证据到判断」推理轨迹的可靠性打分。
- **端到端的化工过程开发。** [CeProBench](../works/ceprobench.md) 把过程开发的评估围绕知识、概念、参数三条线索组织起来：六类任务，共 243 道题与 235 项任务，素材取自 70 份技术文档（4,406 个实体 / 4,967 条关系）、113 张源自竞赛的工艺流程图（986 台设备、1,172 条连接）以及 20 个 Aspen Plus 参数文件；其中参数类任务通过在 Aspen Plus 中实际执行候选操作设定来评分，因此决定分数的是热力学可行性，而不是文本相似度。
- **以收敛作为通过标准，并与专家比耗时。** [Simona](../works/simona.md) 用仿真收敛率（Simulation Convergence Rate, SCR）为 1,000 段专家撰写的工艺描述打分——只有生成的流程图在仿真器中真正收敛，这份设计才算数——并把设计耗时作为并列的另一条评价轴一同报告；人类专家基线为 100% SCR、8,301.91 秒，让受评系统在质量与耗时两方面都有一个可解读的上界参照（所提出的工作流为 80.3%，GPT-4o 为 23.4%）。
- **相似不等于在领域内成立。** [Can Large Language Models Automate the HAZOP Process?](../works/can-large-language-models-automate-the-hazop-proce.md) 在同一批生成的工作表上，把模型层面的表现与过程安全层面的表现分开衡量：四个多模态模型对照专家编制的 HAZOP 参考，F1 都超过 86%，但它们生成的场景中只有 0.19–0.37 在语义上成立，而且所提出的防护措施明显偏向程序性措施，而非工程化的保护层。
- **以过程工程师为基准校准的评审团。** [PSE-Bench](../works/pse-bench.md) 用五个相互独立的 LLM 评审，按七要素 rubric 为 200 道开放式过程系统工程题目打分，再请三位领域专家重新评阅同一批答案：二者的一致性为 Spearman rs = 0.416、ICC = 0.793，且 LLM 评审在 0–7 分制上系统性偏松 +0.85 分——论文把这一偏差当作校准常数明确报出，而不是让它隐而不显。
- **在结构分析里，真值握在求解器手上。** 结构工程方向的一批工作，评的不是 agent 写出的文字，而是它建出的模型，参照物则由 agent 左右不了的软件生成。[Agentic LLMs for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md) 只有当生成的 SAP2000 模型*每一项*受监测响应都落在人工搭建参考模型的 1% 以内时，才判该次试验正确——它的分解式流水线在十个不规则框架上平均达到 90%，而 GPT-5.4 与 Gemini-3.1 Pro 在这十个框架上全是 0%。[Toward Responsible AI in High-Stakes Domains](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) 把同一套相对误差检验换到 ETABS 上，并特意保留裸模型作为对照：无辅助的 GPT-4o 相对误差约在 230–270%，而同一个模型经 MCP server 驱动 OpenSeesPy 后低于 1.427%。[Automating Structural Reliability Analysis with a Multi-Agent LLM Framework](../works/automating-structural-reliability-analysis-with-a.md) 干脆把这种安排上升为架构规则——可靠指标与失效概率只由确定性运行器调用经验证的求解器给出，绝不出自语言模型；[AutoBM / BMEval](../works/autobm.md) 则把容差量化下来，要求生成的 OpenSeesPy 模型的一阶自振周期落在专家校验参考值的 0.30 相对误差之内。
- **把运行间的稳定性当作指标，而不是误差棒。** [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md) 的两项测度都建立在「重复」本身之上：可靠性是同一条提示词独立跑 500 次中答对的比例，鲁棒性则是把荷载沿梁逐点移动，再对由此得到的那组可靠性值算 (1 + CV)⁻¹。Llama-3.3 70B 在简支梁上守住 93.6% 的可靠性，在组合荷载下的外伸梁上却跌到 10.0% 以下；而生成代码的 agent 可靠性超过 99.0%、鲁棒性超过 99.6%。周边一批工作走的也是同一思路，只是规模更小——[Lightweight Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md) 每个框架跑十次，[Integrating LLMs for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md) 跑五次，[LLM-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md) 每个算例跑三次；[TransportBench](../works/transportbench.md) 更是把准确率与稳定性彻底拆开：它最准的模型 Claude 3.5 Sonnet，恰恰也是被要求复核时放弃了 16 个原本答对答案的那一个。
- **一项成规模发布的工业级土木任务。** [DrafterBench](../works/drafterbench.md) 选取的技术图纸修改，是通过走访十余家北美建筑公司确认的劳动密集型工作；它以 100 多份真实修改文件为素材，围绕 46 个自定义图纸操作工具构建了 1,920 个任务。生成器把十二类修改任务与五个二值指令控制变量（措辞是否结构化、取值是否精确、信息是否完整、对象数量、操作数量）做交叉，指令质量因此成为受控变量，分数下滑也就能归因到某一处具体缺陷；配套的 dual function 只记录操作路径而不触碰文件，于是被计分的产物是轨迹本身，而不是渲染出来的图纸。
- **把规范符合性的判定结论作为受评产出。** 当答案由法规决定时，有几个 benchmark 评的就是 agent 有没有得出监管者的结论、又是否给出了应有的理由。[SGR-BIM](../works/sgr-bim.md) 在五个 IFC 建筑模型上提出 679 条经专家核验的消防安全查询，按三档准确率评分——结论对了但没能点明起决定作用的变量与边界条件，就拿不到满分；其基于图的系统总分 84.3，而持有完全相同工具集的单 agent 只有 75.7，CAMEL、AutoGen 与 MetaGPT 落在 64.9–73.2，可见弥合差距的并不是泛用的多智能体协作。[AutoBM / BMEval](../works/autobm.md) 把明确的设计校核结论列为 Pass@k_strict 所合取的三道关卡之一；[AEC-Bench](../works/aec-bench.md) 则发现工作中越依赖判断的一端越难——图纸导航的 reward 达到 100.0，报审资料审查最高却只有 23.1。
- **以专业检测记录作为答案标准。** [BridgeEQA](../works/bridgeeqa.md) 把 200 个真实桥梁场景上的 2,200 道题目扎根于佛蒙特州交通厅的检测报告，状况判定按 NBI 的 0–9 分制评分并允许 ±1 的容差带——因为专家检测员之间的一致程度本就只有这么高——同时引入 Image Citation Relevance，让那些依据无关影像却蒙对评级的 agent 被扣分。[Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) 对照的是六个年度全国桥梁清单版本中实际观测到的劣化，并把「结果如何定义」本身当作实验变量：目标定得含糊时 agent 近乎随机（AUC 0.471），换成「是否恶化进入 poor 状态」则达到 0.705，而同一设定下一个不透明的梯度提升模型只有 0.521；此外还请一位持证检测员对它写出的 100 段理由做盲评，3 分制下平均 2.77 分。[DefectBench](../works/defectbench.md) 把外墙病害逐级加码——命名缺陷、定位缺陷、分割缺陷——且每一问都以模型自己上一问的回答为条件，从而把误差传播暴露出来而非藏起来。
- **以执业资格考试作为难度标尺。** [Evaluating AI Chatbots on the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md) 把 NCEES 的练习题交给 ChatGPT-4 与 Bard，沿用考试本身不给部分分的二值判分：ChatGPT-4 在 FE 与 PE 上分别得到 70.9% 与 46.2%，Bard 则是 39.2% 与 41%——FE 大致能过，PE 则差得远。[PE Civil Bench](../works/pe-civil-bench.md) 把同一来源做成公开发布的 150 题语料，覆盖八个子学科，并把增强策略提升为一等因素，用基础提示、向量 RAG 与 agentic RAG 三种方式跑同一批题目。[Civil-Eval](../works/civil-eval.md) 对中国的国家注册考试做了同样的事，并按各科计算题占比赋予权重；[AECBench](../works/aecbench.md) 的 4,800 道题中有一部分取自执业资格考试，同时把全部 23 类任务沿五个认知层级排布，于是单一分数变成一条退化曲线——术语类高于 95%，文档撰写类则低于 60%。
- **天文原生的科学计算，以职业天文学家为评判尺度。** [AstroVisBench](../works/astrovisbench.md) 把 110 份真实的天文教程 notebook 切成 setup、processing、visualization 三段，处理段按它产出的内存变量评分，图则看它有没有传达出正确的科学洞见——所用的视觉语言 judge 不是想当然指定的，而是依据与五位天文学家标注面板的实测相关性选出（ρ = 0.822，而天文学家彼此之间的 Fleiss' κ 为 0.53）；八个模型中最强的一个，也只有 15.7% 的可视化任务被判为 No Error。[gammapyGPT](../works/gammapygpt.md) 把靶子收窄到一个文档稀薄的仪器分析库，验的是数值分析结果——观测数量、区域显著性、能流、谱指数——而不是代码看上去合不合理，并记下验证是在第几次尝试通过的，从而把一次到位与事后补救区分开来。[Imaging-101](../works/imaging-101.md) 把 57 个以论文为依据的计算成像任务规整成同一条四阶段流水线，在规划、函数级与端到端三条赛道上评分，其天文切片覆盖 Event Horizon Telescope 重建、日冕仪系外行星成像与 Shack–Hartmann 波前探测；端到端最好成绩是 57 中的 17。
- **及格线由领域早已认可的天文软件划定。** 有一批天文工作不肯把「成功」的定义交给语言模型，而是把它锚在领域一直信任的软件上。[Mephisto](../works/mephisto.md) 只有当 agent 给出某个 χ² < 1.2 × 穷举 3.6 亿点 CIGALE 网格搜索所得 χ² 的 SED 模型时，才算这个星系被解释清楚；同一套 256 星系流程还在七种底座上重跑，并对照相对 API 成本。[An LLM-driven framework for cosmological model-building](../works/an-llm-driven-framework-for-cosmological-model-bui.md) 让 agent 去改容器化的 CLASS 3.3.0，并叠了三层检查——二元的执行里程碑、算得的可观测量相对标准实现的最大相对偏差，再到对照 DESI、Planck、Pantheon+ 与 SH0ES 数据的似然、BIC、Hubble 张力与 CMB 自洽性奖励——因此能编译通过的实现并不自动等于成功的实现。[SimAgents](../works/simagents.md) 把还原出的模拟配置，对照 40 余项已发表宇宙学模拟的人工标注做参数级评分，并把 Type Error（软件层面非法的取值）与 Value Error、幻觉分开计数，好让那些物理上说得通、却根本跑不起来的输出不被埋没。
- **准确率、推理与诚实度，评在同一个观测判断上。** [AstroAlertBench](../works/astroalertbench.md) 把 1,500 条真实 ZTF 警报按人类审核者看到的样子呈现——broker 元数据加上 science/reference/difference 三联图——并把元数据感知、结构化的天体物理论证，以及伪迹 → 起源 → 子类的层级判断分开评分；再加一条诚实度轴，衡量模型的自我评估跟不跟得上它的正确率，具体通过群体层面的谦逊度、实例层面的校准度，以及第二轮 rollout 重试这一行为学探针来考察；13 个模型中最好的端到端成绩为 60.60 ± 1.26%，而实测的人类集成基线是 30.67%。[Spec-o3 / SpecVI-Bench](../works/spec-o3.md) 则刻意去搭建同一问题中更难的那一半：负样本按 0.8 的分类器概率做拒绝采样，因而正是部署中的分类器真会推到人跟前的那些光谱；测试集保持不均衡，以正类 F1 为头号指标；LAMOST → SDSS/DESI 的划分用来考察巡天迁移；另有六位天文学家在标签准确率之外，依公开的 0–5 分 rubric 为 100 条推理轨迹打分。
- **先由专家评分，再据此校准 judge。** [CosmoPaperQA](../works/cosmopaperqa.md) 让一位博士级宇宙学家，把九种 RAG 配置在 105 组专家撰写问答对上产生的全部 945 条回答逐条手工评分，并在报告 LLM judge 时一并附上它们的偏差方式——o3-mini 比人类专家低 2–8 分，Gemini 2.5 Pro 高 5–15 分，因此只有排序（Pearson r > 0.99）被认为可以迁移。[From Queries to Criteria](../works/from-queries-to-criteria-understanding-how-astrono.md) 的评判标准来自实践而非 benchmark 设计者的直觉——取自在 STScI 面向天文学家四周部署中的 368 条查询与 11 次访谈——并把公开的 40 题 benchmark 的自动相关性分数，对照部署期间真实的赞/踩评分做了验证，Pearson 相关为 0.82。[AI's Capability in Assisting Scientific Research I](../works/ai-assisting-research-i-literature-review.md) 把八位领域专家与三个 AI 系统摆在同样八个前沿课题上，发现主要失效并不是编造：641 条仅由 AI 给出的参考文献中，33% 元数据完全正确，64% 至少有一个字段出错，3% 属凭空捏造，而人机重合率对每个系统都低于 6%。
- **把「静默地错得很像样」的结果本身当作被测对象。** [Plausible but Wrong](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) 把评分拆成执行成功、参数准确度与数值准确度，并把后两者相乘合成，使配置上的功力无法掩盖物理上的错误；四类失败模式也正是由这几项分数上的阈值定义的。剩下的主导失败模式不是崩溃，而是 Mode C——程序跑通了，求解器参数看着也合理，数字却是错的——在没有文档上下文时约占 47% 的运行，四个开放式 Deep Research 任务更是全部静默失败。[First head-to-head comparison of agentic AI on Einstein Telescope data](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) 从过程一侧触及同一忧虑：两个 agent 拿到相同的规格说明、跑在相同的硬件上，最终收敛到相同的探测效率，可其中一个悄悄把目标信噪比下限从 7 改成了 8；重启、静默偏离、显式自我纠正与未经要求的优化，都是从日志里数出来的，而不是靠轶事描述。[Quantifying the Reproducibility of Astrophysical Methods](../works/quantifying-the-reproducibility-of-astrophysical-m.md) 则把同一道缺口定位到源文本上：重建出的流程按四级 Hierarchy of Scientific Validity 评分，一旦给出 Methods 部分，三个前沿模型都能还原显式的框架（V = 2），却没有一个能还原那些让结果得以校准的隐含统计约束（V = 3）。
- **以天文学家本人为对照的受控实验。** [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) 让科学问题在 32 份格式统一的盲评一页纸计划书中保持固定，再把同一套四方面 rubric 同时交给一个由教师与资深博后组成的四人评审组和两位 LLM 评审：人类给人写的和 AI 写的打分大体相当（3.52 对 3.25–3.74），两位 LLM 评审却都给 AI 撰写的文本多打了大约一整分；而 AI 的优势恰恰集中在人类投入最弱的地方（r ≈ −0.95）。[AI Cosplaying as Astrophysicists](../works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md) 干脆用角色化人设替换真人被试，使每一项指派都能在其他条件全不变的前提下跑遍五种辅助策略，12,960 个回合的评分中还把灾难性失败单列成一条与任务质量分开的通道；平均效用是中性的（+0.0017），灾难性失败率却上升（+0.0112），且集中在推导与推理上——而论文报告的角色互换复现，把这一主结论的正负号翻了过来。

- **把知识结构本身当作产出，而不是当作查询对象。** 有一批工作把本体或知识库变成 agent 被评分的*产出*，而不是它读取的现成资料。[FlyAOC](../works/flyaoc.md) 只给 agent 一个基因符号和一份固定的 16,898 篇果蝇全文论文语料，再拿 FlyBase 策展员实际产出的 7,397 条注释去核对 agent 写出的 Gene Ontology、表达模式与同义词注释——GO 与表达在本体 DAG 上按语义计算 recall@k，本体意义上相近却未完全对上的答案不会被一概判错；另有一个以语料为依据的子集，把可达的上限摆明。[Frontier LLM-based agents can overcome the ontology curation bottleneck](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md) 从另一头逼近同一个问题：原封不动地重放一份 2018 年的生物策展金标准，沿用它原来的指标，并以原来那三位人类策展员为参照带——结果所有被评的 agent 都落在这条带内。[OntoLearner](../works/ontolearner.md) 补上了该领域一直缺的共用基础设施——覆盖 22 个领域的 180 个本体，为术语归类、分类体系发现与非分类关系抽取备好固定切分——只是它的设定是单次结构化预测而非 agent 循环，且 22 个领域中大多数落在本仓库范围之外。
- **领域 skill 是骨架，benchmark 衡量的是它换来了什么。** [CASCADE](../works/cascade.md) 从网络搜索、文档与反思中不断累积可执行 skill，再用 SciSkillBench 的 116 个材料科学与化学任务来衡量它们，并在同一批任务上把各项演化机制逐一消融、与 Native 基线对照（GPT-5 下 93.26% 对 35.36%）。[MolClaw](../works/molclaw.md) 把 70 个精选 skill 组织成工具级、工作流级与学科级三层，并随附 MolBench——其「筛选 → 优化 → 端到端」的分层是有意设计的，好让消融把随手写个脚本就能解的任务，与非得有结构化工作流才行的任务分开。[LQCDMaster](../works/lqcdmaster.md) 用三个专家标注的格点 QCD skill 加一个确定性的 Wick 缩并工具，并要求生成的每条 PyQUDA 工作流在机器精度上与专家参考实现数值相符——另设 Convention Mismatch 一档，使全局符号差异不被记成错误。三者的 skill 库都是系统架构本身，benchmark 评的则是它产出的科学。
- **真实的科学数据库，真正起作用的判据却没写出来。** [BiomedSQL](../works/biomedsql.md) 把 68,000 组 question / SQL / answer 三元组落在一个存放神经退行性疾病遗传学与药物审批记录的生产级 BigQuery 库上，题目刻意写成让起决定作用的那道过滤条件——全基因组显著性、效应方向、哪些试验期算作已获批——必须由模型自己补出来；所有配置都比实测的双分析师基线低约 27 分。[AISE-Bench](../works/aise-bench.md) 瞄准的则是学术知识图谱，除答案外还标注了计划与经校验的 API 参数，于是「答案对、路子错」也会显形。
- **用一棵 rubric 树取代一个笼统的 judge。** [RubricsTree](../works/rubricstree.md) 把开放式的个人健康 agent 评估自顶向下拆成 100 多条医生可以逐条核验的原子布尔叶节点 rubric，再由上下文感知路由器只激活与当前查询相关的那一部分；与专家组的一致性达到 ICC₃ = 0.876、κ = 0.787，而基于原则的基线只有 0.291 与 0.431；同一套 rubric 还被复用为指令、反馈与训练奖励。

## 方法对比

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
| AutoMat | 2026 | 由材料科学专家从近期论文整理的 85 条主张 | 计算材料科学（统计/ML、DFT、MD、DDD） | 以产物为依托的 LLM 评估 agent 对照隐藏专家复现步骤打 1–5 分；成功为至少 4 分 | [→](../works/automat.md) |
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
| Model Discovery Agent | 2026 | ChemBench、ForceBench、七个 BoxingGym domain 和六个 deterministic/stochastic NeuronBench world | 实验预算下的 interactive mechanistic model discovery | Held-out intervention prediction curve + deterministic structural-recovery check | [→](../works/model-discovery-agent.md) |
| FEABench | 2025 | 经 COMSOL Multiphysics API 求解的多物理场问题 | 有限元多物理场仿真 | 对生成 API 调用与计算答案的评估；可执行率指标 | [→](../works/feabench.md) |
| QMP-Bench | 2026 | 提取自 21 种高影响力期刊的 100 个任务 | 量子多体模拟 | 编程验证器加基于物理原理的科学验证器 | [→](../works/qmp-bench.md) |
| gwBenchmarks | 2026 | 8 个任务，底层数据代表 10⁸+ 核时计算 | ≲10⁻⁴ 相对误差要求下的引力波天文学 | 外部预定义评估框架，配单任务物理指标 | [→](../works/gwbenchmarks.md) |
| ReplicationBench | 2025 | 与原作者共同开发的 20 篇论文 111 个任务 | 天体物理论文复现 | 逐任务客观评分：忠实性与正确性 | [→](../works/replicationbench.md) |
| PRL-Bench | 2026 | 100 篇 2025 年 8 月后的 PRL 论文，专家验证 | 五个子领域的前沿物理研究 | 客观可验证的结果；0–100 制评分 | [→](../works/prl-bench.md) |
| EnvTrace | 2025 | 同步辐射装置的光束线控制代码生成 | 实验物理的仪器控制 | 对照数字孪生的执行轨迹对齐 | [→](../works/envtrace.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | 53 个显微术测试 × 105 种 agent 配置 | 自主显微术 / 材料表征 | 带轨迹日志的 benchmark 测试；时延、成本与失败模式比较 | [→](../works/agentic-microscopy-benchmarks.md) |
| CritPt | 2025 | 50 余位物理学家的 71 个未发表挑战 + 190 个检查点 | 11+ 子领域的研究入门级物理 | 防猜测、可机器验证的答案；定制自动判分 | [→](../works/critpt.md) |
| TPBench | 2025 | 57 道全新问题，从本科到研究级 | 理论物理：高能理论与宇宙学 | 可自动验证的答案与定制判分 | [→](../works/tpbench.md) |
| SciCode | 2024 | 科学家整理的 80 个主问题 / 338 个子问题 | 16 个自然科学子领域（数学、物理、化学、生物、材料） | 对照科学家标注的参考解与测试执行 | [→](../works/scicode.md) |
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
| ChemBench | 2024 | 2,700 多个专家策划的问答对 | 与人类化学家对照的化学知识与推理 | 自动化框架评分，配人类化学家基线与置信度分析 | [→](../works/chembench.md) |
| ChemEval | 2024 | 开源数据加专家手工设计的任务 | 化学：4 个递进层级、12 个维度、42 个任务 | 精选提示下的零样本/少样本评估 | [→](../works/chemeval.md) |
| ChemCoTBench | 2025 | 1,495 个样本、22 个任务，以模块化化学操作呈现 | 分子性质优化与反应预测 | 在标注操作工作流上的结构化分步评估 | [→](../works/chemcotbench.md) |
| MolecularIQ | 2026 | 符号可验证的分子图任务 | 分子结构推理 | 对照分子图的符号验证 | [→](../works/moleculariq.md) |
| ChemIQ | 2025 | 816 道有机化学简答题 | 有机化学，含 NMR 结构解析 | 无 judge 的程序化判分（精确匹配、OPSIN、规范 SMILES） | [→](../works/chemiq.md) |
| FGBench | 2025 | 62.5 万个生成问题；7,000 个精选评测子集 | 官能团层面的分子性质推理 | 对照数据集标签的回归与分类评分 | [→](../works/fgbench.md) |
| QCBench | 2025 | 覆盖 7 个化学子领域的 350 个定量问题 | 定量与计算化学 | 防捷径分步计算的分档准确率 | [→](../works/qcbench.md) |
| MolPuzzle | 2024 | 200 个解析实例、23,678 条样例、三个阶段 | 基于 IR/MS/NMR 谱图的结构解析 | 各阶段精确匹配准确率，配人类基线 | [→](../works/molpuzzle.md) |
| MolQuest | 2026 | 多轮交互的解析回合 | 由模型规划实验的结构解析 | 最终结构准确率（SOTA 约 50%） | [→](../works/molquest.md) |
| Speak-to-Structure (TOMG-Bench) | 2024 | 开放域分子生成指令（MolEdit/MolOpt/MolCustom） | 自然语言驱动的分子设计 | 一对多的指令满足性检验 | [→](../works/tomg-bench.md) |
| MolLangBench | 2025 | 化学信息学构造加专家标注的任务 | 语言提示的结构识别、编辑与生成 | 按任务计准确率；识别类答案构造即可验证 | [→](../works/mollangbench.md) |
| FukuyamaBench | 2026 | 取自 Fukuyama《Advanced Organic Reaction Mechanism》的问题 | 层级化反应机理推理 | 完整路径精确匹配（最好成绩 8.3%） | [→](../works/fukuyamabench.md) |
| ChemCensor / CREED | 2026 | 数百万条经验证的反应记录 | 单步逆合成评估 | 以 ChemCensor 化学合理性指标取代精确匹配 Top-K | [→](../works/chemcensor.md) |
| MOOSE-Chem | 2024 | 51 篇 2024 年后的化学论文，由化学博士标注 | 化学假说重发现 | 知识截止控制下与真值假说的相似度 | [→](../works/moose-chem.md) |
| ChemX | 2025 | 10 个专家校验的抽取数据集 | 化学信息抽取（纳米材料、小分子） | 对照专家校验记录的抽取质量 | [→](../works/chemx.md) |
| ChemCost | 2026 | 冻结价格快照上的 1,427 个反应（230,775 条供应商报价） | 化学品采购与成本推理 | 无 judge 的精确真值，配阶段级失败诊断 | [→](../works/chemcost.md) |
| onepot-Bench 0 | 2026 | 私有组件，含实验室产生的私有数据 | 化学信息学素养、拒答行为、反应结果预测 | 分组件对照私有实验真值评分 | [→](../works/onepot-bench.md) |
| MaCBench | 2024 | 多模态的化学与材料任务 | 数据抽取、实验理解、结果解读 | 经 ChemBench 管线计准确率 | [→](../works/macbench.md) |
| LabRobFail | 2026 | 模拟化学自主实验室的失败轨迹（Isaac Sim） | 面向自主化学实验的实验室机器人失败分析 | 六项能力，含检测（90.83%）与时间定位 | [→](../works/labrobfail.md) |
| MaScQA | 2023 | 650 个 GATE 考试的材料与冶金问题 | 材料科学知识问答 | 准确率加「概念 vs 计算」错误分类；GPT-4 约 62% | [→](../works/mascqa.md) |
| MatSciBench | 2025 | 1,340 个大学水平问题（946 个有解、315 个带图像） | 横跨子学科的材料推理 | 文本与图像题准确率；DeepSeek-R1 75.22% / GPT-5 53.02% | [→](../works/matscibench.md) |
| LLM4Mat-Bench | 2024 | 约 190 万晶体、45 种性质、3 种文本模态 | 材料性质预测 | MAD:MAE（回归）与 AUC（分类）；生成式 LLM 近乎随机 | [→](../works/llm4mat-bench.md) |
| MatText | 2024 | 9 种晶体文本表示，参数至 70B / 200 万结构 | 从文本做晶体性质预测 | 对照 GNN 基线的回归误差；「GNN-LM 墙」 | [→](../works/mattext.md) |
| AtomWorld | 2025 | 四类建模范式下的 10 种原子结构操作 | 晶体结构空间推理 | 可验证结构检查；旋转成功率低于 12% | [→](../works/atomworld.md) |
| OpenXRD | 2025 | 217 个专家策划 XRD 问题、74 个模型 | 晶体学（XRD）问答 | 闭卷 vs 开卷准确率；专家 vs AI 生成上下文 | [→](../works/openxrd.md) |
| MatVQA | 2025 | 1,325 个问题、17 个 MLLM、真实显微/衍射 | 材料表征视觉推理 | 四类 SPP 任务准确率，带捷径剔除 | [→](../works/matvqa.md) |
| MatCha | 2025 | 横跨 4 个阶段 / 21 个任务的 1,500 个问题 | 材料表征理解 | 带人类专家基线的准确率；提示无法弥合差距 | [→](../works/matcha.md) |
| MatQnA | 2025 | 10 种表征方法（XPS/XRD/SEM/TEM 等） | 材料表征与分析 | 客观 + 主观问答；前沿 MLLM 客观题约 90% | [→](../works/matqna.md) |
| MatViX | 2024 | 324 篇全文论文 → 1,688 个结构化 JSON | 材料数据抽取（文本/表格/图） | 成分 F1；性质曲线的相似度/对齐分 | [→](../works/matvix.md) |
| MatTools | 2025 | 69,225 对理解问答 + 49 任务 / 138 子任务 | 材料计算工具使用（pymatgen） | 工具理解准确率 + 经执行验证的代码生成 | [→](../works/mattools.md) |
| AutoDFT / VASPBench | 2026 | 横跨 9 种 DFT 计算类型的 34 个任务 | 自主 DFT 工作流编排 | 任务级成功率（GPT-5.2 94.1%）+ 对照数据库的性质准确率 | [→](../works/vaspbench.md) |
| AlchemyBench | 2025 | 17,000 条专家核验合成配方 | 材料合成规划 | 对自由文本预测的、经专家一致性验证的 LLM-as-a-Judge | [→](../works/alchemybench.md) |
| Materials Hypothesis Generation | 2025 | 从近期论文策划的目标/约束/方法 | 材料发现的假说生成 | 一个可扩展、模拟专家的评估指标 | [→](../works/materials-hypothesis.md) |
| VerilogEval | 2023 | 156 个 HDLBits Verilog 问题 | Verilog RTL 代码生成 | 与参考解仿真对比；pass@k | [→](../works/verilogeval.md) |
| RTLLM | 2023 | 29 个手工 RTL 设计（v2 为 50 个） | 从自然语言生成设计级 RTL | 语法、功能、设计质量三目标 | [→](../works/rtllm.md) |
| RTL-Repo | 2024 | 4,000+ 带完整仓库上下文的 Verilog 样本 | 仓库级 RTL 代码补全 | 编辑相似度与精确匹配 | [→](../works/rtl-repo.md) |
| VHDL-Eval | 2024 | 202 个配自验证测试台的 VHDL 问题 | VHDL 代码生成 | 零样本/ICL/PEFT 下的功能正确性 | [→](../works/vhdl-eval.md) |
| CVDP | 2025 | 783 问题 / 13 类别，非 agent + agent（NVIDIA） | RTL 设计、验证与调试 | 容器化开源 EDA 环境中的 pass@1；SOTA ≤34% | [→](../works/cvdp.md) |
| AssertionBench | 2024 | 100 个 OpenCores 设计、经形式验证的断言 | 硬件断言生成 | 功能正确断言的比例 | [→](../works/assertionbench.md) |
| FVEval | 2024 | 3 个形式验证子任务（NVIDIA） | 数字硬件的形式验证 | Cadence Jasper 形式工具校验 | [→](../works/fveval.md) |
| HLS-Eval | 2025 | 94 个 HLS 设计 + 测试台 | 高层综合代码生成与优化 | 可解析/可编译/可运行/可综合 + pass@k | [→](../works/hls-eval.md) |
| AnalogCoder | 2024 | 精选模拟设计任务集（24 个任务） | 经代码生成的模拟电路设计 | 按解出任务数的 Pass@1/Pass@5；20 个电路对 GPT-4o 的 15 个 | [→](../works/analogcoder.md) |
| AnalogXpert | 2024 | 30 个真实 + 2,000 个合成拓扑案例 | 模拟拓扑综合 | 单次正确性；40%/23% 对 GPT-4o 3% | [→](../works/analogxpert.md) |
| EEE-Bench | 2024 | 横跨 10 个 EE 子领域的 2,860 个多模态问题 | 多模态电气与电子工程 | 17 个 LLM/LMM 的准确率；平均 19.48–46.78% | [→](../works/eee-bench.md) |
| MMCircuitEval | 2025 | 横跨数字+模拟、EDA 阶段的 3,614 个多模态问答 | 跨 EDA 流程的电路知识与设计 | 按设计阶段、电路类型、能力、难度的准确率 | [→](../works/mmcircuiteval.md) |
| TeleQnA | 2023 | 取自 3GPP/IEEE 与研究的 10,000 道电信题 | 电信知识 | 对照电信专业人士基线的选择题准确率 | [→](../works/teleqna.md) |
| ControlAgent / ControlEval | 2024 | 500 个控制设计任务（ControlEval） | 控制系统设计与整定 | 对照「工具箱+人工」基线的平均与 agent 成功率 | [→](../works/controleval.md) |
| ElecBench | 2024 | 电力调度场景、8 个 LLM | 电网运行与调度 | 六指标 / 24 子指标（稳定性、安全性……） | [→](../works/elecbench.md) |
| BrainBench (EEG) | 2026 | 指令条件 EEG 分析；4 个子集、17 个数据集、逾 10 万次执行 | 综合 EEG 理解 | 数值/类别/集合/序列/语义/产物校验（CodeAct + BrainAgent） | [→](../works/brainbench-eeg.md) |
| Rodent-Bench | 2026 | 跨范式的啮齿类行为视频（10–35 分钟）；3 个 MLLM | 行为神经科学视频标注 | 逐秒准确率、宏 F1、mAP、互信息、MCC | [→](../works/rodent-bench.md) |
| CPsyExam | 2024 | 4,000 道题（取自 22,000 题库）；知识 + 案例分析两轴 | 心理学考试知识 | 跨学科与两轴的准确率 | [→](../works/cpsyexam.md) |
| ConceptPsy | 2023 | 12 个学科、1,383 个概念；标注到章节 | 概念级心理学知识 | 总体加章节级（逐概念）准确率 | [→](../works/conceptpsy.md) |
| PsychCounsel-Bench | 2025 | 约 2,252 道美国咨询师认证题 | 专业咨询心理学 | 对照约 70% 及格线的准确率 | [→](../works/psychcounsel-bench.md) |
| MLE-bench | 2024 | 75 个精选 Kaggle ML 工程竞赛（OpenAI） | 机器学习工程 | Kaggle 奖牌门槛对照排行榜人类基线 | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | 交互式 Gym 环境中的 200+ Kaggle 挑战 | ML 工程（可训练环境） | 迭代改进、长 horizon 质量、错误修复效率 | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | 13 个 ML 实验任务（CIFAR-10 到 BabyLM） | ML 实验 | 成功率（超基线 >10%）与平均提升 | [→](../works/mlagentbench.md) |
| ML-Bench | 2023 | 18 个 GitHub 仓库上的 9,641 个样例 | 仓库级 ML 代码 | Pass@5（LLM 赛道）与成功率（agent 赛道） | [→](../works/ml-bench.md) |
| DSBench | 2024 | 540 个分析 + 建模任务（多模态、多表） | 数据科学 | 任务解出率与相对性能差距 | [→](../works/dsbench.md) |
| DA-Code | 2024 | 可执行沙箱中的 agent 式数据科学编码 | 数据科学（代码） | 基于执行的准确率；最强 LLM 30.5% | [→](../works/da-code.md) |
| BLADE | 2024 | 12 个配研究问题与专家分析的数据集 | 数据驱动的科学分析 | 对照专家真值为分析决策做多方面评分 | [→](../works/blade.md) |
| MLRC-Bench | 2025 | 7 个 ML 研究竞赛任务 | ML 研究（新颖方法） | 相对顶尖人类的差距缩小（客观）；最佳 9.3% | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | 来自研究仓库的 45 端到端 + 152 子 + 602 自动 | 研究复现 | 端到端与场景成功率；GPT-4o 端到端 16.3% | [→](../works/super.md) |
| MLR-Bench | 2025 | 201 个开放式 ML 研究任务（workshop） | 全流程 ML 研究 | MLR-Judge（LLM 评审 + 评分标准）；约 80% 编造结果 | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | 7 个研究工程环境对照 61 位人类专家 | AI R&D / 研究工程 | 时间预算下对照参考的 best-of-k；与人类直接对照 | [→](../works/re-bench.md) |
| MLGym | 2025 | Gym 中的 13 个开放式 AI 研究任务（Meta） | 开放式 AI 研究 | 五个前沿模型在 Gym 中的任务表现 | [→](../works/mlgym.md) |
| ResearchCodeBench | 2025 | 实现 2024–25 论文贡献的 212 个挑战 | ML 研究代码实现 | 带污染控制的成功率；最佳 37.3% | [→](../works/researchcodebench.md) |
| IdeaBench | 2024 | 以有影响力论文为依据的研究想法生成 | 研究构思 | 两阶段 GPT-4o 排序 + 相对 Insight Score | [→](../works/ideabench.md) |
| LiveIdeaBench | 2024 | 单关键词构思；1,180 关键词、22 领域、40+ 模型 | 科学想法生成 | LLM 面板按五个创造力维度评分 | [→](../works/liveideabench.md) |
| DevAI / Agent-as-a-Judge | 2024 | 55 个 AI 开发任务、365 个层级化需求 | 自动化 AI 开发 | 需求级、过程级的 Agent-as-a-Judge 评估 | [→](../works/devai.md) |
| A Case Study on a Neuroscience Data-to-Discovery Pipeline | 2026 | 真实果蝇光遗传学流水线，分解为 7 个阶段（发布 9 个任务） | 神经科学（果蝇行为分析） | 专家定义的逐阶段判据，对照人类标注与既有代码；统计阶段用 Mann–Whitney U | [→](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| DSAgentBench | 2026 | 真实计算机环境中覆盖完整数据科学生命周期的 275 个任务 | 数据科学（整理 → 建模 → 验证） | 对分析正确性、可视化输出与模型性能的确定性逐任务评估器 | [→](../works/dsagentbench.md) |
| SciVisAgentBench | 2026 | 108 个专家精心设计的科学可视化案例（四维分类法） | 横跨 7 个科学领域的科学可视化 | 以结果为中心的多模态管线：图像指标 + 代码/规则验证器 + 经人类验证的 LLM judge | [→](../works/scivisagentbench.md) |
| TCS-Bench | 2026 | 取自 FOCS/STOC/SODA 论文（2020–2026）的 300 个定理证明任务 | 理论计算机科学 / 数学（证明生成） | 自动验证 agent（4× Gemini 3.1 Flash，四取三表决）；>90% 专家一致 | [→](../works/tcs-bench.md) |
| Science Edge Evaluation (SEE) | 2026 | 取自文献与一手实验数据的 1,116 个专家整理多模态问题 | 化学、生物、材料科学 | 对照专家真值的精确匹配 / 容差评分；严格二元 LLM judge | [→](../works/science-edge-evaluation.md) |
| Fisher-R1 / P-Bench | 2026 | 从专家分析复现的 425 个假设检验任务 | 经济学、生物、医学（统计推断） | 决策与 p 值对照已记录参考代码执行检查（Raw / Strict） | [→](../works/fisher-r1.md) |
| EnergyBridge | 2026 | 基于分地区 EnergyPlus 模型的住宅 VPP 需求响应工作流 | 能源系统（住户电网灵活性） | 计量的 EnergyPlus 结果：授权率 + ±20% 内的容量承诺可靠性 | [→](../works/energybridge.md) |
| PDAgent-Bench | 2026 | 取自真实工业 EDA 产物的 353 道精选任务 + 10 个全流程设计 | VLSI 物理设计 / EDA | pass@1/@5，配经执行检查的脚本与专家参考；全流程时序收敛 / DRC 结果 | [→](../works/pdagent-bench.md) |
| MiraMind | 2025 | 13 个心理健康数据集上的六类任务 | 心理健康 / 精神病学（医学与健康；神经科学与认知科学） | 逐类结果指标加经人类验证的 LLM 判分推理轨迹评分 | [→](../works/miramind.md) |
| CeProBench | 2026 | 6 类任务（243 道题 / 235 项任务），取自 70 份技术文档、113 张源自竞赛的 PFD 与 20 个 Aspen Plus 参数文件 | 化工过程开发：知识、概念（PFD）、参数 | 参数任务在 Aspen Plus 中实际执行；实体 F1 与 MEC/MED、设备与连接准确率、Valid / Correct Rate；以及经评判的 Correctness / Rationality / Clarity / Completeness | [→](../works/ceprobench.md) |
| Simona | 2026 | 1,000 段由化学工程专家撰写的工艺描述 | 化工过程仿真：从描述到能够收敛的流程图 | 自研仿真器中的仿真收敛率，加上设计耗时，对照 LLM、多 agent 与人类专家基线 | [→](../works/simona.md) |
| CRAFTS | 2026 | OpenIDAES-450：450 条请求各配一个可执行的 IDAES 模型，其中 82 条冻结为留出集 | 化工过程仿真（IDAES/Pyomo 面向方程的流程建模） | Staged Workflow Success 契约，由确定性的 IDAES/Pyomo 晋级关卡把关；另计单元、物流与有向连接的宏平均 F1 | [→](../works/crafts.md) |
| A Tutorial on Autonomous Fault-Tolerant Control | 2026 | 两个公开发布的可执行环境（间歇式混合模块、CSTR），支持按类型注入故障 | 过程装置的故障恢复与监督控制 | 逐条方案做符号验证（状态可达性、执行器存在性），并在数字孪生中做仿真验证；未报告模型得分 | [→](../works/ctrl-alt-recover.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | 五个过程装置场景（其中三个取自 Tennessee Eastman Process），外加 43 个人工构造的无效方案 | 工业过程控制与功能安全 | 对每个被提出的动作做确定性 P&ID 图遍历（位号存在性、可执行性、失效状态、下游影响）；错误注入召回率、N = 50 次鲁棒性运行、B0–B3 上下文阶梯 | [→](../works/aae-framework.md) |
| PSE-Bench | 2026 | 200 道开放式题目，四个过程系统工程领域各 50 道，标准答案与 rubric 均已公开 | 过程系统工程：建模与仿真、优化、面向过程的机器学习、设计 | 五个 LLM 评审组成的集成按七要素 rubric 打分，综合分由 ROUGE / 余弦相似度 / 要素覆盖率合成；并以人类专家校准（rs = 0.416，ICC = 0.793，偏松 +0.85） | [→](../works/pse-bench.md) |
| Can Large Language Models Automate the HAZOP Process? | 2026 | 一张带专家参考的 P&ID 与一条统一提示词，四个多模态 LLM 各运行一次 | 过程安全：HAZOP 危险识别 | 对照专家参考计算每份工作表的相似度（F1）与成本，并与场景有效性、防护措施多样性分开评分 | [→](../works/can-large-language-models-automate-the-hazop-proce.md) |
| ChemEBench | 2025 | 三个递进层级、15 个维度下的 101 项化学工程任务 | 化学工程：基础知识、分子层面任务、专业工程技能 | 客观题按准确率计分；主观题按完整性 / 清晰度给 0–5 分 rubric，并逐步核查推理链；14 个模型横向对比 | [→](../works/chemebench.md) |
| ERI Benchmark | 2026 | 57,750 条生成记录，由 9 个工程领域、55 个子领域、7 类意图、3 个难度层级受控交叉组合而成 | 工程推理与指令遵循（化学工程为九个领域之一） | 底层是自动化输出检查，其上是 rubric 层，由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）；115,962 次评判取 1–5 分均值 | [→](../works/eri-benchmark.md) |
| PEOA | 2024 | MathComp（8,500+ 组）与 ChemProc（7,000+ 组），取材自学术文献与教科书 | 结合数学建模与数值方法的化工与过程工程问题求解 | 分阶段的工具学习指标（规划，工具选择的 Recall/NDCG/COMP@K，工具调用，BLEU/ROUGE-L/EM），外加一项八维度的人工评测 | [→](../works/peoa.md) |
| Using Large Language Models for Solving Thermodynamic Problems | 2025 | 22 道由作者自行编写的题目（13 道简单、9 道进阶），每个模型各作答三次 | 化工热力学 | 由受过训练的人类专家按考试方式阅卷，每正确完成一步计 0.5 分；并考察多次作答之间的答案一致性 | [→](../works/llm-thermodynamics.md) |
| LLM-Empowered Agent for Reliable and Robust Structural Analysis | 2026 | 8 道作者构造的静定梁题目（2 种梁型 × 4 种荷载工况），外加 3 项延伸的泛化任务 | 结构分析：静力平衡下的支座反力 | 同一条提示词独立跑 500 次得出的可靠性，以及按 1 m 间隔移动荷载所得的鲁棒性 = (1 + CV)⁻¹；生成的 OpenSeesPy 代码自动执行 | [→](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| Lightweight Multi-Agent System for 2D Frame Structural Analysis | 2025 | 20 个作者设计的二维建筑框架，拓扑抽象自真实建筑，层数轮廓则由抽样得到 | 结构分析：平面框架的有限元建模 | 每题独立跑 10 次中正确生成 OpenSeesPy 程序的比例，并按错误来源（节点/单元/支座/材料）分类 | [→](../works/a-lightweight-large-language-model-based-multi-age.md) |
| Agentic LLMs for Automated Structural Analysis of 3D Frame Systems | 2026 | 10 个由轴网与层数矩阵设定的不规则三维框架体系 | 结构分析：SAP2000 中的三维建筑框架建模 | 全部受监测结构响应相对人工搭建的 SAP2000 真值模型误差均在 1% 以内，每题跑 10 次 | [→](../works/agentic-large-language-models-for-automated-struct.md) |
| Integrating LLMs for Automated Structural Analysis | 2025 | 20 道手工设计的二维框架结构分析应用题，附真值简图 | 结构分析：二维框架的变形与内力 | 四个基础模型上三取优的正确率，外加一项五次运行的生成稳定性研究；OpenSeesPy 执行与专家撰写指令的消融 | [→](../works/integrating-large-language-models-for-automated-st.md) |
| MASSE | 2025 | 100 道题目，由不列颠哥伦比亚省真实货架系统项目记录重组而成，配专家校验的真值 | 结构工程工作流：分析、设计、荷载转换与端到端执行 | GPT-5 评审通读完整分析日志，对照专家真值按四套明确的计分 rubric（SAAB / SDAB / LAB / MASEB）打分，并报告 token 用量与耗时 | [→](../works/masse.md) |
| AutoBM / BMEval | 2026 | 128 个在建筑属性空间中生成、经专家校验的建筑样本，附经验公式给出的参考周期 | 自动建筑建模：由结构规格生成 OpenSeesPy 代码 | 沙箱执行的 pass@k，加上一阶周期相对误差在 0.30 以内以及明确的设计规范符合性结论；Pass@k_strict 把三者合取 | [→](../works/autobm.md) |
| PE Civil Bench | 2026 | 150 道由执业工程师整理的 FE / PE 型资格考试题目，外加 33 个以 ETABS 为参照的梁设计算例 | 覆盖八个子学科的土木工程；钢筋混凝土构件设计 | 基础提示 / 向量 RAG / agentic RAG 三种方式下的答案正确率；设计赛道与 ETABS 有限元输出做相关性检验（r ≥ 0.90） | [→](../works/pe-civil-bench.md) |
| DrafterBench | 2025 | 1,920 个任务，归纳自设计与施工企业提供的 100 多份真实修改文件 | 土木工程技术图纸修改 | 两级自动评分（代码可执行性 + 目标完成度），并把操作链与参考链做交并比 | [→](../works/drafterbench.md) |
| AECBench | 2026 | 4,800 道中文题目，覆盖 23 类任务，由领域工程师编写并取材于执业资格考试 | 建筑、工程与施工知识，横跨五个认知层级 | 客观题计准确率；开放题由 LLM 评审对照专家预设 rubric 打分，并按专家评分重新校准（MAE 2.947 → 约 1.93–2.02） | [→](../works/aecbench.md) |
| AEC-Bench | 2026 | 196 个任务实例，取自公共部门项目公开可得的施工文档集 | 施工文档工作：详图审查、交叉对照、说明书–图纸一致性核对、报审资料审查 | 任务专用的自动验证器在 Docker 化沙箱中评阅结构化的 JSONL 审查发现，给出分级部分分；不使用 LLM 评审 | [→](../works/aec-bench.md) |
| SGR-BIM | 2026 | 五个 IFC 建筑模型上的 679 条经专家核验的消防安全合规查询 | BIM 模型上几何密集的建筑规范符合性校核 | 人工评定的三档准确率——未指明起决定作用的变量与边界条件即不给满分——外加匿名 LLM 评判的连贯性 / 相关性 / 可解释性，并经人工审核 | [→](../works/sgr-bim.md) |
| SoM-1K | 2025 | 1,065 道取自大学教材与力学竞赛的题目，每道附专家撰写的图示文字描述 | 材料力学 | 由专家逐份人工评阅推理有效性与最终答案，取五次采样的多数表决 | [→](../works/som-1k.md) |
| EngDesign | 2025 | 101 个真实工程设计任务，横跨九个领域，共含 473 个可评分项 | 工程设计，含 13 个结构设计任务 | 领域仿真器（MATLAB、SPICE/Cadence、有限元分析、拓扑优化）返回二值通过/不通过，另加 0–100 的部分分 | [→](../works/engdesign.md) |
| MMArch | 2026 | 1,212 道题目，取材于约 10,000 篇同行评审的建筑与土木工程论文素材池中的图件 | 建筑与土木工程十个子领域（多模态） | 对照冻结的 ≤10 token 参考答案计准确率，并做单位 / 同义词 / 容差归一化；以人类专家团作为上界参照 | [→](../works/mmarch.md) |
| Evaluating AI Chatbots on the FE and PE Structural Exams | 2024 | NCEES 官方练习考试中的 79 道 FE 题与 39 道 PE 题 | 土木（FE）与结构（PE）执业资格考试内容 | 对照 NCEES 推荐解答做二值判分，不给部分分也不做曲线调整，按主题领域汇总 | [→](../works/evaluating-the-performance-of-artificial-intellige.md) |
| Civil-Eval | 2026 | 中国国家注册考试 2024 年 5 月场次的 517 道客观题 | 覆盖 8 个考试科目的土木与交通工程知识 | 忠实于考试规则的选项计分（多选题要求选项集合完全一致），科目权重按难题占比设定 | [→](../works/civil-eval.md) |
| DefectBench | 2026 | 487 个基准样本，由 12 个建筑缺陷数据集在统一的四类本体下整合而成 | 建筑外墙结构病害：语义感知、空间定位、生成式分割 | 对照专家核验标注的分级指标族（F1 / MAE、mAP50-95、mIoU），采用零样本多轮协议 | [→](../works/defectbench.md) |
| Cognitive Agents for Bridge Inspection Prioritization | 2026 | FHWA 全国桥梁清单的六个年度版本（2020–2025），筛出 3,389 座康涅狄格州桥梁作为分析样本 | 公路桥梁检测优先级排序 | 对照观测到的持续劣化，在三种结果定义下计算 AUC / 平均精度 / precision@300；另请持证桥梁检测员对 100 段理由做 0–3 分盲评 | [→](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) |
| Toward Responsible AI in High-Stakes Domains | 2025 | 四个钢筋混凝土建筑框架，每个在四种计算分组下分析 | 钢筋混凝土建筑框架的结构静力分析 | 层间位移角、最大位移、基底剪力与周期相对人工搭建的 ETABS 参考模型的相对误差 | [→](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) |
| TransportBench | 2024 | 140 道题目，取自伊利诺伊大学两门开设多年的交通工程课程 | 交通工程：规划、设计、管理与控制 | 由人类专家同时评阅答案与推理；重复试验的 Mixed Response Rate，以及自查式追问下的答案稳定性 | [→](../works/transportbench.md) |
| BridgeEQA | 2025 | 2,200 个问答对，抽取自佛蒙特州交通厅在 200 个真实桥梁场景上的检测报告 | 桥梁检测的具身问答 | LLM 评判的答案正确率，NBI 状况评级的精确命中率与 ±1 容差命中率，以及 Image Citation Relevance（与人工标注 Spearman 0.817） | [→](../works/bridgeeqa.md) |
| LLM-EPANET | 2025 | 69 条精选的自然语言查询，覆盖 Net1、Net3 与 L-Town，分五个复杂度类别 | 供水管网建模（EPANET / EPyT） | 与预先写好并执行过的确定性参考脚本做功能等价判定，边界情形由专家裁定 | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | 4,000 道中文选择题，取自教材、行业标准、法律法规与统计年鉴 | 水科学与水利工程九个子领域 | 温度取 0 时的准确率，由另一个 LLM 抽取最终选项，并按子领域、题型与认知层级分别报告 | [→](../works/hydro-se-bench.md) |
| LLM-Based Multi-Agent Systems for Automated Foundation Design | 2026 | 27 个作者定义的基础设计算例（15 个浅基础、12 个桩基），分七类 | 岩土工程：浅基础与桩基础设计 | 四项判据、四级评分——计算准确性、思维链推理、复杂场景处理、输出结构——每个算例跑三次 | [→](../works/large-language-model-based-multi-agent-systems-for.md) |
| CEQuest | 2025 | 164 道题目，由领域专家依据造价估算教材与图纸解读指南编写 | 施工图纸解读与造价估算 | 按答案精确匹配评分，重复五次运行并以均值 ± 标准差报告，同时给出评测耗时与模型规模 | [→](../works/cequest.md) |
| Automating Structural Reliability Analysis with a Multi-Agent LLM Framework | 2026 | 20 道手工编写的构件级可靠度题目，与微调集不相交 | 结构可靠度分析：可靠指标与失效概率 | β 与 P_f 只由确定性地执行经验证求解器得出，并与蒙特卡洛 / 子集模拟参考解对照；方法类别准确率对照确定性打标规则 | [→](../works/automating-structural-reliability-analysis-with-a.md) |
| TRIP-Evaluate | 2026 | 837 道单选题（文本 596、图像 198、点云 43），按「角色–任务–知识」分类体系组织 | 交通工程，含一个规划与设计角色 | 固定提示词与解码设置下的单字母准确率，按角色、任务域、能力、难度与模态分别报告 | [→](../works/trip-evaluate.md) |
| AstroVisBench | 2025 | 从 110 份 Astro Data Lab 与 STScI 教程 notebook 中抽取的 432 个处理任务与 432 个可视化任务 | 天文：巡天与任务数据的处理，以及传达其科学洞见的可视化 | 对照标准答案内存变量的 Variable Inspection Score，外加一个把图判为 No / Minor / Major 三档错误的视觉语言 judge——该 judge 依据与五位职业天文学家面板的相关性（ρ = 0.822）选出 | [→](../works/astrovisbench.md) |
| Spec-o3 / SpecVI-Bench | 2026 | 五项稀有天体任务，正样本取自 LAMOST 星表，易混淆负样本经拒绝采样得到（测试集 1,122 / 5,632 条） | 天文：稀有天体的光谱甄别（激变变星、碳星、S 型星、M 型巨星、白矮星） | 在刻意保持不均衡的测试集上计算宏平均准确率与正类 F1，另有留出的 LAMOST → SDSS/DESI 巡天迁移划分，以及六位天文学家依公开的 0–5 分 rubric 为 100 条推理轨迹打分 | [→](../works/spec-o3.md) |
| AstroAlertBench | 2026 | 取自 ALeRCE stamp-classifier 数据集的 1,500 条真实 ZTF 警报，五类各 300 条保持均衡 | 天文：时域警报审核，覆盖伪源、小行星、超新星、AGN 与变星 | 在元数据落地、结构化论证与层级分类上报告逐阶段与端到端准确率，另加一条比对自我评估与实际正确率的诚实度轴；人类集成基线为 30.67 ± 5.32% | [→](../works/astroalertbench.md) |
| Plausible but Wrong | 2026 | 取自 CMBAgent 仓库的 14 个 CAMB 计算任务，外加 4 个基于 Union2.1、SPARC、NASA Exoplanet Archive 与 SLACS 数据的研究任务 | 天体物理：Boltzmann 求解器计算、超新星宇宙学、转动曲线、系外行星族群、强引力透镜 | Execution Success Rate、Parameter Accuracy Score 与 Numerical Accuracy Score，后两者以 PAS × NAS 合成；四类失败模式由这几项分数上的阈值界定 | [→](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | 一份七阶段引力波流程规格说明，在同一硬件上自主执行四次（两个 agent × 两轮） | 天文：从模拟 Einstein Telescope 应变中恢复双黑洞信号 | 科学输出（模板库规模、探测效率、恢复的 SNR）与从日志中数出的行为测度——重启、静默偏离、自我纠正、未经要求的优化——并列报告，另附运行时间与峰值内存 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| CosmoPaperQA | 2025 | 由宇宙学专家依据五篇高引宇宙学论文撰写的 105 组问答对 | 天文：宇宙学文献问答，分事实、综合与分析三个层级 | 全部 945 条回答（9 种 RAG 配置 × 105 题）由一位博士级宇宙学家逐条二元手工评分，并用于校准两个 LLM judge；二者保持系统排序一致，Pearson r > 0.99 | [→](../works/cosmopaperqa.md) |
| Enhancing Agentic Autonomous Scientific Discovery with VLM Capabilities | 2025 | 10 个由作者生成的数据驱动发现任务（宇宙学功率谱、分子谱线、振子、SEIR） | 以天文为主的数据驱动模型发现 | 以还原出正确底层模型的 pass@1 计分，回路内的视觉语言绘图 judge 依逐任务生成的 rubric 评图；纯代码为 0.2–0.3，加入 VLM 反馈后为 0.7–0.8 | [→](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| Mephisto | 2025 | 256 个经光谱证认的 COSMOS2020 星系，在四维物理参数空间中均匀采样，外加 31 个 JWST 小红点 | 天文：借 CIGALE 由多波段测光解读星系 SED | 产出的模型只要 χ² < 1.2 × 穷举 3.6 亿点 CIGALE 网格搜索所得 χ² 即算通过；同一套流程在七种 LLM 底座上重跑，并对照相对 API 成本 | [→](../works/mephisto.md) |
| gammapyGPT | 2025 | 四项 Gammapy 分析任务，针对经数据指针访问的真实观测数据定义 | 天文：地基伽马射线分析——观测筛选、反射区显著性与能谱、三维源拟合 | 执行生成的脚本，判据按任务难度分级（整数精确匹配、浮点值落在容差内、端到端跑通），并记录验证是在第几次尝试通过的 | [→](../works/gammapygpt.md) |
| VESTA / DAWN | 2026 | 400 个生成实例——200 个分布拟合与 200 个时间序列——各含一个 50 实例的天文切分 | 天文：恒星初始质量函数还原与引力波啁啾建模，另有领域中立的层级 | 拟合任务用与真实分布之间的 Jensen–Shannon 散度，时间序列用 ELPD-LOO，给的是分级得分而非通过/不通过 | [→](../works/vesta-dawn.md) |
| ScienceBoard | 2025 | 在运行六款专业科学软件的真实 Ubuntu 桌面中，169 个人工整理的工作流任务 | 天文由 Celestia 承载，另有生物化学、代数、定理证明、GIS 与科学文档 | 经 HTTP 状态服务器程序化检查中间 I/O 与虚拟机最终状态，给出二元成功判定；总体最好 24.20%（GPT-5），天文属最弱的领域之一 | [→](../works/scienceboard.md) |
| Quantifying the Reproducibility of Astrophysical Methods | 2026 | 一个天体物理案例研究——海王星外天体的概率化光谱重建——在三种层层嵌套的信息状态（Title / + Abstract / + Methods）下提出 | 天文：从描述它的稿件中还原一项计算方法 | 对每个模型在每种状态下采样的 200 次重建计算 Shannon 熵与 Jensen–Shannon 散度，另由人在回路按四级 Hierarchy of Scientific Validity 为可执行流程评分（明示阈值为 V ≥ 2） | [→](../works/quantifying-the-reproducibility-of-astrophysical-m.md) |
| AstroMMBench | 2025 | 621 道四选一题目，图件挖自 3,592 份 arXiv 天文 TeX 源码，由 15 位子领域对口的专家评审从 1,800 道候选中筛留 | 天文：横跨六个 astro-ph 子领域的图件解读 | 经 VLMEvalKit 测得的单轮选择题准确率，在 25 个 MLLM 上报告总体与逐子领域成绩；最佳为 Ovis2-34B，70.53% | [→](../works/astrommbench.md) |
| From Queries to Criteria | 2025 | 从 STScI 为期四周的 `@Ask-astro-ph` 部署所留 368 条查询日志中采样的 40 道题，标准答案由七位天文学家撰写 | 天文：以文献为依据的问答 | 由 LLM 对照专家标准答案生成 0–1 相关性分数，配以针对含糊措辞的认知标记检测和针对引文准确性的蕴含检验；该相关性与真实用户评分的 Pearson 相关为 0.82 | [→](../works/from-queries-to-criteria-understanding-how-astrono.md) |
| AI's Capability in Assisting Scientific Research I: Literature Review | 2026 | 八个由专家设计的前沿研究课题，每个由一位领域专家检索一轮、每个 AI 系统各检索一轮，上限 50 篇论文 | 天文与天体物理文献检索（八个课题中的六个） | 由专家判定重合，且要求标题与所归类别同时吻合；另以 DOI → 链接 → 标题检索的级联，把 641 条仅由 AI 给出的参考文献判为完全正确、元数据不符或凭空编造 | [→](../works/ai-assisting-research-i-literature-review.md) |
| AI's Capability in Assisting Scientific Research II: Project Planning | 2026 | 针对同样八个专家设计课题、按同一模板写成的 32 份一页纸计划书（8 份人类，24 份 AI） | 天文与天体物理的研究规划 | 由四位教师或资深博后与两位 LLM 评审按公开的四方面 rubric 做 1–5 分盲评，另附一项判断作者是人类还是 AI 的识别任务 | [→](../works/ai-assisting-research-ii-project-planning.md) |
| AstroMLab 1 | 2024 | 由 885 篇 *Annual Review of Astronomy and Astrophysics* 文章（1963–2023）生成的 4,425 道四选一题目 | 覆盖六个子领域与五种受测能力的天文知识 | 在 47 个闭源与开放权重模型上报告附 Wilson 得分区间的准确率，并按 astro-ph 语料规模下的推理成本以及置信度-正确率校准做交叉切分 | [→](../works/astromlab-1.md) |
| LLM-IOAA | 2025 | 取自 2022–2025 年完整国际天文与天体物理奥赛理论卷与数据分析卷的 57 道题 | 天文：奥赛级别的推导与真实观测数据分析 | 依官方 IOAA 评分标准人工评阅并按步给分，全部 285 次评定都由前 IOAA 选手与领队评两遍，分数再映射到真实选手分布与奖牌线上 | [→](../works/llm-ioaa.md) |
| DomainCQA / AstroChart | 2025 | 覆盖 arXiv 天文论文中 482 张图的 1,690 组问答对，分为 1,509 道基础题与 181 道依赖知识的推断题 | 天文：把图表理解与依赖知识的图件推断分离开来 | 数值答案用按坐标轴量程归一化的相对误差，推导题用精确匹配，开放式回答由 DeepSeek-V3 judge 评判并经人工标注验证（r = 0.816）；另有四位天文研究者作答 10% 的抽样 | [→](../works/domaincqa.md) |
| ALeRCE Text-to-SQL | 2026 | 从 10 位一线天文学家与 broker 团队处征集的 110 组自然语言/SQL 对，标准查询由专家撰写 | 天文：查询一个 25 表、304 列的在运行 ZTF/Rubin 警报 broker 数据库 | 把预测查询与标准查询都执行一遍、分别比较返回的行与列，据此判 Perfect Match；每条查询运行十次，按 simple / medium / hard 分层，另附逐阶段的 API 成本表 | [→](../works/alerce-text-to-sql.md) |
| SimAgents | 2025 | 来自 arXiv、ApJ 与 MNRAS 的 40 余项已发表宇宙学模拟，对每个与 MP-Gadget 相关的参数逐一人工标注 | 天文：从已发表论文中还原可执行的模拟配置 | 在人工评分与自动评分两种口径下，对照人工标注计算参数级的精确率、召回率与 micro-F1，并把 Value、Type 与 Hallucination 三类错误逐个模拟分别计数 | [→](../works/simagents.md) |
| HiSciBench | 2025 | 六个学科、五个递进层级下七类任务共 8,735 个实例，其中天文贡献 597 个 | 天文文献的解析、翻译、问答与综述生成，另有其余五个学科 | 各层级各有其评测方案：准确率、词级 OCR 准确率、BLEU、带引文可核验性指标的 LLM 评审综述 rubric，以及发现层基于执行的成功率 | [→](../works/hiscibench.md) |
| SciVQR | 2026 | 3,254 道配图题目，取自 15 项竞赛、9 种高考试卷与 6 种大学或研究生考试及教材，并按「离开图就答不出」筛选 | 天文是六个计分学科之一，其下明列六个天文子领域 | 报告用与不用 CoT 提示的零样本准确率，另由 GPT-4o judge 对照专家撰写的解题过程，按五维推理轨迹 rubric 以 10 分制打分 | [→](../works/scivqr.md) |
| Imaging-101 | 2026 | 57 个经专家核验的计算成像任务，每个都以一篇同行评审论文及其开源参考实现为依据 | 六个领域之一是天文成像（EHT 重建、日冕仪系外行星成像、幸运成像、波前探测） | 三条赛道：规划部分由专家逐项二元判定通过与否，函数与模块实现由 pytest 评分，端到端重建则对照各任务 `metrics.json` 中的 NCC / NRMSE 阈值 | [→](../works/imaging-101.md) |
| An LLM-driven framework for cosmological model-building | 2025 | 两个标准答案宇宙学模型（Thawing Quintessence、Early Dark Energy）外加两种假设生成设置，跑在预装 CLASS 3.3.0 的容器中 | 天文：在 Boltzmann 求解器中实现并探索替代性暗能量模型 | 二元的执行里程碑、算得的可观测量相对标准实现的最大相对偏差，以及对照 DESI、Planck、Pantheon+ 与 SH0ES 数据的似然 / BIC / Hubble 张力 / CMB 自洽性奖励 | [→](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| AI Cosplaying as Astrophysicists | 2026 | 公开发布的 3,000 个天体物理任务库，分六个工作流族；2,592 项指派各在五种辅助策略下运行，共 12,960 个回合 | 天文：日常的天体物理研究工作——写作、信息抽取、代码调试、推导、问题求解、评审 | LLM judge 依各族专属 rubric 评分，输出任务分数、完成情况与一条独立的灾难性失败标记，再合成为带置信区间的效用值；另有一次完整的角色互换复现 | [→](../works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md) |
| FlyAOC | 2026 | 100 个 benchmark 基因，配一份公开的 16,898 篇果蝇全文论文语料，以 7,397 条 FlyBase 专家策展为真值 | 生物：果蝇遗传学——Gene Ontology 功能条目、表达模式、历史同义词 | GO 与表达用本体 DAG 上的 Wang 相似度算语义 recall@k，同义词用精确匹配 recall@k，均取微平均；同时报告每个基因的美元成本 | [→](../works/flyaoc.md) |
| Frontier LLM-based agents can overcome the ontology curation bottleneck | 2026 | 原封未动的 Dahdul 等（2018）Gold Standard——取自七项系统发育研究的 203 个性状 / 463 个状态，评分范围为第 51–203 个性状 | 生物：脊椎动物比较形态学，对照 UBERON / PATO / BSPO / GO 的 Entity-Quality 表型注释 | 沿用原来的四项语义相似度指标（SimJ、NIC、partial precision、partial recall），并与 2018 年研究中同样的三位受训人类策展员及同一条 NLP 基线比较 | [→](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md) |
| OntoLearner | 2026 | 覆盖 22 个领域的 180 个机器可读本体，附带可直接接入流水线的 train / dev / test 切分 | 本体学习；其中的科学部分涉及化学、生物、医学、材料科学与环境科学，另有大量非科学领域 | 以归一化的成对与三元组匹配对照金标准本体结构计 precision、recall 与 F1，覆盖 22 个检索模型与 12 个 LLM | [→](../works/ontolearner.md) |
| CASCADE / SciSkillBench | 2025 | 116 个精选研究任务，分数据类（76）与计算类（40），并区分 Level 0 与 Level 1 两种说明详细程度 | 材料科学与化学：数据检索、分析与处理；仿真与专用工具包 | 在预设容差内自动比对处理结果与真值；每种配置重复三次计成功率（共 16,008 次运行），并与无演化基线做消融对照 | [→](../works/cascade.md) |
| MolClaw / MolBench | 2026 | 筛选与优化题目取自 CARA/ChEMBL、ACNet 与 ChemCoTBench，另加三项自行编写的端到端发现挑战 | 化学与医学：分子筛选、分子编辑与性质优化、结构导向的先导化合物优化 | 筛选用 Accuracy 与 Hits@3；优化用操作准确率与性质变化量；端到端一层用任务专属的加权 rubric，对调用顺序、参数一致性与终止条件分别给分 | [→](../works/molclaw.md) |
| LQCDMaster | 2026 | 70 个格点 QCD 计算任务，每个都配一份专家手写的参考实现，可观测量、系综与运动学设置均与之相同 | 物理：格点 QCD——定域与非定域两点函数、介子与重子三点函数、Wilson 环 | 在机器精度上与专家参考直接做数值比对（绝对偏差 ≲ 10⁻¹²），标为 Matched / Convention Mismatch / Failure，并按可观测量族分别报告 | [→](../works/lqcdmaster.md) |
| BiomedSQL | 2025 | 由 40 条专家编写的种子查询扩展出的 68,000 组 question / SQL / answer 三元组，落在一个十张表的 BigQuery 库上；在 546 道题的测试集上评分 | 生物与医学：神经退行性疾病遗传学（GWAS、SMR、等位基因频率）与药物靶点、适应证及审批状态 | 对照金标准执行结果计 Execution Accuracy，含 Jaccard 部分得分与语法错误率；应答质量与安全性由 LLM 评判；双分析师人类基线的 EX 为 90.0% | [→](../works/biomedsql.md) |
| AISE-Bench | 2026 | 1,133 组 QA，端到端标注了查询分类、计划、实际执行的 API 调用、经校验的参数与参考答案；其中 250 组经双人复核 | 面向学术知识图谱的学术信息检索，覆盖各一级学科——论文、作者、发表场所、机构 | 引用的 precision / recall 与格式合规性；计划的图编辑距离、参数准确率与执行成功率；答案的正确性、完整性、忠实度与 F1-LM | [→](../works/aise-bench.md) |
| RubricsTree | 2026 | 由医生主导、参考约 4,000 条真实用户查询做的人在环中策展；532 条查询的内部元评估集，外加 HealthBench-Hard | 医学与健康：医学解释、健康数据解读、建议与行动规划、症状处理 | 100 多条原子布尔叶节点 rubric 组成分层 DAG，由上下文感知路由器按查询激活；与专家组的一致性为 ICC₃ = 0.876、Cohen's κ = 0.787 | [→](../works/rubricstree.md) |
| Replica | 2026 | 100 篇 ML 与 AI for science 论文（1990–2026），每个任务从 PDF 中不可逆地抹去一张结果图 | 复现一项已发表的机器学习或 AI for science 结果 | 自动生成的五维 rubric 评判器；两次评判采样之间一致性 τ = 0.66，而两位人类之间只有 τ = 0.30 | [→](../works/replica.md) |
| AutoResearchEval | 2026 | 从 5,878 个候选中筛出 100 个任务，取材于七个领域的已发表前沿科学 | 完整研究生命周期，从构思到自我复查 | agent-as-a-judge 通读完整轨迹与中间产物，对照人工标注在模式层面 κ = 0.75、分类体系层面 κ = 0.83 | [→](../works/autoresearcheval.md) |
| PACE-Bench | 2026 | 36 份手工构建的 Box2D 设计，变异出 144 个源到目标的适配对 | 六个物理族，从静力学、运动学到控制与颗粒流 | 刚体仿真；约束满足比例与 [−100, 100] 区间的任务分数，报告为 Pass@2 | [→](../works/pace-bench.md) |
| Apodex Discovery | 2026 | 覆盖 561 个行业的调研识别出 423 个候选，从中选出 20 个问题 | 十个工业与科学领域，从衣壳设计到芯片验证 | 可执行环境内的隐藏验证器，外加盲评的六维过程打分（与结果的 Spearman ρ = +0.51） | [→](../works/apodex-discovery.md) |
| AutoWorldModel-Bench | 2026 | 八个游戏环境 × 四种基础世界模型架构，共 64 个会话 | 不指定改进方向的自主世界模型研究 | 留出集上 Position L1 与 Alive F1 在 1/10/20 三个时程上的组合，权重 0.1/0.2/0.7 | [→](../works/autoworldmodel-bench.md) |
| Agents Catching Agents | 2026 | 六个公开临床数据集上的七个 cohort，覆盖文本、影像与表格记录 | 捷径线索下临床多 agent 委员会的效度 | 捷径采纳率对照孤立条件下的翻转率；三种监督检测器以精确率、召回率与假阳性率计分 | [→](../works/agents-catching-agents.md) |
| ASI-Bench | 2026 | 取自文献的 60 个项目级任务（1,300+ 候选想法、40+ 专家、31,000+ 人时） | 11 个科学领域，四个指导层级下的项目级研究 | 逐任务的评估门与加权打分器，对照可复现的逐任务参考；B1–B4 指导梯度，B3/B4 平均分低于 40 | [→](../works/asi-bench.md) |

## 还没解决的问题

- **正确性的参照标准。** 科学任务允许多种合理的参照标准——已发表 SOTA（NatureBench）、专家分类（MedHELM）、可执行验证（Terminal-Bench Science）、与传统方法对比（SimulCost）。跨 benchmark 比较时，哪一种应成为标准？
- **发现 vs. 复现。** NatureBench 明确区分「匹敌 SOTA」与「真正的方法论创新」。评分指标该如何操作化「发现」？
- **成本作为评估维度。** 科学工作流有真实 tool-use 成本（仿真时间、实验资源）。scientific-agent topic 是否应像 SimulCost 那样把成本作为强制维度？
- **广度 vs. 深度。** 跨学科 benchmark（NatureBench、AIRS-Bench、MedHELM）给出广度；单仿真器 / 单领域 benchmark 给出深度。哪一种更适合作为主要评估面？
- **Judge 可靠性。** MedHELM 报告的 LLM-jury 与医生一致性为 ICC = 0.47。这是否是其他使用 LLM-judge 评分的科学领域 benchmark 应报告的下限？多少才算充分？

## 相关工作

- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [FlyAOC](../works/flyaoc.md)
- [Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md)
- [OntoLearner](../works/ontolearner.md)
- [CASCADE](../works/cascade.md)
- [MolClaw](../works/molclaw.md)
- [LQCDMaster](../works/lqcdmaster.md)
- [BiomedSQL](../works/biomedsql.md)
- [AISE-Bench](../works/aise-bench.md)
- [RubricsTree](../works/rubricstree.md)
- [AstroVisBench](../works/astrovisbench.md)
- [Spec-o3](../works/spec-o3.md)
- [AstroAlertBench](../works/astroalertbench.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [CosmoPaperQA](../works/cosmopaperqa.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [Mephisto](../works/mephisto.md)
- [gammapyGPT](../works/gammapygpt.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
- [ScienceBoard](../works/scienceboard.md)
- [Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory](../works/quantifying-the-reproducibility-of-astrophysical-m.md)
- [AstroMMBench](../works/astrommbench.md)
- [From Queries to Criteria: Understanding How Astronomers Evaluate LLMs](../works/from-queries-to-criteria-understanding-how-astrono.md)
- [AI's Capability in Assisting Scientific Research I: Literature Review](../works/ai-assisting-research-i-literature-review.md)
- [AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation](../works/ai-assisting-research-ii-project-planning.md)
- [AstroMLab 1](../works/astromlab-1.md)
- [LLM-IOAA](../works/llm-ioaa.md)
- [DomainCQA / AstroChart](../works/domaincqa.md)
- [ALeRCE Text-to-SQL](../works/alerce-text-to-sql.md)
- [SimAgents](../works/simagents.md)
- [HiSciBench](../works/hiscibench.md)
- [SciVQR](../works/scivqr.md)
- [Imaging-101](../works/imaging-101.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [AI Cosplaying as Astrophysicists: A Controlled Synthetic-Agent Study of AI-Assisted Astrophysical Research Workflows](../works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [MASSE](../works/masse.md)
- [AutoBM / BMEval](../works/autobm.md)
- [PE Civil Bench](../works/pe-civil-bench.md)
- [DrafterBench](../works/drafterbench.md)
- [AECBench](../works/aecbench.md)
- [AEC-Bench](../works/aec-bench.md)
- [SGR-BIM](../works/sgr-bim.md)
- [SoM-1K](../works/som-1k.md)
- [EngDesign](../works/engdesign.md)
- [MMArch](../works/mmarch.md)
- [Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md)
- [Civil-Eval](../works/civil-eval.md)
- [DefectBench](../works/defectbench.md)
- [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md)
- [Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)
- [TransportBench](../works/transportbench.md)
- [BridgeEQA](../works/bridgeeqa.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [Large Language Model-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md)
- [CEQuest](../works/cequest.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [TRIP-Evaluate](../works/trip-evaluate.md)
- [CeProBench](../works/ceprobench.md)
- [Simona](../works/simona.md)
- [CRAFTS](../works/crafts.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [PSE-Bench](../works/pse-bench.md)
- [Can Large Language Models Automate the HAZOP Process Without Human Intervention?](../works/can-large-language-models-automate-the-hazop-proce.md)
- [ChemEBench](../works/chemebench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [PEOA](../works/peoa.md)
- [Using Large Language Models for Solving Thermodynamic Problems](../works/llm-thermodynamics.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [TCS-Bench](../works/tcs-bench.md)
- [MiraMind](../works/miramind.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [DSAgentBench](../works/dsagentbench.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [EnergyBridge](../works/energybridge.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
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
- [Model Discovery Agent](../works/model-discovery-agent.md)
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
- [LabRobFail](../works/labrobfail.md)
- [MaScQA](../works/mascqa.md)
- [MatSciBench](../works/matscibench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatText](../works/mattext.md)
- [AtomWorld](../works/atomworld.md)
- [OpenXRD](../works/openxrd.md)
- [MatVQA](../works/matvqa.md)
- [MatCha](../works/matcha.md)
- [MatQnA](../works/matqna.md)
- [MatViX](../works/matvix.md)
- [MatTools](../works/mattools.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [AlchemyBench](../works/alchemybench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [VerilogEval](../works/verilogeval.md)
- [RTLLM](../works/rtllm.md)
- [RTL-Repo](../works/rtl-repo.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [CVDP](../works/cvdp.md)
- [AssertionBench](../works/assertionbench.md)
- [FVEval](../works/fveval.md)
- [HLS-Eval](../works/hls-eval.md)
- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [EEE-Bench](../works/eee-bench.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [TeleQnA](../works/teleqna.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [ElecBench](../works/elecbench.md)
- [BrainBench (EEG)](../works/brainbench-eeg.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [CPsyExam](../works/cpsyexam.md)
- [ConceptPsy](../works/conceptpsy.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
- [MLE-bench](../works/mle-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLAgentBench](../works/mlagentbench.md)
- [ML-Bench](../works/ml-bench.md)
- [DSBench](../works/dsbench.md)
- [DA-Code](../works/da-code.md)
- [BLADE](../works/blade.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [SUPER](../works/super.md)
- [MLR-Bench](../works/mlr-bench.md)
- [RE-Bench](../works/re-bench.md)
- [MLGym](../works/mlgym.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [IdeaBench](../works/ideabench.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [Replica](../works/replica.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [PACE-Bench](../works/pace-bench.md)
- [Apodex Discovery](../works/apodex-discovery.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
- [Agents Catching Agents](../works/agents-catching-agents.md)
- [ASI-Bench](../works/asi-bench.md)

## 延伸阅读

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
