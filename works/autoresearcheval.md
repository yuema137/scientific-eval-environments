# AutoResearchEval (2026)

> **English** | [简体中文](../zh/works/autoresearcheval.md)

> **First appeared:** 2026-08-13 · **Source:** [official data-generation pipeline release](https://github.com/PrentisAI/AutoResearchEval/commit/55bb0dbf5e7a4539f22c3ef7f7d8784adb61c4b4)

## Overview

AutoResearchEval checks whether a research agent's claims agree with the code, data, and execution logs it actually produced. It diagnoses 800 trajectories from 100 scientific tasks using ARFT, a taxonomy of 45 failure patterns across research stages and four root-cause categories.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](https://arxiv.org/abs/2608.14905), first submitted August 14, 2026; v3 revised August 25.
- **Full text:** <https://arxiv.org/html/2608.14905v3>
- **Code:** <https://github.com/PrentisAI/AutoResearchEval>
- **Data:** <https://huggingface.co/datasets/PrentisAI/AutoResearchEval>
- **Venue:** arXiv preprint. The official task-generation pipeline predates the paper by one day.

## Summary

A polished report can conceal an unexecuted experiment or a claim contradicted by the agent's own files. The judge therefore inspects the complete artifact set and attaches evidence to each diagnosed failure. Three experts refined the taxonomy through five agreement rounds; an agent judge scales this inspection to eight harness-model combinations. The study reports recurring failures in checking evidence, revising conclusions, and reconsidering a research plan, rather than a leaderboard of scientific success.

## Tasks

From 5,878 candidate papers, the authors construct 70 open-ended discovery tasks and 30 target-anchored optimization tasks. An agent receives the prior scientific context and unresolved question, while the source paper's method and conclusions are withheld. It proceeds through ideation, retrieval, execution, analysis, writing, and self-review, producing `decision.json`, a report, and intermediate artifacts. Live web retrieval is available only in the open-ended subset; optimization containers disable it. The two subsets differ in domain and contribution type and are analyzed separately.

For example, Appendix C.9 traces an echocardiography task in which the agent starts training in the background but ends its session before predictions are delivered. The judge checks the files and logs instead of treating a successful container exit as a successful research result.

## Domains

Figure 2 explicitly gives the source-domain counts: biology **24** (15 discovery + 9 optimization), medicine **15** (12 + 3), chemistry **14** (9 + 5), scientific computing **13** (11 + 2), materials science **12** (7 + 5), physics **12** (7 + 5), and geophysics **10** (9 + 1).

Appendix G includes microbiome and cellular biology, clinical prediction and biomedical modeling, quantum chemistry and biomolecular binding, crystal structure and materials processing, condensed-matter and gravitational physics, and seismic and climate investigations. Repository note: geophysics maps to Earth Science. The heterogeneous scientific-computing label is retained as a source category, not automatically assigned wholesale to Computer Science.

## Evaluation

Each task runs once under eight harness-model combinations: six backbones in Claude Code, gpt-5-mini in Codex, and gemini-3.5-flash in Gemini CLI (Table 1). ARFT labels failures by six lifecycle stages plus a cross-stage layer, and by grounding, cognitive depth, scientific integrity, or engineering robustness.

The artifact-aware judge is calibrated on **50 human-labeled trajectories**. Table 2 reports pattern-level Cohen's **κ = 0.75** and root-category **κ = 0.83**, versus **0.53 / 0.62** for a single-call transcript-only judge; pattern recall rises from **63.5% to 80.7%**. A quality checker rejects insufficiently supported analyses and requests revision before pattern labeling. Across 800 analyses, the paper reports **12,712 pattern hits**, including uncorrected self-awareness in **82.5%** of analyses. These are failure-label frequencies, not task success rates.

## Typical Duration

Appendix F.3 specifies a **four-hour rollout limit**, plus **one hour for environment setup**. Judge analysis has a separate **90-minute nominal budget**, extended to **210 minutes** for verification reruns (Appendix C.3). These are budget ceilings, not measured typical runtimes; a numeric rollout token cap is not specified.

## Main Contribution

A released task and trajectory corpus, a failure taxonomy, and a human-calibrated evaluator that checks research claims against executable artifacts.

## Key Design Ideas

- Separate the stage where a failure appears from the category used to explain it.
- Require concrete evidence from files and logs for the judge's findings.
- Retain open-ended tasks whose process can be inspected even without a single correct final answer.

## Strengths

- Links scientific reports to the intermediate evidence needed to audit them.
- Reports judge agreement and recall against human labels.
- Publishes task-construction and judging code alongside a separately hosted dataset.

## Limitations

- Agreement is reported in aggregate; per-pattern and per-category judge error remain unquantified.
- The paper does not separate failure incidence from remaining resource budget, and cannot exclude contamination from published source papers.
- Repository note: Table 1 does not cross the same models across all harnesses. Recurring failures support a descriptive finding across the tested systems, but do not by themselves isolate a model-only causal mechanism; orchestration interventions are not tested.
- Repository note: the judge comparison changes both artifact access and the judging procedure, so it does not isolate artifact access alone.
- The official code repository excludes the Docker/SLURM rollout orchestration used for the experiments.

## Related Works

- [AutoResearchBench](./autoresearchbench.md)
- [Beyond Final Scores](./beyond-final-scores.md)
- [ScienceAgentBench](./scienceagentbench.md)
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](./ara-survey.md)
