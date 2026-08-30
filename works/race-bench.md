# RACE-Bench (2026)

> **English** | [简体中文](../zh/works/race-bench.md)

> **First appeared:** 2026-03-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2603.26337)

## Overview

RACE-Bench is a reasoning-augmented benchmark for evaluating repository-level code agents on real-world feature-addition tasks, pairing executable patch verification with structured intermediate reference reasoning so that agents are assessed not only on final test correctness but on how their reasoning aligns with developer-accepted trajectories.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


N/A — General-purpose repository-level software-engineering (feature-addition) benchmark; excluded as general application software engineering.

## Links

- **Paper:** <https://arxiv.org/abs/2603.26337>
- **Venue:** arXiv preprint (cs.SE), submitted March 2026

## Summary

RACE-Bench targets a gap in repository-level code-agent evaluation: existing benchmarks judge agents as black boxes by final test correctness, giving little insight into how they reason or where failures arise. The benchmark contains 528 real-world feature-addition instances drawn from 12 open-source repositories. Each instance is paired with executable patch verification and structured intermediate reference reasoning covering issue understanding, file localization, implementation tasks, and step decomposition. On top of this, RACE-Bench defines a dual-track evaluation framework that jointly measures patch correctness and the alignment of an agent's intermediate reasoning with developer-accepted reference trajectories. Evaluating three representative repository-level code agents, the authors report Resolved Rate ranging from 29% to 70% across agents, and find that reasoning quality degrades most when agents translate high-level intent into concrete implementation steps.

## Tasks

528 real-world feature-addition instances from 12 open-source repositories. Each instance carries (a) an executable patch-verification harness and (b) structured intermediate reference reasoning decomposed into issue understanding, file localization, implementation tasks, and step decomposition. The task is repository-level feature addition — implementing a new feature so that the associated tests pass. The specific 12 repositories, the per-repository instance breakdown, and the construction/curation pipeline for the reference reasoning are TODO(reference).

## Domains

Software & Systems — repository-level feature addition across 12 real-world open-source software repositories.

## Evaluation

Dual-track evaluation. (1) **Patch correctness**: agent-produced patches are checked with executable verification (test-based resolution), summarized as a Resolved Rate; reported values range from 29% to 70% across the three evaluated agents. (2) **Reasoning alignment**: the agent's intermediate reasoning is compared against developer-accepted reference trajectories (issue understanding, file localization, implementation tasks, step decomposition), using recall- and over-prediction–style measures of coverage relative to the reference reasoning. The authors report that patches which apply but still fail the tests cover fewer reference-reasoning elements (35.7% lower recall and 94.1% higher over-prediction than successful patches). The exact scoring definitions, whether an LLM judge is used for reasoning alignment, and the identities of the three evaluated agents are TODO(reference).

## Typical Duration

TODO(reference). The paper does not state a per-task step, wall-clock, or token budget in the sources verified here.

## Main Contribution

A reasoning-augmented, repository-level feature-addition benchmark that moves beyond final-test-correctness evaluation by pairing each instance with structured intermediate reference reasoning and a dual-track framework that jointly scores patch correctness and reasoning alignment, surfacing where in the reasoning process agents fail rather than only whether they fail.

## Key Design Ideas

- Repository-level feature addition (rather than bug fixing) as the evaluation target.
- Structured intermediate reference reasoning per instance, decomposed into issue understanding, file localization, implementation tasks, and step decomposition.
- Dual-track evaluation that jointly measures final patch correctness and alignment of intermediate reasoning with developer-accepted reference trajectories.
- Diagnostic reasoning-level analysis linking apply-but-fail patches to reduced coverage of reference-reasoning elements.

## Strengths

- Provides intermediate, process-level signal (reasoning alignment) in addition to outcome-level signal (patch correctness), addressing the black-box limitation of test-only benchmarks.
- Built from real-world feature-addition instances across 12 open-source repositories with executable verification.
- Reasoning-level analysis yields concrete diagnostic findings — e.g., agents understand high-level intent well but degrade when translating it into concrete implementation steps.

## Limitations

- Repository note: The three evaluated agents, the 12 repositories, and the exact reasoning-alignment scoring procedure are not confirmed from the primary source here and remain TODO(reference).
- Repository note: Reference reasoning derived from developer-accepted trajectories may privilege one accepted implementation path; whether alternative valid trajectories are credited is not verified here.

## Related Works

- [SWE-bench ProMax](./swe-bench-promax.md) — Also a repository-level coding-agent benchmark built from real commits, but focused on multilingual large-scale refactoring rather than feature addition with reasoning-alignment scoring.
