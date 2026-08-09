# FEABench (2025)

> **English** | [简体中文](../zh/works/feabench.md)

## Overview

FEABench evaluates whether LLMs and LLM agents can simulate physics, mathematics, and engineering problems end to end using finite element analysis (FEA): reasoning over a natural-language problem description and operating COMSOL Multiphysics® through its API to compute the answer.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.06260>
- **Code:** <https://github.com/google/feabench>
- **Venue:** NeurIPS 2024 Workshops on Mathematical Reasoning and AI, and Open-World Agents

## Summary

FEABench treats professional simulation software as the evaluation surface: solving a task means driving COMSOL Multiphysics® through API calls, not producing a closed-form answer. The paper additionally designs an agent that interacts with the software through the API, examines its outputs, and uses tools to improve its solutions over multiple iterations. The best-performing strategy generates executable API calls 88% of the time.

## Tasks

Multiphysics problems specified in natural language and solved end to end by operating COMSOL Multiphysics® through its API; the agentic setting iterates on API calls against software feedback. Exact task counts are TODO(reference).

## Domains

Multiphysics simulation via finite element analysis, spanning physics, mathematics, and engineering problems.

## Evaluation

- A comprehensive evaluation scheme over generated API calls and computed answers; executability of generated API calls is a headline metric.
- **Reported.** The best-performing strategy generates executable API calls 88% of the time.

## Typical Duration

Iterative interact-examine-improve loops against the FEA software; per-task budgets are TODO(reference).

## Main Contribution

Moves physics-simulation evaluation onto real professional software: competence is measured as the ability to operate an industry FEA tool end to end, not to imitate its output.

## Key Design Ideas

- The software API is the action space, so evaluation captures tool operation, not just physics knowledge.
- Iterative refinement against software outputs makes the setting agentic rather than one-shot code generation.
- Executability of API calls provides an objective, automatically checkable progress signal.

## Strengths

- Real industrial simulation software rather than a purpose-built sandbox.
- The 88% executability versus much harder end-to-end solving exposes where the difficulty actually lives.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — Also evaluates operating professional simulation software (OpenFOAM), with physics-grounded convergence checks.
- [Frontier-Eng](./frontier-eng.md) — Also loops agents against industrial-grade simulators under interaction budgets.
- [SimulCost](./simulcost.md) — Also physics-simulation evaluation, focused on parameter tuning under resource costs.
