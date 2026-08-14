# BiomedSQL (2025)

> **English** | [简体中文](../zh/works/biomedsql.md)

## Overview

BiomedSQL is a text-to-SQL benchmark over a harmonized biomedical knowledge base of gene–disease associations, omics causal-inference results, and drug approval records, in which answering a question correctly requires the model to supply implicit domain criteria — genome-wide significance thresholds, effect directionality, trial-phase filters — that the natural-language question never states.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.20321>
- **Code:** <https://github.com/NIH-CARD/biomedsql>
- **Data:** <https://huggingface.co/datasets/NIH-CARD/BiomedSQL>
- **Venue:** COLM 2026

## Summary

The paper's premise is that existing text-to-SQL benchmarks reward syntactic translation, whereas a biomedical analyst querying a real research database must first decide what the question means operationally — which p-value counts as genome-wide significant, which direction of effect answers "increases risk", which trial phase counts as approved. BiomedSQL grounds 68,000 question / SQL query / answer triples in a live BigQuery database assembled from trusted biomedical resources, so that a correct query depends on domain criteria the question leaves implicit. The authors evaluate open- and closed-source LLMs across several prompting strategies and interaction paradigms, and also build a custom multi-step agent, BMSQL, that refines queries through feedback on intermediate results and execution errors. Every configuration falls well short of the human expert baseline, which the authors present as evidence that scientific reasoning, not SQL syntax, is the binding constraint.

## Tasks

68,000 question / SQL query / answer triples. Construction started from 40 expert-authored seed queries, which "were then templated and expanded by programmatically inserting disease, gene, and SNP mentions, aligning them to the full set of 68,000 QA pairs in CARDBiomedBench." Model scoring is done on "a representative test set of 546 questions, sampled to preserve the expert-authored template distribution of the full benchmark."

Questions are labelled along two orthogonal axes: eight SQL task categories (Select, Distinct, Join, Multi-Filter, Threshold, Calculate, Order By, Similarity Search) and nine biomedical reasoning categories (Approval Status, Trial Phase, GWAS Significance, SMR Significance, Functional Significance, Effect, Genetic Target, Allele Frequency, Metadata).

The underlying store is "a relational database spanning ten core tables drawn from trusted biomedical resources": Alzheimer's Disease GWAS, Parkinson's Disease GWAS, Alzheimer's and Parkinson's Disease Gene Pathway Associations, Neurodegenerative Disease SMR Associations, Neurodegenerative Disease Allele Frequencies, Drug Gene Targets, Drug Target Indications, Drug Licensing, and Drug Dosages. Table scales range from a few hundred rows (pathway associations) to tens of millions (72.2M rows for allele frequencies, 21.1M for the Alzheimer's GWAS table).

## Domains

Biology and Medicine & Health. The genetics half of the database is human-genomics data — GWAS summary statistics, SMR causal-inference results, allele frequencies, and gene–pathway associations for neurodegenerative disease — and answering those questions requires statistical-genetics conventions, which places the work in Biology. The pharmacology half — drug gene targets, indications, licensing status, and dosages — concerns clinical translation and drug approval, which places it in Medicine & Health. A Computer Science reading is defensible because the emitted artifact is SQL, but the scored objective is retrieval of the biomedically correct records rather than generic database reasoning.

## Evaluation

- **Execution Accuracy (EX):** the primary metric, defined as a "binary metric for each question: a generated query receives a score of 1 only if its executed output matches the gold execution results exactly."
- **Jaccard Index (JAC):** intersection-over-union between predicted and gold execution results, a partial-credit companion to EX.
- **Syntax Error Rate (SER):** the proportion of generated queries that fail to execute.
- **Response Quality Rate (RQR) and Safety Rate (SR):** LLM-judged metrics computed via BioScore, covering the quality of the natural-language response and refusal/safety behavior.
- **Human baseline:** "Two biomedical analysts independently completed a randomly sampled subset of 20 questions drawn from the 546-question test set", with the mean across experts reported — 90.0% EX (95% CI approximately [68%, 99%]), 90% JAC, 95% RQR.
- **Reported.** Under baseline prompting the strongest models are Gemini-3-Pro at 58.1% EX / 62.4% JAC / 81.8% RQR, Claude-4.5-Opus at 54.8% / 59.7% / 80.6%, and GPT-o3-mini at 53.5% / 60.4% / 73.3%. The authors' BMSQL multi-step agent reaches 62.6% EX with GPT-o3-mini, the best overall result and still roughly 27 points below the expert baseline.
- **Configurations compared:** baseline schema prompting, few-shot prompting from 1-shot to 40-shot, sample-table-row prompting (3-row and 5-row), explicit domain statistical-threshold instructions, ReAct prompting, schema indexing, a DAIL-SQL adaptation, and BMSQL multi-step refinement.

## Typical Duration

Baseline and few-shot configurations are single-turn generation against the schema. BMSQL is an iterative text-to-SQL loop that refines its query using intermediate results and execution errors. `TODO(reference)` — the primary source consulted does not state a per-task step cap, wall-clock budget, or token budget.

## Main Contribution

The authors present BiomedSQL as "the first benchmark explicitly designed to evaluate scientific reasoning in text-to-SQL generation over a real-world biomedical knowledge base," distinguishing it from text-to-SQL suites that test schema mapping alone. The claimed contribution is the pairing of a production-scale harmonized biomedical database with questions whose correct translation is underdetermined without domain knowledge, plus a measured expert baseline that quantifies the remaining gap.

## Key Design Ideas

- Questions are written so that the operative filter is *implicit*: the model must know the genome-wide significance threshold, the meaning of effect direction, or which trial phases count, rather than reading it off the prompt.
- A two-axis label scheme separates SQL structural difficulty (eight query-form categories) from biomedical reasoning demand (nine reasoning categories), so failures can be attributed to one axis or the other.
- The database is a real harmonized BigQuery store over heterogeneous public biomedical resources at genuine scale, rather than a synthetic or miniaturized schema.
- Scaling from 40 expert-authored seed queries by programmatic template expansion buys a 68,000-item benchmark while keeping every item traceable to an expert-written form; the 546-question test set is sampled to preserve that template distribution.
- Metrics are layered: exact execution match (EX) as the headline, Jaccard for partial credit, syntax error rate to separate malformed queries from wrong ones, and LLM-judged response and safety rates for the natural-language answer.
- A purpose-built agent (BMSQL) is contributed alongside the benchmark to establish how much of the gap iterative execution feedback can close.

## Strengths

- Grounding in a real, operational biomedical database at tens-of-millions-of-rows scale makes the difficulty representative of analyst work rather than of a curated toy schema.
- The implicit-criteria design isolates a failure mode that syntactic text-to-SQL benchmarks cannot surface, and the two-axis labels make it diagnosable.
- A measured human expert baseline, rather than an assumed ceiling, anchors the reported gap.
- Broad configuration sweep — prompting strategies, few-shot scaling, ReAct, schema indexing, DAIL-SQL, and a multi-step agent — shows that the gap is not an artifact of weak prompting.
- Benchmark, database, and agent code are all publicly released.

## Limitations

- The expert baseline rests on 20 questions completed by two analysts, and the authors' own confidence interval on it is wide (approximately [68%, 99%]), so the 90.0% ceiling is loosely estimated.
- The 68,000 triples are template expansions of 40 seed queries, so item diversity is bounded by those seeds; the effective number of distinct question forms is far smaller than the headline count.
- Repository note: the database is confined to neurodegenerative-disease genetics and drug-approval records, so measured performance may not transfer to other biomedical query domains.
- Repository note: RQR and SR are LLM-judged via BioScore, inheriting judge bias, whereas EX and JAC are execution-grounded; the two families of metric are not equally reliable.
- Repository note: the primary source consulted reports no per-task step, latency, or token budget, so the cost of the BMSQL agent's accuracy gain over single-turn prompting is not quantified here.

## Related Works

- [ALeRCE Text-to-SQL](./alerce-text-to-sql.md) — the same problem shape (natural language to SQL over a real scientific database with expert-authored gold queries) in astronomy rather than biomedicine.
- [BioKGBench](./biokgbench.md) — also makes a biomedical knowledge structure the queried substrate, but scores an agent on finding errors in the graph rather than on translating questions into queries.
- [MedBrowseComp](./medbrowsecomp.md) — biomedical fact retrieval where the answer must be assembled from structured records, evaluated for exact correctness.
- [MedAgentGym](./medagentgym.md) — biomedical data-science tasks in an executable environment, sharing the code-execution grading model.
