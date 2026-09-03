# Neuroscience & Cognitive Science

> [English](../../domains/neuroscience_cognitive_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

神经科学，连同心理学与认知科学。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| ScienceAgentBench | 2024 | 心理学与认知科学任务——其 102 个任务中的 28 个——提取自经同行评审的数据驱动发现工作流。 | 每个任务要求生成一个自包含的 Python 程序，复现真实论文中的分析。 | 有效执行加逐任务手写的成功检查器，对照专家标注参考；图形输出由 GPT-4o 评判。 | [→](../works/scienceagentbench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Life Sciences 分组下的神经科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Neuroscience 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文产物的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| MetaSyn | 2026 | 进行忠实于协议的系统综述与 meta 分析；心理学是其 422 个专家整理 meta 分析所覆盖的主题之一。 | 多阶段系统综述工作流：在掺入不合格干扰文献的共享 PubMed 文献库中，依据带结构化 PI/ECO 标准的研究问题找出应纳入的研究。 | 对照原综述作者实际纳入的研究集做识别评估，并以分阶段评估定位 meta 分析流程中的失败环节。 | [→](../works/metasyn.md) |
| BrainBench | 2024 | 预测神经科学实验的结果：在 Journal of Neuroscience 五个栏目上分辨真实与改动结果的摘要。 | 200 对原始/改动摘要（官方数据集）；静态二选一强制选择。 | LLM 以困惑度作答；人类专家附信心与专长评级；校准性单独分析。 | [→](../works/brainbench.md) |
| BrainBench (EEG) | 2026 | 理解 EEG：完成指令条件下的信号处理、定量证据与科学解读，并产出有依据的报告。 | 四个子集（基础、睡眠、神经认知、生理）覆盖 17 个数据集；逾 10 万次执行；CodeAct + agent 范式。 | 对输出做数值、类别、集合、序列、语义与产物校验。 | [→](../works/brainbench-eeg.md) |
| Model Discovery Agent | 2026 | 找出隐藏的 ion-channel mechanism，并预测 mystery neuron 在没见过的 stimulation protocol 下怎么响应。 | 六个 NeuronBench world，包含 deterministic 和 finite-channel-noise stochastic Hodgkin–Huxley dynamics；先给 2 条 passive trace，再允许最多 5 次 designed experiment。 | 在六项 electrophysiological feature 上确定性计算 held-out error，再检查 channel class 的 structural recovery，并比较 random、EIG 和 task-directed design。 | [→](../works/model-discovery-agent.md) |
| Rodent-Bench | 2026 | 从视频标注啮齿类行为：跨神经科学范式的时间分割与分类。 | 真实啮齿类行为视频（10–35 分钟），覆盖社交、理毛、抓挠、僵直范式；两个版本；3 个 MLLM。 | 逐秒准确率、宏 F1、平均精度均值、互信息与 Matthews 相关系数。 | [→](../works/rodent-bench.md) |
| CPsyExam | 2024 | 回答涵盖知识回忆与案例分析的心理学考试题。 | 从 22,000 道题库中精选、学科覆盖均衡的 4,000 道题；静态问答。 | 跨学科与两轴（心理学知识、案例分析）的准确率。 | [→](../works/cpsyexam.md) |
| ConceptPsy | 2023 | 以覆盖 12 个核心学科的全面概念回答心理学题目。 | 12 个学科、1,383 个人工收集的概念；每题标注到章节；静态问答。 | 总体加章节级（逐概念）准确率，显现逐概念差异。 | [→](../works/conceptpsy.md) |
| PsychCounsel-Bench | 2025 | 回答专业咨询心理学的认证考试题。 | 约 2,252 道来自美国国家咨询师认证考试的单选题；静态问答。 | 各模型对照该考试约 70% 及格线的准确率。 | [→](../works/psychcounsel-bench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | 自动化一条真实果蝇光遗传学数据到发现流水线的计算阶段——基于视频的身体/关键点追踪、行走行为分类、步态分割，以及各 GAL4 驱动品系相对遗传对照的统计比较。 | 七个有序的单阶段任务外加端到端流水线变体（共九个计算任务），基于约 47 GB 已发布的果蝇行为数据；agent 产出可运行代码，每个 agent–任务对三次试验。 | 阶段级成功标准锚定领域专家规范，对照专家人工标注与可信的旧有科学家编写代码库；统计阶段用 Mann–Whitney U 检验对照遗传对照组。 | [→](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| MiraMind | 2025 | 证据受限的心理健康与临床心理学推理——认知模式评估、咨询策略选择与精神科判断——其中解读所应有的具体程度与确定程度本身也在评估之列（归入 Neuroscience & Cognitive Science）。 | 覆盖 13 个数据集的六大任务族（评估、诊断、干预、多步精神科问答、抽象、核验），横跨非正式用户叙述、咨询对话、精神科执照式问答与 Cochrane 综述摘要；20 个 LLM。 | 各任务族的结果指标（Micro-F1、Jaccard、专家评分点召回、Macro-F1），外加在 100 条人工标注轨迹上验证的 LLM-as-judge 轨迹 rubric（可用性、逻辑结构、信息贡献）。 | [→](../works/miramind.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的神经科学与认知科学子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`COG` 认知科学与认知神经科学 · `PSY` 作为学科的心理学 · `CLIN` 临床与咨询心理学 · `MH` 心理健康与精神医学 · `BEH` 行为神经科学与动物行为 · `SYS` 系统与环路神经科学 · `CELL` 细胞与分子神经科学 · `DEV` 发育、可塑性与修复 · `DIS` 疾病神经生物学 · `EPHYS` 电生理与神经信号分析（EEG、MEG） · `SLEEP` 睡眠科学 · `IMG` 神经影像 · `CNEU` 计算与理论神经科学 · `GEN` 覆盖全领域或未具体说明，无单一子领域

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
| ResearchClawBench | BEH, SYS, CELL | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| ScienceAgentBench | PSY, COG | ✘ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✔ | ✔ | 2 | 1 | 3 | **8.5** |
| Neuroscience Data-to-Discovery Case Study | BEH, SYS | ? | ◐ | ◐ | ✔ | ◐ | ✔ | ✔ | **4.5** | ◐ | ✔ | ? | 3 | 0 | 4 | **8.5** |
| BrainBench (EEG) | EPHYS, SLEEP, COG | ? | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ? | 2 | 3 | 3 | **8.5** |
| Model Discovery Agent | EPHYS, CELL, CNEU | ✘ | ✔ | ✔ | ✘ | ✘ | ✘ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 0 | 4 | **8** |
| Rodent-Bench | BEH | ✘ | ✘ | ◐ | ✔ | ✘ | ✔ | ✘ | **2.5** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| MetaSyn | PSY, MH | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✘ | **2.5** | ◐ | ✘ | ◐ | 2 | 1 | 3 | **7** |
| BrainBench | COG, SYS, CELL, DIS, DEV | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ✔ | ✘ | ✔ | 3 | 2 | 3 | **10** |
| MiraMind | MH, CLIN | ? | ✘ | ✘ | ✘ | ◐ | ✔ | ✘ | **1.5** | ✘ | ✔ | ◐ | 2 | 3 | 2 | **8.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ? | ? | ? | ✔ | **1** | ✘ | ✘ | ◐ | 3 | 0 | 0 | **3.5** |
| ConceptPsy | PSY | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| CPsyExam | PSY, CLIN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 3 | 2 | **7.5** |
| PsychCounsel-Bench | CLIN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note：`?` 表示来源没有把这一列说清楚，不是仓库推断它不存在。这个区别在 `Net` 和跨领域套件的逐领域 `Scale` 上尤其重要，因为论文经常只报总任务数。

## Related Works

- [Model Discovery Agent](../works/model-discovery-agent.md)
- [BrainBench (EEG)](../works/brainbench-eeg.md)
- [MetaSyn](../works/metasyn.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MiraMind](../works/miramind.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [CPsyExam](../works/cpsyexam.md)
- [BrainBench](../works/brainbench.md)
- [ConceptPsy](../works/conceptpsy.md)
