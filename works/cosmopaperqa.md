# CosmoPaperQA (2025)

> **English** | [简体中文](../zh/works/cosmopaperqa.md)

## Overview

CosmoPaperQA is a 105-pair cosmology question-answering dataset built from five highly cited cosmology papers, used to evaluate nine retrieval-augmented-generation (RAG) agent configurations against expert human grading and to calibrate an LLM-as-a-Judge grader as a proxy for that human evaluation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.07155>
- **Dataset:** <https://huggingface.co/datasets/ASTROANTS/CosmoPaperQA>
- **Code:** <https://github.com/CMBAgents/scirag>
- **Venue:** ICML 2025 Workshop on Machine Learning for Astrophysics (accepted spotlight contribution)

## Summary

The work starts from the observation that existing astronomy QA resources are largely synthetic — AstroMLab 1's 4,425 AI-generated multiple-choice questions and Astro-QA's 3,082 questions are cited as the comparison points — and instead extracts questions directly from real research papers. A team of expert cosmologists wrote 105 question-answer pairs spanning three complexity tiers: factual retrieval of specific parameters, synthetic reasoning that integrates multiple pieces of evidence, and analytical interpretation requiring deep domain expertise. Nine RAG configurations were run over the same five-paper corpus, producing 945 answers, all of which a single PhD-level domain expert graded by hand. Those 945 human grades were then used to calibrate two LLM judges, which reproduced the human ranking of systems closely enough (Pearson r > 0.99 across evaluation methods) for the authors to propose LLM-as-a-Judge as a scalable substitute for expert grading.

## Tasks

105 expert-written question-answer pairs drawn from five highly cited cosmology papers: the Planck 2018 cosmological-parameter results, the CAMELS machine-learning simulation suite, a local Hubble-constant measurement, a "cosmology with one galaxy" analysis, and Atacama Cosmology Telescope DR6 constraints. Questions are organised into three complexity tiers — factual retrieval of specific parameters, synthetic reasoning integrating multiple evidence sources, and analytical interpretation demanding deep domain expertise. Nine RAG configurations were evaluated: three commercial assistants (OpenAI Assistant with GPT-4.1 and text-embedding-3-large; OpenAIPDF Assistant, the same stack on raw PDFs; VertexAI Assistant with Gemini 2.5 Flash and text-embedding-005), two hybrid embedding/generation pairings (HybridOAIGem, HybridGemGem), two academic retrieval tools (PaperQA2 and a domain-adapted Modified PaperQA2), and two non-RAG baselines (a Gemini Assistant with no retrieval and a web-searching Perplexity Assistant). Retrieval used top-k = 20 over 5,000-token chunks with 250-token overlap, at temperature 0.01.

## Domains

Astronomy. Every question is drawn from cosmology literature — CMB power-spectrum and parameter results, Hubble-constant measurements, cosmological simulations, and galaxy-level cosmological inference — so the evaluated objective is astrophysical domain understanding rather than generic reading comprehension. Physics is a secondary co-domain through the cosmological-parameter physics the questions probe.

## Evaluation

Binary grading: an answer scores 1 when it is factually accurate and captures the essential scientific understanding of the ideal answer, and 0 when it contains errors or misses core concepts; scores are scaled to 0–100 for reporting. A single domain expert with PhD-level cosmology expertise graded all 945 responses (9 systems × 105 questions) by hand. The human grades were then used to calibrate two LLM judges, OpenAI o3-mini and Gemini 2.5 Pro, applied to the same responses. Reported accuracies: OpenAI Assistant 91.4%, OpenAIPDF Assistant 89.5%, VertexAI Assistant 86.7%, HybridOAIGem 85.7%, HybridGemGem 84.8%, PaperQA2 81.9%, Modified PaperQA2 73.3%, Perplexity Assistant 17.1%, Gemini Assistant (no retrieval) 16.2%. The judges are biased in opposite directions — the OpenAI judge scores 2–8 percentage points below the human expert, the Gemini judge 5–15 points above — but both preserve the ranking, which is the basis for the LLM-as-a-Judge proxy claim.

## Typical Duration

N/A — single-turn question answering over a fixed five-paper corpus, with no multi-step trajectory, wall-clock, or token budget reported. The paper notes a 4,096-token document-processing constraint for the OpenAI Assistant, and Appendix E reports per-query cost rather than latency: $0.000357 per query for VertexAI versus $0.048798 for the OpenAI-based systems (a factor of 136.7), giving $0.037 versus $5.12 for a full 105-question run.

## Main Contribution

A cosmology QA dataset whose questions are extracted from authentic research papers rather than generated synthetically, a systematic head-to-head comparison of nine RAG configurations on it under uniform retrieval settings, and — using 945 hand-graded answers as ground truth — a calibrated LLM-as-a-Judge grader offered as a robust proxy for expert human evaluation.

## Key Design Ideas

- Questions are written by expert cosmologists from real papers, not generated by a model, to avoid the synthetic-question bias the authors attribute to AstroMLab 1 and Astro-QA.
- Three deliberate complexity tiers separate parameter lookup from multi-source synthesis and from interpretive reasoning.
- All nine configurations share the same corpus, chunking (5,000 tokens, 250-token overlap), retrieval depth (top-k = 20), and temperature (0.01), so the comparison isolates the embedding and generation choices.
- Two non-RAG baselines — a bare Gemini assistant and a web-searching Perplexity assistant — bound how much of the accuracy comes from retrieval over the specific papers.
- Judge calibration is empirical: the LLM judges are validated against the full set of 945 human grades rather than a sample, and both their absolute bias and their rank fidelity are reported.
- Hybrid configurations deliberately cross vendors (OpenAI embeddings with Gemini generation, and vice versa) to separate the contribution of the embedding model from that of the generative model.

## Strengths

- Grading ground truth is a complete human-expert pass over every answer, not a subsample or an automatic proxy.
- The judge-calibration result is reported with its failure mode rather than as a single agreement number: both judges are systematically biased in absolute terms, and only the ranking is claimed to transfer.
- The retrieval-free and web-search baselines score 16–17%, which makes the gap attributable to corpus retrieval unusually legible.
- Dataset and pipeline are publicly released (HuggingFace and the SciRag repository), so the comparison is reproducible.
- Cost per query is reported alongside accuracy, exposing a 136.7× spread between configurations that differ by under five accuracy points.

## Limitations

- The authors note that many questions explicitly reference their source papers, which may systematically inflate RAG performance by supplying retrieval cues.
- The five-paper corpus is far smaller than a realistic research setting where a system must search thousands of papers; the authors expect accuracy to degrade at scale.
- Human evaluation limits scalability, which is the motivation for the judge calibration but also means the ground truth cannot be extended cheaply.
- Repository note: all 945 grades come from a single expert, so inter-annotator agreement on the binary rubric is not measurable.
- Repository note: the evaluated systems are retrieval assistants answering single questions, not agents executing multi-step trajectories, so the results speak to retrieval and answer quality rather than to planning, tool use, or recovery from error.
- Repository note: the reported accuracies are single-pass, with no repeated-run variance despite the near-deterministic but non-zero temperature setting.

## Related Works

- [LAB-Bench](./lab-bench.md) — its LitQA2 subtask is the closest analogue, literature-grounded QA for scientific agents in biology rather than cosmology.
- [ScholarQuest](./scholarquest.md) — also evaluates literature-facing agents, but scores open-literature search rather than answer accuracy over a fixed corpus.
- [ReplicationBench](./replicationbench.md) — same astrophysics domain, evaluating agents on replicating paper results rather than answering questions about them.
- [Stargazer](./stargazer.md) — astronomy agent evaluation on quantitative model fitting, complementary to this work's knowledge-retrieval focus.
