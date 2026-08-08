# CORE-Bench (2024)

> **English** | [简体中文](../zh/works/core-bench.md)

## Overview

CORE-Bench (Computational Reproducibility Agent Benchmark) measures whether AI agents can reproduce the results of published studies from the provided code and data: 270 tasks based on 90 scientific papers across computer science, social science, and medicine, at three difficulty levels.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.11363>
- **Code:** <https://github.com/siegelz/core-bench>
- **Venue:** arXiv preprint, 2024

## Summary

CORE-Bench targets computational reproducibility — reproducing a study's results using its own released code and data — as a real-world scientific task that is fundamental yet surprisingly challenging. Tasks span three difficulty levels and include both language-only and vision-language variants, with a fast, parallelizable evaluation system that saves days per run over sequential evaluation. Baselines (general-purpose AutoGPT and the task-specific CORE-Agent, each with GPT-4o and GPT-4o-mini) top out at 21% accuracy on the hardest level.

## Tasks

270 tasks from 90 scientific papers across three disciplines, at three difficulty levels, in language-only and vision-language forms; agents work from each paper's provided code and data.

## Domains

Computer science, social science, and medicine — the three disciplines whose papers the tasks are drawn from.

## Evaluation

- Accuracy of reproduced results, checked by a fast, parallelizable evaluation system.
- **Reported.** The best agent achieves 21% accuracy on the hardest difficulty level.

## Typical Duration

Multi-step reproduction workflows over provided artifacts; budgets are TODO(reference).

## Main Contribution

Isolates the floor of research automation — rerunning published work from its own artifacts — and shows even that floor is far from solved.

## Key Design Ideas

- Working from provided code and data separates reproducibility from reinvention.
- Three difficulty levels grade how much scaffolding the agent receives.
- Parallelizable evaluation makes repeated agent comparison practical.

## Strengths

- Directly corresponds to a real, consequential scientific practice.
- Cross-disciplinary coverage rather than a single-field testbed.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [PaperBench](./paperbench.md) — Also replication-focused, from scratch against author rubrics rather than from provided artifacts.
- [EXP-Bench](./exp-bench.md) — Also reproduces published experiments end to end, with LLM-judged stage grading.
- [AutoMat](./automat.md) — Also claim reproduction from papers and artifacts, in computational materials science.
