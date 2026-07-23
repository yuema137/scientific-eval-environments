# HeurekaBench (2026)

## Overview

HeurekaBench is a framework for creating benchmarks of exploratory, open-ended research questions over experimental datasets, rather than a fixed benchmark itself. Each question is grounded in a published scientific study and its code repository, and is produced by a semi-automated pipeline whose candidate answers are verified against the findings that study reported.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.01678>
- **Code:** <https://github.com/mlbio-epfl/HeurekaBench>
- **Venue:** ICLR 2026

## Summary

The authors argue that evaluating co-scientist agents requires realistic end-to-end research scenarios that integrate data analysis, interpretation, and the generation of new insights from experimental data, which existing benchmarks do not supply. HeurekaBench addresses this by contributing the construction pipeline rather than a task list: multiple LLMs extract candidate insights from a study and generate candidate workflows, which are then verified against reported findings before becoming questions. The framework is instantiated in single-cell biology as sc-HeurekaBench and used to compare existing single-cell agents, the strongest of which reaches 2.34 out of 5 on open-ended correctness.

## Tasks

sc-HeurekaBench, the single-cell instantiation, comprises 50 open-ended questions and 50 multiple-choice questions built from 41 validated insights across 13 papers — nine from Nature and four from Cell. Questions are produced in three stages: insights generation, in which candidate insights are extracted from scientific articles and semi-automatically validated; questions generation, in which validated insights are reformulated as question–answer pairs; and question solving, in which the agent autonomously designs and executes a multi-step analysis producing a data-driven answer. A reduced subset, sc-HeurekaBench-Lite, restricts to datasets under 750 MB and contains 22 of the open-ended and 18 of the multiple-choice questions, so that every compared agent can be run on the same tasks.

## Domains

Single-cell biology, as the instantiation of a construction pipeline the authors present as domain-general.

## Evaluation

- **Open-ended correctness by LLM judge.** G-Eval with GPT-4o assigns a rating from 1 to 5. Both the response and the ground truth are decomposed into atomic facts, and the rating reflects overlap across complete, partial, and missing facts.
- **Multiple-choice questions** are scored by accuracy, with precision and recall also reported.
- **Ground truth is the published finding.** Candidate workflows produced by the pipeline are verified against what the source study reported, rather than against a synthetic target or an annotator-authored key.
- **Reported.** On sc-HeurekaBench-Lite, open-ended correctness across three existing single-cell agents reaches 2.34 for BixBench-Agent, 2.31 for Biomni, and 2.03 for CellVoyager, on the 1–5 scale. A planner-model ablation gives Claude-4-Sonnet 2.58 ± 0.05, GPT-OSS-120B 2.08 ± 0.05, and Qwen3-235B-thinking 1.85 ± 0.03. The authors further report that adding a critic module improves ill-formed responses for open-source LLM-based agents by up to 22%, closing the gap with closed-source counterparts.

## Typical Duration

Not stated: no per-question wall-clock, step, or token budget is given. The only resource constraint the paper documents is on data volume — the Lite subset restricts to datasets under 750 MB so that all compared agents can be run.

## Main Contribution

A semi-automated pipeline for constructing end-to-end scientific benchmarks from published studies and their code repositories, in which ground truth is verified against the findings those studies reported rather than authored by hand.

## Key Design Ideas

- Benchmark construction is the contributed artifact; the single-cell suite is presented as an instantiation of the pipeline rather than as the deliverable.
- Ground truth is anchored to findings already reported in a published study, paired with that study's code repository, so the correctness standard has an external referent.
- Multiple LLMs extract candidate insights and generate candidate workflows, with a semi-automatic validation step gating what becomes a question.
- The same validated insights are posed in two forms, open-ended and multiple-choice, so that free-form generation and constrained selection are measured against a common source.

## Strengths

- Deriving questions from papers and their repositories means new studies yield new questions without hand-authoring, addressing benchmark staleness structurally rather than through periodic re-release.
- Anchoring the answer key in published findings gives correctness a referent that does not depend on the benchmark authors' own judgement of what the right answer is.
- The paper puts the benchmark to diagnostic use rather than only publishing a ranking, using it to compare planner models and to isolate the effect of a single agent design choice.

## Limitations

- Repository note: The pipeline is semi-automated and relies on multiple LLMs to extract insights and generate candidate workflows, and open-ended answers are graded by an LLM judge, so both the questions and their scoring inherit the reliability of the models used to produce them.
- Repository note: Only the single-cell instantiation exists — the pipeline is presented as domain-general but transfer to another field is not evaluated — and the reported agent comparison runs on the reduced Lite subset rather than the full 50 open-ended questions.

## Related Works

- [NatureBench](./naturebench.md) — Also anchors difficulty in published research and scores against what the paper reported, but distills a fixed set of tasks, whereas HeurekaBench contributes the pipeline that generates them.
- [ScienceAgentBench](./scienceagentbench.md) — Also extracts tasks from peer-reviewed publications and validates them before release, but validation is performed by subject-matter experts over a hand-curated suite rather than semi-automatically against the source study's own findings.
- [SciAgentArena](./sciagentarena.md) — Also targets real research scenarios and reports that agents struggle with novel insights and open-ended questions, which is the capability HeurekaBench's open-ended questions are built to measure; its tasks are curated directly rather than derived through a construction pipeline.
