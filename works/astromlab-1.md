# AstroMLab 1 (2024)

> **English** | [简体中文](../zh/works/astromlab-1.md)

> **First appeared:** 2024-07-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2407.11194)

## Overview

AstroMLab 1 introduces the first astronomy-specific LLM benchmarking dataset — 4,425 multiple-choice questions generated from the *Annual Review of Astronomy and Astrophysics* — and uses it to score 47 proprietary and open-weights models on astronomical knowledge, with accompanying cost-efficiency and confidence-calibration analyses.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.11194>
- **Code:** <https://github.com/AstroMLab>
- **Venue:** Astronomy and Computing, vol. 51, 100893 (2025); DOI 10.1016/j.ascom.2024.100893

## Summary

The paper argues that general-purpose benchmarks say little about a model's grasp of astronomy, and builds a domain benchmark by prompting Gemini-1.5-Pro to write five four-option multiple-choice questions per article over 885 *Annual Review of Astronomy and Astrophysics* review articles published 1963–2023, yielding 4,425 questions. Forty-seven models — 25 proprietary and 22 open-weights — are scored by accuracy, with Wilson score intervals, and the results are cross-cut by six astrophysics subfields and five tested abilities. Beyond the leaderboard, the study measures cost efficiency (accuracy per unit inference price at astro-ph corpus scale) and confidence calibration, finding the strongest models' confidence–correctness correlations above 0.9. It positions itself as the first paper in the AstroMLab series, with the detailed dataset description deferred to a companion paper.

## Tasks

4,425 four-option multiple-choice questions on astronomy and astrophysics. Construction: 885 *Annual Review of Astronomy and Astrophysics* articles (1963–2023) were text-extracted with Nougat OCR, then Gemini-1.5-Pro was instructed to propose five questions answerable from each paper's content, with prompt directives enforcing specificity, generality (avoiding paper-specific trivia) and balanced answer-option lengths; the generator also supplied explanations and supporting citations. Human experts reviewed a subset of the generated items and judged the quality adequate. Questions are additionally categorized into six astrophysics subfields and five tested abilities. Setting is single-turn closed-book question answering; retrieval-augmented generation is deliberately excluded from the evaluation scope.

## Domains

Astronomy and astrophysics — questions are derived entirely from astronomy review literature and span stellar astrophysics, exoplanets, galactic and extragalactic astronomy, cosmology, high-energy astrophysics and instrumentation. The evaluated objective is astronomical knowledge and reasoning, not a generic knowledge probe with astronomical vocabulary.

## Evaluation

Accuracy on the 4,425 questions, with Wilson score intervals of roughly ±0.6–0.8 percentage points. Models that refuse to answer have those items excluded on a per-model basis (affecting up to 0.2% of questions for the strongest models). Two secondary analyses accompany the accuracy ranking: a cost-efficiency analysis reporting price per 0.1M tokens and per 3B tokens (the size of the astro-ph archive), and a calibration analysis correlating self-reported confidence with correctness.

- **Reported:** Claude-3.5-Sonnet leads the proprietary models at 85.0%; Claude-3.0-Opus 82.7%; GPT-4o 80.4%. LLaMA-3-70B leads open-weights models at 80.6%; Qwen-2-72B and Mixtral-8x22B tie at 77.7%.
- **Reported (cost):** roughly a tenfold increase in inference cost per 3.5-point gain in score.
- **Reported (calibration):** confidence–correctness correlations above 0.9 for the top models.

## Typical Duration

Single-turn multiple-choice answering; no interactive environment, tool use or multi-step trajectory.

## Main Contribution

The first astronomy-specific LLM benchmark and the first broad cross-model measurement of astronomical knowledge, establishing the reference scale against which the AstroMLab model line and subsequent astronomy-LLM work report.

## Key Design Ideas

- Source questions from a curated review series (*Annual Review of Astronomy and Astrophysics*) rather than arbitrary papers, so items reflect consolidated field knowledge.
- Generate questions with a strong LLM under explicit prompt constraints (specificity, generality, balanced option lengths) to make automated construction tractable at 4,425 items.
- Require the generator to output an explanation and supporting citation for each item, so human reviewers can spot-check quality efficiently.
- Report cost per unit of accuracy at astro-ph corpus scale, making the benchmark usable for deployment decisions and not only for ranking.
- Include confidence calibration alongside accuracy, treating reliability of self-assessment as a distinct evaluated property.
- Cover both proprietary and open-weights models at scale (47 in total) so the closed/open gap is measurable.

## Strengths

- Large, domain-specific item pool and unusually broad model coverage for a single evaluation.
- Peer-reviewed and published in a domain venue (*Astronomy and Computing*).
- Cost-efficiency and calibration analyses give the benchmark diagnostic value beyond a single accuracy number.
- Subfield and ability breakdowns support finer-grained comparison than an aggregate score.

## Limitations

- Questions are LLM-generated with only a subset human-verified; the authors acknowledge this is "a compromise", that some items may be vague, and that questions from older reviews may encode outdated astronomy — so reported accuracy is "certainly a lower limit".
- Static closed-book multiple choice: no agent, tool use, task environment or free-response reasoning is evaluated, and RAG is explicitly out of scope.
- The dataset was not released with this paper; the authors defer its detailed description and release to a forthcoming companion paper.
- Repository note: multiple-choice recall over review literature measures knowledge, not the ability to carry out astronomical research tasks; the card is included under the repository's exam- and QA-derived benchmark precedent.

## Related Works

- [LLM-IOAA](./llm-ioaa.md) — also an astronomy knowledge evaluation, but free-response olympiad problems graded against official rubrics rather than multiple choice.
- [Stargazer](./stargazer.md) — astronomy evaluation at the opposite end of the spectrum: an interactive model-fitting task environment rather than static QA.
- [From Queries to Criteria](./from-queries-to-criteria-understanding-how-astrono.md) — argues directly that multiple-choice astronomy benchmarks capture only a narrow slice of what astronomers evaluate.
- [MaScQA](./mascqa.md) — comparable domain-knowledge QA benchmark in materials science.
- [EEE-Bench](./eee-bench.md) — comparable large-scale domain QA benchmark with broad model coverage in electrical engineering.
