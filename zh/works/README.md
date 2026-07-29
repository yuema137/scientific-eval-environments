# Works

> [English](../../works/README.md) | **简体中文**

针对单个已有工作的事实性引用卡片。

**"Works"** 比 "benchmarks" 更广。本目录为仓库记录的每一份工作保存一张卡片，包括：

- **Benchmarks** — 带评分协议的任务集。
- **方法学（Methodologies）** — 评估方法、指标与协议（LLM-jury、dense-reward 打分、scaffolded-capability 评估等）。
- **框架（Frameworks）** — 覆盖在现有 benchmark 之上的评估基础设施（诊断审计协议、trace 分析系统、ground-truth 生成工具包）。
- **面向评估的 agent RL 工作** — 以*评估* agent 为核心的强化学习贡献（agent 的 reward 设计、credit-assignment 方法、agent trajectory 的 off-policy 评估）。纯 RL 算法 / 训练 / 策略优化工作不在范围内；参见 [`../../AGENT.md`](../../AGENT.md)。
- **参考论文（Reference papers）** — 综述与立场论文，卡片上会显式标注类型。

每份工作在本目录下**只有一个** Markdown 文件——没有按类别划分的子目录。文件名使用 kebab-case，与工作的官方名称对应（例如 `terminal-bench-science.md`、`medhelm.md`、`trace.md`）。

## 卡片是什么（不是什么）

卡片回答的问题是：**"这份工作是什么？"**

卡片**不是**文献综述。综合、比较与设计空间分析属于 [`../topics/`](../topics/)。

保持卡片轻量。如果一段比较或分析值得写下来，它应该写进 topic 页。

## 卡片模板

逐字复制以下结构。不要新增小节，也不要删除小节（如果某项工作不具备对应内容，留空或写 `N/A` 并附简短说明——例如综述卡片的 Tasks 与 Evaluation 写 `N/A — survey paper`）。

```markdown
# <Work Name> (<Year>)

> **English** | [简体中文](../zh/works/<card-file>.md)

## Overview

一到两句话描述这份工作是什么。

## Topics

- [<Topic Name>](../topics/<topic_file>.md)
- [<Topic Name>](../topics/<topic_file>.md)

## Links

- **Paper:** <已验证的 URL>
- **Project:** <已验证的 URL，或省略>
- **Code:** <已验证的 URL，或省略>
- **Venue:** <已验证的 venue，或省略>

## Summary

两到四句话描述这份工作的总体设计与目标。

## Tasks

任务数量、任务类型以及任务的构建方式。非 benchmark 工作（综述、
立场论文）写 `N/A` 并附说明。

## Domains

覆盖的科学或应用领域。

## Evaluation

答案/trajectory 如何被评分（确定性验证器、专家 rubric、LLM judge、
基于执行的检查等）。综述与立场论文写 `N/A` 并附说明。

## Typical Duration

每个任务的预期 trajectory 长度、墙钟时间或 token 预算。

## Main Contribution

这份工作自述的新颖性，采用作者自己的表述框架。

## Key Design Ideas

值得强调的具体设计选择，逐条列出。

## Strengths

逐条列出。尽可能引用论文或 project 来源。

## Limitations

逐条列出。尽可能引用论文或 project 来源。由本仓库（而非作者）
做出的观察必须标注 `Repository note:`。

## Related Works

- [<Other Work>](./<other-card>.md) — 一句话说明关联原因。
```

## 卡片规则

- **语言切换器。** 每个页面在 H1 正下方带一行切换器：英文页为 `> **English** | [简体中文](../zh/works/<card>.md)`，中文镜像为 `> [English](../../works/<card>.md) | **简体中文**`。新卡片须在同一批次内为两侧都加上切换器。
- **`Topics` 是元数据块，不是装饰。** 它是保持 topic 页同步的内部索引。此处列出的每个 topic，在对应 topic 页的 `Related Works` 中必须有相应条目，反之亦然。只能使用 [`../../AGENT.md`](../../AGENT.md) 定义的规范化 topic 分类。
- **不做定位。** 不得包含 "Gap to Our Work"、"Comparison with Our Framework" 或任何将某份工作与维护者自身项目对照的小节。
- **提交前完成两级引用校验：**
  - *链接校验*：title、URL、project、venue、year——对照实际来源验证。
  - *内容校验*：统计数据、任务数、指标、报告数字——**只从原始论文或官方 project 验证**，绝不使用二手来源。无法校验的内容写为 `TODO(reference)`——不要猜测，也不要从摘要类内容推断。
- **模板稳定性。** 不要为迁就某一张卡片而修改模板结构。新的评估维度应加入 topic 页。
- **Repository Notes 保持克制。** 作者陈述的主张不加标注；仓库补充的任何内容以 `Repository note:` 开头。允许：维护性观察、跨论文的事实综合、论文所述内容的直接推论。不允许：推测性批评、主观意见、向论文未评估设定的外推。如果一条观察无法由所引文献清晰支持，它就不应出现在卡片中。
