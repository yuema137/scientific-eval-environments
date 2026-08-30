# SWE-bench (2023)

> [English](../../works/swe-bench.md) | **简体中文**

> **首次公开：** 2023-10-10 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2310.06770)

## Overview

SWE-bench 评估语言模型能否通过编辑代码库来解决真实的 GitHub issue。它包含来自 12 个流行 Python 仓库的 2,294 个 issue–pull request 任务实例，并通过执行仓库自身的测试来对模型的补丁打分。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

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

- **每个任务两组测试。** 每个实例附带一个*测试补丁*，定义 **FAIL_TO_PASS** 测试（修复前失败、修复后必须通过，用于验证 issue 确实被解决）与 **PASS_TO_PASS** 测试（改动前已通过、改动后仍须通过，用于防止回归）。gold 补丁平均涉及 9.1 个 FAIL_TO_PASS 测试（最多 1,633 个），每个实例平均共 120.8 个测试。
- **判定是全有或全无。** 用 `patch` 应用预测补丁后，只有当补丁成功应用**且所有** FAIL_TO_PASS **与所有** PASS_TO_PASS 测试都通过，实例才算*已解决*，不设部分得分。
- **指标为 % Resolved** =（已解决实例 / 总数）× 100。另有 "% Apply"（补丁能否干净应用的比例）用于诊断，但不作为评分指标。
- **报告的 % Resolved（表 5）。** BM25 检索上下文下：Claude 2 为 1.96%、SWE-Llama 13b 为 0.70%、ChatGPT-3.5 为 0.20%、GPT-4 为 0.00%；oracle（gold 文件）上下文下：Claude 2 为 4.80%、SWE-Llama 13b 为 4.00%、SWE-Llama 7b 为 3.00%、GPT-4 为 1.74%。Claude 2 最强，BM25 下解决 1.96%。

## Typical Duration

原始协议是单次生成（每个实例一个补丁、贪心解码、Pass@1），而非多步 agent 循环，因此没有单任务的步数或 wall-clock 预算。规模由上下文决定：issue 描述平均 195 词，代码库平均约 3,010 个非测试文件 / 43.8 万行（最多 88.6 万行），超过所有被测模型的上下文窗口，因此改用 BM25 检索（13K / 27K / 50K token 预算）或 oracle gold 文件提供上下文；模型分别运行在 16K（ChatGPT-3.5）、32K（GPT-4）、100K+（Claude 2、SWE-Llama）窗口下。gold 补丁平均编辑 1.7 个文件 / 32.8 行 / 3 个函数。

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
