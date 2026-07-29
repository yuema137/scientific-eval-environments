# 科学评估环境（Scientific Evaluation Environments）

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
│   └── ...                # 66 张卡片，扁平目录，kebab-case——每份 work 一个文件
├── topics/                # 面向单一评估方向的文献综述页面
│   ├── README.md          # Topic 页模板与规则
│   └── ...                # 7 个规范化 topic 页
└── zh/                    # 中文镜像（每完成一批英文后同步）
    ├── README.md
    ├── works/
    └── topics/
```

仓库仅有**两层知识组织**：

- **`works/`**：扁平目录，每份 work 一份 Markdown。卡片是事实性引用。"Works" 比 "benchmarks" 更广——该层收录 benchmark、评估方法学、评估框架（诊断覆盖层、trace 分析系统、ground-truth 生成工具包）、面向评估的 RL 工作、综述与立场论文。每张卡片会显式标注类型。
- **`topics/`**：文献综述页面，每个页面对应一个规范化（canonical）的评估方向。每个 topic 拥有各自的比较表和各自的比较维度。**不存在全局比较矩阵。**

**Topic 之间并不互斥。** 一个 work 可以自然地属于多个 topic，因为每个 topic 代表的是一种文献视角，而不是一个互斥的类别。跨 topic 的归属是设计上的预期，而非例外。这种归属关系被冗余地表达两次——一次在卡片的 `Topics` 元数据块中，一次在 topic 页的 `Related Works` 中——并作为一项维护纪律进行同步。

---

## 规范化 topic 分类

Topic 组织围绕以下固定集合：

| # | Topic | 文件 |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | [`long_horizon_evaluation.md`](./topics/long_horizon_evaluation.md) |
| II | Scientific Agent Benchmarks | [`scientific_agents.md`](./topics/scientific_agents.md) |
| III | Trajectory Evaluation | [`trajectory_evaluation.md`](./topics/trajectory_evaluation.md) |
| IV | Skill Hierarchy | [`skill_hierarchy.md`](./topics/skill_hierarchy.md) |
| V | Credit Assignment | [`credit_assignment.md`](./topics/credit_assignment.md) |
| VI | Resource-aware Evaluation | [`resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md) |
| VII | Survey | [`survey.md`](./topics/survey.md) |

Skill Hierarchy 与 Credit Assignment 是两个独立的 topic。

---

## 如何阅读本仓库

Topic 是首要入口。若读者对某一研究方向感兴趣，建议从 topic 页开始：

```
Topic  →  代表性 works  →  原始论文
```

- 想理解**如何对 trajectory 打分**？阅读 [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md)。
- 想理解**资源消耗如何进入评估**？阅读 [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md)。
- 想要某个具体 work 的事实性信息？直接看 [`works/`](./works/) 中对应的卡片。

---

## 命名规范

- **评估方向类 topic** 使用 `_evaluation.md` 后缀：`trajectory_evaluation.md`、`resource_aware_evaluation.md`、`long_horizon_evaluation.md`。
- **更广义的 topic** 使用自然名称：`scientific_agents.md`、`skill_hierarchy.md`、`credit_assignment.md`、`survey.md`。
- **Work 卡片** 使用 kebab-case，与 work 官方名称对应：`agentboard.md`、`t-eval.md`、`long-horizon-terminal-bench.md`。

---

## 贡献须知

贡献前请先阅读英文原版 [`AGENT.md`](../AGENT.md)。核心规则：

- 两级引用校验：*链接校验*（title、URL、project、venue、year）与*内容校验*（统计、任务数、评估指标、报告数字——**必须来自原始论文或官方 project**，绝不使用二手来源）。无法校验的数据一律写为 `TODO(reference)`。
- 保持客观——不使用 "our benchmark" / "our approach" / 任何定位性表述。
- Repository Notes 保持克制。任何论文未直接陈述的观察都需以 `Repository note:` 开头，且不允许出现推测性批评、主观意见、超出论文所评估设定的外推。
- 卡片模板保持稳定——新增评估维度写入 topic 页，而非卡片字段。
- 英文为标准版本，中文镜像位于 `zh/`，**每完成一批英文即同步**，不拖延。

---

## 范围

**在范围内：** 科学评估环境、benchmark 全景、评估方法学、评估框架、科学工作流、trajectory evaluation、resource-aware evaluation、benchmark 设计，以及**面向评估的 agent RL 工作**（reward 设计、credit-assignment 方法、agent trajectory 的 off-policy 评估等）。

**暂不在范围内：** 纯 RL 算法研究、策略优化与训练过程、agent 实现、多 agent 系统、记忆系统。

RL 工作的界线由论文主要贡献判定：如果它推进了**如何评估 agent**，即在范围内；如果它推进的是**如何训练 agent**，则不在范围内。

---

## 状态

7 个规范化 topic 页全部编写，卡片覆盖已远超初始参考列表：

- **66 张卡片** 位于 `works/`——包括 benchmark、评估框架与方法学、以及参考论文（综述与立场论文）。每张卡片显式标注类型；扁平目录本身即权威列表。
- **7 个 topic 页**——完整的文献综述，各自拥有专属比较表与开放问题。各 topic 当前的 Related-Works 覆盖：Scientific Agent Benchmarks（22）、Trajectory Evaluation（18）、Credit Assignment（13）、General Long-Horizon Agent Benchmarks（13）、Skill Hierarchy（6）、Resource-aware Evaluation（5）、Survey（4）。
- **中文镜像**位于 `zh/`，按双语节奏同步维护。
