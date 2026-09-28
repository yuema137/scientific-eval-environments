# FrontierCode (2026)

> **English** | [简体中文](../zh/works/frontiercode.md)

> **First appeared:** 2026-06-08 · **Source:** [Official announcement](https://cognition.com/blog/frontier-code)

## Overview

FrontierCode is Cognition’s benchmark for whether a coding agent produces a pull request that a maintainer would merge. Maintainers of 36 open-source repositories helped define requirements beyond passing tests.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Project and leaderboard:** <https://cognition.com/frontiercode>
- **Initial methodology:** <https://cognition.com/blog/frontier-code>
- **Revision 1.1 (2026-07-07):** <https://cognition.com/blog/frontier-code-1.1>
- **Opus 5.5 evaluation settings:** <https://www.anthropic.com/claude-opus-5-5>
- **Venue:** Industry benchmark; official methodology posts, no accompanying paper located.

## Summary

An agent receives a repository, a concise task description, and codebase guidelines. Tests and reviewer-defined criteria assess the resulting patch for correctness, testing, scope, and style. Version 1.1 preserves legitimate web research while detecting access to solution-bearing upstream material; it also relaxes 75 overly strict blocker criteria after an audit of more than 1,000.

## Tasks

Extended contains 150 tasks; Main contains the 100 hardest. The former 50-task Diamond subset was deprecated in 1.1 because its membership no longer represented the hardest tasks and its low solve rates made results noisy. More than 20 experienced developers invested over 40 hours per task in authoring and review.

## Domains

Open-source software engineering; no science domain.

## Evaluation

- Report both blocker pass rate and a weighted rubric score; the original protocol assigns zero score when blocker requirements fail. Tests and other verifiers are combined with rubric grading and adversarial, calibration, and manual quality checks.
- Legitimate documentation, API, and background searches are allowed. A fair-use prompt and programmatic scanner penalize solution-bearing PRs, patches, mirrors, or upstream files with zero scores.
- The initial protocol runs five trials at each available reasoning effort and reports the best effort’s mean. The leaderboard also compares cost and speed.
- Snapshot checked 2026-09-27: the official Main leaderboard’s published data places Opus 5.5 first at 54.6%, with Opus 5 at 53.4% and GPT-6 Astra at 53.3%. Its changelog added Opus 5.5 on September 22; the methodology remains 1.1.
- Anthropic separately reports Opus 5.5 at 54.4% with max effort and 54.6% with medium effort. Its max-effort table lists Opus 5 at 48.0%; do not substitute that baseline into the best-effort leaderboard comparison.

## Typical Duration

Pull-request-scale tasks. The 40+ hours above measure task-authoring effort, not agent runtime; a common per-run wall-clock budget is TODO(reference).

## Main Contribution

Shifts the coding-agent target from "tests pass" to "a maintainer would merge this," scoring the qualities human reviewers actually gate on.

## Key Design Ideas

- Mergeability bundles correctness with the review-time virtues (scope discipline, style, test quality) that pass/fail metrics ignore.
- Heavy per-task authoring investment (40+ hours) by experienced developers buys task realism.
- Built-in contamination detection zeroes runs that touch solution-bearing sources.

## Strengths

Maintainer-defined acceptance criteria assess code quality beyond functional correctness. Explicit internet-use rules preserve legitimate research while checking solution leakage.

## Limitations

- Repository note: scores depend on methodology revision, reasoning effort, and evaluation setup; the official leaderboard and a model vendor’s table are distinct snapshots.
- Anthropic’s release evaluation enables production safeguards and uses older-model fallbacks on affected task categories. It should not be interpreted as an unconditional, pure Opus 5.5 run on every task.
- Repository note: official methodology posts provide substantive task and grading evidence despite the absence of a conventional paper.

## Related Works

- [SWE-bench](./swe-bench.md) — Also real-repository coding tasks, graded by test suites rather than mergeability.
- [SWE-chat](./swe-chat.md) — Also grounds evaluation in what humans actually accept, via committed lines from real sessions.
- [Agents' Last Exam](./agents-last-exam.md) — Also expert-built realistic professional tasks at high authoring cost.
