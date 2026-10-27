# PHYRD (2026)

> **English** | [简体中文](../zh/works/phyrd.md)

> **First appeared:** 2026-10-23 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.32575)

## Overview

PHYRD tests two kinds of theoretical-physics derivation. Reproduce asks a model to rebuild a published result from stated premises. Discover changes one condition from a source paper and asks what follows. Each problem is split into public subquestions scored right or wrong, so a correct final formula without the requested derivation or applicability condition earns no credit for that part.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** [PHYRD: A Living Benchmark for Reproducing and Extending Theoretical Physics Research](https://arxiv.org/abs/2610.32575), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.32575v1>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

The FormulaForest pipeline turns a source paper into a relation graph of formulas, premises, and derivation relations, each with its stated conditions. Reproduce pairs a published target with the premises needed to derive it. Discover transforms a local structure in that graph, such as an operator, coupling, symmetry, or boundary condition, and records which premises stay fixed. The solver must then decide which source arguments still hold. The authors plan timestamped additions from new papers and say each release will keep the prior task and score versions.

## Tasks

106 problems: 63 Reproduce problems with 279 public subquestions and 43 Discover problems with 225. Most Reproduce problems have four parts (39 of 63); most Discover problems have five (22 of 43). Reproduce draws on 16 source papers. In one Reproduce item, the solver derives a soft-graviton theorem from a supplied vertex, including orbital and spin terms and the contour step. In one Discover item, a matrix family is changed so that two root collisions merge, and the solver must derive new Jordan-structure and projector limits. The solver is given only the problem statement; the reference solution, per-subquestion scoring criteria, and source and verification materials are kept as separate components.

## Domains

Theoretical physics, using the five subfields adopted from PRL-Bench: astrophysics and gravitation, condensed matter, high-energy physics, quantum physics and quantum information, and statistical physics. Coverage is uneven: high-energy physics supplies 39 of 63 Reproduce and 20 of 43 Discover problems. The tasks are analytical derivations, not data analysis or experiments.

## Evaluation

- A subquestion scores 1 only when all requested conclusions, necessary derivations, and applicability conditions are correct. There is no partial credit within a subquestion. Equivalent expressions and other valid derivations are accepted; an unresolved contradiction in a required argument scores 0.
- Subquestion accuracy (SAcc) averages each problem's fraction of correct parts. Whole-problem accuracy (WAcc) counts a problem only when every part is correct. Both divide by the full problem set, so a missing answer counts as wrong.
- Five models are tested: GPT-5.6 Sol, DeepSeek v4 Pro, GLM-5.2, Kimi K2.6, and Qwen3.7-Max. Reproduce is closed-book. Discover is run closed-book and with a sandboxed Python environment (SymPy, NumPy, mpmath), public arXiv search, and paper reading, on the same 43 problems.
- Reproduce WAcc ranges from 49.21% to 68.25%, while SAcc ranges from 79.66% to 88.33%. Of 133 incomplete Reproduce responses, 78 miss one subquestion.
- Closed-book Discover WAcc ranges from 18.60% to 74.42%. With tools, four models complete more problems; DeepSeek and Qwen each gain 20.93 WAcc points, while GLM falls from 14 to 13 complete solutions.
- Each wrong subquestion receives one primary label: conceptual, derivation, calculation, or incomplete. Across 209 paired Discover answers, calculation errors fall from 123 to 67 with tools, while conceptual errors move from 70 to 75.
- Repository note: the paper specifies the scoring rules but does not state whether human graders, a model judge, or symbolic checks apply them to model answers.

## Typical Duration

Tool-assisted Discover allows up to 24 assistant turns, 128 tool calls, and two hours per problem; each Python execution is limited to 40 seconds of CPU time. Closed-book Discover API requests start with a 65,536-token completion limit. A wall-clock time for closed-book runs is not reported.

## Main Contribution

Separates deriving a published result from deriving consequences after a stated premise changes, and scores both against per-subquestion requirements that include applicability conditions.

## Key Design Ideas

- The relation graph keeps explicitly stated results separate from inferred dependencies and attaches conditions to each relation.
- Discover statements say what changes and what stays fixed, so reusing a source argument must be justified.
- Before release, a blind solver sees only the statement; its attempt is jointly reviewed against the reference solution and criteria. Hashes version each statement and task package.

## Strengths

- Reporting SAcc, WAcc, and response-level outcomes shows that many incomplete answers miss only one part.
- Discover compares the same 43 problems in both settings, with paired bootstrap intervals and per-problem gains and losses.
- Paired error counts separate calculation errors that fall with tools from conceptual errors that do not.

## Limitations

- Subfield coverage is uneven; Quantum and Stat have three Reproduce problems each, so one problem moves their accuracy by 33.3 points.
- The authors note that models may have seen related published results during training.
- The two Discover settings also differ in interaction, token limits, and, for GPT, collection through a conversational interface. The paper states that they do not isolate a tool-access effect. Some truncated answers were completed through additional calls.
- The synthetic-data result comes from a separate, anonymous under-review study. It uses 17,577 SciDeriv prompts from the Reproduce pipeline and is evaluated on PHYRD-40, a separate graded set, and Olympiad-100 from FrontierScience. The 61% to 72% Olympiad-100 gain includes a supervised fine-tuning stage that alone reaches 68%.
- Repository note: arXiv v1 links no dataset or code release.

## Related Works

- [PRL-Bench](./prl-bench.md) — Supplies the five-subfield taxonomy; builds research tasks from recent physics papers.
- [TPBench](./tpbench.md) — Evaluates theoretical-physics problems up to research level.
- [DiscoverPhysics](./discoverphysics.md) — Also changes physical premises, but through simulated experiments.
