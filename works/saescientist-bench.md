# SAEScientist-Bench (2026)

> **English** | [简体中文](../zh/works/saescientist-bench.md)

> **First appeared:** 2026-09-08 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.09113)

## Overview

Sparse-autoencoder (SAE) interpretability research is done by people who write probe texts, inspect which dictionary features fire, and test candidates by steering the model. SAEScientist-Bench gives that loop to an agent. For a target concept such as "tax filing language", the agent designs contrastive texts, queries a 131,072-feature Gemma Scope dictionary for Gemma-2-9B-IT, and submits one feature ID. The submitted feature is then scored against an expert reference feature from Neuronpedia on how strongly it activates for the concept, how well it separates the concept from controls, and whether steering with it moves the model's output toward the concept.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?](https://arxiv.org/abs/2609.09113), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.09113v1>
- **Code:** <https://github.com/Trae1ounG/SAEScientist>
- **Venue:** arXiv preprint (cs.AI, cs.CL, cs.LG), 2026; marked "Preprint. Work in Progress."

## Summary

The agent works in a writable workspace with network access disabled and one tool, `probe_sae`, which accepts up to 64 texts per request and returns the top activating features or measures supplied candidates with activations and dictionary-wide ranks. It decides how many probes to run and when to stop, within a 60-minute timeout. The submitted feature is run on fixed text suites. Activation Rank compares its mean dictionary rank on positive texts with the expert feature's; Activation Selectivity is 100 × max(0, 2·AUROC − 1) for positives against hard-negative and neutral controls; Causal Steering has a GPT-4o judge rate baseline, steered, and random-feature outputs in two shuffled passes and credits the steered output's target relevance above the better of the two controls. The overall score is the unweighted mean of the three. The paper reports that agents design reasonable contrasts but often misread their own measurements.

## Tasks

20 concept-layer tasks over 17 concepts at Gemma Scope residual-stream layers 9 and 20, spanning languages (French, German, Latin, Portuguese, Spanish, Turkish), document formats (job postings, real estate listings, weather forecasts), and domain concepts (clinical symptom reports, pharmaceutical dosing, archaeological excavation); earnings reports, portfolio allocation, and tax filing appear at both layers. Each task has a frozen expert feature, taken from public steering presets where available or validated through expert curation with positive, hard-negative, and neutral texts.

## Domains

Mechanistic interpretability of a language model: single-feature discovery in SAE dictionaries of Gemma-2-9B-IT.

## Evaluation

- **Runs:** 10 agent configurations, three runs per task, 600 scored episodes in total; Cursor for most models and Codex for GPT-5.6 Sol and Luna, both at high reasoning effort.
- **Expert reference:** Overall 85.56 (Rank 100.00, Activation 98.92, Steering 57.75).
- **Agents, Overall (Rank / Activation / Steering), mean over three runs:** Kimi K3 65.82 (74.30 / 92.91 / 30.26), Claude Opus 5 65.41 (75.35 / 91.89 / 28.99), Claude Sonnet 5 65.04 (73.45 / 92.01 / 29.66), Grok 4.6 62.93 (67.21 / 90.11 / 31.47), Claude Opus 4.8 62.57, Gemini 3.8 Flash 59.57, GPT-5.6 Sol 57.28, GPT-5.5 54.34, GLM-5.2 52.27, GPT-5.6 Luna 50.27.
- **Pattern:** agents come close to the expert on selectivity (best 92.91 vs. 98.92) and fall furthest behind on steering (best 31.47 vs. 57.75).
- **Failure analysis:** case studies only, e.g. a Portuguese-task feature that fires more on the English control (4.50) than on the Portuguese target (3.81), giving an overall score of 13.91; no counts of measurement misreadings are given.

## Typical Duration

60-minute timeout per task; no step or token budget. The archive holds 4,873 probe calls over all runs.

## Main Contribution

A benchmark that scores an agent's interpretability finding against an expert reference on correlational and causal criteria, rather than grading its written explanation.

## Key Design Ideas

- The deliverable is a single feature ID, so the score depends on measurements of that feature rather than on the agent's report.
- Selectivity uses hard negatives and neutral texts, so a feature that fires on everything scores low.
- Steering is credited only above the better of the unsteered baseline and a random-feature control.

## Strengths

- Two of three metrics are computed deterministically from activations, and each configuration is run three times with standard deviations reported.
- The expert reference row places agent scores on the same scale.
- The probe interface is fixed and shared, so configurations differ only in the agent.

## Limitations

- The authors state the benchmark covers one model, two layers, and a fixed probe interface.
- Tasks are single-feature discovery for a given concept; multi-feature circuits and open-ended hypothesis generation are not covered.
- Steering scores come from an LLM judge without human validation, and text suites and expert features are frozen.
- No downstream editing or unlearning tests are included.
- Repository note: the paper describes run-to-run variation as typically within 1–3 points, while its table reports standard deviations of 5.42 (Opus 4.8) and 7.40 (Luna) on the overall score.

## Related Works

- [EurekaBench](./eurekabench.md) — Also scores a finding the agent reaches through experiments it designs and runs itself.
- [FIRE-Bench](./fire-bench.md) — Also evaluates agents on machine-learning research findings checked against established results.
