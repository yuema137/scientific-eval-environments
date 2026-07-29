# LongDA (2026)

> **English** | [简体中文](../zh/works/longda.md)

## Overview

LongDA is a data analysis benchmark that evaluates LLM-based agents under documentation-intensive analytical workflows: 505 analytical queries grounded in expert-written publications over 17 publicly available U.S. national surveys, whose accompanying documentation averages 263k tokens. It ships with LongTA, a tool-augmented agent framework serving as evaluation scaffold and baseline.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.02598>
- **Code:** <https://github.com/Yiyang-Ian-Li/LongDA>
- **Data:** <https://huggingface.co/datasets/EvilBench/LongDA>

## Summary

In contrast to data-analysis benchmarks that assume well-specified schemas and inputs, LongDA targets settings in which navigating long, heterogeneous documentation is the primary bottleneck. Agents must first retrieve and integrate key information (variable definitions, survey weights, data schemas) from multiple unstructured documents — codebooks, methodological descriptions, survey design reports — before performing multi-step computations and writing executable code. The accompanying LongTA framework provides a ReAct-style coding agent with tools for document reading, keyword search, BM25 retrieval, note-taking, and sandboxed Python execution.

## Tasks

505 analytical queries extracted from 30 official analytical publications across 17 U.S. national surveys released by 6 federal agencies (CDC, U.S. Census Bureau, NSF, BLS, NCES, SAMHSA). Each query consists of a question, an answer structure, and additional information; 221 queries (44%) require a single numerical value and 284 (56%) require fixed-length lists with predefined semantic elements. Publications are first verified to be reproducible from the publicly released survey data, are used exclusively for query extraction, and are hidden from agents during evaluation — agents see only the raw data files and survey documentation.

## Domains

Real-world data analysis over U.S. federal survey data: public health, labor and employment, education, and the scientific workforce.

## Evaluation

- Queries are presented in **blocks**, one block per source publication, so agents can reuse intermediate understanding across related questions; agents run under a 100-step budget per block.
- **Coverage rate** — the proportion of queries whose answer syntactically conforms to the specified answer structure.
- **Match rate** — numerical correctness under tolerance τ(a) = max(ε·|a|, 1) with ε = 5%, applied element-wise for list answers; relative model rankings are stable across tolerance settings from 1% to 20%.
- **Efficiency** — total token consumption, total runtime, and average interaction steps per block are reported alongside effectiveness.
- Reported results: GPT-5 (High) reaches 94.65% coverage / 68.91% match; GPT-5 91.09% / 69.16%; the best open-source model, DeepSeek-V3.2, reaches 67.33% / 53.00%. List queries are consistently harder than scalar ones (28.8% vs. 50.9% match averaged across models). The paper concludes that success is driven primarily by information retrieval and tool-use strategy rather than pure reasoning capability, with explicit-reasoning variants showing no clear gains.

## Typical Duration

Multi-turn ReAct interaction per publication block under a 100-step budget; average steps per block range from 5.5 (GPT-5) to 81.17 (GLM-4.7) across evaluated models. Documentation per survey averages 263k tokens with a maximum exceeding 735k.

## Main Contribution

The first data-analysis benchmark to make documentation-intensive workflows the object of evaluation, positioning long-document navigation — rather than logical inference — as the dominant bottleneck of real-world data analysis, together with the LongTA scaffold for controlled study of tool-augmented data-analysis agents.

## Key Design Ideas

- Documentation navigation as the evaluated capability: variable definitions, sample weights, and schemas must be discovered from long unstructured documents before any code is written.
- Queries derived from expert publications with verified reproducibility from public data, and the publications withheld from agents at evaluation time.
- Structured answer formats (single number or fixed-length semantic list) make automatic evaluation unambiguous while enforcing instruction following.
- Block-level query presentation mirrors analyst workflows and controls evaluation cost.
- Tolerance-based match rate avoids over-penalizing small numeric deviations on small-magnitude targets.

## Strengths

- Per-query context is far longer than prior data-analysis benchmarks: about 263,500 tokens on average against at most roughly 5,200 in the paper's comparison of ten related benchmarks.
- Diagnostic experiments (tool ablations, tool-usage trajectories) attribute performance to retrieval and tool-use strategy rather than reasoning, giving the benchmark an explanatory finding beyond a leaderboard.
- Dataset, code, and agent framework publicly released.

## Limitations

The paper's own limitations section notes:

- The 17 U.S. national surveys represent a small slice of real-world data analysis and may under-represent other modalities and workflows (proprietary enterprise data, streaming analytics, database-centric ETL).
- Surveys are fixed-year snapshots; robustness to cross-year schema drift or versioned documentation is not tested.
- Metrics evaluate final numbers only, not intermediate analytical quality (code best practices, confidence intervals, edge-case handling) or the quality of explanations.
- Survey design complexity is only partially exercised: queries requiring variance estimation (standard errors, confidence intervals) are not included, so strong performance does not imply competence in complex-survey inference beyond point estimation.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also execution-based data-analysis tasks graded against expert-derived references, but with well-specified task setups rather than long-documentation navigation as the bottleneck.
- [AstaBench](./astabench.md) — Includes data analysis as one category within a broad cost-controlled research suite; LongDA is a dedicated benchmark for the documentation-intensive setting.
