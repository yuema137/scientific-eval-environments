# BioProBench (2025)

> **English** | [简体中文](../zh/works/bioprobench.md)

## Overview

BioProBench is a corpus and benchmark for biological protocol reasoning: 22,413 human-written protocols (BioProCorpus) expanded into 523,784 task instances across five task types — protocol QA, step ordering, error correction, protocol generation, and protocol reasoning.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07889>
- **Code:** <https://github.com/YuyangSunshine/bioprobench>
- **Dataset:** <https://huggingface.co/BioProBench>
- **Venue:** arXiv preprint (cs.CL); ICML 2026 per the official repository

## Summary

Wet-lab protocols are where biological reasoning meets physical consequence. BioProBench turns a large human-written protocol corpus into five task families probing procedural understanding, with metrics including accuracy, F1, step recall/precision, Kendall's tau, and BLEU (per the official repository). Evaluating 10 mainstream LLMs, performance drops significantly on tasks demanding deep reasoning, quantitative precision, and safety awareness. The paper pairs the benchmark with ProAgent as a baseline agent.

## Tasks

523,784 task instances derived from 22,413 human-written protocols, across five task types: protocol QA, step ordering, error correction, protocol generation, and protocol reasoning; static evaluation.

## Domains

Biological wet-lab protocols across 16 biological subdomains (per the official repository; the subdomains are not enumerated in the verified sources).

## Evaluation

- Task-specific metrics per the official repository: accuracy, F1, precision/recall, Step Recall/Step Precision, Kendall's tau, exact match, BLEU, Brier score.
- **Reported.** Across 10 mainstream LLMs, performance drops significantly on tasks demanding deep reasoning, quantitative precision, and safety awareness.

## Typical Duration

Single-instance protocol tasks; not an interactive agent setting.

## Main Contribution

Procedural biology at corpus scale: half a million instances that test whether models understand what lab steps do, in what order, and how they fail — the substrate any lab-automation agent must master.

## Key Design Ideas

- Five task types decompose procedural competence from recognition (QA) through repair (error correction) to synthesis (generation).
- Human-written protocols keep the distribution real rather than templated.
- Order-sensitive metrics (Kendall's tau, step recall) score procedures as sequences, not bags of steps.

## Strengths

- Corpus scale (22K protocols, 524K instances) unmatched in procedural biology.
- The reasoning/precision/safety weakness profile is directly relevant to lab-agent risk.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The repository cites the ICML 2026 acceptance under a variant title.
- Repository note: ProAgent, the paper's baseline agent, is agent implementation and out of this repository's scope; the card documents the corpus and benchmark.

## Related Works

- [SciGym](./scigym.md) — Also targets experimental biology, via interactive dry-lab experiment design rather than protocol text.
- [LAB-Bench](./lab-bench.md) — Also includes protocol reasoning (ProtocolQA) within a broader biology-research suite.
- [MDArena](./mdarena.md) — Also evaluates research-protocol-driven scientific work, as executable simulation workflows.
