# Environmental Science

> **English** | [简体中文](../zh/domains/environmental_science.md) · [← All domains](./README.md)

## Scope

Environmental prediction and monitoring. Ecology folds here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | Environmental prediction over real territories: CO2 absorption suitability (Spain), gully erosion probability, and habitat analysis, served through a production-style geospatial API. | 93 tasks in 18 categories with per-task expected tool calls, content constraints, round budgets, and domain-expert ground truth. | Eight mechanistic checks per case — expected tool calls, required/forbidden keywords, numeric tolerance (±2 pp), chart production, round budget — with no LLM judge. | [→](../works/geonatureagent-benchmark.md) |
| Terminal-Bench Science | 2026 | Ecology (Life Sciences track) and environmental science (Earth Sciences track) tasks of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ERI Benchmark | 2026 | Environmental engineering as one of nine covered fields, with five subdomains: water treatment, air quality, hydrology, waste management, and environmental impact. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item. | [→](../works/eri-benchmark.md) |
| LLM-EPANET | 2025 | Water-quality behaviour in municipal water distribution systems — chlorine transport, water age and source tracing — alongside the hydraulic simulation of the same networks. | 69 natural-language queries over the standard Net1, Net3 and L-Town networks in five complexity categories, of which the Quality category requires a water-quality simulation; every query paired with a hand-written deterministic reference script. | Functional correctness of the returned value against the executed EPyT reference implementation, with execution failures, aggregation, indexing and unit errors counted incorrect; accuracy reported per category over seven models, 56–81% overall. | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | Water-resource management within hydro-science and engineering, sitting alongside the benchmark's hydrology, river-dynamics and meteorology subfields. | 4,000 Chinese-language single- and multi-choice questions across nine subfields, each labelled by cognitive level, drawn from textbooks, industry standards, laws and regulations and statistical yearbooks, with at least three independent expert reviews per item; 16 models. | Accuracy reported overall and by subfield, question type and cognitive level, queried zero-shot with chain-of-thought at temperature 0 and the choice letter extracted by a separate LLM; models score higher on the science-grounded subfields than on the codified engineering ones. | [→](../works/hydro-se-bench.md) |
| OntoLearner | 2026 | Construct ontology structure for ecology and environment — one of the 22 domains its ontology collection spans — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [OntoLearner](../works/ontolearner.md)
