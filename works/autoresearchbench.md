# AutoResearchBench (2026)

> **English** | [简体中文](../zh/works/autoresearchbench.md)

## Overview

AutoResearchBench is a benchmark for autonomous scientific literature discovery, evaluating AI agents on tracking down a specific target paper through progressive multi-step probing (Deep Research) and on comprehensively collecting all papers satisfying given conditions (Wide Research).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.25256>
- **Code:** <https://github.com/CherYou/AutoResearchBench>

## Summary

AutoResearchBench targets the literature-finding step of autonomous research — exploring existing knowledge for a research problem and acquiring evidence for verifying assumptions and supporting claims. Compared to prior agentic web-browsing benchmarks, the paper distinguishes it along three dimensions: *research-oriented* (requires in-depth comprehension of scientific concepts), *literature-focused* (demands fine-grained use of detailed information), and *open-ended* (an unknown number of qualified papers, requiring deliberate reasoning and search throughout). The paper positions these properties as making the benchmark extraordinarily challenging even for models that have largely conquered general agentic browsing benchmarks such as BrowseComp.

## Tasks

1,000 queries in two complementary task types: **Deep Research** (600 queries — locate one specific target paper through progressive, multi-step probing) and **Wide Research** (400 queries — collect the set of papers satisfying given conditions; on average 9.23 valid answers per query, ranging from 2 to 34 papers). Tasks are constructed by a full-text-first human–machine pipeline: for Deep Research, target-paper selection, full-text constraint mining with citation-based multi-hop expansion, constraint fuzzification and pruning, and verification; for Wide Research, domain-specific sourcing, structural abstraction, query refinement, and iterative expansion with rigorous auditing, requiring unanimous LLM consensus for paper admission.

## Domains

Scientific literature discovery across eight core computer science domains.

## Evaluation

- **Deep Research:** exact-match accuracy — the predicted set must equal the ground-truth target.
- **Wide Research:** Intersection over Union (IoU) between the predicted and ground-truth paper sets, scoring the predicted set holistically without imposing a ranking.
- Reported results: the strongest evaluated models reach only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, with many strong baselines below 5%.

## Typical Duration

Multi-turn agentic search over academic and general web retrieval backends; per-query turn counts vary by model, averaging up to a few dozen turns.

## Main Contribution

A dedicated benchmark for autonomous scientific literature discovery that separates targeted paper-finding (Deep Research) from open-ended comprehensive collection (Wide Research), with a publicly released dataset, evaluation pipeline, and code.

## Key Design Ideas

- Two complementary task types split the literature-discovery problem: pinpointing one target paper vs. exhaustively collecting a qualifying set.
- Open-endedness by construction: the number of qualifying papers is unknown to the agent, so stopping criteria become part of what is evaluated.
- Full-text-first task construction mines constraints from paper full texts and citation graphs rather than from titles and abstracts alone.
- Set-level IoU scoring for Wide Research evaluates comprehensiveness directly instead of ranking quality.

## Strengths

- Targets a load-bearing step of autonomous research (literature discovery) that general web-browsing benchmarks under-model.
- Large headroom: best reported scores are below 10% on both task types.
- Dataset, evaluation pipeline, and code publicly released (Apache 2.0).

## Limitations

- Repository note: Coverage is limited to computer science literature; the paper does not evaluate discovery in other scientific fields.
- Repository note: Wide Research ground-truth admission relies on LLM consensus during construction, so answer-set completeness inherits the reliability of those judges.

## Related Works

- [AstaBench](./astabench.md) — Also evaluates literature-related research capability, but as one category within a broad research suite rather than as a dedicated discovery benchmark.
- [GAIA](./gaia.md) — General-assistant browsing and tool-use questions with single unambiguous answers; AutoResearchBench contrasts itself with such general agentic browsing by requiring open-ended, literature-focused search.
