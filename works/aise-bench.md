# AISE-Bench (2026)

> **English** | [简体中文](../zh/works/aise-bench.md)

> **First appeared:** 2026-06-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.20498)

## Overview

AISE-Bench is a full-cycle annotated benchmark for academic information seeking over scholarly knowledge graphs: 1,133 QA pairs shipped with query taxonomies, complete API execution trajectories, validated parameters, and source-grounded answers with reference links, scored on process and outcome together.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.20498>
- **Code:** <https://aise-bench.github.io/>
- **Venue:** KDD 2026 (Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Jeju Island, Republic of Korea) — DOI 10.1145/3770855.3817492

## Summary

Existing tool-using benchmarks for information seeking on academic graphs rely on synthetic templates, simplified solution spaces, or narrow paper-centric tasks, leaving realistic user intent, multi-step API planning, rich parameter filling, grounded answers, and joint process/outcome evaluation underexplored. AISE-Bench addresses all five by annotating each instance end to end — query, plan, executed API calls with validated parameters, and a referenced answer. To make that annotation tractable the authors built a customized agent workflow (Planner, Task Executor, Synthesizer) that lets annotators plan, execute and revise complex API workflows, and they evaluate 14 methods under a protocol that scores answer quality, reference grounding, API-planning correctness, and execution success separately.

## Tasks

1,133 QA pairs, comprising 250 double-reviewed and 883 single-reviewed instances. Tasks run against 9 APIs over the AMiner and Google Scholar academic platforms, covering four entity types — papers, authors, venues, organizations — through entity-search and entity-detail APIs. The query taxonomy is reported along four dimensions: user intention (search papers / authors / venues / organizations), knowledge level (memorization versus understanding, with examples, comparison, comprehension and summarization subcategories), planning steps (2 to 5+ API calls), and first-level academic discipline. Per-category counts are TODO(reference).

## Domains

Scholarly information seeking over academic knowledge graphs spanning first-level academic disciplines; the queried objects are papers, authors, venues and organizations rather than the scientific content of any one field. No canonical science or engineering domain is assigned, as the benchmark is discipline-agnostic by design.

## Evaluation

A protocol with three metric groups, covering both the process and the outcome:

- **References / formatting:** reference precision, reference recall, and format compliance.
- **API process:** Planning Graph Edit Distance between the agent's plan and the annotated plan, parameter accuracy, and execution success rate.
- **Answer content:** correctness, completeness, faithfulness, and F1-LM.
- **Reported.** 14 methods are evaluated across three families — six LLMs under the customized agent workflow, four API-using agent frameworks, and coding / deep-research systems. The best result is PLAY2PROMPT at F1-LM 0.6104; Gemini-3-Pro leads the customized-workflow family at F1-LM 0.5606; CodeAct reaches 0.5130 and Perplexity 0.3952. Most methods obtain high partial-completion scores (0.82–0.95) but substantially lower parameter accuracy, which the authors identify as the main bottleneck.

## Typical Duration

Tasks are stratified by planning depth, from 2 to 5+ API calls per query. Wall-clock and token budgets are TODO(reference).

## Main Contribution

A real-world, full-cycle annotated benchmark for multi-step API-using agents on academic knowledge graphs, in which every instance carries not just a gold answer but the validated plan, parameters and execution trace needed to grade the process — plus an annotation workflow that makes producing such supervision feasible at scale.

## Key Design Ideas

- Annotation is full-cycle: query taxonomy, execution trajectory, validated API parameters and reference-grounded answer are all recorded, so process metrics have gold references rather than heuristics.
- Planning quality is measured as graph edit distance against the annotated plan, which tolerates ordering differences that a strict sequence match would penalize.
- Parameter filling is scored as a first-class metric, isolating a failure mode that end-answer accuracy hides.
- A customized annotator-facing agent (Planner / Task Executor / Synthesizer) is used as annotation infrastructure rather than as the system under test.
- Queries are stratified by planning depth and knowledge level, so difficulty is a controlled dimension rather than an emergent property.

## Strengths

- Rejects synthetic templates in favour of curated real-intent queries with human review.
- Process and outcome are reported separately, so a correct answer reached by a wrong plan is visible.
- Answers are required to be source-grounded with reference links, making faithfulness checkable.
- Code and data are released, and the work is peer-reviewed at KDD 2026.

## Limitations

- Only 250 of 1,133 instances are double-reviewed; the remaining 883 rest on a single annotation pass.
- The benchmark is bound to the AMiner and Google Scholar API surfaces, so scores depend on those live services and on API stability over time.
- Per-category counts within the four-dimension query taxonomy are not reported — TODO(reference).
- Repository note: the academic knowledge graph is the agent's queried substrate; the benchmark does not evaluate construction, curation or maintenance of the graph itself.

## Related Works

- [ScholarQuest](./scholarquest.md) — Also benchmarks agentic academic literature search, over open literature retrieval rather than structured graph APIs.
- [MedBrowseComp](./medbrowsecomp.md) — Also requires multi-hop retrieval from live domain knowledge bases with verifiable grounding, in medicine.
- [BioKGBench](./biokgbench.md) — Also evaluates agents acting over a knowledge graph, checking graph facts rather than seeking information through APIs.
- [Toolathlon](./toolathlon.md) — Also evaluates multi-step real API use as the core competence under test.
