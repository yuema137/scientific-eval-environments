# Autonomous Science Bench (2026)

> **English** | [简体中文](../zh/works/autonomous-science-bench.md)

> **First appeared:** 2026-10-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.18449)

## Overview

Autonomous Science Bench (ASB) turns published laboratory experiments into budgeted design-build-test-learn campaigns. An agent orders a fixed number of experiment batches from a candidate pool, receives recorded measurements back from a lab service, and finally hands in a predictive model. Instead of grading a written report or a single best result, the benchmark resolves a trial only when two separate gates pass: the measured batches must contain enough scientifically meaningful hits (the discovery gate), and the submitted model must rank held-out designs well (the learning gate).

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** [Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449), Yibo Wen and Han Liu, 2026 preprint (v1 2026-10-13, v2 2026-11-16).
- **Full text:** <https://arxiv.org/html/2610.18449v2>
- **Project:** <https://asb.open-ssi.org/> (version 0.1, with leaderboard)
- **Code:** <https://github.com/Open-SSI/autonomous-science-bench> (Apache-2.0; `github.com/Yibo-Wen/as-bench` redirects here)
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Each campaign starts from a published screen in which the full measured design pool is known. The agent sees seed data and a pool of orderable designs, then submits one batch per round through an `asb` command-line client. A lab container on an internal network checks the request (round order, batch size, eligibility, uniqueness), charges the budget only for accepted batches, logs them in a ledger the agent cannot edit, and returns the recorded values (replay backend) or values from a hidden surrogate from the source study (digital-twin backend). After the last round the agent submits a JavaScript `predict(design)` function, which is run in a sandbox without files, network, clock, randomness, or labels. Splitting the score into a discovery gate and a learning gate separates "found good designs" from "learned a model of the design space"; across 180 trials, 129 unresolved trials divide into 29 that missed only discovery, 34 that missed only learning, and 66 that missed both.

## Tasks

Six campaigns in version 0.1, two each in biology, chemistry, and materials science, each built on a published experiment (paper Table 2):

| Campaign | Source | Backend | Rounds × batch | Pool | Budget / pool | Discovery gate | Learning gate |
|---|---|---|---|---|---|---|---|
| Nuclease | Thomas et al. 2025 | replay | 4 × 96 | 20,000 | 1.9% | ≥190 hits and ≥175 families | NDCG@100 ≥ 0.42 |
| Biosensor | Wang et al. 2025a | replay | 3 × 10 | 677 | 4.4% | ≥21 selective hits | NDCG@20 ≥ 0.70 |
| Propylene | Kim et al. 2025 | twin | 3 × 20 | 736 | 8.2% | ≥7 hits | NDCG@20 ≥ 0.52 |
| Suzuki | Perera et al. 2018 | replay | 4 × 48 | 2,764 | 6.9% | ≥32 standouts | NDCG@100 ≥ 0.37 |
| OER | Rohr et al. 2020 | replay | 4 × 48 | 3,419 | 5.6% | ≥55 standouts, ≤28 per library | NDCG@100 ≥ 0.55 |
| Coercivity | Wang et al. 2022 | replay | 4 × 16 | 604 | 10.6% | peak score ≥ 0.60 | NDCG@20 ≥ 0.65 |

Expert time estimates per campaign are 8 to 12 hours. Held-out evaluation sets contain 5,000, 332, 244, 1,844, 5,039, and 307 designs, in table order.

A representative trace is the coercivity campaign. The underlying data are a Co–Fe–Ni thin-film composition spread of 921 compositions with measured coercivity and Kerr rotation. The agent starts with 10 seed compositions spread over the composition triangle, orders four rounds of 16 from a pool of 604, and submits a predictor scored on 307 held-out compositions. The landscape has two coercivity peaks (contiguous regions with coercivity ≥ 8 mT and a maximum ≥ 9.5 mT), and the number of peaks is not disclosed to the agent. Half of the discovery score is the fraction of standouts found in the less-covered peak, so ordering only around the literature peak scores at most 0.25 against the 0.60 threshold.

## Domains

Biology (nuclease and biosensor campaigns), chemistry (propylene campaign on a digital twin; Suzuki coupling campaign), and materials science (oxygen evolution reaction libraries; Co–Fe–Ni thin-film coercivity). The per-campaign scientific detail beyond the coercivity card is TODO(reference).

## Evaluation

- **Discovery gate:** a statistic of the agent's measured set compared against a calibrated threshold, usually a count of hits above a scientifically meaningful bar. "Standouts" are hits defined by rank within a group. Nuclease takes the smaller of its hit ratio and family ratio; coercivity uses the two-peak score above.
- **Learning gate:** NDCG@k of the submitted `predict` function on the held-out set, with relevance max(true score − τ, 0); the gate passes when NDCG@k meets the campaign threshold.
- **Resolution:** reward 1 only if both gates pass.
- **Calibration checks:** a no-op agent must score 0, the reference solution must resolve every campaign, and zero-measurement predictors must fail the learning gate. A biosensor catalog tally passed both gates on 2 of 30 splits.
- **Pilot (v2):** 10 agent-model configurations, 3 trials per campaign, 180 trials; 51 resolved. GPT-6 Astra (Codex) resolved 13/18 (72%), Opus 5.5 (Claude Code) 12/18 (67%), GPT-5.6 Terra 8/18 (44%), Muse Wonder (Muse Code) 7/18 (39%), GPT-5.6 Luna 5/18 (28%), Sonnet 5.5 and GLM-5.3 Flash 2/18, Qwen3.8 27B and MiniMax M3 1/18, Haiku 4.5 0/18. Coercivity was the hardest campaign (5/30 resolved) and OER the most resolved (13/30).
- **Cost:** total cost over 18 trials ranges from $6.91 (GPT-5.6 Luna) to $190.22 (GPT-6 Astra); cost per resolved trial is $1.38 (Luna), $6.45 (Terra), $14.41 (Opus 5.5), and $14.63 (GPT-6 Astra).
- **Gate correlation:** Spearman correlation between normalized discovery and learning scores is 0.47 across all 180 trials and 0.42 to 0.75 within campaigns.

## Typical Duration

8-hour limit per trial, run as Harbor tasks (Harbor 0.21.0; Muse Code trials on 0.25.0) on local Docker. Reported total agent time over 18 trials ranges from 1.5 h (Haiku 4.5) to 28.4 h (GLM-5.3 Flash). Token counts are not reported.

## Main Contribution

A closed-loop discovery benchmark in which the agent spends a fixed experimental budget against a lab interface and is scored on two independent outcomes, discovery and learned prediction, with a lab API designed so the same campaign can later run against a digital twin or a physical lab.

## Key Design Ideas

- The lab, not the agent, owns the experiment ledger and budget; rejected requests cost nothing and accepted jobs cannot be edited.
- Two gates per campaign: hits in the measured batches and NDCG@k of a sandboxed predictor on held-out designs.
- Shortcut closures built into gate design, such as withholding two published nuclease columns close to an answer key and the two-peak coercivity score.
- Three backend tiers behind one Lab API: replay (five campaigns), digital twin (one campaign), and a live physical-lab backend defined as an interface only.
- A proposed adaptive budget scheduler for the live backend (not evaluated in v0.1).

## Strengths

- The gate split is diagnostic: per-campaign failure counts show, for example, that 16 of 19 unresolved propylene trials (v1) failed only learning, while coercivity failures mostly missed both gates.
- No-op, reference, and zero-measurement controls check that each gate can be failed and passed as intended.
- Cost and agent time are reported next to resolution rate for every configuration.

## Limitations

- The authors list scale (six campaigns in three fields) as a limitation, and note that replay and twin backends restrict the design space to recorded or simulated designs.
- Published data may be memorized by models, or retrieved during a trial if egress controls fail; the authors state that egress controls block known answer sources.
- The live backend is interface-only in v0.1; no physical-lab trial is evaluated.
- Muse Wonder costs are estimated from token counts at list prices, and Muse Code cannot be pinned to a version.
- The project leaderboard notes that with three trials per task, small gaps between configurations are not yet meaningful.
- Repository note: v1 of the paper reported 8 configurations over 144 trials (best 67%, hardest campaign 3/24); v2 adds GPT-6 Astra and Muse Wonder. The official repository README still shows the v1 count (31 of 144 resolved) and lists seven campaigns in its campaign table while describing results on six.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also packages scientific agent tasks as containerized Harbor-style tasks, but with single-session programmatic verification rather than a multi-round experiment budget.
- [DiscoveryBench](./discoverybench.md) — Also targets data-driven discovery, but from fixed datasets rather than agent-chosen experiment batches.
- [RE-Bench](./re-bench.md) — Also compares agents under explicit budgets, in ML research engineering rather than wet-lab-derived campaigns.
