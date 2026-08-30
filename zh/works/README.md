# Works

> [English](../../works/README.md) | **简体中文**

每篇论文或每个项目一张卡。读者不用先去啃 abstract，也能看懂这份工作改了什么。

**"Works"** 比 "benchmarks" 更广。本目录为仓库记录的每一份工作保存一张卡片，包括：

- **Benchmarks** — 带评分协议的任务集。
- **方法学（Methodologies）** — 评估方法、指标与协议（LLM-jury、dense-reward 打分、scaffolded-capability 评估等）。
- **框架（Frameworks）** — 覆盖在现有 benchmark 之上的评估基础设施（诊断审计协议、trace 分析系统、ground-truth 生成工具包）。
- **面向评估的 agent RL 工作** — 以*评估* agent 为核心的强化学习贡献（agent 的 reward 设计、credit-assignment 方法、agent trajectory 的 off-policy 评估）。纯 RL 算法 / 训练 / 策略优化工作不在范围内；参见 [`../../AGENT.md`](../../AGENT.md)。
- **参考论文（Reference papers）** — 综述与立场论文，卡片上会显式标注类型。

每份工作在本目录下**只有一个** Markdown 文件，不再按类别分子目录。卡片先说原来的 evaluation 或 development path 怎样走，再说这份工作改了哪一步，让一个 task 走到 score，最后交代 source 能支撑到哪里。文件名使用 kebab-case，例如 `terminal-bench-science.md`、`medhelm.md` 和 `trace.md`。

## 卡片是什么（不是什么）

一张卡回答四个具体问题：**这份工作解决什么事？它改了哪一步？这个改动怎样被评估？现有证据还不能证明什么？**

卡片**不是**文献综述。综合、比较与设计空间分析属于 [`../topics/`](../topics/)。

卡片要简洁，但不能只堆名词。它负责解释一份工作，不负责判断整个领域里谁更好。跨工作比较放到 topic 页。

## 卡片模板

逐字复制以下结构。不要新增小节，也不要删除小节（如果某项工作不具备对应内容，留空或写 `N/A` 并附简短说明——例如综述卡片的 Tasks 与 Evaluation 写 `N/A — survey paper`）。

```markdown
# <Work Name> (<Year>)

> **English** | [简体中文](../zh/works/<card-file>.md)

> **首次公开：** YYYY-MM-DD · **来源：** [arXiv 首次提交](<source URL>)

## Overview

用一到两句话回答：原来的 path 怎样走，这份工作改了哪一步，它又怎样检查这个改动。遵循 [`../../EXPLANATION_STYLE.md`](../../EXPLANATION_STYLE.md)，不要粘贴 abstract 或换几个词再抄一遍。

## Topics

- [<Topic Name>](../topics/<topic_file>.md)
- [<Topic Name>](../topics/<topic_file>.md)

## Activities

- [<Activity Name>](../activities/<activity_file>.md)

## Links

- **Paper:** <已验证的 URL>
- **Project:** <已验证的 URL，或省略>
- **Code:** <已验证的 URL，或省略>
- **Venue:** <已验证的 venue，或省略>

## Summary

用两到四句话让核心机制走一遍：输入或 state 先到哪里，谁做了什么 intervention，结果怎样变成 score。如果 `Limitations` 还没有覆盖最重要的边界，就在这里交代。

## Tasks

任务数量、任务类型以及任务的构建方式。非 benchmark 工作（综述、
立场论文）写 `N/A` 并附说明。

## Domains

覆盖的科学或应用领域。

## Evaluation

答案或 trajectory 怎样被打分，比如确定性 verifier、专家 rubric、LLM judge 或基于执行的 check。读者应该能跟着一个代表性样例，从 output 一直走到 score。综述与立场论文写 `N/A` 并附说明。

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
- **首次公开时间戳。** 每张卡在语言切换器下方放一行 `首次公开`，中文镜像必须与英文卡使用相同的日期和来源链接。这里的“首次公开”只问一件事：这项工作最早在哪一天能被公众访问；它当时是预印本、公开投稿、项目或数据发布、软件发布，还是正式论文，都不影响判断。不要拿 venue 年份代替查询。应检查 arXiv、Hugging Face、OpenReview、出版社或 proceedings 官网、DOI 注册记录、官方项目或数据页，以及官方代码库中的首次提交或发布记录；有多个合格记录时取最早一个。后续版本、接收日期、会议日期、晚于公开版本的正式出版日期和页面修改日期，都不能覆盖更早的公开日期。Venue 和出版信息另写在 `Links` 中。只有确实查不到任何可核验的公开日期时，才使用 card 首次加入仓库的 Git 日期，并把来源明确标为 `首次加入本仓库`。来源链接必须保留，方便审核。[`../WORKS_BY_DATE.md`](../WORKS_BY_DATE.md) 按这个时间戳生成。
- **`Topics` 是元数据块，不是装饰。** 它是保持 topic 页同步的内部索引。此处列出的每个 topic，在对应 topic 页的 `Related Works` 中必须有相应条目，反之亦然。只能使用 [`../../AGENT.md`](../../AGENT.md) 定义的规范化 topic 分类。
- **`Activities` 是必填的规范化元数据。** 每张卡片都恰有一个 `## Activities` 块，紧跟在 `## Topics` 之后。它列出一个或多个取自固定分类（见 [`../../AGENT.md`](../../AGENT.md) / [`../activities/README.md`](../activities/README.md)）的规范化活动；对于不评估任何科学/研究任务的工作（综述、纯方法学、通用型或安全性/资源类 benchmark），则写一行明确的 `N/A — <原因>` 且不带链接。活动是**多标签**的，但赋予时保守（通常一到三个，仅当该活动是任务中有意义的受评组成部分——依据卡片内容判断，绝不依据标题关键词）。映射是**双向**的：此处链接的每个活动都必须在对应活动页的 `Related Works` 中列出本工作，反之亦然。不得自造活动标签。
- **不做定位。** 不得包含 "Gap to Our Work"、"Comparison with Our Framework" 或任何将某份工作与维护者自身项目对照的小节。
- **提交前完成两级引用校验：**
  - *链接校验*：title、URL、project、venue、year——对照实际来源验证。
  - *内容校验*：统计数据、任务数、指标、报告数字——**只从原始论文或官方 project 验证**，绝不使用二手来源。无法校验的内容写为 `TODO(reference)`——不要猜测，也不要从摘要类内容推断。
- **模板稳定性。** 不要为迁就某一张卡片而修改模板结构。新的评估维度应加入 topic 页。
- **Repository Notes 保持克制。** 作者陈述的主张不加标注；仓库补充的任何内容以 `Repository note:` 开头。允许：维护性观察、跨论文的事实综合、论文所述内容的直接推论。不允许：推测性批评、主观意见、向论文未评估设定的外推。如果一条观察无法由所引文献清晰支持，它就不应出现在卡片中。
