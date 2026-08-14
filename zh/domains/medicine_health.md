# Medicine & Health

> [English](../../domains/medicine_health.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

临床与生物医学应用评估：医学任务、药物发现、EHR 建模、生物医学建模。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| MedHELM | 2025 | 在经临床医生验证的 5 大类、22 子类分类法下的医学与临床语言任务——从临床病历生成到管理与工作流。 | 121 个任务，聚合自 35 个 benchmark（17 个既有 + 18 个新构），与 29 名临床医生共同开发。 | LLM 陪审团评估，与临床医生一致性经过实测（ICC = 0.47），报告优于 ROUGE-L 与 BERTScore 基线。 | [→](../works/medhelm.md) |
| SciAgentArena | 2026 | 其五个生物医学研究领域中的计算药物发现与 EHR 建模——如 hERG 毒性预测与 FHIR 查询构造。 | 约 200 个任务，分四类（Data Analysis、Optimization、Discovery、Validity），在交互式、agent 无关的环境中运行。 | 按领域的逐步验证：专家设计的二元标准、EHR 任务的动作级 F1、以及在独立运行上取平均的任务原生指标（如 AUROC）；不用 LLM judge。 | [→](../works/sciagentarena.md) |
| NatureBench | 2026 | 达到 Nature 系列 Biomedical Modeling 研究的已发表 SOTA——其 90 个任务中的 14 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Life Sciences 分组下的医学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| MetaSyn | 2026 | 进行忠实于协议的系统综述与 meta 分析；医学是其 422 个专家整理 meta 分析所覆盖的主题之一。 | 多阶段系统综述工作流：在掺入不合格干扰文献的共享 PubMed 文献库中，依据带结构化 PI/ECO 标准的研究问题找出应纳入的研究。 | 对照原综述作者实际纳入的研究集做识别评估，并以分阶段评估定位 meta 分析流程中的失败环节。 | [→](../works/metasyn.md) |
| CORE-Bench | 2024 | 用论文自带的代码与数据重现已发表的计算结果；医学是其三个学科之一。 | 90 篇论文的 270 个任务，分三档难度，含纯语言与视觉-语言两种形式。 | 重现结果的准确率，由快速、可并行的评估系统校验。 | [→](../works/core-bench.md) |
| MedAgentGym | 2025 | 解决以代码为中心的生物医学数据科学任务，含 EHR 场景（据官方仓库为 MIMIC-III、eICU）。 | 12 个真实场景的 72,413 个任务实例、129 类，在带交互反馈的可执行沙箱中。 | 沙箱中检验的可验证真值标注；29 个 LLM 受评。 | [→](../works/medagentgym.md) |
| SMDD-Bench | 2026 | 面向蛋白靶点设计小分子药物：药效团、相互作用位点、骨架跃迁、先导化合物优化、片段组装。 | 102 个蛋白靶点上 502 个保证有解的多轮任务，受有限 oracle 调用预算约束。 | 保证有解实例上的解出率；最佳前沿模型 40.2%。 | [→](../works/smdd-bench.md) |
| MedBrowseComp | 2025 | 跨实时来源检索并调和多跳医学事实：试验、一手研究、监管记录、专利与费用数据。 | 1,000+ 道医生整理的问题，分 deep-research 与 computer-use 切分（据官方数据集为 50/605/484）。 | 实时检索下对照标准答案检验。 | [→](../works/medbrowsecomp.md) |
| AgentClinic | 2024 | 通过序贯对话、不完全信息下的多模态数据采集与工具使用为患者作出诊断。 | 覆盖九个专科与七种语言的模拟临床接诊，配患者、检查与主持 agent。 | 带偏差扰动与以患者为中心指标的诊断准确率；由真实 EHR 与临床阅读者研究支撑。 | [→](../works/agentclinic.md) |
| MedAgentBench | 2025 | 通过生产级 EHR 接口执行医生撰写的临床任务。 | 100 位真实感患者档案（70 万+ 数据元素）上、10 类共 300 个患者级任务，环境符合 FHIR 标准。 | 对照参考解的程序化成功率检验；最佳模型 69.67%。 | [→](../works/medagentbench.md) |
| SDBench | 2025 | 通过向守门人迭代索取发现并开具带费用的检查来作出诊断。 | 304 个 NEJM-CPC 病例的序贯接诊；医生队列基线（21 位临床医生，平均准确率 20%）。 | 诊断准确率与就诊、检查费用联合评分。 | [→](../works/sdbench.md) |
| SciVisAgentBench | 2026 | 对医学科学数据的科学可视化与数据分析——其七个应用领域之一——将自然语言意图转成对体数据与多模态医学数据的可执行可视化操作。 | 108 个专家精制的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，经 CLI、MCP server 与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态流水线：将 MLLM judge（报告为 Claude-Opus-4.6；与人工评分 Pearson 0.808）与确定性评估器结合——图像指标（PSNR、SSIM、LPIPS）、代码检查器与基于规则/按案例的验证器。 | [→](../works/scivisagentbench.md) |
| Fisher-R1 / P-Bench | 2026 | 在真实医学/生物统计数据集（Vanderbilt Biostatistics 教学材料、R 包数据集）上进行统计有效的假设检验——医学是其三个领域之一——覆盖随机实验与观察性研究。 | 425 个开放式假设检验任务（Easy 203 / Hard 222），横跨经济学、生物与医学；每题只给一个假设与一个数据集，要求选择统计检验、计算 p 值并作出拒绝/不拒绝的结论。卡片未给出各领域计数。 | 标准答案的 p 值、检验统计量与决策取自对规范参考代码一次带日志运行的读数；按 Raw（决策匹配）与 Strict（决策加 p 值接近度在 0.5 个 z-score 单位内）计分，pass@1 与 pass@3。 | [→](../works/fisher-r1.md) |
| MiraMind | 2025 | 证据受限的心理健康 / 精神科临床推理——诊断、干预选择与精神科问答——其中判断应有的具体程度、确定性与严重度本身也被评估（折并入 Medicine & Health）。 | 13 个数据集上的六个任务族（评估、诊断、干预、多步精神科问答、抽象、验证），涵盖非正式的用户叙述、咨询对话、精神科执业考试式问答与 Cochrane 综述摘要；20 个 LLM。 | 各任务族的结果指标（Micro-F1、Jaccard、专家评分点召回、Macro-F1），加一套 LLM-as-judge 的轨迹评分标准（可用性、逻辑结构、信息贡献），在 100 条人工标注轨迹上验证。 | [→](../works/miramind.md) |
| Imaging-101 | 2026 | 医学计算成像——它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| MolClaw | 2026 | 计算药物发现：针对蛋白靶点的虚拟筛选与结合亲和力推理、分子编辑，以及对一个具名药物分子（Erlotinib）的结构导向先导优化。 | MolBench 分三层——筛选（50 道性质筛选、37 道结合亲和力、25 道对接）、优化（39 道官能团题，外加一项性质优化子任务，其题量为 `TODO(reference)`），以及三项端到端发现挑战，需要 8 到 50 次以上的连续工具调用，其中先导优化挑战最多跑十五轮。 | 性质筛选与结合亲和力比较用 Accuracy，对接筛选用 Hits@3，优化用操作准确率、性质变化量与成功率，端到端一层用任务专属的加权 rubric；作者声明所有端到端结果均为纯计算结果，仍需湿实验验证。 | [→](../works/molclaw.md) |
| RubricsTree | 2026 | 面向消费者与临床的个人健康问答——医学解释、对用户健康与可穿戴传感指标的解读、建议与行动规划、症状处理——评判的是临床正确性而非文风。 | 作为任务集为 N/A：它是一套评判框架，由 100 多条原子的、临床可核验的布尔 rubric 组成分层 DAG，策展自约 4,000 条真实用户查询。元评估用四个场景下的 532 条真实查询并施加受控扰动；下游优化效果在 HealthBench-Hard（362 条查询）上衡量。 | 与医生主导的专家组的一致性以 ICC₃（0.876）与 Cohen's κ（0.787）衡量，而基于原则的基线只有 0.291 与 0.431；另有 oracle 扰动测试，检验语境上劣化过的回答是否确实会被扣分。 | [→](../works/rubricstree.md) |
| BiomedSQL | 2025 | 围绕药物基因靶点、适应证、许可状态与用量回答临床转化问题，其间还得自行补上自然语言问题从未言明的隐含判据——哪个试验期算作已获批、哪个效应方向才是问题要的答案。 | 68,000 组 question / SQL 查询 / answer 三元组，落在一个十张表的 BigQuery 数据库上（表的规模从几百行到 72.2M 行不等），由 40 条专家编写的种子查询套模板扩展而来；模型在一个有代表性的 546 题测试集上评分，该测试集按九类生物医学推理标注。 | 以 Execution Accuracy 为主指标（查询执行结果须与金标准执行结果完全一致），并列报告 Jaccard 部分得分与语法错误率；对照实测的两位生物医学分析师基线，其 EX 为 90.0%。 | [→](../works/biomedsql.md) |
| OntoLearner | 2026 | 为医学——它的本体集合覆盖的 22 个领域之一，官方 hub 上另有一份医学数据集——构建本体结构：给术语定类型、恢复类型之间的 is-a 层级、抽取非分类关系。 | 覆盖 22 个领域的 180 个机器可读本体，为三项本体学习任务备好可直接接入流水线的 train/dev/test 切分；共评测 22 个检索模型与 12 个 LLM，设定是单次结构化预测而非 agentic 循环。 | 以归一化的成对与三元组匹配对照金标准本体结构计算 precision、recall 与 F1；卡片中逐领域、逐模型的分数为 `TODO(reference)`，因论文的结果章节无法获取。 | [→](../works/ontolearner.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [MiraMind](../works/miramind.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [MedHELM](../works/medhelm.md)
- [SciAgentArena](../works/sciagentarena.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MetaSyn](../works/metasyn.md)
- [CORE-Bench](../works/core-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AgentClinic](../works/agentclinic.md)
- [MedAgentBench](../works/medagentbench.md)
- [SDBench](../works/sdbench.md)
- [Imaging-101](../works/imaging-101.md)
- [MolClaw](../works/molclaw.md)
- [RubricsTree](../works/rubricstree.md)
- [BiomedSQL](../works/biomedsql.md)
- [OntoLearner](../works/ontolearner.md)
