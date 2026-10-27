# PhysClosureBench (2026)

> **English** | [简体中文](../zh/works/physclosurebench.md)

> **First appeared:** 2026-10-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.21767)

## Overview

PhysClosureBench separates how much correct physics an agent produces from whether its investigation answers the question it was given. Each task states a research goal from strong-field, attosecond, or neighbouring physics and leaves the investigation to the agent. A 20-criterion Atomic Score credits local steps, such as a correct setup, the required observables, and a supported mechanism. A separate Research Closure level (RC0–RC4) asks whether the indispensable evidence and scope conditions for a complete answer are all in place. An attempt can therefore score 9/10 and still not reach closure.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** [From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research](https://arxiv.org/abs/2610.21767), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.21767v1>
- **Code:** <https://github.com/uncertainty2019/PhysClosureBench> (MIT-licensed runner and one example case, Case 30; the README points to the Hugging Face dataset `Tauben/PhysClosureBench` for the full 50 cases)
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

A task gives the scientific goal, physical setting, key parameters, necessary constraints, and a CPU and wall-time budget. It prescribes no workflow and no validation sequence. The agent works alone in a network-disabled container, writes and runs its own numerical code, and submits a report with derivations, execution history, and the artifacts behind each claim. A GPT-5.6-Sol grader applies the case rubric in stages. Atomic criteria and closure requirements are graded separately, so RC is not a threshold on the Atomic Score. Across 1,050 attempts, 83 of the 229 that score at least 8/10 (36.2%) fall short of RC4.

## Tasks

50 goal-specified research tasks, each derived from a published study in journals such as Physical Review Letters and Physical Review A. By area: strong-field atomic, molecular, and attosecond physics 24; solid-state and condensed-matter strong-field physics 12; quantum optics and quantum light–matter 8; strong-field QED and relativistic dynamics 4; matter-wave and Kapitza–Dirac 2. One domain expert in ultrafast and strong-field physics designed and supervised a semi-automated construction pipeline; other experts reviewed task validity and grading criteria. The source results behind every task were reproduced by hand before inclusion, and those reproductions set the resource limits. Example (Case 30, after Bray et al. 2018): how does post-release scattering change the attoclock angular offset as laser intensity and screening length vary, for Coulomb and screened potentials with the same binding energy? The instructions forbid network search, external agents, and target-paper materials.

## Domains

Physics: strong-field and attosecond atomic and molecular physics, strong-field condensed-matter physics, quantum optics, strong-field QED and relativistic quantum dynamics, and matter-wave diffraction. Every task is a computational investigation; agents generate their own evidence in code, and the paper describes no experimental data as task input.

## Evaluation

- **Atomic Score (0–10):** 20 binary half-point criteria per case across Formulation (F), Output (O), Identification (I), Mechanism (M), and Validation/Scope (V). Across the 1,000 atoms, Mechanism takes the largest share (369 atoms, 36.9% of score weight). Criteria that do not apply to an attempt's route are marked N/A and keep their 0.5 points.
- **Research Closure:** RC4 complete closure; RC3 main conclusion supported with material validation or scope gaps; RC2 core evidence present but the central mechanism or another key requirement unresolved; RC1 an essential output or branch missing; RC0 central object invalid or absent. RC is set by which indispensable requirements remain unmet.
- **Grading:** GPT-5.6-Sol (high) gives an independent first-pass grade, then a targeted review; adjudication runs only when a residual disagreement could change the score, RC, or validity. Five physics-trained experts reviewed 200 selected criterion-level decisions (192 effective) and agreed with the automated grader in 81.8%; on criteria tied to closure, agreement was 75.9% (60 of 79).
- **Models:** Claude-Opus-5, GPT-5.6-Sol, and Qwen-3.8-Max at xhigh effort; Kimi-K3, DeepSeek-V4.1-Flash, GLM-5.3-Flash, and Gemini-3.1-Pro at high effort. Each runs in OpenCode 1.18.17, three independent runs per task (1,050 attempts in all).
- **Results:** mean Atomic Score 6.29 (Claude-Opus-5), 5.83 (GPT-5.6-Sol), 5.17 (Kimi-K3), 4.50 or below for the rest, down to 2.85 (Gemini-3.1-Pro). RC4 rates are 32.7%, 22.7%, and 19.3% for the top three and 0.7% for Gemini-3.1-Pro. DeepSeek-V4.1-Flash reaches RC4 in 10.7% of attempts, but 50.0% of its attempts sit at RC0.
- **Where closure fails:** high-scoring attempts below RC4 leave 16.0% of Identification and 20.8% of Mechanism criteria unmet, against 2.1% and 3.0% for RC4 attempts. Across the benchmark, scope justification is satisfied in 86.9% of applicable cases, required validation in 59.6%, and risk-linked validation in 47.8%.
- **Repeatability:** Claude-Opus-5 reaches RC4 at least once on 50.0% of tasks but in all three runs on 18.0%; GPT-5.6-Sol 40.0% and 10.0%; Kimi-K3 40.0% and 4.0%.

## Typical Duration

Per-case limits range from 8 to 96 CPU cores and from 30 to 720 minutes of wall time. Runs that hit the limit are graded on what exists, with no extra penalty. Token and dollar costs are not reported.

## Main Contribution

Scores research closure as its own outcome, set by task-specific indispensable requirements. Reporting it alongside a fine-grained Atomic Score shows how often agents complete most local steps without answering the research question.

## Key Design Ideas

- Fix the question and the bounded setting, not the route: any valid evidence path can reach RC4.
- Use hand reproduction of every source result both as a feasibility check and to calibrate CPU and wall-time budgets.
- Report RC4 in at least one run and RC4 in all three runs separately, so that the ability to reach closure is distinguished from reaching it reliably.

## Strengths

- The joint distribution of Atomic Score and RC over all 1,050 attempts shows directly where the two measures diverge.
- Human checks cover all 50 cases and report agreement separately for closure-linked criteria.
- The Case 30 comparison traces three runs on one problem to RC4, RC3, and RC2. It separates misinterpreted trends (Gemini-3.1-Pro) from a supported mechanism with an unresolved applicability limit (GPT-5.6-Sol).

## Limitations

- Coverage is concentrated: 24 of 50 tasks are strong-field atomic, molecular, or attosecond physics.
- Human agreement with the grader is 81.8% overall and 75.9% on closure-linked criteria. The paper states that the reviewed criteria were chosen for scientific consequence, not sampled uniformly from all atoms.
- Repository note: one grader model, GPT-5.6-Sol, scores every attempt, and it is also one of the evaluated models.
- Repository note: tasks derive from published studies. Network search and target-paper materials are prohibited at run time, but the paper describes no further control for exposure during pretraining.
- Repository note: N/A criteria keep their 0.5 points, so the Atomic Score credits inapplicable criteria; the paper states this does not mean the work was done.

## Related Works

- [PRL-Bench](./prl-bench.md) — Long-horizon physics research subtasks with rubric-based assessment; compared in the paper's Table 1.
- [CritPt](./critpt.md) — Research-level physics challenges with machine-verifiable answers rather than open investigations.
- [PaperBench](./paperbench.md) — Rubric-graded research reproduction; the paper rates its closure assessment as absent.
