# SGR-BIM (2026)

> **English** | [简体中文](../zh/works/sgr-bim.md)

## Overview

SGR-BIM is a graph-driven multi-agent framework for checking geometry-intensive building-code provisions against IFC building models, released together with a purpose-built evaluation set of 679 expert-verified fire-safety compliance queries over five IFC models and a four-dimension scoring rubric, on which five agent baselines — including CAMEL, MetaGPT and AutoGen — are compared under identical tool access and inference settings.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12065>
- **Publisher record:** <https://doi.org/10.1016/j.autcon.2026.107038>
- **Venue:** Automation in Construction, Volume 189, article 107038 (2026)

## Summary

Automated compliance checking has long handled attribute-level rules ("is this wall's material X?") but stalls on geometry-intensive provisions, where a verdict requires chaining several clauses and traversing relationships between IFC entities — deciding the required exit-door width, for instance, means first inferring the building's use classification, looking up the occupancy factor, summing room areas, and only then comparing a door dimension. The paper argues that static rule templates cannot express these multi-hop chains, and proposes SGR-BIM, which dynamically builds a cross-modal knowledge graph aligning user intent, regulatory semantics and IFC geometry, with five agents (intent, model, rule, analysis, response) reasoning over the shared graph. To measure this, the authors construct an evaluation set of 679 fire-safety queries with expert-produced ground truth and score every system on a three-tier accuracy scale plus three qualitative dimensions. SGR-BIM reaches 84.3% overall accuracy against 75.7% for a single agent with the same full toolset and 64.9–73.2% for the general-purpose multi-agent frameworks.

## Tasks

679 questions derived from BIM-based design-review scenarios, built over five IFC models chosen for use-classification and scale diversity: two multi-storey residential apartment buildings, one dormitory, one commercial office building, and one industrial factory. Models were obtained from publicly available sources and refined by a three-person BIM team (all with over a year of BIM experience, including one industry practitioner). Questions were produced semi-structurally: domain experts analysed each IFC model and wrote seed questions targeting key regulatory and geometric reasoning challenges, LLMs expanded the seeds for coverage and diversity, and the expert team then manually reviewed and validated every generated question. Ground-truth answers were produced entirely by domain experts from joint analysis of the regulatory provisions and the corresponding BIM model. The set splits across two workflow phases and four categories: design-stage **Rule** questions asking for geometry-related code provisions (113 items, e.g. maximum allowable fire-compartment area) and **Rule Requirement** questions asking what a specific element must satisfy (189, e.g. the clear width the code requires for a given door); check-stage **Model** questions retrieving geometric or spatial facts from the IFC model (240, e.g. which floor a room is on) and **Check** questions asking whether an element complies (137, e.g. does this stair meet code). Difficulty is characterized along three dimensions: 79.65% of Rule queries require simultaneously interpreting two or more distinct regulatory clauses; geometric computing accounts for 53.97%–85.40% of items in the other three categories; and relational dependencies (navigating topological or logical links between two or more IFC entities) reach 10.05% (Rule Requirement), 40.00% (Model) and 44.52% (Check). Table-lookup operations appear across all categories, and each category for every building model contains 1–2 conditional exceptions to test edge cases where a standard rule is superseded.

## Domains

Civil & Structural Engineering. The evaluated objective is design verification of a building against building-code provisions: fire-compartment areas, means of escape and travel distances, occupant capacity derived from use classification and room area, stair and corridor widths, clearances and exit-door dimensions, all checked against IFC geometry. This falls under the domain's design-code compliance and code-checking scope and its BIM/IFC clause, where the evaluated task is engineering verification rather than BIM authoring or space planning for its own sake. The work comes from the University of Hong Kong Department of Urban Planning and Design and HKUST Department of Civil and Environmental Engineering. No structural analysis, load path, or member design is evaluated, so no Mechanical & Aerospace or Materials Science co-domain is assigned; the tasks are building-code verification, not structural mechanics.

## Evaluation

Four evaluation dimensions are defined. **Accuracy** is the primary metric, scored on a three-tier scale: 1 (fully correct) only when the response reaches the correct conclusion *and* identifies all governing regulatory variables and situational boundary conditions; 0.5 (partially correct) when the right regulatory mechanism or IFC entities are identified but the conclusion is imprecise or misses thresholds and edge cases; 0 when both conclusion and reasoning path are wrong or hallucinated. **Coherence**, **Relevance**, and **Explainability & Reasoning** are scored 0–1 against published criteria (no unnatural references or raw GUIDs, proper units, direct answering without digression, a transparent reasoning chain with exceptions explained). Accuracy is human-scored; the three qualitative dimensions are produced by an independent LLM judge (DeepSeek-3.2, with system and baseline names stripped from the judging prompts) and then verified by manual inspection, with discrepancies between judge and reviewers or among reviewers resolved by consensus reconciliation. All systems run under identical tool access and inference settings, with DeepSeek-3.2 as the default backend at temperature 0; the full experiment is a single run, justified by deterministic decoding and the annotation cost of the 679-item set. Baselines span a deliberate capability ladder: a Basic-tool Agent (rule text and BIM attribute retrieval only), an Enhanced-tool Agent (the full domain toolset used by SGR-BIM, isolating tool availability from coordination), and the CAMEL, MetaGPT and AutoGen multi-agent frameworks. Overall average scores: SGR-BIM 84.3, Enhanced-tool Agent 75.7, CAMEL 73.2, AutoGen 70.2, MetaGPT 64.9, Basic-tool Agent 19.1; per-category, SGR-BIM scores 90.7 (Rule), 78.6 (Rule Requirement), 87.9 (Model) and 80.7 (Check). A Tukey HSD pairwise test over per-question results finds SGR-BIM significantly ahead of every baseline, including the Enhanced-tool Agent (+0.0862, p = 0.0008); CAMEL and AutoGen are not significantly different from the Enhanced-tool Agent. On the qualitative dimensions SGR-BIM scores 93.7 coherence, 98.4 relevance and 99.3 explainability overall, against 79.2 / 96.7 / 70.4 for the Enhanced-tool Agent. Error analysis over the 135 non-perfect responses (19.9% of the set) classifies failures into incomplete answer (42.2%), faulty reasoning and inference (24.4%), insufficient understanding of model or rule information (14.8%), systemic tool/system error (14.8%), and misunderstanding of user intent (3.7%). A backend-substitution study on a subsample re-runs SGR-BIM with GPT-4o, giving 74.2 overall against 87.6 for DeepSeek-3.2 on the same subsample, with the largest gaps in the geometry-heavy Check (51.7 vs 85.0) and Rule Requirement (57 vs 76.7) categories.

## Typical Duration

N/A — each item is a single query resolved through iterative tool invocation by the agents, and the paper reports no per-query wall-clock time, step count, or token budget; deterministic decoding at temperature 0 and a single experimental run are the only cost-related settings stated.

## Main Contribution

The authors present SGR-BIM as a graph-based semantic reasoning paradigm for automated compliance checking, replacing rigid rule templates with a dynamically constructed cross-modal knowledge graph that aligns user intent, regulatory semantics and IFC geometry so that multi-hop geometric rule chains can be traversed and the reasoning made inspectable. The accompanying empirical claim is that generic multi-agent collaboration is not what closes the gap: general-purpose frameworks (CAMEL, AutoGen) are statistically indistinguishable from a single agent with good tools, and only explicit cross-modal alignment yields a significant improvement.

## Key Design Ideas

- A cross-modal knowledge graph built at query time, aligning natural-language user intent, narrative and tabular code clauses, and IFC entities into one reasoning space, rather than pre-compiling rules into fixed templates.
- Five role-specialized agents (intent, model, rule, analysis, response) operating over the shared graph, so intermediate entity linkages are visible to every role.
- Deterministic retrieval tools: rule lookup and IFC geometric query are wrapped as plain functions over pre-processed sources, deliberately excluding RAG and SPARQL so that measured differences reflect reasoning and alignment rather than retrieval quality.
- A baseline ladder designed to disentangle three separate contributions — tool availability, multi-agent coordination, and cross-modal alignment — instead of a single headline comparison.
- A three-tier accuracy scale that withholds full credit from answers that reach the right conclusion without identifying the governing variables and boundary conditions, so lucky or shallow correctness is separated from regulatory understanding.
- Question difficulty characterized by explicit structural properties (number of regulatory sources, geometric computing, relational dependencies) and seeded with 1–2 conditional exceptions per category per model, giving edge cases where a default rule is superseded.
- Separation of scoring channels: accuracy human-scored, qualitative dimensions LLM-judged with system identities anonymized and then human-audited.

## Strengths

- The evaluation set is grounded in five real IFC models of different building types with expert-authored ground truth, so answers depend on the actual geometry of a model rather than on recalled code text.
- Baselines include three independently published multi-agent frameworks under identical tool access and backend, which is a stronger comparison than an ablation of the authors' own system.
- Statistical significance is tested with Tukey HSD on per-question results, and the paper reports where differences are *not* significant, including for two of its multi-agent comparators.
- The error taxonomy is computed over all non-perfect responses rather than a hand-picked sample, and is broken down per question category.
- The backend-substitution study separates what the framework contributes from what the underlying model contributes, showing the ordering is preserved while absolute accuracy shifts.

## Limitations

- Neither the source code nor the question dataset is released: the data availability statement says both "will be made available upon reasonable request", so the 679-query set cannot currently be used as a public benchmark.
- The whole evaluation is a single run at temperature 0, justified by determinism and annotation cost; no variance estimate across runs is reported.
- The authors note that an enhanced-tool single agent already handles over 75% of queries, so the framework's advantage concentrates in the harder items and gives diminishing returns on simple ones.
- Retrieval is deliberately simplified — deterministic function calls over pre-processed sources rather than RAG or SPARQL — so the results do not speak to end-to-end performance where code text and IFC data are messy or unindexed.
- Scalability to large, high-density IFC models (high-rise healthcare facilities, complex industrial plants) is untested; the authors expect graph alignment search space and coordination memory to grow non-linearly.
- Repository note: the paper describes its validation domain only as "fire safety codes" and does not name the jurisdiction or the specific code document from which the provisions are drawn, so the regulatory basis of the ground truth cannot be independently checked. TODO(reference)
- Repository note: the benchmark is unnamed and embedded in a framework paper — the evaluation set was constructed to validate SGR-BIM, and two of the four question categories (Rule, Model) test code lookup and IFC fact retrieval rather than a compliance verdict, so only the 137 Check items and, partly, the 189 Rule Requirement items pose an end-to-end engineering-verification task.
- Repository note: the three qualitative dimensions are reported only for SGR-BIM and the Enhanced-tool Agent, not for the three multi-agent baselines, so the coherence and explainability comparison is narrower than the accuracy comparison.

## Related Works

- [StructureClaw](./structureclaw.md) — structural-engineering agent benchmark that also scores code checks, but through solver execution and strict artifact matching rather than expert-graded answers.
- [SoM-1K](./som-1k.md) — civil/structural benchmark on the mechanics side of the same field, where the deliverable is a worked analytical solution rather than a code verdict.
- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction dataset whose CODE intent type covers design-code and standards questions across nine fields, including civil.
- [EnergyBridge](./energybridge.md) — another agent evaluation grounded in executable building models, scoring plans against building-simulation state rather than regulatory provisions.
