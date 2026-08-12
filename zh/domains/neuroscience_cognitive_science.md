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
| Rodent-Bench | 2026 | 从视频标注啮齿类行为：跨神经科学范式的时间分割与分类。 | 真实啮齿类行为视频（10–35 分钟），覆盖社交、理毛、抓挠、僵直范式；两个版本；3 个 MLLM。 | 逐秒准确率、宏 F1、平均精度均值、互信息与 Matthews 相关系数。 | [→](../works/rodent-bench.md) |
| CPsyExam | 2024 | 回答涵盖知识回忆与案例分析的心理学考试题。 | 从 22,000 道题库中精选、学科覆盖均衡的 4,000 道题；静态问答。 | 跨学科与两轴（心理学知识、案例分析）的准确率。 | [→](../works/cpsyexam.md) |
| ConceptPsy | 2023 | 以覆盖 12 个核心学科的全面概念回答心理学题目。 | 12 个学科、1,383 个人工收集的概念；每题标注到章节；静态问答。 | 总体加章节级（逐概念）准确率，显现逐概念差异。 | [→](../works/conceptpsy.md) |
| PsychCounsel-Bench | 2025 | 回答专业咨询心理学的认证考试题。 | 约 2,252 道来自美国国家咨询师认证考试的单选题；静态问答。 | 各模型对照该考试约 70% 及格线的准确率。 | [→](../works/psychcounsel-bench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | 自动化一条真实果蝇光遗传学数据到发现流水线的计算阶段——基于视频的身体/关键点追踪、行走行为分类、步态分割，以及各 GAL4 驱动品系相对遗传对照的统计比较。 | 七个有序的单阶段任务外加端到端流水线变体（共九个计算任务），基于约 47 GB 已发布的果蝇行为数据；agent 产出可运行代码，每个 agent–任务对三次试验。 | 阶段级成功标准锚定领域专家规范，对照专家人工标注与可信的旧有科学家编写代码库；统计阶段用 Mann–Whitney U 检验对照遗传对照组。 | [→](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| MiraMind | 2025 | 证据受限的心理健康与临床心理学推理——认知模式评估、咨询策略选择与精神科判断——其中解读所应有的具体程度与确定程度本身也在评估之列（归入 Neuroscience & Cognitive Science）。 | 覆盖 13 个数据集的六大任务族（评估、诊断、干预、多步精神科问答、抽象、核验），横跨非正式用户叙述、咨询对话、精神科执照式问答与 Cochrane 综述摘要；20 个 LLM。 | 各任务族的结果指标（Micro-F1、Jaccard、专家评分点召回、Macro-F1），外加在 100 条人工标注轨迹上验证的 LLM-as-judge 轨迹 rubric（可用性、逻辑结构、信息贡献）。 | [→](../works/miramind.md) |

## Related Works

- [MiraMind](../works/miramind.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MetaSyn](../works/metasyn.md)
- [BrainBench](../works/brainbench.md)
- [BrainBench (EEG)](../works/brainbench-eeg.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [CPsyExam](../works/cpsyexam.md)
- [ConceptPsy](../works/conceptpsy.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
