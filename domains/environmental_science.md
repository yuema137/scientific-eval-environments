# Environmental Science

> **English** | [简体中文](../zh/domains/environmental_science.md) · [← All domains](./README.md)

## Scope

Environmental prediction and monitoring. Ecology folds here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | Environmental prediction over real territories: CO2 absorption suitability (Spain), gully erosion probability, and habitat analysis, served through a production-style geospatial API. | 93 tasks in 18 categories with per-task expected tool calls, content constraints, round budgets, and domain-expert ground truth. | Eight mechanistic checks per case — expected tool calls, required/forbidden keywords, numeric tolerance (±2 pp), chart production, round budget — with no LLM judge. | [→](../works/geonatureagent-benchmark.md) |
| Terminal-Bench Science | 2026 | Ecology (Life Sciences track) and environmental science (Earth Sciences track) tasks of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ERI Benchmark | 2026 | Environmental engineering as one of nine covered fields, with five subdomains: water treatment, air quality, hydrology, waste management, and environmental impact. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item. | [→](../works/eri-benchmark.md) |
| LLM-EPANET | 2025 | Water-quality behaviour in municipal water distribution systems — chlorine transport, water age and source tracing — alongside the hydraulic simulation of the same networks. | 69 natural-language queries over the standard Net1, Net3 and L-Town networks in five complexity categories, of which the Quality category requires a water-quality simulation; every query paired with a hand-written deterministic reference script. | Functional correctness of the returned value against the executed EPyT reference implementation, with execution failures, aggregation, indexing and unit errors counted incorrect; accuracy reported per category over seven models, 56–81% overall. | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | Water-resource management within hydro-science and engineering, sitting alongside the benchmark's hydrology, river-dynamics and meteorology subfields. | 4,000 Chinese-language single- and multi-choice questions across nine subfields, each labelled by cognitive level, drawn from textbooks, industry standards, laws and regulations and statistical yearbooks, with at least three independent expert reviews per item; 16 models. | Accuracy reported overall and by subfield, question type and cognitive level, queried zero-shot with chain-of-thought at temperature 0 and the choice letter extracted by a separate LLM; models score higher on the science-grounded subfields than on the codified engineering ones. | [→](../works/hydro-se-bench.md) |
| OntoLearner | 2026 | Construct ontology structure for ecology and environment — one of the 22 domains its ontology collection spans — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the environmental science subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`AIR` air quality & atmospheric pollution · `WQ` water quality & treatment · `WRM` water resources & hydrology · `SOIL` soil & land degradation · `ECO` ecology, biodiversity & habitat · `CARB` carbon cycle & climate mitigation · `WASTE` waste management · `EIA` environmental impact assessment & policy · `GEO` environmental geospatial analysis & remote sensing · `GEN` curriculum-wide or unspecified, no single subfield

**Two scores, not one.** The columns split into **coverage** — what the evaluation setup puts under test — and **rigor** — how far you can trust what it reports. They are summed separately because they pull against each other: a benchmark can put everything under test and verify none of it carefully, and a deliberately narrow one can be the most trustworthy thing on the page. Rows are ordered by `Cov`, highest first, and by `Rig` within equal coverage; remaining ties keep Comparison-table order. Coverage leads because it is the axis a reader scans for — *does this benchmark even put my problem under test* — and `Rig` then says how far to trust what it reports.

### Coverage (`Cov`, max 7)

Yes/no, ordered by rarity — the properties fewest works have come first, so the left of the group is where the field is thin. A property nearly every work satisfies does not earn a column: *writing and running code* was dropped on that ground.

- **Net** — network or live external retrieval permitted; a supplied fixed corpus does not count.
- **E2E** — end-to-end research: a question or goal only, with no source paper, reference implementation, or step-by-step specification supplied, and the agent drives the whole investigation.
- **Cost** — budget or resource cost is a scored or priced dimension, not merely a step cap.
- **MM** — multimodal content is load-bearing, either required as input or scored as an output artifact.
- **Repro** — grounded in a specific published result the agent must match or recover.
- **Real** — real experimental or observational data, as opposed to synthetic or simulated (a digital twin is simulated).
- **Inter** — interactive: the agent takes multiple actions against an environment, tool, or simulator and gets feedback that shapes the next one.

### Rigor (`Rig`, max 13)

- **Human** — a measured human-expert baseline or human reference performance anchors the scale. `◐` where the anchor is a published result or expert reference implementation rather than a measured human run.
- **Rubric** — an expert-authored rubric or official marking scheme with named criteria or weights; a continuous automatic metric is not a rubric.
- **Contam** — a deliberate mechanism makes the answer unmemorizable: post-cutoff sourcing, unpublished or newly authored problems, counterfactual alteration, on-demand generation, or screened leakage. Withholding a published paper at evaluation time is `◐` — it does not remove that paper from a pretraining corpus.
- **Verif** `0`–`3` — how far the score can be trusted without trusting a model. `0` scored only by an LLM judge or rubric, with no validation of that scorer · `1` judge or rubric scoring whose agreement with human experts is measured and reported · `2` deterministic checks alongside judge or rubric scoring · `3` fully deterministic — execution, tests, numerical comparison to a reference, symbolic checking, or a proof kernel, with no judge in the loop. This replaces a plain yes/no *deterministic verification* column, which 85% of works satisfied and which therefore separated nothing; as a ladder it separates a great deal. A separate `Judge` column was dropped as near-redundant with `Verif` < 2.
- **Scale** `0`–`3` — items evaluated **in this domain**: `0` fewer than 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 or more · `?` the source does not give a per-domain count. This counts items, not effort: 30 paper-reproduction tasks are far more work than 3,000 exam questions, and the column cannot see that.
- **Fail** `0`–`4` — how deep the failure analysis goes, because "reports a failure analysis" spans everything from a single remark to a controlled experiment. `0` nothing beyond headline scores · `1` narrative remarks on where models fall short, no classes named · `2` named error classes or illustrative case studies, but no counts or shares · `3` a quantified failure account: a taxonomy with per-class counts or shares, or measured breakdowns isolating specific failure conditions · `4` level 3 plus a controlled experiment or ablation built to test *why* the failures occur.

### Reading the two scores

Yes/no columns score `✔` 1, `◐` 0.5, `✘` 0, `?` 0; graded columns contribute their number, with `?` scoring 0. `Domain` does not score.

Three cautions. A `?` costs exactly what a `✘` costs, so both scores are floors on what a work *demonstrably* does, not verdicts on it. Neither score is a quality ranking: high `Cov` with low `Rig` describes a benchmark that reaches for everything and pins down little, while low `Cov` with high `Rig` describes one that measures a narrow thing carefully — and which of those is the right design depends entirely on the question being asked. And `Cov` is a property of the *evaluation setup*, not of the science: a work can sit at the bottom of this table and still be the most important paper in its subfield.

For multi-domain suites the row describes this domain's slice, as in the Comparison table.
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | GEO, CARB, SOIL, ECO | ✘ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| LLM-EPANET | WQ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | ? | 4 | **7.5** |
| Terminal-Bench Science | ECO, GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| ERI Benchmark | WQ, AIR, WRM, WASTE, EIA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✘ | 2 | 2 | 3 | **8** |
| Hydro-SE Bench | WRM | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 2 | ? | 3 | **5** |
| OntoLearner | ECO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [OntoLearner](../works/ontolearner.md)
