# MaD Physics (2026)

> **English** | [简体中文](../zh/works/mad-physics.md)

## Overview

MaD Physics (Measuring and Discovering Physics) is a benchmark that evaluates whether agents can plan informative measurements under a fixed cost budget and then infer the underlying physical law from the data they collect. It spans three simulated environments — classical mechanics, fluid mechanics, and quantum mechanics — each also offered with altered physical laws to control for memorized knowledge.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.10820>
- **Project:** <https://mad-physics.github.io/>

## Summary

MaD Physics argues that existing scientific-discovery benchmarks test either static knowledge recall or unconstrained experimental design, and so miss an agent's ability to make measurements and plan under constraints. It casts discovery as a two-phase process: in each trial the agent spends a fixed budget on measurements of a system — every observation priced by its fidelity — and then infers the underlying law to predict the system's future state. Across three environments based on distinct physical laws, with altered-physics variants to mitigate memorized-knowledge contamination, the authors benchmark four Gemini models and report shortcomings in their structured exploration and data-collection capabilities.

## Tasks

Three simulated environments, each built on a distinct physical law: classical mechanics (N particles in D dimensions), fluid mechanics (a 2D incompressible viscous fluid), and quantum mechanics (two particles in a 2D box). Each is presented in a normal configuration and in several altered-physics configurations — for classical mechanics, anisotropic inertia, an altered 1/r gravity law, and a ripple potential — plus a combined setting that applies multiple alterations at once. All environments are implemented in JAX, and agents collect data by issuing measurement code against the simulator.

## Domains

Simulated experimental physics across three regimes: classical mechanics, fluid dynamics, and quantum mechanics.

## Evaluation

- **Two-phase protocol.** In the measurement phase the agent queries the simulator until it exhausts a budget; in the prediction phase it infers the law and predicts the system state at queried times.
- **Fidelity-priced measurements.** Each observation costs 2, 5, or 10 for the Low, Medium, and High fidelity levels — noise 0.1, 0.01, and 0.001 respectively — with total spend capped at a per-trial budget of 200 for classical and fluid environments and 30 for quantum.
- **Prediction error.** Prediction error against the true future state is the primary metric, lower is better: normalized RMSE for classical mechanics, and L2 error on vorticity and probability density for fluid and quantum mechanics, each averaged over 33 random initializations.
- **Prompting conditions.** Every model is run with a base prompt and a strategy-augmented prompt.
- **Reported.** On the normal classical-mechanics configuration under the base prompt, prediction error is 6.61 for Gemini 2.5 Flash Lite, 5.97 for Gemini 2.5 Flash, 1.93 for Gemini 2.5 Pro, and 0.29 for Gemini 3 Flash; errors rise sharply under altered-physics configurations for the smaller models, and no human baseline is reported.

## Typical Duration

No fixed step or wall-clock cap; the length of a trial is bounded by the measurement budget — 200 for classical and fluid, 30 per trial for quantum. Generated measurement code is limited to 30 seconds of runtime with up to 5 retries, and the model's thinking budget is set to 4,000 tokens.

## Main Contribution

A benchmark that frames scientific discovery as budgeted measurement — pricing each observation by fidelity and capping total spend — so that agents must jointly infer an unknown, sometimes altered, physical law and plan their data collection under a resource constraint.

## Key Design Ideas

- Two-phase trials: a budgeted measurement phase followed by an inference-and-prediction phase.
- Fidelity-priced observations, with cost strictly increasing in precision, so measurement quality trades directly against quantity under a fixed budget.
- Altered physical laws — anisotropic inertia, modified gravity, velocity and vorticity modulation, entanglement scaling — to blunt contamination from memorized textbook physics.
- Differentiable JAX simulators for classical, fluid, and quantum systems, queried through agent-generated measurement code.

## Strengths

- Turns the trade-off between measurement quality and quantity into an explicit, scored constraint rather than a post-hoc statistic.
- Altered-physics variants separate genuine information-seeking from recall of standard laws.
- Executable simulators across three physical regimes give deterministic, reproducible scoring.

## Limitations

- Repository note: Every environment is a simulated physics system with a synthetic, hand-set cost function; whether performance under this budget transfers to real experimental cost structures is not evaluated.
- Repository note: Reported results cover four Gemini models with no human or non-Gemini baseline, so absolute difficulty and cross-family generality are not established.

## Related Works

- [SimulCost](./simulcost.md) — Also prices a scientific resource beyond tokens, but its currency is physics-simulation time and experimental resources rather than the fidelity of measurements an agent spends to uncover an unknown law.
- [CATP-LLM / OpenCATP](./catp-llm.md) — Also makes resource cost an explicit objective the agent optimizes, but over tool-use cost in general task planning rather than measurement fidelity under a fixed physics budget.
- [CostBench](./costbench.md) — Also scores cost-aware decision-making, but on tool-call budgets in generic tool-use rather than experimental measurement inside physical simulators.