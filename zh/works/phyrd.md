# PHYRD (2026)

> [English](../../works/phyrd.md) | **简体中文**

> **首次公开：** 2026-10-23 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.32575)

## Overview

PHYRD 考察两类理论物理推导。Reproduce 要求模型从给定前提出发，重新推出一个已发表的结果；Discover 改动源论文中的一个条件，要求推出改动之后的结论。每道题拆成若干公开小问，逐问判对错。最终公式写对了，但缺少题目要求的推导或适用条件，这一问照样不得分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **论文：** [PHYRD: A Living Benchmark for Reproducing and Extending Theoretical Physics Research](https://arxiv.org/abs/2610.32575)，2026 年预印本。
- **全文：** <https://arxiv.org/html/2610.32575v1>
- **Venue:** arXiv 预印本（cs.CL，2026）

## Summary

FormulaForest 流程把一篇源论文整理成关系图：节点是公式和前提，边记录推导关系及其成立条件。Reproduce 把一个已发表的目标结果和推出它所需的前提配成一题。Discover 改动图中的一个局部结构，比如算符、耦合、对称性或边界条件，并记下哪些前提保持不变。解题者因此要自己判断，源论文里哪些论证仍然成立。作者计划按时间戳从新论文中追加题目，并表示每次发布都会保留此前的题目版本和成绩版本。

## Tasks

共 106 道题：Reproduce 63 道，含 279 个公开小问；Discover 43 道，含 225 个。Reproduce 大多数题有四问（63 道中 39 道），Discover 大多数题有五问（43 道中 22 道）。Reproduce 的题目来自 16 篇源论文。举一个 Reproduce 的例子：解题者要从给定顶点出发推出软引力子定理，包括轨道项、自旋项和围道积分这一步。举一个 Discover 的例子：一族矩阵被改成两处根碰撞合并，解题者必须重新推出 Jordan 结构和投影算符的极限。解题者只拿到题面；参考解答、各小问评分标准，以及来源和验证材料作为单独的部分另行保存。

## Domains

理论物理，沿用 PRL-Bench 的五个子领域：天体物理与引力、凝聚态、高能物理、量子物理与量子信息、统计物理。覆盖并不均衡：高能物理占 Reproduce 63 道中的 39 道、Discover 43 道中的 20 道。题目都是解析推导，不涉及数据分析或实验。

## Evaluation

- 一个小问要拿 1 分，题目要求的结论、必要推导和适用条件必须全部正确。小问内部不给部分分。数学上等价的表达式和其他有效推导都算对；必需的论证里留有未解决的矛盾，则记 0 分。
- 小问准确率（SAcc）先算每道题答对小问的比例，再对题目取平均。整题准确率（WAcc）只在一道题所有小问都对时才计入。两者都以全部题目为分母，没有作答也算错。
- 共测试五个模型：GPT-5.6 Sol、DeepSeek v4 Pro、GLM-5.2、Kimi K2.6 和 Qwen3.7-Max。Reproduce 只做闭卷。Discover 在同样 43 道题上做两种设置：闭卷，以及开放工具。工具包括隔离的 Python 环境（SymPy、NumPy、mpmath）、公开 arXiv 搜索和论文阅读。
- Reproduce 的 WAcc 在 49.21% 到 68.25% 之间，SAcc 在 79.66% 到 88.33% 之间。133 份未完全答对的 Reproduce 回答中，有 78 份只错了一个小问。
- 闭卷 Discover 的 WAcc 在 18.60% 到 74.42% 之间。用上工具后，四个模型完整解出的题变多；DeepSeek 和 Qwen 的 WAcc 各提高 20.93 个百分点，GLM 的完整解则从 14 道降到 13 道。
- 每个答错的小问只标一个主要错误类型：概念、推导、计算或不完整。在 209 对 Discover 配对回答中，用上工具后计算错误从 123 个降到 67 个，概念错误则从 70 个变成 75 个。
- Repository note：论文写明了评分规则，但没有说明模型回答由人工评分者、模型 judge 还是符号检查来按这些规则打分。

## Typical Duration

开放工具的 Discover 每题最多 24 轮 assistant 回复、128 次工具调用、两小时；每次 Python 执行限 40 秒 CPU 时间。闭卷 Discover 的 API 请求初始补全上限为 65,536 token。论文没有报告闭卷运行的实际耗时。

## Main Contribution

把推出已发表结果和推出改动前提后的结论分成两类任务，并按包含适用条件在内的逐问要求给两者评分。

## Key Design Ideas

- 关系图把论文明确写出的结果和推断出的依赖关系分开记录，并给每条关系附上成立条件。
- Discover 题面写明改了什么、什么不变，沿用源论文的论证必须先说明理由。
- 发布前，由一位只看题面的盲解者作答，再把答案和参考解答、评分标准放在一起联合审查。每个题面和完整任务包都用哈希值标记版本。

## Strengths

- 同时报告 SAcc、WAcc 和逐份回答的结果分布，能看出许多不完整的回答只差一个小问。
- Discover 在同样 43 道题上比较两种设置，给出配对 bootstrap 区间以及逐题的得失。
- 配对错误计数把用工具后减少的计算错误和没有减少的概念错误分开。

## Limitations

- 子领域覆盖不均衡；Quantum 和 Stat 在 Reproduce 中各只有三道题，一道题就能让准确率变动 33.3 个百分点。
- 作者指出，模型可能在训练中见过相关的已发表结果。
- 两种 Discover 设置在交互方式和 token 上限上也不同，GPT 还是通过对话界面收集的回答。论文明确表示，这种比较不能单独归因于工具使用。部分被截断的回答通过额外调用补全。
- 合成数据的结果来自另一项匿名、仍在审稿中的研究。该研究使用 Reproduce 流程生成的 17,577 条 SciDeriv 提示，在另一套分级评分的 PHYRD-40 和 FrontierScience 的 Olympiad-100 上评测。Olympiad-100 从 61% 到 72% 的提升包含一个监督微调阶段，仅这一阶段就已达到 68%。
- Repository note：arXiv v1 没有给出数据集或代码的发布链接。

## Related Works

- [PRL-Bench](./prl-bench.md) — 提供五个子领域的划分；从近期物理论文中构造研究任务。
- [TPBench](./tpbench.md) — 评测直至研究级的理论物理问题。
- [DiscoverPhysics](./discoverphysics.md) — 同样改动物理前提，但通过模拟实验来考察。
