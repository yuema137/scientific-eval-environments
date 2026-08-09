# DeepResearch Bench (2025)

> **English** | [简体中文](../zh/works/deepresearch-bench.md)

## Overview

DeepResearch Bench is a benchmark for Deep Research Agents (DRAs) built from 100 PhD-level research tasks across 22 topic domains, paired with two evaluation frameworks: RACE for report-generation quality and FACT for citation grounding and retrieval effectiveness.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.11763>
- **Code:** <https://github.com/Ayanami0730/deep_research_bench>

## Summary

DeepResearch Bench argues that no comprehensive benchmark existed for end-to-end deep research agents, because their internal reasoning and retrieval are not transparent and the final report is therefore the primary interface for assessment — while long-form reports admit no definitive ground truth. The benchmark grounds its topic mix in real demand: 96,147 anonymized user queries from a web-search-enabled LLM chatbot were filtered to 44,019 deep-research queries, classified into 22 WebOrganizer topic domains, and that distribution was proportionally compressed into 100 expert-authored tasks. On top of the task set the paper contributes RACE, a reference-based adaptive-criteria judging framework with dynamic weighting, and FACT, an automated citation-verification pipeline. Both are validated against a human study rather than assumed reliable.

## Tasks

100 tasks, 50 in Chinese and 50 in English. Task counts per domain are set by the measured real-world distribution: 96,147 raw anonymized user queries were filtered by DeepSeek-V3-0324 to 44,019 conforming to the paper's deep-research definition (problems requiring multiple rounds of web search, information gathering, analysis, and a high-quality report), then classified into 22 topic domains from the WebOrganizer taxonomy. That distribution was proportionally compressed to 100 tasks preserving the same topical balance. Tasks were proposed by PhD-holders or senior practitioners with 5+ years of domain experience, then manually screened for quality, clarity, complexity, and alignment with the deep-research definition.

## Domains

22 WebOrganizer topic domains covering general research demand — the paper's examples span science and technology, finance and business, software, art and design, entertainment, history, and transportation. Coverage is driven by observed user demand rather than by a scientific-discipline taxonomy.

## Evaluation

- **RACE (Reference-based Adaptive Criteria-driven Evaluation with dynamic weighting)** scores report quality on four orthogonal top-level dimensions — Comprehensiveness, Insight/Depth, Instruction-Following, Readability.
  - **Dynamic weights and adaptive criteria.** For each task the Judge LLM derives dimension weights `W_d` by averaging over `T` trials, then generates per-dimension tailored criteria with their own weights summing to 1.
  - **Reference-based scoring.** Scoring reports in isolation proved insufficiently discriminative — models assign uniformly high scores — so the Judge LLM scores the target report and a high-quality reference report against every criterion. The final score is relative: `S_final(R_tgt) = S_int(R_tgt) / (S_int(R_tgt) + S_int(R_ref))`, which is why absolute values cluster near 50 and the paper directs attention to rankings and proportional differences rather than raw magnitudes.
  - Reference reports were taken from Gemini-2.5-pro-based Deep Research output collected in April 2025; **Gemini-2.5-pro** is the Judge LLM.
- **FACT (Factual Abundance and Citation Trustworthiness)** is an automated pipeline: extract statement–URL pairs from the report, deduplicate pairs whose statements state the same fact against the same URL, fetch each page via the Jina Reader API, and have the Judge LLM issue a binary support / not-support verdict. It reports **Citation Accuracy (C. Acc.)** and **Average Effective Citations per Task (E. Cit.)**. Gemini-2.5-flash serves as the judge here, chosen as economical for token-heavy verification.
- **Human validation.** 70+ annotators with Master's degrees and relevant domain expertise, three experts per task over 50 tasks and four agents (600 reports), each annotator capped at three queries. Alignment is measured by Pairwise Agreement Rate (PAR), Overall Pearson Correlation (OPC), and Filtered Average Pearson / Spearman (FAP / FAS) computed on the 37 tasks surviving an ICC ≥ 0 filter. RACE (Full) reaches PAR 71.33, OPC 99.54, FAP 60.24, FAS 59.12 (overall 72.56), against a vanilla-prompt baseline at 58.89 / 98.89 / 40.30 / 43.75 — and above the 68.44 human inter-agreement rate on PAR. Ablation shows the reference report is the largest single contributor: removing it drops PAR to 66.56 and FAS to 51.23.
- **Reported (Table 1).** Among Deep Research Agents, Gemini-2.5-Pro Deep Research leads RACE overall at 48.88, then OpenAI Deep Research at 46.98 (which beats Gemini on Instruction-Following, 49.27 vs. 49.18), Perplexity Deep Research 42.25, Grok Deeper Search 40.24. On FACT the ordering differs sharply: Perplexity Deep Research posts the best citation accuracy among DRAs at 90.24 while Gemini-2.5-Pro Deep Research reaches 81.44 with by far the most effective citations at 111.21 per task, against 40.79 for OpenAI Deep Research. Among search-enabled LLMs, Claude-3.7-Sonnet w/Search leads RACE at 40.67 and Claude-3.5-Sonnet w/Search records the highest citation accuracy in the table at 94.04 with only 9.78 effective citations.
- **Judge-model comparison (Table 3).** Gemini 2.5 Pro Preview scores best overall (72.56) at $0.13 per query; o4-mini is cheapest at $0.04 (71.63), o3 costs $0.37 (68.58), Claude 3.7 Sonnet $0.47 (72.28).

## Typical Duration

No per-task step or wall-clock budget is imposed — the evaluated systems are commercial deep research products and search-enabled LLMs run to completion, with `search_context_size` standardized to high for LLMs with search tools. Output scale is indicated by the human study: a single report may run to dozens of pages, and a thorough expert review takes 30–60 minutes.

## Main Contribution

The first specialized benchmark for evaluating Deep Research Agents end to end, constructed from a measured distribution of real user demand, together with RACE and FACT — two evaluation frameworks that the paper validates for human alignment rather than assuming.

## Key Design Ideas

- Task distribution is derived from 96,147 real anonymized user queries rather than authored top-down, so topical balance reflects observed demand.
- Report quality is scored *relative to a reference report*, because absolute LLM-as-a-Judge scoring of long-form reports is insufficiently discriminative.
- Judging criteria and dimension weights are generated per task rather than fixed, so a single rubric need not fit 22 domains.
- Retrieval capability is evaluated by verifying citations against the live web, splitting grounding into precision (Citation Accuracy) and abundance (Effective Citations) instead of one score.
- The evaluation frameworks are themselves benchmarked — against human experts, against ablated variants, and across candidate Judge LLMs with cost reported.
- The authors note RACE and FACT are not confined to deep research: RACE generalizes to text-generation evaluation, FACT to assessing retrieved-information reliability.

## Strengths

- Grounding the topic distribution in a large real query corpus gives the task mix an empirical basis rather than an authorial one.
- The human study is substantial for this setting (600 reports, 70+ qualified annotators) and reports alignment on several complementary metrics, including a filtered subset that controls for low inter-rater agreement.
- RACE's pairwise agreement with experts exceeds the experts' agreement with each other.
- FACT separates citation precision from citation abundance, and the reported results show the two orderings genuinely diverge from RACE rankings.
- Judge-LLM cost is reported alongside quality, making the evaluation's own operating cost visible.

## Limitations

- The authors note benchmark scale is constrained by the expert-authoring process — 100 tasks limits statistical robustness and topic coverage, and expanding it while holding quality is named as a priority.
- The authors note possible domain-coverage bias from in-team curation, and plan external reviewers with specialized domain knowledge.
- The authors note human-evaluation throughput is the binding constraint: three experts per task over 50 tasks is described as modest and susceptible to individual variability.
- The authors note the iteration cycles of the evaluated commercial agents are not transparent, so results are pinned to a stated data-collection timeframe.
- Repository note: Both frameworks are LLM-judge pipelines — RACE scores through Gemini-2.5-pro and FACT's support judgments through Gemini-2.5-flash — so measured quality inherits those judges' reliability, and the reference-based design additionally ties scores to the particular reference reports collected in April 2025.
- Repository note: Evaluation targets the final report and its citations, not the agent's action sequence; the paper states this is deliberate, since the internal retrieval and reasoning processes of commercial DRAs are not observable.

## Related Works

- [TRACE](./trace.md) — Also evaluates deep-research agents, but scores the trajectory via a hierarchical utility function rather than the final report. Repository note: TRACE's companion task set is separately named "DeepResearch-Bench"; the two are distinct works despite the shared name.
- [AutoResearchBench](./autoresearchbench.md) — Also targets agentic research over the web, scoped to literature discovery with an unknown answer-set size rather than report generation.
- [TELBench](./telbench.md) — Complementary view of deep-research agents: span-level error localization within trajectories rather than terminal report quality.
- [GAIA](./gaia.md) — The short-answer, single-unambiguous-answer paradigm for tool-using assistants that report-generation benchmarks like this one deliberately step away from.
