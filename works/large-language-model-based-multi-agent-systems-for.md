# Large Language Model-Based Multi-Agent Systems for Automated Foundation Design (2026)

> **English** | [简体中文](../zh/works/large-language-model-based-multi-agent-systems-for.md)

> **First appeared:** 2025-06-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2506.13811)

## Overview

A 27-case foundation-design evaluation protocol for geotechnical engineering — shallow footings and piles — paired with a four-criterion grading rubric and used to compare nine configurations of standalone LLMs, sequential agentic workflows, and a router-driven multi-agent system that classifies an incoming design problem and dispatches it to a specialist agent.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://doi.org/10.1007/s43503-026-00088-8>
- **Preprint:** <https://arxiv.org/abs/2506.13811> — circulated under the title "Investigating the Potential of Large Language Model-Based Router Multi-Agent Architectures for Foundation Design Automation: A Task Classification and Expert Selection Study"
- **Venue:** AI in Civil Engineering (Springer), volume 5, 2026

## Summary

The authors observe that reviews of LLM use in construction engineering find essentially no work applying LLMs to the fundamental engineering calculations at the core of practice, and that the geotechnical studies that do exist rely on retrieval-augmented monolithic agents validated on narrow shallow-foundation datasets. They build a router-based multi-agent workflow in which a dual-tier classifier first separates pile from shallow-foundation problems and then routes to a per-calculation expert agent, followed by a technical reviewer and a senior engineer agent that produce a final engineering report. To evaluate it they define a 27-case test protocol spanning seven categories of foundation design problems, a four-dimension grading rubric that scores calculation accuracy alongside reasoning quality, complex-scenario handling, and output structure, and a triple-trial execution regime to expose run-to-run variability. Nine configurations are compared under this protocol: four standalone frontier LLMs, two conventional sequential agentic workflows instantiated on two different base models, and the proposed router system on those same two base models.

## Tasks

27 distinct test cases spanning seven primary categories of geotechnical engineering problems. Shallow-foundation analysis contributes 15 test cases covering dimensional design calculations, allowable load determinations, bearing capacity computations, and settlement analysis. Pile-foundation evaluation contributes 12 test cases across four specialized categories: dimensional design calculations, bearing capacity analysis including skin friction and ultimate bearing capacity, settlement computations for prestressed concrete piles, and pile group analysis encompassing load distribution and elastic settlement behavior. Cases are posed as short professional design prompts with the soil profile, loading, and safety factors given — for example, finding footing dimensions B × L to carry a wind-induced moment given dead and live loads, an allowable soil pressure and a factor of safety, or computing ultimate skin friction and allowable bearing capacity for a 15 m concrete pile of 0.45 m × 0.45 m cross-section embedded in sand. Results are reported against per-criterion columns: Finding Dimensions, Allowable Load, Bearing Capacity, Settlement, and Factor of Safety for the shallow-foundation set, and Finding Dimensions, Bearing Capacity, Settlement, and Pile Group for the pile set. Each test case is executed three times to account for LLM stochasticity. The test cases are described in the paper but not released as a public dataset.

## Domains

Civil & Structural Engineering, in its geotechnical branch. The evaluated objective is a foundation design result — footing dimensions, ultimate and allowable bearing capacity, immediate and consolidation settlement, factor of safety, pile group efficiency and load distribution — computed under established design procedures (Terzaghi's bearing capacity theory and its shape and depth factor extensions for shallow foundations, Vesic's method for pile end-bearing and skin friction) and framed throughout as safety-critical civil engineering practice requiring professional oversight. No co-domain is assigned: soil mechanics enters only as the mechanics of the foundation being designed, and LangChain, n8n, OpenRouter and SerpAPI are the instruments rather than the evaluated objective.

## Evaluation

- **Grading rubric.** Four criteria, each scored on a four-point scale — Excellent 2.0, Good 1.0, Needs Improvement 0.5, Poor 0.0. The criteria are (1) Accuracy of Calculations, covering bearing capacity, slope stability and foundation design results; (2) Chain-of-Thought Reasoning, whether the model explains how it arrives at each calculation or design decision and whether the logic is complete; (3) Handling Complex Scenarios, robustness on non-standard boundary conditions and multifaceted problems; and (4) Consistent and Structured Output Format, whether inputs, calculations and final results are presented in a consistently structured way. Scores are reported as a percentage grade per criterion and averaged.
- **Protocol.** Triple-trial execution per test case under identical input conditions, isolating model randomness. Reported indicators include numerical accuracy, output format consistency, computational methodology validity, and frequency of invalid outputs.
- **Ablation over architecture.** Three workflow configurations are compared: the full router system; Agentic Workflow I, which removes the router subsystem leaving a static sequential Designer → Reviewer → Senior Engineer pipeline; and Agentic Workflow II, which adds an iterative refinement loop giving the Reviewer authority to reject or request revisions.
- **Shallow-foundation results (average grade).** Proposed router with Grok 3, 95.00%; standalone Grok 3, 86.25%; proposed router with Gemini 2.5 Pro, 82.50%; DeepSeek R1, 77.50%; Agentic Workflow II with Grok 3, 73.75%; Gemini 2.5 Pro-preview and Agentic Workflow I with Grok 3, 71.25%; Agentic Workflow II with Gemini 2.5 Pro, 72.50%; ChatGPT 4.0-turbo, 58.75%; Agentic Workflow I with Gemini 2.5 Pro, 38.75%.
- **Pile-foundation results (average grade).** Proposed router with Grok 3, 90.63%; standalone Grok 3, 87.50%; proposed router with Gemini 2.5 Pro, 84.38%; Gemini 2.5 Pro-preview, 81.25%; DeepSeek R1 and ChatGPT 4.0-turbo, 75.00%; Agentic Workflow II with Grok 3, 62.50%; Agentic Workflow II with Gemini 2.5 Pro, 56.25%; Agentic Workflow I with Gemini 2.5 Pro and with Grok 3, 51.56%.
- **Headline comparisons.** The router configuration improves on standalone Grok 3 by 8.75 percentage points on shallow foundations and 3.13 on piles, and exceeds the conventional sequential workflows by margins of 10.0 to 43.75 percentage points. It reaches 100% on Pile Group analysis with both base models, where the conventional workflows score 50.00–68.75%.
- Who applies the rubric — human expert graders or an automated judge — is not stated in the paper: `TODO(reference)`.

## Typical Duration

N/A — no trajectory length, wall-clock time, or token budget per test case is reported. The only protocol-level quantity given is three independent executions per test case.

## Main Contribution

The authors present what they describe as the first router-based multi-agent system designed specifically for foundation engineering, with intelligent task classification and expert selection, and alongside it a multi-dimensional evaluation methodology for AI models in geotechnical engineering that scores calculation accuracy, chain-of-thought reasoning, complex-scenario handling, and structured output consistency over 27 test cases with triple-trial execution. They argue that accuracy metrics alone are a dangerously incomplete assessment in safety-critical geotechnical applications, because a correct final number can emerge from flawed reasoning.

## Key Design Ideas

- Dual-tier classification: a first stage separates pile from shallow-foundation problems, because the two require fundamentally different analytical approaches, and a second stage routes to the specific calculation expert (pile length, pile bearing capacity, pile settlement, group pile; or foundation dimensions, bearing capacity, settlement, factor of safety, allowable load).
- The calculation methodology is embedded in each agent's system prompt rather than retrieved, so an engineer can specify a preferred design approach or a local design code by editing the prompt; the paper reproduces the shallow-foundation and pile system prompts in full.
- Deliberate rejection of RAG: the authors argue retrieval couples performance to document segmentation quality, suffers semantic drift across engineering terminology, degrades on novel problem types, and cannot distinguish superseded from current design codes.
- One-shot worked examples inside each expert prompt, with an explicit instruction to avoid hedging phrases such as "it depends" or "consult a table" and to state what additional data would be required if the problem is underspecified.
- A two-stage quality-assurance tail mirroring professional practice: a Technical Reviewer agent that checks calculations against design codes, assigns a 1–10 quality score, and states PASS or REQUIRES REVISION, followed by a Senior Engineer agent that formats the final engineering report.
- Web search (SerpAPI) is available to agents for retrieving current standards, rather than a fixed knowledge base.
- The evaluation rubric scores reasoning quality and output structure as first-class dimensions beside numerical accuracy.

## Strengths

- The evaluation covers both shallow and deep foundations, whereas the prior geotechnical LLM studies the paper reviews are confined largely to shallow footings.
- The rubric is published in full with explicit level descriptors for each of the four criteria, so the grading standard is inspectable.
- Architecture is ablated rather than only compared to standalone models: removing the router and removing the refinement loop are tested separately, isolating the routing contribution.
- Triple-trial execution addresses run-to-run variability instead of reporting single-run scores.
- Per-criterion results are reported for every configuration, exposing where each model is weak (for example Grok 3's strength on Finding Dimensions against its weakness on Factor of Safety).
- The paper states plainly that the system is a computational assistance tool requiring continued human oversight, not an autonomous design replacement.

## Limitations

- The authors state that the 27-case, seven-category test set is a significant limitation, representing only a fraction of the scenarios met in professional geotechnical practice.
- The test cases are not released as a dataset and the evaluation set is not given a name, so results cannot be reproduced independently or compared across papers.
- Repository note: the rubric's non-accuracy dimensions (reasoning quality, complex-scenario handling, output structure) are qualitative judgments, and the paper does not report who graded, how many graders were used, or any inter-rater agreement.
- Repository note: the router system and the baselines are graded by the same rubric, but the router's own pipeline contains a Reviewer agent that assigns a quality score and can trigger revision, so the compared configurations differ in inference-time compute as well as in architecture; the paper reports no cost, latency, or token accounting.
- Repository note: the paper reports a variance-reduction motive for triple trials but does not publish per-trial spreads or variance statistics, only averaged grades.

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — the same pattern of a small purpose-built civil-engineering problem set used to measure run-to-run reliability of an LLM agent.
- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — a hand-curated structural-analysis problem set used to compare LLMs inside an engineering framework, cited by this paper as prior work.
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — the structural-analysis counterpart of the multi-agent decomposition used here.
- [PE Civil Bench](./pe-civil-bench.md) — civil-engineering licensure problems paired with an agentic reinforced-concrete design pipeline, covering the structural side of the same design-calculation question.
