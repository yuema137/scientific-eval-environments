# PSE-Bench (2026)

> **English** | [简体中文](../zh/works/pse-bench.md)

> **First appeared:** 2026-04-04 · **Source:** [Official repository creation](https://github.com/sombsuk/PSE-Bench)

## Overview

PSE-Bench is a benchmark of 200 open-ended questions spanning four core domains of process systems engineering, paired with a multi-judge evaluation framework in which five independent LLM judges score each response against a seven-element rubric.

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://doi.org/10.1016/j.ceja.2026.101375>
- **Code:** <https://github.com/sombsuk/PSE-Bench>
- **Venue:** Chemical Engineering Journal Advances, Volume 27 (2026), article 101375

## Summary

PSE-Bench targets the use of large language models as engineering consultation tools in chemical process systems engineering, where confidently phrased but incomplete answers carry risk in safety-critical settings. The benchmark holds 200 open-ended questions divided evenly across process modeling and simulation, process optimization, machine learning for chemical processes, and process design and systems engineering. Each model answer is scored by an ensemble of five independent AI judges against a seven-element rubric, a design intended to damp the systematic bias of any single judge, and the scores are checked against human expert judgment. Five commercial LLMs are evaluated zero-shot, and the released artifacts include the question set with ground truths and rubrics, the raw responses, the per-judge evaluations, and the human-validation data.

## Tasks

200 open-ended questions, 50 per domain, released as `ChemEng_Bench_200_GroundTruth.xlsx` with ground-truth answers and per-question rubrics. The four domains and their listed topics are: Process Modeling & Simulation (MOD) — thermodynamic modeling, flash calculations, reactor modeling, dynamic simulation; Process Optimization (OPT) — LP/NLP/MILP/MINLP, pinch analysis, real-time optimization, multi-objective optimization; Machine Learning for Chemical Processes (ML) — soft sensors, fault detection, physics-informed neural networks, transfer learning; Process Design & Systems Engineering (DES) — HAZOP, LOPA, process intensification, plantwide control, FEED. Questions are answered in a single turn without tools; the official repository records that all responses were collected on 23 February 2026 under zero-shot conditions.

## Domains

Chemical Engineering — the question set is process systems engineering throughout: thermodynamic and reactor modeling, flash calculations, dynamic simulation, LP/NLP/MILP/MINLP process optimization, pinch analysis, real-time optimization, soft sensors and process fault detection, HAZOP and LOPA process-safety analysis, process intensification, plantwide control, and front-end engineering design. No co-domain is assigned: the machine-learning subset is ML applied to chemical processes rather than a contribution to machine-learning research.

## Evaluation

- Each response is scored by five independent AI judges against a seven-element rubric.
- The composite score is `Overall = 0.15 x ROUGE-1 + 0.15 x ROUGE-L + 0.20 x Cosine + 0.50 x Element%`, with grade bands Good (>= 0.50), Fair (0.35–0.49), and Poor (< 0.35).
- Human expert validation is run alongside the automated scoring and released as `Human_Validation_Final.xlsx`.
- Rubric element coverage is scored on a 0–7 scale, and model differences are tested with the Friedman test, reported as significant at χ²(4) = 491.4, p < 0.001.
- **Reported.** Five models were evaluated: DeepSeek-V3 (`deepseek-chat`), Claude Sonnet 4 (`claude-sonnet-4-20250514`), Gemini 2.5 Flash (`gemini-2.5-flash`), GPT-4o (`gpt-4o-2024-08-06`), and Llama 3.3 70B (`llama-3.3-70b-versatile`, via Groq). Element coverage ranged from 78.1% for DeepSeek down to 60.8% for Llama. Domain difficulty followed a consistent DES > ML > OPT > MOD ordering across models. Three domain experts re-graded answers to validate the judge ensemble: AI–human agreement was Spearman rs = 0.416 (p < 0.001) with ICC = 0.793, and the experts' re-grading exposed a systematic AI leniency bias of +0.85 points on the 0–7 scale. Model rankings were stable across alternative scoring schemes (rs = 1.000), though the paper notes the ordering of middle-tier models was less stable than the broad performance tiering.

## Typical Duration

N/A — single-turn, zero-shot question answering with no agent trajectory; the benchmark reports no per-question wall-clock or token budget.

## Main Contribution

The authors present PSE-Bench as the first benchmark for evaluating large language models across process systems engineering domains, and pair it with a multi-judge evaluation framework whose five-judge ensemble is meant to reduce the systematic bias of a single AI evaluator. The reported conclusion is that LLMs assist with procedural PSE tasks but require expert verification on modeling and optimization.

## Key Design Ideas

- Four PSE domains held at an equal 50 questions each, so domain-level score differences are not confounded by sample size.
- Open-ended questions with released ground truths and per-question rubrics, rather than multiple choice.
- Judge ensembling: five independent AI judges per response instead of a single LLM judge.
- A composite metric that mixes lexical overlap (ROUGE-1, ROUGE-L), embedding similarity, and rubric element coverage, with element coverage carrying half the weight.
- A human expert validation layer used to check the automated judges rather than to replace them, with the resulting leniency offset reported as an explicit calibration constant instead of left implicit.
- Non-parametric significance testing (Friedman) plus a sensitivity analysis over alternative scoring schemes, establishing that the reported ranking is not an artifact of the chosen weighting.
- Full release of questions, ground truths, raw model responses, per-judge evaluations, summary statistics, and human-validation data under an MIT license.

## Strengths

- The evaluation artifacts are released end to end — question set, ground truths, rubrics, raw responses, per-judge scores, and human-validation data — so the reported numbers can be recomputed rather than taken on trust.
- Judge-ensembling plus an explicit human-agreement statistic addresses the single-LLM-judge reliability problem directly instead of assuming it away.
- Robustness of the model ranking is checked against alternative scoring schemes (rs = 1.000), separating the ranking claim from the specific weighting choice.
- Domain coverage reaches genuinely process-engineering material — HAZOP, LOPA, pinch analysis, plantwide control, FEED — rather than the chemistry knowledge that dominates most chemistry-adjacent LLM benchmarks.

## Limitations

- Single-turn, zero-shot, tool-free question answering: no simulator, no code execution, and no multi-step trajectory, so the benchmark measures consultation-style knowledge rather than agentic process-engineering capability.
- The composite score gives 30% of its weight to ROUGE overlap against a reference answer, which rewards surface similarity to the ground-truth phrasing.
- Reported AI–human agreement of rs = 0.416 is moderate, which bounds how much confidence the automated scores can carry on their own; the paper states the benchmark separates broad performance tiers more reliably than it separates individual middle-tier models.
- The AI judges are systematically lenient by +0.85 points on the 0–7 scale, so absolute scores overstate model competence unless that offset is applied.
- Repository note: at 200 questions across four domains, each domain rests on 50 items, so per-domain conclusions are drawn from a small sample.
- Repository note: the citation block in the official repository names a different journal and marks the work "Under review," while the published article of record appears in Chemical Engineering Journal Advances, Volume 27 (2026), article 101375.

## Related Works

- [CeProBench](./ceprobench.md) — the other chemical-process-engineering benchmark here, but built as an executable multi-task environment (knowledge graphs, PFD parsing, Aspen Plus optimization) rather than open-ended QA.
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — also scores LLMs on chemical-engineering problems, but with human expert graders instead of an AI judge ensemble.
- [Autonomous Action Execution (AAE) Framework](./aae-framework.md) — also targets LLM reliability in chemical process settings, but through deterministic validation of proposed control actions rather than answer grading.
