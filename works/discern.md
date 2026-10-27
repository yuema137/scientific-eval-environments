# DISCERN (2026)

> **English** | [简体中文](../zh/works/discern.md)

> **First appeared:** 2026-09-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.33357)

## Overview

DISCERN tests whether a research agent makes sound decisions at three stages of a life-science workflow: vetting data, verifying an analysis, and proposing a hypothesis. Each stage has its own tasks and score, so a strong result at one stage cannot hide a failure at another.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](https://arxiv.org/abs/2609.33357)
- **Full text:** <https://arxiv.org/html/2609.33357v1>
- **Project:** <https://discern-benchmark.github.io/discern-website/> (listed in the comments of arXiv v2, 2026-10-26)
- **Data:** <https://huggingface.co/datasets/discern-bench-anon/discern-benchmark>
- **Venue:** arXiv preprint (2026)

## Summary

The paper notes that earlier benchmarks usually score analytical task completion or hypothesis generation separately. DISCERN places controlled problems in public datasets and also gives matched clean controls, so an agent loses credit both for missing a defect and for rejecting sound data. At the hypothesis stage, the agent states its expectation before seeing the evidence. Counterfactual dossiers are kept only when their evidence conflicts with that stated expectation. Agents earn perfect scores on 60.8% of Level 1, 34.2% of Level 2, and 0.6% of Level 3 evaluations.

## Tasks

203 tasks: 79 Level 1 data-integrity tasks (58 task types), 102 Level 2 analysis-verification tasks in 24 analysis families, and 22 Level 3 hypothesis dossiers. Level 1 challenges include genome-build mismatches and ambient RNA contamination. Level 2 runs analyses under clean or perturbed conditions with data confounds, tool or procedure failure modes, and statistical pitfalls; in the histone track, the default narrow-peak setting fragments broad H3K27me3 domains. The 22 dossiers comprise 8 real controls where evidence agrees with the prior, 6 native counterfactuals built on unexpected relationships already in the data, and 8 injected counterfactuals that alter a well-characterized relationship and regenerate consistent statistics. Eight models are ranked; Claude Fable 5 is reported separately because of incomplete coverage.

## Domains

Life sciences, in eight tracks: genome-wide association studies, clinical variant interpretation, bulk RNA-seq, single-cell RNA-seq, CRISPR perturbation screening, enhancer activity, chromatin regulation, and protein stability/structure. The paper groups them under genetics, transcriptomics, regulatory genomics, epigenomics, and protein biophysics. Calorimetry and nuclear-decay tracks are reported separately and do not enter the 203-task denominator or score.

## Evaluation

- Level 1 scores the agent's code, execution output, and report, with partial credit for partial diagnoses or remedies. On a clean control, full credit requires accepting the data; unsupported alarms, rejection, or fabricated defects lose credit.
- Level 2 averages four dimensions: analytical correctness, issue recognition, methodological response, and result calibration.
- An independent LLM verifier cross-checks the deterministic Level 1 and Level 2 grading; a human adjudicates every disagreement against the recorded evidence.
- Level 3 responses pass through three adversarial review rounds by GLM-4.6, Gemini 3.1 Flash-Lite Preview, and DeepSeek Reasoner. An LLM judge then applies the rubric for evidence fidelity, scientific reasoning, and novelty, and the authors validate each response. Novelty means a substantive idea not obvious from the supplied results; it is not checked against the literature. Abstention earns capped partial credit and no novelty credit.
- Each track composite is the geometric mean of its three level scores; the Overall Score (0–100) is the mean of the eight composites. It ranges from 39.8 (GPT-4.1) to 78.1 (GPT-6 Astra).
- Only 19 of 64 Level 1 clean-control evaluations (29.7%) correctly accept the data. Of 94 submitted hypotheses, 46.8% receive no novelty credit.
- Input and output tokens, API calls, and estimated cost are reported beside scores, excluding grading and reviewer activity. Token efficiency is Overall Score per million tokens; dollar figures are upper bounds because cache discounts are not logged.

## Typical Duration

No wall-clock duration is reported. Levels 1 and 2 run in a sealed Python sandbox with a 20-step execution budget and no network access. Level 3 allows three to six agent steps before the three review rounds.

## Main Contribution

Scores data vetting, analysis verification, and hypothesis generation as separate levels on the same life-science tracks, with clean controls that penalize over-rejection.

## Key Design Ideas

- Pair controlled data defects with matched clean controls under identical instructions.
- Elicit the agent's expectation before showing evidence, and keep counterfactual dossiers only when the evidence conflicts with it.
- Combine levels with a geometric mean, so a weak level lowers the track composite.

## Strengths

- Reports failure shares, such as identifying the wrong cause (21.7%) or diagnosing a problem without acting (7.9%) on challenged Level 1 evaluations.
- Reports token, call, and cost accounting under a stated protocol (frozen on 2026-08-24, per the paper).

## Limitations

- Bounded tasks and independently instantiated levels do not establish autonomous end-to-end research; hypotheses are not experimentally confirmed.
- Coverage is limited to selected life-science tracks. Models may already know the public datasets or published phenomena, and related tasks share datasets.
- Level 3 scores depend on an LLM judge and author validation; residual grading uncertainty remains.
- The v1 paper states that the Hugging Face repository and immutable release identifier remain placeholders until a separate public-release freeze.
- Repository note: on 2026-10-27 the Hugging Face dataset page held a populated dataset card (manifests, prompts, model outputs, grades, adjudication ledgers), but its dataset viewer failed to load rows; no separate code repository is linked from the project page.

## Related Works

- [GeneBench-Pro](./genebench-pro.md) — Scores multistage genomics analyses on simulated data.
- [HeurekaBench](./heurekabench.md) — Poses open-ended single-cell research questions from published studies.
- [BixBench](./bixbench.md) — Evaluates computational-biology data analysis.
