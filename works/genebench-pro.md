# GeneBench-Pro (2026)

> **English** | [简体中文](../zh/works/genebench-pro.md)

## Overview

GeneBench-Pro is a benchmark for AI agents performing realistic multistage statistical analyses in genomics, quantitative biology, and translational biomedicine. Its 129 problems are built on constructively simulated data-generating processes rather than real datasets, so that a wrong answer is attributable to a scientific error rather than to one of several equally defensible analyst choices.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://cdn.openai.com/pdf/21938268-21af-442f-af93-3b2249afb241/genebench-pro.pdf>
- **Code:** <https://huggingface.co/datasets/openai/genebench-pro-public-package>

## Summary

The authors argue that existing biology benchmarks begin from a curated dataset and a highly specified prompt and evaluate a narrowly scoped analysis step with a cleanly verifiable answer, while real analysis spans a wider and more iterative process. GeneBench-Pro stages each problem in an isolated container with deliberately messy simulated data and a minimal prompt that fixes the target estimand but gives no prescriptive instruction on method, then grades a single binary pass on whether the agent recovered the decision-relevant number. Over the full suite the best configuration measured, GPT-5.6 Sol at the `max` reasoning level, reaches an eval-level pass rate of 28.7%.

## Tasks

129 evaluations across 10 primary domains and 21 terminal subdomains, with a genomics-centered core. Every problem is constructed from a simulated data-generating process whose full causal structure is known, and contains substantive inferential forks — decision points where a plausible wrong choice leads to a qualitatively different downstream answer — ranging from 3 to 13 per problem with a median of 6. The suite descends from GeneBench's 103 problems: three were withdrawn for fatal issues, 54 of the remaining 100 were significantly redesigned and hardened, and 29 new problems were added. Problems were chosen so as not to recapitulate well-known textbook examples or papers, to avoid benchmarking against memorized solutions.

## Domains

Statistical genetics and genetic epidemiology, population and evolutionary genetics, quantitative genetics, regulatory and molecular omics, functional genomics, proteomics and biomarkers, clinical variant interpretation and penetrance, pharmacogenomics, prenatal and reproductive genetics, cancer somatic genomics and liquid biopsy, microbial and metagenomic genomics, and forensic genetics.

## Evaluation

- **Binary grading against recoverable targets.** Pre-specified problem-specific target fields, exact-match rules, and absolute numeric tolerances; a run passes only if every graded field satisfies its constraint. Ground truth is the estimate recoverable from the staged files, not the parameter under which the data were generated.
- **No partial credit.** The primary metric uses no partial-credit or diagnostic scoring pathway, on the argument that an agent executing several intermediate steps correctly but returning the wrong decision-relevant answer has not automated the analysis.
- **Pass rate as an unweighted mean** of per-problem pass rates across the 129 problems, with 10 independent attempts per model–problem pair, reduced to 5 for GPT Pro (Extended) and Claude Opus runs.
- **Uncertainty and exclusions.** 95% hierarchical bootstrap confidence intervals from 20,000 resamples, resampling both problems and repeated runs within each problem; fewer than 1% of runs were excluded for container, tooling, provider, or response-format failures.
- **Stratified secondary reporting.** Per-problem pass rates are also reported by regime (0%, 0–10%, 10–50%, ≥50%) and broken out by release subset and external-review status, which the authors introduce specifically so that selection effects remain visible.
- **Reported.** GPT-5.6 Sol reaches 28.7% at the `max` reasoning level and GPT-5.6 Sol Pro reaches 31.5% in separately reported GPT Pro runs; GPT-5.5 reaches 12.0%, GPT-5.4 reaches 8.9%, and the strongest non-GPT baseline, Claude Opus 4.8, reaches 16.0%. Within GPT-5.6 Sol, pass rate climbs from 3.7% at `none` through 14.4%, 22.5%, 24.4% and 26.8% to 28.7% at `max`.

## Typical Duration

No uniform wall-clock budget is imposed by the evaluation harness and no step cap is stated; runs remain subject to provider and platform behavior in the evaluation stack. The only duration anchor the paper offers is human: it estimates that a typical problem executed unaided by a human expert would take on the order of 10–40 hours all-in, and labels the figure illustrative.

## Main Contribution

A simulation-grounded benchmark design for multistage scientific analysis, in which the data-generating process is constructed rather than borrowed so that grading remains insensitive to nearby defensible analyst choices while staying sensitive to missing scientifically necessary stages.

## Key Design Ideas

- Fully simulated data-generating processes, with ground truth defined as the estimate recoverable from the staged data rather than the generating parameter, so that a correct analysis is not marked wrong when sampling variation makes that parameter unrecoverable.
- A minimum viable prompt that defines the question and the graded estimand but withholds prescriptive method instructions, which the authors argue is what keeps the task from collapsing into execution of a well-defined analysis.
- Binary all-or-nothing grading, chosen to mirror the downstream decision the analysis feeds rather than to maximize measurement resolution.
- Tiered release — 10 problems public, 50 held out with a third party for independent benchmarking, and the remainder an internal holdout — as an explicit contamination-management mechanism.

## Strengths

- Grading validity is engineered and then audited rather than assumed: ablation suites demonstrate that plausible but incorrect analyses fail by clear margins, and quality-control requirements ensure nearby reasonable thresholds produce the same graded outcome.
- Unusually disciplined statistical reporting for a benchmark release — unweighted per-problem means, repeated attempts per pair, and bootstrap intervals that resample both problems and runs.
- The evaluation-integrity layer is documented rather than asserted: 82 of the 129 problems were reviewed by external domain experts, with reviewer objections and their dispositions reproduced in the paper, including cases where reviewers caught the authors grading against an incorrect ground truth.

## Limitations

- Repository note: Binary grading collapses stage-level diagnostic evidence — a run resolving most decision points but failing late scores identically to one failing immediately — and the per-problem decision-point counts are carried as qualitative metadata rather than used to stratify performance, so the benchmark measures its multistage claim end to end without yet reporting performance as a function of chain length.
- Repository note: 119 of the 129 problems are unreleased, so the headline leaderboard cannot be independently reproduced from the public package, and the paper's own stratified reporting shows results shifting materially by release subset — any figure quoted from this benchmark should carry the stratum it came from.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also an execution-based benchmark for data-driven scientific analysis, but its tasks are extracted from real published work, which is the basis GeneBench-Pro argues against on the grounds that real data admit multiple defensible paths.
- [NatureBench](./naturebench.md) — Also sources scientific difficulty from published research rather than synthetic tasks; its difficulty comes from the breadth of the literature, whereas GeneBench-Pro's comes from the depth of a single engineered chain of dependent decision points.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also runs scientific tasks in sandboxed containers without internet access, but its difficulty lies substantially in tooling and execution, whereas GeneBench-Pro designs its problems not to require the installed tools so that statistical judgement is isolated.
