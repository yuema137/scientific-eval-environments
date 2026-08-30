# HiSciBench (2025)

> **English** | [简体中文](../zh/works/hiscibench.md)

> **First appeared:** 2025-12-28 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2512.22899)

## Overview

HiSciBench is a hierarchical multi-disciplinary benchmark of 8,735 instances that arranges scientific capability into five ascending levels — factual literacy, literature parsing, literature question answering, literature review generation, and data-driven scientific discovery — across mathematics, physics, chemistry, biology, geography and astronomy, with multimodal and cross-lingual inputs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.22899>

## Summary

The benchmark is built on the premise that "scientific intelligence" is not a single capability but a ladder that runs from reading to discovery, and that a model can look competent at the bottom while failing at the top. Seven tasks are grouped into five levels: L1 general scientific question answering, L2 literature OCR and literature translation, L3 monolingual and cross-lingual literature question answering, L4 topic-guided literature review generation, and L5 data-driven scientific discovery in which the model must write and execute Python analysis code. Each level carries its own scoring protocol, from plain accuracy at the bottom through LLM-as-judge rubrics and citation-verification metrics at L4 to execution-based success rate at L5. Eighteen models are evaluated, including closed and open-weight text models, vision-language models and research-oriented specialised systems, and the reported pattern is a steep decline in performance as the level rises.

## Tasks

8,735 instances across seven tasks and six disciplines. Per Table III of the paper: **L1.1 General Scientific QA**, 1,200 multiple-choice questions testing factual recall, evenly split at 200 per discipline (mathematics, physics, chemistry, astronomy, geography, biology); **L2.1 Literature OCR**, 629 instances requiring extraction of text, tables and formulas from scientific PDFs (mathematics 208, physics 357, astronomy 19, biology 45); **L2.2 Literature Translation**, 629 instances with the same discipline split, translating scientific documents across languages; **L3.1 Monolingual Literature QA**, 5,514 instances answering questions within single papers (mathematics 821, physics 1,025, chemistry 886, astronomy 330, geography 500, biology 1,952); **L3.2 Cross-lingual Literature QA**, 629 instances where the question language differs from the source document (mathematics 208, physics 357, astronomy 19, biology 45); **L4.1 Topic-guided Literature Review**, 60 review-generation topics, 10 per discipline; and **L5.1 Data-driven Scientific Discovery**, 74 instances in which the model receives a research problem, a dataset and domain background, and must formulate an approach, implement it in Python, execute the analysis and interpret the results (chemistry 20, geography 27, biology 27). L2 and L3.2 source their documents from arXiv. Languages covered are English as the primary language with Chinese for the cross-lingual and translation tasks.

## Domains

Astronomy is one of the six named disciplines, contributing 597 instances in total: 200 general scientific QA items, 19 literature OCR documents, 19 literature translation documents, 330 monolingual literature QA pairs, 19 cross-lingual literature QA pairs and 10 literature-review topics. The astronomy tasks are literature-facing — parsing, translating, answering questions about and synthesising reviews from astronomy papers sourced from arXiv — rather than observational data analysis; astronomy contributes no L5.1 discovery instances, which are drawn only from chemistry, geography and biology. Co-domains follow the remaining disciplines: Mathematics, Physics, Chemistry, Biology, and Earth Science (the paper's "geography" discipline).

## Evaluation

Each level has its own protocol. L1 and L3 are scored by classification accuracy against reference answers. L2.1 literature OCR is scored by word-level accuracy against the reference extraction. L2.2 literature translation is scored by BLEU. L4.1 splits into content quality and citation quality: content is graded by LLM-as-judge on a 1–5 scale across five dimensions — Coverage (comprehensiveness with which the review addresses the topic), Structure (logical organisation and coherence), Relevance (degree to which content pertains to the topic), Synthesis (effectiveness of integrating ideas across sources) and Critical Analysis (depth of methodological critique and identification of research gaps) — while citations are scored on verifiability rate, metadata accuracy, faithfulness rate and a recency measure. L5.1 uses an execution-based Success Rate that assesses whether the generated program's outputs meet the task-specific success criteria, such as achieving target performance on held-out test data; if the code fails to execute or produces invalid results the success rate is set to zero. Eighteen models were evaluated, spanning GPT-5, DeepSeek-V3, DeepSeek-R1, Llama-3.1-Instruct-70B, Qwen3-32B, QwQ-32B, DeepSeek-R1-Distill-Qwen-32B, the vision-language models Qwen3-VL-8B, Qwen2.5-VL-7B, InternVL3-8B, InternVL3.5-8B and GLM-4.5V, and research-oriented specialised systems including Tongyi-DeepResearch and SurveyX. The headline result is a sharp decline across the hierarchy: GPT-5 reaches up to 69% accuracy on the basic literacy tasks but falls to 25% on discovery-level challenges. Citation hallucination is reported as severe, with general-purpose models scoring verifiability rates below 20% against 71.4% for the specialised research systems.

## Typical Duration

N/A — the paper reports no per-instance trajectory length, wall-clock budget or token budget. L1 through L4 are single-turn generation tasks; L5.1 requires code generation and execution but is scored on the outcome rather than on a bounded interaction budget.

## Main Contribution

A hierarchical rather than flat organisation of scientific benchmarking: instead of a single difficulty axis, HiSciBench separates reading-level competence from synthesis-level and discovery-level competence, so that the point at which a model's scientific ability breaks down can be located rather than averaged away. The authors pair this with multimodal document inputs and cross-lingual evaluation, and with citation-quality metrics that expose hallucinated references at the review-generation level.

## Key Design Ideas

- Five ascending levels, from factual recall to autonomous data-driven discovery, so that aggregate scores decompose into a capability profile instead of one number.
- Level-appropriate metrics rather than one universal scorer: accuracy at L1/L3, word-level accuracy at L2.1, BLEU at L2.2, rubric-based LLM judging plus citation verification at L4, and execution-based success rate at L5.
- Citation quality is measured separately from content quality at the review level, isolating reference fabrication as its own failure mode.
- L5 grounds discovery in executable code over a supplied dataset, so the score depends on a program that runs and meets stated criteria rather than on a plausible narrative.
- Literature tasks are built on real papers sourced from arXiv, with document images retained so that multimodal parsing is part of the pipeline rather than assumed away.
- A cross-lingual track pairs English source documents with Chinese questions and translations, separating scientific understanding from language of presentation.
- The model panel deliberately mixes general text models, vision-language models and purpose-built research systems, which is what makes the citation-verifiability contrast between them measurable.

## Strengths

- The hierarchy is operationalised, not just asserted: each level has distinct instances, distinct inputs and a distinct scoring protocol.
- The per-discipline instance table makes the composition auditable, including the fact that some levels do not cover all six disciplines.
- Execution-based scoring at L5 avoids crediting unverifiable discovery claims.
- Citation verifiability is a directly measurable quantity and the reported spread between general and specialised systems is large enough to be actionable.
- Eighteen models across several architectural families give the level-wise decline a broad base.

## Limitations

- The benchmark is unevenly distributed across disciplines and levels: astronomy has 19 instances at three of the seven tasks and none at L5.1, so the discovery-level conclusions rest on chemistry, geography and biology only.
- L3.1 dominates the instance count (5,514 of 8,735), so an aggregate score is largely a monolingual literature-QA score.
- L2.2 literature translation is scored by BLEU, which measures surface overlap rather than scientific correctness.
- The paper states that the benchmark "will be publicly released" but records no repository or dataset URL, so the artifact could not be inspected.
- Repository note: the tasks are predominantly single-turn generation; only L5.1 involves code execution, and no task requires multi-step tool use, planning or recovery, so the benchmark measures scientific model capability more than agent behaviour.
- Repository note: the astronomy slice is entirely literature-facing — parsing, translating, answering questions about and reviewing astronomy papers — and contains no observational data analysis, so it probes domain reading comprehension rather than astronomical inference.
- Repository note: L4 content scoring depends on an LLM judge whose agreement with human expert graders is not reported.

## Related Works

- [Humanity's Last Exam](./hle.md) — another broad multi-disciplinary scientific benchmark with an astronomy component, scored as single-turn question answering.
- [CosmoPaperQA](./cosmopaperqa.md) — astronomy literature QA built from real papers with expert-written answers, the narrow-domain counterpart to this work's L3 level.
- [ScholarQuest](./scholarquest.md) — evaluates literature-facing agents on open search rather than fixed-corpus reading.
- [ScienceAgentBench](./scienceagentbench.md) — data-driven scientific task execution scored on runnable code, comparable to this work's L5 level.
- [MaScQA](./mascqa.md) — a named, sized domain QA benchmark evaluated across multiple models, sharing this work's exam-style lower levels.
