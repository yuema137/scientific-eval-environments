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

## Related Works

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
