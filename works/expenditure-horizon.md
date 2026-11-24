# Expenditure Horizon (2026)

> **English** | [简体中文](../zh/works/expenditure-horizon.md)

> **First appeared:** 2026-07-21 · **Source:** [METR research report](https://metr.org/blog/2026-07-21-expenditure-horizon/)

## Overview

Expenditure horizon is a METR metric for an agent's ability to improve a continuous optimization target. Instead of asking whether an agent solved a task, it puts agent and human progress on the same dollar axis: agent cost is API tokens plus experiment compute, human cost is estimated labor hours at a wage. The expenditure horizon is the budget at which the agent's cumulative improvement equals what humans achieved for the same spend; beyond it, paying humans is more cost-effective. The report illustrates the metric on the NanoGPT speedrun.

## Topics


- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Report:** [Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT](https://metr.org/blog/2026-07-21-expenditure-horizon/), Tom Cunningham, Manish Shetty, Vincent Cheng, Nate Rush, METR, 2026-07-21.
- **Task source:** NanoGPT speedrun, <https://github.com/KellerJordan/modded-nanogpt>
- **Related METR note:** <https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/>
- **Venue:** METR research report (no accompanying paper or code release is linked)

## Summary

The old way to report an agent on an open-ended optimization problem is a score after some run, which says nothing about whether a human would have got further with the same money. METR builds two returns-to-expenditure curves. The human curve comes from the speedrun's record history: effort per record is estimated from contributor interviews and an LLM judge, calibrated, and priced at $150/hour. The agent curve comes from long agent runs, where every claimed gain is re-validated with repeated runs. The expenditure horizon is where the agent curve meets the human curve. After more than $10K of spend per run, the report estimates horizons of $0 to about $3K; the result is sensitive to the assumed human cost per 1% improvement.

## Tasks

One optimization task: the NanoGPT speedrun (modded-nanogpt), which minimizes wall-clock training time to reach validation loss 3.28 on FineWeb on 8× H100 GPUs. The record history has 82 records from May 2024 to April 2026. Agent runs start from record #78 (March 2026, 85.56 s). The agent edits only `solution.py`; `runner.py` (which owns the timer) and `validate.py` (which computes cross-entropy from returned logits) are root-owned and protected.

Repository note: the report states that the method applies to constrained optimization problems and can summarize existing AI R&D benchmarks such as RE-Bench and MLE-bench, but only the NanoGPT speedrun is measured.

## Domains

AI and machine-learning research: language-model training speed optimization.

## Evaluation

- **Definition:** expenditure horizon is "the dollar value at which the improvement to the goal metric is equal to the improvement by a human" with the same budget. A related quantity, cost saving, is the expenditure an agent saves before switching back to humans becomes cheaper; the authors describe it as harder to estimate.
- **Human returns curve:** focused on records #19–#82 (since January 2025). Two top contributors were interviewed about six records (9.8% total speedup, about 142 hours); an LLM judge (Opus-4.6) estimated hours per PR; the two estimates are combined by geometric mean with a correction factor α = 1.58 (bootstrap 95% CI [1.07, 2.62]). At $150/hour this gives about $2,500 per 1% improvement, and total human expenditure of about $250,000. Before the elbow near record #19, each 1% cost about $200.
- **Agent returns curve:** runs of up to $10,000 (API plus GPU) over 5 days, with 4 H100 nodes (32 GPUs) on Modal and asynchronous tools for running experiments in parallel. Agents may score intermediate solutions freely and are prompted to explore with few runs and confirm with n = 8. Claimed progress is re-run 40+ times, and the top-3 intermediate solutions are re-run for every $500 spent; curves are shown cumulatively and per doubling with bootstrap ±1 SD bands.
- **Trace:** an agent change that shortens training time is timed by the protected runner, the validator checks loss from logits, and the gain is re-validated; the re-validated percentage speedup at each cumulative dollar spent is compared with the human curve at $2,500 per 1%.
- **Results:** six high-expenditure runs. GPT-5 and Opus-4.1 made no meaningful progress after re-validation. The other four models have positive horizons from $600 to $3.3K. Opus-4.8 (about 1.5% re-validated gain) has $3,300 and GPT-5.5 (about 1% gain) $2,300 at the medium assumption. Under easy / medium / hard human costs ($1K / $2.5K / $10K per 1%), Opus-4.8 is $120 / $3,300 / $14,400 and GPT-5.5 $160 / $2,300 / $9,400.
- **Mergeability:** a maintainer judged about 70% of agent ideas mergeable; the mergeable share of speedup was about 60% for Opus-4.8 and about 50% for GPT-5.5.

## Typical Duration

Up to $10,000 and 5 days per agent run; experiments account for roughly 70–90% of trajectory cost.

## Main Contribution

A dollar-denominated metric that compares agent and human returns on the same optimization problem, with an empirical illustration on the NanoGPT speedrun.

## Key Design Ideas

- Agent and human effort measured in the same unit (dollars), including model API, GPU compute, and human labor.
- Repeated re-validation of agent-claimed gains, because raw trajectories overstate progress through noise.
- Human effort estimated from two sources (interviews and an LLM judge) and calibrated against contributor retro-estimates.
- Sensitivity analysis across easy, medium, and hard human-cost assumptions.

## Strengths

- Continuous scoring captures partial progress on a problem where pass/fail would discard it.
- Re-validation and a protected runner and validator guard against noise-driven and tampered gains; the report documents reward-hacking and brittle changes it found.
- Contamination is probed: runs from record #12 showed memorization of later records and are excluded from the main results.

## Limitations

- The authors state that the harness is likely inefficient and that agent changes were largely hyperparameter tuning ("mostly fiddling with knobs" per the maintainer).
- Human effort is uncertain: the judge underestimated totals by about 37% relative to contributors, and upstream research and collaboration are not fully captured.
- Results are sensitive to the assumed human cost per 1%, and the method assumes agent returns diminish faster than human returns.
- Only autonomous optimization is measured, not hybrid human–AI work; record #78 already includes some agent-produced optimizations.
- Runs from #78 are mostly after model knowledge cutoffs, except possibly Opus-4.8.
- Repository note: one run per model is reported on one task, so model-to-model differences are not accompanied by run-to-run variance; the sixth model is not named in the report text.

## Related Works

- [RE-Bench](./re-bench.md) — Also compares agents with human experts on ML research-engineering optimization at matched budgets (time rather than dollars); named in the report as a benchmark the metric could summarize.
- [MLE-bench](./mle-bench.md) — Named in the report as another AI R&D benchmark the metric could summarize.
