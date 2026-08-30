# 科学评估环境（Scientific Evaluation Environments）

> [English](../README.md) | **简体中文**

一个开放的知识库，研究**科学与工程 AI agent 的 evaluation**：测什么、怎么设计和解释评估，以及怎样用评估推动系统改进。

**Evaluation 不只用于测量 AI 系统，也是构建系统时的反馈机制。** 本仓库覆盖完整闭环：测量、诊断、干预、再次评估，并追踪 planning、trajectory、skill、harness、data 和 post-training 的变化。

每份工作都有一张简明的事实卡片。卡片按三条互不从属的轴组织：**topic** 看它要解决哪个评估问题，**domain** 看任务落在哪个科学领域，**activity** 看受评 agent 到底做什么。Topic 页会先讲实际问题，让一个具体例子走一遍，再梳理相关文献。你可以从手头的问题出发，顺着链接找到代表性工作，最后回到原始资料。

本仓库是参考资料，不是 benchmark 实现。文档遵循[解释写作规范](./EXPLANATION_STYLE.md)：把 actor 和改变的步骤写出来；需要时让一条真实 trace 走完整个过程；最后说明结论没有证明什么。

---

## 持续演进的知识库

科学评估环境是持续维护的，而不是定期发布。一个自动更新 agent 每隔三天扫描公开来源、寻找新工作，把其中相关的内容整合进知识库，并通过 pull request 提交更新、交由人工审核。

---

## 从这里开始

- **[按 Topic 浏览](./topics/README.md)**：从一个评估问题出发，先看具体例子怎样变化，再比较相关文献。
- **[按 Domain 浏览](./domains/README.md)**：查某个科学或工程领域内有哪些评估工作。
- **[按 Research Activity 浏览](./activities/README.md)**：按受评 agent 或系统实际执行的任务查找工作。
- **[浏览全部 Works](./works/README.md)**：查看已收录的全部工作卡片。

三条轴是覆盖同一批卡片的平级入口：

```
Topic     →  代表性 works       →  原始论文   （测什么/怎么测/怎样使用评估）
Domain    →  该领域中的评估工作  →  原始论文   （任务位于哪个领域）
Activity  →  执行该任务的工作    →  原始论文   （agent 做什么）
```

一份工作可以同时归入多个 topic、domain 与 activity。它们是看同一份工作的不同角度，不是互斥分类。

---

## 按 Topic 浏览

Topic 是**evaluation research 轴**，覆盖被测能力与行为、评估的设计和解释，以及 evaluation-driven improvement。每个页面都是一篇带专属比较表的文献综述。完整索引见 [`topics/`](./topics/README.md)。

| Topic | 你会读到什么 |
|---|---|
| [General Long-Horizon Agent Benchmarks](./topics/long_horizon_evaluation.md) | 任务需经过许多次连续决策、工具调用或交互回合的 benchmark——失败会逐步累积，中间状态至关重要。 |
| [Scientific Agent Benchmarks](./topics/scientific_agents.md) | 让 agent 完成取自真实科研与实践的任务，以已发表或专家给定的结果为对照评判。 |
| [Planning & Decision-Making Evaluation](./topics/planning_decision_evaluation.md) | 面对当前状态、目标、约束、工具和证据，agent 能否选出合理的计划或下一步，并在收到反馈后妥善调整。 |
| [Hierarchical Decision Abstraction](./topics/hierarchical_decision_abstraction.md) | 应该怎样在目标、策略、子目标、语义 action、primitive action 和控制信号这些层级上表示、评价和优化 agent 行为。 |
| [Trajectory Evaluation](./topics/trajectory_evaluation.md) | 对整条动作与中间状态序列打分的方法，而不仅看最终答案。 |
| [Skill Hierarchy](./topics/skill_hierarchy.md) | 把一项复杂能力拆解为更细的子技能，并分别打分。 |
| [Credit Assignment](./topics/credit_assignment.md) | 把一条 trajectory 的成败归因到具体步骤或子目标——稠密奖励、部分给分、逐步打分。 |
| [Resource-aware Evaluation](./topics/resource_aware_evaluation.md) | 把 token、费用、墙钟时间或算力纳入 benchmark 的测量范围——有时更作为显式的优化目标。 |
| [Evaluator Reliability & Validation](./topics/evaluator_reliability_validation.md) | 用人工或确定性 ground truth 验证 judge、reward model、rubric 和 verifier。 |
| [Benchmark Design, Validity & Contamination](./topics/benchmark_design_validity_contamination.md) | 任务构造、verifier 严谨度、contamination 控制、动态评估与现实有效性。 |
| [Skill Learning & Evolution](./topics/skill_learning_evolution.md) | 把经验和反馈转成可复用 skill，并测试迁移和失败模式。 |
| [Agent Harnesses & Scaffolding](./topics/agent_harnesses_scaffolding.md) | 测量、归因和优化围绕模型运行的控制结构。 |
| [Evaluation-Driven Data Curation](./topics/evaluation_driven_data_curation.md) | 根据 downstream evaluation feedback 修改数据选择、生成、过滤与 mixture policy。 |
| [Evaluation-Driven Post-Training](./topics/evaluation_driven_post_training.md) | 让 evaluation 成为模型和 agent 改进的目标、反馈或实验环境。 |
| [Survey](./topics/survey.md) | 关于 agent 评估的综述与立场论文——是参考文献的索引，而非任务套件。 |

---

## 按 Domain 浏览

Domain 是**领域轴**：一份工作在哪个科学或工程学科内评估，与 topic 平级。work 数量反映当前覆盖情况；权威索引与各页比较表见 [`domains/`](./domains/README.md)。

**科学**

| Domain | Works |
|---|--:|
| [Physics](./domains/physics.md) | 47 |
| [Chemistry](./domains/chemistry.md) | 38 |
| [Biology](./domains/biology.md) | 38 |
| [Materials Science](./domains/materials_science.md) | 28 |
| [AI & Machine Learning Research](./domains/ai_ml_research.md) | 27 |
| [Mathematics](./domains/mathematics.md) | 19 |
| [Medicine & Health](./domains/medicine_health.md) | 22 |
| [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | 12 |
| [Astronomy](./domains/astronomy.md) | 34 |
| [Earth Science](./domains/earth_science.md) | 12 |
| [Computer Science](./domains/computer_science.md) | 7 |
| [Environmental Science](./domains/environmental_science.md) | 6 |

**工程**

| Domain | Works |
|---|--:|
| [Electrical Engineering](./domains/electrical_engineering.md) | 18 |
| [Robotics](./domains/robotics.md) | 18 |
| [Software & Systems Engineering](./domains/software_systems_engineering.md) | 18 |
| [Mechanical & Aerospace Engineering](./domains/mechanical_aerospace_engineering.md) | 12 |
| [Energy Systems](./domains/energy_systems.md) | 5 |
| [Civil & Structural Engineering](./domains/civil_structural_engineering.md) | 30 |
| [Chemical Engineering](./domains/chemical_engineering.md) | 12 |

更细的领域折并入这些规范化 domain（bioinformatics → Biology、GIS → Earth Science、psychology → Neuroscience & Cognitive Science 等），一份工作也可出现在多个 domain。web/UI agent、computer use 与纯评估方法学不属于科学或工程领域，不在此列出。


---

## 按 Research Activity 浏览

活动是**任务轴**：受评 agent 或系统实际做什么，与领域和评估方法无关。一份工作可以执行多项活动；不评估任何科学或研究任务的工作（综述、纯方法学、通用型 benchmark）标注为 `N/A`，不出现在任何活动页上。完整索引见 [`activities/`](./activities/README.md)。

| Activity | 涵盖内容 | Works |
|---|---|--:|
| [科学问题求解与推理](./activities/scientific_problem_solving_reasoning.md) | 科学问答、推导、证明、定量与多模态问题求解、诊断推理 | 94 |
| [科学软件与工作流工程](./activities/scientific_software_workflow_engineering.md) | 科学/工程代码、仓库与流水线工程、HDL 与形式化规约代码 | 71 |
| [数据分析与统计推断](./activities/data_analysis_statistical_inference.md) | 统计分析与推断、生物信息学/组学分析、数据解读 | 43 |
| [实验设计与科学发现](./activities/experiment_design_discovery.md) | 实验与观测规划、假设生成、规律发现 | 22 |
| [模拟与科学计算](./activities/simulation_scientific_computing.md) | 数值模拟、PDE/FEM、MD/DFT、运行与构建科学模拟器 | 35 |
| [文献检索与证据综合](./activities/literature_evidence_synthesis.md) | 文献检索、系统综述、证据综合、以文献为依托的抽取 | 23 |
| [建模与预测](./activities/modeling_prediction.md) | 预测与代理建模、性质预测、预报 | 21 |
| [优化与工程设计](./activities/optimization_engineering_design.md) | 参数与控制器调优、工程/逆向设计、材料与分子设计 | 26 |
| [研究复现与重复](./activities/research_reproduction_replication.md) | 复现已发表的分析、结果与方法；匹配已报告的结论 | 11 |
| [端到端研究](./activities/end_to_end_research.md) | 跨越多个主要阶段的多阶段研究生命周期 | 9 |
| [实验室与仪器控制](./activities/laboratory_instrument_control.md) | 仪器、显微镜与光束线控制、实验室自动化、行为定义的控制代码 | 3 |

---

## 范围

**在范围内：** 科学与工程 agent evaluation，包括 benchmark、方法、诊断、evaluator validation、benchmark validity、科学工作流，以及由 evaluation 驱动的 skill learning、harness optimization、data curation 和 post-training。

**暂不在范围内：** evaluation 只出现在常规结果章节里的训练、优化、数据和 agent implementation 工作；没有 evaluation-centered contribution 的通用 multi-agent 或 memory system。

判断标准是 evaluation 是否真正控制开发过程。如果它决定 objective、feedback、selection、diagnosis 或实验 loop，改进工作就在范围内；只报告 benchmark 分数不够。

"Works" 比 "benchmarks" 更广：集合中收录 benchmark、评估方法学、评估框架、面向评估的 RL 工作、综述与立场论文的卡片，每张卡片都会显式标注类型。目前共有 **381 张卡片**、**15 个 topic 页**、**19 个 domain 页**、**11 个 activity 页**，并在 [`zh/`](./README.md) 下配有中文镜像。

---

## 仓库结构

知识库分**四层**：works 层，以及其上三条平级的聚合轴。

| 目录 | 作用 |
|---|---|
| [`works/`](./works/README.md) | 每份工作一张事实性参考卡片。扁平目录、kebab-case，每份一个 Markdown 文件。 |
| [`topics/`](./topics/README.md) | 文献综述页，覆盖 measurement、diagnosis 与 improvement。每个 topic 拥有专属比较表。 |
| [`domains/`](./domains/README.md) | 领域轴参考页，每个规范化科学或工程 domain 一页，含一张列固定的比较表。 |
| [`activities/`](./activities/README.md) | 任务轴参考页，每个规范化研究活动一页，含定义、范围、任务模式综述与比较表。 |
| [`zh/`](./README.md) | 每个页面的中文镜像，每完成一批英文后同步。 |

topic 与 activity 两轴靠双向约定保持同步：每张卡片的 `Topics`／`Activities` 块向上链接到所属页面，每个页面的 `Related Works` 再向下链回卡片；domain 映射则在 domain 页单向维护。根目录的 [`AGENT.md`](../AGENT.md) 是仓库章程，[`CLAUDE.md`](../CLAUDE.md) 是其速查；各目录自己的 `README.md` 记录该层的页面模板与规则。

---

## 贡献须知

欢迎贡献。自动更新是对社区贡献的补充，而非替代；若有遗漏或新出现的相关工作，仍可手动提交。所有面向贡献者与维护者的规则——引用校验、页面模板、规范化分类法与双语同步节奏——都在 [`AGENT.md`](../AGENT.md)（章程）与 [`CLAUDE.md`](../CLAUDE.md)（章程速查）中，各目录的 README 给出层内规则。每个页面都有英文与中文两个版本，使用任意页面顶部的语言切换器即可切换。
