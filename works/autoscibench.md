# AutoSciBench (2026)

> **English** | [简体中文](../zh/works/autoscibench.md)

> **First appeared:** 2026-10-04 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.05140)

## Overview

Scientific-agent benchmarks take expert time to build and saturate as agents improve. AutoSciBench has an agent generate the benchmark instead. Each task is specified by a concept (domain, data modality, reasoning approach) and a recipe for building the data, question, and reference answer. Solver agents then attempt the task, and a judge reads their trajectories. When the task is too easy, not verifiable, or solvable by a shortcut, the generator revises the recipe or concept. The evaluation compares solver accuracy on generated tasks with accuracy on the human-curated benchmarks used as seeds.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** [AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents](https://arxiv.org/abs/2610.05140), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.05140v1>
- **Venue:** arXiv preprint (cs.AI), 2026
- **Code / data:** no release link found in the paper. TODO(reference)

## Summary

The generator (Claude Opus 4.8 in Claude Code, or GPT-5.6 Sol in Codex) builds a task from a concept and recipe; the same model then solves it in three independent trials without the reference answer. A judge LLM reviews the question, data, reference answer, solver answers, and trajectories and rates verifiability and difficulty. It also flags shortcuts, which the paper defines as solution paths that bypass the intended validation or evidence integration, for example taking the answer from a single tool output without re-examining the raw data. The generator revises the recipe for up to 10 rounds, and after four consecutive recipe revisions without meeting both criteria it revises the concept. Experience distilled from completed runs guides later concept generation. Solver answers are checked by exact match against a single reference answer in a specified format.

## Tasks

50 generated tasks per domain per generator, from five experience-guided iterations of 10 concepts each, in three domains seeded by human-curated benchmarks: computational biology (CompBioBench), materials science (MatTools), and clinical imaging (MedCTA).

## Domains

Computational biology, materials science (computational materials tools), and clinical medical imaging.

## Evaluation

- **Solvers:** ten models (Claude Opus 5, Opus 4.8, Opus 4.7, Sonnet 5, Haiku 4.5; GPT-6 Astra, GPT-5.6 Sol, Terra, Luna; GPT-5.5).
- **Average solver accuracy (%), human-curated seed / Opus-generated / GPT-generated:** computational biology 79.8 / 57.4 / 74.1; materials science 95.7 / 70.2 / 77.6; clinical imaging n/a / 71.1 / 74.5. The headline drops of 22.4 and 25.5 points compare Opus-generated tasks with the seeds. MedCTA has no seed column because it is scored by an LLM evaluator.
- **Per-solver example:** Claude Haiku 4.5 scores 93.7% on MatTools and 21.3% on the Opus-generated materials tasks; GPT-6 Astra scores 98.0% and 81.0% on the computational-biology seed and Opus-generated tasks.
- **Quality ratings:** two LLM judges (Claude Opus 4.8 and GPT-5.6 Sol) rate verifiability, usefulness, and fitness on a 1–5 scale; the abstract reports higher average ratings for generated tasks in all three domains. TODO(reference): rating values.
- **Ablations:** iterative refinement raises the share of hard tasks; experience-guided generation lowers solver success in materials science from 66.7% to 35.0% and raises the hard-task share from 15.0% to 50.0%.
- Repository note: some seed-benchmark accuracies are leaderboard entries at a reasoning effort other than high, or with effort not reported, so not every seed-versus-generated comparison uses matched settings.

## Typical Duration

A 3,600-second timeout per pipeline stage. Generation cost per question: Opus 4.8 $58.47 (computational biology), $22.36 (materials), $24.88 (clinical imaging); GPT-5.6 Sol $111.26, $114.11, $110.45. Task implementation and solving account for most of the cost.

## Main Contribution

A generator–solver–judge loop that builds scientific-agent benchmark tasks and revises them from solver trajectories until they are verifiable, hard, and free of detected shortcuts, so the benchmark can be regenerated as agents improve.

## Key Design Ideas

- The concept/recipe split lets the loop fix a task's construction without changing its scientific aim, and change the aim only after repeated recipe failures.
- Shortcuts are detected from solver trajectories, not from final answers alone.
- Experience from finished runs feeds later concept generation.
- Answers are constrained to a single value in a specified format so they can be exact-matched.

## Strengths

- On-demand generation produces new tasks, so answers cannot have been memorized from a published benchmark.
- Results cover ten solvers on generated and seed tasks, with per-solver numbers.
- Generation cost is reported per question and broken down by pipeline stage.

## Limitations

- The paper describes no human expert review of the generated tasks; quality is rated by LLM judges, one of which is also a generator.
- The generator also solves its own tasks during refinement, so difficulty is calibrated against that model.
- An appendix notes that benchmark performance does not indicate clinical readiness.
- Repository note: lower accuracy on generated tasks shows they are harder for current solvers; whether they measure the same capabilities as the seed benchmarks rests on the LLM quality ratings.

## Related Works

- [MatTools](./mattools.md) — Seed benchmark for the materials-science domain.
- [HeurekaBench](./heurekabench.md) — Also derives scientific-agent tasks semi-automatically from existing research artifacts.
- [CODE2BENCH](./code2bench.md) — Also builds benchmarks through a repeatable construction pipeline to resist contamination.
