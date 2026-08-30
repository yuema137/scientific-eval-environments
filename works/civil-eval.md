# Civil-Eval (2026)

> **English** | [简体中文](../zh/works/civil-eval.md)

> **First appeared:** 2026-01-31 · **Source:** [Official publication page](https://zgglxb.chd.edu.cn/EN/10.19721/j.cnki.1001-7372.2026.01.012)

## Overview

Civil-Eval is a Chinese-language evaluation dataset for civil and transportation engineering knowledge, built from Chinese national professional-registration examinations, together with a weighted scoring method used to benchmark general-purpose LLMs, reasoning models, and a domain-specific civil-engineering model.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://zgglxb.chd.edu.cn/EN/10.19721/j.cnki.1001-7372.2026.01.012>
- **Venue:** China Journal of Highway and Transport (中国公路学报), Vol. 39, No. 1 (2026), pp. 148–161; DOI 10.19721/j.cnki.1001-7372.2026.01.012

## Summary

The authors argue that general-domain LLM evaluation datasets contain no civil-engineering knowledge, so the capability boundary of large models in this vertical is unmeasured. They build Civil-Eval from the questions of Chinese national registration examinations — Class-1 Registered Architect, Class-2 Registered Architect, and Supervising Engineer — after manual screening, organization, and re-checking, covering 8 examination subjects with 426 single-choice and 91 multiple-choice questions. Ten representative Chinese and international general LLMs are evaluated alongside the reasoning models OpenAI o1 and DeepSeek-R1 and the civil-engineering domain model CivilGPT. The reported conclusion is that general base models without civil-engineering corpus training still fall short of human experts, that models handle regulation- and law-oriented text comprehension better than tasks requiring mathematical reasoning, and that multiple-choice items remain the weakest format.

## Tasks

517 objective questions in total: 426 single-choice and 91 multiple-choice items, distributed over 8 examination subjects. By certificate: Class-1 Registered Architect — Construction Economics, Construction and Design Practice Management (68 single-choice), Building Materials and Construction (63 single-choice), Pre-design and Site Design (41 single-choice); Class-2 Registered Architect — Building Structures, Building Physics and Services (51 single-choice); Supervising Engineer — Construction Contract Management (50 single-choice, 30 multiple-choice), Basic Theory and Related Regulations of Construction Supervision (50 single-choice, 30 multiple-choice), Project Objective Control for civil works (67 single-choice, 20 multiple-choice), and Project Objective Control for transportation (36 single-choice, 11 multiple-choice). Items were drawn from the May 2024 sitting of these examinations and manually screened; questions containing tables, figures, or other multimodal information were discarded so that the dataset probes single-modality text understanding and reasoning. Each subject's items are further split into "easy" (answerable directly from comprehension or retrieval of laws, regulations, standards, and engineering common sense) and "hard" (requiring mathematical calculation and logical reasoning grounded in standards and mechanics fundamentals); reported hard-question shares per subject range from 17.65% to 34.15%.

## Domains

Civil & Structural Engineering, covering building structures and building physics/services, building materials and construction, pre-design and site design, construction economics and practice management, construction contract management, and construction-supervision theory and regulations. One subject targets project objective control for transportation infrastructure, so the dataset also spans transportation-infrastructure engineering within the same domain.

## Evaluation

Scoring is the accuracy of the answer-option symbols the model emits. A multiple-choice item counts as correct only when the selected set matches the reference exactly; single-choice items require the one correct option out of four. Malformed responses — multiple selections on a single-choice item, incomplete selections on a multiple-choice item, or failure to produce an option — are all graded as wrong. Following the real examinations, single-choice items are worth 1 point and multiple-choice items 2 points. Subjects are then given different weights according to their share of hard questions (weight 3 for a hard share below 20%, 4 for 20–30%, and 5 above 30%), and a weighted average accuracy is computed. Testing is zero-shot without an added chain-of-thought prompt. To limit contamination, model versions released before the examination date were used wherever possible (GPT-4o, DeepSeek-R1, and CivilGPT excepted). Reported headline results: CivilGPT reaches 73.0% average accuracy and the best score in 4 of the 8 subjects; DeepSeek-R1 reaches 70.6%; iFlytek Spark is the strongest non-reasoning general LLM at 69.3%; the lowest-scoring model is Claude at 38.8%.

## Typical Duration

N/A — single-turn, zero-shot multiple-choice question answering; no trajectory length, wall-clock, or token budget is reported.

## Main Contribution

A Chinese-language civil- and transportation-engineering knowledge evaluation dataset assembled from national registration examinations, plus an evaluation method that combines exam-faithful item scoring with difficulty-based subject weighting, applied to general LLMs, reasoning models, and a domain-specific model in order to locate where industry-specific large models still fall short.

## Key Design Ideas

- Source items from government-administered national registration examinations, on the argument that their official backing, expert authorship, and review process make contamination from web resources and past papers less likely.
- Restrict the dataset to objective multiple-choice items so that grading avoids the subjectivity and variance of manual scoring.
- Manually discard questions whose content depends on tables or figures, isolating single-modality text comprehension and reasoning.
- Split items into easy and hard by whether the answer follows from text retrieval or requires calculation and standards-based reasoning, and weight subjects by their hard-question share.
- Score multiple-choice items only on exact set match, and weight them at twice a single-choice item to reflect their greater difficulty.
- Select model versions predating the examination date where possible to reduce training-data contamination.

## Strengths

- Task counts, per-subject question distributions, difficulty shares, and scoring weights are all specified, so the evaluation is reproducible in protocol even where the items themselves are exam-derived.
- Covers a breadth of professional civil-engineering subjects — structures, materials, site design, economics, contract management, and supervision regulations — rather than a single narrow topic.
- Compares three model families that are usually reported separately: general LLMs, reasoning models, and a domain-pretrained civil-engineering model, which isolates the effect of domain corpus training versus reasoning ability.
- Contamination control is addressed explicitly through both the source of the items and the choice of model release dates.

## Limitations

- Text-only by construction: multimodal items were removed, so drawings, detailing, and diagram-based engineering reasoning — a large part of real practice — are out of scope.
- All items are multiple-choice knowledge questions; there is no executable task, no design or analysis deliverable, and no agentic tool use or trajectory.
- Evaluation is single-turn and zero-shot without chain-of-thought, so the reported gaps reflect a specific prompting regime rather than a model's best attainable performance.
- Repository note: no public code or data release is cited in the article record, so the dataset itself does not appear to be independently obtainable.
- Repository note: several per-model, per-subject accuracies in the results table could not be transcribed with confidence from the primary PDF and are left as TODO(reference).

## Related Works

- [StructureClaw](./structureclaw.md) — the other structural-engineering evaluation in the repository, but executable and solver-verified rather than exam-derived multiple choice.
- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction benchmark that includes a civil field.
- [MaScQA](./mascqa.md) — the same exam-derived static-QA paradigm applied to materials science via India's GATE examinations.
- [EEE-Bench](./eee-bench.md) — professional-examination-style engineering benchmark in the electrical and electronics domain.
