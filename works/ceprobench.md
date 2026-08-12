# CeProBench (2026)

> **English** | [简体中文](../zh/works/ceprobench.md)

## Overview

CeProBench is a chemical-process-development benchmark introduced alongside CeProAgents, a hierarchical multi-agent system for automated chemical process development. The benchmark organizes evaluation around three pillars of chemical engineering — knowledge, concept, and parameter — with six task classes spanning document-to-knowledge-graph extraction, process flow diagram (PFD) parsing and design, and Aspen Plus parameter optimization.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.01654>
- **Code:** <https://github.com/kronos7777777/CeProAgents>

## Summary

The paper proposes CeProAgents, a hierarchical multi-agent system whose three agent cohorts target knowledge, concept, and parameter aspects of process development, each combining dynamic agent chat groups with structured agentic workflows. To evaluate the system, the authors construct CeProBench, a multi-dimensional benchmark built around the same three pillars, with six distinct task types intended to assess process-development capability end to end. The reported results are framed both as evidence for the proposed architecture and as a measurement of the current boundaries of large language models on industrial chemical engineering tasks.

## Tasks

CeProBench comprises 6 task classes spanning "a total of 243 questions and 235 specific tasks." The six task types are Knowledge Extract (turning unstructured technical literature into formalized knowledge graphs), Knowledge Augment (retrieving and synthesizing specialized context for engineering scenarios), Concept Parse (digitizing process flow diagrams into semantic graphs), Concept Complete (inferring missing unit operations from underspecified topologies), Concept Design (generating PFDs from natural-language descriptions), and Parameter Optimize (closed-loop refinement of operating parameters).

Construction differs per dimension. The Knowledge dimension draws on a curated corpus of 70 core technical documents, from which 4,406 entities and 4,967 relations were extracted, stratified over process route selection, catalyst selection, production methods, and separation techniques. The Concept dimension uses 113 PFDs derived from the National College Student Chemical Design Competition, annotated with topological structure and containing 986 equipment units and 1,172 connections. The Parameter dimension is built from 20 high-fidelity Aspen Plus backup files paired with structured constraint descriptions, covering 91 adjustable parameters and 65 optimization objectives.

## Domains

Chemical Engineering. Every dimension is a process-systems-engineering task: literature on process routes, catalysts, production methods and separation techniques; process flow diagram parsing, completion and design; and operating-parameter optimization validated inside Aspen Plus. Chemistry appears only as background subject matter for the process knowledge — the evaluated objectives are process design and plant-operating decisions, not molecular or reaction prediction.

## Evaluation

Scoring is dimension-specific. The Knowledge dimension combines reasoning-quality judgments along Correctness, Rationality, Clarity, and Completeness with graph-integrity measures — entity F1, recall, and accuracy, plus a Mapping-based Edge Connectivity (MEC) and Mapping-based Edge Distance (MED) for the extracted graph structure. The Concept dimension scores parsing with equipment and connection accuracy and recall against expert annotations, completion with Top-K accuracy against ground-truth unit operations, and design with a Valid Rate and a Correct Rate reflecting engineering-logic validation. The Parameter dimension is scored by executing candidate parameter settings in Aspen Plus, which validates chemical and thermodynamic feasibility, and aggregating yield, purity, cost, an Effective Score, and a Comprehensive Score, alongside convergence efficiency measured as total iterations versus the iteration reaching the best result.

Five foundation models are evaluated: Gemini-3.0-Pro, GPT-5.0, Claude-4.5-Opus, Qwen-3.0-Max, and DeepSeek-V3. Gemini-3.0-Pro is reported as the strongest across most dimensions.

## Typical Duration

TODO(reference) — the paper does not report per-task wall-clock time, trajectory length, or token budgets. For the Parameter dimension it reports convergence efficiency in optimization iterations (total iterations versus the iteration at which the best result is reached) rather than a time or token budget.

## Main Contribution

In the authors' framing, the contributions are CeProAgents — a hierarchical multi-agent system that decomposes chemical process development into knowledge, concept, and parameter cohorts, each using a hybrid of dynamic agent chat groups and structured agentic workflows — and CeProBench, a multi-dimensional benchmark structured around three core pillars of chemical engineering with six task types designed to assess process-development capability holistically.

## Key Design Ideas

- Three-pillar decomposition of chemical process development (knowledge, concept, parameter) used symmetrically for both the agent architecture and the benchmark.
- Six task types that span the development pipeline rather than a single question format: knowledge-graph extraction, retrieval-augmented knowledge synthesis, PFD parsing, topology completion, PFD generation, and closed-loop parameter optimization.
- Simulator-grounded scoring for the Parameter dimension: candidate operating parameters are executed in Aspen Plus so that chemical and thermodynamic feasibility, not text similarity, determines the score.
- Graph-structured ground truth for both knowledge (entities/relations) and concept (equipment units/connections), enabling structural metrics such as entity F1, MEC/MED, and connection accuracy.
- PFD tasks sourced from a national chemical design competition rather than synthesized, so topologies reflect industrial-style design practice.

## Strengths

- Covers the process-development workflow end to end rather than testing isolated question answering, with six task types across three declared dimensions.
- Execution-grounded evaluation in Aspen Plus for the parameter tasks gives an objective feasibility check that text-only grading cannot provide.
- Reports the scale of each dimension explicitly (70 documents, 4,406 entities / 4,967 relations; 113 PFDs with 986 equipment units and 1,172 connections; 20 parameter files with 91 adjustable parameters and 65 objectives).
- Knowledge and Parameter datasets are released publicly in the project repository, together with the CeProAgents code.

## Limitations

- The Concept-dimension data derived from the National College Student Chemical Design Competition is not publicly released; the paper states it is available from the corresponding author upon reasonable request, which limits full reproducibility of that third of the benchmark.
- Parameter-dimension evaluation depends on a licensed Aspen Plus installation, so the environment is not freely reproducible.
- Absolute scale is modest — 243 questions and 235 tasks across six task types, and only 20 parameter scenarios — relative to the breadth of the three declared dimensions.
- Several Knowledge-dimension criteria (Correctness, Rationality, Clarity, Completeness) are graded judgments rather than execution-verified outcomes.
- Repository note: the benchmark is introduced inside a system paper whose primary claim is the CeProAgents architecture, so the reported numbers are produced under the authors' own agent scaffolding rather than a scaffold-independent harness.

## Related Works

- [FEABench](./feabench.md) — engineering evaluation grounded in driving a commercial simulator through its API, the same execution-verified pattern as the Parameter dimension.
- [CFDLLMBench](./cfdllmbench.md) — multi-tier engineering-simulation benchmark spanning domain knowledge through end-to-end simulator configuration.
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — chemical-engineering evaluation focused on thermodynamics problem solving rather than process development.
- [Simona](./simona.md) — evaluates automated conversion of process descriptions into converging simulation flowsheets, overlapping with the Concept and Parameter dimensions.
