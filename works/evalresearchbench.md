# EvalResearchBench (2026)

> **English** | [简体中文](../zh/works/evalresearchbench.md)

> **First appeared:** 2026-10-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.04184)

## Overview

An agent that improves itself needs a feedback signal, and the usual signal is a set of large benchmarks that are slow and expensive to rerun after every change. EvalResearchBench (ERB) asks whether an agent can build a cheaper substitute. A "researcher" agent gets target benchmark descriptions, permitted task sources, metered model APIs, and fixed time and money budgets, and must freeze an executable evaluator for coding, co-work, and reasoning. The frozen evaluator then scores a panel of candidate models, and the benchmark checks how closely those scores and rankings match the scores the candidates earned on 14 target benchmarks, including targets the researcher never saw.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — the researcher agent designs evaluators for general coding, co-work, and reasoning capability; no scientific research task is evaluated.

## Links

- **Paper:** [EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?](https://arxiv.org/abs/2610.04184), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.04184v1>
- **Project:** <https://mercury7353.github.io/self-evaluation-bench/>
- **Code:** <https://github.com/Mercury7353/self-evaluation-bench>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

The researcher has three hours, $100 for its own inference, and $100 for pilot tests of candidate models. It sees development targets and their reference scores for four development candidates; eight sealed targets and nine sealed candidates are withheld until after the freeze. It selects or writes at least 100 scored questions, implements graders, sets aggregation weights, pilots them, and freezes everything. An independent assessment then runs the frozen evaluator on all candidates (capped at $120 total, $30 per candidate). Each domain score is compared with the target references by 100 × Lin's concordance correlation coefficient, which rewards matching level and spread as well as order, and by pairwise agreement: the share of non-tied reference pairs the evaluator orders the same way, with measured ties counted as half. A constant evaluator gets Score 0 and 50% pairwise agreement.

## Tasks

One task, run once per researcher: build a compact evaluator for three domains. The 14 targets are split into six development-visible (DeepSWE, SciCode, SWE-bench Multilingual, GDPval, AdvancedIF, HLE) and eight sealed (Terminal-Bench 2.1, ProgramBench, SWE-bench, BrowseComp, Harvey LAB-AA, AA-Briefcase, AA-LCR, CritPt). The 13 candidate models are split into four development and nine sealed. Nine researchers are evaluated, one episode each, in Codex or Claude Code.

## Domains

General model capability in coding, co-work, and reasoning. SciCode and CritPt are among the targets, but the researcher's task is evaluator design rather than scientific work.

## Evaluation

- **Overall Score / pairwise agreement (target-equal over 14 targets):** GPT-6 Astra 22.79 / 69.54%, Grok 4.7 22.59 / 74.87%, Fable 5.1 21.96 / 67.80%, Opus 5 21.79 / 64.88%, Kimi K3 18.03 / 74.58%, GPT-5.6 Sol 16.99 / 63.32%, GLM-5.3 14.27 / 64.72%, DeepSeek V4 Pro 10.49 / 63.50%.
- **Ceiling:** an oracle computed with label knowledge reaches 91.20% pairwise agreement, the limit set by disagreements among the targets themselves.
- **Human-selected baseline (Random120):** a source-stratified sample of 120 public tasks (40 per domain) scores 13.10 / 68.29% on 12 candidates; on the matched panel seven of eight agent-built evaluators exceed its Score but only four exceed its pairwise agreement.
- **Development vs. sealed:** Fable 5.1 has the highest development-target Score (23.40), while Grok 4.7 has the highest sealed-target Score (26.14).
- **Failure cases:** in Opus 5's development diagnostic, 36 of 102 responses hit the answer cap, 32 of them empty; Fable 5 exhausted its assessment budget after 20 of 39 candidate-domain scores, so its row is an imputation scenario; six of Grok 4.7's 20 co-work questions carry 93.87% of that domain's weight.

## Typical Duration

Three hours of research time per researcher, with $100 researcher inference, $100 development testing, and up to $120 for assessment.

## Main Contribution

A benchmark that treats evaluator construction as the agent's task and scores the result by agreement with held-out benchmark scores, separating fit to visible targets from transfer to sealed ones.

## Key Design Ideas

- Sealed targets and candidates are hidden until the evaluator is frozen, so overfitting to visible references is measurable.
- Lin's concordance penalizes evaluators that order models correctly but at the wrong level or spread.
- Budgets for research, piloting, and assessment are fixed and metered separately.
- A human-selected public-task sample and a constant evaluator give reference points for the scores.

## Strengths

- Results separate development and sealed targets, showing that the best fit on visible targets does not give the best transfer.
- The agreement ceiling from cross-target disagreement is computed and reported.
- Failure cases are counted from the researchers' own diagnostics.

## Limitations

- Each researcher contributes one episode, so run-to-run variation is not measured.
- Reference scores are fixed public snapshots from different protocols, and target scales are not fully compatible.
- Some costs are collaborator reports rather than metered usage, and the Fable 5 row relies on imputation.
- Repository note: the v1 full text is titled "EvalResearchBench: Can AI Agents Design Their Own Evaluations?"; the arXiv listing carries the title used in Links. The card follows v1 for all numbers.

## Related Works

- [PTA-IRT](./pta-irt.md) — Also predicts full-suite outcomes from a smaller evaluation and validates the prediction on held-out agents.
- [AutoSciBench](./autoscibench.md) — Also has agents construct benchmark tasks, for scientific domains.
- [SciCode](./scicode.md) — One of the development targets.
