# SlowLab (2026)

> **English** | [简体中文](../zh/works/slowlab.md)

> **First appeared:** 2026-10-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.34644)

## Overview

SlowLab tests AI agents as experimenters when each experiment is slow, scarce, and cannot be undone. The agent runs a one-year campaign in four simulated greenhouse compartments: every crop it plants occupies a compartment for 180 days and can only be continued or destroyed. At the end, it recommends one climate policy, which a private evaluator scores in weather the agent never saw.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [SlowLab: Benchmarking Autonomous AI Agents on a Year of Experiments They Cannot Undo](https://arxiv.org/abs/2610.34644)
- **Full text:** <https://arxiv.org/html/2610.34644v1>
- **Code:** <https://github.com/dingningpei/slowlab-benchmark> (MIT license)
- **Venue:** arXiv preprint (2026)

## Summary

Each site hides cultivar and facility parameters, so the agent must learn them from its own crops. A branched design separates in-season measurements from end-of-crop totals, and a Reader swap separates gathering evidence from reading it. In a preregistered study on 48 unseen sites, three low-cost language-model agents end near a fixed grower setting and below a prior-informed Bayesian-optimisation baseline. In 94–100% of Full branches, the agents plant their second wave only after the first closes, so in-season readings never change what they plant.

## Tasks

- An experiment is one start action: a compartment, a start day (no later than day 183), and a climate policy. The crop then grows for 180 days, followed by 2 cleaning days; stopping destroys it without salvage.
- A policy sets six values: day temperature (18–26 °C), night temperature (15–22 °C, not above day), CO₂ (400–1200 ppm), supplemental light (0–16 h), ventilation temperature offset (2–6 °C), and ventilation humidity limit (70–90%).
- Eight channels are recorded every 300 s: air temperature, relative humidity, CO₂, a canopy LAI proxy, and cumulative harvest, heat, light, and CO₂ dosing.
- Full feedback lets the agent read any record measured so far; Endpoint feedback shows only compartment status and each crop's totals at closure.
- The study uses 48 test sites and 8 pilot sites. Each site draws one campaign year and three evaluation years from eleven audited KNMI Cabauw weather years (2002–2011 and 2015).

## Domains

Controlled-environment crop production: greenhouse climate management of a simulated fruiting crop, built on the GreenLight greenhouse model (Katzin et al., 2020) with Cabauw weather. The paper does not name the crop species. The score is an economic margin, so the task combines crop growth with heating, lighting, and CO₂ costs.

## Evaluation

- The evaluator runs the recommended policy over three held-out weather years and two planting dates (1 January and 2 July). The site score is the mean of those six contribution margins in EUR/m²: harvest revenue minus electricity, heat, CO₂, planting, cleaning, and daily overhead costs at public prices.
- The agent knows the scoring rule but never sees its score.
- Agents: DeepSeek V4.1 Flash, MiMo V2.6 Flash, and GLM-5.3 Flash, two repeats per site. References: a fixed grower setting chosen on development sites without experiments, and a prior-informed local Bayesian-optimisation baseline (TuRBO-style trust region starting from the grower setting).
- Full-feedback means: baseline 33.62, GLM 29.62, MiMo 28.90, DeepSeek 28.02, fixed setting 29.34 EUR/m². Model-minus-baseline gaps range from −3.99 to −5.60 (all Holm p < 0.001).
- Full minus Endpoint is not significant for any method. Reader swaps do not significantly improve model recommendations.
- Statistics: two-sided sign-flip permutation tests and BCa bootstrap intervals; seven primary tests with Holm correction. The smallest effect of interest, 2 EUR/m², was fixed in advance; smallest detectable differences at 80% power are 1.30–3.03 EUR/m².
- On 8 test sites, a numerical search finds best-known policies 7.56 EUR/m² above the fixed setting on average. These values are lower bounds; repeated searches differed by 1.63 and 2.05 EUR/m².

## Typical Duration

Each campaign covers 365 simulated days. Budgets are 16 experiments, 32 decision calls (start, stop, recommend), 128 interface calls, and 5×10⁶ prompt characters; model agents are also capped at 200 model calls. A branched campaign costs about USD 0.079 (DeepSeek), 0.048 (GLM), or 0.052 (MiMo). The formal run comprised 480 campaigns and 2,880 evaluations, at USD 18.70 total API spend. The paper does not report wall-clock time per campaign.

## Main Contribution

A benchmark of slow, irreversible, budgeted experimentation with hidden site parameters and private out-of-sample scoring, plus branched and Reader-swap diagnostics that locate where agent shortfalls arise.

## Key Design Ideas

- Long, irreversible crops make each planting decision consume scarce compartment time.
- Scoring in unseen weather years separates a learned policy from one fitted to the campaign year.
- Branching Full and Endpoint feedback from one shared day-0 design isolates the value of in-season data.
- Preregistration hash-locked sample size, tests, models, prompts, code, and configuration before the formal run.

## Strengths

- Reports power analysis, multiple-comparison correction, intervals, and documented deviations from preregistration.
- Separates evidence gathering from evidence reading instead of reporting only final margins.
- Reports per-campaign API cost and call counts.

## Limitations

- The simulator failed the paper's external check against greenhouse data for air temperature (RMSE 2.579 °C, threshold 2.04) and humidity (RMSE 9.983 points, threshold 8.50); CO₂ passed. Results describe the simulation, not a physical facility.
- Only three low-cost models were tested, and GLM ran with capped reasoning.
- The baseline has domain priors the models lack, and it was redesigned after a pilot.
- The Reader-swap study used different sites per method, so it cannot compare evidence quality across methods.

## Related Works

- [Model Discovery Agent](./model-discovery-agent.md) — Scores what an agent learns after each experiment under a budget.
- [Gravity-Bench-v1](./gravity-bench.md) — Caps observations of a simulated physical system.
- [Frontier-Eng](./frontier-eng.md) — Optimizes engineering designs under a fixed simulator-interaction budget.
