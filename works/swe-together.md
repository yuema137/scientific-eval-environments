# SWE-Together (2026)

> **English** | [简体中文](../zh/works/swe-together.md)

## Overview

SWE-Together is a multi-turn coding benchmark reconstructed from real user-agent sessions: 109 repository-level tasks curated from 11,260 recorded sessions, replayed across agents through a reactive LLM-based user simulator that preserves the original users' intents.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.29957>
- **Venue:** arXiv preprint (cs.SE, cs.AI), 2026

## Summary

Most coding-agent benchmarks are static — full task up front, judged on final code — while real assistance is interactive. SWE-Together makes real interactions verifiable by selecting sessions with recoverable repository states, clear user goals, and observable outcomes, then replaying them via a user simulator that preserves original intent and intervenes when the agent's progress requires it. Agents are scored as collaborators: final repository correctness plus the number of corrective feedback turns needed. Stronger agents generally achieve higher success with fewer interventions.

## Tasks

109 repository-level multi-turn tasks curated from 11,260 recorded real user-agent sessions, each with recoverable repository state, a clear user goal, and an observable outcome.

## Domains

Interactive software engineering grounded in real user sessions.

## Evaluation

- **Final repository correctness** plus the **number of corrective feedback turns** required during the interaction.
- **Reported.** Stronger agents generally achieve higher final success rates while requiring fewer interventions.

## Typical Duration

Multi-turn replayed sessions per task.

## Main Contribution

Turns real, messy user-agent collaborations into a verifiable benchmark, and measures agents on the cost they impose on the user — corrections needed — alongside whether the code ends up right.

## Key Design Ideas

- Curation from real sessions (recoverable state, clear goal, observable outcome) makes authenticity compatible with verifiability.
- The intent-preserving user simulator lets one real interaction be replayed fairly across different agents.
- Corrective-turn counting prices the human effort a collaboration consumes.

## Strengths

- Task distribution inherited from 11,260 real sessions rather than benchmark authors' imagination.
- The dual metric captures user experience, not just terminal correctness.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [SWE-chat](./swe-chat.md) — The observational counterpart: metrics over real sessions in the wild rather than replayed interactions.
- [SWE-Interact](./swe-interact.md) — Also multi-turn user-driven coding, with fully simulated progressive requirements.
- [SWE-bench](./swe-bench.md) — The static paradigm both interactive benchmarks depart from.
