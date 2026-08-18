# Apodex Discovery (2026)

> **English** | [简体中文](../zh/works/apodex-discovery.md)

## Overview

Apodex Discovery is a set of executable "reality-based" environments and an accompanying process-scoring rubric for evaluating AI systems on real-world discovery problems. Twenty problems were selected from a two-month survey of 561 industries, each realised as a stateful environment with tools, data and a hidden verifier, and solver trajectories are scored on six process dimensions blind to the outcome.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.11341>
- **Project:** <https://discovery.apodex.com>
- **Venue:** arXiv preprint (August 2026); 85 pages, 9 figures, 38 tables.

## Summary

The paper's framing analogy is the Apollo program: frontier models can solve difficult problems once the problem, the tools and the success criteria are specified, so the bottleneck is the specification rather than the model. Apodex accordingly contributes three things. A problem-scouting process surveyed 561 industries to identify problems that are simultaneously technically tractable, valuable, and commercially accessible, narrowing 423 candidates to an initial release of 20. An environment abstraction then turns each problem into a stateful interactive substrate — tools, data, computational resources and experimental interfaces — that returns fresh observations in response to solver actions, with hidden ground truth structurally prevented from reaching the solver. Finally, a process rubric scores how a solver worked rather than only what it produced, evaluated blind to the outcome and with the solver's identity withheld. The authors report results on adeno-associated virus capsid design and on drug repurposing, in both cases comparing against an external reference rather than against another agent.

## Tasks

**20 problems** in the initial release, selected from **423 candidates** identified by a **ten-person team over two months across 561 industries**, assessed on three dimensions: technical fit (reasoning depth, verifiability, executability), value (a landmark scientific result or a large market), and commercial access (scalability beyond a single customer). The problems span **ten areas**: Bioinformatics & Genomic Medicine; Foundation Models for Scientific Reasoning; Scientific HPC Code Generation & Optimization; Healthcare IT & Digital Health; Weather-Driven Commodity & Energy Forecasting; Structural & Civil Engineering Services; Chip Design & Verification (EDA); Market Data & Financial Indices; Materials Discovery, Design & Qualification; and Industrial Automation & Control.

Each problem is realised as a runnable environment carrying data, budgets and a hidden verifier, with a fixed episode interface that allows attribution to specific solver components.

## Domains

**Biology** and **Medicine & Health** are assigned on the strength of the two problems reported quantitatively: adeno-associated virus capsid design (viability, tropism, structure prediction and generative design) and drug repurposing and reformulation.

`TODO(reference)` — the release names ten areas that would also touch Materials Science, Civil & Structural Engineering, Electrical Engineering, Energy Systems and Computer Science, but the paper does not report how many of the 20 problems fall in each area, and results are reported for only two. Because a multi-field release earns a domain on this repository's domain axis only when the slice is identifiable and sized, the remaining areas are not assigned.

## Evaluation

Trajectories are scored on six process dimensions, referred to in the abstract as **HDS6** and in the body by the mnemonic **TRACES**: **Tools** (selecting, invoking and correctly interpreting external tools), **Repair** (responding to verification feedback or observed failure, correcting the underlying error, and confirming the fix), **Alternatives** (making competing hypotheses explicit and adjudicating among them as evidence accumulates), **Coherence** (maintaining state, constraints and logical consistency over an extended horizon), **Evidence** (grounding claims in observations, tool outputs, data, experiments or references), and **Scope** (identifying the conditions under which a conclusion holds and the boundaries beyond which it should not apply).

Two scoring methods are used. A subrubric method scores **25 subcapabilities (3–5 per dimension)** on ordinal bands of **0/1/2**. A load-bearing-step method builds a trajectory dependency graph, identifies critical steps, and re-solves each independently for a continuous gap score. Both run as **blind process verification** — outcome unknown, solver identity withheld — and an integrity gate detects phantom tool calls or fabricated results.

Process and outcome scores are reported to agree substantially but not fully: **Spearman ρ = +0.51 pooled**, ranging **+0.24 to +0.65** by environment.

Reported outcomes: on capsid design, **Apodex surpassed the task-level published state of the art by 7% across all four tasks** (viability prediction, tropism prediction, structure prediction, generative design). On drug repurposing, adding a task-specific biomedical environment improved the mean normalized prediction score of **GPT-5.5 by 2.5 points and GPT-5.6-sol by 7.6 points** over the same closed-book backbone.

## Typical Duration

Environments carry explicit budgets as part of the episode interface, but the paper does not state their values. `TODO(reference)` — per-problem time, token or compute budgets are not reported.

## Main Contribution

An environment abstraction that makes real-world discovery problems executable and verifiable — with hidden ground truth structurally isolated from the solver — paired with a process rubric scored blind to the outcome, and the accompanying measurement that process and outcome judgments correlate only moderately (ρ = +0.51), which is the paper's argument for scoring both.

## Key Design Ideas

- The isolation principle is structural rather than procedural: hidden ground truth is prevented from reaching the solver by the environment's construction, not by asking the solver not to look.
- Process verification is blind in two ways at once — the verifier does not know the outcome and does not know which solver produced the trajectory — so process credit cannot be back-inferred from success.
- Two independent scoring methods are applied to the same trajectories: ordinal subrubric bands and a load-bearing-step method that re-solves critical steps in isolation for a continuous score.
- An integrity gate specifically targets phantom tool calls and fabricated results, treating trajectory dishonesty as a distinct failure mode rather than as low quality.
- The problem-scouting stage screens on commercial access as well as scientific merit, which is unusual for a benchmark and is what produces the industrial breadth of the ten areas.
- Reporting the process–outcome correlation is itself a design choice: at ρ = +0.51 the two are related enough to cross-validate and distinct enough that neither substitutes for the other.

## Strengths

- Both reported results are anchored to references outside the system — published state of the art for capsid design, and the same backbone without the environment for drug repurposing — rather than to another agent or to a self-assessment.
- The drug-repurposing comparison is a clean ablation: same model, same question, environment added or removed, so the measured gain is attributable to the environment.
- Blind, identity-withheld process verification is a stronger protocol than the outcome-aware process scoring common in agent evaluation.
- Environments are executable and stateful with hidden verifiers, so tasks are not static question sets.
- The selection funnel is documented (561 industries → 423 candidates → 20 problems) with stated criteria, so the release's composition is auditable.
- Reporting that process and outcome scores correlate only moderately is a finding that complicates the paper's own scoring story, and it is reported with per-environment range.

## Limitations

- Quantitative results cover two of the twenty problems. The remaining eighteen environments are described but not, in this paper, accompanied by reported agent performance.
- Per-area problem counts are not given, which prevents assigning most of the ten named areas on the domain axis (recorded above as `TODO(reference)`).
- The set of evaluated models is not enumerated exhaustively; GPT-5.5 and GPT-5.6-sol are named, with unnamed agentic procedures used for process verification.
- The metric is called HDS6 in the abstract and TRACES in the body, and the paper does not reconcile the two names.
- Per-problem budgets are not reported, so the resource conditions under which the reported gains were obtained are not reproducible from the paper.
- Repository note: access is via a project website (discovery.apodex.com) associated with a commercial entity rather than an open code release, and the paper's license line refers only to the arXiv posting. Whether the environments are freely obtainable is not established here.
- Repository note: the 7% capsid figure is described as surpassing the task-level published state of the art across four tasks; the paper as summarised does not give the four per-task baseline values, so the aggregate cannot be decomposed.

## Related Works

- [LAB-Bench](./lab-bench.md) — Biology research capability with expert baselines, using static question formats rather than executable environments with hidden verifiers.
- [BixBench](./bixbench.md) — Exploratory computational-biology analysis in a containerized environment, scored on open-ended answers rather than on process dimensions.
- [AutoResearchEval](./autoresearcheval.md) — Also scores the research process rather than only outcomes, via a failure taxonomy over annotated trajectories instead of a blind rubric.
- [ScienceAgentBench](./scienceagentbench.md) — Data-driven scientific tasks validated by domain experts, complementary on the outcome-verification side.
- [Beyond Final Scores](./beyond-final-scores.md) — Process measurement for long-horizon agent runs computed deterministically from execution signals rather than by blind rubric judging.
