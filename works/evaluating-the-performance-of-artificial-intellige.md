# Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams (2024)

> **English** | [简体中文](../zh/works/evaluating-the-performance-of-artificial-intellige.md)

> **First appeared:** 2023-03-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2303.18149)

## Overview

An early evaluation study that administers NCEES Fundamentals of Engineering (FE) and Principles and Practice of Engineering (PE, structural discipline) practice-exam questions to ChatGPT-4 and Google Bard, grading each answer against the official NCEES solutions and reporting per-topic and overall pass-equivalent scores.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://ascelibrary.org/doi/10.1061/PPSCFX.SCENG-1369>
- **Venue:** Practice Periodical on Structural Design and Construction (ASCE), Vol. 29, No. 2 (2024); DOI 10.1061/PPSCFX.SCENG-1369. Preprint: <https://arxiv.org/abs/2303.18149> ("Can AI Chatbots Pass the Fundamentals of Engineering (FE) and Principles and Practice of Engineering (PE) Structural Exams?")

## Summary

The study asks whether the then-new chatbots could pass the two licensure examinations that gate professional engineering practice in the United States. Questions are taken from the NCEES practice exams for the FE (civil) and the PE structural discipline, put to each chatbot one at a time, and graded against the recommended NCEES solutions on a strict correct/not-correct basis. ChatGPT-4 scored 70.9% on the FE and 46.2% on the PE; Bard scored 39.2% and 41%. The authors conclude that ChatGPT-4 could plausibly pass the FE exam — whose passing threshold is historically believed to sit around 60–70% — but that neither model is close to passing the PE, and they analyse the recurring failure modes behind the wrong answers.

## Tasks

Each chatbot was examined on 79 FE questions and 39 PE questions, drawn from the NCEES FE and PE practice exams. The FE portion spans the 18 areas of the FE civil exam (mathematics, probability and statistics, computational tools, ethics and professional practice, engineering economics, statics, dynamics, mechanics of materials, materials, fluid mechanics, hydraulics and hydrologic systems, structural analysis, structural design, geotechnical engineering, transportation engineering, environmental engineering, construction, surveying), with roughly five questions per area and more in several. The PE portion spans the 11 areas of the structural PE exam (project planning, means and methods, soil mechanics, structural mechanics, hydraulics and hydrology, geometrics, materials, site development, analysis of structures, design and details of structures, codes and construction). Coverage in the study is thinner than a real sitting because many questions carry intricate visuals; visual questions were included only where they could be transcribed into text, which is why the surveying and environmental-engineering areas are under-represented relative to a typical FE exam and the PE sample is substantially smaller than the actual 80-question exam. The actual questions are not reproduced in the paper, to respect NCEES copyright; only paraphrased samples with altered values are shown. Task counts and area breakdowns above are taken from the arXiv preprint version of the study.

## Domains

Civil & Structural Engineering. The PE portion is the structural discipline specifically — structural mechanics, analysis of structures, design and details of structures, soil mechanics, and codes and construction, with the responses citing ACI and ASCE provisions. The FE civil portion is broader and additionally touches general engineering foundations (mathematics, probability and statistics, computational tools, engineering economics, ethics) and the transportation, environmental, surveying, and hydraulics subareas of civil engineering.

## Evaluation

Each chatbot was asked one question at a time, and each answer was graded by the authors against the recommended solution in the NCEES practice exam. Grading is binary correct/not-correct with no partial credit, mirroring the scheme used in the real exams, and no curving was applied; counts of correct and incorrect answers were then aggregated per topic area and overall. Responses were additionally discussed qualitatively for relevance, accuracy, and clarity against NCEES recommendations. Reported results: FE — ChatGPT-4 70.9%, Bard 39.2%; PE — ChatGPT-4 46.2%, Bard 41%. The authors note that 6 of ChatGPT-4's wrong FE answers followed a correct procedure and failed only on arithmetic or unit conversion, that both models answered no structural-design question correctly while answering all ethics questions correctly, and that both struggled to distinguish uniform from point loads.

## Typical Duration

Single-turn question answering, one question per prompt, with no tool use and no multi-step trajectory. The authors report that the complete examination process across both exams took 2 hours.

## Main Contribution

A quantified, topic-resolved report on how the first generation of general-purpose chatbots performs on the civil and structural engineering licensure examinations, establishing an early reference point for LLM competence against a professionally recognized standard rather than an ad hoc question set.

## Key Design Ideas

- Use the official NCEES practice exams as the item source, so difficulty, format, and reference solutions come from the body that administers the real examinations.
- Grade correct/not-correct without partial credit or curving, matching the scoring scheme of the actual exams.
- Present one question per prompt, keeping each item independent rather than allowing context to accumulate.
- Report scores per topic area, not only in aggregate, which is what surfaces the structural-design versus ethics contrast.
- Withhold the verbatim questions for copyright reasons and publish only paraphrased examples with altered values.
- Cross-check the study's area-by-area question distribution against the distribution of a typical FE exam as a coverage validity check.

## Strengths

- The item source is an externally administered professional standard, which makes the difficulty calibration credible in a way that self-authored question sets are not.
- Per-area score breakdowns make the failure pattern interpretable rather than reducing performance to a single number.
- The error analysis distinguishes procedural competence from arithmetic slips, and identifies concrete engineering confusions (uniform versus point loads, misapplied deflection formulas).
- Both a general engineering exam (FE) and a discipline-specific one (PE structural) are covered, giving a breadth-versus-depth contrast within the same protocol.

## Limitations

- No benchmark artifact is released: the questions are withheld for copyright, so the evaluation cannot be re-run by others on the same items.
- Coverage is partial — 79 of 110 FE questions and 39 of 80 PE questions — because visually intensive items could not be transcribed, and the paper states the sampling does not conform to an actual exam sitting.
- Only two models are evaluated, both from early 2023, and each on a single run, so the numbers are a snapshot without variance estimates.
- Manual transcription of figure-based items into text changes the task, and the paper acknowledges this drove the under-representation of surveying and environmental engineering.
- Repository note: the setting is single-turn chatbot question answering, with no tool use, no code execution, and no agentic trajectory, so it measures knowledge and reasoning in isolation rather than engineering task execution.
- Repository note: the task counts and per-area distributions cited here are read from the arXiv preprint; the published ASCE version is paywalled and its headline scores match, but any revision to the question counts could not be checked against the version of record.

## Related Works

- [PE Civil Bench](./pe-civil-bench.md) — a later open benchmark of NCEES-modelled civil engineering problems, addressing the reusability this study could not provide.
- [Civil-Eval](./civil-eval.md) — the same registration-examination paradigm applied to Chinese civil and transportation engineering, with a released question count and weighted scoring method.
- [StructureClaw](./structureclaw.md) — structural-engineering evaluation moved from static exam questions to executable, solver-verified scenarios.
- [MaScQA](./mascqa.md) — exam-derived static QA evaluation of LLM domain knowledge, in materials science.
- [EEE-Bench](./eee-bench.md) — professional engineering examination-style benchmark in the electrical and electronics domain.
