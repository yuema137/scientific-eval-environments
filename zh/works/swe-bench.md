# SWE-bench (2023)

## Overview

SWE-bench 评估语言模型能否通过编辑代码库来解决真实的 GitHub issue。它包含来自 12 个流行 Python 仓库的 2,294 个 issue–pull request 任务实例，并通过执行仓库自身的测试来对模型的补丁打分。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.06770>
- **Code:** <https://github.com/SWE-bench/SWE-bench>
- **Venue:** ICLR 2024

## Summary

SWE-bench 把软件工程作为评估语言模型的测试床。每个任务提供一个代码库与一段自然语言的 issue 描述；模型需编辑代码库以解决该 issue。解决一个 issue 通常需要理解并协调跨多个函数、类乃至文件的改动，与执行环境交互，处理超长上下文，并进行超出传统代码生成的推理。2,294 个实例从真实 GitHub issue 及其对应的已合并 pull request 中挖掘，使任务来源天然可获取且可刷新。

## Tasks

2,294 个软件工程问题，来自 12 个流行 Python 仓库的真实 GitHub issue 及对应 pull request。每个任务给定代码库与 issue 描述；目标是解决该 issue 的补丁。

## Domains

软件工程——开源 Python 仓库。

## Evaluation

- 基于执行：将模型生成的补丁应用到仓库，运行仓库关联的测试套件以判断 issue 是否被解决。
- 报告：发表时表现最佳的模型 Claude 2 解决了 1.96% 的 issue。

## Typical Duration

在 agentic 设定下为多步——理解 issue、浏览代码库、跨多文件编辑。单任务 wall-clock / token 预算：TODO(reference)——摘要未说明。

## Main Contribution

将真实世界的软件工程（GitHub issue 解决）引入为一个丰富、可持续、基于执行验证的测试床，用于评估超出传统单函数代码生成的语言模型。

## Key Design Ideas

- 任务从真实 GitHub issue 与已合并 pull request 中挖掘——天然可获取、可刷新的任务来源。
- 通过各仓库自身的测试套件进行基于执行的打分，而非参考字符串匹配。
- 任务需要跨多文件、跨函数的协调与长上下文处理。
- **SWE-bench Verified**——与 OpenAI 合作创建的 500 实例人工筛选子集，人工标注者审阅每个实例，确保问题描述清晰、测试补丁正确、任务可解，从而对 coding agent 提供更可靠的评估。

## Strengths

- 真实、可持续的任务来源，抵抗饱和并可随新 issue 刷新。
- 客观的基于执行的打分。
- 极低的初始求解率（1.96%）为后续模型世代留出大量 headroom。

## Limitations

- Repository note: 范围为 Python 开源仓库；对其他语言与生态的泛化未被直接评估。
- Repository note: 原始测试集包含一些描述不足或不可解的实例，这促成了人工筛选的 SWE-bench Verified 子集。

## Related Works

- [Enconda-bench](./enconda-bench.md) — 同为软件工程 agent 评估，但对环境配置进行过程级打分，而非端到端 issue 解决。
- [AgentBench](./agentbench.md) — 同为通用 agent benchmark；多环境而非软件工程专用。
