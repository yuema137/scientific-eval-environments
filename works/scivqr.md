# SciVQR (2026)

> **English** | [简体中文](../zh/works/scivqr.md)

> **First appeared:** 2026-05-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.10187)

## Overview

SciVQR is a multimodal scientific-reasoning benchmark of 3,254 image-paired questions spanning 6 subjects and 54 subfields — mathematics, physics, chemistry, geography, astronomy and biology — in which astronomy is a first-class, separately scored subject with its own subfield breakdown.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.10187>
- **Code:** <https://github.com/CASIA-IVA-Lab/SciVQR>
- **Venue:** arXiv preprint (cs.CV), May 2026

## Summary

SciVQR asks whether multimodal large language models can carry out scientific reasoning that genuinely depends on a diagram, chart, equation or structural figure rather than on text alone. Questions are drawn from scientific competitions, college entrance exams, and college and graduate-level exams and textbooks, then filtered so that visual information is indispensable rather than auxiliary. Beyond final-answer accuracy, the benchmark supplies expert-authored stepwise solution traces for a large fraction of its items and uses them to score the fidelity of a model's chain of thought. Fifteen open-source and proprietary MLLMs are evaluated zero-shot, with and without CoT prompting.

## Tasks

3,254 image-question pairs (one image per question), built from 15 scientific competitions, 9 college entrance exams, and 6 college or graduate-level exams and textbooks. Composition: 2,545 multiple-choice (78.2%) and 709 free-form (21.8%); 1,490 items (45.8%) carry an expert-authored explanation; 2,661 items are in English (81.8%) and 593 in Chinese (18.2%). Difficulty is stratified into 997 easy, 1,240 medium and 1,017 hard. Construction: over 20 postgraduate annotators screenshotted visual questions and extracted text with the Mathpix OCR API, producing an initial pool of about 5k questions that was deduplicated by lexical overlap and Levenshtein distance; subfield labels were proposed by GPT-4V against a predefined list and then manually reviewed and corrected, with difficulty assigned from the original source material. Average question length is 77.2 words (max 495) and average explanation length 102.4 words (max 782).

## Domains

Six subjects: mathematics, physics, chemistry, biology, geography and **astronomy**. Astronomy is one of the six top-level subjects and carries its own scored column in the results tables, with six enumerated subfields — astrophysics, cosmology, stellar astronomy, galactic astronomy, planetary science and observational astronomy. Co-domains follow the remaining subjects: Mathematics, Physics, Chemistry, Biology, and Earth Science (the paper's "geography" subject, whose subfields include geology, geomorphology, hydrology, climatology and cartography).

## Evaluation

- Zero-shot accuracy, reported overall and per subject, under two prompt formats: direct question answering and CoT-prompted answering. The main results table reports the CoT setting; a separate table contrasts CoT-on against CoT-off per subject, and a third breaks results out by easy/medium/hard.
- A separate reasoning-quality evaluation scores the generated chain of thought against the expert-authored solution trace on five dimensions — faithfulness, informativeness, redundancy, hallucination and missing steps — each on a 10-point scale, averaged into an overall score. GPT-4o is used as the automated judge on a subset of SciVQR; the subset size is not stated (`TODO(reference)`).
- **Reported.** 15 models were evaluated: 11 open-source (LLaVA-NeXT-7B, LLaVA-OneVision-7B, MiniCPM-o-2.6-8B, Molmo-7B-D-0924, InternVL3-8B/14B/78B-Instruct, Qwen2.5-VL-7B/72B-Instruct, Keye-VL-1.5-8B, MiMo-VL-7B-RL-2508) and 4 proprietary (GPT-4o, o1, o4-mini, Gemini-2.5-Flash). o4-mini and Gemini-2.5-Flash tie for the best overall score at 79.3%, ahead of o1 at 77.2% and GPT-4o at 60.7%. The strongest open-source entry is the reasoning-tuned MiMo-VL-7B-RL-2508 at 69.2%, with Qwen2.5-VL-72B-Instruct at 61.8% and Keye-VL-1.5-8B at 59.7%; the smallest models remain below 40%. Mathematics and physics are the hardest subjects; o4-mini exceeds 70% accuracy in every subject. CoT prompting helps most models (Qwen2.5-VL-72B +7.9 overall, GPT-4o +6.1, Keye-VL-1.5-8B +16.3) but slightly hurts InternVL3-8B (-1.1). On the reasoning-quality rubric o4-mini scores 7.7 overall and o1 7.2, against 5.2 for Qwen2.5-VL-72B.
- Per-subject astronomy accuracies are not cited here; see Limitations.

## Typical Duration

N/A — static single-turn question answering with no tool use, no environment interaction and no step or token budget. Experiments were run on an internal cluster of NVIDIA A800 GPUs; no per-item wall-clock or token cost is reported.

## Main Contribution

The authors position SciVQR as the first multimodal scientific-reasoning benchmark to combine three properties they argue prior work only partially satisfies: disciplinary coverage (6 subjects and 54 subfields, against ScienceQA's 5/41 and MMMU's 5/39), difficulty diversity spanning high-school to graduate-level multi-hop inference rather than saturating at K-12 or college level, and solution traceability via stepwise expert annotations that make fine-grained CoT evaluation possible. Dual-language (English/Chinese) coverage is offered as a fourth axis for cross-lingual study.

## Key Design Ideas

- Questions are selected only where visual information is indispensable rather than auxiliary, to suppress language priors and text-only shortcuts.
- Expert-authored stepwise solutions for 45.8% of items enable process scoring separate from answer scoring.
- A five-dimension CoT rubric (faithfulness, informativeness, redundancy, hallucination, missing steps) rated on a 10-point scale by an LLM judge against the reference trace.
- Difficulty is inherited from the original source material rather than assigned post hoc, giving a three-tier stratification usable for saturation analysis.
- Subfield assignment is a two-stage process: model-proposed labels from a predefined taxonomy, followed by manual review and correction.
- Bilingual composition (81.8% English, 18.2% Chinese) supports cross-lingual comparison within a single benchmark.

## Strengths

- Astronomy is a genuine top-level subject with an explicit six-subfield taxonomy and its own scored column, not an incidental dataset borrowed as a visual testbed.
- Answer accuracy and reasoning-trace quality are measured separately, so a model cannot look competent purely by guessing final answers on multiple-choice items.
- Broad model panel (15 systems across parameter scales, open and proprietary) with a uniform zero-shot protocol.
- The CoT-on/CoT-off contrast isolates the contribution of explicit reasoning per subject rather than only in aggregate.
- Difficulty stratification shows the expected monotonic degradation, supporting the claim that the tiers are meaningful.

## Limitations

- The benchmark evaluates static multimodal question answering only; there is no agent, tool use, execution, or multi-step environment interaction, so it speaks to scientific reasoning capability rather than to agent behaviour.
- No per-subject item counts are published, so the size of the astronomy slice within the 3,254 questions is unknown (`TODO(reference)`).
- The size of the subset used for the reasoning-quality rubric is not stated, and GPT-4o serves as judge while also being one of the evaluated models.
- Subfield labels originate from GPT-4V proposals; the paper reports manual review but gives no inter-annotator agreement statistic.
- Repository note: the per-subject columns of the main results table and the CoT ablation table are ordered differently (Biology/Geography/Astronomy versus Astronomy/Geography/Biology) while carrying identical numbers for shared rows, so the astronomy-specific accuracies cannot be read off unambiguously from the paper as published. Overall and cross-model figures are unaffected.

## Related Works

- [AstroMMBench](./astrommbench.md) — multimodal astronomy question answering over figures from astronomy papers, the astronomy-only counterpart to SciVQR's astronomy subject.
- [LLM-IOAA](./llm-ioaa.md) — exam-derived astronomy and astrophysics evaluation graded against official marking schemes.
- [SeePhys](./seephys.md) — multimodal benchmark built on vision-essential physics problems, the same design principle applied to a single discipline.
- [EEE-Bench](./eee-bench.md) — multimodal exam-derived benchmark in electrical engineering, with a comparable diagram-dependence failure analysis.
- [HLE](./hle.md) — broad multi-subject frontier exam benchmark with a much smaller per-subject footprint.
