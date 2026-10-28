# Predictive Credit (2026)

> **English** | [简体中文](../zh/works/predictive-credit.md)

> **First appeared:** 2026-09-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.00314)

## Overview

Research-agent benchmarks often reward an agent for the explanation it writes, but a judge reading the explanation cannot tell whether it carries information or only sounds plausible. Predictive Credit replaces that reading with a forecasting test. A fixed LLM forecaster predicts the measured effect of a planned intervention three ways: from a plain description, with the state's own explanation, and with a donor explanation from a different state. The explanation earns credit only if it lowers forecast loss relative to the description and to the donor. Decision rules are frozen before outcomes are seen, and a researcher-written mechanism note serves as a positive control.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — an evaluation methodology for scoring explanations; it does not evaluate an agent on a scientific task.

## Links

- **Paper:** [Predictive Credit: Measuring What Scientific Explanations Add to Experimental Forecasts](https://arxiv.org/abs/2610.00314), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.00314v1>
- **Venue:** arXiv preprint (cs.AI), 2026
- **Code:** the paper mentions an anonymous supplement and repository without a link. TODO(reference)

## Summary

Each state is a public experimental setup plus a planned intervention; the forecast target is the held-out child-minus-parent change in an outcome metric, which the forecaster never sees. For each context c the protocol computes risk R_c = E[ℓ(f(c_i), y_i)] and reports G_description = R_D − R_M (description versus matched explanation) and G_alignment = R_S − R_M (donor versus matched); positive values favor the matched explanation. A Tox21 state, for instance, gets two independent forecasts of the ROC AUC change under each context, and the interval scores are compared against a frozen harm threshold. Across three settings the frozen decisions came out inconclusive or no-go: the authors conclude that predictive credit for natural explanations was not confirmed at the donor resolutions they tested, while the researcher-written mechanism note did lower point error.

## Tasks

N/A — methodology paper. The protocol is applied to 336 prospective states (3,708 prospective forecast slots) in three settings plus a positive control:

- **Controlled v5:** 120 states from one synthetic learning environment with six ML regimes; accuracy and log-loss targets.
- **Tox21 anchor:** 72 states (12 endpoints × 3 label budgets × 2 seeds) from MoleculeNet molecular assays, with a logistic model.
- **OpenML v2.1:** 144 states from 24 tasks (12 CC18 classification, 12 CTR23 regression), a LightGBM pipeline, and six interventions.
- **Mechanism positive control:** 40 paired tasks whose true note discloses a latent quadratic functional form.

## Domains

The settings are machine-learning experiments: a synthetic learning environment, Tox21 molecular toxicity assays, and OpenML tabular tasks. The protocol targets forecasts of experimental outcomes in general rather than one scientific field.

## Evaluation

- **Metrics:** point MAE, direction accuracy, 80% interval coverage and width, interval score IS80, and repeat drift |ŷ₁ − ŷ₂| between two independent forecasts.
- **Frozen decisions:** v5 "inconclusive"; Tox21 and OpenML "confirmation_no_go". The Tox21 rule requires matched-minus-control estimates ≥ .005 with positive one-sided lower bounds, joint positivity in at least 8 endpoints and 4 actions, and extraction integrity ≥ .95 in every stratum. Bootstraps are hierarchical; some contrasts are exploratory and not adjusted for multiplicity.
- **Controlled v5:** accuracy MAE, description minus matched, +.071 pp [−.102, +.252]; log-loss MAE +.0363 [−.0061, +.0807].
- **Tox21 (DeepSeek V4 Pro):** ROC AUC interval score, description minus matched, −.002628 [−.017392, +.010375] against the .005 threshold. Repeat drift falls from .01004 with the description to .00357 with the matched explanation and .00411 with a donor; point MAE is .02056, .02041, and .02023.
- **Tox21 Flash replay:** drift falls from .00704 to .00278 (matched) and .00288 (donor), while matched point MAE rises from .01823 to .02020; the matched-minus-donor interval score, .003268 [−.008096, .014485], gives "replication_not_supported".
- **OpenML:** full explanation cards widen mean intervals from .06179 to .07474 while coverage is 49.3% against 51.4% for the description; cards were nonempty in 66 of 144 states. Point MAE, description minus matched, is −.00741 [−.02804, +.00251].
- **Positive control (240 Flash forecasts):** point MAE 3.795 with the true note, 6.391 with the description, and 8.151 with a false note; the true note gains 2.596 [2.314, 2.880] over the description.
- Repository note: drift falls about equally with matched and donor explanations in Tox21, so the drift reduction does not by itself show that the explanation's content was used.

## Typical Duration

Calls ran through Claude CLI sessions to DeepSeek's Anthropic-compatible endpoint. Reconstructed API cost: v5 USD 6.01, Tox21 Pro USD 2.87, Tox21 Flash replay USD 0.50, OpenML USD 9.59.

## Main Contribution

A paired-forecast protocol that measures an explanation's value as the forecast loss it removes, compared against both a plain description and a donor explanation, with credit decisions frozen before outcomes are revealed.

## Key Design Ideas

- The donor condition separates content from format: a donor explanation from another state has the same form, so a matched advantage over it is attributable to the explanation's content.
- Donor resolution is controlled: Tox21 and OpenML swap seeds within the same task, budget, and intervention cell, while v5 uses a different intervention.
- Analysis is intention-to-treat; exhausted calls receive deterministic fallbacks rather than being dropped.
- A researcher-authored mechanism note checks that the protocol can detect credit when an explanation carries real information.

## Strengths

- Negative and inconclusive results are reported against pre-set rules rather than reinterpreted after the fact.
- The positive control shows the forecaster responds to explanation content: a true note lowers error and a false note raises it.
- Interval width, coverage, and drift are reported separately, which shows that a lower drift can coexist with no point-accuracy gain.

## Limitations

- The authors state that natural-explanation predictive credit is unconfirmed at the tested donor resolutions.
- OpenML elicited extraction integrity was 60.42%, below the .95 gate.
- Full-card drift magnitudes varied across Flash runs, and wider intervals coexisted with undercoverage.
- The authors note that one OpenML task (brazilian_houses) drives much of the OpenML error.
- The positive control is researcher-authored.
- The returned API wrappers did not record a resolved model ID.

## Related Works

- [AutoResearchEval](./autoresearcheval.md) — Also asks whether an evaluator's signal about research-agent output can be trusted, using human labels instead of forecasts.
- [EurekaBench](./eurekabench.md) — Scores submitted mechanisms partly by the held-out predictions they produce.
