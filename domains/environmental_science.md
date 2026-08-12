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

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ERI Benchmark](../works/eri-benchmark.md)
