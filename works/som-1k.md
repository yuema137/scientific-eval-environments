# SoM-1K (2025)

> **English** | [简体中文](../zh/works/som-1k.md)

## Overview

SoM-1K is a multimodal benchmark of 1,065 annotated strength-of-materials (mechanics of materials) problems — each pairing a textual problem statement with a schematic diagram, an expert-written description of that diagram, and a full worked ground-truth solution — used to evaluate eight foundation models under three prompting strategies with expert manual grading.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.21079>
- **Project:** <https://som-1k.github.io/>
- **Dataset:** <https://huggingface.co/datasets/Crazyyyyman/SoM-1K>
- **Venue:** arXiv preprint (cs.CL), v1 September 2025, v2 August 2026

## Summary

Strength of materials sits at the base of civil, mechanical, aerospace and materials engineering curricula, and solving its problems requires reading a schematic — supports, member geometry, load positions and directions — at the same time as the text. The authors argue that this makes it a natural probe for multimodal engineering reasoning, and build a dataset in which the diagram is a first-class annotated component rather than an image dropped into a prompt. Alongside the raw schematic they introduce **Descriptions of Images (DoI)**: a rigorous expert-verified textual rendering of exactly what the diagram shows, containing no solution steps, so that the contribution of visual information can be isolated from the contribution of reasoning hints. Evaluating five LLMs and three VLMs, they find that the best configuration reaches only 56.6% accuracy, and that text-only models given DoI generally beat vision-language models given the actual diagram.

## Tasks

1,065 annotated problems, categorized by deformation mode into axial loading of bars (201, 18.87%), torsion of shafts (137, 12.86%), bending of beams (630, 59.15%), bending of frames (54, 5.07%), and integrated tasks (43, 4.04%); and by static indeterminacy into statically determinate/easy (917, 86.10%) and statically indeterminate/hard (148, 13.90%). Task content spans computation of internal forces, stresses, strains and deformations, diagram construction, and design-oriented optimizations. Problems are drawn from widely used university textbooks (Chinese and international editions, including Hibbeler and Gere & Goodno) and from advanced mechanics competitions obtained from official exam websites; integrated problems come from competitions and combine static analysis with vibration, impact, and rigid-body motion. Construction pipeline: textbooks scanned to PDF, schematics manually extracted as PNGs, problem statements and ground-truth solutions extracted by Doubao OCR and then manually reviewed and corrected, with diagram-based solution elements (such as internal-force diagrams) supplied manually by the annotation team. LaTeX equations were converted to natural-language descriptions using the DeepSeek-V3-0324 API because models handled LaTeX poorly in batch inference. Each problem has four standardized components: problem statement (PS), image (I), description of the image (DoI), and ground truth (GT). DoI itself is produced by first prompting the Doubao VLM for a description and then having the annotation team correct structure type, boundary conditions, geometry, and load direction. The annotation team comprised researchers and educators in structural engineering and mechanics of materials — one PhD candidate, two lecturers, and four teaching assistants.

## Domains

Civil & Structural Engineering: the benchmark's subject is strength of materials, which the repository's domain scope lists explicitly under structural analysis and structural modelling, and the dominant problem categories are the load-bearing members of structural analysis — beams (59.15%) and frames (5.07%) account for the majority of the dataset, with tasks covering internal forces, bending moments, deflections, and statically indeterminate systems. The paper is written out of civil engineering departments (Hunan University College of Civil Engineering; University of Miami Department of Civil & Architectural Engineering) and the annotators are described as structural engineering and mechanics-of-materials educators. Mechanical & Aerospace is a genuine co-domain through shared solid mechanics: the paper states that SoM is a core subject in civil, mechanical, aerospace and materials engineering curricula, and the torsion category (12.86%) is posed on shafts rather than civil structures. The problems are generic textbook members rather than named buildings or bridges, so the civil/structural claim rests on the subject matter and the member types, not on identified infrastructure.

## Evaluation

Three prompting strategies are defined: PS+I (statement plus diagram), PS+I+DoI (statement, diagram and description) and PS+DoI (statement and description, no image). VLMs are run under all three; LLMs, being text-only, are run under PS+DoI alone — giving 14 model–prompt settings in total (3 strategies × 3 VLMs plus PS+DoI × 5 LLMs). For each problem and setting, five independent responses are generated and reduced to a single answer by majority vote implemented through the DeepSeek-V3-0324 API. Grading is manual: the DoI annotation expert team examined every model response across all 1,065 problems in two stages — whether the reasoning followed a logically valid sequence of steps, and whether the final answer was correct — awarding 1 only when both criteria hold and 0 otherwise, with ambiguous cases resolved by discussion until consensus. The authors ran a pilot in which Qwen-plus was used as an automated judge on 200 sample problems and reached 83% agreement with expert judgment, but rejected LLM-as-judge for the full run in favour of human scoring, citing the dataset's manageable size and the need for reliable error analysis. Accuracy is the single reported metric. Results: Qwen-plus 56.6% (PS+DoI, best overall), DeepSeek-R1 52.4%, Doubao 48.5%, GPT-oss-120b 39.0%, Llama-70B 9.1%, GPT-3.5 1.0% (lowest); the top three models all achieved their best result under PS+DoI. For the VLMs Doubao and GPT-4o, adding the image (PS+I or PS+I+DoI) barely improved on the text-only PS+DoI prompt. A separate error study had experts review 100 problems that no model solved, yielding a four-way taxonomy — Type K (knowledge-based: correct domain knowledge not applied, e.g. misjudging internal loads), Type C (calculation: right formula, wrong arithmetic), Type E (extraction: failure to interpret or extract information from the prompt), and Type O (other: incomplete or off-target responses). Supplying DoI sharply cut extraction errors: Qwen-VL's Type E rate fell from 34% under PS+I to 6% under PS+DoI and 5% under PS+I+DoI, and GPT-4o's from 10% to 2.0% and 3.0%.

## Typical Duration

N/A — items are single-turn question-answering with no interactive environment or tool use; the only per-item cost the protocol fixes is five sampled responses followed by majority voting, and the paper reports no wall-clock, trajectory-length, or token-budget figures.

## Main Contribution

The authors present SoM-1K as the first large-scale multimodal benchmark dedicated to evaluating foundation models on strength-of-materials problems, and pair it with the Descriptions of Images prompting strategy as a diagnostic instrument. The headline empirical claim is that current models fail badly on this material — 56.6% at best — and that, counter to the expectation behind vision-language models, an expert-written textual description of a diagram is a more reliable input than the diagram itself, because it removes the visual-misinterpretation failure mode that dominates VLM errors.

## Key Design Ideas

- The diagram is annotated rather than merely attached: DoI is a curated, expert-corrected textual rendering of the schematic, deliberately restricted to visually present information so it cannot leak solution steps the way a chain-of-thought hint would.
- Three prompting strategies form a controlled factorial over modality, letting the effect of "having the picture" and "having a correct reading of the picture" be separated.
- Categorization along two orthogonal axes — deformation mode and static indeterminacy — supports difficulty-sliced reporting rather than a single aggregate.
- Ground truth is the textbook's full worked solution, and grading requires a valid reasoning sequence as well as a correct final answer, so answer-matching alone does not earn a point.
- Human expert grading of every response across all 1,065 problems, adopted over LLM-as-judge despite a pilot showing 83% agreement, so that the error taxonomy rests on expert reads of the reasoning.
- Majority voting over five samples per problem-setting to suppress sampling variance.

## Strengths

- The DoI ablation isolates a concrete mechanism rather than reporting only aggregate scores: extraction errors drop several-fold when a verified description replaces raw image input, which explains the headline LLM-beats-VLM result instead of just asserting it.
- Grading is fully manual by domain experts across all problems, with two-stage criteria and consensus resolution, giving unusually strong label quality for a benchmark of this size.
- Source material is genuine textbook and competition content with recorded provenance (the released dataset carries book, page, and figure references per item), and includes a deliberately harder statically indeterminate slice.
- The dataset is publicly released on Hugging Face with the problem statement, DoI, ground truth, and image-source metadata as structured fields.

## Limitations

- Scope is deliberately bounded to linear-elastic strength of materials; the authors list structural dynamics, plasticity, and nonlinear mechanics as future extensions, so nothing about advanced or nonlinear structural behaviour is probed.
- Diagram-based reasoning and calculation errors persist across all models, and the paper notes that generating accurate engineering diagrams (internal-force diagrams, deformation shapes) remains out of reach — a capability the benchmark identifies but does not itself score.
- Repository note: the evaluation is single-turn text generation with no tool access, no calculator, and no environment; Type C calculation errors are therefore counted against models that would have a symbolic or numeric tool in any realistic engineering setting, and the authors themselves observe that K and C errors could plausibly be mitigated by retrieval or computational tools.
- Repository note: manual grading of every response makes the protocol expensive to rerun, and the paper gives no released grading rubric or automated harness, so reproducing scores for a new model requires repeating the expert-scoring effort (or falling back to the LLM judge the authors rejected).
- Repository note: problems are generic textbook members — bars, shafts, beams, frames — rather than identified buildings, bridges, or civil structures, so the benchmark measures the mechanics foundation shared by civil and mechanical engineering rather than civil-specific design practice.
- Repository note: source material is drawn largely from long-published textbooks, some scanned from physical copies of Chinese editions; the paper reports no contamination analysis against model training data. TODO(reference)

## Related Works

- [StructureClaw](./structureclaw.md) — structural-engineering agent benchmark where tasks run through a solver-backed workbench rather than closed-form textbook mechanics.
- [EEE-Bench](./eee-bench.md) — single-field engineering benchmark built on the same premise, that professional problems require reading diagrams alongside text.
- [SeePhys](./seephys.md) — multimodal physics benchmark whose vision-essential problems raise the same question of whether models can read technical schematics.
- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction dataset whose civil field covers statics and mechanics of materials among other subdomains.
- [MaScQA](./mascqa.md) — exam-derived engineering question-answering dataset probing domain knowledge with a comparable answer-accuracy protocol.
- [FEM-Bench](./fem-bench.md) — computational-mechanics benchmark that asks for verified code rather than a worked analytical solution.
