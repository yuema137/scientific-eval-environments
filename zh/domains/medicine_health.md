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

## Related Works

- [MedHELM](../works/medhelm.md)
- [SciAgentArena](../works/sciagentarena.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MetaSyn](../works/metasyn.md)
