# Materials Science

> [English](../../domains/materials_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

材料表征与计算材料科学，横跨物理仪器与仿真。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| AFMBench | 2025 | 操作真实的原子力显微镜——校准、特征检测、力学性质测量、石墨烯层数计数、压头检测——从实验设计到结果分析。 | 在 Nanosurf DriveAFM 上经 Python API 完成 100 个专家整理的任务；69% 需多工具，按复杂度与功能领域分层，每模型–任务对三次试验。 | 在真实硬件上物理执行；按功能领域的任务完成率，加一套命名失败分类（如 'sleepwalking'——超出指令的越权操作）。 | [→](../works/afmbench.md) |
| AutoMat | 2026 | 端到端复现计算材料科学论文中的论断，覆盖统计/ML 方法、密度泛函理论、分子动力学与离散位错动力学。 | 85 个专家整理的论断复现任务，分三类（from-paper、from-artifact 复现、from-artifact 解读），在资源受控的 HPC 式环境中运行。 | 可浏览工件的 LLM 评估 agent 对照隐藏的专家复现步骤打 1–5 分（≥4 为成功），与盲评专家评分的二次加权 kappa 校准为 0.69。 | [→](../works/automat.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的材料科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Material 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | 通过 agentic 工作流控制显微镜与材料表征仪器，并检验 benchmark 分数能否泛化到未见任务。 | 53 个 benchmark 测试跑遍 105 种 agent 配置（图拓扑 × 五个 LLM × RAG/上下文参数）；1,949 次运行，附完整轨迹日志。 | 带轨迹日志的 benchmark 测试，比较时延、token、成本与失败模式；用代理模型在未见任务上做预测来检验泛化性。 | [→](../works/agentic-microscopy-benchmarks.md) |
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，材料科学是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的金标准解与测试用例执行。 | [→](../works/scicode.md) |
| SciConvBench | 2026 | 澄清不适定的仿真请求；材料科学是其四个计算科学领域之一。 | 基于结构化任务本体的多轮消歧与矛盾消解对话。 | 按评分标准为澄清行为、对话共识建立与最终规格保真度打分。 | [→](../works/sciconvbench.md) |

## Related Works

- [AFMBench](../works/afmbench.md)
- [AutoMat](../works/automat.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [SciCode](../works/scicode.md)
- [SciConvBench](../works/sciconvbench.md)
