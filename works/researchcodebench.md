# ResearchCodeBench (2025)

> **English** | [简体中文](../zh/works/researchcodebench.md)

## Overview

ResearchCodeBench benchmarks LLMs on implementing novel machine-learning research code: 212 coding challenges that require translating cutting-edge contributions from top 2024–2025 research papers into executable code — where even the best model (Gemini-2.5-Pro) correctly implements only 37.3%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.02314>
- **Code:** <https://github.com/PatrickHua/ResearchCodeBench>
- **Project:** <https://researchcodebench.github.io/>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

ResearchCodeBench targets a contamination-resistant capability: implementing the novel contributions of very recent papers, published after most training cutoffs. Its 212 coding challenges ask a model to translate cutting-edge ML contributions from top 2024–2025 papers into executable code. Across 30+ proprietary and open-source LLMs, even the best implement less than 40%: Gemini-2.5-Pro-Preview leads at 37.3%, followed by o3 (High) at 32.3% and o4-mini (High) at 30.8%. A contamination-safe subset (13 of 20 papers, per the project page) isolates genuine novelty.

## Tasks

212 coding challenges translating novel contributions from recent (2024–2025) ML papers into executable code; static code generation. Full set spans 20 papers, with a 13-paper contamination-safe subset (project page).

## Domains

AI & Machine Learning Research — ML research-code implementation: turning recent paper contributions into working code.

## Evaluation

- Success rate on implementing the paper contributions, with analyses of contamination and error patterns.
- **Reported.** Best models under 40%: Gemini-2.5-Pro 37.3%, o3 (High) 32.3%, o4-mini (High) 30.8%.

## Typical Duration

Single-shot code-implementation challenges (static, not an interactive agent loop).

## Main Contribution

A recency-grounded, contamination-aware benchmark for implementing novel research code — measuring whether models can build the latest ideas rather than recall memorized ones.

## Key Design Ideas

- Post-cutoff 2024–2025 papers make memorization implausible, isolating genuine implementation.
- A contamination-safe subset explicitly separates novelty from possible leakage.
- Executable-code grading ties correctness to running the contribution, not describing it.

## Strengths

- Recency and contamination controls that most code benchmarks lack.
- Wide model coverage (30+) with a public repository and project site.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); no venue is stated in arXiv metadata. The 20-paper/13-paper-subset detail comes from the project page, not the abstract.

## Related Works

- [ML-Bench](./ml-bench.md) — Also ML code evaluation, at repository level rather than paper-contribution level.
- [SUPER](./super.md) — Also research-code execution, focused on repository setup and reproduction.
- [PaperBench](./paperbench.md) — Also implementing research from papers, at full-replication scale.
