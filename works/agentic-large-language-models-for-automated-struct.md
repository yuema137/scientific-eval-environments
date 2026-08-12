# Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems (2026)

> **English** | [简体中文](../zh/works/agentic-large-language-models-for-automated-struct.md)

## Overview

A benchmark of ten irregular 3D building-frame systems in which an agent must produce an executable SAP2000 script from a natural-language description, scored by whether every monitored structural response falls within 1% of a manually built ground-truth SAP2000 model.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.06525>
- **Venue:** arXiv preprint (cs.GR, cs.AI), v1 2 June 2026, v2 11 June 2026

## Summary

This work carries the same group's structural-modeling lineage from plane frames into 3D building systems, where topological consistency must hold both within each floor plan and across stories. Its first contribution is a representation: an irregular 3D frame is projected onto a 2D plan defined by orthogonal gridlines, and a matrix of number of stories (MNS) assigns an integer to each grid cell specifying how far that cell extrudes vertically, so voids, atria, and setbacks are expressible in a compact text form. A multi-agent pipeline then decomposes the frame floor by floor: node, girder, and slab agents run in parallel within each floor plan, a column agent connects adjacent floors, and support, load, and code-translation agents produce the final SAP2000 script. Two lightweight backbones are used — GPT-OSS 120B for spatial reasoning and Llama-3.3 70B Instruct Turbo for code translation. Unlike the earlier 2D work, correctness is judged against numerical structural responses rather than code executability.

## Tasks

Ten representative 3D frame systems with irregular geometric configurations, designed to cover three categories of complexity encountered in practice: height irregularity, plan asymmetry, and discontinuous layouts. Plan grids range from 3 × 3 to 4 × 6 cells, with the number of stories varying from 0 to 7 across cells. Representative configurations include stepped setbacks, internal voids, and asymmetric L-shaped, U-shaped, and cross-shaped plans; non-uniform grid spacing is also included to test generalization beyond regular grids. Each problem is expressed through the structured textual template: gridline positions, the matrix of number of stories, story heights, boundary conditions, loading, and material properties. Conditions other than geometry are held constant across all ten problems — all supports fixed at the base, a 10 kN/m² uniformly distributed area load applied downward on each slab as gravity loading, and 50 kN lateral point loads applied in the positive X direction at the top-floor nodes of each story on the left exterior façade to represent wind effects. Materials are linear elastic with E = 2 × 10¹¹ Pa, distinct section properties for girders and columns including torsional constants, and slabs modeled as thin shells of uniform 0.15 m thickness.

## Domains

Civil & Structural Engineering. The evaluated objects are 3D building frame systems — columns, girders, and floor slabs assembled across stories — under gravity and wind-representative lateral loading, and the graded outcome is the structural response of the resulting finite-element model. The irregularity taxonomy (height irregularity, plan asymmetry, discontinuous layouts) is the vocabulary of building structural engineering. No co-domain is assigned; SAP2000 is the instrument, not the evaluated objective.

## Evaluation

- Each of the ten benchmark problems is evaluated over ten repeated trials using the same input description. In each trial the agent produces a SAP2000 script, which is executed to obtain structural analysis results.
- Ground-truth SAP2000 models were manually constructed by the authors for every benchmark case. Responses from the generated model are compared against the ground-truth model at selected key locations, and a trial counts as accurate only when the relative errors of **all** monitored response quantities are below 1%. Per-problem accuracy is the ratio of accurate trials to total trials. The protocol therefore tests analytical correctness of the resulting model, not merely syntactic executability of the script.
- **Proposed agentic framework.** Accuracy exceeding 80% on every benchmark problem, averaging 90% across the ten problems with a variance of 0.007.
- **Baselines.** GPT-5.4 and Gemini-3.1 Pro, given the same input template and instructed to produce complete SAP2000 scripts, both achieve 0% accuracy on all ten problems, failing in every repeated trial. Failure analysis locates the first barrier at script import, where SAP2000 requires exact matching of predefined table names: GPT's scripts import successfully 4% of the time on average, Gemini's 47%. Even among importable scripts, geometric and topological consistency is not maintained across runs — GPT misreads an open-atrium configuration differently in different runs, and Gemini omits girder elements across floor plans.
- **Ablation** on the first three benchmark cases, ten trials each. Full framework: 90% / 80% / 90%. Without the floor decomposition agent: 30% / 50% / 20%. With node, girder, and slab agents merged into one in-plane geometry agent: 50% / 70% / 60%. With geometry translation and code compilation merged into a single script translation agent: 0% / 0% / 0%.
- **Runtime and cost** are reported alongside accuracy as an analysis-time comparison: the proposed framework averages approximately 175 s and USD 0.193 per case, against approximately 158 s and USD 0.306 for GPT-5.4 and approximately 386 s and USD 0.502 for Gemini-3.1 Pro. These are reported metrics, not budgets the agent must plan against.

## Typical Duration

Approximately 175 seconds and USD 0.193 per case on average for the proposed framework; approximately 158 s / USD 0.306 for GPT-5.4 and 386 s / USD 0.502 for Gemini-3.1 Pro. A complete SAP2000 script for a 3D frame can exceed one thousand lines, which the paper cites as the reason code translation cannot be handled in a single generation step.

## Main Contribution

The authors propose a structured geometric representation that makes irregular 3D frames expressible as unambiguous text, and an agentic pipeline built on it that decomposes long-horizon 3D structural modeling into floor-level subtasks with checkpoints. The accompanying ten-case benchmark, graded on numerical response agreement with hand-built reference models, is the evidence: frontier general-purpose models score zero on it while the decomposed lightweight pipeline averages 90%.

## Key Design Ideas

- The matrix of number of stories (MNS) over a gridline plan encodes vertical extrusion per cell, so a value of 0 denotes a void or atrium and irregular 3D topology reduces to a compact 2D table an LLM can parse reliably.
- Correctness is defined numerically — all monitored response quantities within 1% relative error of a manually constructed ground-truth SAP2000 model — rather than by script executability or geometric inspection.
- The 3D problem is decomposed into a stack of independent floor-level generation tasks and then reconstructed by connecting adjacent floors, bounding how much topology any single agent must hold at once.
- Node, girder, and slab agents run in parallel within a floor, with a deterministic connectivity mapping function converting coordinate-pair element definitions into node-ID connectivity afterwards.
- Checkpoints after the planning stage and after geometry assembly perform consistency checks (duplicate nodes, duplicate elements, dangling coordinates, unreferenced nodes) and trigger regeneration, capped at five attempts.
- Two different lightweight backbones are assigned by task type — GPT-OSS 120B for spatial reasoning agents, Llama-3.3 70B Instruct Turbo for translation agents — and the ablations test the decomposition boundaries rather than the model choice.

## Strengths

- The correctness criterion is the strongest in this lineage: agreement of the computed structural responses with a hand-built reference model, which catches scripts that execute and look plausible but model the wrong structure.
- The irregularity taxonomy is drawn from building engineering rather than from what is convenient to generate, and includes voids, setbacks, and L/U/cross-shaped plans with non-uniform grid spacing.
- The zero-versus-90% gap against GPT-5.4 and Gemini-3.1 Pro is diagnosed rather than merely reported, separating import failure, syntax failure, and run-to-run topological inconsistency.
- The ablation isolates each decomposition boundary and shows that merging translation and compilation collapses accuracy to zero on all three tested cases, which is a concrete result about long-horizon code generation limits.
- Reporting per-case runtime and dollar cost alongside accuracy makes the lightweight-backbone claim checkable.

## Limitations

- Ten problems is a small benchmark, and loading, boundary, and material conditions are identical across all of them, so only geometry varies.
- Only linear elastic static analysis is evaluated; no nonlinearity, dynamics, seismic response, or design decisions are covered.
- Ground-truth models are built manually by the authors, so the reference depends on their modeling choices, and the monitored response quantities and key locations are selected rather than exhaustive.
- The ablation covers only the first three of the ten cases.
- Two error modes remain in the proposed framework: incorrect section-property assignment during the long-context geometry translation step, and omitted or spurious load assignments.
- Repository note: no code or dataset release is stated in the paper, and SAP2000 is commercial software, so independent reproduction requires a licence.
- Repository note: runtime and cost are reported for comparison only; there is no budget the agent must plan against, so this is analysis-time rather than benchmark-time resource awareness.

## Related Works

- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — The direct predecessor, on plane frames with an OpenSeesPy target and code-level correctness.
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — The origin of this lineage, on 1D beams with reliability and robustness metrics.
- [StructureClaw](./structureclaw.md) — Also scores structural-engineering agents by numerical agreement with frozen reference solver responses.
- [FEABench](./feabench.md) — Also drives commercial finite-element software from natural language, through COMSOL's API.
- [MooseBench](./moosebench.md) — Also targets simulations that run but encode the wrong model.
