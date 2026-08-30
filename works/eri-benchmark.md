# ERI Benchmark (2026)

> **English** | [简体中文](../zh/works/eri-benchmark.md)

> **First appeared:** 2026-02-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2603.02239)

## Overview

The Engineering Reasoning and Instruction (ERI) benchmark is a taxonomy-driven instruction dataset of 57,750 instruction–response records built as a controlled cross-product of nine engineering fields (55 subdomains, chemical engineering among them), seven task intents, and three difficulty tiers, released with validation scripts and an evaluation harness for scoring LLMs and agents.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2603.02239
- **Code:** https://github.com/mznaser-clemson/ERI-Benchmark
- **Dataset:** https://huggingface.co/datasets/mznaser/ERI-Benchmark

## Summary

ERI is designed around the argument that a general-purpose benchmark cannot diagnose engineering competence, because pooled prompts hide where failures concentrate. Coverage is therefore treated as a controlled combination of field, task intent, and difficulty tier: every (field, subdomain, intent, difficulty) cell receives a fixed number of samples so that no high-volume prompt class dominates the aggregate score. Records are generated synthetically under that taxonomy, schema-validated, deduplicated, and spot-verified, then scored by a mix of automatic checks and rubric-based judging. The authors run a seven-model baseline study and pair it with a validation protocol intended to bound the hallucination risk inherent in an LLM-generated reference set.

## Tasks

57,750 instruction–response records spanning nine engineering fields and 55 subdomains: civil, mechanical, electrical, chemical, environmental, materials, aerospace, industrial engineering, and fire science. Each field is crossed with seven intent types — definition (DEF), explanation (EXP), calculation (CALC), comparison (CMP), design/synthesis (DES), troubleshooting (TRB), and code/standard (CODE) — and three difficulty tiers (undergraduate, graduate, professional), giving 1,155 unique cells with 50 instruction–response pairs generated per cell. Construction is synthetic: a generator model (GPT-5 Mini) is seeded with the explicit (field, subdomain, intent, difficulty) tuple and constrained to emit strict JSON, returning five pairs per call with each seed queried ten times; records are stored as JSONL with `instruction`, `response`, `field`, `subdomain`, `type`, and `difficulty` metadata. Post-processing applies schema validation, exact deduplication on a hash of the lowercased instruction, an optional Sentence-BERT-style semantic deduplication step, and length-based filtering, followed by a verification pass in which an advanced model (GPT-5.1) rates a random 10% subset on a five-point quality scale. The paper's dataset-access snippet reports released splits of 45,415 train / 2,671 validation / 5,343 test records. Benchmark subsets are defined by filtering the held-out split on the metadata axes (for example a CALC-only subset for numeric and unit checks, TRB and CMP subsets for hypothesis management, DES and CODE subsets for feasibility and context sensitivity).

## Domains

Chemical Engineering is one of the nine explicitly enumerated fields, with six subdomains: mass and energy balances, chemical thermodynamics, reaction engineering, separation processes, process control, and transport phenomena — core chemical/process engineering subject matter, and results are reported per field so the chemical-engineering slice is separately scoreable. The benchmark is genuinely multi-field, so co-domains include Civil & Structural (statics, mechanics of materials, structural analysis, steel and concrete design, geotechnical, structural dynamics, construction management), Mechanical & Aerospace (thermodynamics, fluid mechanics, heat transfer, machine design, dynamics and vibrations, manufacturing, HVAC; plus aerodynamics, flight mechanics, propulsion, aerospace structures, orbital mechanics), Electrical (circuits, electronics, signals and systems, power systems, electromagnetics, control systems), Materials Science (structure of materials, mechanical properties, phase diagrams, failure analysis, polymers and composites, corrosion), and Environmental Science (water treatment, air quality, hydrology, waste management, environmental impact). Industrial engineering and fire science are two further covered fields.

## Evaluation

A three-stage protocol: response generation, multi-judge scoring, and metric aggregation. Each of the seven benchmark models was evaluated on a 10% subsample of the dataset, stratified across field, subdomain, intent type, and difficulty tier (over 5,000 scored items per model). The first scoring layer is automatic and operates on the output text: it flags empty outputs, refusal patterns, missing final answers where the intent requires one, and length/formatting anomalies, and emits a constraint-satisfaction flag when the instruction contains numeric bounds or feasibility conditions that parse into simple predicates. The second layer is rubric scoring of reasoning quality and verification behaviour (whether assumptions are stated and bounded, whether verification appropriate to the intent is performed, whether constraints are respected, whether unjustified premises are introduced), implemented as LLM-as-a-judge with a fixed prompt template and structured JSON output. Judging uses a panel of three models from three providers — Claude Haiku 4.5, GPT-4.1 Mini, and Mistral Small 3 — each returning a 1–5 score plus a brief justification; the final per-item score is the arithmetic mean across the three judges, with 115,962 judgments made in total. Inter-judge Spearman correlations range from 0.70 to 0.80 with within-one-point agreement above 85% for all judge pairs. Reported means: GPT-5 4.48 (σ = 0.49), Claude Sonnet 4 4.31 (0.66), DeepSeek V3.1 4.30 (0.68), Mistral 7B 3.81 (0.82), Llama 3.3 70B 3.75 (0.78), Qwen 2.5 7B 3.27 (0.92), Llama 3.1 8B 2.96 (0.85). Design (DES) items were the hardest intent for every model and definition (DEF) items the easiest; cross-field spread was modest (GPT-5 spanned 0.23 points across fields, Llama 3.1 8B 0.44 points), with industrial engineering scoring highest and aerospace engineering and fire science hardest. When human scoring is used, the paper recommends a small seed-stratified subset with at least two independent raters and a disagreement-resolution procedure.

## Typical Duration

N/A — items are single-turn instruction–response pairs with no interactive environment; the paper reports no per-item wall-clock, trajectory-length, or token-budget figures.

## Main Contribution

The authors present ERI as the first large-scale evaluation instrument designed to measure LLM capability across the breadth of engineering knowledge and reasoning, arguing that existing benchmarks either test general knowledge, target a single discipline, or use multiple-choice formats that cannot capture open-ended professional reasoning. Beyond the dataset itself, they present the convergent validation protocol — cross-provider triangulation at each pipeline stage, convergent-validity analysis through cross-model agreement, and hallucination bounding via frontier-inversion detection — as a replicable methodological template for LLM-generated evaluation datasets in domains where human-curated ground truth is expensive to obtain at scale.

## Key Design Ideas

- Coverage as a controlled cross-product of field × subdomain × intent × difficulty, with a fixed sample count per cell, so aggregate scores cannot be dominated by whichever prompt class is cheapest to generate.
- Intent types as a second conditioning axis that separates "knowing about" a domain from "doing" it, each with its own success criteria (for example CALC requires reported units, TRB requires discriminating checks between hypotheses, DES requires explicit constraint recognition).
- Difficulty tiers supplied as explicit conditioning attributes at generation time and encoded in record metadata, so tier-wise degradation can be traced per model.
- Two-layer scoring: deterministic automatic checks (refusals, missing final answers, machine-parsable constraint violations) beneath a rubric layer that is deferred to only when a constraint is not machine-checkable.
- Multi-provider judge panel with averaged scores, chosen so that systematic bias from any single provider is diluted; the paper reports per-judge offsets (Claude Haiku 4.5 strictest at −0.41 from the grand mean of 3.84, Mistral Small 3 most lenient at +0.29, GPT-4.1 Mini near-neutral at +0.12) and shows model rankings are stable across judges.
- Deliberate separation of generator, evaluated models, and judges across different providers to break the circularity of a single system generating, answering, and grading its own questions.
- Hallucination bounding by frontier-inversion detection: items where frontier models score at or below 3.0 are treated as candidate bad references (1.7% of items), and cases where smaller models outperform frontier models are treated as the strongest signal of a hallucinated reference (score inversion rate below 0.1%).

## Strengths

- The metadata schema makes every reported score traceable to a field, subdomain, intent, and tier, which supports slice-level failure attribution rather than a single aggregate number.
- Judging is triangulated across three providers with reported inter-judge agreement statistics, and the paper quantifies individual judge bias rather than assuming judge neutrality.
- The reference-quality problem inherent to synthetic benchmarks is addressed empirically: 68.8% of items had all three frontier models score at or above 4.0, cross-model standard deviations were low (mean σ = 0.74), and only 0.7% of items showed high disagreement (σ > 1.5).
- The release package includes taxonomy specifications, schema-validation scripts, hygiene utilities for deduplication and filtering, and an evaluation harness that reproduces the automatic checks and reporting structure, with a versioned reporting format for longitudinal comparison.
- The limitations section is explicit about what the benchmark cannot certify: it states ERI should not be used to claim compliance, safety certification, or readiness for autonomous control of high-stakes engineering decisions.

## Limitations

- Reference answers are LLM-generated and not human-verified; a human-verified "gold" calibration subset is listed as a roadmap item for ERI-V2 rather than shipped with V1.
- Records reflect the knowledge state of the generating model's training data at a fixed time, so code-related (CODE) and design-oriented (DES) items may reference superseded material, limiting the dataset's value as a reference for current professional practice.
- The authors note that prompt-based construction over-represents "clean" problem statements and under-represents messy real constraints, and that benchmark optimization can produce teaching-to-the-test dynamics.
- Coverage omits disciplines such as biomedical, nuclear, and software engineering beyond CODE-type items, and within included fields the subdomain list reflects salience at taxonomy-design time rather than principled sampling of professionally relevant topics.
- Repository note: chemical engineering accounts for 6 of the 55 subdomains, i.e. 126 of the 1,155 cells and, at the stated 50 records per cell, roughly 6,300 generated records — a substantive but minority slice of the benchmark, so ERI is a broad engineering benchmark with a chemical-engineering component rather than a chemical-engineering benchmark.
- Repository note: the chemical-engineering items are textbook-style instruction–response pairs on balances, thermodynamics, reaction engineering, separations, process control, and transport; no flowsheeting, simulator-in-the-loop, or plant-operations task is evaluated.
- Repository note: despite the framing as a dataset "for foundation models and agents", the V1 evaluation is single-turn text scoring — no tool calls, environment interaction, or trajectories are executed; a tool-trace extension for evaluating agentic pipelines is listed only as future work.
- Repository note: the released split sizes printed in the paper's access snippet (45,415 / 2,671 / 5,343) sum to 53,429, fewer than the 57,750 generated records, consistent with the described validation and deduplication filtering but not reconciled explicitly in the text. TODO(reference)
- Repository note: the paper simultaneously gives public GitHub and Hugging Face links and a "Data is available on request from the author" statement, so the exact public availability of the full release is ambiguous from the paper alone. TODO(reference)

## Related Works

- [CeProBench](./ceprobench.md) — chemical-process-development benchmark whose tasks are executable (PFD parsing/design, Aspen Plus parameter optimization) rather than textbook instruction–response items.
- [EEE-Bench](./eee-bench.md) — single-field engineering benchmark (electrical/electronics) with a comparable subdomain-coverage design.
- [MaScQA](./mascqa.md) — exam-derived engineering question-answering dataset used to probe LLM domain knowledge.
- [Frontier-Eng](./frontier-eng.md) — multi-field engineering benchmark that scores simulator-verified designs instead of rubric-judged text.
