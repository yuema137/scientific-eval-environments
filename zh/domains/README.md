# Domains

> [English](../../domains/README.md) | **简体中文**

按 work **所评估的科学或工程领域**聚合的索引页。这条轴与 [`topics/`](../topics/) 正交：topic 按评估*方法学*分组，domain 按*领域*分组。完整规则见 [`AGENT.md`](../../AGENT.md)。

## Domain 页模板

- **Scope**——一到两句话：范围是什么，包括折并规则。
- **Related Works**——指向 work 卡片的链接，各附一行提示。

Domain 页是**索引，不是文献综述**——没有比较表，没有综合分析。那些属于 topic 页。

## 规则

- 更细的领域**折并**入规范化 domain（bioinformatics → Biology、GIS → Earth Science、psychology → Neuroscience & Cognitive Science、软件形式化验证 → Software & Systems Engineering 等）。
- 一个 work 可以属于**多个 domain**；多领域套件出现在其覆盖的每个 domain 中。
- **没有兜底类别。** 没有科学或工程领域的 work——web/UI agent、computer use、通用 tool use、评估方法学、综述——不出现在这里。UI 与 computer-use 环境不是科学或工程领域。
- 映射是**单向的，仅在 domain 页维护**。卡片不因这条轴而修改；卡片的 `## Domains` 段落是归属依据。
- 归属必须可从卡片（以论文为依据）**验证**。未具名的类别不强行归属。

## 规范化 domain 分类

| 分组 | Domain | Works |
|---|---|---|
| Science | [Physics](./physics.md) | 8 |
| Science | [Astronomy](./astronomy.md) | 3 |
| Science | [Mathematics](./mathematics.md) | 9 |
| Science | [Chemistry](./chemistry.md) | 4 |
| Science | [Biology](./biology.md) | 10 |
| Science | [Neuroscience & Cognitive Science](./neuroscience_cognitive_science.md) | 3 |
| Science | [Medicine & Health](./medicine_health.md) | 4 |
| Science | [Earth Science](./earth_science.md) | 4 |
| Science | [Environmental Science](./environmental_science.md) | 2 |
| Science | [Materials Science](./materials_science.md) | 4 |
| Science | [Computer Science](./computer_science.md) | 2 |
| Science | [AI & Machine Learning Research](./ai_ml_research.md) | 4 |
| Engineering | [Mechanical & Aerospace Engineering](./mechanical_aerospace_engineering.md) | 2 |
| Engineering | [Electrical Engineering](./electrical_engineering.md) | 1 |
| Engineering | [Energy Systems](./energy_systems.md) | 1 |
| Engineering | [Chemical Engineering](./chemical_engineering.md) | 1 |
| Engineering | [Civil & Structural Engineering](./civil_structural_engineering.md) | 1 |
| Engineering | [Robotics](./robotics.md) | 0 |
| Engineering | [Software & Systems Engineering](./software_systems_engineering.md) | 7 |
