# LLM-EPANET (2025)

> **English** | [简体中文](../zh/works/llm-epanet.md)

## Overview

LLM-EPANET is a retrieval-augmented, multi-agent pipeline that turns natural-language questions about a water
distribution system into executable EPANET simulation code, released together with a curated benchmark of 69
queries whose ground truth is a hand-written, deterministic reference script for every query.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.16191>
- **Code:** <https://github.com/yinon-gold/LLMs-in-WDS-Modeling>
- **Venue:** arXiv preprint, first submitted March 2025, revised February 2026

## Summary

EPANET is the standard simulator for hydraulic and water-quality behaviour in water distribution systems, but
using it beyond its GUI requires coding against its toolkit, which keeps model-based analysis confined to a
small group of specialists. LLM-EPANET retrieves function-level chunks of the EPyT Python wrapper
documentation, prompts an LLM to write a Python function that answers the user's query, has a smaller model
build the evaluation call, and executes the result in an isolated sandbox with an automatic self-debugging
loop. The evaluation set of 69 queries spans five complexity categories over three standard networks, and the
paper reports categorised accuracy, an error taxonomy, prompt-sensitivity, and an accuracy–cost–latency
comparison across seven commercial LLMs.

## Tasks

69 natural-language benchmark queries over three networks — Net1 and Net3 from the original EPANET
distribution, and L-Town — in five categories of increasing complexity: **Static** (answerable from the
network file without simulation), **Hydraulics** (requiring a hydraulic simulation), **Quality** (requiring a
water-quality simulation), **Hydraulics Scenario** (network modification followed by simulation), and
**Iterative** (repeated parameter changes with conditional feasibility checks). Each query is assigned to the
category of the most complex modelling operation it needs. The Iterative category is explicitly exploratory
and contains only three queries. The benchmark queries, expected answers, and ground-truth scripts are
released as open source.

## Domains

Civil & Structural Engineering: hydraulic infrastructure engineering on municipal water distribution
networks — pressures, flows, pump energy, network modification and scenario analysis on standard benchmark
networks; the authors are from a Faculty of Civil and Environmental Engineering. The water-quality queries
(chlorine transport, water age, source tracing) also touch Environmental Science, but the evaluated object
throughout is a piped distribution network rather than a natural water body.

## Evaluation

- Functional correctness of the returned result, not text or code similarity. For every benchmark query a
  reference implementation was written by hand against EPyT and executed in advance; these deterministic
  reference outputs are the ground truth and are published as executable test scripts.
- A response is *correct* when the returned value is equivalent to the reference result. Execution failures,
  unrecovered errors, incorrect aggregation, indexing mistakes, and unit mismatches count as incorrect. Where
  an LLM output differed from the reference but was arguably equivalent (rounding, scalar versus structured
  output), a hydraulic modelling expert adjudicated equivalence without modifying the generated code.
- Accuracy is reported per category as the fraction of correct answers.
- **Reported.** Seven models were run: `microsoft/phi-4`, `google/gemini-2.0-flash-001`,
  `qwen/qwen2.5-vl-72b-instruct`, `openai/gpt-4.1-mini`, `meta-llama/llama-4-maverick`,
  `anthropic/claude-3.7-sonnet`, and `openai/o3-mini-high`. Overall accuracy spans 56–81%, above 90% on the
  Static category for all models, with `o3-mini-high` highest at 80% overall and above 60% in every category.
  `phi-4` failed to produce executable code on 40 of the 69 queries.
- A failure taxonomy is reported over all runs: execution errors are dominated by signature mismatch (44.6%)
  and importing problems (23.8%), while wrong answers are dominated by indexing errors (31.5%), bad logic
  (25.9%), and aggregation mistakes (20.4%).

## Typical Duration

Each query is a single prompt-to-execution episode with up to five self-debugging retries (set to 5 in the
reported experiments); more than 85% of eventual successes are achieved on the first attempt and no model
solved anything new on the fifth. Sandboxed execution is capped at a 60-second timeout. A full 69-query run
costs roughly $1 in LLM usage for `o3-mini-high`, more than four times the cost of the cheaper models the
paper places on the accuracy–cost Pareto front; per-query response time is reported per model, with
`o3-mini-high` substantially the slowest.

## Main Contribution

An agent-based, no-code natural-language interface to EPANET combining RAG over the EPyT documentation with a
multi-agent code-generation and self-debugging pipeline, together with a curated, openly released benchmark of
69 queries with executable reference scripts, used to measure how well current LLMs support water distribution
system modelling tasks.

## Key Design Ideas

- Ground truth is an executable reference script per query, so scoring is reproducible and independent of the
  LLM-generated code — no text or code similarity metric is used.
- Queries are stratified by the most complex modelling operation they require, making the accuracy decay from
  static lookups to scenario and iterative tasks directly readable.
- Documentation is chunked at function-level granularity rather than by token windows, keeping each retrieval
  unit semantically self-contained; retrieval quality itself is validated with precision/recall/F1 against
  functions actually invoked by successful runs, fixing K = 5.
- A structured error traceback is fed back to the code-generation agent for a bounded number of retries, and
  the accuracy gained per additional retry is reported as a robustness curve.
- A meta prompt carrying EPANET/EPyT modelling conventions is treated as an explicit, ablatable component:
  Basic, Simple, and Complex variants are compared, and the gap widens on the harder categories.
- Cost and latency per model are reported alongside accuracy, so model choice is presented as a trade-off
  rather than a ranking.

## Strengths

- Deterministic, executable ground truth published with the benchmark, which is unusual for simulator-mediated
  natural-language tasks.
- Seven models spanning open-weight and frontier commercial tiers are compared under an identical protocol.
- The failure analysis is quantitative and mechanism-level (signature mismatch, one-based versus zero-based
  indexing, aggregation), not just an accuracy table.
- Prompt content is isolated as a variable through a three-level meta-prompt ablation.
- Physics is enforced by the EPANET engine rather than approximated by the model, so a correct program yields
  exactly what a human modeller would obtain.

## Limitations

- 69 queries is small, and the Iterative category contains only three, which the authors describe as
  exploratory rather than a statistically robust estimate.
- Adjudication of near-miss answers is by a single human expert.
- The system is scored only on whether the returned value matches the reference; the authors note it does not
  check whether a runnable solution is hydraulically feasible (negative pressures, tank bound violations).
- The paper states it does not aim to benchmark LLM providers and cautions that its model ranking is a
  snapshot; models were chosen to span cost tiers rather than to form a complete field.
- Performance depends heavily on a hand-tuned meta prompt injecting domain knowledge, which the authors accept
  as an intentional design choice rather than a demonstration of autonomous reasoning.
- Repository note: the three networks are the standard EPANET/ L-Town examples, so generalisation to
  utility-scale or badly conditioned real network files is untested.

## Related Works

- [HydroAgent](./hydroagent.md) — the closest analogue outside distribution networks: frontier agents
  calibrating an operational hydrologic model with simulator-grounded scoring.
- [FEABench](./feabench.md) — the same shape of task in another engineering simulator, driving COMSOL through
  its API from a natural-language problem statement.
- [CFDLLMBench](./cfdllmbench.md) — tiered evaluation of simulator-mediated engineering tasks, from domain
  knowledge to end-to-end case configuration and execution.
