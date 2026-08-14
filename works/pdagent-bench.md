# PDAgent-Bench (2026)

> **English** | [简体中文](../zh/works/pdagent-bench.md)

## Overview

PDAgent-Bench is a benchmark for evaluating LLM/VLM-based agents across the VLSI physical design stack, combining task-level assessment (conceptual and tool-centric problems) with workflow-level closed-loop execution in realistic Electronic Design Automation (EDA) environments.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities


- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.17253
- **Venue:** arXiv preprint (cs.AR), submitted June 15, 2026

## Summary

PDAgent-Bench targets the underexplored capability of language and vision-language models for VLSI physical design, which requires high-dimensional, multi-stage optimization under strict design constraints, coordinated interaction with EDA tools, and iterative refinement. The benchmark integrates a task-level suite of 353 curated problems — spanning conceptual questions and real-world industrial artifacts with expert-validated references and executable solutions — with a workflow-level agentic framework that enables closed-loop evaluation of holistic physical design flows. The authors evaluate 11 state-of-the-art models and report that while modern LLMs/VLMs are competitive on conceptual tasks, they remain substantially limited in tool-centric execution and long-horizon, multi-stage reasoning.

## Tasks

353 curated tasks across five capability dimensions (as reported in the paper):

- **Foundational Knowledge:** 90 tasks
- **Report Comprehension:** 11 tasks
- **Root Cause Analysis:** 21 tasks
- **Static Timing Analysis:** 11 tasks
- **Script Generation:** 210 tasks (Innovus: 90, ICC2: 88, ECO: 10, FM: 22)
- **Full-Flow Implementation:** 10 design projects

Tasks combine conceptual questions with real-world industrial artifacts. All questions and reference answers are independently reviewed by three domain experts, and all script-based solutions are validated through execution. Reported technology and tools: TSMC 28nm as the primary node and Nangate 45nm for an open-source flow; commercial EDA tools include Cadence Innovus 22, Synopsys IC Compiler II 2022, PrimeTime 2022, and Formal 2022, alongside the open-source OpenROAD flow.

## Domains

VLSI physical design / Electronic Design Automation — chip back-end implementation, including floorplanning, power planning, placement, clock tree synthesis, routing, static timing analysis, and engineering change order (ECO) work.

## Evaluation

Two-part evaluation. **Task-level:** pass@1 / pass@5 accuracy over the curated problems, with script-based solutions checked by execution and conceptual/analysis answers scored against expert-validated references. Reported headline numbers (for GPT-5.5) include 80.4% on Foundational Knowledge, 74.6% on Report Comprehension, 73.3% on Root Cause Analysis, 45.5% on ICC2 script generation, and 42.2% on Innovus script generation. **Workflow-level:** the PDAgent framework orchestrates specialized agents through a closed loop of planning, implementation, debugging, and optimization; full-flow execution is assessed by timing closure and DRC (design-rule) violation outcomes on representative designs (e.g., TinyRISCV, AES-256, Ethernet MAC), where the paper reports timing closure with zero or minimal DRC violations.

## Typical Duration

TODO(reference) — the paper does not state a per-task wall-clock or token budget. Full-flow implementation tasks span the multi-stage physical design flow (initialization, floorplanning, power planning, placement, clock tree synthesis, CTS optimization, routing, route optimization), which is long-horizon relative to the single-question conceptual tasks.

## Main Contribution

A comprehensive, multi-dimensional benchmark for LLM/VLM agents in VLSI physical design that unifies task-level assessment with workflow-level closed-loop execution, together with a human-aligned agentic physical design workflow framework (PDAgent). The authors report that human-skill-enhanced agentic workflows significantly improve end-to-end physical design performance.

## Key Design Ideas

- Splits evaluation into task-level assessment (conceptual + tool-centric problems) and workflow-level closed-loop execution in realistic EDA environments.
- Grounds tasks in real-world industrial artifacts with expert-validated references and executable reference solutions.
- Covers the tool-centric surface directly via script generation for multiple EDA tools (Innovus, ICC2), ECO, and formal verification (FM).
- Provides a multi-agent PDAgent framework that closes the loop over planning, implementation, debugging, and optimization across the physical design stages.
- Includes both commercial (TSMC 28nm; Innovus, ICC2, PrimeTime, Formal) and open-source (Nangate 45nm; OpenROAD) tool/technology settings.

## Strengths

- Targets a domain (VLSI physical design back-end) that the paper notes is significantly underexplored for LLM/VLM agents, in contrast to front-end design.
- Executable validation of script-based solutions and three-expert review of references support answer quality (paper).
- Evaluates a broad set of 11 models spanning proprietary and open-source families, enabling cross-model comparison.

## Limitations

- Reported script-generation accuracy remains low for tool-centric execution (e.g., 42.2% on Innovus for the strongest reported model), which the authors frame as a substantial limitation of current models rather than of the benchmark.
- Repository note: at the time of writing the paper states the benchmark and framework will be open-sourced "soon" but provides no public repository URL, so code/data availability is unverified.
- Repository note: the paper does not report per-task duration or token/compute budgets, limiting resource-aware comparison.

## Related Works

- TODO(reference) — related EDA/hardware-agent evaluations (e.g., AMS-circuit and ASIC-design agent benchmarks) may be linked once indexed.
