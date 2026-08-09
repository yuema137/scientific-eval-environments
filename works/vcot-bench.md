# VCoT-Bench (2026)

> **English** | [简体中文](../zh/works/vcot-bench.md)

## Overview

VCoT-Bench is a benchmark that evaluates whether LLMs understand the Verification Chain-of-Thought (VCoT) behind Rust program verification rather than only its pass or fail outcome. It comprises 1,988 VCoT completion tasks derived from 150 verified Verus programs and stratified along three orthogonal dimensions: removal ratio, proof type, and proof location.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.18334>
- **Venue:** ICML 2026

## Summary

VCoT-Bench addresses the limitation that existing evaluations treat Rust verification as a black box, assessing models only by binary pass or fail outcomes for proof hints, which obscures whether they understand the logical deductions the proof requires. The authors introduce VCoT-Lift, a framework that lifts low-level Z3 solver reasoning into high-level, human-readable Verus proof steps, and use it to build VCoT-Bench-Org, a ground-truth corpus averaging a 6.5× increase in proof lines over Verus-Bench. Evaluation of ten state-of-the-art models reveals severe fragility: the strongest model, Claude Sonnet 4.5, falls from 71.58% accuracy at 10% block removal to 17.22% when all blocks are removed.

## Tasks

1,988 VCoT completion tasks, constructed by digging structured proof holes into VCoT-Bench-Org at the granularity of semantic blocks — lemma blocks (each independent lemma function), invariant blocks (all loop invariants for one loop), and assertion blocks (all assertions between two executable code lines). Three sub-benchmarks stratify the suite: VCoT-Bench-Ratio, 1,159 tasks that randomly remove between 1 and N of a program's N blocks; VCoT-Bench-Type, 439 tasks that remove all blocks of one type; and VCoT-Bench-Loc, 390 tasks that remove blocks from the Front (first 33%), Middle (33%–66%), or End (final 33%) of the chain. The source programs are the 150 verified Verus programs of Verus-Bench, drawn from MBPP-DFY-153, CloverBench, Diffy, and the Verus libraries.

## Domains

Formal verification of Rust programs in Verus, with proofs discharged by the Z3 SMT solver.

## Evaluation

- **Syntactic Accuracy (SynAcc).** Whether the completed program parses, checked by invoking Verus in syntax-only mode (`--no-verify`).
- **Semantic Accuracy (SemAcc).** Whether the completed steps are semantically equivalent to the ground-truth VCoT, decided by a specialized LLM-based judge guided by a protocol with curated examples; a meta-evaluation on 100 stratified tasks puts the judge at 94% agreement with author consensus.
- **Overall Accuracy (Acc).** A weighted score emphasizing semantics over syntax: each prediction is binned as both-correct, semantically-correct-only, syntactically-correct-only, or neither, weighted 1, 0.5, 0.25, and 0, then averaged over all cases and reported as a percentage.
- **Reported.** At 10% block removal accuracy spans 71.58% (Claude Sonnet 4.5) down to 32.89% (gpt-oss), and at 100% removal Claude Sonnet 4.5 falls to 17.22% and Qwen 3 think to 0.66%. Claude Sonnet 4.5 scores 68.71% on loop invariants against 39.55% on assertions, and drops from 69.04% on Front blocks to 46.35% on Middle ones. No human baseline is given.

## Typical Duration

Zero-shot completion, with all models run under default settings. Not stated: no per-task wall-clock, step, or token budget is given — the paper reports only that output limits were set sufficiently high for all programs.

## Main Contribution

A benchmark of 1,988 Verification Chain-of-Thought completion tasks, together with the VCoT-Lift framework that lifts low-level Z3 solver reasoning into human-readable Verus proof steps to supply its ground truth, moving evaluation of Rust verification beyond binary pass or fail outcomes to fine-grained analysis of verification reasoning.

## Key Design Ideas

- Solver-derived reference chains: Z3 proofs are lifted into Verus-level verification steps, so the ground truth follows the prover's own reasoning rather than a human's chosen exposition.
- A Z3 rule hierarchy sorting all 36 proof rules into 8 high-level, 12 medium-level, and 16 low-level tiers, steering the transformer toward semantically informative steps.
- A perform-all-check-partial loop in which the transformer sees the entire Z3 proof while five specialized checker agents validate only the high-level rule categories and return coarse binary complete or incomplete signals.
- A pruning and repair tail that strips trivial and redundant steps, then has the Verus verifier compile and check the program, feeding error messages back until verification succeeds.

## Strengths

- Deriving the reference chain from the solver's own proof anchors the ground truth to what verification actually required, rather than to an annotator's sense of which steps matter.
- Separating syntactic from semantic accuracy exposes per-model imbalances that a single pass or fail score would hide.
- Stratifying one corpus along removal ratio, proof type, and proof location isolates where reasoning degrades rather than only how much.

## Limitations

- Repository note: The ground-truth chain is not read directly off the solver — an LLM lifts the Z3 proof, LLM checker agents judge its completeness, and an LLM pruner trims it, while the Verus verifier gates only that the final program compiles and verifies; the completeness of the reference chain therefore rests on LLM judgement rather than on a machine-checked criterion.
- Repository note: Semantic Accuracy is assigned by an LLM judge whose reported 94% agreement is measured against author consensus on 100 stratified tasks, so semantic scores inherit that judge's residual error and its validation is not independent of the authors.

## Related Works

- [TRACE](./trace.md) — Also scores the intermediate reasoning chain instead of the final outcome alone, but over deep-research trajectories judged on cognitive quality dimensions rather than proof steps lifted from a solver.
- [T-Eval](./t-eval.md) — Also decomposes evaluation below end-task success, but along tool-use capability subprocesses rather than the type and position of missing steps within a single proof chain.
- [AgentBoard](./agentboard.md) — Also awards partial credit over intermediate steps rather than binary success, but from hand-annotated task subgoals rather than steps derived from a solver's own proof.
