# Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering (2025)

> **English** | [简体中文](../zh/works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)

> **First appeared:** 2025-10-24 · **Source:** [Official publication record](https://doi.org/10.3390/data10110169)

## Overview

A published dataset and validation protocol in which GPT-4o answers structural-analysis prompts for reinforced-concrete frames twice — once as a bare language model and once as a tool-using agent that drives OpenSeesPy through a Model Context Protocol (MCP) server — with both sets of answers scored as relative error against manually built ETABS reference models.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://doi.org/10.3390/data10110169>
- **Code:** <https://doi.org/10.17632/gh9sbjzz5z.2> (Mendeley Data, `LLMS_MCP`, CC BY 4.0)
- **Venue:** *Data* (MDPI), Vol. 10, Issue 11, Article 169, 24 October 2025

## Summary

The work publishes the full record of a controlled comparison in structural analysis: four reinforced-concrete building frames are each analysed by GPT-4o in two configurations — unaided, and as a tool-using agent driving OpenSeesPy through a Model Context Protocol server — alongside a manually written OpenSees model and a commercial ETABS model that supplies ground truth. Every prompt, exchange, output and error metric is released under an open licence. The stated purpose is to separate probabilistic language generation from deterministic numerical computation and to document how far each configuration can be trusted in a safety-critical workflow.

## Tasks

Four study cases (A–D), each a three-dimensional reinforced-concrete building frame and each defined by a single structured prompt written in a five-part "CIDI" template (Context, Instructions, Details, Tasks, Intent). Case A is a 2-storey symmetric frame with 4.0 m spans in both directions; Case B a 3-storey asymmetric frame with variable spans; Case C a 5-storey symmetric frame with 4.0 m spans; Case D a 5-storey asymmetric frame with variable spans. The frames are designed under the Ecuadorian NEC-15 and U.S. ASCE 7-22 codes. Every case is analysed under four computational groups — GPT alone, GPT+MCP, manually written OpenSees, and ETABS — giving 16 analyses in total. Outputs that failed validation were logged and excluded from the curated dataset.

## Domains

Civil & Structural Engineering. The evaluated objective is the static and seismic response of reinforced-concrete building frames — inter-storey drift, maximum displacement, base shear and fundamental period — computed against design-code requirements, which is a structural-engineering analysis task rather than generic tool operation. No co-domain is claimed: the language-model and MCP machinery is the means, not the evaluated objective.

## Evaluation

Each analysis reports inter-storey drift in the X and Y directions (dimensionless ratios), maximum displacement (m), base shear (kN) and building period (s). Correctness is scored as relative error against the ETABS reference model, `|X_model − X_ETABS| / X_ETABS × 100%`, applied to each reported quantity. Reported outcome: the GPT-only configuration produces relative errors of roughly 230–270% with large dispersion, while GPT+MCP and manual OpenSees stay below 1.427%.

## Typical Duration

End-to-end runtime of 6–12 seconds per GPT+MCP analysis, compared with approximately 12–15 minutes for the manual ETABS route reported by the authors.

## Main Contribution

The authors present a curated, openly licensed dataset that records the full natural-language-to-solver exchange for building static analysis, together with the error metrics needed to judge it, and frame it as a reproducible methodology for integrating generative AI into safety-critical structural workflows by separating probabilistic language generation from deterministic numerical computation.

## Key Design Ideas

- The Model Context Protocol is used as the bridge: a FastAPI server converts the model's natural-language output into a structured JSON schema that drives OpenSeesPy 3.8.x (OpenSees 3.7.1).
- The bare-LLM condition is retained as a deliberate control, so the dataset measures the effect of grounding the model in a solver rather than only the accuracy of the grounded pipeline.
- Ground truth comes from an independent commercial tool (ETABS 20.3.0) rather than from the same solver the agent drives.
- The prompt is fixed to one structured template across all four cases, so differences between cases come from the structure, not from prompt engineering.
- Four frames span two storey counts and both symmetric and asymmetric plan configurations, and are designed under two different seismic codes.

## Strengths

- Ground truth comes from an independent commercial package (ETABS) rather than from the same solver the agent drives, so the reference is not circular.
- The bare-LLM control condition is retained rather than discarded, which is what makes the roughly 230–270% versus under-1.427% error gap interpretable as an effect of solver grounding.
- The artifacts are openly licensed and include the prompts, exchanges, outputs and error metrics, so the comparison can be recomputed rather than taken on trust.
- Runtime is reported alongside accuracy (6–12 seconds versus 12–15 minutes for the manual route), making cost an explicit second axis.
- A fixed prompt template across all four cases isolates structural difficulty from prompt engineering.

## Limitations

- Very small scale: four frames, four prompts and 16 analyses in total, all of the same structural type (reinforced-concrete moment frames), which limits the range of structural behaviour probed.
- A single language model (GPT-4o) is exercised, so the dataset does not support cross-model comparison as released.
- Only the end result is scored; no trajectory, intermediate-step or tool-call-level scoring is defined.
- The paper reports no limitations or user-notes section of its own.
- Repository note: the published abstract describes the dataset as including "150+ prompts", while the body states that each of the four study cases is defined by a single CIDI-style prompt and that the total is 16 analyses. The card follows the body.
- Repository note: this is a data descriptor accompanying a separate study rather than a benchmark suite designed for open leaderboard-style use; reuse as an evaluation set is possible but is not the stated framing.

## Related Works

- [Integrating Large Language Models for Automated Structural Analysis](./integrating-large-language-models-for-automated-st.md) — also scores LLM-generated OpenSeesPy analyses against reference structural solutions.
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — same OpenSeesPy code-generation setting, on 2D frames with repeated trials.
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — compares a bare LLM with a solver-backed agent on the same structural problems.
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](./agentic-large-language-models-for-automated-struct.md) — 3D frame analysis scored against a commercial-tool ground truth (SAP2000).
