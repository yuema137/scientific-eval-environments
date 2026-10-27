# QFT-Bench (2026)

> **English** | [简体中文](../zh/works/qft-bench.md)

> **First appeared:** 2026-10-23 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.33134)

## Overview

QFT-Bench tests whether language models can complete long quantum field theory (QFT) derivations that end in one closed-form quantity. A symbolic check decides correctness first; an LLM judge decides only when that check is inconclusive. A separate judge then asks whether the displayed derivation actually supports a correct answer.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** [LLMs Can Tackle High Energy Theoretical Physics, yet Gaps Remain: Part I, Quantum Field Theory](https://arxiv.org/abs/2610.33134), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.33134v1>
- **Project:** <https://qft-bench.github.io/>
- **Dataset:** <https://huggingface.co/datasets/LLMsHEP/QFT-Bench>
- **Code:** <https://github.com/qft-bench/qft-bench>
- **Venue:** arXiv preprint (hep-ph, cs.CL), 2026

## Summary

The authors use textbooks and lecture notes to choose topics, then write original problems or rewrite existing ones so that answers are not easily retrieved. Preliminary Sonnet-5 runs exposed missing assumptions, undefined notation, and unstated conventions, which were fixed in the statements. Fixing conventions and target quantities lets SymPy settle many answers. Across 39 models, twelve exceed 95% accuracy. The faithfulness check finds correct answers whose shown derivation does not justify them.

## Tasks

75 problems described as hard graduate to early research level, in eight areas: classical field theory (7), quantization of scalar, spinor, and vector fields (8), QED (7), regularization and renormalization (6), non-Abelian gauge theory and QCD (6), electroweak theory and the Higgs mechanism (8), supersymmetric field theories (18), and conformal field theories (15). Each has a closed-form reference answer and a reference step-by-step solution. For example, one problem asks for all classical supersymmetric vacua of a Wess–Zumino model. Sonnet-5 found the correct values but did not put them in a box, so the response was scored wrong.

## Domains

Physics, specifically high-energy theoretical physics through QFT. The authors call this Part I of a broader evaluation of high-energy theoretical physics.

## Evaluation

- The final answer is read from `\boxed{}`. A SymPy grader checks symbolic equivalence with the reference. If that check fails or is inconclusive, for example because of convention or gauge choices, Claude Opus-5 compares the answer with the reference answer and solution and returns a binary score. Responses without a boxed answer are wrong.
- The primary metric is average accuracy over the 75 problems. Table 4 also reports a separate symbolic-verification score for each model, from 33.3% to 85.3%.
- Among 39 models, GPT-6.1-Sol reaches 100.0% and the lowest scores are 41.3%.
- An Opus-5 judge assigns each wrong response one cause: conceptual, calculation, strong-prior, or instruction following. Averaged over three evaluations, conceptual errors make up 47.2% of failures in the lower-scoring half and 23.4% in the top half; instruction following makes up 31.5% in the top half.
- An Opus-5 rubric judge labels each response as having insufficient derivation, faithful, or unfaithful. The unfaithfulness rate is `U_m / C_m`, the share of correct answers labeled unfaithful. The average across 39 models is 7.2% over three runs; Llama models reach roughly 20–40%.
- Three QFT experts reviewed 60 responses from 15 models. Agreement on correctness is 98% for Opus-5 and 92% for GPT-5.6; agreement on faithfulness is 73% and 67%.

## Typical Duration

Generation uses `max_tokens` = 65,536 with thinking enabled when available; the Table 4 caption describes this as 64k. The faithfulness and error-category judges use a 32k-token limit; no limit is stated for the correctness judge. A wall-clock time is not reported.

## Main Contribution

A QFT-specific derivation benchmark with symbolic-first grading and a separate measure of whether a correct answer is supported by its displayed derivation.

## Key Design Ideas

- State conventions and target quantities so equivalence can usually be checked symbolically.
- Use the LLM judge only for answers that symbolic checking cannot settle.
- Score correctness and faithfulness separately, and compare both judges with human experts.

## Strengths

- Covers eight QFT areas, including 18 supersymmetry and 15 conformal field theory problems.
- Table 4 reports each model's symbolic-verification score beside its final accuracy.
- Human agreement is reported for both correctness and faithfulness judges.

## Limitations

- Faithfulness labels agree with experts only 73% (Opus-5) and 67% (GPT-5.6) of the time on 60 responses. Error categories are also judge-assigned.
- A correct but unboxed answer is scored wrong, and instruction following is the largest failure category among top-half models.
- Each problem receives one binary score; the authors leave accuracy@k to future work.
- Some problems are adapted from existing course material, and the scope is QFT only.
- Repository note: the public dataset includes reference answers and solutions, which later models could see during training.
- Repository note: with twelve models above 95%, accuracy leaves little room to separate the strongest models.

## Related Works

- [TPBench](./tpbench.md) — Evaluates theoretical-physics problems in high-energy theory and cosmology.
- [CritPt](./critpt.md) — Uses unpublished research-level physics challenges.
- [PHYSICS](./physics-benchmark.md) — Evaluates university-level physics problems with automated grading.
