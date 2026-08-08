# Environmental Science

> **English** | [简体中文](../zh/domains/environmental_science.md)

## Scope

Environmental prediction and monitoring. Ecology folds here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | Environmental prediction over real territories: CO2 absorption suitability (Spain), gully erosion probability, and habitat analysis, served through a production-style geospatial API. | 93 tasks in 18 categories with per-task expected tool calls, content constraints, round budgets, and domain-expert ground truth. | Eight mechanistic checks per case — expected tool calls, required/forbidden keywords, numeric tolerance (±2 pp), chart production, round budget — with no LLM judge. | [→](../works/geonatureagent-benchmark.md) |
| Terminal-Bench Science | 2026 | Ecology (Life Sciences track) and environmental science (Earth Sciences track) tasks of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
