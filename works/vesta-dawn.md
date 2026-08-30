# VESTA / DAWN (2026)

> **English** | [简体中文](../zh/works/vesta-dawn.md)

> **First appeared:** 2026-05-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.00384)

## Overview

VESTA is a vision-language agent that performs iterative statistical model fitting with a dynamically
expanding toolkit, introduced together with DAWN, a 400-instance benchmark of distribution-fitting and
time-series modelling tasks whose hardest splits are real astrophysical modelling problems — stellar initial
mass functions and gravitational-wave chirp signals.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.00384
- **Code:** https://github.com/wrudman/VESTA

## Summary

The paper argues that current models fail at the iterative loop scientists actually run when fitting a model
to data — plot, hypothesise a functional form, fit, inspect residuals, revise — and gives agents a toolkit
that grows during the episode with data transformations, hypothesis-driven visualisations, and statistical
tests. To measure progress on this loop the authors introduce DAWN (Dataset for Automated Workflows and
Numerical Modeling), which pairs synthetic easy and hard splits with astronomy splits drawn from genuine
astrophysical functional families, so that difficulty comes from the shape of real scientific models rather
than from added noise. DAWN is presented as a first-class contribution alongside the agent.

## Tasks

400 instances in total: 200 distribution-fitting tasks and 200 time-series tasks, each split into three
tiers. Distribution fitting comprises 50 easy instances (single distributions), 100 hard instances (mixtures
of two distributions), and a 50-instance astronomy split on stellar initial mass functions. Time series
comprises 50 easy instances (linear trends with basic seasonality), 100 hard instances (complex dynamics and
non-standard periodicities), and a 50-instance astronomy split on gravitational-wave chirps. The initial-mass
-function tasks span five functional forms — Salpeter (single power law), Kroupa (three-segment broken power
law), Chabrier (log-normal transitioning to a power law), and two freeform variants — which the paper notes
become visually distinguishable only in log-log space. The chirp tasks model continuously increasing
frequency, with complex variants adding amplitude-decay envelopes for inspiral-ringdown behaviour. Instances
are generated synthetically by sampling parameters uniformly from per-tier, per-family ranges; each
distribution-fitting dataset contains 600–1,500 points and each time-series dataset 600 observations.

## Domains

Astronomy is the domain of the two hardest DAWN splits: recovering the correct initial-mass-function family
and its parameters is a stellar-population modelling task, and fitting a chirp with an inspiral-ringdown
envelope is a gravitational-wave source-modelling task. The remaining splits are domain-neutral statistical
modelling, so the work also sits on the statistical-inference methodology axis (Mathematics). The astronomy
data are simulated from astrophysical functional families rather than taken from a survey archive, but the
scored objective on those splits is an astrophysical model-recovery result.

## Evaluation

Distribution-fitting tasks are scored by Jensen-Shannon divergence between the fitted and ground-truth
distributions — symmetric, bounded on [0,1], lower is better. Time-series tasks are scored by expected log
predictive density under leave-one-out cross-validation (ELPD-LOO), computed with sliding-window sampling to
keep the cost tractable. Three backbones were evaluated: GPT-5.4-mini, Claude Sonnet 4.6, and Kimi K2.5.

## Typical Duration

`TODO(reference)` — the paper does not report a per-task step limit, wall-clock time, or token budget in the
material verified for this card.

## Main Contribution

The authors' stated contribution is twofold: an agent framework that equips vision-language models with a
dynamically expanding statistical toolkit for iterative, visualization-grounded model fitting, and the DAWN
benchmark, introduced explicitly "to support advancement on challenging model fitting problems where current
approaches fail."

## Key Design Ideas

- A toolkit that expands during the episode rather than a fixed tool list, letting the agent construct the
  transformation or test it needs next.
- Visualization as an evidence channel: the agent generates hypothesis-driven plots and reads them back as
  visual input, which is what makes a vision-language backbone necessary.
- Difficulty tiers that separate synthetic easy and hard cases from a real-science split, so that domain
  difficulty is measured separately from statistical difficulty.
- Astronomy splits chosen for functional families that are near-degenerate in linear space and separable only
  under the right transformation, which directly tests the plot-transform-refit loop.
- Proper-scoring-rule metrics (Jensen-Shannon divergence, ELPD-LOO) instead of pass/fail matching, giving
  graded credit for a partially correct fit.

## Strengths

- The benchmark is a named, separable contribution with an explicit scoring protocol, not an evaluation
  appendix to the agent.
- Continuous, distribution-level metrics reward genuinely better fits rather than exact-answer matching.
- The astronomy splits use real astrophysical functional families rather than a generic dataset relabelled
  as scientific.
- Multiple backbones from different providers are evaluated under the same protocol.

## Limitations

- All DAWN instances are synthetically generated from known parameter ranges, so ground truth exists by
  construction and the benchmark does not test fitting against real survey or detector data with its own
  systematics.
- Only three backbones are evaluated, which limits how firmly the reported ranking generalises.
- Astronomy covers two functional families (initial mass functions and chirps); it does not span the breadth
  of astronomical inference.
- Repository note: the compute or step budget per episode is not reported, so results from iterative agents
  and single-shot baselines cannot be compared on equal cost.

## Related Works

- [Stargazer](./stargazer.md) — the closest astronomy-agent neighbour, evaluating agents on astronomical
  research analysis rather than on statistical model fitting.
- [gwBenchmarks](./gwbenchmarks.md) — gravitational-wave agent evaluation, overlapping DAWN's chirp split.
- [BLADE](./blade.md) — evaluates agents on data-analysis decisions, a related analysis-loop setting.
- [ScienceAgentBench](./scienceagentbench.md) — data-driven scientific agent tasks scored on executable
  outputs.
