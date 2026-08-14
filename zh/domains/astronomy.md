# Astronomy

> [English](../../domains/astronomy.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

天文学与天体物理——即以天体、观测或宇宙学模型为评分目标的评测。本页收录的工作涵盖：从真实观测数据出发的推断（径向速度系外行星拟合、由多波段测光对星系做光谱能量分布建模、LAMOST 光谱中的稀有天体甄别、ZTF 暂现源警报分类、地基伽马射线源分析）；宇宙学，从 CLASS 与 CAMB 中的 Boltzmann 求解器计算与暗能量模型实现，到已发表宇宙学模拟的参数配置；引力波源科学，包括在模拟 Einstein Telescope 数据上的模板库搜索，以及波形与并合遗迹建模；面向巡天与任务档案的天文科学计算与可视化，以及对在运行的警报 broker 数据库的查询；已发表天体物理方法与论文的复现与可重复性，连同其周边的研究工作流（文献检索、课题规划、辅助分析）；还有天文知识与图件解读，从奥赛试题、综述文献题集，到取自论文的图表、图像与光谱问答。若干跨领域套件之所以出现在这里，是因为它们自己点明并单独报告了可辨识的天文切片。

有两条边界需要说明。与 **Physics** 的分界看的是研究对象，而不是用到了哪些方程：引力、场论、探测器响应与波形物理若是作为自身课题来研究，仍留在 Physics；没有观测依托的理论宇宙学推导按理论物理处理。一项工作只要其受评目标是一项天文测量、一个天体源，或一个要与数据对照检验的宇宙学模型，就归入本页。横跨两者的工作在两页同时列出。与 **Earth Science** 的分界则落在日地系统上：日球物理、空间天气及其对地球的影响归 Earth Science，GIS 与地理空间分析同样如此；而作为天文学科的太阳与恒星天体物理归本页。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Stargazer | 2026 | 从径向速度时间序列推断系外行星系统：提出能解释观测恒星信号的行星数量与轨道参数，并基于逐项反馈迭代。 | 120 个模型拟合任务——100 个合成任务分三个难度层，另有 20 个来自 NASA Exoplanet Archive 与 VizieR 的真实档案系统，行星数 1–7。 | 四项物理判据须同时满足：残差 RMS ≤ 1.5× 测量不确定度、相对常数零模型的 ΔBIC 为正、匈牙利算法匹配的行星恢复 ≥ 0.8、行星数完全正确。 | [→](../works/stargazer.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的天文任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Astronomy 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| gwBenchmarks | 2026 | 以引力波科学实际要求的精度建模引力波源：数值相对论波形代理模型、黑洞轨道动力学、并合遗迹、模板库。 | 8 个任务，底层数据代表 10⁸ 核时以上的计算；12 个 coding agent 受评。 | 外部预定义评估框架配单任务物理指标，对照 ≲10⁻⁴ 的相对误差领域要求。 | [→](../works/gwbenchmarks.md) |
| ReplicationBench | 2025 | 复现天体物理研究论文的核心贡献：实验设置、推导、数据分析与代码库。 | 111 个复现任务覆盖 20 篇论文（官方仓库），与原作者共同开发，在计算沙箱中运行。 | 逐任务客观评分：对原方法的忠实性与结果的正确性。 | [→](../works/replicationbench.md) |
| SciVisAgentBench | 2026 | 天文数据的科学可视化与数据分析——其七个应用领域之一——把自然语言意图翻译为对标量/矢量/张量场及时变场的可执行可视化操作。 | 108 个专家精心设计的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，通过 CLI、MCP 服务器与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态管线，结合一个 MLLM judge（报告为 Claude-Opus-4.6；与人类评分 Pearson 0.808）与确定性评估器——图像指标（PSNR、SSIM、LPIPS）、代码检查器，以及基于规则/逐案例的验证器。 | [→](../works/scivisagentbench.md) |
| Mephisto | 2025 | 驱动 CIGALE 光谱能量分布代码，从多波段测光反推真实观测星系的物理性质——恒星质量、恒星形成率、尘埃消光、红移、AGN 贡献。 | 256 个 COSMOS2020 星系，按红移、恒星质量、尘埃消光与恒星形成率均匀采样，另加 31 个 JWST/JADES「小红点」天体；七种 LLM 底座都在完整的 256 星系集上运行。 | 当且仅当 agent 给出某个 χ² < 1.2 × 穷举 3.6 亿点 CIGALE 网格搜索所得 χ² 的 SED 模型时才算通过；推断出的恒星质量另需与网格结果吻合到约 ±0.3 dex。 | [→](../works/mephisto.md) |
| Spec-o3 / SpecVI-Bench | 2026 | 查看诊断性波段区间，从 LAMOST 巡天光谱中甄别稀有天体候选体——激变变星、碳星、S 型星、M 型巨星与白矮星。 | 五项稀有天体识别任务；测试集 1,122 条正样本 / 5,632 条负样本光谱，困难负样本由拒绝采样得到（概率阈值 0.8，接受率 1.74%）；另有 LAMOST → SDSS/DESI 的跨巡天划分，覆盖五项任务中的三项，每项约 50 条正样本 / 250 条负样本。 | 以 LAMOST 星表归属为准计算逐任务准确率与正类 F1，并在五项任务上取宏平均；另有六位天文学家依照公开的 0–5 分 rubric，就连贯性与物理自洽性为 100 条推理轨迹打分。 | [→](../works/spec-o3.md) |
| AstroAlertBench | 2026 | 甄别时域巡天警报：判断一次 ZTF 差异图像探测究竟是伪迹、太阳系内的移动天体，还是真实的暂现源或变源，并给出它的天体物理类别。 | 取自 ALeRCE stamp-classifier 数据集的 1,500 条真实 ZTF 警报，五类各 300 条保持均衡，每条都把 broker 元数据与 science/reference/difference 三联图像拼版配对；13 个具备视觉能力的模型受评，另设人类集成基线。 | 三个逐级递进的阶段——元数据落地、结构化科学论证，以及伪迹 → 物理起源 → 子类的层级级联——以逐阶段、条件与端到端五分类准确率计分；人类集成基线实测为 30.67 ± 5.32%。 | [→](../works/astroalertbench.md) |
| gammapyGPT | 2025 | 借助 Gammapy 库，在 CTAO 场景下完成地基伽马射线天文分析——观测筛选、反射区显著性、能流与谱指数，以及空间-能谱联合的源拟合。 | 四项 Gammapy 任务（ObservationList、ReflectedSignificance、ReflectedSpectrum、Source3DAnalysis），针对经数据指针访问的真实观测数据定义，在精简过的环境中于硬性时限内执行。 | 按复杂度分级的逐任务数值判据：观测数量要求整数精确匹配，显著性、能流与谱指数要求浮点值落在容差内，三维空间-能谱分析则以端到端跑通为准。 | [→](../works/gammapygpt.md) |
| AstroVisBench | 2025 | 在巡天与任务数据上实现天文专有的数据处理流程，再画出能传达既定科学洞见的图。 | 从 110 份 Astro Data Lab 与 STScI 教程 notebook 中抽取的 432 个处理任务与 432 个可视化任务，每份 notebook 划分为 setup / processing / visualization 三段；8 个模型受评。 | 处理阶段用 Variable Inspection Score（对标准答案内存变量的召回率）；可视化阶段由一个 VLM judge 把每张图判为 No Error / Minor / Major，该 judge 是依据与五位职业天文学家 ρ = 0.822 的一致性选出来的。 | [→](../works/astrovisbench.md) |
| ALeRCE Text-to-SQL | 2026 | 根据天文学家的自然语言提问，从在运行的 ALeRCE ZTF/Rubin 警报 broker 数据库中取出正确的天文记录——天体、分类、测光与光变曲线属性。 | 由 10 位天文学家与 ALeRCE 团队撰写的 110 组自然语言/SQL 对，标准查询出自专家之手，按 simple/medium/hard 分为 58 条开发集 / 52 条测试集，面向一个 25 表、304 列的数据库；13 个模型，每条查询运行 10 次。 | 基于执行的 Perfect Match：预测查询与标准查询都实际执行，比较返回的行标识（PMrows）与列标识（PMcols），并按难度层级分别报告。 | [→](../works/alerce-text-to-sql.md) |
| VESTA / DAWN | 2026 | 从数据中还原天体物理模型：判定恒星初始质量函数属于哪一族（Salpeter、Kroupa、Chabrier 及两种自由形式变体）及其参数，并拟合带有旋进-衰荡振幅包络的引力波啁啾信号。 | 400 个实例的 benchmark 中，DAWN 的两个天文切分——50 个初始质量函数实例与 50 个啁啾实例；三种视觉语言底座受评。 | 初始质量函数切分用拟合分布与真实分布之间的 Jensen–Shannon 散度，啁啾切分用留一交叉验证下的期望对数预测密度（ELPD-LOO）。 | [→](../works/vesta-dawn.md) |
| Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities | 2025 | 在天文数据中判定正确的底层模型：谱指数有误的宇宙学功率谱、EE 偏振谱与有误的哈勃常数，以及带双高斯轮廓、自吸收和超精细结构的分子谱线。 | benchmark 的十项任务中有六项属天文（三项宇宙学功率谱、三项谱线），每项都把作者生成的数据集与一段自然语言提示配对；对比三个 coding agent 与两个 judge 模型。 | 以系统能否判出正确底层模型的 pass@1 计分；视觉语言绘图 judge 只看产出的图（不给代码），依照由任务提示逐任务生成的 rubric 评分。 | [→](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope | 2026 | 用完整的匹配滤波流程，从模拟 Einstein Telescope 探测器噪声中恢复注入的双黑洞信号：由原始应变估计 PSD、生成几何模板库、注入与搜索。 | 同一份书面规格说明自主执行四次——两个 agent（Claude Code、Codex）× 两档注入强度——在同一硬件上处理模拟 ET E1 应变中的 100 次 BBH 注入。 | 实测的科学输出——模板库规模、ρ = 8 以上的探测效率，以及恢复 SNR 的均值/中位数/最小值/最大值——与逐项计数的过程行为（重启、静默偏离与显式自我纠正之别、未经要求的优化）并列报告。 | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| Gravity-Bench-v1 | 2025 | 从有计划的观测中发现模拟二体引力系统所隐藏的（有时是分布外的）物理规律；该任务集归类于 astro-ph.IM。 | 交互式的观测规划与分析回合，每次运行的实验预算上限为 100 次观测（官方项目页）。 | 答案对照由严格引力动力学模拟导出的参考解检验，并以人类专家水平作校准。 | [→](../works/gravity-bench.md) |
| An LLM-driven framework for cosmological model-building and exploration | 2025 | 通过改写 CLASS Boltzmann 求解器来实现并探索替代性暗能量宇宙学，计算 CMB 与物质功率谱，再与巡天数据对照检验。 | 在容器化的 CLASS 3.3.0 环境中，每个模型实例走三个顺序阶段（模型实现、计算可观测量、参数探索）；两个标准答案模型——Thawing Quintessence 与 Early Dark Energy——外加两次假设生成运行，评测一种 agent 配置。 | 二元的执行里程碑；Ω_X 与物质功率谱相对标准参考实现的最大相对偏差；以及由 DESI、Planck、Pantheon+ 与 SH0ES 数据算出的宇宙学奖励——含 BIC 的似然、Hubble/M_B 张力，以及以宇宙方差为单位的 CMB C_ℓ 吻合度。 | [→](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| SimAgents | 2025 | 从论文中还原一项已发表宇宙学模拟的配置——Ω_m、Ω_b、Ω_Λ、h、σ8、n_s、初始条件设定与关键模型开关——并写成 MP-Gadget 能接受的形式。 | 来自 arXiv、ApJ 与 MNRAS 的 40 余项已发表模拟，逐项人工标注全部相关的参数/取值对，并作为 `golden_standard` 集发布，覆盖 IllustrisTNG、Millennium、MTNG、Magneticum 与 SIMBA。 | 与人工标注做参数级匹配，给出精确率、召回率与 micro-F1；另按 Value / Type / Hallucination 的错误分类逐个模拟计数，人工评分与自动评分两种口径都有报告。 | [→](../works/simagents.md) |
| Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows | 2026 | 天体物理计算与分析：CAMB Boltzmann 求解器运行，以及基于 Union2.1 的 Ia 型超新星拟合、基于 SPARC 的 NGC 3198 转动曲线建模、取自 NASA Exoplanet Archive 的系外行星质量-半径分析，和 SLACS 强引力透镜分析。 | 18 个任务——14 个按复杂度分层的结构化 CAMB 计算任务，外加 4 个基于公开档案数据的研究导向任务——在 CMBAgent 的 One-Shot 与 Deep Research 两种配置下运行。 | 以阈值定义的自动评分：Execution Success Rate、按物理量加权的 Parameter Accuracy Score，以及由 NRMSE、SMAPE 与 Lin 一致性相关系数构成的 Numerical Accuracy Score，PAS 与 NAS 两者相乘合成为总分；另有四类失败模式的划分，把静默的错误计算单独隔离出来。 | [→](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory | 2026 | 仅凭文字描述重建一项已发表的天体物理方法——由稀疏宽带测光对海王星外天体做概率化光谱重建。 | 一个案例研究，在三种层层嵌套的信息状态（Title；+ Abstract；+ Methods）下实例化，两个开放权重模型在每种状态下各采样 N = 200 次重建；另由三个前沿模型在原始观测数据上生成可执行流程。 | 执行后的流程对照原作者的实现，按 Hierarchy of Scientific Validity 评分（V ∈ {0,1,2,3}；V ≥ 2 即功能上可重建），并考察重建光谱是否满足反射率非负一类的物理约束。 | [→](../works/quantifying-the-reproducibility-of-astrophysical-m.md) |
| AI Cosplaying as Astrophysicists | 2026 | 日常的天体物理研究工作——X 射线后随观测申请、爱丁顿比推导、星表交叉匹配的调试、暂现源后随策略——在五种不同的 AI 辅助策略下完成。 | 公开发布的 3,000 个天体物理任务库，分成六个工作流族、每族 500 个；2,592 项指派各在五种策略下跑一遍，得到跨 144 个研究者人设的 12,960 个受评回合，并做了一次完整的角色互换复现。 | 由 LLM judge 依各族专属的 rubric 评分（推导看代数、算术与单位是否正确；写作看科学含义是否保留；评审看有没有指出真实的推理缺口），输出任务分数、二元完成指示与灾难性失败标记，再合成为一个综合效用值。 | [→](../works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md) |
| AI's Capability in Assisting Scientific Research I: Literature Review | 2026 | 为八个真实的前沿研究课题整理文献，其中六个属天体物理或宇宙学：基于 MaNGA 的 AGN 占空比、莱曼断裂星系与暗晕的关联、弱引力透镜的内禀取向、HalfDome 的 CMB 前景、引力波双星的环境，以及脉冲星计时阵的灵敏度。 | 每个课题、每个系统各做一轮文献检索，至多 50 篇论文并归入四个类别；三个 AI 系统与每个课题的一位人类专家对照，共产出 701 条 AI 参考文献与 194 条人类参考文献。 | 与专家列表的重合只在标题与所归类别都吻合时才计入，相关性由该课题的领域专家判定；每条 AI 参考文献另经 DOI → 链接 → 标题检索的级联核验，判为完全正确 / 元数据不符 / 凭空编造。 | [→](../works/ai-assisting-research-i-literature-review.md) |
| AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation | 2026 | 为同样这八个课题（六个属天体物理或宇宙学）规划真实的观测与巡天分析，点明一页纸研究计划书所需的数据集、设备与方法。 | 32 份一页纸计划书（8 份人类撰写，24 份来自三个 LLM），都依据同一份专家提供的任务说明与模板写成；六位评审每人都评了全部 32 份。 | 由四位教师或资深博后评审与两位前沿 LLM 评审做盲评，按 1–5 分 rubric 打分，涵盖表述与结构的清晰度、方法的适切性、资源与工具规划，以及可行性/时间安排/风险意识；每份计划书另做一次「人类还是 AI 撰写」的二元判断。 | [→](../works/ai-assisting-research-ii-project-planning.md) |
| CosmoPaperQA | 2025 | 回答取自五篇高引论文的宇宙学问题——Planck 2018 参数、CAMELS 模拟、一次本地哈勃常数测量、用单个星系做宇宙学，以及 ACT DR6——覆盖事实检索、多源综合与分析性解读。 | 105 组专家撰写的问答对，分三个复杂度层级，在统一检索设置（top-k = 20、5,000 token 分块、温度 0.01）下跑过九种 RAG 配置，共产生 945 条回答。 | 全部 945 条回答由一位博士级宇宙学家对照理想答案做二元评分，再据此校准两个 LLM judge——二者的绝对分数偏向相反，但对系统的排序一致，Pearson r > 0.99。 | [→](../works/cosmopaperqa.md) |
| From Queries to Criteria | 2025 | 回答一线天文学家真正会问的天文文献问题，题目来自一套 RAG 助手在 STScI 为期四周的部署，其底库约 30 万篇 arXiv 天体物理论文。 | 从 368 条查询日志中采样、公开发布的 40 题 benchmark，标准答案为自由文本，由七位天文学家撰写，每题引用 2–5 篇 arXiv 论文（每题约耗时 30 分钟），另由一位天文学家复核。 | 以专家标准答案为准，由 LLM 生成 0–1 的相关性分数，辅以 embedding/BERTScore 接近度、认知标记检测与对引文的 NLI 蕴含检验；该分数与部署期间真实用户评分的 Pearson 相关为 0.8239。 | [→](../works/from-queries-to-criteria-understanding-how-astrono.md) |
| AstroMLab 1 | 2024 | 回忆并推理已成体系的天文知识，覆盖恒星天体物理、系外行星、银河系与河外天文、宇宙学、高能天体物理与仪器。 | 由 885 篇 *Annual Review of Astronomy and Astrophysics* 文章（1963–2023）生成的 4,425 道四选一单选题；47 个模型闭卷受评，RAG 明确不在范围内。 | 准确率并附 Wilson 得分区间（约 ±0.6–0.8 个百分点），按六个天体物理子领域与五种受测能力交叉切分；题目质量在一个子集上经人类专家审核。 | [→](../works/astromlab-1.md) |
| LLM-IOAA | 2025 | 完整求解国际天文与天体物理奥林匹克竞赛试题：位置天文与球面天文、天体力学、恒星结构与演化、银河系与河外天文、宇宙学，以及对真实光变曲线、光谱与巡天图像的解读。 | 取自 2022–2025 年官方 IOAA 试卷的 57 道题（49 道理论、8 道数据分析），经 IOAA 执行委员会许可转写为 LaTeX；五个前沿模型，共 285 次模型-题目评定。 | 按官方 IOAA 评分标准并沿用选手的分步给分规则人工评阅——每次评定都由前 IOAA 选手与领队独立评两遍、分歧协商定论——分数再映射到真实选手分布与奖牌线上。 | [→](../works/llm-ioaa.md) |
| AstroMMBench | 2025 | 解读天文图件——曲线图、光谱、巡天图像与仪器示意图——覆盖六个 astro-ph 子领域：星系（97）、宇宙学（111）、地球与行星（105）、高能（110）、仪器（87），以及太阳与恒星（111）。 | 从 3,592 份 arXiv 天文 TeX 源码中挖出 19,299 组图文对，再提炼成 621 道四选一单选题；25 个多模态模型经 VLMEvalKit 评测。 | 报告总体与逐子领域的选择题准确率；题目从 1,800 道候选中筛出，由 15 位子领域对口的天文专家就图题匹配、答案正确性与是否必须依赖领域知识审定后保留。 | [→](../works/astrommbench.md) |
| DomainCQA / AstroChart | 2025 | 读懂并推理天文论文里的图，把单纯的图表理解与那些需要图中并未呈现的天体物理知识的推断区分开来。 | AstroChart：覆盖 arXiv 天文论文中 482 张图的 1,690 组问答对——1,509 组 Fundamental QA 与 181 组依赖知识的 Advanced QA；21 个多模态模型受评，另有四位研究者在 10% 抽样上给出人类基线。 | 数值答案用按坐标轴量程归一化的相对误差，推导题用精确匹配，开放式回答由 DeepSeek-V3 judge 评判——该 judge 在 176 题抽样上与人工标注的 Pearson r = 0.816；每道题都由领域专家裁定为 Valid 或 Flawed 直至达成共识。 | [→](../works/domaincqa.md) |
| SciVQR | 2026 | 天文学中的多模态科学推理——六个顶层计分学科之一，明列六个子领域：天体物理、宇宙学、恒星天文、银河系天文、行星科学与观测天文。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 零样本准确率并单列天文一栏，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。卡片记下：天文那一栏无法被无歧义地读出，因为结果表与消融表中各学科列的排序并不一致。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 面向文献的天文工作：对来自 arXiv 的天文论文做解析、翻译、问答与综述生成。 | 8,735 个实例中天文占 597 个——200 个通用科学问答、19 个文献 OCR、19 个翻译、330 个单语文献问答、19 个跨语文献问答与 10 个综述选题；天文不贡献数据驱动发现类实例。18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性。 | [→](../works/hiscibench.md) |
| ScienceBoard | 2025 | 通过 Celestia 天象软件驱动的天文工作流——它是承载各领域的六款专业软件之一——要求对真实天文场景具备时空感知。 | 单台 Ubuntu 虚拟机中 169 个人工整理的计算机使用任务：38 个纯 GUI、33 个纯 CLI、98 个 GUI+CLI 混合；天文一项的逐软件任务数未公布，卡片上记为 `TODO(reference)`。 | 通过支持精确匹配、区间判定与数值容差的评估模板，程序化检查关键中间输入/输出与虚拟机的最终状态；按领域报告二元成功率，天文在所有受评 agent 上都属最弱之列。 | [→](../works/scienceboard.md) |
| Imaging-101 | 2026 | 天文计算成像：由增益污染的可见度数据做 Event Horizon Telescope 黑洞重建、高对比度系外行星日冕仪成像、大气湍流下的幸运成像、Shack–Hartmann 波前探测，以及 shapelet 源重建。 | 天文是 57 个以论文为依据的任务所覆盖的六个具名领域之一，每个任务都规整为预处理 → 正向物理 → 逆问题求解 → 可视化的流水线，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| PRL-Bench | 2026 | 完成源自 2025 年 8 月之后 Physical Review Letters 论文的前沿物理研究任务；天体物理是其明列的五个子领域之一。 | 100 个经专家验证的长程研究任务，以探索性方式设问；各子领域的任务数未说明。 | 客观可验证的任务结果，经专家验证，按 0–100 分制评分。 | [→](../works/prl-bench.md) |

## Related Works

- [Stargazer](../works/stargazer.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [ReplicationBench](../works/replicationbench.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Mephisto](../works/mephisto.md)
- [Spec-o3 / SpecVI-Bench](../works/spec-o3.md)
- [AstroAlertBench](../works/astroalertbench.md)
- [gammapyGPT](../works/gammapygpt.md)
- [AstroVisBench](../works/astrovisbench.md)
- [ALeRCE Text-to-SQL](../works/alerce-text-to-sql.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [SimAgents](../works/simagents.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory](../works/quantifying-the-reproducibility-of-astrophysical-m.md)
- [AI Cosplaying as Astrophysicists](../works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md)
- [AI's Capability in Assisting Scientific Research I: Literature Review](../works/ai-assisting-research-i-literature-review.md)
- [AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation](../works/ai-assisting-research-ii-project-planning.md)
- [CosmoPaperQA](../works/cosmopaperqa.md)
- [From Queries to Criteria](../works/from-queries-to-criteria-understanding-how-astrono.md)
- [AstroMLab 1](../works/astromlab-1.md)
- [LLM-IOAA](../works/llm-ioaa.md)
- [AstroMMBench](../works/astrommbench.md)
- [DomainCQA / AstroChart](../works/domaincqa.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
- [ScienceBoard](../works/scienceboard.md)
- [Imaging-101](../works/imaging-101.md)
- [PRL-Bench](../works/prl-bench.md)
