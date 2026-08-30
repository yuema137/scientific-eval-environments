# MiraMind (2025)

> **English** | [简体中文](../zh/works/miramind.md)

> **First appeared:** 2025-12-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2512.09636)

## Overview

MiraMind is a benchmark for evaluating large language models on mental-health reasoning, scoring not only task outcomes but also the reliability of the explicit reasoning trajectories that connect limited, subjective evidence to clinical judgments.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2512.09636
- **Venue:** Preprint (arXiv, cs.CL)

## Summary

MiraMind frames mental-health reasoning as an evidence-constrained judgment problem: models must transform limited and ambiguous evidence into interpretations, decisions, or claims whose specificity, certainty, severity, and actionability remain warranted by that evidence. The benchmark unifies six task families across 13 datasets spanning appraisal, diagnosis, intervention, multi-step psychiatry question answering, abstraction, and verification. Beyond final-answer accuracy, it evaluates the reasoning trajectory connecting evidence to judgment along usability, logical structure, and informational contribution. Evaluating 20 LLMs surfaces a "restraint gap," in which the specificity or certainty of model judgments exceeds what the available evidence supports; the authors additionally train an 8B model, Mindora, targeting evidence-to-judgment transitions.

## Tasks

Six task families over 13 datasets (dataset names as reported in the paper):

- **Appraisal (cognitive-pattern reasoning):** identify cognitive-error patterns from brief personal statements — CognitiveReframing, PatternReframe, Therapist Q&A.
- **Diagnosis (mental-condition reasoning):** predict mental-health condition or severity labels from informal user narratives — DepSign, SWMH, T-SID.
- **Intervention (therapeutic-action reasoning):** select appropriate counseling strategies from client case summaries — PsyDTCorpusM, AnnoMIM.
- **Multi-step (psychiatry question answering):** MHQA, MedQAM, MedMCQAM, PubMedQAM.
- **Abstraction (evidence-based psychiatry summarization):** generate "Main Results" summaries from Cochrane psychiatric systematic-review abstracts — PSRS (newly curated).
- **Verification (mental-health misinformation detection):** binary classification of whether online mental-health claims are accurate or misleading — MentalMisinfo.

Reported sample counts include PSRS with 108 test samples (annotated by psychiatrists on a 0–2 rubric) and AnnoMIM with 133 test samples (real motivational-interviewing dialogues). Other per-dataset train/valid/test sizes are given in the paper's dataset table. TODO(reference) for the complete per-dataset size table.

## Domains

Mental health / psychiatry and clinical psychology — folding into Medicine & Health and Neuroscience & Cognitive Science. Evidence sources span informal user narratives (e.g., Reddit/Twitter posts), counseling dialogues, psychiatric board-style question answering, and Cochrane systematic-review abstracts.

## Evaluation

Task outcomes use per-family metrics: Micro-F1 for appraisal and diagnosis, Jaccard similarity for intervention (multi-label strategy selection), recall over expert-annotated scoring points for abstraction, and Macro-F1 for verification. TODO(reference) for the multi-step QA metric.

Reasoning trajectories are scored with an LLM-as-judge protocol along three dimensions: **usability** (terminology parsimony, step adequacy), **logical structure** (logical coherence, irrelevance rate, contradiction rate), and **informational contribution** (informativeness). The judge segments each trajectory into reasoning content units before scoring. The authors report a human-validation study in which 100 trajectories were independently annotated by two trained evaluators. TODO(reference) for the specific judge model.

## Typical Duration

TODO(reference) — the paper does not report a standardized per-task wall-clock time or token budget.

## Main Contribution

A unified benchmark that evaluates mental-health reasoning "beyond answer accuracy" by jointly assessing task outcomes and the reliability of explicit reasoning trajectories, and that exposes a shared "restraint gap" across LLMs where judgment specificity or certainty exceeds what the evidence supports.

## Key Design Ideas

- Casting mental-health reasoning as an evidence-constrained judgment problem where the warranted level of specificity, certainty, severity, and actionability is itself the object of evaluation.
- Separating outcome scoring from trajectory scoring, so a correct final answer does not mask an unreliable evidence-to-judgment path.
- A multi-dimensional trajectory rubric (usability, logical structure, informational contribution) applied to LLM-segmented reasoning units.
- Coverage across six functionally distinct task families (appraisal, diagnosis, intervention, multi-step QA, abstraction, verification) rather than a single clinical role.
- A demonstration model, Mindora (8B, based on Qwen3-8B), post-trained via hard-case supervision, structured trajectory rewriting, and a consistency-aware SFT–RL objective; reported to achieve the best average rank among evaluated models and to improve over its backbone across all six task families.

## Strengths

- Evaluates reasoning trajectories, not only final answers, giving a reliability signal that outcome accuracy alone would miss.
- Broad coverage: six task families and 13 datasets spanning multiple mental-health reasoning roles and evidence formats.
- Includes a human-annotation validation of the trajectory-judging protocol (100 trajectories, two annotators).
- Surfaces a cross-model "restraint gap" as a concrete, shared failure mode.

## Limitations

- Trajectory scoring relies on an LLM-as-judge, which inherits the biases and reliability limits of the judge model. TODO(reference) for the judge model identity and reported judge–human agreement.
- Repository note: the paper couples an evaluation benchmark (MiraMind) with a trained model (Mindora); the benchmark is the evaluation contribution, while Mindora is a training demonstration whose gains are reported on this benchmark's own metrics.
- Repository note: no public code or dataset-release URL was found in the paper text at the time of carding; several constituent datasets carry their own licenses and access conditions.

## Related Works

TODO(reference) — related mental-health / medical reasoning benchmarks and trajectory-evaluation works to be linked once carded.
