# Earth Science

> **English** | [简体中文](../zh/domains/earth_science.md) · [← All domains](./README.md)

## Scope

Geosciences: atmospheric, ocean, and geological sciences. GIS and geospatial analysis fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | Environmental geospatial analysis over Spain and Portugal through structured tool calls to a production-style API serving three environmental indicators via 16 tools. | 93 tasks in 18 categories: municipality analysis, spatial reasoning, cross-indicator synthesis, multilingual queries, and deliberately unsolvable tasks that must be declined. | Eight mechanistic checks per case — expected tool calls, required/forbidden keywords, numeric tolerance (±2 pp), chart production, round budget — with no LLM judge. | [→](../works/geonatureagent-benchmark.md) |
| ScienceAgentBench | 2024 | Geographical Information Science tasks — 27 of its 102 — extracted from peer-reviewed data-driven discovery workflows. | Each task requires generating a self-contained Python program reproducing an analysis from a real publication. | Valid execution plus task-specific hand-written success checkers against expert-annotated references; figure outputs judged by GPT-4o. | [→](../works/scienceagentbench.md) |
| Terminal-Bench Science | 2026 | Atmospheric, environmental, geo-, and ocean science tasks in the Earth Sciences track of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Earth is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| HydroAgent | 2026 | Calibrate the operational CREST distributed hydrologic model used by the U.S. National Weather Service for flash-flood forecasting. | Iterative simulate-and-adjust calibration on four held-out gauges spanning 329–40,792 km², best of twenty rounds; nine frontier agents. | Nash–Sutcliffe Efficiency on held-out gauges against a human-expert calibration reference. | [→](../works/hydroagent.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of earth-system-science data — one of its seven application domains — translating natural-language intent into executable visualization operations over multivariate and time-varying fields. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | Interleaved web-browsing-plus-computation questions in the geophysical domain (folding into Earth Science) — multi-hop entity identification and retrieval of quantitative geophysical properties from knowledge-graph sources, followed by domain-specific computation. | Answer-first questions synthesized from knowledge-graph chains requiring multi-hop identification, quantitative-property retrieval, and multi-step computation; spans five domains (biochemistry, geophysical, financial, security, history), of which geophysical is one. | Execution-based: gold answers computed by executing parameterized code over knowledge-graph values, scored within ~2% relative tolerance; two-stage difficulty cascade; 76% human-validated validity. | [→](../works/drbencher.md) |
| Hydro-SE Bench | 2025 | Hydrology and water resources, hydraulics and river dynamics, and meteorology — three of the nine subfields of hydro-science and engineering. | 4,000 Chinese-language single- and multi-choice questions across nine subfields, sourced from textbooks, industry standards, laws and regulations and statistical yearbooks through a semi-automatic pipeline seeded with expert exemplars and reviewed by at least three experts per item; 16 models. | Accuracy reported overall and by subfield, question type and cognitive level, queried zero-shot with chain-of-thought at temperature 0 with answer extraction delegated to a separate LLM; the paper reports models are stronger on these science-grounded subfields than on the codified engineering ones. | [→](../works/hydro-se-bench.md) |

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [HydroAgent](../works/hydroagent.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
