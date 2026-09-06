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
- **Screening out what the model already knows.** [HeurekaBench](../works/heurekabench.md) has GPT-4o and Claude-4-Sonnet answer every candidate question with no dataset access and keeps only the ones they miss, so a surviving question cannot be answered from pre-training alone; its judge rubric additionally penalizes an answer that leans on model knowledge instead of the supplied data.
- **Reproducible tools as a validity condition.** [AstaBench](../works/astabench.md) states five principles for benchmarking agents and builds the suite to them: corpus tools restricted to papers predating benchmark creation so later publications cannot contaminate results, one standard task interface, and a leaderboard where openness and tooling are declared alongside every score.
- **Guarding the run, not just the task set.** [EXP-Bench](../works/exp-bench.md) screens agent logs for disallowed behavior — reading the source paper, Git operations, fabricated data — before any grading happens, and splits each task into individually gradable subtasks so per-aspect credit never stands in for end-to-end success.

## Comparison

| Work | Task source | Validity intervention | Verification | Refresh model |
|---|---|---|---|---|
| CODE2BENCH | Recent Python and Java repositories | Dynamic sourcing + dependency classification + test-quality gate | Property-based tests, 100% branch coverage | Repeatable construction pipeline |
| PRL-Bench | Newly published physics papers | Rolling recency frontier | Reference-grounded evaluation | Journal issue cycle |
| CritPt | Unpublished expert problems | Answers unavailable to training corpora | Expert/reference checking | New authored batches |
| DiscoverPhysics | Generated physical worlds | On-demand counterfactual laws | Simulator ground truth | Per instance |
| ResearchCodeBench | Recent ML papers | Contamination-safe paper subset | Executable code tests | New paper cohorts |
| ASI-Bench | 60 project tasks from the literature, expert-filtered | B1-B4 guidance gradient within one project; B3 and B4 mean forced strictly below 40 at task acceptance | Task-specific gates and weighted scorers vs reproducible per-task references; private `seed42` reference set | New authored task batches via public portal |
| AstaBench | 11 benchmarks: 7 author-created (4 previously unreleased), the rest adapted | Five stated benchmarking principles; corpus tools cut off at benchmark-creation date; openness and tooling declared per leaderboard entry | Per-benchmark metrics with normalized cost; 6 of the 11 use LLM judges | New benchmarks and new cutoffs at each suite revision |
| EXP-Bench | 461 tasks from 51 NeurIPS/ICLR 2024 papers and their repositories | Impact-based filtering, multi-pass extraction, human validation; run-time monitor for source-paper access and fabricated data | Containerized execution plus LLM judges over 12,737 gradable subtasks | New paper cohorts through the same pipeline |
| HeurekaBench | Published studies paired with their code repositories | Two frontier models discard questions answerable without the data; manual pass removes hallucinations, duplicates, and non-validated components | Ground truth verified against the study's reported findings; judge checked against 11 experts | New studies re-run through the pipeline |

## Open Questions

- How can contamination audits quantify absence rather than merely search for known overlaps?
- What test-adequacy evidence is sufficient for claiming functional correctness?
- How should benchmark refreshes preserve longitudinal comparability?
- When does synthetic control sacrifice the ecological validity needed for scientific and engineering claims?
- How should uncertainty in references, rubrics, and judges be reflected in scores?

## Related Works

- [AI4AI-Bench](../works/ai4ai-bench.md)
- [ASI-Bench](../works/asi-bench.md)
- [OnePot-Bench](../works/onepot-bench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [FrontierCode](../works/frontiercode.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [PRL-Bench](../works/prl-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [HeurekaBench](../works/heurekabench.md)
- [AstaBench](../works/astabench.md)
- [CritPt](../works/critpt.md)
- [CODE2BENCH](../works/code2bench.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [EXP-Bench](../works/exp-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [Robotouille](../works/robotouille.md)
