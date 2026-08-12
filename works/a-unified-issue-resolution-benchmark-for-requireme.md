# SWE-RPG (2026)

> **English** | [简体中文](../zh/works/a-unified-issue-resolution-benchmark-for-requireme.md)

## Overview

SWE-RPG is a repository-level issue-resolution benchmark that pairs executable patch evaluation with validated ground-truth references for Requirement Clarification and Implementation Planning, enabling stage-aligned diagnosis of complete coding-agent trajectories rather than pass/fail-only scoring.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


N/A — General-purpose repository-level software-engineering issue-resolution benchmark (SWE-RPG); excluded as general application software engineering.

## Links

- **Paper:** https://arxiv.org/abs/2608.09072
- **Venue:** arXiv preprint (cs.SE; cs.AI), 2026

## Summary

Existing repository-level coding benchmarks typically score only whether the final patch passes tests, which cannot characterize how an unsuccessful trajectory diverges from the requirements and implementation process needed for a correct patch. SWE-RPG augments executable patch evaluation with intermediate ground-truth references (GTs) for two upstream stages — recovering explicit and implicit requirements (Requirement Clarification) and formulating a repository-grounded implementation plan (Implementation Planning). These intermediate GTs support retrospective, GT-aligned diagnosis of full trajectories across clarification, planning, code generation, and artifact submission. The benchmark comprises 163 tasks from 31 Python and Java repositories and is used to evaluate three coding agents across six LLM backends.

## Tasks

163 tasks drawn from 31 Python and Java repositories, comprising 113 bug fixes and 50 feature additions. Each task carries an executable evaluation harness (fail-to-pass and pass-to-pass tests) plus two validated intermediate ground-truth references:

- **Requirement Clarification GT** — question–answer information points derived from the base repository, issue and PR discussion, developer patch, and selected tests, organized under a practitioner-guided six-category taxonomy (C1–C6): Functional Intent, Business Semantics, Technical Context, Interface/Protocol, Code Structure/Conventions, and Data-Structure Semantics. The taxonomy was informed by seminar-style interviews with ten experienced software engineers. Synthesis agents produced candidate QA pairs using seed examples as few-shot demonstrations; a validation agent checked each pair against the repository, developer patch, and validated plan for evidential support, cross-stage consistency, and absence of implementation-detail leakage.
- **Implementation Planning GT** — an ordered sequence of modular steps recovered from the original issue, base repository, and merged PR. Each step is validated for functional reproducibility: a coding agent follows the step to generate a patch and an evaluator judges whether it is semantically equivalent to the corresponding gold subpatch, with failing steps revised via a gap-analysis and resolution agent.

The agentic components of the construction pipeline were instantiated with GPT-5.4. Two authors independently reviewed every clarification reference and every plan for evidential support and cross-stage consistency.

## Domains

Software & Systems Engineering — repository-level bug fixing and feature addition in real Python and Java software projects (31 repositories).

## Evaluation

- **Resolved rate (primary outcome metric):** a task is resolved only if its patch applies successfully, all fail-to-pass tests pass, and no pass-to-pass test regresses.
- **Failure attribution:** an LLM judge (GPT-5.6-Sol) assigns each failure to the earliest deviating stage — requirement understanding, planning, implementation, or others; reported stage-attribution accuracy was 92% on a 50-case sample.
- **Clarification coverage:** for each run, an LLM judge (GPT-5.6-Sol) determines whether the trajectory covers each GT information point, with coverage rates computed by category/dimension. On a 50-case sample, judge coverage decisions agreed with human consensus in 96% of cases.
- **Planning coverage:** trajectories are assessed against five planning dimensions — goal, target location, implementation approach, constraints, and validation strategy — evaluating semantic implementation responsibilities rather than exact plan matching.

## Typical Duration

TODO(reference) — the primary sources reviewed do not state a per-task trajectory length, wall-clock time, or token budget.

## Main Contribution

A repository-level benchmark that combines executable patch evaluation with validated intermediate ground-truth references for Requirement Clarification and Implementation Planning, enabling retrospective, GT-aligned diagnosis of complete coding-agent trajectories (clarification → planning → code generation → artifact submission) instead of pass/fail-only assessment, together with an empirical study localizing where coding agents fail.

## Key Design Ideas

- Attach validated intermediate ground truths for the requirement and planning stages to each executable issue-resolution task, so a trajectory can be diagnosed against a reference process, not just a final outcome.
- Ground the clarification reference in a practitioner-derived six-category information taxonomy elicited from interviews with ten software engineers.
- Validate planning steps by functional reproducibility — regenerate a patch from each step and check semantic equivalence to the gold subpatch — rather than by surface plan matching.
- Use an agentic synthesis-plus-validation construction pipeline with explicit checks for evidential support, cross-stage consistency, and implementation-detail-leakage, backed by independent two-author human review.
- Decompose evaluation into an outcome resolved-rate metric plus LLM-judge stage attribution and per-stage coverage metrics, calibrated against human consensus.

## Strengths

- Moves beyond pass/fail patch scoring to localize failures across clarification, planning, and implementation stages (paper).
- Intermediate GTs undergo both automated validation and independent human review by two authors (paper).
- Judge-based coverage and attribution decisions are calibrated against human consensus (96% agreement on coverage; 92% stage-attribution accuracy on 50-case samples) (paper).
- Covers two languages (Python and Java) across 31 repositories and both bug fixes and feature additions (paper).

## Limitations

- Evaluated coding agents achieve an average resolved rate of only 31.5%, with the best configuration (OpenCode–MoonshotAI-Kimi-K3) reaching 49.7% (paper).
- Failure attribution and coverage assessment rely on LLM judges (GPT-5.6-Sol); although calibrated against human consensus on samples, these judgments are not deterministic verifiers (paper).
- Repository note: the scale is moderate (163 tasks, 31 repositories) relative to the space of real-world repositories, and generalization beyond Python and Java is not evaluated in the primary source.

## Related Works

- [SWE-bench Pro Max](./swe-bench-promax.md) — another repository-level coding-agent issue-resolution benchmark.
