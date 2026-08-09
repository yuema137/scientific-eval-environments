# SWE-Interact (2026)

> **English** | [简体中文](../zh/works/swe-interact.md)

## Overview

SWE-Interact is a testbed for evaluating coding agents on multi-turn, interactive, user-driven software-engineering tasks: a user simulator reveals requirements progressively and gives feedback, testing whether agents can discover intent, adapt to changes, and build on prior work.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.30573>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

SWE-Interact reimagines SWE benchmarks as user-driven long-horizon coding sessions: instead of a complete task description up front, requirements arrive progressively through a simulated user who also reacts to the agent's work. The headline finding is a transfer gap — frontier models (Opus 4.8, GPT-5.5, and open-weight variants) that solve roughly 50% of the tasks in single-turn form drop to roughly 25% in the multi-turn, user-driven setting: strong single-turn SWE performance does not reliably transfer to interactive workflows.

## Tasks

Multi-turn, user-driven software-engineering sessions in which a user simulator progressively reveals requirements and provides feedback; task counts are TODO(reference).

## Domains

Interactive software engineering with simulated users.

## Evaluation

- Task success under the multi-turn user-driven protocol, compared directly against single-turn baselines on the same underlying tasks.
- **Reported.** Top models solve ~50% single-turn but only ~25% multi-turn — interactive performance roughly halves.

## Typical Duration

Multi-turn sessions with progressive requirement revelation.

## Main Contribution

Quantifies the single-turn-to-interactive transfer gap in software engineering: the benchmark's paired design shows one-shot competence overstates collaborative competence by roughly a factor of two.

## Key Design Ideas

- Progressive requirement revelation makes intent discovery a scored skill, not an assumption.
- The same tasks run single-turn and multi-turn, so the interaction penalty is isolated.
- A reactive user simulator standardizes the human side of the collaboration.

## Strengths

- The paired ~50%→~25% comparison is a clean, controlled measurement of interactivity cost.
- Targets the deployment reality of coding assistance rather than batch issue-solving.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [SWE-Together](./swe-together.md) — Also multi-turn interactive coding evaluation, reconstructed from real sessions rather than simulated from scratch.
- [SWE-bench](./swe-bench.md) — The single-turn paradigm whose transfer limits SWE-Interact measures.
- [SWE-chat](./swe-chat.md) — Also studies user-agent coding interaction, observationally over real sessions.
