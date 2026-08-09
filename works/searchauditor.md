# SearchAuditor (2026)

> **English** | [简体中文](../zh/works/searchauditor.md)

## Overview

SearchAuditor is a multi-perspective auditing framework that localizes, attributes, and repairs failures in long-horizon search agents, released with SearchAuditBench — 1,243 expert-annotated failed trajectories collected from eight open-weight models on five deep-search benchmarks.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.05212>
- **Venue:** arXiv preprint, 2026

## Summary

SearchAuditBench's failed trajectories average 73.1 messages and 65.1K tokens; each is expert-annotated with the critical error step, a search-specific root cause, and a reference repair with grading rubrics. SearchAuditor performs evidence-grounded adjudication across multiple perspectives to localize and attribute failures and to propose repairs whose application improves agent recovery.

## Tasks

SearchAuditBench: 1,243 failed trajectories (avg. 73.1 messages, 65.1K tokens) from eight open-weight models on five deep-search benchmarks, each expert-annotated with critical error step, search-specific root cause, and a reference repair with grading rubrics.

## Domains

Long-horizon deep-search agent trajectories.

## Evaluation

- Auditing quality measured end-to-end: localization of the critical step, attribution to a root cause, and repair against reference rubrics.
- **Reported.** The strongest baseline reaches only a 26.6% end-to-end pass rate, while SearchAuditor reaches 32.3% with frontier models such as GPT-5.5; applying its repairs improves agent recovery.

## Typical Duration

Post-hoc auditing of long failed search trajectories (average 65.1K tokens).

## Main Contribution

Turns search-agent failure analysis into a benchmarked, expert-anchored task — localize, attribute, repair — rather than an informal debugging practice.

## Key Design Ideas

- Expert annotation fixes the critical step and root cause, so auditors are scored against ground truth.
- Root causes are search-specific rather than generic error labels.
- Reference repairs with rubrics make the repair step gradable, not just the diagnosis.

## Strengths

- Large, expensive-to-produce corpus of real failures across models and benchmarks.
- End-to-end pass rate shows the task is far from solved (best 32.3%).

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [TRAJDEBUG](./trajdebug.md) — Also attributes critical failures in annotated failed trajectories, for tool-use and coding rather than deep search.
- [TELBench](./telbench.md) — Also expert-segments deep-research trajectories for error localization, at span level.
- [Who&When Pro](./who-and-when-pro.md) — Also scores failure attribution, with constructed rather than natural failures.
