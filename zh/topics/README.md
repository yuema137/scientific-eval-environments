# Topics

> [English](../../topics/README.md) | **简体中文**

文献综述页面，每页对应一个规范化的 evaluation-research 方向。

Topic 页是**evaluation research 轴**，与 domain 和 activity 平级。它回答三个问题：测什么、怎么测，以及怎样用 evaluation 改进 agent。

```
Topic  →  代表性 works  →  原始论文
```

## 规范化 topic 分类

Topic 集合是固定的。新增 topic 需要更新 [`../../AGENT.md`](../../AGENT.md)。

| # | Topic | 文件 | 收录 works |
|---|---|---|---|
| I | [General Long-Horizon Agent Benchmarks](./long_horizon_evaluation.md) | `long_horizon_evaluation.md` | 59 |
| II | [Scientific Agent Benchmarks](./scientific_agents.md) | `scientific_agents.md` | 246 |
| III | [Planning & Decision-Making Evaluation](./planning_decision_evaluation.md) | `planning_decision_evaluation.md` | 14 |
| IV | [Hierarchical Decision Abstraction](./hierarchical_decision_abstraction.md) | `hierarchical_decision_abstraction.md` | 7 |
| V | [Trajectory Evaluation](./trajectory_evaluation.md) | `trajectory_evaluation.md` | 57 |
| VI | [Skill Hierarchy](./skill_hierarchy.md) | `skill_hierarchy.md` | 43 |
| VII | [Credit Assignment](./credit_assignment.md) | `credit_assignment.md` | 25 |
| VIII | [Resource-aware Evaluation](./resource_aware_evaluation.md) | `resource_aware_evaluation.md` | 21 |
| IX | [Evaluator Reliability & Validation](./evaluator_reliability_validation.md) | `evaluator_reliability_validation.md` | 8 |
| X | [Benchmark Design, Validity & Contamination](./benchmark_design_validity_contamination.md) | `benchmark_design_validity_contamination.md` | 11 |
| XI | [Skill Learning & Evolution](./skill_learning_evolution.md) | `skill_learning_evolution.md` | 6 |
| XII | [Agent Harnesses & Scaffolding](./agent_harnesses_scaffolding.md) | `agent_harnesses_scaffolding.md` | 7 |
| XIII | [Evaluation-Driven Data Curation](./evaluation_driven_data_curation.md) | `evaluation_driven_data_curation.md` | 3 |
| XIV | [Evaluation-Driven Post-Training](./evaluation_driven_post_training.md) | `evaluation_driven_post_training.md` | 11 |
| XV | [Survey](./survey.md) | `survey.md` | 9 |

Skill Hierarchy 与 Credit Assignment 是两个独立的 topic。

**Topic 之间并不互斥。** 一个 work 可以自然地属于多个 topic，因为每个 topic 代表的是一种文献视角，而不是一个互斥的类别。跨 topic 归属是设计上的预期，而非例外。

## 命名规范

- **评估方向类 topic** 在名称自然时使用 `_evaluation.md` 后缀，例如 `trajectory_evaluation.md` 与 `resource_aware_evaluation.md`。
- **更广的研究主题** 使用自然名称，例如 `skill_learning_evolution.md`、`agent_harnesses_scaffolding.md` 与 `survey.md`。

## Topic 页模板

```markdown
# <Topic Name>

> **English** | [简体中文](../zh/topics/<topic_file>.md) · [← All topics](./README.md)

## Definition

对该 topic 的简明定义。一个段落。

## Motivation

该 topic 对科学评估为何重要。它解决什么问题？缺少它会缺失什么？

## Existing Approaches

代表性工作，可以按任何最能阐明该 topic 的方式分组或排序。引用
`../works/` 中的卡片，而不是复述其中的事实细节。

## Comparison

使用适配**本** topic 的维度构建比较表或矩阵——不要试图复用其他
topic 的维度。

## Open Questions

当前挑战与未来研究方向。明确标注为前瞻性内容，而非既定事实。

## Related Works

- [<Work Name>](../works/<work-card>.md) — 一句话说明收录原因。
```

## Topic 页规则

- **语言切换器与返回链接。** 每个页面在标题正下方有一行导航，包含语言切换器和一个返回本索引页的链接：英文页为 `> **English** | [简体中文](../zh/topics/<file>.md) · [← All topics](./README.md)`，中文镜像为 `> [English](../../topics/<file>.md) | **简体中文** · [← 全部 topics](./README.md)`。
- **没有全局比较矩阵。** 每个 topic 拥有各自的维度。不要用共享表格把 topic 页串联起来。
- **综合，而非摘要。** Topic 页应阐明该 topic 的设计空间，而不是复述单张卡片。需要某份工作的细节时，链接到它的卡片。
- **Related Works 是反向索引。** 此处列出的每份工作，其卡片的 `Topics` 块中必须包含本 topic，反之亦然。保持两侧同步是一项维护责任。
- **保持客观。** 不与任何维护者自身的项目做比较。
- **引用经过验证。** 与卡片相同的两级标准——链接校验与内容校验，无法从一手来源验证的数字写 `TODO(reference)`。
