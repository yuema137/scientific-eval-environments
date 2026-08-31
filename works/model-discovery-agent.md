# Model Discovery Agent (2026)

> **English** | [简体中文](../zh/works/model-discovery-agent.md)

> **First appeared:** 2026-08-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.09696v1)

## Overview

Model Discovery Agent (MDA) asks a scientific agent to do more than fit one model to a supplied dataset: it must decide which experiment to run next, maintain a Bayesian posterior over competing mechanistic models, and ask an LLM for new hypotheses when the current model set cannot explain the evidence. The paper evaluates that loop by plotting held-out predictive error and mechanism recovery against the number of experiments used.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.09696>
- **Benchmark code (NeuronBench):** <https://github.com/murphyk/neuronbench>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

At each round, MDA uses nested sequential Monte Carlo to update a posterior over model structures, parameters, and—when needed—latent states. A value-of-information objective chooses the next intervention; when posterior predictive checks show that the live hypotheses are inadequate, an LLM proposes new executable model structures and Bayesian evidence prunes the pool. Evaluation repeats after every experiment on held-out interventions, so the central result is a learning curve: how quickly the agent reaches accurate predictions or recovers the true mechanism, rather than whether it eventually succeeds with unlimited data.

## Tasks

Four interactive model-discovery families are evaluated: a 36-task subset of ChemBench/ActiveSciBench-Chem covering 12 enzyme-kinetic mechanism families at three difficulty tiers; six two-particle ForceBench worlds wrapped from DiscoverPhysics; seven BoxingGym probabilistic-programming domains; and six newly designed NeuronBench mystery neurons, each offered with deterministic Hodgkin–Huxley dynamics and a stochastic finite-channel-noise variant. The agent selects experimental conditions, observes simulated outcomes, updates its model, and predicts responses to interventions it did not run.

## Domains

Physics (counterfactual force laws), chemistry (enzyme kinetics), neuroscience (ion-channel mechanisms and electrophysiology), and general probabilistic model discovery through BoxingGym.

## Evaluation

- **Per-experiment learning curves.** After each intervention, the current Bayes predictor is scored on a disjoint held-out query distribution. The paper uses normalized MSE for most continuous targets, RMSLE-compatible error for chemical reaction rates, and Brier score for binary targets.
- **Mechanism recovery.** ChemBench uses SymPy-based mathematical-equivalence checking; ForceBench compares the submitted force law through held-out trajectories; NeuronBench records whether the discovered channel class matches the hidden mechanism.
- **Controlled comparisons.** MDA is compared with the original per-benchmark agents, a model-free in-context forecaster, random experimental design where applicable, and an ablation without M-open hypothesis expansion.
- **Reported.** With Opus 4.7 held constant across LLM-based methods, MDA reaches lower held-out error with fewer experiments than the published baselines on ChemBench, ForceBench, and BoxingGym. On NeuronBench, both information-directed policies beat random design in every deterministic world; task-directed value of information is slightly better than expected information gain in the stochastic setting.

## Typical Duration

Interactive episodes are bounded by an experiment budget rather than a reported wall-clock limit: the main evaluations run to 60 designed experiments on ChemBench, 8 on ForceBench, 10 on BoxingGym, and at most 5 additional experiments after two fixed passive observations on NeuronBench. The full stochastic NeuronBench loop is compute-intensive because each round nests particle filtering inside parameter and model inference.

## Main Contribution

A unified, data-efficiency-centered evaluation of LLM-assisted Bayesian model discovery, together with an M-open SMC³ agent that can expand its hypothesis space and a new stochastic electrophysiology benchmark for testing mechanism discovery under latent process noise.

## Key Design Ideas

- Three inference levels separate uncertainty over model structure, parameters, and latent dynamics instead of asking the LLM to carry those beliefs in text.
- Posterior predictive checks trigger LLM proposals only when the current hypothesis pool is inadequate; marginal likelihood then selects among old and new mechanisms.
- Expected information gain and task-directed value of information turn experiment selection into an explicit decision rule whose data efficiency can be measured.
- Held-out interventions are disjoint from the agent's chosen experiments, preventing a numerically good fit on collected data from standing in for a useful world model.
- NeuronBench hides novel ion-channel mechanisms behind ordinary textbook responses, then tests whether targeted stimulation protocols uncover them in deterministic and stochastic regimes.

## Strengths

- Uses one agent–environment protocol across chemistry, physics, probabilistic modeling, and electrophysiology, making experiment-efficiency curves comparable across otherwise different benchmarks.
- Separately checks predictive usefulness and structural recovery, exposing fitted expressions that predict well locally but are mechanistically wrong.
- The no-M-open ablation and random/EIG/task-directed design comparisons test which components account for the reported gains.

## Limitations

- The authors identify hypothesis proposal as a bottleneck: if the LLM never proposes a model family containing the truth, Bayesian selection cannot recover it.
- Full-batch nested SMC scales as `O(B²N_m)` in experiment budget `B` and live model count `N_m`, limiting the practical budget on the stochastic benchmark.
- Repository note: All four evaluation families use simulators or probabilistic programs rather than live laboratory experiments, so the reported data efficiency does not establish cost savings under real instruments, samples, or operator constraints.
- Repository note: The experiments use one LLM, Opus 4.7; the paper isolates the inference and design machinery more cleanly than it establishes model-family generality.

## Related Works

- [DiscoverPhysics](./discoverphysics.md) — Supplies the counterfactual force-law environments wrapped as ForceBench; MDA adds Bayesian model selection and experiment-efficiency evaluation.
- [MaD Physics](./mad-physics.md) — Also evaluates law discovery under a measurement budget, while pricing observation fidelity rather than optimizing value of information over a fixed action menu.
- [NewtonBench](./newtonbench.md) — Also tests interactive recovery of counterfactually shifted laws, with a larger generated task set and symbolic-expression submissions.
- [Gravity-Bench-v1](./gravity-bench.md) — Also makes observation planning part of simulated physics discovery and reports the cost of limited data access.
