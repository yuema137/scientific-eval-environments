# A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis (2026)

> **English** | [简体中文](../zh/works/a-large-language-model-empowered-agent-for-reliabl.md)

## Overview

An eight-problem beam structural-analysis benchmark paired with two explicitly defined measures — reliability (fraction of correct outputs over repeated identical runs) and robustness (stability of that reliability as load position and boundary conditions vary) — used first to characterize a bare LLM and then an OpenSeesPy code-generating agent on the same problems.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.02938>
- **Venue:** Structure and Infrastructure Engineering (Taylor & Francis), published online 19 February 2026, pp. 1–16, <https://doi.org/10.1080/15732479.2026.2630123>

## Summary

The work asks how reliable and robust a state-of-the-art LLM is on structural analysis that demands exact numerical computation, and builds a small benchmark specifically to answer it. Eight statically determinate beam problems are constructed, and Llama-3.3 70B Instruct is sampled 500 times per problem configuration to measure reliability, then re-sampled across the full sweep of load positions to measure robustness. Finding that the model reasons qualitatively about statics but cannot be trusted quantitatively, the authors reframe the task from text generation to code generation and build an agent that emits OpenSeesPy code, executes it, and visualizes the result with OpsVis. The same benchmark and the same two measures are then applied to the agent, so the before/after comparison is made on identical ground.

## Tasks

Eight beam structural-analysis problems, each solved for the reaction forces at the supports — magnitudes and directions — of a statically determinate beam. Two canonical beam types are used, both of 10 m span: a simply supported beam and an overhang beam whose roller support sits at mid-span (5 m). Each beam type is paired with four load conditions: (I) a 10 kN point load; (II) a 10 kN/m uniformly distributed load over a 1 m segment; (III) a 10 kN point load combined with a full-span 10 kN/m distributed load; (IV) a 10 kN point load combined with a 1 m segment of 10 kN/m distributed load. Each problem is expressed as a textual prompt specifying geometry, support conditions, load conditions, and target outputs. Three additional extended beam problems — two overhang configurations with varied support locations and load directions, and a cantilever with a fixed support — are used as held-out generalization tasks and as the setting for the prompt-component ablation.

## Domains

Civil & Structural Engineering. The evaluated objective is a structural-mechanics decision on a load-bearing member: static equilibrium analysis of beams to obtain support reactions, with bending-moment and shear diagrams produced for the extended tasks. The paper positions the work explicitly within civil engineering and treats beam analysis as the foundational step before larger structural systems. No co-domain is assigned — OpenSeesPy is the means, not the evaluated objective.

## Evaluation

- **Reliability** = N_correct / N_total, with N_total = 500 independent runs of the same problem prompt. Prompt variants were screened in a preliminary step and the best-performing formulation was fixed before measurement.
- **Robustness** = (1 + CV)⁻¹ = (1 + σ_R / R̄)⁻¹, a normalized score in (0, 1] computed over the reliability values obtained as the load is moved along the beam in 1 m intervals from one end to the other; higher is more robust.
- **Reported for Llama-3.3 70B Instruct.** Simply supported beams: average reliability 87.1% under a point load and 93.6% under a localized distributed load, falling to 75.8% and 73.1% when a point load is combined with a full-length or a localized distributed load. Robustness for the four simply supported cases: 0.881, 0.952, 0.949, 0.937. Overhang beams degrade sharply once the load moves into the cantilevered region: robustness 0.577, 0.691, 0.588, 0.590, with reliability falling below 10.0% for the combined point-plus-full-length-distributed case.
- **Reported for the proposed agent.** Reliability above 0.990 and robustness above 0.996 across all benchmark conditions; the paper's conclusions state reliability exceeding 99.0% and robustness exceeding 99.6%. On the three extended generalization tasks, reliability of 100%, 99.8%, and 99.6% over 500 runs each.
- **Prompt-component ablation** (reliability on the three extended tasks; robustness in the last column). Full template: 1.000 / 0.998 / 0.996, robustness 0.998. Without the complete example: 0.000 / 0.000 / 0.000. Without function usage examples: 0.026 / 0.296 / 0.623, robustness 0.513. Without prescriptive constraints: 0.936 / 0.970 / 0.556, robustness 0.781. Without chain of thought: 1.000 / 0.998 / 0.784, robustness 0.882.

## Typical Duration

`N/A — the paper reports no per-task wall-clock, token, or cost budget.` Each measured configuration is sampled 500 times, so the reported statistics rest on a large repeated-sampling budget rather than on long individual trajectories.

## Main Contribution

The authors frame this as a first step toward assessing and enhancing the reliability and robustness of LLMs in structural engineering: constructing a benchmark for beam static-equilibrium analysis, showing that a state-of-the-art open-weight LLM has a qualitative grasp of structural mechanics but lacks the quantitative reliability and robustness that engineering practice requires, and demonstrating that reframing the task as code generation against a domain solver closes the gap.

## Key Design Ideas

- Repeated sampling is built into the metric rather than added as an error bar: reliability is defined over 500 independent runs of an identical prompt, so run-to-run inconsistency is what is measured.
- Robustness is a second, orthogonal axis defined over a systematic parameter sweep — the load is walked along the beam in 1 m steps — rather than over prompt paraphrases, so it tests sensitivity to the engineering configuration itself.
- The robustness score is normalized as the inverse of one plus the coefficient of variation, bounding it in (0, 1] and making it comparable across problems.
- The baseline and the proposed agent are measured on the same eight problems with the same two metrics, so the paradigm shift from text generation to code generation is isolated.
- The structured prompt template is decomposed into five named components (role specification, chain of thought, a complete example, function usage examples, prescriptive constraints), each of which is ablated separately.
- Generated OpenSeesPy code is executed automatically and the resulting model is rendered with OpsVis, giving axial-force, shear, and bending-moment diagrams that a human can check.

## Strengths

- The reliability/robustness pair is a sharper instrument than single-shot accuracy for a safety-relevant engineering task, and the 500-run sampling budget makes the reported curves stable.
- The load-position sweep exposes a failure mode a fixed test set would miss entirely: the bare model is fine when the load sits inside the supported span and collapses when it moves into the cantilevered region.
- The ablation is decisive rather than decorative — removing the complete example drops reliability to exactly zero on all three extended tasks, identifying which prompt component actually carries the performance.
- Extended generalization tasks use support types, support locations, and load directions absent from the benchmark and from the prompt examples.

## Limitations

- The benchmark is very small and deliberately elementary: eight problems over two beam types with a single span length, restricted to statically determinate static equilibrium. It does not touch indeterminate structures, frames, dynamics, or design.
- Only one model, Llama-3.3 70B Instruct, is characterized as a baseline; no closed-source or larger open-weight model is measured on the benchmark.
- The agent's residual errors are diagnosed qualitatively: hallucinating an extra roller support at the free end of a cantilever, and mis-extending the span of a distributed load when it is combined with a point load.
- The authors note the difficulty of specifying increasingly complex structures in text alone and point to vision-language models as future work.
- Repository note: no code or dataset release is stated in the paper, so the benchmark is reproducible only from the figures and problem descriptions in the text.
- Repository note: all statistics on this card were verified from the arXiv preprint (v1, 27 June 2025); the journal version of record was not accessible, and its numbers may have been revised in review.

## Related Works

- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — The same group's direct successor, extending the setting from 1D beams to 2D frames with a new 20-problem benchmark.
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — The same lineage extended to irregular 3D frames, scored on numerical response agreement rather than code executability.
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — An independent, contemporaneous OpenSeesPy structural-analysis benchmark that also measures run-to-run stability.
- [StructureClaw](./structureclaw.md) — Also evaluates agents on OpenSees-backed structural analysis, at workbench scale and with frozen reference solver responses.
- [FEABench](./feabench.md) — Also language-driven finite-element engineering, through COMSOL's API rather than OpenSeesPy.
