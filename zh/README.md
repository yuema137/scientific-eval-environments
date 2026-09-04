# 科学评估环境（Scientific Evaluation Environments）

> [English](../README.md) | **简体中文**

如果你做科学、工程，或者做 AI，很快就会碰到一个问题：agent benchmark 论文很多，但你不容易一下看明白它到底在测什么、对应哪类真实 workflow、以及失败以后你到底能从里边学到啥。

这个仓库就是拿来把这件事讲清楚的。

它收集的是科学与工程 AI agent 的评估工作，但不只盯着“模型拿了多少分”。真正有用的问题是，这个分数能不能告诉你下一步该改哪儿。比如一个 agent 没复现出论文结果，问题可能出在 plan、tool use、verifier、任务设计，或者预算不够。这几种问题不是一回事，修法也不一样。

换句话说，这个仓库盯的是这条闭环：

![评估闭环](../site/assets/readme-eval-loop.svg)

仓库本身不复杂：

- 一张 work card 讲清一篇论文或一个项目到底贡献了什么。
- 三组平级索引让你从不同问题找到同一张卡。
- 月报讲的是文献结构怎么变了，不只是这个月又多了哪些 PDF。

![仓库结构图](../site/assets/readme-repo-map.svg)

这是参考资料库，不是 benchmark 实现仓库。[解释写作规范](./EXPLANATION_STYLE.md) 约束正文都得写人话：谁在做什么，哪一步变了，必要时跟一条具体对象走一遍流程，同时把边界讲清楚，别把结论写过头。

---

## 从哪开始看

> **在线交互页面：** [打开 SciEval](https://yuema137.github.io/scieval/) 可以搜索、筛选，还能按图和时间线浏览整个仓库。这里的 Markdown 才是唯一真源，网站只是自动生成的展示快照。

你手上如果已经带着问题，直接按问题选入口：

| 如果你想问的是…… | 从这里开始 |
|---|---|
| “这篇 work 真正在解决哪个评估问题？” | [Topics](./topics/README.md) |
| “物理 / 化学 / 生物 / 机器人 / 土木这些领域各有哪些 work？” | [Domains](./domains/README.md) |
| “哪些 benchmark 真让 agent 去做文献综述、模拟、实验设计或复现？” | [Activities](./activities/README.md) |
| “这个 benchmark / 方法本身到底是怎么回事？” | [Works](./works/README.md) |
| “最近新增了什么，以及为什么值得看？” | [月度报告](./monthly/README.md) |
| “我想按最早公开时间看整个时间线。” | [按首次公开时间浏览](./WORKS_BY_DATE.md) |
| “我想直接看交互式页面。” | [SciEval explorer](https://yuema137.github.io/scieval/) |

这几组入口不是互相打架的分类，而是读同一批 work 的三种方式：

```text
Topic     → 这份 work 在解决哪个评估问题？
Domain    → 它落在哪个科学或工程领域？
Activity  → 被评估的 agent 实际在做什么？
```

同一份 work 可以同时出现在多个 topic、多个 domain、多个 activity 下。

---

## 什么算在范围里

最短的版本就是：

- 如果 evaluation 是核心，这个 work 就在范围里
- 如果 evaluation 只是最后一张 results table，它通常不在范围里

具体来说，这个仓库会收：

- 科学与工程 agent benchmark
- trajectory、judge、credit assignment、resource use 这些评估方法
- benchmark validity、contamination、verifier design 相关工作
- 用 evaluation 去驱动 skill、harness、data curation、post-training 改进的工作
- 有助于把整个空间讲明白的 survey 和 position paper

但普通训练论文、普通 agent 论文，不会因为最后报了几个 benchmark 分数就自动收进来。判断标准很具体：evaluation 有没有定义 objective、提供 feedback、承担 diagnosis、决定 intervention，或者直接构成 experiment environment？

## 这个仓库怎么读

最不容易绕晕的方法，就是记住每一层各管什么：

- [Works](./works/README.md) 是事实卡片，讲单篇论文、单个 benchmark、单种方法、单篇 survey。
- [Topics](./topics/README.md) 是围绕评估问题写的文献综述。
- [Domains](./domains/README.md) 讲 work 落在哪个科学或工程领域。
- [Activities](./activities/README.md) 讲 agent 实际在做哪类研究任务。
- [Monthly reports](./monthly/README.md) 讲每个月文献结构怎么变。

Markdown 文件才是唯一真源。HTML explorer 只是从这些 Markdown 自动导出来的展示层。

## 当前覆盖情况

现在仓库里有：

- **384** 张 work card
- **15** 个 topic 页面
- **19** 个 domain 页面
- **11** 个 activity 页面
- **32** 份月报，覆盖 2024-01 到 2026-08

目前收录最密的地方，主要集中在：

- scientific agent benchmarks
- trajectory evaluation
- physics、chemistry、biology、astronomy、civil/structural engineering
- scientific problem solving、scientific software/workflow engineering、data analysis

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
| [Physics](./domains/physics.md) | 48 |
| [Chemistry](./domains/chemistry.md) | 39 |
| [Biology](./domains/biology.md) | 38 |
| [Materials Science](./domains/materials_science.md) | 28 |
| [AI & Machine Learning Research](./domains/ai_ml_research.md) | 28 |
| [Mathematics](./domains/mathematics.md) | 19 |
| [Medicine & Health](./domains/medicine_health.md) | 22 |
| [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | 13 |
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
| [科学软件与工作流工程](./activities/scientific_software_workflow_engineering.md) | 科学/工程代码、仓库与流水线工程、HDL 与形式化规约代码 | 72 |
| [数据分析与统计推断](./activities/data_analysis_statistical_inference.md) | 统计分析与推断、生物信息学/组学分析、数据解读 | 44 |
| [实验设计与科学发现](./activities/experiment_design_discovery.md) | 实验与观测规划、假设生成、规律发现 | 23 |
| [模拟与科学计算](./activities/simulation_scientific_computing.md) | 数值模拟、PDE/FEM、MD/DFT、运行与构建科学模拟器 | 35 |
| [文献检索与证据综合](./activities/literature_evidence_synthesis.md) | 文献检索、系统综述、证据综合、以文献为依托的抽取 | 23 |
| [建模与预测](./activities/modeling_prediction.md) | 预测与代理建模、性质预测、预报 | 22 |
| [优化与工程设计](./activities/optimization_engineering_design.md) | 参数与控制器调优、工程/逆向设计、材料与分子设计 | 27 |
| [研究复现与重复](./activities/research_reproduction_replication.md) | 复现已发表的分析、结果与方法；匹配已报告的结论 | 11 |
| [端到端研究](./activities/end_to_end_research.md) | 跨越多个主要阶段的多阶段研究生命周期 | 9 |
| [实验室与仪器控制](./activities/laboratory_instrument_control.md) | 仪器、显微镜与光束线控制、实验室自动化、行为定义的控制代码 | 3 |

---

## 范围

如果 evaluation 改变了我们对系统的认识，或者改变了开发闭环的下一步，这份工作就在范围内。这包括 benchmark、diagnostic method、evaluator validation、benchmark-validity research、科学 workflow，以及用 evaluation 修改 skill、harness、data 或 post-training 的系统。

一篇论文有 benchmark 分数，不等于它自动进入范围。如果 evaluation 只在最后的 results table 里出现，纯 training、optimization、data、memory 或 multi-agent work 仍然不收。具体判断时看这几件事：evaluation 有没有定义 objective，提供 feedback，选择 intervention，诊断 failure，或直接成为 experiment environment。

"Works" 比 "benchmarks" 更广：集合中收录 benchmark、评估方法学、评估框架、面向评估的 RL 工作、综述与立场论文的卡片，每张卡片都会显式标注类型。目前共有 **383 张卡片**、**15 个 topic 页**、**19 个 domain 页**、**11 个 activity 页**，并在 [`zh/`](./README.md) 下配有中文镜像。

---

## 持续维护，而不是一次性发布

这个仓库是持续维护的。

每三天，自动更新 agent 会从公开来源找新 work，起草 cards 和索引更新，再发一个 pull request 给人审。每个月 1 号，仓库还会为上个月生成一份中英双语月报。日更链路和月报链路都支持手动触发，所以维护者可以中途补跑某个窗口，但不会凭空再造第二份同月文件。

## 交互式 explorer

GitHub 仓库很适合维护和追溯，不太适合做视觉浏览。配套的 explorer 就是为了解这个问题，但它不会改变真源。

这个 explorer：

- 作为独立的 `/scieval/` 子页面，部署在维护者的 GitHub Pages 个人站里
- 读取从仓库 Markdown 导出的 JSON
- 提供可搜索、可筛选的交互式浏览界面
- 补上时间线和结构图这类更适合视觉理解的东西

相关 Markdown 合并以后，自动 workflow 会先构建并检查一份自包含的静态快照。检查通过后，它只更新个人站仓库里的 `scieval/**`，不会碰主页的其他文件。中间任何一步失败，线上继续使用上一份快照，个人主页也照常工作。

但 explorer **不拥有内容**。如果网页和某个 Markdown 文件说的不一样，以 Markdown 为准。

### 网站怎么保持同步

相关改动合并到 `main` 后，[`Publish Explorer Snapshot`](../.github/workflows/explorer-pages.yml) 会从仓库 Markdown 重新构建并检查网站。检查通过后，它会在个人主页仓库里开一个受保护的机器 PR，而且只改 `scieval/**`。个人主页会再次校验快照，确认没问题才合并和部署。构建或校验失败时，线上继续用上一版快照，个人主页的其他内容也不会被碰。

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
