# From Queries to Criteria: Understanding How Astronomers Evaluate LLMs (2025)

> **English** | [简体中文](../zh/works/from-queries-to-criteria-understanding-how-astrono.md)

> **First appeared:** 2025-07-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2507.15715)

## Overview

An empirical study of how domain experts actually judge an LLM system in situ: 368 real queries and 11 interviews from a four-week deployment of an astronomy literature RAG bot are inductively coded into a query taxonomy and five evaluation criteria, which are then used to build and release a 40-item expert-authored astronomy benchmark with an automatic scoring protocol validated against user ratings.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.15715>
- **Code:** <https://huggingface.co/datasets/jhu-clsp/astro-llms-benchmark-dataset>
- **Venue:** Conference on Language Modeling (COLM) 2025

## Summary

The authors deployed `@Ask-astro-ph`, a Slack retrieval-augmented-generation bot over roughly 300,000 astrophysics arXiv papers (through July 2023) using bge-small-en-v1.5 retrieval of the top five papers and GPT-4o for generation, to astronomers at the Space Telescope Science Institute. Over four weeks (29 May – 24 June 2024) 35 of 43 recruited participants issued 368 queries; eleven were interviewed afterwards. Inductive coding of the queries yields a nine-type query taxonomy, and the interviews yield five criteria astronomers apply when judging responses — criteria that existing multiple-choice astronomy benchmarks largely do not capture. The findings are turned into concrete benchmark-construction recommendations and instantiated as a 40-question benchmark with expert-written gold answers, whose automatic relevance scores correlate at Pearson 0.82 with real user thumbs-up/down ratings.

## Tasks

The benchmark comprises 40 question–answer pairs sampled from the deployment's real query log, distributed as roughly 55% specific-factual knowledge seeking, 22% deep knowledge (synthesis and higher-order reasoning) and 17% broad description. Seven astronomers each selected questions matching their expertise and wrote free-form gold answers citing 2–5 arXiv papers, spending about 30 minutes per question; one further astronomer performed a quality review. The underlying study corpus is the full de-identified log of 368 queries, coded into nine types: knowledge seeking — specific factual (33%), deep knowledge (21%), bibliometric search — topic (14%), knowledge seeking — broad description (13%), stress testing (7%), bot capabilities (5%), knowledge seeking — procedure (2%), bibliometric search — specific paper/author (2%), and unresolved topic (2%). Krippendorff's alpha for the coding was 0.51.

## Domains

Astronomy — the deployed system, the participant population (PhD astronomers at the Space Telescope Science Institute), the retrieval corpus (astrophysics arXiv), and every benchmark question and gold answer are astronomical. The authors expect the evaluation framing to generalize to other observational and semi-verifiable sciences, but the evaluated material is astronomy throughout.

## Evaluation

Two layers. First, the study's own instrument: inductive qualitative coding of queries and interviews into a query taxonomy and five evaluation criteria — general correctness (term accuracy, citation relevance and recency, faithful summarization of retrieved sources), hedging and caveating (appropriate uncertainty and explained refusals; users criticized overconfidence), response specificity and clarity, correct query interpretation (context, disambiguation of domain terminology, intent), and broader impact (time saved, discovery value, effects on research practice and equity). Second, the released benchmark: bot responses are scored against the expert gold answers by LLM-generated relevance scores on a 0–1 scale, supplemented by closeness-to-human-response measures (embeddings and BERTScore), epistemic-marker detection for the hedging criterion, and natural-language-inference entailment checks for citation accuracy.

- **Reported:** benchmark relevance scores correlate with real user thumbs-up/down ratings at Pearson 0.8239, offered as validation that the automatic protocol tracks practitioner judgment.
- The authors state explicitly that the broader-impact criterion cannot be captured by any static dataset and requires user studies.

## Typical Duration

Four-week live deployment; single-turn query–response interaction with the bot. Gold-answer authoring took roughly 30 minutes of expert time per benchmark question. No per-query token or latency budgets are stated in the primary source.

## Main Contribution

An empirically grounded account of the criteria domain experts actually use when evaluating an LLM system in real research work, and the translation of those criteria into benchmark-design recommendations and a released, validated astronomy benchmark — arguing that prevailing multiple-choice astronomy benchmarks capture only a narrow band of correctness.

## Key Design Ideas

- Derive evaluation criteria from observed practitioner behaviour in a live deployment rather than from benchmark-designer intuition.
- Pair the query log with follow-up interviews, so what users asked and why they judged a response good are both recorded.
- Map query types to evaluation criteria to candidate metrics in a single table, making the benchmark-construction argument concrete and auditable.
- Build gold answers from working astronomers writing in their own area of expertise, with mandatory arXiv citations, rather than from an LLM.
- Validate the automatic scoring protocol against real in-deployment user ratings instead of asserting it.
- Match metric to criterion: entailment models for citation accuracy, epistemic-marker detection for hedging, embedding similarity for closeness — rather than one aggregate score.
- Release both the full de-identified query log and the benchmark.

## Strengths

- Grounded in real research use by 35 PhD astronomers, not in a synthetic or crowdsourced task.
- Produces an artifact, not only findings: a released benchmark plus a released query corpus.
- The scoring protocol carries an explicit external validation against user ratings.
- Names an evaluation dimension (broader impact) that it honestly declares out of reach of static benchmarks.
- Peer-reviewed at COLM 2025.

## Limitations

- Single U.S. institute, all participants holding PhDs, opt-in recruitment; the sample may exclude disinterested users, students and amateur astronomers.
- 40 benchmark items is small, and they are drawn from one deployment's query distribution.
- Findings reflect one specific bot (a GPT-4o RAG system over a corpus frozen at July 2023); evaluation strategies may differ against other tools.
- A four-week window may not capture long-term adaptation of user expectations.
- Inter-annotator agreement on the query taxonomy is moderate (Krippendorff's alpha 0.51), which the authors attribute to annotator diversity.
- Repository note: the system evaluated is a single-turn RAG assistant, not a tool-using agent; the contribution is evaluation methodology plus a small benchmark rather than an agent task environment.

## Related Works

- [AstroMLab 1](./astromlab-1.md) — the multiple-choice astronomy benchmark whose narrowness this work argues against.
- [Stargazer](./stargazer.md) — astronomy evaluation with an executable task environment rather than literature question answering.
- [ScholarQuest](./scholarquest.md) — also evaluates literature search and evidence synthesis, at larger scale but in computer science.
- [AI's Capability in Assisting Scientific Research I: Literature Review](./ai-assisting-research-i-literature-review.md) — a complementary astronomy/astrophysics evaluation of AI literature search against human experts.
