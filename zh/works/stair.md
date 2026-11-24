# STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents (2026)

> [English](../../works/stair.md) | **简体中文**

> **首次公开：** 2026-07-31 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.29658)

## Overview

STAIR 把 coding agent 以前修复 issue 的 trajectory 转换成多层 plan tree，在 agent 修复新 issue 时挑选其中的节点注入 prompt。仓库级修复 agent 通常每个 issue 都从头处理；已有的经验复用方法传下去的，要么是原始 trajectory，要么是只有一层的摘要。STAIR 改的是存什么、取什么：每次过去的修复都变成一棵树，从具体的诊断步骤一直往上抽象到与项目无关的策略和通用原则，检索时跨层挑选节点。论文在 SWE-bench Verified 上用 Pass@1 检验这个改动；ablation 则在同一批实例上比较原始 trajectory、各个单独的抽象层级和混合层级。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 这是经验复用方法，评测对象是通用的软件 bug 修复（SWE-bench Verified），没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.29658>
- **Venue:** arXiv preprint, July 2026

## Summary

对一个目标 issue，STAIR 从同一仓库中检索在它之前创建、并且已经解决的 issue（按 embedding 相似度排序，再由 LLM 相关性 verifier 过滤），然后关掉 Lingxi 修复 scaffold 自带的知识复用，在这些 issue 上运行它。每条 trajectory 被切成定位、规划、执行与验证三个阶段；随后 GPT-5 反复把节点分组，并把每组抽象成一个父节点，直到最多剩下两个根节点。这样得到三层视图：低层（针对具体代码文件或函数的 sub-goal）、中层（与项目无关的排查策略）和高层（跨项目的原则）。每个节点都记录修复意图、关键 action、适用条件和常见陷阱。修复时，先按文本相似度给节点打分，再由 LLM verifier 过滤，按原始执行顺序排好，最后由 LLM 改写成分阶段的 plan，放进修复 agent 的 prompt。

## Tasks

N/A — 方法论文，没有提出新的任务集。实验使用 SWE-bench Verified：来自 12 个 Python 仓库的 500 个实例。总共检索并抽象了 479 条相似的历史 trajectory。Ablation 使用一个 125 实例的子集（92 个中等或困难，33 个简单）。

## Domains

Software & Systems：Python 项目中的仓库级 bug 修复。

## Evaluation

一个实例的流程如下：issue 报告和 STAIR 生成的分阶段 plan 一起交给 base agent；agent 产出一个 patch；patch 由 benchmark 自带的测试判分，测试通过时，Pass@1 就把这个实例记为已解决。论文还报告了每个实例的平均步数和 token 数。

报告的结果：

- **主结果（Lingxi + STAIR）：** 使用 MiniMax M2.5（High Reasoning）时 Pass@1 为 81.2%，使用 GPT-5（High Reasoning）时为 79.2%；同样的 backbone 下单独的 Lingxi 分别为 74.6% 和 75.6%。
- **迁移到 mini-SWE-agent v2（MiniMax M2.5），不改代码：** 不用 plan 时 379/500（75.8%），用 plan 时 405/500（81.0%）；平均步数 60.45 → 58.18；每个实例的 token 数 1,244,923 → 1,179,885。
- **增益与退化分析：** Lingxi + STAIR 相比 Lingxi（MiniMax），新解决 43 个实例、退化 10 个（净 +33）；mini-SWE-agent v2 用 plan 后新解决 33 个、退化 7 个（净 +26）。对这些变化的人工标注 Cohen's kappa 为 0.85。17 个退化中，8 个与 plan 有关（覆盖不全），9 个是执行错误。
- **抽象层级 ablation（125 个实例，MiniMax M2.5）：** 完整层级 100/125（80.0%）；原始 trajectory 72/125（57.6%）；只用低层 80/125（64.0%）；只用中层 76/125（60.8%）；只用高层 73/125（58.4%）。

## Typical Duration

每个实例 10–15 分钟。每个实例的花费为 $0.84（MiniMax M2.5）和 $1.60（GPT-5）；预处理每条源 trajectory 约 $0.44，合计约 $211。

## Main Contribution

把过去的修复 trajectory 分层抽象成可复用的 plan，并给出证据：混合多个抽象层级比任何单一层级或原始 trajectory 解决的 issue 更多，而且这些 plan 能迁移到结构不同的 agent 上。

## Key Design Ideas

- 抽象之前，先按修复阶段（定位、规划、执行与验证）切分每条 trajectory。
- 用 LLM 的分组操作和抽象操作自底向上构建层级，反复执行直到最多剩两个根节点。
- 所有层级共用一套节点格式：修复意图、关键 action、适用条件、常见陷阱。
- 跨层级挑选节点，而不是只用某一种粒度，然后把它们改写成针对当前 issue 的 plan。
- 历史 issue 只取在目标 issue 之前创建的，避免时间上的信息泄漏。
- Plan 只通过 prompt 注入，所以换一个 agent 也能直接使用，无需改代码。

## Strengths

- Ablation 用同一条 pipeline，直接比较了每个抽象层级以及完全不抽象的情况（论文）。
- 迁移到 mini-SWE-agent v2 的实验，检验了 plan 是否依赖于产生它们的那个 agent（论文）。
- 除了净 Pass@1，还报告了新解决和退化的实例，并人工标注了原因（论文）。
- 报告了运行费用和预处理成本（论文）。

## Limitations

- 作者指出，抽象质量取决于 LLM 的生成和输入长度；LLM 做的 plan 兼容性过滤可能丢掉有用的 plan，也可能留下不适用的 plan。
- 只测试了 SWE-bench Verified（Python）和两个 LLM；plan 的质量可能取决于产生 trajectory 的 base agent（论文）。
- Pass@1 依赖自带测试，行为上不正确的 patch 也可能通过（论文）。
- 论文没有展开 STAIR 这个缩写，也没有给出代码或复现链接。
- Repository note: ablation 在 125 实例的子集上进行，没有报告各变体的成本。

## Related Works

- [SWE-bench](./swe-bench.md) — 评测所用 SWE-bench Verified 实例的来源。
- [Trace2Tower](./trace2tower.md) — 同样把过去的 trajectory 抽象成多层 skill 并比较各层级，场景是家居和网购环境。
- [Agent Workflow Memory](./agent-workflow-memory.md) — 从 web agent 过去的 trajectory 中归纳可复用的子流程，主要只在一种粒度上。
