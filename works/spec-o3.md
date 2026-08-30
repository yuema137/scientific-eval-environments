# Spec-o3 (2026)

> **English** | [简体中文](../zh/works/spec-o3.md)

> **First appeared:** 2026-01-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2601.06498)

## Overview

Spec-o3 is a tool-augmented vision-language agent for vetting rare celestial object candidates by automated spectral inspection. Alongside the agent, the paper contributes SpecVI-Bench, a standardized five-task benchmark of rare-object identification from LAMOST spectra with deliberately imbalanced test sets, external baselines, a cross-survey generalization split, and a published rubric for expert scoring of the agent's reasoning traces.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.06498>
- **Code:** <https://github.com/Maxwell-Jia/spec-o3>
- **Venue:** ACL 2026 Main Conference

## Summary

Final vetting of rare-object candidates in spectroscopic surveys still depends on expert visual inspection, which does not scale with survey volume. Spec-o3 replicates that workflow as an interleaved multimodal chain of thought: the agent reasons over a spectrum and calls a visualization tool to re-render arbitrary wavelength intervals before committing to a verdict. It is produced by a two-stage post-training recipe — cold-start supervised fine-tuning on expert inspection trajectories, then outcome-based reinforcement learning on rare-type verification. The evaluation artifact, SpecVI-Bench, defines five rare-object tasks with rarity-preserving test sets, compares against specialist deep models and proprietary and open VLMs, adds a held-out survey-shift split from LAMOST to SDSS/DESI, and has six astronomers score reasoning traces against a five-level rubric.

## Tasks

SpecVI-Bench comprises five rare-object identification tasks, one per category: cataclysmic variables (CV), carbon stars (CS), S-type stars (SS), M-type giants (MG) and white dwarfs (WD). Positive samples come from official LAMOST catalogs. Negatives are produced by rejection sampling over the full LAMOST archive, retaining only spectra whose predicted positive probability exceeds 0.8 — an acceptance rate of 1.74% — so that the negatives are genuinely confusable rather than trivially separable. Aggregate sizes are 1,681 positive / 1,683 negative for training and 1,122 positive / 5,632 negative for test; the CV task, for example, holds 343 / 368 training and 229 / 1,229 test samples. Test sets are deliberately imbalanced to reflect the rarity of true targets in practice. A separate cross-survey split cross-matches to SDSS/DESI with roughly 50 positive and 250 negative samples per task, covering CV, CS and MG only, since insufficient matched samples were available for SS and WD.

## Domains

Astronomy: the evaluated objective is spectroscopic classification of rare celestial objects from survey spectra — cataclysmic variables, carbon stars, S-type stars, M-type giants and white dwarfs — using LAMOST catalogs and archive data, with generalization tested against SDSS and DESI. Secondary co-domain is AI & Machine Learning Research, since the agent contribution is a vision-language post-training recipe.

## Evaluation

- **Primary metrics.** Per-task accuracy and positive-class F1, macro-averaged across the five tasks; the authors treat macro F1 as primary and accuracy as complementary because the test sets are imbalanced.
- **Reported (Table 1).** Spec-o3-7B reaches 88.7% macro accuracy and 76.5% macro F1, against 85.5% / 52.3% for o3 and 48.6% / 29.8% for GPT-4.1. Baselines span specialist deep models (CarbonNet, AstroCLIP, GaiaNet), proprietary VLMs (GPT-4.1, o3) and open-source VLMs (Qwen2.5-VL 3B and 7B, Qwen3-VL 8B and 30B-A3B).
- **Survey shift.** The same protocol is applied to the LAMOST → SDSS/DESI cross-matched split for CV, CS and MG as an unseen-distribution test.
- **Reasoning-trace evaluation.** Six astronomers with spectroscopy expertise scored 100 reasoning trajectories (50 each from Spec-o3-3B and Spec-o3-7B) on a published 0–5 rubric for coherence and physical consistency, ranging from "complete hallucination" (0) to "fully correct" (5). A separate pairwise-preference comparison of Spec-o3 against o3 used 50 cases per survey.

## Typical Duration

The RL stage caps the agent at a maximum of 8 tool calls per trajectory, and the average number of tool calls per trajectory decreases over training. Inference latency, wall-clock time and token or dollar cost are not reported.

## Main Contribution

A tool-augmented vision-language agent, trained by cold-start SFT on expert inspection trajectories plus outcome-based RL, that reaches state of the art on rare celestial object vetting; and SpecVI-Bench, the standardized five-task evaluation with rarity-preserving negatives, external baselines, a survey-shift split and an expert reasoning-trace rubric on which those claims are measured.

## Key Design Ideas

- Interleaved multimodal chain of thought: reasoning steps alternate with calls to a `spectral_visualization_tool` that re-renders a chosen wavelength interval (λmin, λmax) with optional labels, mirroring how an astronomer zooms into diagnostic features.
- The original numerical spectrum is cached and localized views are generated on demand, so the agent controls its own evidence rather than receiving a fixed image.
- Negatives mined by rejection sampling at a 0.8 classifier-probability threshold, making the benchmark's hard cases the ones a deployed classifier would actually surface for vetting.
- Test sets kept imbalanced on purpose, with positive-class F1 as the headline metric, so that scores track real vetting utility rather than balanced-accuracy artifacts.
- Outcome-based RL reward with an explicit format term: 1 for a correct prediction in valid format, 1−α for correct but malformed, 0 for incorrect in valid format, −α for incorrect and malformed.
- Trace quality assessed separately from label accuracy, via a five-level rubric and a pairwise-preference study.

## Strengths

- The benchmark's negative-sampling design targets exactly the confusable population that makes human vetting expensive, rather than random archive spectra.
- Baselines are genuinely external and span three families — astronomy specialist networks, proprietary VLMs and open-weight VLMs — so the comparison is not confined to ablations of the authors' own system.
- A held-out survey-shift evaluation (LAMOST → SDSS/DESI) tests the failure mode that most concerns operational deployment.
- Physical consistency of the reasoning traces is measured by domain experts against a published rubric, not asserted from example transcripts.

## Limitations

- Cross-survey generalization covers only three of the five tasks; insufficient cross-matched samples were available for S-type stars and white dwarfs.
- The agent has a single tool, spectral visualization, so the evaluation does not exercise catalog queries, cross-matching, or multi-instrument evidence gathering.
- Repository note: the paper's own framing is an agent and post-training method, with SpecVI-Bench presented as supporting infrastructure. It is carded here on the strength of that named benchmark — defined splits, external baselines, a stated scoring protocol and a published trace rubric — not on the training recipe, which falls outside the repository's scope.
- Repository note: benchmark construction depends on LAMOST catalog membership as ground truth, so catalog incompleteness or misclassification propagates directly into both training and test labels.

## Related Works

- [AstroAlertBench](./astroalertbench.md) — Also multimodal classification of astronomical survey detections with expert baselines, but on ZTF alert stamps rather than spectra, and without a trained agent.
- [Stargazer](./stargazer.md) — Also an astronomy evaluation over real archival observations, but scoring iterative physical model fitting rather than classification verdicts.
- [AstroVisBench](./astrovisbench.md) — Also an astronomy benchmark whose judging protocol is validated against professional astronomers, in the code-and-visualization setting.
