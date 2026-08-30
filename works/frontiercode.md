# FrontierCode (2026)

> **English** | [简体中文](../zh/works/frontiercode.md)

> **First appeared:** 2026-06-08 · **Source:** [Official announcement](https://cognition.com/blog/frontier-code)

## Overview

FrontierCode is an industry benchmark from Cognition presented as the first to measure mergeability — would the maintainer actually merge this pull request? — on realistic open-source programming tasks built by 20+ experienced developers spending more than 40 hours per task. No accompanying paper has been released (see the repository note under Limitations).

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Project:** <https://cognition.com/frontiercode>
- **Venue:** Industry benchmark (Cognition); no paper; current revision FrontierCode 1.1 (2026-07-07)

## Summary

FrontierCode scores end-to-end code quality — correctness, test quality, scope discipline, style, and adherence to codebase standards — on maintainer-written tasks in real open-source repositories, using an ensemble of grading techniques including unit tests, rubrics, and new types of verifiers. Internet access is restricted to documentation: runs that consult solution-bearing sources such as the original pull request are detected and scored zero.

## Tasks

Maintainer-written tasks across multiple real open-source repositories, authored by 20+ experienced developers at over 40 hours per task; exact task counts are TODO(reference).

## Domains

Open-source software engineering; no science domain.

## Evaluation

- Mergeability as the target construct; graded by an ensemble of unit tests, rubrics, and new verifier types over correctness, test quality, scope discipline, style, and codebase-standard adherence.
- Solution-leak detection: runs consulting sources such as the original pull request are scored zero.
- Headline numbers are published only on the interactive leaderboard; TODO(reference).

## Typical Duration

End-to-end pull-request-scale coding tasks; budgets are TODO(reference).

## Main Contribution

Shifts the coding-agent target from "tests pass" to "a maintainer would merge this," scoring the qualities human reviewers actually gate on.

## Key Design Ideas

- Mergeability bundles correctness with the review-time virtues (scope discipline, style, test quality) that pass/fail metrics ignore.
- Heavy per-task authoring investment (40+ hours) by experienced developers buys task realism.
- Built-in contamination detection zeroes runs that touch solution-bearing sources.

## Strengths

- Evaluates the deployment-relevant construct — acceptance by a maintainer — rather than a proxy.
- Explicit anti-leak enforcement at evaluation time.

## Limitations

- Repository note: card compiled from the official website only (August 2026); FrontierCode has no accompanying paper, so task counts, scores, and methodology details beyond the site's claims are TODO(reference) and the two-level content validation this repository applies to papers cannot be fully performed.

## Related Works

- [SWE-bench](./swe-bench.md) — Also real-repository coding tasks, graded by test suites rather than mergeability.
- [SWE-chat](./swe-chat.md) — Also grounds evaluation in what humans actually accept, via committed lines from real sessions.
- [Agents' Last Exam](./agents-last-exam.md) — Also expert-built realistic professional tasks at high authoring cost.
