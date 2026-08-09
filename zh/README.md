# 科学评估环境（Scientific Evaluation Environments）

> [English](../README.md) | **简体中文**

一个开放的知识库，用于记录**面向 AI agent 的科学评估环境**的设计空间——涵盖 benchmark、评估方法学、评估框架、trajectory evaluation、resource-aware evaluation 以及科学工作流。

本仓库**不是** benchmark 实现。它是一份参考手册，目标是无论读者使用什么工具或 benchmark，都能在其中获得有价值的参考。

---

## 仓库结构

```
scientific-eval-environments/
├── README.md              # 英文首页
├── AGENT.md               # 仓库章程（规范），贡献前必读
├── CLAUDE.md              # 章程速查
├── works/                 # 每个 work 一张 Markdown 卡片（事实性引用）
│   ├── README.md          # 卡片模板与规则
│   └── ...                # 238 张卡片，扁平目录，kebab-case——每份 work 一个文件
├── topics/                # 面向单一评估方向的文献综述页面
│   ├── README.md          # Topic 页模板与规则
│   └── ...                # 7 个规范化 topic 页
├── domains/               # 领域轴参考页，每个规范化 domain 一页
│   ├── README.md          # Domain 页模板与规则
│   └── ...                # 19 个 domain 页，snake_case——每个领域一个文件
└── zh/                    # 中文镜像（每完成一批英文后同步）
    ├── README.md
    ├── works/
    ├── topics/
    └── domains/
```

仓库有**三层知识组织**——works，以及其上两条平级的聚合轴：

- **`works/`**：扁平目录，每份 work 一份 Markdown。卡片是事实性引用。"Works" 比 "benchmarks" 更广——该层收录 benchmark、评估方法学、评估框架（诊断覆盖层、trace 分析系统、ground-truth 生成工具包）、面向评估的 RL 工作、综述与立场论文。每张卡片会显式标注类型。
- **`topics/`**：文献综述页面，每个页面对应一个规范化（canonical）的评估方向。每个 topic 拥有各自的比较表和各自的比较维度。**不存在全局比较矩阵。**
- **`domains/`**：参考页，按 work **所评估的科学或工程领域**聚合。这是**领域轴**，与 topic 正交且地位对等：topic 按评估*方法学*分组，domain 按*领域*分组。每个 domain 页含范围说明、一张列固定的比较表（科学问题、任务形式与规模、领域内验证——所有 domain 页列一致）与带链接的 work 列表；方法学综合留在 topic 页。没有科学或工程领域的 work（web/UI agent、computer use、评估方法学、综述）不出现在 domain 层。

**Topic 之间并不互斥。** 一个 work 可以自然地属于多个 topic，因为每个 topic 代表的是一种文献视角，而不是一个互斥的类别。跨 topic 的归属是设计上的预期，而非例外。你可以双向浏览：每张卡片的 `Topics` 块向上链接到所属 topic，每个 topic 页的 `Related Works` 向下链接到卡片。

---

## 规范化 topic 分类

Topic 组织围绕以下固定集合：

| # | Topic | 文件 |
|---|---|---|
| I | [General Long-Horizon Agent Benchmarks](./topics/long_horizon_evaluation.md) | `long_horizon_evaluation.md` |
| II | [Scientific Agent Benchmarks](./topics/scientific_agents.md) | `scientific_agents.md` |
| III | [Trajectory Evaluation](./topics/trajectory_evaluation.md) | `trajectory_evaluation.md` |
| IV | [Skill Hierarchy](./topics/skill_hierarchy.md) | `skill_hierarchy.md` |
| V | [Credit Assignment](./topics/credit_assignment.md) | `credit_assignment.md` |
| VI | [Resource-aware Evaluation](./topics/resource_aware_evaluation.md) | `resource_aware_evaluation.md` |
| VII | [Survey](./topics/survey.md) | `survey.md` |

Skill Hierarchy 与 Credit Assignment 是两个独立的 topic。

---

## 规范化 domain 分类

Domain 围绕以下固定的 19 个科学与工程领域组织：

| 分组 | Domain | 文件 |
|---|---|---|
| 科学 | [Physics](./domains/physics.md) | `physics.md` |
| 科学 | [Astronomy](./domains/astronomy.md) | `astronomy.md` |
| 科学 | [Mathematics](./domains/mathematics.md) | `mathematics.md` |
| 科学 | [Chemistry](./domains/chemistry.md) | `chemistry.md` |
| 科学 | [Biology](./domains/biology.md) | `biology.md` |
| 科学 | [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | `neuroscience_cognitive_science.md` |
| 科学 | [Medicine & Health](./domains/medicine_health.md) | `medicine_health.md` |
| 科学 | [Earth Science](./domains/earth_science.md) | `earth_science.md` |
| 科学 | [Environmental Science](./domains/environmental_science.md) | `environmental_science.md` |
| 科学 | [Materials Science](./domains/materials_science.md) | `materials_science.md` |
| 科学 | [Computer Science](./domains/computer_science.md) | `computer_science.md` |
| 科学 | [AI & Machine Learning Research](./domains/ai_ml_research.md) | `ai_ml_research.md` |
| 工程 | [Mechanical & Aerospace Engineering](./domains/mechanical_aerospace_engineering.md) | `mechanical_aerospace_engineering.md` |
| 工程 | [Electrical Engineering](./domains/electrical_engineering.md) | `electrical_engineering.md` |
| 工程 | [Energy Systems](./domains/energy_systems.md) | `energy_systems.md` |
| 工程 | [Chemical Engineering](./domains/chemical_engineering.md) | `chemical_engineering.md` |
| 工程 | [Civil & Structural Engineering](./domains/civil_structural_engineering.md) | `civil_structural_engineering.md` |
| 工程 | [Robotics](./domains/robotics.md) | `robotics.md` |
| 工程 | [Software & Systems Engineering](./domains/software_systems_engineering.md) | `software_systems_engineering.md` |

更细的领域折并入规范化 domain（bioinformatics → Biology、GIS → Earth Science、psychology → Neuroscience & Cognitive Science 等），一个 work 可以出现在多个 domain 中。UI 与 computer-use 环境不是科学或工程领域。各 domain 的 work 数量与完整规则见 [`domains/README.md`](./domains/README.md) 与 [`AGENT.md`](../AGENT.md)。

---

## 如何阅读本仓库

仓库有两个平级入口，各对应一条轴。若带着方法学问题而来，从 topic 页进入；若带着某个领域而来，从 domain 页进入：

```
Topic   →  代表性 works       →  原始论文
Domain  →  该领域中的评估工作  →  原始论文
```

- 想理解**如何对 trajectory 打分**？阅读 [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md)。
- 想理解**资源消耗如何进入评估**？阅读 [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md)。
- 想知道**物理或流体力学领域有哪些工作**？阅读 [`domains/physics.md`](./domains/physics.md) 或 [`domains/mechanical_aerospace_engineering.md`](./domains/mechanical_aerospace_engineering.md)。
- 想要某个具体 work 的事实性信息？直接看 [`works/`](./works/) 中对应的卡片。

---

## 语言

每个页面都有英文与中文两个版本。使用任意页面顶部的语言切换器（English | **简体中文**）即可切换；英文为标准版本，位于仓库根目录。

---

## 贡献须知

欢迎贡献。所有面向贡献者与维护者的规则——引用校验、页面模板、分类法与双语同步节奏——都在英文原版 [`AGENT.md`](../AGENT.md)（章程）与 [`CLAUDE.md`](../CLAUDE.md)（章程速查）中，各目录的 README 给出层内规则。

---

## 范围

**在范围内：** 科学评估环境、benchmark 全景、评估方法学、评估框架、科学工作流、trajectory evaluation、resource-aware evaluation、benchmark 设计，以及**面向评估的 agent RL 工作**（reward 设计、credit-assignment 方法、agent trajectory 的 off-policy 评估等）。

**暂不在范围内：** 纯 RL 算法研究、策略优化与训练过程、agent 实现、多 agent 系统、记忆系统。

RL 工作的界线由论文主要贡献判定：如果它推进了**如何评估 agent**，即在范围内；如果它推进的是**如何训练 agent**，则不在范围内。

---

## 状态

7 个规范化 topic 页全部编写，卡片覆盖已远超初始参考列表：

- **238 张卡片** 位于 `works/`——包括 benchmark、评估框架与方法学、以及参考论文（综述与立场论文）。每张卡片显式标注类型；扁平目录本身即权威列表。
- **7 个 topic 页**——完整的文献综述，各自拥有专属比较表与开放问题。各 topic 当前的 Related-Works 覆盖：Scientific Agent Benchmarks（24）、Trajectory Evaluation（20）、General Long-Horizon Agent Benchmarks（17）、Credit Assignment（13）、Skill Hierarchy（7）、Resource-aware Evaluation（7）、Survey（4）。
- **19 个 domain 页**——领域轴的参考页，各含一张列固定的比较表（每份 work 的科学问题、任务形式与规模、领域内验证）；目前覆盖最多的是 Biology、Mathematics、Physics 与 Software & Systems Engineering。
- **中文镜像**位于 `zh/`，按双语节奏同步维护。
