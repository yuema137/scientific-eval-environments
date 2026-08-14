# An LLM-driven framework for cosmological model-building and exploration (2025)

> **English** | [简体中文](../zh/works/an-llm-driven-framework-for-cosmological-model-bui.md)

## Overview

A multi-stage evaluation framework that measures whether an LLM-driven coding agent can autonomously propose, implement and explore alternative cosmological models by modifying the CLASS Boltzmann-solver codebase inside a containerized environment. Agent submissions are scored automatically against binary execution milestones, numerical agreement with ground-truth reference implementations, and cosmological likelihood/tension rewards computed from real survey data.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_178.pdf>
- **Venue:** Machine Learning and the Physical Sciences Workshop, NeurIPS 2025 (preprint number MIT-CTP/5945)

## Summary

The authors state that they "introduce a multi-stage framework to evaluate the ability of an LLM-driven agent to autonomously propose, implement and explore cosmological models." The agent works inside a Podman/Docker container that pre-installs CLASS version 3.3.0 together with stage-specific prompt files, LLM-generated file maps of the `background.c`, `perturbations.c` and `input.c` modules, model descriptions and auxiliary testing code. Its deliverable is a patch to the CLASS repository, which is exported from the container and evaluated automatically. The framing is explicitly evaluative: the paper's concluding claim is that the results provide "a concrete framework for evaluating AI agents on complex scientific workflows that combine domain knowledge, mathematical reasoning, coding, and empirical validation."

## Tasks

Tasks are organised as three sequential stages per cosmological model instance. Stage 1 (Model Implementation) requires reading a model description and modifying CLASS to implement the model; it succeeds when the code compiles and implements the target model. Stage 2 (Computing Observables) requires using the modified code to compute observables such as power spectra at fiducial parameters via a provided helper script. Stage 3 (Parameter Exploration and Rewards) evaluates the implemented model's agreement with observations, run either in *Minimization* mode (numerical maximum-likelihood fitting) or *Exploration* mode (the agent manually proposes and tests parameter combinations) depending on whether the model is amenable to optimization.

Each model instance is specified by three artifacts: a Model Description (either a curated `description.md` with in-depth implementation tips, or the original research paper's TeX source), Fiducial Parameters used to test the modified code and enable quantitative comparison against a target implementation, and a Context File (`problem_context.yaml`).

Two target models are evaluated: a phenomenological *Thawing Quintessence* (TQ) model and an *Early Dark Energy* (EDE) model, in increasing order of difficulty; both have ground-truth implementations available. Two further hypothesis-generation experiments ask the agent to invent its own dark-energy model (*One-Shot*, and *One-Shot + Summary* where a `gemini-2.5-pro` summary of five recent papers is supplied). The paper reports that in two additional hypothesis-generation experiments with different contextual information the agent could not generate code passing all binary execution milestones.

## Domains

Astronomy — specifically cosmology: implementing alternative dark-energy and modified-cosmology models in a Boltzmann solver, computing CMB and matter power spectra, and confronting them with DESI baryon acoustic oscillation measurements, a Planck early-Universe CMB three-parameter prior, Pantheon+ supernovae, and SH0ES Hubble-constant measurements. Physics is a legitimate co-domain (the models are dark-energy field theories), and Scientific Software & Systems work is instrumental (patching a ~43,000-line C codebase plus 10,000 lines of numerical files).

## Evaluation

Scoring is automatic and layered:

- **Binary execution milestones** — three milestones tracking that the agent generated a patch, that it compiles, and that it can be used to compute observables.
- **Numerical accuracy** — the agent's computed physical quantities (power spectra and the evolution of the dark-energy field) are compared against a ground-truth repository implementing the same cosmological model, reporting the maximum fractional deviation. If Stage 2 execution fails, a separate LLM (`o1-2024-12-17`) is queried to compare the model description against the generated patch and identify inconsistencies, functioning as an LLM-as-a-Judge.
- **Stage 3 cosmological rewards** — (1) data likelihood together with the Bayesian Information Criterion (BIC) to penalize overfitting via extra parameters; (2) Hubble tension, measured by comparing predicted `H0` to SH0ES, or alternatively comparing `M_B` values as a more robust late-time diagnostic; (3) CMB power spectrum agreement, the maximum deviation of the predicted `C_l` from the Planck 2018 `C_l` in cosmic variance units, used as a consistency check.

**Reported results (Table 1, Target Artifact-based Evaluation Results).** The evaluated agent is Claude Code with `claude-sonnet-4-20250514`. All three settings passed the execution milestones. Max fractional deviation of `Ω_X`/mPk(0)/mPk(1): EDE [curated] 0.026/0.116/0.110; TQ [curated] 2.2e−7/1.1e−4/7.6e−5; TQ [paper] 0.248/0.100/0.027. `ln L`: 558 (EDE curated), 830 (TQ curated), 830 (TQ paper). BIC: N/A, −1616, −1616. `H0` tension: 4.12σ [67.94], 4.73σ [67.19], 3.57σ [68.61]. `M_B` tension: N/A, 5.01σ [−19.42], 5.03σ [−19.42].

**Table 2 (LLM-proposed Model Results).** ΛCDM reference: `ln L` 831, BIC −1640, `H0` tension 4.22σ [67.82], `M_B` tension 5.25σ [−19.43]. Agent-proposed EDE-RC (One-Shot): 828, −1604, 2.75σ [69.63], 4.69σ [−19.41]. Agent-proposed ODEM (One-Shot + Summary): 828, −1612, 3.70σ [68.46], 4.70σ [−19.41].

## Typical Duration

TODO(reference) — the paper does not report per-task wall-clock time, trajectory length or token budgets.

## Main Contribution

In the authors' framing, a multi-stage framework for evaluating whether an LLM-driven agent can autonomously propose, implement and explore cosmological models, applied to show that agents produce reasonable implementations when given rich domain context but struggle to attain numerical accuracy without expert-crafted prompts, and that an agent's self-proposed dark-energy model achieved observational fits comparable to the standard model while requiring additional parameters.

## Key Design Ideas

- Uses a real, unified scientific workflow: the paper argues cosmology is unusually suited to this evaluation because "almost all papers implementing an alternate cosmological model rely on 2-4 codebases" and alternate theories "must pass a set of unified tests," so model discovery "can be reformulated as an optimization problem with well-defined metrics."
- Separates capability levels into three sequential stages with distinct success criteria, so partial progress is observable rather than collapsing to a single pass/fail.
- Contrasts a *curated description* condition against a *paper-to-code* condition (swapping `description.md` for the source paper's TeX file) to isolate how much of agent success depends on human-authored implementation guidance.
- Grounds scoring in ground-truth target repositories via maximum fractional deviation of physical quantities, rather than judging code text.
- Adds an empirical-validation layer (likelihood, BIC, Hubble tension, CMB consistency) so a compiling implementation is not automatically a successful one.
- Deliberately disables the agent's web access: the launch command disallows the `WebSearch` and `WebFetch` tools, and the container overwrites web-access commands such as `ping` and `curl` so they pass through a network filter permitting only allowlisted domains.
- Supplies LLM-generated (`gemini-2.5-pro`) file maps of large CLASS modules so navigation cost does not dominate the task.

## Strengths

- The scoring protocol is quantitative and physics-grounded rather than rubric-based: numerical deviation from a reference implementation plus likelihood/BIC/tension rewards against real DESI, Planck, Pantheon+ and SH0ES data.
- The curated-description versus paper-source contrast produces an interpretable finding — the paper reports that working from papers rather than curated descriptions "significantly degrades numerical accuracy though qualitative behavior remains correct."
- The environment is a genuine executable task environment (containerized CLASS 3.3.0, patch-based submission) rather than a static question set.
- Hypothesis-generation stages extend the evaluation past implementation into open-ended model proposal, with the same empirical rewards applied to agent-invented models.

## Limitations

- Only two ground-truth cosmological models (Thawing Quintessence and Early Dark Energy) are evaluated, so the task pool is very small.
- Only one agent configuration is evaluated (Claude Code with `claude-sonnet-4-20250514`); there is no cross-model comparison, and the other LLMs mentioned serve as judge or summarizer rather than as evaluated agents.
- The framework is unnamed and the paper reports no public release of the environment, prompts or task specifications.
- The authors note that ground-truth implementations are "known to be public only for the EDE model," limiting external reproducibility of the TQ comparison.
- The authors note the agent-generated hypotheses "are of an empirical nature, and not related to the physical field properties of dark energy," and state that future work will add mechanisms avoiding empirical parametrisations.
- Repository note: this is a 5-page workshop paper; several protocol details (per-task budgets, prompt text, milestone definitions in full) live in appendices or are not reported.

## Related Works

- [ReplicationBench](./replicationbench.md) — Also scores agents on reproducing astrophysics research results from papers, with author-co-developed ground truth.
- [CosmoPaperQA](./cosmopaperqa.md) — Also targets cosmology, but evaluates retrieval-augmented question answering rather than codebase modification.
- [FEABench](./feabench.md) — Also requires an agent to drive a large scientific simulation codebase and is scored on numerical agreement with reference outputs.
- [Gravity-Bench-v1](./gravity-bench.md) — Also evaluates discovery of non-standard physics rather than recall of textbook results.
