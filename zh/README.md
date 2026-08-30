# 科学评估环境（Scientific Evaluation Environments）

> [English](../README.md) | **简体中文**

这个知识库追踪两件事：科学和工程 AI agent 怎样被评估，评估结果又怎样回到开发过程里。

核心想法很直接：一个分数不应该只说 agent 成功了还是失败了，它还应该帮人判断下一步改什么。比如一个科研 agent 没能复现论文结果，真正有用的问题是：plan 选错了，tool call 失败了，verifier 漏掉了错误，还是预算用完了？四种原因对应四种修法。

这个仓库追踪的就是这条闭环：

```text
任务 → agent 执行 → 评估 → 诊断 → 修改系统 → 再次评估
```

每张 work card 记录一篇论文或一个项目实际贡献了什么。三组索引让读者从不同问题找到同一张卡：**topic** 看它解决哪个评估问题，**domain** 看任务落在哪个学科，**activity** 看 agent 实际做什么。Topic 页再把这些卡连成文献脉络，解释各种方法到底差在哪里。

本仓库是参考资料，不是 benchmark 实现。[解释写作规范](./EXPLANATION_STYLE.md) 约束所有正文：写清谁在做什么，原来哪一步有问题，新方法改了哪一步，以及这个结果还不能证明什么。

---

## 持续演进的知识库

这个集合会跟着领域一起变。每隔三天，自动更新 agent 会从公开来源寻找新工作。它会起草卡片和索引更新，但不会直接发布。每批内容都要通过 pull request，由人检查来源、分类、文字和中文镜像后才能合并。

---

## 从这里开始

- **[按 Topic 浏览](./topics/README.md)**：从一个评估问题出发，先看具体例子怎样变化，再比较相关文献。
- **[按 Domain 浏览](./domains/README.md)**：查某个科学或工程领域内有哪些评估工作。
- **[按 Research Activity 浏览](./activities/README.md)**：按受评 agent 或系统实际执行的任务查找工作。
- **[浏览全部 Works](./works/README.md)**：查看已收录的全部工作卡片。
- **[按首次公开时间浏览](./WORKS_BY_DATE.md)**：按首次公开日期从新到旧查看全部 works。
- **[阅读月度报告](./monthly/README.md)**：查看每个月知识库新增了什么，以及这些工作放在一起带来了什么新认识。

先看你手里带着什么问题，再选入口：

```
Topic     →  代表性 works       →  原始论文   （测什么/怎么测/怎样使用评估）
Domain    →  该领域中的评估工作  →  原始论文   （任务位于哪个领域）
Activity  →  执行该任务的工作    →  原始论文   （agent 做什么）
```

这三组不是互相排斥的分类。一个化学 agent benchmark 可以同时属于多个 topic、一个 domain 和多个 activity。每条链接只是在回答同一份工作的不同问题。

---

## 按 Topic 浏览

Topic 从一个评估问题出发。有的问测什么，比如 planning 或 long-horizon work；有的问测量本身可不可信；还有的问 evaluation feedback 怎样改变 skill、harness、data 和 post-training。每个 topic 页会先讲清这个问题，再组织代表性方法，最后用适合这个问题的维度做比较。完整索引见 [`topics/`](./topics/README.md)。

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

Domain 页回答的问题更具体：受评工作发生在哪个学科？一个物理 benchmark 和一个生物 benchmark 可以用同一种 evaluation method，但它们的 tool、artifact、cost 和正确性标准可能完全不同。下面的数字表示当前收录量，正式索引和各领域表格见 [`domains/`](./domains/README.md)。

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

Activity 页跟着 agent 实际完成的工作走。它是在搜文献、跑 simulation、设计 experiment、复现结果，还是把一个研究项目从头做到尾？同一项 activity 可以出现在多个 domain，也可以用多种 evaluation method。如果一份工作根本不评估科学或研究任务，比如 survey 或纯评估方法，它会明确标成 `N/A`。完整索引见 [`activities/`](./activities/README.md)。

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

如果 evaluation 改变了我们对系统的认识，或者改变了开发闭环的下一步，这份工作就在范围内。这包括 benchmark、diagnostic method、evaluator validation、benchmark-validity research、科学 workflow，以及用 evaluation 修改 skill、harness、data 或 post-training 的系统。

一篇论文有 benchmark 分数，不等于它自动进入范围。如果 evaluation 只在最后的 results table 里出现，纯 training、optimization、data、memory 或 multi-agent work 仍然不收。具体判断时看这几件事：evaluation 有没有定义 objective，提供 feedback，选择 intervention，诊断 failure，或直接成为 experiment environment。

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
