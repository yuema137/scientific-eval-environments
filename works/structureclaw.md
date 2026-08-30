# StructureClaw (2026)

> **English** | [简体中文](../zh/works/structureclaw.md)

> **First appeared:** 2026-07-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.14896)

## Overview

StructureClaw pairs a traceable LLM-agent workbench for structural engineering with an executable benchmark of 150 controlled scenarios spanning standard workflows, interactive robustness, and multimodal structural-model reconstruction, verified by strict structural-model matching and numerical agreement with frozen reference solver responses.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.14896>
- **Code:** <https://github.com/structureclaw/structureclaw>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.MA), 2026

## Summary

Agents operate an artifact-centered workbench — governed engineering skills, typed tools, shared artifact state, and local analysis backends (OpenSees among them, per the official repository) — carrying tasks from structural model through validation, solver execution, code checks, and reporting. A trial succeeds only when every fixture-required assertion passes: one-to-one structural-model matching plus numerical-response agreement with frozen reference responses; interactive cases additionally require positive clarification or recovery evidence, together with safe non-execution when appropriate. Across nine text-agent configurations, generic-only execution passes the model-artifact check 87.0% of the time but achieves only 22.0% end-to-end success, while the automatic StructureClaw configuration reaches 82.9%.

## Tasks

150 controlled structural-engineering scenarios in three families: standard workflows, interactive robustness (clarification/recovery/safe refusal), and multimodal structural-model reconstruction.

## Domains

Structural engineering: structural analysis workflows, model validation, solver execution, and code compliance checks.

## Evaluation

- Strict one-to-one structural-model matching plus numerical-response agreement with frozen reference solver outputs; all fixture assertions must pass (E2E Success); interactive cases require clarification/recovery evidence or safe non-execution.
- **Reported.** Generic-only execution: 87.0% model-artifact pass but 22.0% E2E Success; automatic StructureClaw: 82.9% across nine text-agent configurations.

## Typical Duration

Multi-step workbench sessions per scenario, including interactive clarification cases.

## Main Contribution

Shows that in safety-relevant engineering, producing a plausible model artifact (87%) and completing the engineering job correctly (22%) are wildly different claims — and that governed tooling closes most of that gap.

## Key Design Ideas

- Frozen reference solver responses make numerical agreement the arbiter, not judges.
- Safe non-execution is a scored correct behavior, importing refusal into engineering evaluation.
- Typed tools and shared artifact state leave an auditable trace of every step.

## Strengths

- The 87%-vs-22% artifact/E2E gap is a crisp warning against shallow success metrics.
- Real analysis backends rather than mock solvers.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: the StructureClaw workbench is a system contribution paired with the benchmark; the card documents the benchmark.

## Related Works

- [FEABench](./feabench.md) — Also language-driven finite-element engineering, through COMSOL's API.
- [Frontier-Eng](./frontier-eng.md) — Also real-world engineering evaluation under simulator feedback and hard constraints.
- [MooseBench](./moosebench.md) — Also verifies that generated simulation artifacts encode the intended physics.
