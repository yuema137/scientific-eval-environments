# Benchmark Design, Validity & Contamination

> **English** | [简体中文](../zh/topics/benchmark_design_validity_contamination.md) · [← All topics](./README.md)

## Start Here

A benchmark can return a precise number and still measure the wrong thing. The test set may already be in training data, a weak verifier may accept broken output, or a toy environment may omit the condition named in the paper's claim. The problem is not arithmetic; it is whether the path from task to score supports the conclusion.

Trace one coding item: choose a recent repository, generate tests, require those tests to cover the changed branches, run the submitted patch, and record what the verifier misses. Each step closes one failure route. None makes the benchmark permanently valid; repositories age, models see new data, and verifiers need their own audits.

## Definition

This topic studies whether benchmark tasks, reference answers, verifiers, sampling procedures, and reported scores support the claims made from them. It covers task construction, contamination resistance, dynamic evaluation, ecological validity, verifier rigor, and benchmark maintenance.

## Motivation

A precise score can still be invalid if tasks are memorized, tests are weak, reference answers are incomplete, or the environment omits the conditions the claimed capability requires. Benchmark validity is therefore an empirical research object, not housekeeping.

## Existing Approaches

- **Dynamic and recent sources.** [CODE2BENCH](../works/code2bench.md), [PRL-Bench](../works/prl-bench.md), and [MedBrowseComp](../works/medbrowsecomp.md) refresh tasks from recent repositories, publications, or live sources.
- **Private or newly authored answers.** [CritPt](../works/critpt.md), [OnePot-Bench](../works/onepot-bench.md), and [GeneBench-Pro](../works/genebench-pro.md) use unpublished, private, or held-out material.
- **Procedural and counterfactual construction.** [DiscoverPhysics](../works/discoverphysics.md) generates worlds on demand; [Robotouille](../works/robotouille.md) procedurally generates embodied tasks.
- **Verifier rigor.** CODE2BENCH gates property-based tests on branch coverage, while [FrontierCode](../works/frontiercode.md) combines execution with contamination detection.
- **Recency-aware implementation.** [ResearchCodeBench](../works/researchcodebench.md) derives implementation tasks from recent research contributions and publishes a contamination-safe subset.

## Comparison

| Work | Task source | Validity intervention | Verification | Refresh model |
|---|---|---|---|---|
| CODE2BENCH | Recent Python and Java repositories | Dynamic sourcing + dependency classification + test-quality gate | Property-based tests, 100% branch coverage | Repeatable construction pipeline |
| PRL-Bench | Newly published physics papers | Rolling recency frontier | Reference-grounded evaluation | Journal issue cycle |
| CritPt | Unpublished expert problems | Answers unavailable to training corpora | Expert/reference checking | New authored batches |
| DiscoverPhysics | Generated physical worlds | On-demand counterfactual laws | Simulator ground truth | Per instance |
| ResearchCodeBench | Recent ML papers | Contamination-safe paper subset | Executable code tests | New paper cohorts |

## Open Questions

- How can contamination audits quantify absence rather than merely search for known overlaps?
- What test-adequacy evidence is sufficient for claiming functional correctness?
- How should benchmark refreshes preserve longitudinal comparability?
- When does synthetic control sacrifice the ecological validity needed for scientific and engineering claims?
- How should uncertainty in references, rubrics, and judges be reflected in scores?

## Related Works

- [CODE2BENCH](../works/code2bench.md)
- [PRL-Bench](../works/prl-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [CritPt](../works/critpt.md)
- [OnePot-Bench](../works/onepot-bench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [Robotouille](../works/robotouille.md)
- [FrontierCode](../works/frontiercode.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [PostTrainBench](../works/posttrainbench.md)
