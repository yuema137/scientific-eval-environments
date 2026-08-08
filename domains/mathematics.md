# Mathematics

> **English** | [简体中文](../zh/domains/mathematics.md) · [← All domains](./README.md)

## Scope

Mathematical reasoning and proof: olympiad and research mathematics, formal mathematics, and logic-grounded deduction. Applied mathematics and statistics fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Hard2Verify | 2025 | Grade the individual steps of frontier-model proofs to recent open-ended Olympiad problems (IMO Shortlist, Putnam, EGMO, USAMO). | 1,860 expert-labeled steps across 200 model-generated solutions to 80 post-2024 problems, produced with 500+ hours of expert labor. | Expert binary step labels as ground truth; verifiers scored on step-level, response-level, and first-error (ErrorID) balanced accuracy and F1. | [→](../works/hard2verify.md) |
| ProcessBench | 2024 | Locate the earliest erroneous step in step-by-step mathematical solutions, from grade-school (GSM8K) to competition and Olympiad level (MATH, OlympiadBench, Omni-MATH). | 3,400 problem–solution pairs, solutions from twelve open-source generators reformatted into uniform paragraph-level steps. | Expert-annotated earliest-error index as ground truth; judges scored by harmonic-mean F1 over erroneous and correct samples. | [→](../works/processbench.md) |
| PRMBench | 2025 | Detect fine-grained error types in multi-step mathematical reasoning — nine sub-categories under simplicity, soundness, and sensitivity. | 6,216 instances carrying 83,456 step-level labels (avg. 13.4 steps per instance), with injected ground-truth negative steps. | Step-level binary classification against the injected labels; negative F1 and PRMScore, with a human annotator baseline. | [→](../works/prmbench.md) |
| Pseudo-Formalization | 2026 | Verify natural-language mathematical proofs — olympiad, Putnam, and published research mathematics — by rewriting them into self-contained premise–conclusion modules checked independently. | 200 frontier-model proofs (via Hard2Verify) plus ArxivMathGradingBench: 35 arXiv research papers carrying 40 author-disclosed errors. | Step- and proof-level precision/recall against expert labels; on arXiv papers, error-location matching against the authors' own disclosed corrections. | [→](../works/pseudo-formalization.md) |
| FormalRewardBench | 2026 | Prefer a correct Lean 4 proof over an incorrect variant, on olympiad-level algebra, number theory, and combinatorics from MiniF2F. | 250 preference pairs; incorrect variants produced by five expert-curated error-injection strategies. | Ground truth determined by the Lean type checker; reward models scored by pointwise and position-consistent pairwise accuracy. | [→](../works/formalrewardbench.md) |
| MATP | 2025 | Adjudicate each step of natural-language deductive reasoning by autoformalizing it to First-Order Logic and invoking an automated theorem prover. | 10,830 reasoning instances (1,083 cases × 10 LLMs) from PrOntoQA-OOD, ProofWriter, and FOLIO, deliberately sampled from harder subsets. | Prover verdicts (True / False / Unknown) on each step and its negation; valid-proof-path existence checked against ground-truth labels. | [→](../works/matp.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks in mathematics, one of its four fields, covering the full research lifecycle with no baseline code provided. | 20 tasks total across the suite; the agent submits held-out test-split predictions as a CSV. | Execution-based, outcome-only scoring by task-specific evaluators; SOTA-normalized score with a 'march of nines' transform near the ceiling. | [→](../works/airs-bench.md) |
| Terminal-Bench Science | 2026 | Applied and formal mathematics, operations research, and statistics tasks in the Mathematical Sciences track of its five-track suite. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Math is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |

## Related Works

- [Hard2Verify](../works/hard2verify.md)
- [ProcessBench](../works/processbench.md)
- [PRMBench](../works/prmbench.md)
- [Pseudo-Formalization](../works/pseudo-formalization.md)
- [FormalRewardBench](../works/formalrewardbench.md)
- [MATP](../works/matp.md)
- [AIRS-Bench](../works/airs-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
