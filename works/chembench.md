# ChemBench (2024)

> **English** | [简体中文](../zh/works/chembench.md)

## Overview

ChemBench asks whether large language models are "superhuman chemists": an automated evaluation framework with more than 2,700 curated question–answer pairs comparing leading open- and closed-source LLMs against the expertise of human chemists — the best models outperformed the best human chemists in the study on average.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2404.01475>
- **Code:** <https://github.com/lamalab-org/chembench>
- **Project:** <https://chembench.lamalab.org>
- **Leaderboard:** <https://huggingface.co/spaces/jablonkagroup/ChemBench-Leaderboard>
- **Venue:** Nature Chemistry, 2025 (per the official project site; arXiv metadata carries no venue)

## Summary

Published as "Are large language models superhuman chemists?", ChemBench curates over 2,700 question–answer pairs spanning chemical knowledge and reasoning and scores state-of-the-art LLMs with an automated framework against a human-chemist cohort. The best models beat the best human chemists in the study on average, yet struggle with some basic tasks and provide overconfident predictions — a combination the authors read as both impressive capability and a safety concern, with implications for chemistry education.

## Tasks

More than 2,700 curated question–answer pairs on chemical knowledge and reasoning; static QA answered without tools, scored automatically.

## Domains

Chemistry — chemical knowledge and reasoning benchmarked directly against practicing chemists.

## Evaluation

- Automated framework scoring model answers on curated QA pairs, with a human-chemist expert baseline and confidence analysis.
- **Reported.** The best models outperform the best human chemists in the study on average; models struggle with some basic tasks and give overconfident predictions.

## Typical Duration

Single-turn question answering; no interactive or agentic setting.

## Main Contribution

A large-scale, human-baselined measurement of LLM chemical capability whose framework became reusable infrastructure — the multimodal MaCBench runs on the same pipeline.

## Key Design Ideas

- Curated QA at a scale (2,700+) that supports per-topic capability breakdowns rather than one aggregate score.
- A recruited chemist cohort turns "superhuman" from rhetoric into a measured comparison.
- Confidence is probed alongside accuracy, surfacing overconfidence as a distinct failure mode.

## Strengths

- One of the largest expert-baselined chemistry evaluations, with an actively maintained leaderboard.
- The framework outlived the paper: it is the substrate for follow-on multimodal evaluation.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The Nature Chemistry venue is stated by the official project site, not arXiv metadata.
- Static QA — chemical capability is measured without tool use or multi-step lab/agent workflows.

## Related Works

- [MaCBench](./macbench.md) — The multimodal (vision-language) chemistry and materials extension, run via the ChemBench pipeline.
- [ChemEval](./chemeval.md) — Also broad-coverage chemical capability evaluation, organized into progressive levels.
- [ChemIQ](./chemiq.md) — Also expert-style chemistry questions, focused on organic chemistry with judge-free checking.
