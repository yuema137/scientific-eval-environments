# Civil & Structural Engineering

> [English](../../domains/civil_structural_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

土木与结构工程——建筑物与土木基础设施的分析、设计、验算、施工与维护。本页收录的工作评估以下内容：借助 OpenSeesPy、SAP2000、ETABS 等求解器，对梁、二维与三维建筑框架以及钢筋混凝土体系做结构分析与有限元建模；结构、岩土与基础设计，以及对照规范目标值的可靠度安全评估；设计规范与建筑规范的合规校核，包括在 IFC 与 BIM 模型上做几何密集的规则校核；围绕图纸、技术规格书、报审资料、工程量计算与造价估算的施工工程工作；桥梁与建筑外立面的检测与状态评估；以及土木与结构执业资格考试所考查的专业知识，连同折并入本领域的交通基础设施与水利基础设施两个子方向。与 Mechanical & Aerospace Engineering 的边界落在固体力学上：只有论文自身声明了这一共通范围时（如 SoM-1K 与 EngDesign），一项工作才同时列入两页；若受评对象是机器、车辆或流动而非结构或设施，则归入 Mechanical & Aerospace Engineering 而不在本页。与 Earth Science 的边界落在水上：作为自然过程的水文、河流动力学与气象学归入 Earth Science，而作用于它们的人工基础设施——供水管网、大坝、溢洪道、闸门——归入本页，横跨两者的工作则两页并列。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的土木工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| StructureClaw | 2026 | 把结构工程任务从建模一路做到验证、求解与规范校核。 | 以工件为中心的 agent 工作台上的 150 个受控场景（标准、交互、多模态重构）。 | 严格结构模型匹配加与冻结参考求解器响应的数值一致；所有断言须通过（E2E Success）。 | [→](../works/structureclaw.md) |
| ERI Benchmark | 2026 | 土木工程是其覆盖的九个领域之一，下设七个子领域：静力学、材料力学、结构分析、钢结构与混凝土设计、岩土工程、结构动力学与施工管理。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值。 | [→](../works/eri-benchmark.md) |
| A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis | 2026 | 静定梁的静力平衡分析——支座反力的大小与方向，扩展任务还要求给出剪力图与弯矩图。 | 8 道题：两种 10 m 梁型（简支梁；跨中带滚轴的外伸梁）与四种荷载工况交叉组合，另加三道留出的扩展梁题；每种配置采样 500 次。 | 可靠性（500 次相同运行中答对的比例）与鲁棒性（荷载沿梁以 1 m 为步长扫掠时的 (1 + CV)⁻¹），在同一批题目上分别对裸 LLM 和生成 OpenSeesPy 代码的 agent 计算。 | [→](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis | 2025 | 多跨多层二维建筑框架——结构的承重骨架——在固定竖向与水平荷载下的有限元建模。 | 20 道平面框架题（5 道三跨，15 道五跨、各跨层数逐跨抽样；两种拓扑抽象自真实建筑），荷载、支座与材料保持恒定，只有几何变化；每题独立试验 10 次。 | 准确率取所有运行中正确生成 OpenSeesPy 代码的比例；语法错误经人工修复，以便单独查看还原出的几何，并按来源（节点、单元、支座、材料）给出错误分类。 | [→](../works/a-lightweight-large-language-model-based-multi-age.md) |
| Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems | 2026 | 不规则三维建筑框架体系——逐层装配的柱、主梁与楼板——在竖向荷载与代表风荷载的水平荷载下的有限元建模。 | 10 个不规则三维框架，涵盖竖向不规则、平面不对称与布置不连续（平面网格 3 × 3 至 4 × 6，每格 0–7 层），每个重复试验 10 次。 | 只有当全部受监测响应量相对人工搭建的 SAP2000 真值模型的相对误差都低于 1% 时，该次试验才计为正确。 | [→](../works/agentic-large-language-models-for-automated-struct.md) |
| Integrating Large Language Models for Automated Structural Analysis | 2025 | 二维建筑框架——柱、主梁、悬臂梁与斜杆——的结构分析，求变形与内力（轴力、剪力、弯矩）。 | 20 道手工编写、附真值示意图的结构分析文字题，按三种既定模式生成（层数与跨数放缩、不对称、斜杆与悬臂）；四个模型三取优，稳定性另跑五次，指令消融每种条件跑十次。 | 对照准备好的真值示意图与预期输出判定正确性，报告三取优解题率与逐题的生成稳定性，并把布局错误与边界及荷载错误分开归类。 | [→](../works/integrating-large-language-models-for-automated-st.md) |
| Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering | 2025 | 三维钢筋混凝土建筑框架的静力与地震响应——层间位移角、最大位移、基底剪力与基本周期——并对照设计规范要求。 | 四个钢筋混凝土框架（2 至 5 层，含对称与不对称，按 NEC-15 与 ASCE 7-22 设计），每个在四组计算方式下分析（纯 GPT、GPT+MCP、手工 OpenSees、ETABS），共 16 次分析。 | 各项报告量相对 ETABS 参考模型的相对误差：纯 GPT 约 230–270%，GPT+MCP 与手工 OpenSees 均低于 1.427%。 | [→](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) |
| AutoBM / BMEval | 2026 | 依据结构设计说明生成物理上自洽的建筑模型：钢筋混凝土框架的节点与单元布置、截面与材料赋值、地震作用、模态分析，以及一条设计规范验算结论。 | BMEval——128 项经专家验证的建模任务，按建筑功能、层高与平面尺寸抽样，每个设计均对照抗震设计规范校验，并以其基本周期作为真值；对比 16 个模型。 | 沙箱执行生成的 OpenSeesPy 程序，并在其上叠加 Pass@k_period（一阶自振周期与参考值的相对误差在 0.30 以内）、Pass@k_compliance（给出明确的设计验算结论）以及三者同时满足的 Pass@k_strict。 | [→](../works/autobm.md) |
| MASSE | 2025 | 咨询公司做货架体系时的整套结构工作流：从建筑规范文件中查取场地地震参数，换算为楼层荷载，搭建并求解 OpenSeesPy 的梁柱与支撑模型，计算构件承载力，最后给出结构是否满足要求的结论。 | 100 道题，由不列颠哥伦比亚省真实货架项目的生产记录改编而成，真值由专家推导；每题独立试验十次，按四套基准（SAAB、SDAB、LAB、MASEB）评分。 | 由 GPT-5 充当 LLM judge，对照专家核定的解答通读完整分析日志，按已公布、带明确分值权重的分项 rubric 打分；MASEB 还把 token 成本与运行时长计入其效率与鲁棒性分项。 | [→](../works/masse.md) |
| Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework | 2026 | 构件级结构可靠度：结构构件或土木基础设施单元超越规定极限状态的概率，并对照规范目标值解读，例如 Eurocode EN 1990 中承载能力极限状态的 β = 3.8。 | 20 道手工编写的留出题——梁屈服、混凝土受压、欧拉柱失稳、相关荷载下的桥梁主梁、海洋导管架、相关性桩群、Mohr–Coulomb 边坡等——涵盖 11 种分布类型、2 至 30 个随机变量，失效概率从常见到罕见。 | 可靠指标 β 与失效概率 P_f 只由确定性运行器调用经验证的求解器算出，再与蒙特卡罗（或子集模拟）参考解比对，总体吻合在 Δβ ≤ 0.1 以内；方法类别的选择另按一套已公布的确定性标注准则单独评分。 | [→](../works/automating-structural-reliability-analysis-with-a.md) |
| EngDesign | 2025 | 在给定目标与约束下做结构设计：确定构件尺寸并布置承力结构——桁架杆件截面、钢梁厚度、以柔度最小化为目标的拓扑优化、Michell 布置、预制裂纹的断裂域。 | Structure Design 方向，取自该基准九个工程方向、101 项经仿真验证的设计任务（共 473 个可评分条目）中的 13 项；提示词平均 345.31 个 token，是九个方向中最短的。 | 模型输出结构化结果，由逐任务脚本调用有限元与拓扑优化求解器执行；Structure Design 方向的校核项是柔度、体积分数是否达标与对称性分类，结果报告为二元通过与 0–100 的部分给分。不校核任何建筑或桥梁设计规范。 | [→](../works/engdesign.md) |
| Large Language Model-Based Multi-Agent Systems for Automated Foundation Design | 2026 | 岩土基础设计：按 Terzaghi 与 Vesic 的设计方法计算基础尺寸、极限与容许承载力、瞬时沉降与固结沉降、安全系数，以及桩群效率与荷载分配。 | 七个类别共 27 个测试算例——15 道浅基础题与 12 道桩基础题，以简短的专业设计提示给出，附土层剖面、荷载与安全系数——在九种模型与工作流配置下各执行三次。 | 采用一套已公布的四项准则 rubric（计算准确性、思维链推理、复杂场景处理、结构化输出的一致性），按四级量表打分并按准则折算成百分制；论文未说明由谁执行该 rubric。 | [→](../works/large-language-model-based-multi-agent-systems-for.md) |
| SGR-BIM | 2026 | 在 IFC 模型上做几何密集的建筑规范合规校核：防火分区面积、疏散方式与疏散距离、由使用功能分类与房间面积推算的容纳人数，以及楼梯、走道与安全出口门的宽度。 | 五个 IFC 模型（两栋公寓、一栋宿舍、一栋办公楼、一座厂房）上的 679 条经专家核验的消防安全查询，分为 Rule（113）、Rule Requirement（189）、Model（240）与 Check（137）四类，每个模型的每一类中植入 1–2 处附条件例外。 | 人工评定的三档准确率——未识别出起控制作用的规范变量与边界条件即不给满分——另由一个匿名化的 LLM judge 对连贯性、相关性与可解释性打分并经人工审核；逐题结果做 Tukey HSD 显著性检验。 | [→](../works/sgr-bim.md) |
| DrafterBench | 2025 | 设计与施工阶段之间的土木工程施工图修改，涉及文字、表格以及钢筋、柱等矢量图元，还包括指令中从未言明的制图惯例。 | 1,920 项任务，由十二种修改任务类型（三类对象图元 × 四种修改操作）与五个二值指令控制变量交叉而成，通过 46 个自定义的图纸修改函数执行；任务类型归纳自设计与施工企业提供的 100 多份真实修改文件。 | 两级自动评分——代码可执行性（0 或 30 分）加六个子任务上的目标完成度（70 分）；方案执行部分按 agent 记录的操作链与参考操作链的交并比计分，因此从不对图纸本身做视觉检查。 | [→](../works/drafterbench.md) |
| AEC-Bench | 2026 | 施工文件的工程审查：节点详图的技术审查、在整套图纸中解析索引与交叉引用、把技术规格书与图纸对齐核对，以及审查报审资料是否合规。 | 三个范围层级、九个任务族共 196 个任务实例——图内（43）、图集内（89）、项目内（64）——素材取自公共部门项目公开发布的多专业 PDF 施工文件集。 | agent 通过 Harbor harness 在沙箱化的 Docker 容器中运行，输出结构化的 JSONL 审查发现，由逐任务的自动验证器对照已知真值判分并给部分分；不使用 LLM judge。 | [→](../works/aec-bench.md) |
| CEQuest | 2025 | 施工图识读与工程估算：辨识图元与视图类型、在不同视图之间交叉查证，以及依据尺寸数据做工程量计算与造价估算。 | 五个主题领域共 164 道专家编写的题目——101 道选择题、63 道判断题——主题顺序对应识图与估算的递进阶段；5 个 LLM，每个重复运行五次。 | 固定提示词下的答案精确匹配，以准确率的均值 ± 标准差报告，并附评测墙钟时间与模型规模；论文给出的失败案例是一块混凝土板的体积（5.33 立方码），模型按四舍五入取整，而估算实务要求向上取整。 | [→](../works/cequest.md) |
| AECBench | 2026 | 以建筑规范与规范表格为根基的建筑、工程与施工知识，涵盖结构与抗震设计、混凝土结构、施工实务与工程经济。 | 23 项任务共 4,800 道中文题，按记忆、理解、推理、计算、应用五个认知层级编排，由领域工程师编写并取材于执业资格考试，经两轮专家审核；9 个 LLM。 | 客观题按准确率评分；开放式回答——含约 2,000 字的工程文书——由 LLM judge 依专家预设的 rubric 打分，并以专家评分为准衡量 judge 偏差，再用保序回归与分段线性回归校正（平均绝对误差 2.947 → 约 1.93–2.02）。 | [→](../works/aecbench.md) |
| PE Civil Bench | 2026 | 执业资格考试所考查的土木工程实务——结构、岩土、交通、水资源、测量、施工、数学与职业道德——外加钢筋混凝土构件设计。 | 八个子学科共 150 道 FE 与 PE 风格的题目（110 道选择题、40 道开放式数值题），每题标注子学科、难度、题型与推理需求；配套的设计赛道含 33 种梁的配置；13 个模型分别在基础、向量 RAG 与 agentic RAG 三种条件下测试。 | 选择题看答案是否正确，开放题看推算出的数值；生成的钢筋混凝土设计既校核是否符合设计规范，又与 ETABS 有限元真值做相关性比对，达到 r ≥ 0.90，其自动评估器对照传统评分方式校准，相关系数 r = 0.976。 | [→](../works/pe-civil-bench.md) |
| Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams | 2024 | 土木与结构执业资格考试的内容：FE 土木考试的 18 个板块与结构 PE 考试的 11 个板块，包括结构力学、结构分析、结构设计与构造、土力学，以及规范与施工。 | 取自 NCEES 模拟试卷的 79 道 FE 题与 39 道 PE 题，每次提示只问一题，分别提给 ChatGPT-4 与 Google Bard；重度依赖图形的题目仅在能转写为文字时才纳入。 | 对照 NCEES 推荐解答做对/错二元评判，不给部分分也不调分，按主题板块与总体汇总——FE 70.9% / 39.2%，PE 46.2% / 41%——两个模型都没有答对任何一道结构设计题。 | [→](../works/evaluating-the-performance-of-artificial-intellige.md) |
| Civil-Eval | 2026 | 中国国家注册考试中的土木与交通工程知识：建筑结构与建筑物理、建筑材料与构造、场地设计与前期工作、建设工程经济、合同管理，以及建设工程监理法规。 | 2024 年 5 月考次 8 个考试科目共 517 道客观题（426 道单选、91 道多选），依赖表格与图形的题目已剔除，每个科目再分为易与难两档；10 个通用 LLM 外加 2 个推理模型与 1 个土木领域专用模型。 | 答案选项精确匹配，多选题须选项集合完全一致；按考试原有分值以及由难题占比确定的科目权重，报告加权平均准确率；选用考试之前发布的模型版本以抑制数据污染。 | [→](../works/civil-eval.md) |
| SoM-1K | 2025 | 承力构件的材料力学：杆、轴、梁与刚架（含超静定体系）的内力、应力、应变与变形，以及内力图绘制与面向设计的优化。 | 取自大学教科书与力学竞赛的 1,065 道标注题，按变形形式分类（梁 630、轴向 201、扭转 137、刚架 54、综合 43），并按静定性分类（静定 917、超静定 148）；每题配有题干、示意图、经专家核验的图示文字描述（Description of the Image）与完整解答。 | 全部回答由结构工程与材料力学教师人工评分，只有推理过程成立且最终答案正确才计分，对五次采样取多数表决；最佳成绩 56.6%。 | [→](../works/som-1k.md) |
| MMArch | 2026 | 把分散在一幅建筑或土木工程图件中的视觉证据与起主导作用的工程原理组合起来作答；结构工程、抗震工程、建筑检测与 BIM/数字建造是其十个子领域中的四个。 | 1,212 道简答题，取材于约 10,000 篇同行评审论文中的图件，经规划器与撰写器解耦的流水线、自动筛查、盲式对抗审核、双重答案验证，以及三位执业建筑师与工程师的一致复核构建而成。 | 对照不超过十个 token 的冻结参考答案计算准确率，并做单位、同义词、数值容差与答案集合的归一化，解码温度为 0；人类专家组达到 94.57%，最佳闭源模型约为 52%。 | [→](../works/mmarch.md) |
| DefectBench | 2026 | 建筑外立面的结构病害：识别、计数、定位并勾画开裂、材料缺失、表面污渍与外挂附着物，据此给出建筑状态判断。 | 12 个此前各自孤立的病害数据集，按同一套四大类、十一子类的本体归并为 1,488 张图像、4,527 处异常；评测子集为 487 个样本，每个样本设五道题，分属三个层级（语义感知、空间定位、生成式几何分割）。 | 对照经专家核验的标注，按层级采用不同指标族——精确率/召回率/F1 与计数 MAE；拓扑关系用 mAP50、mAP50-95 与命中率；掩膜用 mIoU、精确率、召回率、F1 与像素准确率——全程零样本多轮，每道题都以模型此前的回答为条件。 | [→](../works/defectbench.md) |
| BridgeEQA | 2025 | 依据多视角检测影像评估在役公路桥梁的技术状况，答案须落到 National Bridge Inventory 的 0–9 级状况评定标度上。 | 2,200 组开放词表问答，覆盖佛蒙特州 73 个镇的 200 个真实桥梁场景、9,586 张图像（平均每场景 47.93 张），按四种题型从佛蒙特州交通厅的检测报告中提取。 | 由 LLM judge 对照报告支撑的真值判定答案正确性；状况评定准确率分精确匹配与 NBI 标度上 ±1 以内两档；图像引用相关性由 VLM judge 打分，并对照人工标注校准（Spearman 0.817）。 | [→](../works/bridgeeqa.md) |
| Cognitive Agents for Bridge Inspection Prioritization | 2026 | 一个机构应当优先检测哪些公路桥梁、按什么周期检测，推理须依据 National Bridge Inspection Standards 与 AASHTO《Manual for Bridge Element Inspection》。 | 依据结构化的 National Bridge Inventory 记录逐桥定优先级，数据取自 FHWA 六个年度版本（2020–2025）并筛出康涅狄格州，得到 3,389 座桥的分析样本，在其中共有的 3,365 座上打分；对比四种方法——固定周期、加权规则指数、梯度提升集成模型与 LLM agent。 | 以截至 2025 年观测到的持续劣化为准，在三种结果定义下用 AUC、平均精度与 precision@300 评价排序；另由一位持证桥梁检测工程师对分层抽取的 100 条 agent 理由做盲评，按 0–3 分 rubric 打分（均值 2.77）。 | [→](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) |
| TransportBench | 2024 | 本科阶段的交通系统工程：公路几何设计、车辆运动、交通流与交通控制、交通网络分析、交通规划与方式划分，以及公共交通系统设计。 | 140 道题（73 道判断题，其余为开放题），取自伊利诺伊大学两门开设多年的土木工程课程，所有图形均改写为文字描述；7 个模型零样本作答。 | 由领域专家人工评判最终答案与推理过程（最佳模型 67.1%），另对每道判断题做五次独立试验统计 Mixed Response Rate，并单独设一套自检一致性流程。 | [→](../works/transportbench.md) |
| TRIP-Evaluate | 2026 | 交通基础设施的规划、设计与运营：几何设计审查、通行能力评价、需求预测与交通安全审计，以及信号控制、标志标线标准、路侧设备与法规解读。 | 837 道单选题（文本 596、图像 198、点云 43），按「角色–任务–知识」分类体系组织，含 4 类角色、16 个任务领域与 226 个知识点；规划设计角色 194 题，交通管理 281 题。 | 统一提示词、固定解码，模型只能输出一个选项字母，异常输出按一套有日志记录的规则统一处理；准确率按角色、任务领域、知识点、能力、难度与模态分别报告，并记录基准与提示词的版本。 | [→](../works/trip-evaluate.md) |
| LLM-EPANET | 2025 | 市政供水管网的水力建模：压力、流量、水泵能耗、管网改造与情景分析。 | 在 Net1、Net3 与 L-Town 上提出 69 条自然语言查询，分五个复杂度类别（Static、Hydraulics、Quality、Hydraulics Scenario、Iterative），每条都配一份手写的确定性参考脚本；对比七个模型。 | 以返回数值与执行后的 EPyT 参考实现是否功能等价为准——绝不比对文本或代码相似度——执行失败以及聚合、索引、单位错误一律判错，接近正确的情形由水力建模专家裁定；准确率按类别报告，总体 56–81%。 | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | 水科学与水利工程知识，其土木内核是水工建筑物与设备（大坝、溢洪道、闸门）、岩土工程、行业设计标准，以及工程安全与管理。 | 覆盖九个子领域的 4,000 道中文题（约 2,700 道单选、1,300 道多选），每题标注认知层级，取材于教科书、行业标准、法律法规与统计年鉴，每题至少经三位专家独立审核；16 个模型。 | 零样本思维链、温度 0 提问，最终选项由另一个 LLM 抽取；准确率按总体以及子领域、题型、认知层级分别报告，商业模型达到 0.74–0.80，开源模型 0.41–0.68，在行业标准与水工建筑物两项上最弱。 | [→](../works/hydro-se-bench.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的土木与结构工程子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`STRUC` 结构分析与结构力学 · `SDES` 结构设计与构件选型 · `SEIS` 抗震工程与结构动力学 · `GEO` 岩土与基础工程 · `REL` 结构可靠度与安全评定 · `CODE` 设计规范与建筑规范符合性检查 · `BIM` BIM、IFC 与数字化建造模型 · `CONST` 施工工程、图纸、技术规格与造价估算 · `INSP` 检测、状态评定与结构病害 · `TRAN` 交通与公路基础设施工程 · `HYD` 水利与供排水基础设施工程 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

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
| AEC-Bench | CONST | ? | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| MASSE | STRUC, SEIS | ✘ | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ | **3** | ✔ | ✔ | ◐ | 0 | 2 | 4 | **8.5** |
| BridgeEQA | INSP | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ◐ | ✘ | ✘ | 2 | 3 | 2 | **7.5** |
| DefectBench | INSP | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **2.5** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| SGR-BIM | CODE, BIM | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✘ | ✔ | ✘ | 3 | 2 | 4 | **10** |
| DrafterBench | CONST | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 4 | **10** |
| StructureClaw | STRUC, CODE | ? | ✘ | ◐ | ◐ | ✘ | ✘ | ✔ | **2** | ◐ | ✘ | ✘ | 3 | 2 | 3 | **8.5** |
| MMArch | STRUC, SEIS, INSP, BIM | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✔ | ✘ | ◐ | 3 | ? | 3 | **7.5** |
| Large Language Model-Based Multi-Agent Systems for Automated Foundation Design | GEO | ✔ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✔ | ✘ | 0 | 1 | 3 | **5** |
| Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems | STRUC | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | 1 | 4 | **8.5** |
| LLM-EPANET | HYD | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | 1 | 4 | **8.5** |
| EngDesign | STRUC, SDES | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✔ | ✘ | 3 | 1 | 3 | **8** |
| Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering | STRUC, SEIS | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | 0 | 3 | **6.5** |
| Cognitive Agents for Bridge Inspection Prioritization | INSP | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✔ | ✘ | 3 | 3 | 4 | **11** |
| SoM-1K | STRUC | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ◐ | ✘ | 3 | 3 | 4 | **10.5** |
| A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis | STRUC | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 1 | 4 | **8** |
| TRIP-Evaluate | TRAN | ✘ | ✘ | ✘ | ✔ | ✘ | ? | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| PE Civil Bench | GEN, SDES | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 2 | 2 | 1 | **5.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| AutoBM / BMEval | STRUC, SEIS, CODE | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework | REL, STRUC, GEO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ◐ | ✘ | ✘ | 3 | 1 | 4 | **8.5** |
| A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis | STRUC | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✘ | 3 | 1 | 4 | **8** |
| Integrating Large Language Models for Automated Structural Analysis | STRUC | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✘ | 3 | 1 | 4 | **8** |
| CEQuest | CONST | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| ERI Benchmark | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✔ | 2 | 2 | 3 | **9** |
| AECBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| Civil-Eval | CONST, STRUC, TRAN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| TransportBench | TRAN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ◐ | ✘ | ✘ | 3 | 2 | 3 | **8.5** |
| Hydro-SE Bench | HYD, GEO, CODE | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 2 | ? | 3 | **5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [StructureClaw](../works/structureclaw.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)
- [AutoBM / BMEval](../works/autobm.md)
- [MASSE](../works/masse.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [EngDesign](../works/engdesign.md)
- [Large Language Model-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md)
- [SGR-BIM](../works/sgr-bim.md)
- [DrafterBench](../works/drafterbench.md)
- [AEC-Bench](../works/aec-bench.md)
- [CEQuest](../works/cequest.md)
- [AECBench](../works/aecbench.md)
- [PE Civil Bench](../works/pe-civil-bench.md)
- [Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md)
- [Civil-Eval](../works/civil-eval.md)
- [SoM-1K](../works/som-1k.md)
- [MMArch](../works/mmarch.md)
- [DefectBench](../works/defectbench.md)
- [BridgeEQA](../works/bridgeeqa.md)
- [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md)
- [TransportBench](../works/transportbench.md)
- [TRIP-Evaluate](../works/trip-evaluate.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
