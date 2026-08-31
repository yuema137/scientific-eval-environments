# Benchmark Design, Validity & Contamination

> [English](../../topics/benchmark_design_validity_contamination.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Benchmark 可以给出一个很精确的数字，却仍然测错东西。Test set 可能已经进过训练数据；verifier 可能太弱，坏结果也能通过；toy environment 也可能根本没有论文声称要测的关键条件。问题不在算分，而在 task 到 score 这条路能不能支撑最后的结论。

拿一道 coding task 走一遍：从近期 repository 取题，生成 test，要求 test 覆盖改动过的 branch，执行 agent 提交的 patch，再记录 verifier 漏掉了什么。每一步都堵住一种失真来源，但没有哪一步能让 benchmark 永久有效。Repository 会变，model 会见到新数据，verifier 自己也得定期审计。

## 定义

这个 topic 检查的是「从 task 到结论」这条链。Task 从哪里来，model 有没有可能背过答案，参考答案是否容得下其他正确解，verifier 能不能拦住看着合理但其实是错的结果，environment 有没有保留真实任务的关键约束。这些问题的答案，决定了分数能不能支撑论文的结论。

## 为什么重要

计分算得再准，也救不了坏测量。任务被记住会高估能力，test 太弱会让错误结果通过，参考答案不全会拒绝合理解，toy environment 会把真实工作中最难的条件拿掉。所以 benchmark design 本身就是研究结果的一部分，需要实测，也需要持续维护。

## 现有方法

- **动态、近期来源。** [CODE2BENCH](../works/code2bench.md)、[PRL-Bench](../works/prl-bench.md) 和 [MedBrowseComp](../works/medbrowsecomp.md) 从近期 repository、论文或实时来源刷新题目。
- **私有或新写答案。** [CritPt](../works/critpt.md)、[OnePot-Bench](../works/onepot-bench.md) 和 [GeneBench-Pro](../works/genebench-pro.md) 使用未发表、私有或留出的材料。
- **程序生成与反事实构造。** [DiscoverPhysics](../works/discoverphysics.md) 按需生成物理世界，[Robotouille](../works/robotouille.md) 则程序化生成具身任务。
- **Verifier 严谨度。** CODE2BENCH 要求 property-based tests 达到 branch-coverage gate；[FrontierCode](../works/frontiercode.md) 同时做执行检查与 contamination 检测。
- **近期研究实现。** [ResearchCodeBench](../works/researchcodebench.md) 从近期研究贡献构造实现任务，并单独发布 contamination-safe 子集。

## 方法对比

| Work | 任务来源 | 有效性措施 | Verification | 刷新方式 |
|---|---|---|---|---|
| CODE2BENCH | 近期 Python 与 Java repository | 动态取材、依赖分类、测试质量 gate | Property-based tests，100% branch coverage | 可重复运行的构造 pipeline |
| PRL-Bench | 新发表的物理论文 | 持续移动的时间边界 | 参考结果约束的评估 | 随期刊更新 |
| CritPt | 未发表的专家问题 | 答案不进入训练语料 | 专家与参考答案检查 | 新的专家题批次 |
| DiscoverPhysics | 自动生成的物理世界 | 按需生成反事实规律 | Simulator ground truth | 每个实例更新 |
| ResearchCodeBench | 近期 ML 论文 | contamination-safe 论文子集 | 可执行代码测试 | 新论文批次 |

## 还没解决的问题

- Contamination audit 怎样从“没搜到重合”进一步支持“确实不存在”？
- 要声称功能正确，test adequacy 需要达到什么证据标准？
- Benchmark 更新时怎样保留跨时间比较能力？
- Synthetic control 在什么情况下会损失科学和工程场景所需的现实有效性？
- Reference、rubric 和 judge 的不确定性应如何进入最终分数？

## 相关工作

- [OnePot-Bench](../works/onepot-bench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [FrontierCode](../works/frontiercode.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [PRL-Bench](../works/prl-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [CritPt](../works/critpt.md)
- [CODE2BENCH](../works/code2bench.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [Robotouille](../works/robotouille.md)
