# NatureBench (2026)

## Overview

NatureBench evaluates whether AI coding agents can match the published state-of-the-art of Nature-family scientific publications — framed as a move beyond reproduction toward the claim of methodological discovery.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.24530>

## Summary

NatureBench distills tasks from peer-reviewed Nature-family publications and asks whether coding agents can reach or exceed the published SOTA. The benchmark tests both cross-discipline scientific coverage and the depth needed to match a real publication's results.

## Tasks

90 tasks distilled from peer-reviewed Nature-family publications (2022–2025) across six domains: Cellular Omics 31, Protein Biology 16, Biomedical Modeling 14, Physical Modeling 13, Molecular Design 11, Relational Reasoning 5. Tasks are built by a review-gated "NatureGym" pipeline from ~5,500 candidate papers, with an information firewall that gives the agent the target algorithm's inputs but none of its operations or outputs.

## Domains

Six domains distilled from Nature-family publications: Cellular Omics, Protein Biology, Biomedical Modeling, Physical Modeling, Molecular Design, and Relational Reasoning.

## Evaluation

- **SOTA-normalized relative gap.** Each instance designates one primary metric; the score is g = dir · (m − m_sota) / |m_sota|, where m is the agent's value, m_sota the paper-reported SOTA, and dir ∈ {+1, −1} the metric direction — making g scale-free and comparable across the 81 distinct heterogeneous metrics used (AUROC, RMSE, Spearman ρ, ARI, F1, …). g ≥ 0 means the agent matched or surpassed the published result. A task's score averages g across its instances (mean 3.7 primary metrics per task); a failed submission scores g = −1.0, and a Claude Sonnet 4.6 judge flags shortcut runs.
- **Two threshold rates over the 90 tasks:** Match-SOTA (g ≥ 0) and Surpass-SOTA (g > 0.1).
- **Reported:** the strongest agent, Claude Opus 4.7, surpasses SOTA (g > 0.1) on only 17.8% of tasks (≈ 16/90) and matches it (g ≥ 0) on 47.8% (≈ 43/90), under a strict web-search-disabled protocol across three harnesses (Claude Code, Codex CLI, Gemini CLI).
- Author observation: agent successes are frequently driven by reformulating scientific problems into conventional prediction tasks, rather than genuine methodological innovation.

## Typical Duration

A 4-hour wall-clock budget per task (the clock pauses during scoring). Compute is allocated per task: 3 CPU-only tasks, 70 on a single RTX 3090/4090, and the 17 most intensive on a single A800.

## Main Contribution

Anchors benchmark difficulty to the published SOTA of top-venue scientific publications, providing a bar aligned with real research output rather than curated toy tasks.

## Key Design Ideas

- Task grounding in Nature-family publications provides a real-world SOTA reference point.
- Cross-discipline scope within a single benchmark.
- Explicit distinction between "matching SOTA" and "discovery."

## Strengths

- SOTA-grounded difficulty is tied directly to published scientific outcomes.
- Reveals a substantial gap (the strongest agent surpasses SOTA on only 17.8% of tasks) against a hard reference.
- Author observation surfaces a distinct evaluation concern (problem reformulation).

## Limitations

- Repository note: Distilled from Nature-family publications only — coverage is shaped by those venues' editorial focus.

## Related Works

- [AIRS-Bench](./airs-bench.md) — Also research-lifecycle science, but organized around a curated task suite rather than published SOTA reference.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also science-focused, but centered on containerized executable verification.
