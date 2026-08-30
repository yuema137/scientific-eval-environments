# PE Civil Bench (2026)

> **English** | [简体中文](../zh/works/pe-civil-bench.md)

> **First appeared:** 2026-03-26 · **Source:** [Official repository creation](https://github.com/komal-blkmmb/Benchmarking_agentic-design_and_evaluation)

## Overview

PE Civil Bench is an open benchmark of 150 professional-licensure-style civil engineering problems, modelled
after the NCEES Fundamentals of Engineering and Professional Engineering Civil examinations, used to compare
base prompting, vector retrieval-augmented generation, and agentic RAG across thirteen frontier and
open-weight LLMs, and paired with an agentic reinforced-concrete component-design pipeline validated against
finite-element analysis.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://doi.org/10.1016/j.cacaie.2026.100126
- **Code:** https://github.com/komal-blkmmb/Benchmarking_agentic-design_and_evaluation
- **Venue:** Computer-Aided Civil and Infrastructure Engineering, vol. 49, art. 100126 (2026)

## Summary

The work addresses the absence of a standardized civil engineering corpus for evaluating LLMs and
augmentation strategies, a gap that the authors contrast with the mature datasets available in mathematics
and medicine. PE Civil Bench supplies that corpus as licensure-exam problems annotated by subdiscipline,
difficulty, question type, and reasoning demand, and establishes baseline performance for thirteen models
under base prompting, vector RAG, and agentic RAG. A second contribution is a multi-agent framework that
automates reinforced-concrete element design through code retrieval, calculation, validation, and iterative
refinement while emitting transparent reasoning traces. The framework is exercised on 33 beam configurations
and then extended to column design without reprogramming, and an autonomous evaluator is calibrated against
traditional assessment.

## Tasks

150 FE- and PE-style problems: 110 multiple-choice questions in the FE style testing conceptual reasoning,
calculation, and code interpretation, and 40 open-ended numerical problems in the PE style requiring
multi-step formulation and engineering judgement. The released dataset spans eight subdisciplines —
construction, ethics, geotechnical, mathematics, structural, surveying, transportation, and water resources.
Questions were curated by professional engineers at the Structures and Artificial Intelligence Lab,
University of Houston, and each was manually annotated along four dimensions: subdiscipline, difficulty,
question type, and reasoning demand. A separate PE Civil Design dataset supports the component-design track,
holding parametric inputs (span length, beam width and depth, concrete strength, steel yield strength, dead
and live loads, clear cover) paired with ETABS finite-element outputs as ground truth; 33 beam configurations
are reported in the design experiments. Both datasets are released under CC-BY-4.0.

## Domains

Civil & Structural Engineering. The evaluated objective is civil engineering practice as tested for
professional licensure, with the exam subdisciplines covering structural analysis and design, geotechnical
engineering, transportation, water resources, surveying, and construction — each a canonical civil
engineering subarea that folds into this domain under the repository's taxonomy, including water-resources
questions, which concern hydraulic infrastructure rather than environmental process science. The design track
is unambiguously structural: reinforced-concrete beam and column proportioning and detailing checked for
design-code compliance and cross-validated against finite-element results. No co-domain is claimed.

## Evaluation

Exam problems are scored under three configurations applied to the same question set — baseline prompting
with no augmentation, vector RAG over a retrieved corpus, and agentic RAG that couples reasoning agents with
iterative retrieval — so that the benchmark isolates the contribution of each augmentation strategy rather
than only ranking models. Multiple-choice items are graded by answer correctness; open-ended numerical items
require the multi-step derived value. For the design track, generated reinforced-concrete designs are checked
for code compliance and their computed quantities correlated against finite-element analysis, with the
reported agreement at r ≥ 0.90 over the 33 beam configurations. An autonomous LLM evaluator is separately
calibrated against traditional assessment methods, reaching r = 0.976 agreement. Per-model accuracy figures
across the thirteen systems and three configurations: TODO(reference) — the publisher's full text could not be
retrieved.

## Typical Duration

N/A — the accessible record does not report per-task wall-clock time, trajectory length, or token budget.

## Main Contribution

The authors present PE Civil Bench as the first benchmark built from Fundamentals of Engineering and
Professional Engineering Civil examination questions, establishing baseline performance across thirteen
frontier models under base, retrieval-augmented, and multi-agent prompting strategies, and demonstrating an
extensible agentic framework that produces code-compliant reinforced-concrete designs matching
finite-element analysis while generalizing from beam to column design without reprogramming.

## Key Design Ideas

- Licensure examinations are used as the task source, which supplies problems already vetted for professional
  relevance and difficulty calibration rather than requiring the authors to invent a difficulty scale.
- Two answer formats are deliberately mixed: multiple choice to probe conceptual reasoning and code
  interpretation, open-ended numerical to force multi-step formulation where an answer cannot be guessed.
- Four-dimensional manual annotation (subdiscipline, difficulty, question type, reasoning demand) allows
  results to be sliced by what a question actually demands.
- Augmentation strategy, not just model identity, is a first-class experimental factor, with the same
  benchmark run under base, vector-RAG, and agentic-RAG conditions.
- The component-design track closes the loop with an external physical check, correlating agent-produced
  designs against ETABS finite-element ground truth rather than against a rubric.
- The design pipeline is architected for extension, evidenced by transferring from beam to column design
  without reprogramming.

## Strengths

- Broad subdiscipline coverage across eight civil engineering areas, unusual for a domain benchmark that also
  ships an executable design track.
- Both the question benchmark and the design dataset are publicly released under a permissive licence, with
  accompanying notebook code.
- Model coverage spans thirteen frontier and open-weight systems, giving a usable spread rather than a
  two-model comparison.
- The design results are validated against an independent finite-element tool rather than the agent's own
  computation.
- An autonomous evaluator is validated against conventional assessment before being relied upon, rather than
  assumed trustworthy.

## Limitations

- At 150 questions the benchmark is small relative to the eight subdisciplines it spans, so per-subdiscipline
  cells are thin.
- The design track validates on a single component class family — reinforced-concrete beams, with a column
  extension — rather than complete structural systems.
- Repository note: the article is hybrid open access but the publisher's full text returned HTTP 403 to
  automated retrieval, so per-model scores, the agentic-RAG gain over vector RAG, and the retrieval corpus
  composition are recorded here as unverified.
- Repository note: exam problems test knowledge recall and closed-form calculation under a known answer key,
  which measures professional-competency reasoning rather than long-horizon agent behaviour; only the design
  track exercises multi-step tool-mediated work.

## Related Works

- [StructureClaw](./structureclaw.md) — structural-engineering agent benchmark with executable solver
  verification, complementing the exam-style question format used here.
- [MASSE](./masse.md) — structural engineering multi-agent system evaluated on rubric-scored real consulting
  workflows, sharing the code-compliance and capacity-verification objective.
- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction benchmark whose taxonomy includes
  a civil engineering field.
- [EEE-Bench](./eee-bench.md) — professional-examination-style engineering benchmark in the electrical and
  electronics domain, the same evaluation format applied to a different field.
- [ChemEBench](./chemebench.md) — domain engineering benchmark organized by professional engineering skill
  levels rather than exam provenance.
