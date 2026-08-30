# Science Edge Evaluation (SEE) (2026)

> **English** | [简体中文](../zh/works/science-edge-evaluation.md)

> **First appeared:** 2026-08-07 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.06931)

## Overview

Science Edge Evaluation (SEE) is a multimodal benchmark of expert-curated questions grounded in peer-reviewed literature and experimental practice in chemistry, biology, and materials science, designed to test whether multimodal large language models can make justified, evidence-bounded inferences from real laboratory-science data.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.06931
- **Code:** https://github.com/SKYLENAGE-AI/science-edge-evaluation
- **Venue:** arXiv preprint (2608.06931v1, submitted 2026-08-07)

## Summary

SEE evaluates multimodal large language models (MLLMs) on expert-level scientific problems that require reasoning over experimental data rather than recalling established concepts. Questions are built from figures and data drawn from peer-reviewed papers, recent research literature, and first-hand experimental data contributed by domain experts. The authors report that even the best-performing model reaches only 48.7% accuracy in the standard setting, that general-purpose models outperform science-specialized models on average, and that adding tool use in a visual-agent setting raises the best accuracy only modestly to 52.7% — arguing that the bottleneck is evidence-bounded reasoning discipline, not access to more information.

## Tasks

The benchmark consists of 1,116 questions spanning 3 disciplines (chemistry, biology, materials science) and 17 reported sub-fields. Questions use multiple-choice and numerical fill-in-the-blank formats. They were constructed from figures and data in peer-reviewed papers, recent research literature, and first-hand experimental data from experts, then passed through a multi-stage quality-control pipeline (standardization, AI-assisted checks, expert review for scientific accuracy, and image-ablation checking to verify that each question genuinely requires its visual input). The public GitHub release states 1,049 questions are publicly released.

## Domains

Chemistry, biology, and materials science. Visual inputs include bioactivity measurements, Cryo-EM structures, Western blot and gel electrophoresis images, spectra (infrared, NMR, mass spectrometry), microscopy images (SEM, TEM, AFM), X-ray diffraction patterns, and thermal analysis curves.

## Evaluation

Answers are scored against expert ground truth: multiple-choice answers must exactly match the ground-truth answer, and numerical fill-in-the-blank answers are evaluated against an expert-provided tolerance. A strict binary LLM-as-judge protocol is used, with Gemini 3.1 Pro as the primary judge. In the visual-agent evaluation, models may iteratively call web search and a code interpreter before returning a final answer.

## Typical Duration

TODO(reference) — the paper does not report a per-question trajectory length, wall-clock time, or token budget.

## Main Contribution

A multimodal, expert-curated benchmark that isolates evidence-bounded scientific reasoning over experimental results, showing that current MLLMs — including tool-augmented visual agents — cannot reliably derive justified, evidence-bounded inferences from experimental data, with the best model reaching 48.7% accuracy (52.7% with tools).

## Key Design Ideas

- Questions grounded in real experimental figures and data (spectra, microscopy, blots, diffraction patterns) rather than textbook concepts, targeting inference over experimental evidence.
- Image-ablation checking during curation to confirm each question genuinely depends on its visual input.
- Multi-stage quality control combining standardization, AI-assisted checks, and expert scientific review.
- A visual-agent setting that grants web search and a code interpreter, enabling a controlled comparison of tool-augmented versus tool-free accuracy.
- Coverage of both general-purpose and science-specialized MLLMs (19 models total: 15 general-purpose, 4 science-specialized).

## Strengths

- Grounds questions in peer-reviewed literature and first-hand experimental data across three experimental disciplines (per paper).
- Image-ablation checking guards against questions answerable without the visual input (per paper).
- Directly compares tool-free and tool-augmented (web search + code interpreter) settings on the same benchmark (per paper).

## Limitations

- The paper reports no human-expert baseline, so model accuracy is not calibrated against expert performance.
- Repository note: the paper reports 1,116 questions while the public GitHub release states 1,049 questions are publicly released; the full benchmark is larger than the public subset.
- Repository note: the primary LLM judge (Gemini 3.1 Pro) is also one of the evaluated general-purpose models, which the paper does not separately analyze for judge bias.

## Related Works

- [MaCBench](./macbench.md) — another multimodal chemistry and materials-science benchmark for (M)LLMs.
- [SciVisAgentBench](./scivisagentbench.md) — another benchmark evaluating agents on scientific visual/experimental data.
