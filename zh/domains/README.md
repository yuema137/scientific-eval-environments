# Domains

> [English](../../domains/README.md) | **简体中文**

每个规范化科学或工程领域一页参考页——仓库的**领域轴**，与 [`topics/`](../topics/) 的方法学轴、[`activities/`](../activities/) 的研究活动轴地位对等：topic 按评估*方法学*分组，domain 按*领域*分组，activity 按 *agent 所执行的任务*分组。完整规则见 [`AGENT.md`](../../AGENT.md)。

## Domain 页模板

- **Scope**——一到两句话：范围是什么，包括折并规则。
- **Comparison**——一张事实性表格，**列固定且在所有 domain 页一致**：
  `Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card`。
  *科学问题* 陈述该工作实际处理的科学问题；*任务形式与规模* 陈述 agent 具体做什么、本领域内有多少任务；*领域内验证* 陈述科学正确性如何被检查（对照参考解的数值误差、专家标签、执行、物理判据、LLM judge 等）。
- **Related Works**——指向 work 卡片的纯链接（映射列表）。

Domain 页是**事实性参考页，不是文献综述**——作为入口与 topic 页地位对等，但性质不同：表格描述本领域内的每份工作，而方法学综合、topic 专属比较维度与开放问题都留在 topic 页。

## 规则

- **语言切换器与返回链接。** 每个页面在标题正下方有一行导航，包含语言切换器和一个返回本索引页的链接：英文页为 `> **English** | [简体中文](../zh/domains/<file>.md) · [← All domains](./README.md)`，中文镜像为 `> [English](../../domains/<file>.md) | **简体中文** · [← 全部 domains](./README.md)`。
- 更细的领域**折并**入规范化 domain（bioinformatics → Biology、GIS → Earth Science、psychology → Neuroscience & Cognitive Science、软件形式化验证 → Software & Systems Engineering 等）。
- 一个 work 可以属于**多个 domain**；多领域套件出现在其覆盖的每个 domain 中，表格行侧重本领域的切片。
- **没有兜底类别。** 没有科学或工程领域的 work——web/UI agent、computer use、通用 tool use、评估方法学、综述——不出现在这里。UI 与 computer-use 环境不是科学或工程领域。
- 映射是**单向的，仅在 domain 页维护**。卡片不因这条轴而修改；卡片的 `## Domains` 段落是归属依据，且每个表格单元都必须可从卡片验证。
- 归属必须可从卡片（以论文为依据）**验证**。未具名的类别不强行归属。

## 规范化 domain 分类

| 分组 | Domain | Works |
|---|---|---|
| Science | [Physics](./physics.md) | 36 |
| Science | [Astronomy](./astronomy.md) | 6 |
| Science | [Mathematics](./mathematics.md) | 14 |
| Science | [Chemistry](./chemistry.md) | 31 |
| Science | [Biology](./biology.md) | 29 |
| Science | [Neuroscience & Cognitive Science](./neuroscience_cognitive_science.md) | 12 |
| Science | [Medicine & Health](./medicine_health.md) | 15 |
| Science | [Earth Science](./earth_science.md) | 7 |
| Science | [Environmental Science](./environmental_science.md) | 2 |
| Science | [Materials Science](./materials_science.md) | 24 |
| Science | [Computer Science](./computer_science.md) | 5 |
| Science | [AI & Machine Learning Research](./ai_ml_research.md) | 21 |
| Engineering | [Mechanical & Aerospace Engineering](./mechanical_aerospace_engineering.md) | 9 |
| Engineering | [Electrical Engineering](./electrical_engineering.md) | 16 |
| Engineering | [Energy Systems](./energy_systems.md) | 4 |
| Engineering | [Chemical Engineering](./chemical_engineering.md) | 1 |
| Engineering | [Civil & Structural Engineering](./civil_structural_engineering.md) | 2 |
| Engineering | [Robotics](./robotics.md) | 16 |
| Engineering | [Software & Systems Engineering](./software_systems_engineering.md) | 16 |
