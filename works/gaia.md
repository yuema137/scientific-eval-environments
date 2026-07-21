# GAIA (2023)

## Overview

GAIA is a benchmark for General AI Assistants posing real-world questions that require reasoning, multi-modality handling, web browsing, and general tool-use proficiency. The questions are conceptually simple and unambiguous for humans yet hard for frontier models.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.12983>
- **Project:** <https://huggingface.co/gaia-benchmark>

## Summary

GAIA proposes real-world questions whose solution would represent a milestone for general AI assistants. Each question requires a set of fundamental abilities — reasoning, multi-modality handling, web browsing, and tool use — yet is designed to have a single unambiguous answer that humans can produce reliably. The benchmark exposes a large human-model gap: human respondents reach 92% while GPT-4 equipped with plugins reaches 15%.

## Tasks

466 real-world questions with answers, of which 300 answers are retained for a leaderboard. Each requires composing fundamental assistant abilities (reasoning, multimodality, web browsing, tool use).

## Domains

General-assistant questions spanning everyday and knowledge-intensive tasks requiring web and tool access; multimodal inputs are included.

## Evaluation

- Each question is designed to have a single correct, unambiguous answer, enabling automatic scoring.
- Exact scoring protocol details: TODO(reference) — not detailed in the abstract.
- Reported: humans obtain 92% vs. 15% for GPT-4 equipped with plugins.

## Typical Duration

Multi-step: questions typically require several browsing/tool-use steps. Per-task budget: TODO(reference) — not stated in the abstract.

## Main Contribution

A benchmark whose questions are conceptually simple and unambiguous for humans but require real assistant capabilities (tool use, browsing, multimodality), exposing a large and diagnostic human-model gap.

## Key Design Ideas

- Questions easy and unambiguous for humans but hard for models — an asymmetry that resists shortcut-solving.
- Requires composing multiple fundamental abilities in one question.
- Single-answer design enables objective, low-ambiguity scoring.
- A held-out answer split supports a leaderboard.

## Strengths

- Clear, unambiguous answers make scoring objective.
- Tests real assistant abilities (browsing, tools, multimodality) rather than closed-book knowledge.
- Large human-model gap gives a strong headroom signal.

## Limitations

- Repository note: The precise automatic-scoring protocol is not detailed in the abstract and is marked `TODO(reference)`.

## Related Works

- [AgentBench](./agentbench.md) — Also targets general agent capability, but across multiple interactive environments rather than a unified QA surface.
- [WebArena](./webarena.md) — Also requires real web interaction, but scored by functional correctness inside live websites rather than answer matching.
