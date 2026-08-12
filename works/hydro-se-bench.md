# Hydro-SE Bench (2025)

> **English** | [简体中文](../zh/works/hydro-se-bench.md)

## Overview

Hydro-SE Bench is a Chinese-language multiple-choice benchmark of 4,000 questions covering nine subfields of hydro-science and hydraulic engineering, built to measure how much practical water-engineering knowledge — including hydraulic structures, geotechnical engineering, and industry design standards — general-purpose LLMs actually hold.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.03672>
- **Code:** <https://github.com/sheishijun/Hydro-SE-Bench>
- **Venue:** arXiv preprint, 3 December 2025

## Summary

The authors argue that hydro-science and engineering (Hydro-SE) is a knowledge-intensive field whose LLM capabilities have not been measured systematically, and build what they describe as the first benchmark that evaluates LLM knowledge across Hydro-SE subfield dimensions. Questions are drawn from textbooks, industry standards, laws and regulations, and statistical yearbooks, then generated semi-automatically with LLMs guided by expert-designed exemplars and independently reviewed by at least three experts each. Sixteen models — ten commercial and six open-source — are evaluated zero-shot with chain-of-thought reasoning at temperature 0, and the results are broken down by subfield and by cognitive level so that knowledge gaps can be localized rather than reported as a single score.

## Tasks

4,000 question-answer pairs presented in Chinese. The paper reports the split as 2,700 single-choice questions (68%) and 1,300 multi-choice questions (32%); the accompanying repository states 2,696 single-choice and 1,304 multi-choice. Questions span nine subfields: Background Knowledge, Industry Standards, Hydrology and Water Resources, Geotechnical Engineering, Hydraulic Structures and Equipment, Engineering Safety and Management, Hydraulics and River Dynamics, Meteorology, and Power Systems. Each question is additionally labelled with one of three cognitive levels: Type A, basic conceptual knowledge; Type B, scenario-based engineering application; Type C, reasoning and calculation. The repository gives the level distribution as 43.75% Type A, 43.75% Type B, and 12.5% Type C. Sources are textbooks, industry standards, laws and regulations, and statistical yearbooks; a semi-automatic LLM-based generation pipeline seeded with expert-written exemplars produced candidate items, and at least three domain experts reviewed each item independently. Per-subfield question counts are shown only as a distribution figure in the paper — `TODO(reference)` for the exact per-subfield numbers. The repository notes that only half of the items (odd-numbered IDs) have been released publicly.

## Domains

Civil & Structural Engineering, as hydraulic-infrastructure engineering. Four of the nine subfields sit inside the civil engineering of built water infrastructure: Hydraulic Structures and Equipment (dams, spillways, gates, and the machinery serving them), Geotechnical Engineering, Industry Standards (the design codes and specifications governing water-conservancy and hydropower works), and Engineering Safety and Management. The paper's headline finding is specifically that models are weakest on "domain-specific knowledge such as industry standards and hydraulic structures," which is the civil-engineering core of the benchmark. Co-domains: Earth Science (Hydrology and Water Resources, Hydraulics and River Dynamics, Meteorology), Environmental Science (water-resource management), and Energy Systems (Power Systems, reflecting the hydropower side of the field).

## Evaluation

Accuracy, defined as the ratio of correctly answered questions to total questions, reported overall and broken down by subfield, question type, and cognitive level. Models are queried zero-shot with chain-of-thought prompting at temperature 0 for deterministic outputs; a two-stage protocol has the evaluated model produce its reasoning first and a separate LLM then extract the final choice letter from that free-form response. Whether multi-choice items receive partial credit is not stated — `TODO(reference)`. Reported results: commercial models fall in the 0.74–0.80 accuracy band and open-source models in 0.41–0.68. DeepSeek-V3.2-Exp and DeepSeek-R1 lead overall, both above 0.79, with DeepSeek-V3.2-Exp at 0.796. Sixteen models were evaluated: ten commercial (DeepSeek-V3.2-Exp, DeepSeek-R1, Kimi K2, GLM-4.5, GPT-5, Grok-4, Qwen-Plus, Gemini-2.5-Pro, Llama-4, Claude-4.5) and six open-source (GLM-4-32B, Qwen2.5 at 32B/72B/7B, Llama-3 at 70B/8B). The authors observe that models perform better on subfields grounded in the natural and physical sciences than on the codified, practice-specific engineering subfields, and that scaling mainly improves reasoning rather than domain knowledge.

## Typical Duration

N/A — single-turn multiple-choice questions with no trajectory, tool use, or wall-clock budget. No per-question token budget is reported.

## Main Contribution

The authors present Hydro-SE Bench as the first benchmark to comprehensively evaluate LLM knowledge and capability across the subfield dimensions of hydro-science and engineering, and use its subfield and cognitive-level breakdown to show that current models are far stronger on science-grounded content than on the industry standards and hydraulic-structures knowledge that practical water engineering depends on.

## Key Design Ideas

- Two orthogonal labels per item — a subfield tag and a cognitive-level tag (A conceptual / B engineering application / C reasoning and calculation) — so that a model's weakness can be attributed to a field or to a reasoning mode.
- Item sources deliberately weighted toward practice documents: industry standards, laws and regulations, and statistical yearbooks alongside textbooks.
- Semi-automatic generation with expert-designed exemplars, followed by independent review from at least three experts per item.
- Chinese-language construction, matching the national standards and regulatory corpus the questions are drawn from.
- Deterministic evaluation at temperature 0, with answer extraction delegated to a separate LLM so that chain-of-thought responses can be graded without format constraints on the model under test.
- Mixed single- and multi-choice formats rather than single-choice only.

## Strengths

- Covers the codified, standards-bound side of water engineering that generic science benchmarks omit, and shows it is precisely where models fail.
- Subfield-by-subfield reporting makes the failure modes actionable rather than a single aggregate number.
- Broad model panel of sixteen systems spanning commercial frontier models and open-weight models at several scales.
- Expert review loop with at least three independent reviewers per item.
- Dataset and evaluation package released with batch evaluation, statistical breakdowns by category, difficulty and question type, and report generation.

## Limitations

- The authors note the benchmark is confined to multiple-choice questions and therefore cannot fully reflect real engineering application.
- The authors note it incorporates no real-time data and no scenario-based agentic tasks.
- The authors note evaluation is text-only, whereas much of Hydro-SE practice depends on multimodal inputs such as satellite remote-sensing imagery, station time series, and video streams.
- Repository note: only half of the items — those with odd-numbered IDs — are publicly released, so results computed on the public split are not directly comparable to the paper's full-set numbers.
- Repository note: per-subfield question counts are given only as a figure, so subfield-level results cannot be reweighted from the paper text alone.
- Repository note: because item candidates were LLM-generated before expert review, question phrasing may be correlated with the answering models' own distributions, though the paper does not test for this.

## Related Works

- [Civil-Eval](./civil-eval.md) — the other Chinese-language civil-engineering knowledge benchmark built from national professional-registration examination material.
- [PE Civil Bench](./pe-civil-bench.md) — professional-licensure-style civil engineering problems, the English-language counterpart in construction and intent.
- [HydroAgent](./hydroagent.md) — the executable, agentic end of the same field, calibrating an operational distributed hydrologic model instead of answering questions.
