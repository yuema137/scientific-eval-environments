# ALeRCE Text-to-SQL (2026)

> **English** | [简体中文](../zh/works/alerce-text-to-sql.md)

> **First appeared:** 2026-06-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.18108)

## Overview

A natural-language-to-SQL system for the ALeRCE astronomical alert-broker database, released together with an evaluation set of 110 natural-language/SQL pairs written by astronomers with expert-authored gold queries, on which thirteen LLMs are compared under a perfect-match execution metric.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.18108>
- **Venue:** arXiv preprint, submitted 16 June 2026

## Summary

ALeRCE is a community alert broker for the Zwicky Transient Facility and the Vera C. Rubin Observatory; its database is large and irregular enough that astronomers without SQL fluency cannot easily interrogate it. The paper builds a four-module pipeline — schema linking, query classification, prompt decomposition and self-correction — that turns an astronomer's question into an executable SQL query against that database, and evaluates it by executing both the predicted and the gold query and comparing the returned rows and columns. The evaluation set of 110 NL/SQL pairs was elicited from practising astronomers rather than synthesized, and thirteen LLM backends are scored on it, with an accompanying per-model API cost table. The headline finding is that current state-of-the-art text-to-SQL performance does not carry over to a real scientific database: results are strong on simple queries and degrade sharply once queries require joins and domain-specific semantics.

## Tasks

110 natural-language/SQL pairs over the ALeRCE database. 21 examples came from the ALeRCE team and had been presented in workshops; the remaining 89 were written by 10 astronomers, and an SQL expert then authored the gold target query for each. The pairs are split into a development set of 58 (32 simple, 14 medium, 12 hard) and a test set of 52 (32 simple, 10 medium, 10 hard). As of early 2026 the target database has 25 tables and 304 columns.

## Domains

Astronomy. The database is an operational time-domain survey broker over the ZTF alert stream (and prospectively Rubin/LSST), so the queries concern astronomical objects, classifications, photometry and light-curve properties, and answering them correctly requires the domain semantics of the broker schema rather than generic database reasoning. A secondary Computer Science reading is defensible, since the produced artifact is executable SQL and the method is a text-to-SQL pipeline, but the scored objective is retrieval of the correct astronomical records.

## Evaluation

- **Perfect Match (PM):** the predicted and ground-truth queries are both executed and their results compared; a query counts as a perfect match when the execution results are identical. PM is computed separately for row identifiers (`PMrows`) and column identifiers (`PMcols`), with precision and recall also computed per query against the ground-truth sets.
- **Protocol:** every query is run 10 times per model and per generation method, and results are reported broken down by the simple/medium/hard difficulty labels.
- **Ablation:** direct (one-shot) generation is compared against step-by-step generation and step-by-step generation with the self-correction module; direct inference performs worse across difficulty levels.
- **Reported.** Thirteen models evaluated: GPT-4o, GPT-4.1, GPT-5, GPT-5.2, GPT-5.2-Codex, GPT-5.3-Codex, Claude 3.7, Claude Sonnet 4.5, Claude Opus 4.6, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash and Gemini 3.1 Flash. The best configuration is Claude Opus 4.6 with step-by-step generation and self-correction, at PMrows/PMcols of 0.97/0.94 on simple queries, 0.44/0.72 on medium and 0.59/0.49 on hard. The authors name Claude Opus 4.6, Gemini 2.5 Pro, Gemini 3 Flash and GPT-5.2-Codex as the strongest performers overall.

## Typical Duration

Reported as monetary cost rather than wall-clock. Table 3 gives the "average total cost per run in US dollars by LLM and query generation method", aggregated over all test-set queries and averaged over 10 runs, broken down by pipeline stage (schema linking, difficulty classification, decomposition, SQL generation, self-correction): Claude Opus 4.6 in the step-by-step configuration costs $2.87 per run, and Gemini 3 Flash is the cheapest of the top group at $0.27. The paper states that all stages stay well within model context limits; per-query token counts and runtimes are not given.

## Main Contribution

A domain-grounded text-to-SQL pipeline for a real astronomical alert-broker database, together with a publicly released astronomer-authored NL/SQL evaluation set and a systematic thirteen-model comparison showing that reported text-to-SQL progress on standard benchmarks does not transfer to a scientific database with irregular schema and domain-specific semantics.

## Key Design Ideas

- Decomposition into four independently prompted modules — schema linking, query classification, prompt decomposition, self-correction — each issuing its own API call, so failures can be attributed to a stage.
- A difficulty classifier that routes queries, paired with a difficulty-stratified evaluation set, so accuracy is reported against query complexity rather than averaged away.
- Self-correction driven by executing the candidate query and feeding back the error, which repairs syntactic and schema-reference failures but not semantic ones.
- Execution-based scoring split into row and column agreement, which distinguishes selecting the right objects from returning the right fields.
- Ten runs per query, so the stochasticity of LLM generation is measured rather than assumed away.
- Explicit domain-knowledge injection into the prompt, reflecting the paper's finding that performance depends heavily on the external schema and astronomy context provided.

## Strengths

- The evaluation set is elicited from 10 practising astronomers plus the broker team, so the questions are the ones real users ask, and gold queries are written by an SQL expert.
- Scoring is execution-based rather than string-matching, and separates row-level from column-level correctness.
- Difficulty stratification with matched development and test splits makes the degradation with complexity legible.
- Thirteen backends spanning three vendors and several generations, each run 10 times, with a per-stage cost table so accuracy and price can be read together.
- The target is a live operational broker for ZTF and Rubin, not a synthetic schema.

## Limitations

- The evaluation set is small — 110 pairs in total, of which only 52 are test items and only 10 each are medium and hard — so per-difficulty rates rest on very few queries.
- Results are non-monotonic across difficulty (PMrows 0.44 on medium versus 0.59 on hard for the best model), which the small per-bin counts make hard to interpret.
- Self-correction repairs execution failures but does not catch semantically wrong queries that execute cleanly, so PM can still reward or punish for the wrong reason.
- Repository note: the benchmark covers a single database. It measures whether a model can query ALeRCE, not whether it can query astronomical archives generally.
- Repository note: the paper states the 110-pair dataset is made publicly available, but no repository or archive URL for it was located in the preprint.
- Repository note: the substantive contribution is a system; it is recorded here because it also ships a released, expert-curated evaluation set with an execution-based scoring protocol and a thirteen-model comparison.

## Related Works

- [AstroAlertBench](./astroalertbench.md) — Also built on the ALeRCE/ZTF alert stream, but evaluates multimodal classification of individual alerts rather than database querying.
- [Stargazer](./stargazer.md) — Also an astronomy evaluation grounded in real archival observational data, scoring iterative model fitting instead of query generation.
- [DA-Code](./da-code.md) — General-domain counterpart: agent-oriented data-science code generation in an executable sandbox, including database work, without domain-specific schema semantics.
