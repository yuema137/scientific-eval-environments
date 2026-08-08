# Materials Science

> [English](../../domains/materials_science.md) | **简体中文**

## Scope

材料表征与计算材料科学，横跨物理仪器与仿真。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| AFMBench | 2025 | 操作真实的原子力显微镜——校准、特征检测、力学性质测量、石墨烯层数计数、压头检测——从实验设计到结果分析。 | 在 Nanosurf DriveAFM 上经 Python API 完成 100 个专家整理的任务；69% 需多工具，按复杂度与功能领域分层，每模型–任务对三次试验。 | 在真实硬件上物理执行；按功能领域的任务完成率，加一套命名失败分类（如 'sleepwalking'——超出指令的越权操作）。 | [→](../works/afmbench.md) |
| AutoMat | 2026 | 端到端复现计算材料科学论文中的论断，覆盖统计/ML 方法、密度泛函理论、分子动力学与离散位错动力学。 | 85 个专家整理的论断复现任务，分三类（from-paper、from-artifact 复现、from-artifact 解读），在资源受控的 HPC 式环境中运行。 | 可浏览工件的 LLM 评估 agent 对照隐藏的专家复现步骤打 1–5 分（≥4 为成功），与盲评专家评分的二次加权 kappa 校准为 0.69。 | [→](../works/automat.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的材料科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Material 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [AFMBench](../works/afmbench.md)
- [AutoMat](../works/automat.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
