# DiscoveryBench (2024)

> **English** | [简体中文](../zh/works/discoverybench.md)

> **First appeared:** 2024-07-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2407.01725)

## Overview

DiscoveryBench asks an agent to find a hypothesis rather than compute an answer. Earlier data-analysis suites fixed the question and the answer form — run this test, produce this number, pass this assertion — so an agent that picked the right library usually scored. DiscoveryBench hands over one or more datasets, their column metadata, and a discovery goal written in natural language, and leaves the analysis workflow entirely to the agent. Scoring then compares the declarative hypothesis it returns against a gold hypothesis replicated from a published paper, decomposed into three dimensions — context, variables, relationship — so a run that finds the right variables under the wrong population is separated from one that finds nothing.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.01725>
- **Code:** <https://github.com/allenai/discoverybench>
- **Venue:** ICLR 2025

## Summary

From the Allen Institute for AI, OpenLocus, and UMass Amherst, DiscoveryBench formalizes a data-driven discovery task as: given task datasets *D* and a discovery goal *G*, derive the hypothesis *h* = ψ(*c*, *v*, *r*) with the highest specificity for context *c*, variables *v*, and relationship *r* that *D* supports. Its real split (DB-Real) replicates the analysis workflow of over 20 published papers in Python and takes the papers' findings as gold hypotheses; its synthetic split (DB-Synth) generates datasets bottom-up from a hypothesis semantic tree so that workflow depth can be varied on demand. Because the hypothesis is scored dimension by dimension, the paper can report *where* agents break down rather than only that they do: the best system reaches 25%, and biology tasks — which lean hardest on advanced statistical methods — score 0%. The score still depends on a GPT-4 evaluator, which the authors audit rather than assume.

## Tasks

**DB-Real: 264 tasks (25 train, 239 test)** across six scientific domains — sociology, biology, humanities, economics, engineering, and meta-science — with 14 unique gold hypotheses in train and 144 in test. Test-split tasks by domain: meta-science 100, sociology 58, humanities 38, biology 16, engineering 15, economics 12. Each task supplies one or more datasets, a dataset and column description, background knowledge about the domain, and a discovery goal; 114 tasks (4 train, 110 test) require more than one dataset, with a maximum of six for a single task, and the suite contains over 500 instances of data-preparation activity such as cleaning, deduplication, and integration.

Task construction ran two routes. The **data-first** route filtered papers built on open public datasets — the National Longitudinal Surveys, the Global Biodiversity Information Facility, and World Bank Open Data — and replicated their workflows in Python, taking 15 to 40 person-hours per NLS-related paper and up to 90 person-hours for the GBIF dataset, with roughly 30% of attempts failing. The **code-first** route searched 785 data points in Zenodo for computational notebooks; over 85% of repositories had missing code, code that would not translate to Python, or a proprietary dataset, leaving a candidate list of 14 repositories of which 3 passed all checks. Every implementation workflow was manually verified by the authors for solvability, with Economics PhDs consulted for the economics and sociology hypotheses.

**DB-Synth: 903 tasks over 48 domains**, split 80/20 into development and test and labeled with difficulty 1–4. An LLM samples a domain, builds a hypothesis semantic tree whose root is the target variable, operationalizes each edge as a pandas expression, generates the columns bottom-up from leaves to root, and then perturbs values with noise and missing entries.

## Domains

Six domains in DB-Real: sociology, biology, humanities, economics, engineering, and meta-science. The biology tasks come from two published studies — accelerated body-size evolution in upland environments correlated with recent speciation in South American freshwater fishes, and the effect of introduction pathways on the invasion success of non-native plants along environmental gradients. The engineering tasks analyze a survey of industrial requirements-engineering practice for ML-enabled systems; humanities tasks are archaeological; meta-science tasks study shrinkage and heterogeneity in large-scale replication projects.

## Evaluation

- **Hypothesis Matching Score (HMS).** A `gpt-4-preview-0125` evaluator extracts the context, variables, and relationship of both the gold and the predicted hypothesis, matches predicted sub-hypotheses to gold ones by context equivalence, and computes `HMS = ctx_align × var_F1 × rel_acc`, scaled to [0, 100]. Relationship accuracy is scored 1 for an exact match, 0.5 when the predicted relationship is broader but encompasses the gold one, and 0 otherwise.
- **One item, end to end.** For the gold hypothesis *"The effect of socioeconomic status on college degree completion is higher for females (0.4995) than males (0.4467)"*, the authors mask the relationship and hand the agent the goal *"How does socioeconomic status impact college degree completion for females compared to males?"* together with the NLS dataset. The agent must clean and join the data, choose and run an appropriate analysis, and return a declarative sentence; HMS then checks whether it named the same population, the same variables, and the same direction and form of the relationship.
- **Evaluator audit.** Two authors independently checked the step-by-step LLM evaluation on 200 examples; after resolving disagreements, GPT-4 was 97% correct in context extraction, 99% in context matching, 94% in variable extraction, and 99% in assessing relationship accuracy.
- **Human alignment.** Three annotators ranked two predicted hypotheses against the gold hypothesis for 100 random pairs from the DB-Real test set. Human preference rankings agree with HMS-based rankings 95% of the time, with Fleiss κ = 0.91 among annotators, and the null hypothesis of a difference between human and HMS rankings is rejected at *p* < 0.001.
- **Reported.** Across CodeGen, ReAct, DataVoyager, and Reflexion (Oracle) agents over GPT-4o, GPT-4-preview-0125, and Llama-3-70B, the best system scores only 25% — Reflexion (Oracle) with GPT-4o at 24.6 HMS on DB-Real, with ReAct + GPT-4o the best non-oracle agent at 24.4. The `NoDataGuess` baseline, which answers from the dataset description and goal without touching the data, scores 0.0 (GPT-4o), 4.7 (GPT-4p), and 11.5 (Llama-3-70B). By domain, the best non-oracle agent reaches 0% on biology and 7% on engineering against 25% on economics and 23% on sociology. By workflow category, its top three are correlation analysis, time-series analysis, and social-science-related analysis, and its bottom three are spatial analysis, pollen modeling, and ecological modeling.
- **Domain-knowledge ablation.** For the archaeology tasks, which needed substantial domain knowledge during data collection, the authors supply that knowledge as an additional hint. DataVoyager with GPT-4-preview-0125 rises from 9.9% without it to 25.4% with it, which locates part of the failure in missing background rather than in analysis ability.
- **Qualitative error analysis.** Three trajectories of the best non-oracle agent are walked through with their HMS: one scoring 100, one scoring 50 because a summary statistic was reported without the significance test that would justify it, and one scoring 0 because a simpler analysis replaced the multivariate regression the data required.

## Typical Duration

Not reported as wall-clock time. Difficulty is instead measured by *workflow length*, the number of unit actions in the reference implementation workflow; DB-Real bins tasks as short (< 10), medium (> 10 and < 20), and long (> 20), and performance drops sharply already at medium length.

## Main Contribution

The first benchmark that formalizes data-driven discovery as a multi-step search-and-verification process, together with a structured hypothesis formalism (context, variables, relationship; hypothesis semantic tree) that makes facet-level, failure-mode-revealing evaluation possible.

## Key Design Ideas

- Splitting a hypothesis into context, variables, and relationship turns a single pass/fail into three separable signals, so a partly-correct discovery is neither discarded nor over-credited.
- Gold hypotheses are replicated from published, peer-reviewed workflows rather than authored for the benchmark, and the replication also surfaces hypotheses the papers never reported but the data supports.
- Masking one dimension of a gold hypothesis to form the discovery goal keeps each goal pointed at exactly one answer.
- A `NoDataGuess` agent that never opens the datasets measures how much of a score could come from memorizing published work.
- DB-Synth reverse-engineers the discovery process: build the semantic tree first, then generate data that satisfies it, so workflow depth becomes a controllable variable.

## Strengths

- HMS is validated in two directions — a 200-example audit of the evaluator's extraction steps and a 100-pair preference study against human annotators (95% agreement, Fleiss κ = 0.91).
- The facet-based analysis converts low scores into diagnoses: context prediction is a prerequisite for variable prediction, and failure concentrates in tasks needing advanced statistics or long workflows.
- The archaeology domain-knowledge ablation goes past diagnosis to a controlled test — adding the missing background lifts DataVoyager from 9.9% to 25.4% on those tasks.
- Task construction cost is reported honestly (15–90 person-hours per paper, 30% failure rate, 3 of 785 Zenodo candidates surviving), which documents how expensive faithful replication is.

## Limitations

- The authors filtered out domains and tasks requiring forecasting, simulation, or highly specific modeling (species distribution, infection spread, exoplanet astrophysics), which left proportionally fewer natural- and physical-science papers than social-science ones.
- Massive datasets are out of scope; the paper names the 8.92-petabyte Cancer Genome Atlas as an example it does not tackle.
- Multimodal data and complex pipelines — satellite and other geospatial data for climate science — are not handled.
- The authors state that ensuring discovered findings are robust and not the product of *p*-hacking remains unaddressed by their methods.
- Repository note: the reported scores depend on a GPT-4 evaluator. The audit and preference study bound its reliability on this benchmark's hypotheses but do not remove the model from the scoring path.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also derives data-driven scientific tasks from peer-reviewed papers, but fixes the deliverable to a self-contained Python program.
- [BLADE](./blade.md) — Also scores open-ended data analysis against expert reference analyses, at the level of individual analytical decisions.
- [AstaBench](./astabench.md) — Uses DiscoveryBench as the data-analysis benchmark inside its 11-benchmark scientific-research suite.
