# A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis (2025)

> **English** | [简体中文](../zh/works/a-lightweight-large-language-model-based-multi-age.md)

> **First appeared:** 2025-10-06 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.05414)

## Overview

A benchmark of twenty 2D building-frame structural-analysis problems, each evaluated over ten independent trials, together with a five-agent Llama-3.3 70B pipeline that converts a textual frame description into executable OpenSeesPy finite-element code.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.05414>
- **Venue:** arXiv preprint (cs.CL), 6 October 2025

## Summary

Extending the same group's earlier beam work from 1D members to 2D frames, this paper builds a twenty-problem benchmark of multi-bay, multi-story plane frames and uses it to show that general-purpose LLMs cannot construct valid finite-element models of them. The proposed system decomposes the modeling task across five specialized agents — problem analysis, geometry, code translation, model validation, and load — all powered by the lightweight Llama-3.3 70B Instruct model. Its central design choice is a two-stage split in which geometric reasoning is resolved in natural language and emitted as a structured JSON topology before any code is written, so that the LLM performs a constrained translation rather than open-ended code generation. A deterministic, tool-based validation agent then deduplicates nodes and elements and renumbers identifiers before loads are applied.

## Tasks

Twenty distinct 2D frame structural-analysis problems, composed of vertical columns and horizontal girders. The set mixes topologies abstracted from real buildings with synthetically generated ones: the 3-2-3 frame (three stories in the first bay, two in the second, three in the third) is derived from Notre Dame de Paris, and the 3-4-3 frame is adapted from the Mollien Pavilion of the Louvre. Five problems are three-bay frames and fifteen are five-bay frames; for the five-bay frames the number of stories in each bay is sampled independently between one and five, producing irregular story profiles. All bays span 6 m. Boundary, load, and material conditions are held constant across the set: fixed supports along the base, a 10 kN/m uniformly distributed load applied downward along every beam, and a 50 kN point load applied rightward at the top of each story in the leftmost bay. Material parameters are fixed at E = 2 × 10¹¹ Pa, with distinct cross-sectional areas and moments of inertia for columns (2 × 10⁻³ m², 1.6 × 10⁻⁵ m⁴) and girders (6 × 10⁻³ m², 5.4 × 10⁻⁵ m⁴). Each problem is presented as a structured textual description covering geometry, boundary conditions, load conditions, and material properties.

## Domains

Civil & Structural Engineering. The evaluated objects are multi-bay, multi-story building frames — the paper frames them as the load-bearing skeleton of structures ranging from industrial plants to high-rise buildings — and the graded outcome is a valid finite-element model of that frame with its axial, shear, and bending responses. Two of the benchmark topologies are abstracted from real buildings. No co-domain is assigned; OpenSeesPy is the instrument, not the evaluated objective.

## Evaluation

- Each of the twenty problems is run over ten independent trials to account for LLM stochasticity. Accuracy is the proportion of correctly generated codes relative to the total number of runs.
- **Proposed multi-agent system (Llama-3.3 70B Instruct).** Accuracy over 80% in most cases. Three-bay frames are solved perfectly across all trials. Five-bay frames average 88% across the 15 problems, with the lowest results at 70% for the 2-4-3-2-5 and 2-3-3-2-5 frames and 60% for the 2-3-1-4-5 frame.
- **Vanilla Llama-3.3 70B Instruct baseline.** Fails on all twenty problems: every one of the ten runs terminates with syntax errors. The error-source distribution is element definition 61.0%, node definition 27.5%, support conditions 7.0%, material properties 4.5%. After syntax errors are manually corrected, the recovered geometries reveal deeper failures — a truss-like configuration with diagonal members instead of an orthogonal grid, duplicated nodes at bay intersections, and bays modeled as isolated entities with no shared nodes.
- **Gemini 2.5 Pro.** Average accuracy 37%, ranging from 90% down to 0% across problems. 88.5% of the 200 generated programs execute without runtime errors, so its failures are geometric rather than syntactic: omitted nodes, cross-connections between non-adjacent bays, and redundant stories.
- **ChatGPT-4o.** 0% across all ten trials for all twenty problems, with 89.0% of errors occurring at element definition, 6.5% at node definition, 2.5% at load application, and 2.0% at support conditions.
- An ablation merges the geometry agent and the code translation agent into a single integrated agent given the same prompts, isolating the contribution of separating geometric reasoning from code generation.

## Typical Duration

`N/A — the paper reports no per-task wall-clock, token, or cost budget.` Each problem is repeated over ten independent trials.

## Main Contribution

The authors present the benchmark and a lightweight multi-agent system as the step that carries LLM-driven finite-element modeling from 1D beams to 2D frames, where spatial reasoning and topological consistency become the binding constraints, and show that a decomposed pipeline built on an open-weight 70B model outperforms substantially larger general-purpose models on the task.

## Key Design Ideas

- The benchmark mixes real building topologies with randomly sampled story profiles, so irregular and asymmetric frames are represented rather than only regular grids.
- Loads, supports, and material properties are held identical across all twenty problems, isolating geometric topology as the variable under test.
- Geometric reasoning is decoupled from code generation through a structured JSON intermediate representation, so the LLM never has to resolve topology and syntax in the same step.
- The geometry agent follows a fixed deterministic assembly order — bay by bay from left to right, story by story from bottom to top — under four explicit expert-defined rules that state how many nodes and elements each step adds.
- The model validation agent is tool-based rather than generative: deterministic Python functions deduplicate nodes, deduplicate elements, renumber nodes, and renumber elements, and the agent only interprets their corrective actions.
- Failure analysis is reported as an error taxonomy by source (node, element, support, material) rather than as a single accuracy number, and geometry is inspected separately from syntax by manually repairing syntax errors before visualizing the recovered frames.

## Strengths

- The baseline spread is stark and informative: two frontier general-purpose models score 37% and 0% while a decomposed 70B pipeline exceeds 80% on most problems, which is a clear statement about where the difficulty lies.
- Separating syntactic validity from geometric correctness — and measuring both — catches the case where code runs cleanly but models the wrong structure.
- The benchmark proved reusable in practice: two later papers from the same group adopt this exact twenty-problem set as their evaluation testbed.
- OpsVis visualizations of geometry, load patterns, and internal-force diagrams give a human-checkable trace of what was actually modeled.

## Limitations

- Twenty problems is a small set, and the load, boundary, and material conditions are fixed across all of them, so only geometric topology varies.
- All frames are planar and elastic; no 3D systems, nonlinearity, dynamics, or design decisions are evaluated.
- Correctness is judged on the generated code and the resulting model rather than against an independently computed numerical reference for the structural responses.
- The system remains vulnerable where the assembly sequence is long and conditional rules fire frequently, dropping to 60% on the hardest five-bay frame.
- Repository note: no code or dataset release is stated in the paper.
- Repository note: two follow-up papers by the same group — a hallucination-reducing multi-agent architecture (arXiv 2603.07728) and a cross-platform OpenSees/SAP2000/ETABS variant (arXiv 2604.09866) — reuse this benchmark unchanged rather than extending it, so reported gains on these twenty problems accumulate against a fixed and now well-exposed target.

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — The same group's predecessor, on 1D beams with reliability and robustness metrics.
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — The same group's successor, extending to irregular 3D frames with a stricter numerical correctness criterion.
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — An independent 20-problem OpenSeesPy 2D frame benchmark from a different group.
- [StructureClaw](./structureclaw.md) — Also evaluates agents on OpenSees-backed structural analysis, with frozen reference solver responses and interactive robustness cases.
- [MooseBench](./moosebench.md) — Also checks that a generated simulation artifact encodes the intended model rather than merely running.
