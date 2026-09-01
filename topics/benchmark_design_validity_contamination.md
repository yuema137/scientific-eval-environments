# Benchmark Design, Validity & Contamination

> **English** | [简体中文](../zh/topics/benchmark_design_validity_contamination.md) · [← All topics](./README.md)

## Start Here

A benchmark can return a precise number and still measure the wrong thing. The test set may already be in training data, a weak verifier may accept broken output, or a toy environment may omit the condition named in the paper's claim. The problem is not arithmetic; it is whether the path from task to score supports the conclusion.

Trace one coding item: choose a recent repository, generate tests, require those tests to cover the changed branches, run the submitted patch, and record what the verifier misses. Each step closes one failure route. None makes the benchmark permanently valid; repositories age, models see new data, and verifiers need their own audits.

## Definition

This topic checks the chain that turns a task into a claim. Where did the task come from? Could the model have memorized it? Does the reference answer cover valid alternatives? Can the verifier reject a plausible but broken result? Does the environment preserve the real constraint the benchmark claims to test? The answers determine whether the reported score means what readers think it means.

## Motivation

Clean arithmetic does not rescue a bad measurement. Memorized tasks inflate capability, weak tests admit false passes, incomplete references reject defensible answers, and toy environments remove the hard part of real work. Benchmark design is therefore part of the research result. It must be tested and maintained, not treated as packaging around the model evaluation.

## Existing Approaches

- **Dynamic and recent sources.** [CODE2BENCH](../works/code2bench.md), [PRL-Bench](../works/prl-bench.md), and [MedBrowseComp](../works/medbrowsecomp.md) refresh tasks from recent repositories, publications, or live sources.
- **Private or newly authored answers.** [CritPt](../works/critpt.md), [OnePot-Bench](../works/onepot-bench.md), and [GeneBench-Pro](../works/genebench-pro.md) use unpublished, private, or held-out material.
- **Procedural and counterfactual construction.** [DiscoverPhysics](../works/discoverphysics.md) generates worlds on demand; [Robotouille](../works/robotouille.md) procedurally generates embodied tasks.
- **Verifier rigor.** CODE2BENCH gates property-based tests on branch coverage, while [FrontierCode](../works/frontiercode.md) combines execution with contamination detection.
- **Sealed replay after open exploration.** [AI4AI-Bench](../works/ai4ai-bench.md) lets agents use a cheap proxy during development, then transfers only source code into a fresh run scored by a fixed final evaluator; the original algorithm is rerun under the same conditions.
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

- [AI4AI-Bench](../works/ai4ai-bench.md)
- [OnePot-Bench](../works/onepot-bench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [FrontierCode](../works/frontiercode.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [PRL-Bench](../works/prl-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [CritPt](../works/critpt.md)
- [CODE2BENCH](../works/code2bench.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [Robotouille](../works/robotouille.md)
