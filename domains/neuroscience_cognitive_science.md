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
