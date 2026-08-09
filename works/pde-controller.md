# PDE-Controller (2025)

> **English** | [简体中文](../zh/works/pde-controller.md)

## Overview

PDE-Controller brings LLMs to autoformalization and reasoning for PDE control: informal natural-language instructions are transformed into formal specifications (signal temporal logic), followed by reasoning and planning steps that improve the utility of PDE control for systems governed by heat and wave equations. Its datasets — human-written cases plus 2 million synthetic samples — and evaluation metrics constitute the benchmark component documented here.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.00963>
- **Code:** <https://github.com/delta-lab-ai/pde-controller>
- **Dataset:** <https://huggingface.co/datasets/delta-lab-ai/pde-controller>
- **Project:** <https://pde-controller.github.io/>
- **Venue:** ICML 2025 (per the official project page)

## Summary

PDE control asks not "what is the solution" but "what inputs make the system behave as specified." The paper builds the full pipeline — a Translator for natural-language-to-STL autoformalization, a Controller proposing STL subgoals, and a Coder emitting executable programs — and, for evaluation, releases human-written cases and 2 million synthetic samples with novel metrics over reasoning, autoformalization, and program synthesis, reporting up to a 62% improvement in utility gain for PDE control over baselines.

## Tasks

Autoformalization, reasoning, and program-synthesis tasks for PDE control of heat- and wave-equation systems; human-written cases plus 2M synthetic samples.

## Domains

Applied mathematics: control of PDE-governed systems (heat and wave equations) under signal-temporal-logic specifications.

## Evaluation

- Metrics over reasoning, autoformalization, and program synthesis; utility gain for the resulting PDE control; metric definitions are TODO(reference).
- **Reported.** Up to a 62% improvement in utility gain for PDE control.

## Typical Duration

Formalize-plan-synthesize pipelines per instruction; not an interactive environment.

## Main Contribution

Established datasets and metrics for LLM-driven PDE control — evaluating whether models can go from informal intent to formally specified, executable control of physical systems.

## Key Design Ideas

- STL as the intermediate representation makes control intent formally checkable.
- Utility gain scores the control outcome, not the text of the plan.
- Synthetic-scale data (2M) coexists with human-written cases for validity.

## Strengths

- The only PDE-control evaluation resource for LLMs documented here.
- ICML-accepted with released code and data.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The ICML 2025 venue is stated by the official project page; arXiv metadata carries no venue.
- Repository note: the PDE-Controller framework (Translator/Controller/Coder, RLHF-trained) is the paper's headline contribution and out of this repository's scope; the card documents the datasets and evaluation.

## Related Works

- [Lean4Physics](./lean4physics.md) — Also autoformalization-centered physics evaluation, into a proof assistant rather than temporal logic.
- [CodePDE](./codepde.md) — Also LLM code generation for PDE systems, for solving rather than controlling.
- [MaD Physics](./mad-physics.md) — Also interacts with PDE-governed simulated systems, for discovery rather than control.
