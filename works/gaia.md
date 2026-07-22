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

466 real-world questions, organized into three difficulty levels by the number of steps and tools required: **Level 1** (146 questions — no tools or at most one, ≤5 steps), **Level 2** (245 — roughly 5–10 steps combining different tools), and **Level 3** (75 — arbitrarily long action sequences for a near-perfect assistant). Answers to 166 questions are released as a validation set; the 300-question test set withholds answers to power a leaderboard. Each question requires composing fundamental assistant abilities (reasoning, multimodality, web browsing, tool use).

## Domains

General-assistant questions spanning everyday and knowledge-intensive tasks requiring web and tool access; multimodal inputs are included.

## Evaluation

- **Metric: quasi-exact-match accuracy.** A model's answer is compared to a single ground-truth answer up to a normalization tied to the answer type: numbers are written without commas or units, strings without articles or abbreviations and with digits in plain text. Answers must be a number, as few words as possible, or a comma-separated list. There is no partial credit.
- **No LLM judge.** Scoring is deterministic string/number matching under those normalization rules, which is why questions are authored to have a single unambiguous answer.
- **Reported (overall):** humans 92% vs. 15% for GPT-4 equipped with plugins. **Per level** (human vs. GPT-4+plugins): Level 1 93.9% vs. 30.3%, Level 2 91.8% vs. 9.7%, Level 3 87.3% vs. 0%.

## Typical Duration

Multi-step tool use scaled by level: Level 1 needs ≤5 steps with at most one tool, Level 2 roughly 5–10 steps across multiple tools, and Level 3 arbitrarily long action sequences. Human annotators take from ~6 minutes (simplest) to ~17 minutes (most complex) per question. No fixed model step-cap is specified.

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

- Repository note: The single-answer quasi-exact-match format is objective but excludes open-ended tasks whose quality cannot be captured by one normalized string.

## Related Works

- [AgentBench](./agentbench.md) — Also targets general agent capability, but across multiple interactive environments rather than a unified QA surface.
- [WebArena](./webarena.md) — Also requires real web interaction, but scored by functional correctness inside live websites rather than answer matching.
