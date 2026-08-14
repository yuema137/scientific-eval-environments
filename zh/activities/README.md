# Research Activities

> [English](../../activities/README.md) | **简体中文**

按**研究活动轴**组织的参考页——依据「受评 agent 或系统实际做什么」对 works 分组。研究活动是与 [`../topics/`](../topics/README.md) 的方法论轴、[`../domains/`](../domains/README.md) 的领域轴平级的第三条导航层：

```
Topic     →  代表性 works  →  原始论文   （为什么/如何评估）
Domain    →  该领域中的 works  →  原始论文   （任务位于哪个领域）
Activity  →  执行该任务的 works  →  原始论文   （agent 做什么）
```

- **Topic**——一份工作所关联的评估或研究*主题*。
- **Domain**——一份工作所立足的科学或工程*领域*。
- **Activity**——受评 agent 所执行的实质性科学或研究*任务*。

带着「哪些 benchmark 让 agent *设计实验*？*复现*论文？*求解*物理题？」这类问题而来的读者，可从这里出发，顺链接进入 [`../works/`](../works/README.md)，再到原始论文。

## 规范化分类

活动集合是固定的。新增、重命名或删除某个活动需同步更新 [`../AGENT.md`](../AGENT.md)。数量为当前映射到各活动的 work 卡片数（一份工作可归入多个活动）。

| Activity | 涵盖内容 | Works |
|---|---|--:|
| [文献检索与证据综合](./literature_evidence_synthesis.md) | 文献检索、研究筛选、系统综述、证据综合、以文献为依托的抽取 | 20 |
| [科学问题求解与推理](./scientific_problem_solving_reasoning.md) | 科学问答、推导、证明、定量与多模态问题求解、诊断推理 | 93 |
| [数据分析与统计推断](./data_analysis_statistical_inference.md) | 预处理、统计分析与推断、生物信息学/组学分析、数据解读 | 41 |
| [建模与预测](./modeling_prediction.md) | 预测与代理建模、性质预测、预报、以模型为核心产物的拟合 | 20 |
| [模拟与科学计算](./simulation_scientific_computing.md) | 数值模拟、PDE/FEM、MD/DFT、运行与构建科学模拟器 | 32 |
| [实验设计与科学发现](./experiment_design_discovery.md) | 实验与观测规划、主动测量、假设生成、规律发现 | 21 |
| [实验室与仪器控制](./laboratory_instrument_control.md) | 仪器、显微镜与光束线控制、实验室自动化、行为定义的控制代码 | 3 |
| [优化与工程设计](./optimization_engineering_design.md) | 参数与控制器调优、工程/逆向设计、材料与分子设计 | 24 |
| [科学软件与工作流工程](./scientific_software_workflow_engineering.md) | 科学/工程代码生成、仓库与流水线工程、HDL 与形式化规约代码 | 66 |
| [研究复现与重复](./research_reproduction_replication.md) | 复现已发表的分析、结果与方法；匹配已报告的结论 | 10 |
| [端到端研究](./end_to_end_research.md) | 跨越多个主要阶段的多阶段研究生命周期，从提出问题到汇报 | 5 |

在整个语料中，共对适用的 work 卡片赋予了 335 条活动归属。

## 活动是多标签的

活动**并不**互斥。当某个 benchmark 确实评估了多项实质性活动时，一份工作可以出现在多个活动页上（例如既需要模拟、又需要科学软件的论文复现任务）。标签的赋予是保守的：仅当某活动是**有意义的受评组成部分**——即移除它会实质改变该 benchmark 所衡量的能力——时才列出。顺带的工具使用不算数，典型卡片带有一到三个活动。

## 并非每份工作都有活动

有些工作并不评估科学或研究活动，因而不出现在任何活动页上：综述与立场论文、在任意轨迹上运作的纯评估方法学与诊断/奖励框架、通用型 Web/UI/computer-use 与编码助手 benchmark，以及安全性/鲁棒性/资源感知类探针。这些卡片的 `## Activities` 块写作 `N/A — <原因>`，且从不被强行归入某个活动。

## 活动页模板

每个活动页遵循统一结构：

```markdown
# <活动名称>

> [English](../../activities/<file>.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition      — 一段简洁的活动定义
## Scope           — 归属范围与关键边界情形
## Task Patterns   — 该活动在语料中如何呈现的综述，并链接 work 卡片
## Comparison      — 表格：Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card
## Related Works   — 反向索引：指向每个成员 work 卡片的裸链接
```

## 维护规则

- **反向索引是双向的。** 卡片 `## Activities` 块中的每个活动都必须出现在该活动页的 `Related Works`（及 Comparison 表）中，反之亦然。两侧必须完全一致——不得有仅出现在表中的条目、重复项或失效链接。
- **数量自动生成。** 上表中的 work 数量（以及仓库中所有计数）均由 [`../scripts/update_counts.py`](../scripts/update_counts.py) 从反向索引生成——任何卡片改动后运行该脚本，切勿手工修改计数。
- **仅用规范化标签。** 卡片只能取自上表分类；不得自造活动标签。
- **证据标准。** 分类依据卡片所描述的实际任务（`Overview`、`Tasks`、`Summary`、`Main Contribution`、`Domains`、`Key Design Ideas`），必要时回溯到经核验的原始来源——绝不依据标题关键词。
- **不强行归类、不设 `Other`。** 确实不适用的工作给出明确的 `N/A` 原因；不存在兜底活动。
- **职责划分。** Topic 负责评估方法学综述与开放问题；Domain 描述领域内的任务落地与科学验证；Activity 描述任务与工作流模式；卡片仍为个体工作的事实性参考。详细的评分方法学留在卡片、Topic 与 Domain 中。
- **双语镜像。** 每个活动页与每张卡片的 `## Activities` 块都在 [`../zh/activities/`](../zh/activities/README.md) 与 `../zh/works/` 下镜像，随每次英文改动同步。
- **分类变更**需同步更新 [`../AGENT.md`](../AGENT.md) 与 [`../CLAUDE.md`](../CLAUDE.md)。
