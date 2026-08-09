# Research Reproduction & Replication

> **English** | [简体中文](../zh/activities/research_reproduction_replication.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on reproducing, reconstructing, validating, or replicating existing scientific results — recreating a published analysis, reimplementing a method to match its results, or reconstructing results from public information.

## Scope

Intentionally cross-cutting; it frequently co-occurs with Simulation, Data Analysis, or Scientific Software & Workflow Engineering. It is assigned only when reproduction or replication is the task itself, not merely because a benchmark compares outputs against a gold reference.

## Task Patterns

Several members reproduce or replicate **ML/AI research papers**, ranging from getting existing repositories to run to full from-scratch replication. [SUPER](../works/super.md) isolates the setup-and-execute bottleneck of running real ML/NLP repos, [PaperBench](../works/paperbench.md) requires replicating ICML 2024 papers from scratch against author-co-developed rubrics, and [FIRE-Bench](../works/fire-bench.md) asks agents to rediscover published ML findings from only a research question. These co-occur heavily with Scientific Software and Data Analysis, and lean on LLM-as-judge grading.

A second cluster reproduces **physics, astro, and materials claims** using open software and specialized toolchains, co-occurring strongly with Simulation and Scientific Software. [ReplicationBench](../works/replicationbench.md) targets astrophysics paper replication, [PRBench](../works/prbench.md) reimplements physics algorithms from scratch to match published numbers, [Collider-Bench](../works/collider-bench.md) recasts LHC searches through a public simulation stack scored by histogram fidelity, and [AutoMat](../works/automat.md) reproduces computational materials-science claims across DFT/MD/ML workflows.

A third grouping reproduces **study results from provided code and data** or benchmarks against published SOTA. [CORE-Bench](../works/core-bench.md) reruns published studies from their own released code and data across CS, social science, and medicine, while [NatureBench](../works/naturebench.md) pushes past reproduction toward matching the published SOTA of Nature-family papers across six domains.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| CORE-Bench | 2024 | Reproduce published study results from released code and data | 270 tasks from 90 papers, 3 difficulty levels, language + vision | Computational reproducibility accuracy (hardest level | [card](../works/core-bench.md) |
| SUPER | 2024 | Set up and execute tasks from real research repositories | 45 end-to-end + 152 sub + 602 auto-generated ML/NLP GitHub problems | End-to-end success (GPT-4o 16.3%) | [card](../works/super.md) |
| PaperBench | 2025 | Replicate SOTA AI papers from scratch | 20 ICML 2024 papers, 8,316 rubric tasks, sandbox | Rubric-graded replication score (best 21.0%) | [card](../works/paperbench.md) |
| ReplicationBench | 2025 | Replicate astrophysics paper core contributions | 111 tasks over 20 papers, computational sandboxes | Faithfulness + correctness scores (best <20%) | [card](../works/replicationbench.md) |
| AutoMat | 2026 | Reproduce computational materials science claims end-to-end | 85 SME-curated claims, HPC-representative resource-controlled env | Reproducibility score / success rate (best 54.1%) | [card](../works/automat.md) |
| Collider-Bench | 2026 | Recast published LHC collider searches from public software | 10 Simulation tasks, four CMS SUSY searches, containerized stack | Continuous histogram fidelity vs hidden reference yields | [card](../works/collider-bench.md) |
| FIRE-Bench | 2026 | Rediscover established findings from ML papers | 40 executed tasks + 60-paper pool, 24h/A100 compute-light | Reference-based rediscovery score (best <50 F1) | [card](../works/fire-bench.md) |
| NatureBench | 2026 | Match published SOTA of Nature-family publications | 90 tasks, six domains, review-gated NatureGym pipeline | Reach or exceed published SOTA under info firewall | [card](../works/naturebench.md) |
| PRBench | 2026 | Reproduce physics papers, implementing algorithms from scratch | 30 expert-curated tasks, 11 subfields, sandbox | Quantitative results matching publication (best 34%) | [card](../works/prbench.md) |

## Related Works

- [CORE-Bench](../works/core-bench.md)
- [SUPER](../works/super.md)
- [PaperBench](../works/paperbench.md)
- [ReplicationBench](../works/replicationbench.md)
- [AutoMat](../works/automat.md)
- [Collider-Bench](../works/collider-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [NatureBench](../works/naturebench.md)
- [PRBench](../works/prbench.md)
