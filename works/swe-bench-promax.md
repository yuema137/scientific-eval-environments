# SWE-Bench ProMax (2026)

> **English** | [简体中文](../zh/works/swe-bench-promax.md)

> **First appeared:** 2026-08-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.09802)

## Overview

SWE-Bench ProMax is an expert-curated, multilingual code-refactoring benchmark of 170 real-commit instances across seven programming languages, designed to test coding agents on coordinated, behavior-preserving changes that span many files.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General-purpose software-engineering (multilingual code-refactoring) benchmark; excluded as general application software engineering, not scientific/engineering software.

## Links

- **Paper:** <https://arxiv.org/abs/2608.09802>
- **Venue:** COLM 2026 (arXiv comment: "Published as a conference paper at COLM 2026")

## Summary

SWE-Bench ProMax targets code refactoring — coordinated, behavior-preserving changes across many files — which the authors argue is a substantially harder and more realistic test of agent capability than existing issue-resolution benchmarks that are rapidly saturating. It comprises 170 instances drawn from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Each instance undergoes a multi-stage curation process intended to address quality problems identified in prior benchmarks: issue descriptions are rewritten from scratch to provide precise, unambiguous specifications, and test suites are manually reviewed to remove overly narrow tests (which reject correct solutions) and overly broad tests (which check unstated requirements). Tasks with insufficient complexity or limited cross-file scope are filtered out, yielding large-scale refactoring tasks that average 11.4 modified files and 261.6 lines of code per instance.

## Tasks

170 code-refactoring instances drawn from real commits across seven programming languages: Python, Java, TypeScript, Go, C, C++, and Rust. Each task requires coordinated, behavior-preserving changes across multiple files. Tasks average 11.4 modified files and 261.6 lines of code per instance. Instances are produced by a multi-stage curation pipeline: (a) issue descriptions rewritten from scratch for precise, unambiguous specifications; (b) test suites manually reviewed to remove overly narrow and overly broad tests; and (c) filtering out tasks with insufficient complexity or limited cross-file scope. The exact per-language instance breakdown and the full curation procedure are TODO(reference).

## Domains

Software engineering — real-world multilingual open-source repositories spanning seven programming languages (Python, Java, TypeScript, Go, C, C++, Rust).

## Evaluation

Execution-based: agents are scored by a resolve rate (fraction of instances resolved) against the instances' manually reviewed test suites, which are curated so that a correct behavior-preserving refactoring passes while overly narrow or overly broad tests are removed. Frontier models were evaluated under two agent scaffolds; the best model achieves only a 41.2% resolve rate. The specific models evaluated, the exact pass/fail criteria, and the two agent scaffolds are TODO(reference).

## Typical Duration

TODO(reference). The paper characterizes task scale by edit size — 11.4 modified files and 261.6 lines of code per instance on average — but a per-task step, wall-clock, or token budget is not stated in the abstract.

## Main Contribution

Introduces a multilingual, expert-curated benchmark of large-scale code-refactoring tasks whose curation directly addresses quality problems identified in prior software-engineering benchmarks (flawed narrow/broad tests, ambiguous issue specifications), providing a harder, less-saturated test of coding-agent capability at a scale exceeding existing benchmarks.

## Key Design Ideas

- Refactoring — coordinated, behavior-preserving, cross-file changes — as the evaluation target, rather than single-issue bug fixes.
- Multilingual coverage across seven programming languages (Python, Java, TypeScript, Go, C, C++, Rust).
- Multi-stage curation: issue descriptions rewritten from scratch for precise specifications, test suites manually reviewed to remove overly narrow and overly broad tests, and low-complexity or narrow-scope tasks filtered out.
- Large-scale tasks by construction (average 11.4 modified files and 261.6 lines of code per instance).

## Strengths

- Curation explicitly targets test-quality defects (overly narrow tests that reject correct solutions; overly broad tests that check unstated requirements) that a prior audit reported in a large fraction of unsolved SWE-bench Verified instances.
- Multilingual and large-scale by design, exceeding the per-instance edit scale of prior issue-resolution benchmarks.
- Low headroom reported (best model 41.2% resolve rate), indicating the benchmark is far from saturated.

## Limitations

- Repository note: At 170 instances the benchmark is comparatively small; per-language coverage and its balance are not verified here (TODO(reference)).
- Repository note: Specific evaluated models, agent scaffolds, and the exact grading harness are not stated in the abstract and remain unverified (TODO(reference)).

## Related Works

- [SWE-bench](./swe-bench.md) — Earlier real-GitHub-issue resolution benchmark; ProMax positions itself against its saturation and reported test-quality problems, and shifts the task to multilingual refactoring.
- [SWE-Interact](./swe-interact.md) — Also a software-engineering agent benchmark, focused on interactive, progressively specified requirements rather than large-scale refactoring.
- [SWE-Together](./swe-together.md) — Also repository-level software-engineering agent evaluation, focused on human–agent collaboration.
- [FrontierCode](./frontiercode.md) — Also a hard, real-repository coding-agent benchmark emphasizing curation quality.
