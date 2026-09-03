# Earth Science

> **English** | [简体中文](../zh/domains/earth_science.md) · [← All domains](./README.md)

## Scope

Geosciences: atmospheric, ocean, and geological sciences. GIS and geospatial analysis fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | Environmental geospatial analysis over Spain and Portugal through structured tool calls to a production-style API serving three environmental indicators via 16 tools. | 93 tasks in 18 categories: municipality analysis, spatial reasoning, cross-indicator synthesis, multilingual queries, and deliberately unsolvable tasks that must be declined. | Eight mechanistic checks per case — expected tool calls, required/forbidden keywords, numeric tolerance (±2 pp), chart production, round budget — with no LLM judge. | [→](../works/geonatureagent-benchmark.md) |
| ScienceAgentBench | 2024 | Geographical Information Science tasks — 27 of its 102 — extracted from peer-reviewed data-driven discovery workflows. | Each task requires generating a self-contained Python program reproducing an analysis from a real publication. | Valid execution plus task-specific hand-written success checkers against expert-annotated references; figure outputs judged by GPT-4o. | [→](../works/scienceagentbench.md) |
| Terminal-Bench Science | 2026 | Atmospheric, environmental, geo-, and ocean science tasks in the Earth Sciences track of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Earth is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| HydroAgent | 2026 | Calibrate the operational CREST distributed hydrologic model used by the U.S. National Weather Service for flash-flood forecasting. | Iterative simulate-and-adjust calibration on four held-out gauges spanning 329–40,792 km², best of twenty rounds; nine frontier agents. | Nash–Sutcliffe Efficiency on held-out gauges against a human-expert calibration reference. | [→](../works/hydroagent.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of earth-system-science data — one of its seven application domains — translating natural-language intent into executable visualization operations over multivariate and time-varying fields. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | Interleaved web-browsing-plus-computation questions in the geophysical domain (folding into Earth Science) — multi-hop entity identification and retrieval of quantitative geophysical properties from knowledge-graph sources, followed by domain-specific computation. | Answer-first questions synthesized from knowledge-graph chains requiring multi-hop identification, quantitative-property retrieval, and multi-step computation; spans five domains (biochemistry, geophysical, financial, security, history), of which geophysical is one. | Execution-based: gold answers computed by executing parameterized code over knowledge-graph values, scored within ~2% relative tolerance; two-stage difficulty cascade; 76% human-validated validity. | [→](../works/drbencher.md) |
| Hydro-SE Bench | 2025 | Hydrology and water resources, hydraulics and river dynamics, and meteorology — three of the nine subfields of hydro-science and engineering. | 4,000 Chinese-language single- and multi-choice questions across nine subfields, sourced from textbooks, industry standards, laws and regulations and statistical yearbooks through a semi-automatic pipeline seeded with expert exemplars and reviewed by at least three experts per item; 16 models. | Accuracy reported overall and by subfield, question type and cognitive level, queried zero-shot with chain-of-thought at temperature 0 with answer extraction delegated to a separate LLM; the paper reports models are stronger on these science-grounded subfields than on the codified engineering ones. | [→](../works/hydro-se-bench.md) |
| ScienceBoard | 2025 | Geospatial analysis driven through GRASS GIS — one of the six professional applications instantiating its domains. | 169 human-curated computer-use tasks in a single Ubuntu virtual machine: 38 GUI-only, 33 CLI-only, 98 hybrid GUI+CLI; per-application task counts are not published. | Programmatic checking of key intermediate input/output and of the final virtual-machine state through templates supporting exact match, range-based assessment and numerical tolerance; GIS is among the weakest domains for every evaluated agent. | [→](../works/scienceboard.md) |
| Imaging-101 | 2026 | Earth-science computational imaging — one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| SciVQR | 2026 | Multimodal scientific reasoning in the geography subject — one of six top-level scored subjects — whose subfields include geology, geomorphology, hydrology, climatology and cartography. | 3,254 image-paired competition and exam questions across six subjects and 54 subfields (2,545 multiple-choice, 709 free-form; easy/medium/hard tiers); 15 multimodal models zero-shot, with and without CoT. Per-subject item counts are not published. | Zero-shot accuracy reported per subject, plus a five-dimension rubric (faithfulness, informativeness, redundancy, hallucination, missing steps) scoring the generated reasoning against expert-authored solution traces. | [→](../works/scivqr.md) |
| HiSciBench | 2025 | The geography discipline across the hierarchy: literature question answering over geoscience papers, plus data-driven discovery in which the model writes and executes Python analysis code. | 737 geography instances within 8,735 — 200 general scientific QA, 500 monolingual literature QA, 10 review topics and 27 data-driven discovery tasks; 18 models evaluated. | Level-appropriate metrics: accuracy at the QA levels, word-level accuracy for literature OCR, BLEU for translation, at the review level an LLM-judge 1–5 rubric over Coverage, Structure, Relevance, Synthesis and Critical Analysis plus citation verifiability, metadata accuracy, faithfulness and recency, and at the discovery level an execution-based Success Rate zeroed when the generated program fails to execute. | [→](../works/hiscibench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the earth science subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`GIS` geographic information science & geospatial analysis · `RS` remote sensing & Earth observation · `HYD` hydrology & water resources · `ATM` atmospheric science & meteorology · `CLI` climatology & climate science · `OCE` ocean & marine science · `GEOL` geology & geomorphology · `GPH` geophysics & subsurface imaging (seismic, InSAR) · `ENV` environmental & ecological earth science · `ESM` earth-system modeling & data analysis · `GEN` curriculum-wide or unspecified, no single subfield

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
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| Imaging-101 | GPH, RS, ATM | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | 0 | 3 | **6.5** |
| ScienceAgentBench | GIS | ✘ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✔ | ✔ | 2 | 1 | 2 | **7.5** |
| GeoNatureAgent Benchmark | GIS, ENV, RS | ✘ | ✘ | ✔ | ◐ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 3 | 1 | 2 | **6** |
| SciVisAgentBench | ESM | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| DrBencher | GPH | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 1 | 1 | **6** |
| HydroAgent | HYD | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✔ | ✘ | ✘ | 3 | 0 | 2 | **6** |
| ScienceBoard | GIS | ? | ✘ | ✘ | ✔ | ✘ | ? | ✔ | **2** | ✔ | ✘ | ✘ | 3 | ? | 2 | **6** |
| HiSciBench | GEN | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | ✘ | **1.5** | ✘ | ✔ | ✘ | 2 | 2 | 3 | **8** |
| SciVQR | GEOL, HYD, CLI | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| Hydro-SE Bench | HYD, ATM | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 2 | ? | 3 | **5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [Imaging-101](../works/imaging-101.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [HydroAgent](../works/hydroagent.md)
- [SciVQR](../works/scivqr.md)
- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [HiSciBench](../works/hiscibench.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [ScienceBoard](../works/scienceboard.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
