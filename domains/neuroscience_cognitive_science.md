# Neuroscience & Cognitive Science

> **English** | [简体中文](../zh/domains/neuroscience_cognitive_science.md) · [← All domains](./README.md)

## Scope

Neuroscience together with psychology and cognitive science.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| ScienceAgentBench | 2024 | Psychology & Cognitive Science tasks — 28 of its 102 — extracted from peer-reviewed data-driven discovery workflows. | Each task requires generating a self-contained Python program reproducing an analysis from a real publication. | Valid execution plus task-specific hand-written success checkers against expert-annotated references; figure outputs judged by GPT-4o. | [→](../works/scienceagentbench.md) |
| Terminal-Bench Science | 2026 | Neuroscience tasks within the Life Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Neuroscience is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| MetaSyn | 2026 | Conduct protocol-faithful systematic review and meta-analysis; psychology is among the subjects its 422 expert-curated meta-analyses span. | Multi-stage systematic-review workflows: identify the eligible studies for a research question with structured PI/ECO criteria within a shared PubMed-anchored corpus containing ineligible distractors. | Study identification against the original expert reviewers' included set, with stage-wise evaluation locating failures along the meta-analysis pipeline. | [→](../works/metasyn.md) |
| BrainBench | 2024 | Predict the outcomes of neuroscience experiments: distinguish real from result-altered abstracts across five Journal of Neuroscience sections. | 200 original-vs-altered abstract pairs (official dataset); static two-alternative forced choice. | Perplexity-based choice for LLMs; human experts with confidence and expertise ratings; calibration analyzed. | [→](../works/brainbench.md) |
| BrainBench (EEG) | 2026 | Understand EEG: perform instruction-conditioned signal processing, quantitative evidence, and scientific interpretation, then produce a grounded report. | 4 subsets (foundational, sleep, neurocognitive, physiological) over 17 datasets; 100K+ executions; CodeAct + agentic paradigms. | Numerical, categorical, set, sequence, semantic, and artifact validation of outputs. | [→](../works/brainbench-eeg.md) |
| Rodent-Bench | 2026 | Annotate rodent behavior from video: temporal segmentation and classification across neuroscience paradigms. | Real rodent behavior video (10–35 min) across social, grooming, scratching, freezing paradigms; two versions; 3 MLLMs. | Second-wise accuracy, macro F1, mean average precision, mutual information, and Matthews correlation coefficient. | [→](../works/rodent-bench.md) |
| CPsyExam | 2024 | Answer psychology examination questions across knowledge recall and case analysis. | 4,000 questions curated from a 22,000-question pool with balanced subject coverage; static QA. | Accuracy across subjects and the two axes (psychological knowledge, case analysis). | [→](../works/cpsyexam.md) |
| ConceptPsy | 2023 | Answer psychology questions with comprehensive concept coverage across 12 core subjects. | 12 subjects and 1,383 manually collected concepts; each question annotated to a chapter; static QA. | Overall plus chapter-wise (per-concept) accuracy, exposing per-concept variation. | [→](../works/conceptpsy.md) |
| PsychCounsel-Bench | 2025 | Answer professional counseling-psychology certification questions. | ~2,252 single-choice questions from the U.S. National Counselor Certification Exam; static QA. | Accuracy against the exam's ~70% passing threshold across models. | [→](../works/psychcounsel-bench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | Automate the computational stages of a real fly-optogenetics data-to-discovery pipeline — video-based body/keypoint tracking, walking-behavior classification, gait segmentation, and statistical comparison across GAL4 driver lines versus a genetic control. | Seven ordered single-stage tasks plus end-to-end pipeline variants (nine computational tasks total) over ~47 GB of released fly-behavior data; agents produce runnable code, three trials per agent–task pair. | Stage-level success criteria grounded in domain-expert standards, compared against expert human annotations and trusted legacy scientist-authored codebases; the statistical stage uses Mann–Whitney U tests against a genetic control. | [→](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| MiraMind | 2025 | Evidence-constrained mental-health and clinical-psychology reasoning — cognitive-pattern appraisal, counseling-strategy selection, and psychiatric judgment — where the warranted specificity and certainty of interpretations is itself evaluated (folds into Neuroscience & Cognitive Science). | Six task families over 13 datasets (appraisal, diagnosis, intervention, multi-step psychiatry QA, abstraction, verification) spanning informal user narratives, counseling dialogues, psychiatric board-style QA, and Cochrane review abstracts; 20 LLMs. | Per-family outcome metrics (Micro-F1, Jaccard, expert-scoring-point recall, Macro-F1) plus an LLM-as-judge trajectory rubric (usability, logical structure, informational contribution) validated on 100 human-annotated trajectories. | [→](../works/miramind.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the neuroscience and cognitive science subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`COG` cognitive science & cognitive neuroscience · `PSY` psychology as an academic subject · `CLIN` clinical & counseling psychology · `MH` mental health & psychiatry · `BEH` behavioral neuroscience & animal behavior · `SYS` systems & circuit neuroscience · `CELL` cellular & molecular neuroscience · `DEV` development, plasticity & repair · `DIS` neurobiology of disease · `EPHYS` electrophysiology & neural signal analysis (EEG, MEG) · `SLEEP` sleep science · `IMG` neuroimaging · `CNEU` computational & theoretical neuroscience · `GEN` field-wide or unspecified, no single subfield

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
| ResearchClawBench | BEH, SYS, CELL | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| ScienceAgentBench | PSY, COG | ✘ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✔ | ✔ | 2 | 1 | 3 | **8.5** |
| Neuroscience Data-to-Discovery Case Study | BEH, SYS | ? | ◐ | ◐ | ✔ | ◐ | ✔ | ✔ | **4.5** | ◐ | ✔ | ? | 3 | 0 | 4 | **8.5** |
| BrainBench (EEG) | EPHYS, SLEEP, COG | ? | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ? | 2 | 3 | 3 | **8.5** |
| Rodent-Bench | BEH | ✘ | ✘ | ◐ | ✔ | ✘ | ✔ | ✘ | **2.5** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| MetaSyn | PSY, MH | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✘ | **2.5** | ◐ | ✘ | ◐ | 2 | 1 | 3 | **7** |
| BrainBench | COG, SYS, CELL, DIS, DEV | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ✔ | ✘ | ✔ | 3 | 2 | 3 | **10** |
| MiraMind | MH, CLIN | ? | ✘ | ✘ | ✘ | ◐ | ✔ | ✘ | **1.5** | ✘ | ✔ | ◐ | 2 | 3 | 2 | **8.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ? | ? | ? | ✔ | **1** | ✘ | ✘ | ◐ | 3 | 0 | 0 | **3.5** |
| ConceptPsy | PSY | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| CPsyExam | PSY, CLIN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 3 | 2 | **7.5** |
| PsychCounsel-Bench | CLIN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [MiraMind](../works/miramind.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MetaSyn](../works/metasyn.md)
- [BrainBench](../works/brainbench.md)
- [BrainBench (EEG)](../works/brainbench-eeg.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [CPsyExam](../works/cpsyexam.md)
- [ConceptPsy](../works/conceptpsy.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
