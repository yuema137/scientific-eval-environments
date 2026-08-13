# AstroAlertBench (2026)

> **English** | [简体中文](../zh/works/astroalertbench.md)

## Overview

AstroAlertBench is a multimodal benchmark for astronomical alert review: models classify real Zwicky Transient Facility (ZTF) alerts into five categories along a three-stage chain of metadata grounding, scientific reasoning and hierarchical classification, with an explicit "honesty" axis measuring whether a model's self-assessment tracks its actual correctness.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.05573>
- **Project:** <https://astroalertbench.com>
- **Code:** <https://github.com/LLM-for-Astronomy/AstroAlertBench>
- **Venue:** arXiv preprint (astro-ph.IM, cs.AI), 2026

## Summary

Modern time-domain surveys generate far more alerts than experts can vet, which is the bottleneck AstroAlertBench targets. Each item pairs tabular alert metadata with a single RGB stamp montage (science, reference/template, difference) for one object, and a model must first demonstrate that it reads the metadata fields correctly, then produce a structured scientific rationale, then commit to a hierarchical classification. The benchmark separates accuracy from calibration: models also self-score their own reasoning, and the gap between self-score and correctness is reported as an honesty measure. Thirteen frontier vision-capable models are evaluated, alongside a human ensemble baseline and a Zooniverse-based protocol intended to scale human-in-the-loop annotation.

## Tasks

A pilot set of 1,500 real ZTF alerts, balanced at 300 examples per class so that scores reflect multimodal reasoning rather than majority-class priors. Items are built from the ALeRCE real-time stamp-classifier dataset derived from the ZTF alert stream, taking the first-detection alert of each unique astrophysical object. The five categories are bogus, asteroid, supernova, AGN and variable star. Each item consists of tabular metadata plus an RGB montage of the science, reference and difference stamps.

## Domains

Astronomy: the evaluated objective is time-domain astronomical classification — deciding whether a difference-image detection is an artifact, a moving solar-system object, or a genuine transient or variable source, and which astrophysical class it belongs to. The item construction is drawn from an operational survey alert broker.

## Evaluation

Three graded stages:

- **Stage A — metadata grounding (perception).** The model maps numerical alert parameters to their scientific meaning across six fields (`fid`, `isdiffpos`, `magpsf`, `sigmapsf`, `ndethist`, `ncovhist`). All 13 evaluated models scored 100% accuracy on all six fields.
- **Stage B — scientific rationale (reasoning).** The model emits a structured justification and assigns itself a 0–5 score per dimension; reported metrics are the mean self-reasoning score and the self pass rate, defined as the proportion of alerts averaging ≥ 4.
- **Stage C — staged classification (decision).** A hierarchical cascade — artifact rejection, then physical origin, then astrophysical subclass — scored by per-stage accuracy, conditional accuracy, and end-to-end 5-class accuracy.
- **Honesty.** Defined as alignment between a model's self-evaluation and its objective correctness, probed three ways: population-level modesty, instance-level calibration via Pearson correlation, and a behavioral second-rollout retry.
- **Reported.** End-to-end 5-class accuracy across 13 models: Claude Opus 4.7 (thinking) 60.60 ± 1.26%, GPT-5.4 high-think 51.07 ± 1.29%, Kimi K2.5 think 49.34 ± 1.29%, Claude Opus 4.7 no-think 48.87 ± 1.29%, Qwen3.5-397B-A17B think 44.27 ± 1.28%, GPT-5.4 no-think 43.67 ± 1.28%, Gemini 2.5 Pro high-think 41.93 ± 1.27%, Gemini 2.5 Flash no-think 36.27 ± 1.24%, Qwen3.5-397B-A17B no-think 34.98 ± 1.23%, Qwen3.5-35B-A3B think 26.73 ± 1.14%, Qwen3.5-35B-A3B no-think 25.50 ± 1.13%, Qwen3.5-4B no-think 22.32 ± 1.08%, Qwen3.5-4B think 8.41 ± 0.72%. A human ensemble baseline reaches 30.67 ± 5.32%.

## Typical Duration

Not reported as wall-clock or cost. Decoding settings are specified: temperature 0.2 with `max_tokens` 2,048 for standard models and 20,000 for reasoning models; total token consumption and runtime are not disclosed.

## Main Contribution

A multimodal, class-balanced benchmark for astronomical event review that decomposes the task into perception, reasoning and hierarchical decision stages, and introduces an honesty/self-calibration axis showing that accuracy and reliable self-assessment do not coincide.

## Key Design Ideas

- Alerts are presented in operational form — broker metadata plus the science/reference/difference stamp triplet — rather than as curated images, so the input matches what a human vetter sees.
- The three-stage chain isolates whether errors come from misreading metadata, from faulty astrophysical reasoning, or from the final decision.
- Class-balanced sampling (300 per class) removes the extreme class imbalance of the real alert stream from the score, at the cost of realism in prior.
- Hierarchical classification (artifact → physical origin → subclass) supports conditional accuracy, so partial competence is visible.
- Honesty measured behaviorally as well as statistically, including a second-rollout retry to see whether a model revises when unsure.
- A Zooniverse project is initialized as a route to community-scale human annotation beyond the internal expert baseline.

## Strengths

- Items come from a live survey broker (ALeRCE over the ZTF stream) in the same modality a human vetter reviews, so the task form matches operational practice.
- Breadth of comparison: 13 vision-capable models spanning closed and open weights, with thinking and non-thinking variants of the same model reported separately.
- A human ensemble baseline is measured rather than assumed, giving the accuracy numbers an interpretable reference point.
- The honesty axis is operationalized in three independent ways instead of a single confidence-calibration statistic.
- Data, prompts, runners and scorers are released, with the dataset card and 1,500-row manifest hosted publicly.

## Limitations

- The item set is explicitly described as a pilot sample, and the class balance is imposed rather than natural, so accuracies do not transfer directly to alert-stream throughput.
- Stage A is saturated — every model scores 100% on all six metadata fields — so it contributes no discrimination between models.
- Repository note: the benchmark is single-turn multimodal classification with self-scoring, not an agent loop; there is no tool use, no archive query and no multi-step trajectory, so it evaluates astronomical judgment rather than autonomous investigation. It is admitted here under the repository's exam-derived-QA precedent: sized item set, stated protocol, multiple models compared.
- Repository note: the human ensemble baseline (30.67%) is measured on a representative subset with wide error bars, which limits how firmly model-versus-human claims can be read.

## Related Works

- [Stargazer](./stargazer.md) — Also an astronomy evaluation on real archival observational data, but an iterative model-fitting environment rather than single-shot multimodal classification.
- [AstroVisBench](./astrovisbench.md) — Also an astronomy-native benchmark with a judge validated against professional astronomers, but scoring code and visualization rather than alert classification.
- [SciVisAgentBench](./scivisagentbench.md) — Also pairs LLM judging with expert-agreement analysis, in the scientific-visualization setting.
- [MaScQA](./mascqa.md) — Precedent for admitting a sized, protocol-stated domain question set evaluated across multiple models.
