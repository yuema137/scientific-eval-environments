# Insights Generator (2026)

## Overview

Insights Generator is a multi-agent system for corpus-level trace diagnostics for LLM agents. It answers diagnostic questions by proposing and testing hypotheses across a corpus of execution traces to produce an evidence-backed insights report — automating what would otherwise be manual trace inspection.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.21347>

## Summary

Insights Generator addresses automated diagnosis of LLM agent failures. Rather than manual inspection of individual traces, it deploys a multi-agent system that formulates and tests hypotheses across the entire trace corpus. Users who implemented its recommendations improved downstream agent performance by 30.4 percentage points.

## Tasks

Not a task suite. The system operates on corpora of execution traces from arbitrary agent tasks.

## Domains

General LLM-agent trace diagnostics.

## Evaluation

- Diagnostic-report quality as the direct output.
- Downstream impact: users implementing the recommendations improved performance by 30.4 percentage points.

## Typical Duration

Offline analysis over a trace corpus; not task-bounded.

## Main Contribution

An automated multi-agent diagnostic system that turns trace corpora into evidence-backed insights reports, and demonstrates measurable downstream improvement (+30.4 pp) from acting on those insights.

## Key Design Ideas

- Multi-agent hypothesis proposal and testing over a trace corpus.
- Evidence-backed insights report as the output artifact.
- Corpus-level rather than per-trace analysis.
- Measurable downstream lift as the primary success metric.

## Strengths

- Automates trace inspection that would otherwise be manual and unscalable.
- Reports concrete downstream impact rather than only diagnostic-report quality.
- Corpus-level analysis surfaces cross-trace patterns that per-trace inspection misses.

## Limitations

- Repository note: Not a task suite — utility depends on the trace corpora it is applied to.

## Related Works

- [AgentAtlas](./agentatlas.md) — Also a diagnostic contribution rather than a task suite; AgentAtlas emphasizes a shared vocabulary, Insights Generator emphasizes automated hypothesis testing.
