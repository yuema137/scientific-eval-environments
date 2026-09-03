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
| ERI Benchmark | 2026 | 材料工程是其覆盖的九个领域之一，下设六个子领域：材料结构、力学性能、相图、失效分析、高分子与复合材料以及腐蚀。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值。 | [→](../works/eri-benchmark.md) |
| Imaging-101 | 2026 | 材料计算成像——与化学合并计为它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| CASCADE | 2025 | SciSkillBench 中的材料科学研究任务：检索与处理材料数据，并借助专用材料工具包运行仿真；论文归档于 cond-mat.mtrl-sci。 | 116 个材料科学与化学任务——76 个数据类、40 个计算类，再按说明详细程度分为 58 个点明关键函数的 Level 0 任务与 58 个只给出高层目标的 Level 1 任务；每种配置重复三次，共 16,008 次实验运行。 | 以结果为准的自动打分：在预设容差阈值内比对 agent 处理后的输出与标准答案，报告为成功率（GPT-5 下 DeepSolver 为 93.26%，Native 配置为 35.36%）。 | [→](../works/cascade.md) |
| OntoLearner | 2026 | 为材料科学与工程——它的本体集合覆盖的 22 个领域之一，官方 hub 上另有一份材料数据集——构建本体结构：给术语定类型、恢复类型之间的 is-a 层级、抽取非分类关系。 | 覆盖 22 个领域的 180 个机器可读本体，为三项本体学习任务备好可直接接入流水线的 train/dev/test 切分；共评测 22 个检索模型与 12 个 LLM，设定是单次结构化预测而非 agentic 循环。 | 以归一化的成对与三元组匹配对照金标准本体结构计算 precision、recall 与 F1；卡片中逐领域、逐模型的分数为 `TODO(reference)`，因论文的结果章节无法获取。 | [→](../works/ontolearner.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的材料科学子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`STRUCT` 晶体结构与晶体学（含衍射分析） · `CHAR` 材料表征、显微与波谱 · `INSTR` 仪器操作与自动化实验室 · `COMP` 计算材料学（DFT、分子动力学、介观模拟） · `INFO` 材料信息学、数据整理与性质预测 · `SYN` 合成与加工 · `NANO` 纳米材料 · `POLY` 高分子、软物质与复合材料 · `METAL` 冶金与合金 · `MECH` 材料力学行为 · `THERMO` 热力学与相图 · `CORR` 腐蚀、劣化与失效分析 · `DISC` 材料发现与设计 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

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
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| Imaging-101 | CHAR, COMP | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| Agentic Self-Driving Microscopy Benchmarks | INSTR, CHAR | ✘ | ✘ | ✔ | ◐ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| AFMBench | INSTR, CHAR | ? | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 0 | 2 | 4 | **6** |
| Science Edge Evaluation (SEE) | CHAR, STRUCT | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ◐ | 2 | ? | 3 | **5.5** |
| AutoMat | COMP, INFO | ? | ✘ | ✘ | ◐ | ✔ | ✘ | ✔ | **2.5** | ◐ | ✔ | ✘ | 1 | 1 | 3 | **6.5** |
| MatCha | CHAR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✔ | ✘ | ◐ | 3 | 3 | 4 | **11.5** |
| ChemX | NANO, INFO | ? | ✘ | ✘ | ◐ | ✘ | ✔ | ◐ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MatVQA | CHAR, STRUCT | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MatViX | POLY, INFO | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| AlchemyBench | SYN | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ◐ | ✔ | ✔ | 1 | 3 | 1 | **7.5** |
| MatQnA | CHAR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| MaCBench | CHAR, INSTR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 2 | ? | 4 | **6** |
| CASCADE | COMP, INFO | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| Materials Hypothesis Generation | DISC | ✘ | ◐ | ✘ | ✘ | ✔ | ✘ | ✘ | **1.5** | ◐ | ✔ | ✔ | 1 | 1 | 1 | **5.5** |
| AutoDFT / VASPBench | COMP | ? | ✘ | ✘ | ✘ | ◐ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 1 | 1 | **5** |
| MatTools | COMP, INFO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| SciConvBench | COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✔ | ◐ | 1 | ? | 3 | **5.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| MatSciBench | GEN | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ◐ | 2 | 3 | 3 | **8.5** |
| MatText | INFO, STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 4 | **10** |
| AtomWorld | STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 2 | **9** |
| ERI Benchmark | STRUCT, MECH, THERMO, POLY, CORR | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| MaScQA | GEN, METAL | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| LLM4Mat-Bench | INFO, STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| OpenXRD | STRUCT, CHAR | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| SciCode | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | INFO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [Imaging-101](../works/imaging-101.md)
- [OntoLearner](../works/ontolearner.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [SciConvBench](../works/sciconvbench.md)
- [AutoMat](../works/automat.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [CASCADE](../works/cascade.md)
- [AFMBench](../works/afmbench.md)
- [MatSciBench](../works/matscibench.md)
- [AtomWorld](../works/atomworld.md)
- [ChemX](../works/chemx.md)
- [MatQnA](../works/matqna.md)
- [MatCha](../works/matcha.md)
- [OpenXRD](../works/openxrd.md)
- [MatVQA](../works/matvqa.md)
- [MatTools](../works/mattools.md)
- [AlchemyBench](../works/alchemybench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [MaCBench](../works/macbench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatViX](../works/matvix.md)
- [SciCode](../works/scicode.md)
- [MatText](../works/mattext.md)
- [MaScQA](../works/mascqa.md)
