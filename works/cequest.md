# CEQuest (2025)

> **English** | [简体中文](../zh/works/cequest.md)

## Overview

CEQuest is a 164-question benchmark on construction drawing interpretation and construction estimation, written by domain experts from construction estimating textbooks and drawing-interpretation guides, and used to compare five LLMs on accuracy, evaluation time, and model size.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2508.16081>
- **Code:** <https://github.com/mlsysx/CEQuest>

## Summary

The paper argues that general-purpose LLM benchmarks such as MMLU and HellaSwag do not capture the reasoning required in construction, and that existing construction datasets such as FloorPlanCAD target visual symbol recognition rather than the textual reasoning and estimation that construction professionals actually perform. CEQuest is presented as a pilot benchmark filling that gap: a curated question set covering the progression from foundational drawing literacy through spatial cross-referencing to quantity takeoff and cost estimation. Five LLMs — four open-weight models served locally through Ollama plus GPT-4.1 through the OpenAI API — are evaluated on it, with each run repeated five times and reported as mean ± standard deviation. The authors report that no model exceeds 80% accuracy and diagnose two recurring failure modes: inability to hold the required answer format, and estimation answers that are numerically plausible but violate professional practice.

## Tasks

164 questions in total, all collected and designed by domain experts using reference materials from construction estimating textbooks, drawing interpretation guides, and real-world instructional practices in construction education. Two question formats are used: 101 multiple-choice questions (62%), each offering three to six labelled answer options, and 63 TRUE/FALSE questions (38%). The questions are classified into five subject areas aligned with the progressive learning stages of construction drawing interpretation and estimation: **General Construction Knowledge** (broad conceptual understanding of construction processes); **Drawing Element Identification** (scales, labels, notes, legends, materials, and building elements such as walls and doors); **Drawing Organization and View Types** (plan, section and detail views, projections, drawing layouts); **Spatial Reasoning and Cross-referencing** (spatial relationships of building elements within a view, and connecting information across multiple drawings, e.g. matching a wall in a plan view to its section detail); and **Quantity Takeoff and Estimating** (interpreting dimensional data to compute counts, linear or area measurements and perform cost estimation). Reported dataset statistics: 3.59 choices per question on average (maximum 6), 1.69 sentences per question (maximum 3), 14.29 tokens per question (maximum 67), and 1.97 tokens per choice (maximum 8). The dataset is stored as structured JSON, each entry carrying a problem ID, question text, correct answer, and — for multiple-choice items — the option list. The paper does not report the per-subject-area question counts numerically; they are shown only as a figure. `TODO(reference)` for the per-area breakdown.

## Domains

Civil & Structural Engineering. The evaluated objective is construction engineering work on building projects: reading and cross-referencing construction drawings, identifying drawing elements and view types, and performing quantity takeoff and cost estimation from dimensional data. This falls under the domain's construction engineering, planning, scheduling and quantity/cost estimation scope. The worked failure case in the paper is a concrete-slab volume computation (5.33 cubic yards) where the models pick the nearest integer rather than rounding up as professional estimating practice requires — an estimating-practice judgement, not document comprehension for its own sake. The authors are from Florida International University and the University of Florida. No structural analysis, member design, or code-compliance checking is evaluated, so no additional co-domain is assigned.

## Evaluation

Single-turn question answering scored by exact answer match. The authors implement evaluation functions integrated with the OpenAI API that query the model, parse its output, and compute the metrics. Three metrics are reported: **accuracy** (percentage of correctly answered questions), **execution/evaluation time** (total wall-clock time for a model to complete the full question set), and **model size** (storage size or parameter count). Prompting is held constant across models with a fixed instruction — for multiple-choice items, "Please answer with only the letter of the correct option (A, B, C, D, E, or F)." Every experiment is repeated five times and reported as mean ± standard deviation. The evaluated models and results are: Gemma3:4b (3.3 GB) 61.83 ± 0.30% in 11.04 ± 0.73 s; Phi4:14b (9.1 GB) 64.02 ± 0.55% in 70.00 ± 4.06 s; LLaVA:34b (20 GB) 62.56 ± 1.06% in 29.24 ± 4.36 s; Llama 3.3:70b (43 GB) 65.37 ± 0.60% in 175.00 ± 2.52 s; and GPT-4.1 75.37 ± 1.13% in 86.26 ± 5.21 s (API call duration; model size not publicly available). Open-weight models are served locally through Ollama on a machine with an AMD Ryzen Threadripper PRO 7965WX CPU, 256 GB memory, and two NVIDIA RTX 3090 GPUs. The benchmark framework is described as extensible to new models, metrics, and construction data types.

## Typical Duration

Single-turn question answering with no multi-step trajectory. The reported per-model wall-clock time to complete the entire 164-question set ranges from 11.04 s (Gemma3:4b) to 175.00 s (Llama 3.3:70b); GPT-4.1 takes 86.26 s of API time. No per-task token budget is reported.

## Main Contribution

Three contributions in the authors' framing: the development and public release of CEQuest as a benchmark for construction drawing interpretation and estimation question answering; a comprehensive empirical evaluation of five diverse LLMs on it along accuracy, execution time, and model size; and actionable insights into current LLM capabilities and limitations in construction, motivating construction-specialized models.

## Key Design Ideas

- Subject areas follow the progressive learning stages of construction drawing interpretation and estimation, so the set spans foundational drawing literacy through to quantity takeoff rather than testing a single competence.
- Questions are authored by domain experts from construction estimating textbooks and drawing-interpretation guides rather than scraped, and both multiple-choice and TRUE/FALSE formats are used.
- Evaluation reports evaluation time and model size alongside accuracy, so the accuracy/compute/size trade-off is visible rather than accuracy alone.
- All experiments are repeated five times with mean ± standard deviation, so run-to-run variance is reported rather than a single number.
- Prompting is fixed and identical across models, and the harness is designed to be extended with new models, metrics, and construction data types.

## Strengths

- Expert-authored rather than generated: every item was collected and designed by domain experts from construction estimating references and instructional practice.
- Reports a genuine multi-model comparison spanning four open-weight models of very different sizes plus a proprietary model, under identical prompting.
- Repeated runs with reported standard deviations, and a compute/size axis alongside accuracy — unusual for a small domain QA set.
- The error analysis is specific and domain-grounded, distinguishing format-following failures from failures of estimating judgement (the concrete-quantity rounding case).
- Dataset and evaluation code are released under an open repository.

## Limitations

- The paper describes CEQuest explicitly as a pilot study; at 164 items across five subject areas, per-area sample sizes are small and per-area results are not reported numerically.
- All items are multiple-choice or TRUE/FALSE, so the benchmark measures recognition of a correct option rather than production of an estimate; a model can score without carrying out the takeoff.
- No agent, tool use, or multi-step trajectory is evaluated — this is single-turn question answering against a static answer key.
- The authors themselves note that models frequently deviate from the required answer format, which conflates format compliance with domain knowledge in the accuracy metric.
- Future work listed by the authors — dataset expansion, fine-tuning, retrieval augmentation, and multi-modal learning — indicates the current version does not yet exercise multimodal drawing input.
- Repository note: despite the framing around "construction drawing interpretation", the released dataset consists of question text and answer options in JSON, and the reported per-question length (14.29 tokens on average) indicates short textual items; no drawing images are described as part of the task input, even though one evaluated model (LLaVA) is a vision-language model.
- Repository note: the paper carries an ACM template with placeholder venue and DOI fields, so no peer-reviewed venue could be verified.

## Related Works

- [DrafterBench](./drafterbench.md) — the other civil-engineering benchmark built on construction documents, but scoring produced drawing revisions rather than answers about them.
- [AECBench](./aecbench.md) — a much larger expert-authored knowledge benchmark over the same architecture/engineering/construction field, with open-ended rubric-judged answers.
- [AEC-Bench](./aec-bench.md) — agentic tasks over real construction document sets, the executable counterpart to CEQuest's static question answering.
- [PE Civil Bench](./pe-civil-bench.md) — licensure-style civil engineering problems, similarly built from professional reference material.
- [Civil-Eval](./civil-eval.md) — an examination-derived civil engineering knowledge benchmark with a comparable single-turn scoring design.
