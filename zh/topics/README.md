# Topics

文献综述页面，每页对应一个规范化（canonical）的评估方向。

Topic 页是本仓库的**首要入口**。对某一研究方向感兴趣的读者应从这里开始，沿链接进入 [`../works/`](../works/)，再到原始论文：

```
Topic  →  代表性 works  →  原始论文
```

## 规范化 topic 分类

Topic 集合是固定的。新增 topic 需要更新 [`../../AGENT.md`](../../AGENT.md)。

| # | Topic | 文件 |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | `long_horizon_evaluation.md` |
| II | Scientific Agent Benchmarks | `scientific_agents.md` |
| III | Trajectory Evaluation | `trajectory_evaluation.md` |
| IV | Skill Hierarchy | `skill_hierarchy.md` |
| V | Credit Assignment | `credit_assignment.md` |
| VI | Resource-aware Evaluation | `resource_aware_evaluation.md` |
| VII | Survey | `survey.md` |

Skill Hierarchy 与 Credit Assignment 是两个独立的 topic。

**Topic 之间并不互斥。** 一个 work 可以自然地属于多个 topic，因为每个 topic 代表的是一种文献视角，而不是一个互斥的类别。跨 topic 归属是设计上的预期，而非例外。

## 命名规范

- **评估方向类 topic** 使用 `_evaluation.md` 后缀：`trajectory_evaluation.md`、`resource_aware_evaluation.md`、`long_horizon_evaluation.md`。
- **更广义的 topic** 使用自然名称：`scientific_agents.md`、`skill_hierarchy.md`、`credit_assignment.md`、`survey.md`。

## Topic 页模板

```markdown
# <Topic Name>

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

- **没有全局比较矩阵。** 每个 topic 拥有各自的维度。不要用共享表格把 topic 页串联起来。
- **综合，而非摘要。** Topic 页应阐明该 topic 的设计空间，而不是复述单张卡片。需要某份工作的细节时，链接到它的卡片。
- **Related Works 是反向索引。** 此处列出的每份工作，其卡片的 `Topics` 块中必须包含本 topic，反之亦然。保持两侧同步是一项维护责任。
- **保持客观。** 不与任何维护者自身的项目做比较。
- **引用经过验证。** 与卡片相同的两级标准——链接校验与内容校验，无法从一手来源验证的数字写 `TODO(reference)`。
