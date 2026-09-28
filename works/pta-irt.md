# PTA-IRT (2026)

> **English** | [简体中文](../zh/works/pta-irt.md)

> **First appeared:** 2026-08-29 · **Source:** [official code and data release commit](https://github.com/DeepSoftwareAnalytics/PTA-IRT/commit/b38263b72f3c4a52fcc8fe478e1eae385ba423a6)

## Overview

PTA-IRT estimates a software agent's full-benchmark score from a small executed subset. It uses historical execution trajectories during calibration, adding evidence about solving behavior to the pass/fail outcomes used by conventional item response models.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — evaluation methodology for generic software issue resolution, rather than a scientific research workflow.

## Links

- **Paper:** [Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation](https://arxiv.org/abs/2609.01603), September 1, 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.01603v1>
- **Code and data:** <https://github.com/DeepSoftwareAnalytics/PTA-IRT>

## Summary

Historical traces are summarized and used to learn task difficulty and discrimination. The method selects informative tasks across difficulty strata and trains a teacher–student estimator. A new agent runs only the selected tasks; the estimator predicts its performance on the rest.

## Tasks

The study uses SWE-bench Lite (300 tasks), Verified (500), Full (2,294), and Pro (730). These are overlapping benchmark variants, not four disjoint collections. The respective agent/model pools contain 35, 70, 14, and 14 entries. A held-out agent produces calibration outcomes, which are converted into estimated full-suite scores and rankings.

## Domains

Software and systems engineering: repository-level software issue resolution. The contribution is an evaluation estimator over existing tasks, not a new scientific coding suite.

## Evaluation

Four-fold cross-validation separates historical and held-out model pools. Mean absolute error measures score recovery; Kendall's tau and Spearman's rho measure ranking recovery against full-suite outcomes. At 10% calibration, the reported averages are MAE 0.041, tau 0.888, and rho 0.973. Ablations remove trajectory conditioning, change selection, and corrupt or drop summaries. Full-suite traces from the new agent are not required at scoring time.

## Typical Duration

No universal wall-clock duration. The main comparison executes 10% of a benchmark for calibration; a Lite sweep tests 5–25%. Historical trajectory collection and model-based summarization remain offline costs.

## Main Contribution

Trajectory-informed subset selection and score estimation that preserve a low execution budget for new agents.

## Key Design Ideas

- Use historical process evidence as privileged training information.
- Balance information-based selection across difficulty levels.
- Test score and ranking recovery separately from task success itself.

## Strengths

- Evaluates four suite variants and reports component ablations.
- Separates information available offline from observations available for a new agent.

## Limitations

- Requires historical outcomes and usable execution traces.
- Full and Pro have much smaller agent pools than Lite and Verified.
- Repository note: a predicted score is not a directly measured pass rate on unexecuted tasks; these results do not establish transfer to unrelated scientific workflows.

## Related Works

- [SWE-bench](./swe-bench.md)
- [The Replay Gap](./the-replay-gap.md)
