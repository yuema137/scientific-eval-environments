# From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models (2026)

> [English](../../works/from-reasoning-to-agentic.md) | **简体中文**

> **首次公开：** 2026-04-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.09459)

## Overview

一篇综述，梳理了大语言模型强化学习中的信用分配（credit assignment, CA）方法，横跨推理 RL 与 agentic RL，并给出一个诊断框架，把假设失效映射到辨识障碍、估计量与评估控制。

## Topics


- [Survey](../topics/survey.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities


N/A — 关于 LLM 强化学习中信用分配方法的综述；不含可执行任务，也不评估任何科学/研究活动。

## Links

- **Paper:** https://arxiv.org/abs/2604.09459
- **Venue:** arXiv 预印本（cs.CL）；2026 年 4 月 10 日提交，2026 年 8 月 9 日最后修订

## Summary

本文讨论 LLM 强化学习中的信用分配问题：稀疏的结果奖励几乎无法说明是哪个 token、哪一步推理、哪次工具调用、哪次记忆操作或哪个 agent 导致了某个结果。文章认为该问题在 agentic RL 中更为尖锐，因为与环境的交互引入了转移非闭合、部分可观测、回放受限、动作异质、中间可验证性弱以及 agent 耦合等复杂因素。它综合了 2024 年 1 月至 2026 年 7 月 31 日发表的 69 篇论文（56 篇核心 CA 方法与 13 篇邻接或边界使能工作，从 92 条去重筛选记录中选出），保留了「按粒度 × 按方法论」的分类法，并新增一个六诊断框架，以及一张可复用的「CA-ID Card」用于溯源与证伪。

## Tasks

N/A — 综述论文。它并不定义可执行的 benchmark 或任务套件，而是对一份文献语料进行整理与审计。一项定位到原文的全文审计覆盖固定的 42 篇核心论文子集。

## Domains

大语言模型的强化学习与评估方法学（推理 RL 与 agentic RL）。不绑定到任何具体的科学或工程应用领域。

## Evaluation

N/A — 综述论文。文章不做任务打分，转而报告编码可靠性证据：两位算法研究者独立且盲态地交叉编码了 252 个诊断单元，其中 223 个（88.5%）达成一致；逐诊断的 Cohen's kappa 在 .543 到 .909 之间，主族一致性为 42/42（kappa = 1.000）。

## Typical Duration

N/A — 综述论文。

## Main Contribution

对推理 RL 与 agentic RL 中信用分配方法的统一综合，具体而言（据作者）：保留原有的「按粒度 × 按方法论」分类法，同时新增一个把假设失效映射到辨识障碍、估计量与评估控制的六诊断框架；明确了「恢复状态比较」在何时能辨识出某种协议特定的因果对比；表明仅含文本的历史可能连信用的符号都无法辨识；并引入一张可复用的 CA-ID Card，把每条主张链接到其估计目标、证据溯源与证伪测试，并配一套原子级报告审计。

## Key Design Ideas

- 由 69 篇论文（56 篇核心 CA 方法、13 篇邻接/边界使能工作）构成的语料，取自 92 条去重筛选记录，覆盖 2024 年 1 月 – 2026 年 7 月 31 日。
- 沿用先前组织方式的「按粒度 × 按方法论」分类法，并扩展出一个把假设失效关联到辨识障碍、估计量与评估控制的六诊断框架。
- 枚举了信用分配在 agentic RL 中的复杂因素：转移非闭合、部分可观测、回放受限、动作异质、中间可验证性弱与 agent 耦合。
- 对固定的 42 篇核心论文子集做定位到原文的全文审计，并对 252 个诊断单元进行盲态双人交叉编码以检验可靠性。
- 「CA-ID Card」模板，把每条主张链接到其估计目标、证据溯源与证伪测试。
- 配套仓库托管一个持续更新的目录与决策辅助（URL 未在 arXiv 摘要页给出）。

## Strengths

- 显式报告评分者间可靠性（252 个单元上 88.5% 一致；逐诊断 kappa .543–.909；主族 kappa = 1.000）。
- 用统一的诊断词汇把推理 RL 与 agentic RL 的信用分配桥接起来。
- 提供可复用的评估产物（六诊断框架、CA-ID Card、原子级报告审计），而不只是叙述式分类法。

## Limitations

- Repository note: 作为综述，它贡献的是组织与诊断，而非可执行的 benchmark 或可复现的打分协议。
- Repository note: 配套的持续更新目录 / 审计包 URL 在摘要中被引用，但未在 arXiv 摘要页给出，因此此处无法核验。
- Repository note: 全文审计仅限于固定的 42 篇核心论文子集，而非整个 69 篇语料。

## Related Works

TODO(reference)
