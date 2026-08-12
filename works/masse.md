# MASSE (2025)

> **English** | [简体中文](../zh/works/masse.md)

## Overview

MASSE is a training-free multi-agent LLM system for structural engineering that ships alongside a released
100-problem structural engineering dataset with expert-verified ground truth and four rubric-scored
benchmarks (SAAB, SDAB, LAB, MASEB) covering structural analysis, structural design, load transformation,
and end-to-end workflow execution.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://arxiv.org/abs/2510.11004
- **Code:** https://github.com/DelosLiang/masse

## Summary

MASSE decomposes a real consulting-firm structural engineering workflow into an Analyst Team, an Engineer
Team, and a Management Team of LLM agents that pass structured JSON between roles, retrieve seismic
parameters from building-code documents via RAG, build and solve OpenSeesPy finite-element models, and
issue capacity-verification verdicts. To measure the system, the authors construct a dataset of one hundred
structural engineering problems of varying difficulty, each paired with an expert-validated ground-truth
solution, and define four benchmarks with explicit point rubrics that an LLM judge applies to the complete
analysis log. The paper reports a model comparison across four LLM backends, a cost/runtime trade-off
analysis, an ablation on agent memory and structured I/O, and a human study against practising engineers.

## Tasks

One hundred distinct problem instances built around a racking-system design scenario, each containing a
natural-language problem description, intermediate reasoning steps, and final results used as evaluation
criteria. The data is reorganized from production records of real racking-system projects in British
Columbia, Canada, anonymized for release; ground-truth solutions are expert-derived. Component tasks span
parameter retrieval, seismic-load transformation, structural modelling, structural analysis, section-property
determination, section-capacity calculation, and structural-adequacy verification. Each problem was run over
ten independent trials, with one hundred traces collected for the overall system assessment.

## Domains

Civil & Structural Engineering. The evaluated objective is a structural engineering decision throughout:
retrieving site-specific seismic parameters (Sa(0.2), Sa(0.5), Sa(1.0), Sa(2.0), PGA, PGV) from building-code
documents, converting them to seismic floor loads, assembling an OpenSeesPy beam-column and brace model of a
racking structure, running the finite-element analysis, computing member capacities, and returning a
pass/fail structural-adequacy verdict. This is earthquake *engineering* — the design and verification of a
load-bearing structure — rather than seismic hazard science. No co-domain is claimed: the finite-element and
RAG tooling is a means to the structural verdict, not an evaluated objective in its own right.

## Evaluation

GPT-5 acts as an LLM judge, reading one complete MASSE analysis log against the expert-verified ground-truth
solution and emitting a JSON object with four 0–100 scores plus total token usage and total time. Each
benchmark carries an explicit component rubric: SAAB = Model Geometry Accuracy (30 pts) + Integration of
Section and Load Data (20) + OpenSees Analysis Execution (30) + Result Retrieval Accuracy (20);
SDAB = Extraction Accuracy (30) + Capacity Computation (30) + Data Storage and Memory Update (20) + Transfer
and Availability (20); LAB = Load Extraction (25) + Adjustment and Normalization (25) + RAG Seismic
Retrieval (25) + Load Calculation (25); MASEB = Pipeline Completion (30) + Consistency Across Agents (30) +
Final Result Accuracy (20) + Efficiency and Robustness (20). Reported results: o4-mini leads on SAAB (96.6),
SDAB (91.4) and MASEB (94.7); GPT-4o leads on LAB (98.1); Claude 3.5 Sonnet averages 89.2 and GPT-3.5-turbo
73.6. An ablation shows agent memory plus JSON-structured I/O lifting the average from 61.8 to 88.5.

## Typical Duration

Runtime scales with the maximum number of agent-to-agent communication rounds: roughly 20 seconds at one
round rising to nearly 70 seconds at four rounds, measured on ten representative MASEB problems repeated ten
times each, with the system score rising from below 40 to nearly 90 over the same range. In the human study,
MASSE with a GPT-4o backend completed the standardized racking-system design task in approximately two
minutes. MASEB additionally folds token cost and wall-clock runtime into its Efficiency and Robustness
component.

## Main Contribution

The authors present MASSE as the first multi-agent system for structural engineering and as a proof of
concept that most real-world structural engineering workflows can be fully automated by a training-free
LLM-based multi-agent system, supported by a new dataset and case studies grounded in real-world problems
and by evaluation metrics aligned with the core agent roles.

## Key Design Ideas

- Agent roles mirror a consulting-firm hierarchy — Analyst Team (loading, seismic, dynamic, structural
  analysts), Engineer Team (design engineer, verification engineer), Management Team — so that a long-horizon
  workflow is partitioned into subtasks each tractable for a single agent.
- Benchmarks are defined per agent role (SAAB, SDAB, LAB) plus one holistic system benchmark (MASEB), so a
  failure can be localized to the analysis, design, or loading stage.
- MASEB deliberately mixes technical accuracy with system cost and runtime, making efficiency part of the
  score rather than a separate report.
- Seismic parameters are obtained by retrieval-augmented generation over building-code documents rather than
  from model memory, and the retrieved values are checked as part of LAB.
- All inter-agent communication is JSON-constrained and agent memory is shared, which the ablation identifies
  as the two components responsible for most of the performance.
- A controlled single-agent versus two-agent experiment on OpenSeesPy code generation reports the single-agent
  system failing all ten trials while the decomposed two-agent system executed stably across all cases.

## Strengths

- The 100-problem dataset derives from certified production records rather than synthetic constructions, and
  loading reports of this kind must legally be signed by a structural engineer in the jurisdictions cited.
- Scoring rubrics are published component by component with point weights, so the judge's decision surface is
  inspectable rather than an opaque holistic score.
- Cost, token usage, and runtime are reported alongside accuracy, and the accuracy–cost trade-off across
  backends is analysed explicitly.
- A human baseline is measured directly: 11 experienced structural engineers averaged 132 minutes on the same
  standardized task.
- Code and dataset are released publicly.

## Limitations

- All one hundred problems instantiate a single scenario family — racking-system design — so the benchmarks
  measure breadth of difficulty within one structural typology rather than breadth of structural engineering.
- Scoring depends on a single LLM judge (GPT-5) reading analysis logs; no inter-judge agreement or
  human-versus-judge calibration is reported.
- The benchmarks are defined against MASSE's own agent roles and log format, so applying them to an
  externally built agent requires mapping onto the same role decomposition.
- Repository note: the model comparison covers four backends available in 2025 and evaluates them only as
  backends inside MASSE, so the scores measure the system-plus-model pair rather than the model alone.
- Repository note: the human study compares a fully automated pipeline against unassisted manual practice,
  which measures automation speed-up rather than the correctness margin between the two.

## Related Works

- [StructureClaw](./structureclaw.md) — the other structural-engineering agent benchmark with executable
  solver verification, scoring against frozen reference solver responses rather than an LLM judge.
- [AutoBM / BMEval](./autobm.md) — also evaluates OpenSeesPy structural-model generation from natural
  language, but scores executability and modal-period consistency instead of rubric-graded workflow logs.
- [FEABench](./feabench.md) — finite-element agent evaluation driving COMSOL through its API, the same
  simulation-mediated pattern in a non-civil setting.
- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction benchmark whose taxonomy includes
  a civil engineering field.
