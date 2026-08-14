# CASCADE (2025)

> [English](../../works/cascade.md) | **简体中文**

## Overview

CASCADE 是一个自我演化的 agentic 框架：agent 借助持续学习与自我反思两项 meta-skill，为科学工作获取并积累可执行的 skill；随框架发布的 SciSkillBench 含 116 个材料科学与化学任务，用来衡量积累下来的 skill 究竟值多少。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.23880>
- **Code:** <https://github.com/CederGroupHub/CASCADE>
- **Data:** <https://doi.org/10.6084/m9.figshare.30924998>

## Summary

论文认为当前的科学 agent 受限于对预定义工具的依赖，或停留在工具生成的早期阶段，并主张从「LLM + 工具使用」转向「LLM + skill 获取」。CASCADE 给 agent 配了两项 meta-skill：持续学习，途径是网页搜索、从文档中抽取代码以及利用记忆；自我反思，途径是内省与知识图谱探索。这样学到的 skill 会被持久化，跨会话复用，还能在 agent 之间以及 agent 与人类科学家之间共享。为衡量效果，作者提出 SciSkillBench——一套精心整理的 116 个材料科学与化学研究任务，并把完整系统与去掉演化机制的若干配置作对比。benchmark 之外，论文还展示了计算分析、自主实验室实验以及对已发表论文的选择性复现等应用。

## Tasks

SciSkillBench 含 116 个材料科学与化学研究任务，分为 76 个数据类任务（数据检索、分析、管理与处理）和 40 个计算类任务（仿真，以及需要专门模型或工具包的问题）。任务另按需求说明的详细程度切分：58 个 Level 0 任务允许用户指定要用的关键函数，58 个 Level 1 任务只给出高层目标。论文称这套任务是「精心整理」的，但在所查阅的章节中未详述其来源与整理流程。论文称，DeepSolver agent 的 benchmark 运行是在关闭全部记忆工具、且无人工干预的条件下完成的。

## Domains

材料科学与化学。任务要求操作专门的材料与化学工具包、检索并处理材料数据、运行仿真；论文的 arXiv 分类为 cs.AI 与 cond-mat.mtrl-sci。自主实验室的演示另外触及实验化学，但那是演示，不属于计分的 benchmark。

## Evaluation

基于结果的自动打分：把 agent 处理后的输出在预设容差阈值内与标准答案自动比对，报告指标为成功率。每种系统配置各跑三次独立重复，实验总数为 16,008 次。对比的配置有 Native（无演化机制）、Search & Debug（S&D）、DeepSolver（论文提出的四步顺序工作流，带条件式并行调试）以及一个 Claude Code 基线。受评的基座模型包括 GPT-5、GPT-5-mini、GPT-5-nano、O3、O4-mini、GPT-4.1、GPT-4.1-mini、GPT-4.1-nano、Qwen3-Coder-30B-A3B-Instruct-FP8 与 Claude-Sonnet-4.5。以 GPT-5 为基座时，DeepSolver 成功率达 93.26%，Native 为 35.36%；O3 达到 91.84%。消融实验逐一移除持续学习与自我反思这两项 meta-skill。

## Typical Duration

TODO(reference) — 所查阅的章节未报告单任务的步数、token 与 wall-clock 预算；唯一给出的资源总量数字，是跨配置与重复合计的 16,008 次实验运行。

## Main Contribution

按作者的说法，这是科学 agent 从工具使用转向 skill 获取这一转变的一次早期实例：agent 通过持续学习与自我反思，把知识固化为可执行、可持久、可共享的 skill；SciSkillBench 则是用来佐证这一点的手段——增益来自积累的 skill，而非基座模型。

## Key Design Ideas

- 用两项 meta-skill 取代固定工具集：持续学习（网页搜索、代码抽取、记忆利用）与自我反思（内省、知识图谱探索）。
- 混合双存储的 skill 与知识记忆——一个部署在 Supabase 上的 PostgreSQL 库做基于向量的语义检索，一个 Neo4j 图数据库刻画材料、性质与计算工具之间的实体关系。
- 会话级记忆（引用先前对话）与固化记忆（留存并检索关键信息、经验与 skill 集合）分开。
- 积累下来的 skill 交给 DeepSolver 消费：这是一条四步顺序求解的工作流，带条件式并行调试。
- SciSkillBench 采用两轴任务切分——数据类对计算类、Level 0 对 Level 1 的说明详细程度——使结果能把工具熟练度与目标理解分开。
- skill 以可执行工件的形式表示，供 agent 之间以及与人类科学家共享，而不是自由文本笔记。

## Strengths

- 在同一批任务上对照 Native 基线做消融，把演化机制单独隔离出来，93.26% 对 35.36% 的差距因而可以归因于积累的 skill，而非基座模型。
- 基座模型覆盖面广，共十个（含一个开放权重模型），支撑了「扩大基座带来的收益不如框架」这一论断。
- 每种配置三次独立重复，避免了执行式 benchmark 上的单次运行方差。
- 头条指标靠对照标准答案的容差式自动核对，不依赖 LLM 评判者。
- 代码与 benchmark 数据均已发布，数据记录还带 DOI 归档。

## Limitations

- 论文承认，该工作流距离能产出真正新颖洞见的自主端到端发现仍很远，且如何识别最优工具、如何在工作流中正确排布它们，仍是开放难题。
- SciSkillBench 的任务来源，论文只说是精心整理；所查阅的章节没有交代构造流程，也没有交代标准答案的出处。
- benchmark 评的是任务成功与否，而不是诱导出的 skill 本身——skill 的正确性、冗余度与复用率都没有直接测量，因此 skill 库的价值只能从下游成功率间接推断。
- 基座覆盖以某一家厂商的模型为主，开放权重模型与 Anthropic 模型各只有一个。
- 实验室自动化与论文复现的结果属于计分 benchmark 之外的演示，没有对照基线。
- Repository note: 该工作落在现有主题轴上略显别扭——它的主题是从经验中构造可复用的 skill，而非把一项能力拆解为可计分的子技能，后者才是 Skill Hierarchy 主题所覆盖的内容。

## Related Works

- [MatTools](./mattools.md) — 同样考察材料科学的工具能力，但用的是固定、预先写好的工具包（pymatgen），正是 CASCADE 所反对的设定。
- [GATE](./gate.md) — 语料中另一个构建并演化可复用工具结构的框架，而不是为固定的能力拆解打分。
- [SkillSV](./skillsv.md) — 为 agent skill 的内部单元估值，与「agent 能不能自己造出这个 skill」互为补充。
- [MatSciBench](./matscibench.md) — 同一领域的材料科学推理，停留在问答层面，不涉及执行与 skill 积累。
- [AlchemyBench](./alchemybench.md) — 同领域的端到端材料合成 benchmark，由 LLM 评判，而非对照标准答案执行判定。
