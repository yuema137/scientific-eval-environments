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

- Execution-based: a model-generated patch is applied to the repository, and the repository's associated test suite is run to determine whether the issue is resolved.
- Reported: the best-performing model at publication, Claude 2, solved 1.96% of the issues.

## Typical Duration

Multi-step in agentic settings — understanding the issue, navigating the codebase, and editing across multiple files. Per-task wall-clock/token budget: TODO(reference) — not stated in the abstract.

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
