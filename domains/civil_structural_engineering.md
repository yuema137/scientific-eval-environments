# Civil & Structural Engineering

> **English** | [简体中文](../zh/domains/civil_structural_engineering.md) · [← All domains](./README.md)

## Scope

Civil and structural engineering.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | Civil Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| StructureClaw | 2026 | Carry structural-engineering tasks from model through validation, solver execution, and code checks. | 150 controlled scenarios (standard, interactive, multimodal reconstruction) on an artifact-centered agent workbench. | Strict structural-model matching plus numerical agreement with frozen reference solver responses; all assertions must pass (E2E Success). | [→](../works/structureclaw.md) |
| ERI Benchmark | 2026 | Civil engineering as one of nine covered fields, with seven subdomains: statics, mechanics of materials, structural analysis, steel and concrete design, geotechnical engineering, structural dynamics, and construction management. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item. | [→](../works/eri-benchmark.md) |

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [StructureClaw](../works/structureclaw.md)
- [ERI Benchmark](../works/eri-benchmark.md)
