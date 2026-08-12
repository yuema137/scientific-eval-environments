# Modeling & Prediction

> **English** | [简体中文](../zh/activities/modeling_prediction.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on building or applying a scientific model that predicts quantities or behaviour — predictive and surrogate modelling, forecasting, property prediction, and model-fitting where the model itself is a central artifact.

## Scope

Includes scientific machine learning, property regression and classification, forecasting, and learning functional relationships for prediction. It is distinguished from Data Analysis (which extracts conclusions from observed data); the two co-occur only when both are genuinely evaluated. Optimization inside an ML training loop alone does not qualify.

## Task Patterns

One cluster targets **scientific property prediction** — mapping molecular or material structure to properties. [LLM4Mat-Bench](../works/llm4mat-bench.md) and [MatText](../works/mattext.md) both test whether LLMs predict crystal properties from text encodings, converging on the finding that geometry-aware task-specific models still dominate. [FGBench](../works/fgbench.md) localizes molecular property prediction to functional-group-level reasoning, while [AlchemyBench](../works/alchemybench.md) and [onePot-Bench](../works/onepot-bench.md) extend prediction to synthesis recipes and reaction/catalyst outcomes graded against private lab data.

A second cluster is **ML-engineering to optimize a model metric**, where the agent iteratively builds and trains models. [MLAgentBench](../works/mlagentbench.md), [MLE-bench](../works/mle-bench.md), and [MLE-Dojo](../works/mle-dojo.md) frame ML research/engineering as interactive improve-a-metric loops over Kaggle-style tasks; [DSBench](../works/dsbench.md) adds data-modeling tasks alongside analysis; and [BioXArena](../works/bioxarena.md) applies the full train-and-submit loop to biomedical ML under a fixed compute budget.

A third cluster is **physics-grounded forecasting and model-fitting**, where the fitted model is the central artifact. [gwBenchmarks](../works/gwbenchmarks.md) demands high-precision waveform surrogates and remnant fits, [RealPDEBench](../works/realpdebench.md) measures the sim-to-real gap for scientific ML on physical systems, [Stargazer](../works/stargazer.md) fits Keplerian orbital models to radial-velocity series, and [DiscoverPhysics](../works/discoverphysics.md) requires inferring and implementing the laws of counterfactual simulated worlds.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| MLAgentBench | 2023 | Iteratively improve an ML model's target metric | 13 ML-experimentation tasks, read/write/execute code, agentic | Beat starter-code baseline; best agent 37.5% avg | [card](../works/mlagentbench.md) |
| DSBench | 2024 | End-to-end predictive data modeling from data files | 540 tasks (74 modeling + 466 analysis), multimodal multi-table | Solve task; best solves 34.12% of analysis | [card](../works/dsbench.md) |
| LLM4Mat-Bench | 2024 | Predict materials properties from text-encoded crystals | Static regression/classification, | 1.9M structures, 45 properties, 3 modalities | [card](../works/llm4mat-bench.md) |
| MatText | 2024 | Predict crystal properties from text representations | Static regression, 9 representations, up to 70B params, 2M structures | Match geometric GNN baselines; documents geometric blindness | [card](../works/mattext.md) |
| MLE-bench | 2024 | End-to-end ML engineering to train competitive models | 75 curated Kaggle competitions, agentic, long-horizon | Kaggle medal thresholds; o1-preview bronze on 16.9% | [card](../works/mle-bench.md) |
| AlchemyBench | 2025 | Predict full materials synthesis recipe and outcomes | Static prediction over 17,000 expert-verified recipes | LLM-as-a-Judge agreement with expert assessment | [card](../works/alchemybench.md) |
| FGBench | 2025 | Reason about molecular property at functional-group level | 625K problems (245 groups); 7K curated LLM subset, static QA | Regression/classification accuracy; LLMs struggle | [card](../works/fgbench.md) |
| MLE-Dojo | 2025 | Iteratively build and refine ML models with feedback | 200+ Kaggle challenges, Gym-style interactive, SFT/RL-trainable | Iterative improvement and solution quality across 8 LLMs | [card](../works/mle-dojo.md) |
| BioXArena | 2026 | Build and train biomedical predictive models | 76 end-to-end tasks, 9 domains, 2-hour single-GPU budget | Hidden-label 0-1 score; best MLEvolve 0.666 | [card](../works/bioxarena.md) |
| DiscoverPhysics | 2026 | Infer and implement laws of counterfactual worlds | 22 simulated N-body worlds, iterative experiment proposal | Trajectory MSE plus rubric-judged explanation; best | [card](../works/discoverphysics.md) |
| DSAgentBench | 2026 | Build predictive models within data-science workflows | 275 real-environment tasks including a modeling stage | Deterministic model-performance verification | [card](../works/dsagentbench.md) |
| gwBenchmarks | 2026 | Build high-precision surrogates and fit remnant properties | 8 tasks over >10^8 core-hours of NR-grade data | Relative error near 1e-4 via external evaluator; agents fall short | [card](../works/gwbenchmarks.md) |
| onepot-Bench 0 | 2026 | Predict reaction outcomes and select catalysts | 3-part suite (cheminformatics, refusal, synthesis), private lab data | Prediction against private experimental ground truth | [card](../works/onepot-bench.md) |
| RealPDEBench | 2026 | Scientific ML models bridging real and simulated physics | 5 real+paired-sim datasets, 3 tasks, 8 metrics, 10 baselines | Data/physics metrics; pretraining improves accuracy | [card](../works/realpdebench.md) |
| Stargazer | 2026 | Iteratively fit Keplerian orbital models to RV series | 120 tasks (100 synthetic 3 tiers + 20 real), REPL feedback | Per-criterion pass/fail; Easy 80% to Hard 5.8%, real 0% | [card](../works/stargazer.md) |

## Related Works

- [DSAgentBench](../works/dsagentbench.md)
- [MLAgentBench](../works/mlagentbench.md)
- [DSBench](../works/dsbench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatText](../works/mattext.md)
- [MLE-bench](../works/mle-bench.md)
- [AlchemyBench](../works/alchemybench.md)
- [FGBench](../works/fgbench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [BioXArena](../works/bioxarena.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [RealPDEBench](../works/realpdebench.md)
- [Stargazer](../works/stargazer.md)
