# ChemEBench (2025)

> **English** | [简体中文](../zh/works/chemebench.md)

## Overview

ChemEBench is a chemical-engineering evaluation benchmark introduced alongside ChemELLM, a 70-billion-parameter domain-specific language model built on Spark-70B by the Dalian Institute of Chemical Physics and iFLYTEK. It organizes evaluation into three progressive levels covering 15 dimensions and 101 distinct chemical-engineering tasks, from foundational domain knowledge through professional engineering skills such as equipment selection, separation, heat transfer, process safety, and process economics.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://doi.org/10.1016/S1872-2067(25)64725-5>
- **Venue:** Chinese Journal of Catalysis, vol. 73 (2025), pp. 159–173

## Summary

The paper "From lab to fab: A large language model for chemical engineering" presents three coupled artifacts: ChemEData, a curated chemical-engineering corpus of 19 billion pre-training tokens and 1 billion fine-tuning tokens; ChemELLM, a 70B model obtained by domain-adaptive pre-training and supervised fine-tuning of Spark-70B on that corpus; and ChemEBench, described by the authors as the first multidimensional benchmark for chemical engineering. ChemEBench is used to compare ChemELLM against fourteen mainstream commercial and open-weight models on a level-structured task suite that rises from factual chemical-engineering knowledge to applied professional skills. The framing of the benchmark is capability measurement in a discipline where general-purpose models are argued to be shallow, rather than agentic or tool-using evaluation.

## Tasks

ChemEBench comprises three progressive levels evaluating 15 dimensions of LLM capability across 101 distinct chemical tasks.

- **L1 — Foundational knowledge:** objective items (multiple choice, fill-in-the-blank, true/false) and subjective items (short answer, calculation) over fundamental chemical-engineering concepts.
- **L2 — Advanced knowledge:** SMILES-to-IUPAC name translation, molecular name generation from textual descriptions, molecular property prediction, and reaction prediction (reactants/products, high-yield assessment).
- **L3 — Professional skill:** applied engineering tasks spanning catalyst (deactivation, stability, industrial processes), equipment (reactors, dryers, centrifuges, pumps, towers), fluid simulation (CFD, discrete element method, machine learning, DNS), separation (absorption, distillation, extraction), heat exchangers, safety (process, environmental, personnel, equipment, regulatory, hazardous chemistry), economics, and engineering construction (electrical, automatic control, materials, equipment, civil, thermal, water supply and drainage, plot planning, chemical systems, fire protection).

The 15 dimensions are catalyst, equipment, simulation, separation, heat, safety, economics, electrical engineering, automatic control, material engineering, equipment engineering, civil engineering, thermal engineering, water supply/drainage engineering, and fire protection engineering.

TODO(reference) — the paper does not state the total number of benchmark questions, the per-level item counts, or the sourcing and expert-verification procedure used to construct the benchmark items.

## Domains

Chemical Engineering is the primary domain: the L1 and L3 levels are chemical-engineering knowledge and applied process-engineering skill — reactor and separation equipment, distillation/absorption/extraction, heat exchangers, process and plant safety, process economics, fluid simulation methods, and plant engineering-construction disciplines (electrical, control, civil, thermal, water/drainage, fire protection). Chemistry is a genuine co-domain through the L2 level, whose tasks are molecular nomenclature translation, molecular property prediction, and reaction prediction rather than process-engineering objectives.

## Evaluation

Scoring is item-type dependent. Objective formats — multiple choice, fill-in-the-blank, and true/false — are scored by accuracy. Subjective formats — short answer and calculation — are graded on a score scale, using criteria that require the answer to be complete and clear without omitting critical information, and that require the reasoning chain to be checked step by step for factual, logical, computational, or knowledge errors, each rated 0–5.

Fourteen models were evaluated: ChemELLM, DeepSeek-R1, DeepSeek-V3, O1-Preview, O3-mini, GPT-4o, Claude-3.7, ERNIE-4.0, GLM-4, Kimi, LLaMA 3.1-70B, ChemDFM-13B, ChemLLM-7B-Char-1.5-SFT, and LlaSMol-Mistral-7B. Reported mean scores place ChemELLM first at 72.90, followed by DeepSeek-R1 at 70.33 and O1-Preview at 65.76; the chemistry-specialized small models score lowest (ChemDFM-13B 31.22, ChemLLM-7B-Char-1.5-SFT 20.67, LlaSMol-Mistral-7B 19.81).

## Typical Duration

N/A — ChemEBench is a static question-answering benchmark with single-response items; the paper reports no trajectory length, wall-clock time, or token budget per task.

## Main Contribution

In the authors' framing, the paper contributes ChemELLM, a 70-billion-parameter LLM specialized for chemical engineering; ChemEData, a purpose-built domain corpus of 19 billion pre-training tokens and 1 billion fine-tuning tokens; and ChemEBench, presented as the first multidimensional benchmark for chemical engineering, spanning 15 dimensions and 101 essential tasks over three progressive capability levels.

## Key Design Ideas

- Three-level progression — foundational knowledge, advanced knowledge, professional skill — so that domain recall, chemical prediction, and applied engineering judgment are measured separately rather than as one aggregate score.
- Breadth over the plant-engineering disciplines, including electrical, automatic control, civil, thermal, water supply and drainage, and fire protection engineering, which are rarely represented in chemistry-oriented LLM benchmarks.
- Mixed item formats within a level: accuracy-scored objective items alongside score-graded calculation and short-answer items, so numerical process calculations are not reduced to multiple choice.
- Rubric-based grading of subjective items that scores the reasoning chain step by step (0–5) rather than only the final answer.
- Baseline panel deliberately mixes general-purpose reasoning models, commercial APIs, and chemistry-specialized open-weight models, isolating the gap between chemistry specialization and chemical-engineering competence.

## Strengths

- Covers chemical engineering as a discipline rather than as an extension of chemistry, with L3 dimensions for equipment, separation, heat transfer, safety, economics, and engineering construction.
- The level structure separates knowledge recall from applied professional skill, making capability gaps legible instead of averaged away.
- Fourteen models evaluated, including four chemistry-specialized models, giving a comparison that distinguishes molecular-chemistry specialization from process-engineering competence.
- Built on a documented domain corpus (1.06 million scholarly papers, 5.79 million chemical patents, and 1,200 professional books for pre-training), so the discipline coverage is grounded in the industrial literature.

## Limitations

- The benchmark's construction protocol is not reported: the paper states the dimension and task counts but not the total number of items, the per-level distribution, the sourcing of questions, or whether items were validated by chemical-engineering experts.
- Item formats are static question answering; there is no tool use, simulator execution, or multi-step agent trajectory, so "professional skill" is measured by written answers rather than by executed engineering work. Fluid-simulation and equipment dimensions are assessed as questions about those subjects, not by running a simulation.
- The scoring rubric for subjective and calculation items is described qualitatively (0–5 on completeness/clarity and reasoning-chain correctness), and the paper does not state who or what applies it, leaving the grader — human expert or model judge — unspecified.
- Repository note: the benchmark is introduced inside a paper whose headline claim is that the authors' own model ChemELLM leads the leaderboard, and the benchmark shares its authorship and its ChemEData source corpus with that model's training pipeline, so the reported ranking is not an independent measurement.
- Repository note: ChemEBench does not appear to be publicly released. The paper points to a public chat deployment of ChemELLM (`https://chemindustry.iflytek.com/chat`) rather than to benchmark data, and the associated GitHub repository referenced for the project (`DICPZhou/ChemELLM`) contained only a licence and a one-line README when checked, with no test data or evaluation harness.
- Repository note: the L2 level overlaps substantially with existing molecular-chemistry benchmarks (nomenclature translation, property prediction, reaction prediction), so roughly a third of the level structure is not chemical-engineering evaluation.

## Related Works

- [CeProBench](./ceprobench.md) — chemical-process-development benchmark that scores the same discipline through executed PFD and Aspen Plus tasks rather than written answers.
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — chemical-engineering evaluation narrowed to thermodynamics calculation, comparable to the calculation items in ChemEBench L1.
- [ChemEval](./chemeval.md) — same multi-level, multi-dimension, multi-task benchmark shape applied to chemistry rather than chemical engineering.
- [ChemBench](./chembench.md) — large curated chemistry question set with human-expert baselines, the chemistry-side counterpart to ChemEBench's L2 level.
- [ERI Benchmark](./eri-benchmark.md) — cross-engineering instruction benchmark that includes chemical engineering as one of nine fields.
