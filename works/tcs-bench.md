# TCS-Bench (2026)

> **English** | [简体中文](../zh/works/tcs-bench.md)

## Overview

TCS-Bench is a benchmark for evaluating large language models on research-level Theoretical Computer Science (TCS) proof generation, where each task asks a model to produce a self-contained proof of a target result drawn from papers published at top TCS venues.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.09538
- **Venue:** arXiv preprint, 2026

## Summary

TCS-Bench assembles theorem-proving tasks from papers published at the top theoretical computer science venues — FOCS, STOC, and SODA — between 2020 and 2026. Each task supplies the context needed to derive a self-contained proof of a target statement, and models are scored on whether they can produce a correct proof. Because grading research-level proofs is itself difficult, the authors build an automated verification agent and calibrate it against human-expert judgements, reporting over 90% agreement with expert labels.

## Tasks

300 theorem-proving tasks. Each task presents a target statement together with the context required to derive a self-contained proof, extracted from papers at FOCS, STOC, and SODA (2020–2026). The construction pipeline parses LaTeX to extract statements, builds a dependency graph via an LLM-based analysis pass, assembles context through iterative section pruning and LLM compression, and applies structural and semantic quality filtering.

## Domains

Research-level theoretical computer science (theorem proving over results from FOCS, STOC, and SODA). Proof-generation tasks are mathematical in nature.

## Evaluation

Generated proofs are checked by an automated verification agent. The reference verifier makes four calls to Gemini 3.1 Flash and applies majority voting: a candidate proof is deemed correct when at least three of the four verdicts mark it correct. The verifier is calibrated against a human-expert–labeled set of 100 proofs (reported as 50 correct and 50 incorrect), on which it achieves over 90% accuracy. Reported model accuracies on the benchmark: GPT 5.6 Pro 68%, Colosseum (cross-model selection) 67.7%, Gemini 3.1 DeepThink 52%, Opus 5 32.77%, and Gemini 3.1 Pro 30.3%.

## Typical Duration

TODO(reference) — the sources consulted do not report a standardized per-task token budget or wall-clock time.

## Main Contribution

A benchmark of 300 research-level TCS theorem-proving tasks curated from top-tier venue papers (FOCS, STOC, SODA; 2020–2026), together with a validated automated proof-verification system that reaches over 90% agreement with human-expert judgements on a labeled calibration set.

## Key Design Ideas

- **Research-level source material.** Tasks are derived from proofs in papers accepted at FOCS, STOC, and SODA, rather than from textbook or competition problems.
- **Self-contained task construction.** A pipeline of LaTeX statement extraction, LLM-built dependency graphs, context assembly with section pruning and compression, and quality filtering produces tasks that carry the context needed to derive the target proof.
- **Automated verifier calibrated to experts.** Correctness is judged by an agent that issues four Gemini 3.1 Flash calls with 3-of-4 majority voting, calibrated against a 100-item human-expert–labeled set.

## Strengths

- Targets research-level proof generation from recently published top-venue TCS results rather than standardized exam-style problems (paper).
- Validates its automated grader against human-expert judgements, reporting over 90% accuracy on a 100-proof labeled set (paper).
- Evaluates a range of contemporary frontier models, with the strongest reaching 68% accuracy, indicating substantial remaining headroom (paper).

## Limitations

- The authors note a gap between the strongest model (68%) and perfect performance, indicating substantial room for improvement in multi-step mathematical reasoning (paper).
- Repository note: correctness relies on an LLM-based verification agent; while calibrated to over 90% expert agreement on a 100-item set, this leaves a residual error rate on automated grading of research-level proofs.

## Related Works

TODO(reference)
