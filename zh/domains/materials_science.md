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
| SciCode | 2024 | 为科学家整理的问题编写科研代码；其 16 个自然科学子领域分属五大主领域，材料科学是其中之一。 | 80 个主问题分解为 338 个子问题，混合知识回忆、推理与代码合成。 | 对照科学家标注的参考解与测试用例执行。 | [→](../works/scicode.md) |
| SciConvBench | 2026 | 澄清不适定的仿真请求；材料科学是其四个计算科学领域之一。 | 基于结构化任务本体的多轮消歧与矛盾消解对话。 | 按评分标准为澄清行为、对话共识建立与最终规格保真度打分。 | [→](../works/sciconvbench.md) |
| ChemX | 2025 | 从纳米材料文献——纳米酶、纳米磁性材料——与小分子数据集中抽取结构化数据。 | 10 个人工整理、专家校验的抽取数据集；agent 式文档处理。 | 对照领域专家校验记录的抽取质量。 | [→](../works/chemx.md) |
| MaCBench | 2024 | 承担材料研究中的视觉工作：认读仪器与实验场景、抽取数据、解读实验结果。 | 三个方面的多模态（图像 + 文本）任务——数据抽取、实验理解、结果解读。 | 经 ChemBench 管线计准确率；抽取近乎完美，空间与跨模态推理受限。 | [→](../works/macbench.md) |
| MaScQA | 2023 | 回答横跨 14 个主题的材料科学与冶金考题。 | 650 个源自 GATE 的问题，四种题型；零样本与链式思维提示下的静态问答。 | 准确率加「概念 vs 计算」错误分类；GPT-4 约 62%。 | [→](../works/mascqa.md) |
| MatSciBench | 2025 | 求解横跨材料核心子学科的大学水平问题。 | 1,340 个问题（946 个配参考解、315 个带图像）；静态文本与多模态问答。 | 文本与图像题准确率；DeepSeek-R1 75.22% / GPT-5 53.02%。 | [→](../works/matscibench.md) |
| LLM4Mat-Bench | 2024 | 从晶体的文本编码预测材料性质。 | 约 190 万结构、45 种性质、3 种模态（成分/CIF/文本）；静态预测。 | 回归用 MAD:MAE、分类用 AUC；生成式 LLM 近乎随机。 | [→](../works/llm4mat-bench.md) |
| MatText | 2024 | 从文本表示预测晶体性质，并对照几何感知模型。 | 9 种文本表示，参数至 70B，数据至 200 万结构；静态预测。 | 对照 GNN 基线的回归误差；记录「GNN-LM 墙」。 | [→](../works/mattext.md) |
| AtomWorld | 2025 | 在标准建模操作下构建与修改晶态原子结构。 | 四类建模范式下的 10 种基本操作；可静态验证。 | 可验证结构检查；旋转成功率低于 12%。 | [→](../works/atomworld.md) |
| OpenXRD | 2025 | 回答 X 射线衍射与晶体学问题。 | 217 个专家策划问题，闭卷与开卷；74 个 LLM/MLLM。 | token 数相同下比较专家策划与 AI 生成上下文的准确率。 | [→](../works/openxrd.md) |
| MatVQA | 2025 | 对材料显微与衍射影像做视觉推理。 | 横跨 4 类结构-性质-性能任务的 1,325 个问题；17 个 MLLM；剔除捷径。 | 真实材料影像上的准确率，带文本捷径剔除。 | [→](../works/matvqa.md) |
| MatCha | 2025 | 理解贯穿研究工作流的材料表征。 | 横跨 4 个阶段、21 个任务、覆盖真实表征影像的 1,500 个问题。 | 带人类专家基线的准确率；少样本与 CoT 无法弥合差距。 | [→](../works/matcha.md) |
| MatQnA | 2025 | 解读十种主流表征方法（XPS、XRD、SEM、TEM 等）的数据。 | 覆盖真实表征数据的选择题与主观题；多模态。 | 客观准确率（前沿 MLLM 约 90%）加主观评估。 | [→](../works/matqna.md) |
| MatViX | 2024 | 从图文丰富的论文中抽取结构化数据——成分与性质曲线。 | 324 篇全文论文 → 1,688 个专家策划 JSON；零样本 VLM 抽取。 | 成分 F1；曲线的相似度分与对齐分。 | [→](../works/matvix.md) |
| MatTools | 2025 | 理解并编程材料科学工具（pymatgen）以计算性质。 | 69,225 对理解问答 + 49 个真实任务（138 个子任务），需 Python 代码。 | 理解准确率加经执行验证的代码生成。 | [→](../works/mattools.md) |
| AutoDFT / VASPBench | 2026 | 自主规划、运行并修复密度泛函理论（VASP）计算。 | 横跨 9 种 DFT 计算类型的 34 个任务；闭环多 agent 执行。 | 任务级成功率（GPT-5.2 94.1%）加对照数据库的性质准确率。 | [→](../works/vaspbench.md) |
| AlchemyBench | 2025 | 规划无机材料合成：前体、设备、流程、表征。 | 对 17,000 条专家核验合成配方的端到端预测；静态。 | 对自由文本预测的、经专家一致性验证的 LLM-as-a-Judge。 | [→](../works/alchemybench.md) |
| Materials Hypothesis Generation | 2025 | 在明确目标与约束下生成材料发现假说。 | 基于从近期论文策划的数据集的假说生成。 | 一个模拟材料科学家批判性评估的可扩展指标。 | [→](../works/materials-hypothesis.md) |
| Science Edge Evaluation (SEE) | 2026 | 在真实材料表征数据上做证据受限的推理——SEM/TEM/AFM 显微、X 射线衍射图样与热分析曲线——而非概念背诵；材料科学是其三个学科之一。 | 1,116 道专家整理的多模态题（1,049 道公开），横跨三个实验学科（化学、生物、材料科学）与 17 个子领域，含选择题与数值填空；视觉 agent 设定另加网页搜索与代码解释器。 | 答案对照专家真值评分——选择题精确匹配，数值答案按专家容差——在严格的二元 LLM-as-judge 协议（Gemini 3.1 Pro）下判定；图像消融检查确认每题都需其视觉输入。 | [→](../works/science-edge-evaluation.md) |

## Related Works

- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [AFMBench](../works/afmbench.md)
- [AutoMat](../works/automat.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [SciCode](../works/scicode.md)
- [SciConvBench](../works/sciconvbench.md)
- [ChemX](../works/chemx.md)
- [MaCBench](../works/macbench.md)
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
