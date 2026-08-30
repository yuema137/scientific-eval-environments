# CRAFTS (2026)

> **English** | [简体中文](../zh/works/crafts.md)

> **First appeared:** 2026-08-02 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.01369)

## Overview

CRAFTS is a role-decomposed, fine-tuned LLM-agent system for automated construction of executable chemical-process simulation models, introduced together with OpenIDAES-450, a 450-case IDAES process-simulation dataset with a held-out evaluation split and structured validation contracts.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.01369
- **Code:** https://github.com/Galigeigei-Z/CRAFTS-Multi-agent-for-Equation-oriented-PSE

## Summary

CRAFTS (Collaborative Role-Adaptive Fine-Tuning of LLM Agents for Chemical Process Simulation) builds executable IDAES/Pyomo process-simulation models from natural-language requests and process flowsheet diagram (PFD) evidence. The task is decomposed into seven bounded roles that mirror the staged workflow of chemical engineers, with deterministic IDAES/Pyomo gates validating typed intermediate artifacts between stages. The work is evaluated on OpenIDAES-450, a 450-case IDAES process-simulation dataset introduced by the same paper, using a workflow-success contract and structural F1 metrics on a frozen held-out split.

## Tasks

OpenIDAES-450 contains 450 user-facing chemical-engineering requests paired with executable IDAES process models, intermediate artifacts, and execution records. Cases span unit-operation selection, topology construction, property-package assignment, specification closure, initialization, recycle handling, solver diagnosis, and optimization. 82 requests are frozen as the held-out test set used for all reported evaluations; the remaining 368 are used only for training and development, with cases from the same source model or template kept in the same split and duplicates removed. Each task requires constructing an executable process model from a natural-language request plus PFD evidence, with the pipeline emitting typed intermediate representations along the way — VisualGraphIR, TopologyIR, SpecIR, BuildPlan, and SolveReport. TODO(reference) — the paper does not state the original provenance of the 450 cases beyond describing them as curated and auditable.

## Domains

Chemical Engineering — the evaluated objective is automated construction of executable chemical-process simulation models (flowsheeting) in IDAES/Pyomo, a process systems engineering task centered on unit operations, streams, and process topology.

## Evaluation

Scoring combines a Workflow Success (WS) contract — the percentage of requests that pass every required stage, covering interpretation, topology validation, specification closure, BuildPlan compilation, model construction, initialization, accepted solver termination, and optional optimization — with three macro-F1 structural metrics against the reference model: unit records (UC), stream records (SC), and directed connection pairs (CC). Promotion gates between stages enforce schema validity, entity consistency, connectivity, port compatibility, unit availability, property-package support, degrees-of-freedom closure, initialization, solver termination, and physical consistency. On the frozen 82-request split CRAFTS reports 91.5% WS with UC/SC/CC F1 of 0.815 / 0.791 / 0.782, above reimplemented prior-system baselines (CeProAgents-style 74.4% WS, Sketch2Simulation-style 76.8%, Text-to-Simulation-style 68.3%), an OpenAI Agents SDK pipeline (79.3%), and single-model baselines (GPT-5 mini 54.9%, Claude Sonnet 4.6 45.1%, Gemini 3.5 Flash 28.0%). Ablations remove role-specific fine-tuning (36.6% WS), chemical-engineering knowledge (0%), visual evidence (25.6%), topology–specification separation (30.5%), and Debug replay (18.3%).

## Typical Duration

TODO(reference) — the paper reports no per-task wall-clock time, token budget, or step count; the only related figure is that 75 of the 82 held-out cases required at least one debugging interaction.

## Main Contribution

A collaborative, role-adaptive fine-tuning approach that splits chemical-process model construction across seven bounded LLM-agent roles with typed intermediate representations and deterministic IDAES/Pyomo engineering gates, introduced together with OpenIDAES-450 and a workflow-success-plus-structural-F1 evaluation protocol on a frozen held-out split.

## Key Design Ideas

- Decompose process-model construction into seven bounded roles — Input Understanding, Intent, Visual, Topology, and Specification specialists, plus Debug and Optimization — orchestrated as a LangChain/LangGraph workflow.
- LoRA fine-tune only the three schema-critical roles (Visual Descriptor on Qwen3-VL-8B-Instruct; Topology and Specification agents on Qwen2.5-Coder-7B-Instruct), leaving the other four roles as untuned locally deployed Qwen with knowledge-informed prompting.
- Insert deterministic IDAES/Pyomo promotion gates between stages so intermediate artifacts are validated before proceeding.
- Represent engineering decisions through typed intermediate representations (VisualGraphIR, TopologyIR, SpecIR, BuildPlan, SolveReport), attaching constructors, property packages, and runners only after semantic artifacts pass the gates.
- Score with a staged workflow-success contract plus unit/stream/directed-connection F1 rather than a single end-to-end pass/fail signal.
- Freeze an 82-request held-out split and assign cases sharing a source model or template to the same split to limit leakage.

## Strengths

- Contributes a named dataset (OpenIDAES-450) with a frozen held-out split and a defined scoring protocol, not just a system demonstration.
- Grounds evaluation in an executable simulator (IDAES/Pyomo), so validation reflects whether constructed models actually build, initialize, and solve.
- Structural metrics on units, streams, and directed connections expose where model construction fails beyond an aggregate success rate.
- Compares against reimplementations of prior process-simulation agent systems, a general agent SDK pipeline, and single-model baselines, and includes five ablations isolating fine-tuning, domain knowledge, visual evidence, role separation, and debug replay.

## Limitations

- The benchmark is single-simulator: all tasks target IDAES/Pyomo equation-oriented models, so results do not speak to sequential-modular simulators such as Aspen Plus or HYSYS.
- Repository note: the public repository provides only an architecture preview and states that source data, benchmark records, model weights, and evaluation references are withheld pending a later release, so OpenIDAES-450 is not independently reusable as of this card.
- Repository note: the prior-system baselines are "-style" reimplementations by the authors rather than the original released systems, which weakens the comparison.
- Repository note: no runtime or token-cost accounting is reported, so the cost of the seven-role pipeline relative to single-model baselines cannot be assessed.

## Related Works

- [FEABench](./feabench.md) — LLM agents constructing and running engineering simulations against a numerical solver.
- [MooseBench](./moosebench.md) — agent evaluation on setting up executable multiphysics simulations.
