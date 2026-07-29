# SWE-bench (2023)

## Overview

SWE-bench evaluates whether language models can resolve real-world GitHub issues by editing a codebase. It consists of 2,294 issue-and-pull-request task instances drawn from 12 popular Python repositories, and grades a model's patch by executing the repository's own tests.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.06770>
- **Code:** <https://github.com/SWE-bench/SWE-bench>
- **Venue:** ICLR 2024

## Summary

SWE-bench frames software engineering as a testbed for evaluating language models. Each task provides a codebase and a natural-language description of an issue to resolve; the model must edit the codebase to address it. Resolving an issue frequently requires understanding and coordinating changes across multiple functions, classes, and files, interacting with execution environments, processing very long contexts, and reasoning beyond traditional code generation. The 2,294 instances are mined from real GitHub issues and their corresponding merged pull requests, making the task source naturally sourced and refreshable.

## Tasks

2,294 software-engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories. Each task gives a codebase plus an issue description; the target is a patch that resolves the issue.

## Domains

Software engineering — open-source Python repositories.

## Evaluation

- **Two test sets per task.** Each instance ships a *test patch* that defines **FAIL_TO_PASS** tests (failing before the fix, required to pass after — they verify the issue is actually resolved) and **PASS_TO_PASS** tests (already passing before the change, required to still pass — they guard against regressions). Gold patches touch on average 9.1 FAIL_TO_PASS tests (max 1,633) out of 120.8 total tests per instance.
- **Resolution is all-or-nothing.** The predicted patch is applied with `patch`; an instance counts as *resolved* only if the patch applies **and every** FAIL_TO_PASS **and every** PASS_TO_PASS test passes. There is no partial credit.
- **Metric: % Resolved** = (resolved instances / total) × 100. A separate "% Apply" (fraction of patches that apply cleanly) is reported for diagnosis but is not the scored metric.
- **Reported % Resolved (Table 5).** With BM25-retrieved context: Claude 2 1.96%, SWE-Llama 13b 0.70%, ChatGPT-3.5 0.20%, GPT-4 0.00%. With "oracle" (gold-file) context: Claude 2 4.80%, SWE-Llama 13b 4.00%, SWE-Llama 7b 3.00%, GPT-4 1.74%. Claude 2 is the strongest, resolving 1.96% under BM25.

## Typical Duration

The original protocol is single-shot generation (one patch per instance, greedy decoding, Pass@1) rather than a multi-step agent loop, so there is no per-task step or wall-clock budget. Scale is instead set by context: issue descriptions average 195 words, and codebases average ~3,010 non-test files / 438K lines (max 886K) — larger than every evaluated model's context window, so context is supplied by BM25 retrieval at 13K / 27K / 50K-token budgets or by oracle gold-file selection. Models were run at 16K (ChatGPT-3.5), 32K (GPT-4), and 100K+ (Claude 2, SWE-Llama) token windows. Gold patches edit 1.7 files / 32.8 lines / 3 functions on average.

## Main Contribution

Introduces real-world software engineering (GitHub issue resolution) as a rich, sustainable, execution-verified testbed for evaluating language models beyond traditional single-function code generation.

## Key Design Ideas

- Tasks mined from real GitHub issues and merged pull requests — a naturally sourced, refreshable task supply.
- Execution-based grading via each repository's own test suite rather than reference-string matching.
- Tasks require multi-file, cross-function coordination and long-context processing.
- **SWE-bench Verified** — a 500-instance human-filtered subset created in collaboration with OpenAI, where human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable, enabling more reliable evaluation of coding agents.

## Strengths

- Real, sustainable task source that resists saturation and can be refreshed as new issues arise.
- Objective, execution-based grading.
- Very low initial solve rate (1.96%) left large headroom for successive model generations.

## Limitations

- Repository note: Scope is Python open-source repositories; generalization to other languages and ecosystems is not directly evaluated.
- Repository note: The original test set contains some under-specified or unsolvable instances, which motivated the human-filtered SWE-bench Verified subset.

## Related Works

- [Enconda-bench](./enconda-bench.md) — Also software-engineering agent evaluation, but process-level scoring of environment configuration rather than end-to-end issue resolution.
- [AgentBench](./agentbench.md) — Also a general agent benchmark; multi-environment rather than software-engineering-specific.
