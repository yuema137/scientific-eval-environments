# BridgeEQA (2025)

> **English** | [简体中文](../zh/works/bridgeeqa.md)

> **First appeared:** 2025-11-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2511.12676)

## Overview

BridgeEQA is an embodied question-answering benchmark for bridge inspection: 2,200 open-vocabulary
question-answer pairs grounded in professional inspection reports over 200 real bridge scenes, where an agent
must gather visual evidence across many viewpoints of a structure, answer to a standardised condition rubric,
and cite the images that support its verdict.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.12676>
- **Code:** <https://github.com/drags99/bridge-eqa>
- **Venue:** CVPR 2026 (stated on the project page <https://drags99.github.io/bridge-eqa/>); arXiv preprint, 2025

## Summary

The authors propose *Inspection EQA* as a problem class for episodic-memory embodied question answering,
arguing that infrastructure inspection supplies what generic EQA benchmarks lack: egocentric imagery,
professional reports as grounding, and a standardised evaluation scale. BridgeEQA instantiates it on real
bridge inspection data, and the paper adds Image Citation Relevance, a metric for whether a model cites the
images that actually support its answer. Evaluation of state-of-the-art vision-language models exposes
substantial performance gaps, and the paper proposes Embodied Memory Visual Reasoning (EMVR), which casts
inspection EQA as a Markov decision process over a scene graph and outperforms the baselines.

## Tasks

2,200 open-vocabulary question-answer pairs over 200 real-world bridge scenes containing 9,586 images in
total, averaging 47.93 images per scene; the bridges span 73 Vermont towns. Questions were extracted
automatically with Gemini vision-language models from Vermont Agency of Transportation inspection reports,
grounded in inspector notes and the photographs those notes explicitly reference. Four question types are
reported: Aggregative (38.5%), Comparative (27.2%), Relational (21.3%), and Spatial (17.5%). QA pairs were
filtered by automated checks on faithfulness (0.997), answer relevancy (0.997), answerability (0.996), and
inspector relevancy (0.980), with manual review of random subsets for visual coverage and image quality.

## Domains

Civil & Structural Engineering: bridge inspection and condition assessment of in-service highway bridges,
with answers aligned to the National Bridge Inventory 0–9 condition rating scale used by state
transportation agencies. The imagery and the reasoning are drawn from professional structural inspection
practice rather than from generic indoor or outdoor scene understanding.

## Evaluation

- **Answer Correctness** — LLM-as-a-judge comparison of the response against the report-grounded ground truth,
  following the OpenEQA protocol.
- **Condition Rating Accuracy** — exact-match and within-±1 accuracy on the NBI 0–9 scale; the ±1 band is used
  because expert inspectors typically agree only to within one rating.
- **Image Citation Relevance** — a VLM-as-a-judge (Gemini 2.5 Flash) scores agent-cited images against
  reference images on a 0.0–1.0 scale and penalises over-selection; the metric attains a Spearman correlation
  of 0.817 with human annotations.
- **Reported.** Five methods (Multi-Frame VLM, Socratic LLM with scene graph, Multi-Frame VLM with scene
  graph, EMVR with scene graph only, EMVR with images plus scene graph) were run over three proprietary
  vision-language models (Gemini 2.5 Flash Lite, Gemini 2.5 Flash, Grok 4 Fast). Answer-correctness scores
  span 0.484–0.648 and Image Citation Relevance 0.687–0.889. On Grok 4 Fast, EMVR improves over the
  Multi-Frame VLM baseline by +9.3 points on within-±1 condition rating accuracy, +20.2 points on Image
  Citation Relevance, and +7.2 points on answer correctness.

## Typical Duration

N/A — the paper reports no per-episode step limit, wall-clock budget, or token budget. Episodes operate over
per-bridge scene graphs averaging 47.93 images.

## Main Contribution

Introducing Inspection EQA as a problem class for episodic-memory embodied question answering, releasing
BridgeEQA as its first benchmark, proposing Image Citation Relevance as an evaluation metric for evidence
citation, and showing that a Markov-decision-process formulation (EMVR) over an episodic scene graph closes
part of the gap left by direct multi-frame prompting.

## Key Design Ideas

- Ground the questions in documents that already exist and already carry an accepted answer standard —
  professional inspection reports and the NBI condition scale — instead of authoring synthetic questions.
- Score the evidence as well as the answer: an agent that reaches the right condition rating while citing
  irrelevant images is penalised by Image Citation Relevance.
- Use the ±1 band on condition ratings so that scoring reflects real inter-inspector agreement rather than
  demanding an exactness human experts do not achieve.
- Treat the multi-view image collection of a bridge as an episodic memory to be navigated, formalised as an
  MDP over a scene graph, rather than as a flat image stack fed to a long-context model.
- Validate the judge metric against three human annotators before using it to rank systems.

## Strengths

- The scenes, images, and answer standard come from a real state inspection programme, so the task
  distribution is not authored by the benchmark designers.
- Three separate scoring axes (answer text, engineering condition verdict, evidence citation) make it visible
  when a model is right for the wrong reasons.
- The citation metric is calibrated against human annotation rather than assumed reliable.
- The comparison covers five method variants crossed with three models, separating the contribution of the
  scene-graph representation from that of the navigation policy.

## Limitations

- Only proprietary models are benchmarked: the authors report that open-source VLMs could not reliably follow
  the required structured-output and function-calling formats.
- Ground-truth QA pairs are generated automatically by Gemini models from the reports, with human review only
  on random subsets, so the benchmark's labels partly inherit a model's reading of the source documents.
- Two of the three headline metrics are model-judged (LLM-as-a-judge and VLM-as-a-judge), and one of the
  judges is drawn from the same family as an evaluated model.
- All scenes come from a single state inspection programme (Vermont Agency of Transportation), so reporting
  conventions and bridge population are not diverse.
- Repository note: the benchmark scores condition assessment from imagery; it does not evaluate quantitative
  structural analysis, load rating, or any downstream maintenance decision.

## Related Works

- [StructureClaw](./structureclaw.md) — the other civil work pairing an agent workbench with an executable
  structural-engineering benchmark, but verified by solver agreement rather than inspection findings.
- [DrafterBench](./drafterbench.md) — civil-engineering deliverables as the evaluated artifact, on drawings
  rather than inspection imagery.
- [PE Civil Bench](./pe-civil-bench.md) — civil engineering competence measured through licensure-style
  problems instead of field evidence.
