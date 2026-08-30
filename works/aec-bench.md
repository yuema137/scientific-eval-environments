# AEC-Bench (2026)

> **English** | [简体中文](../zh/works/aec-bench.md)

> **First appeared:** 2026-03-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2603.29199)

## Overview

AEC-Bench is a multimodal agentic benchmark over real construction document sets: 196 task instances across nine task families and three scope levels, executed by agents in sandboxed Docker environments through the Harbor harness and graded by task-specific automatic verifiers on structured findings.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.29199>
- **Code:** <https://github.com/nomic-ai/aec-bench>
- **Venue:** arXiv preprint, 2026

## Summary

The benchmark targets the document work that actually consumes engineering time on a construction project: reading details, resolving callouts and cross-references across a drawing set, reconciling specifications against drawings, and reviewing submittals. Agents operate in a sandboxed environment with Bash access and CLI PDF tooling, so they must navigate the document space themselves rather than being handed pre-extracted content, and they report their conclusions as structured JSONL findings that automatic verifiers grade against ground truth. Tasks are organized by how much context they require — a single sheet, a full drawing set, or the whole project — which separates context-assembly failures from reasoning failures. The authors also ablate the tooling around fixed model backends to isolate what document parsing contributes.

## Tasks

196 task instances in nine families across three scope levels. Intra-sheet, single-page reasoning (43 instances): detail technical review (14), answering localized technical questions about a detail; detail title accuracy (15), checking whether detail titles match what is drawn; note callout accuracy (14), checking whether callout text correctly describes the referenced element. Intra-drawing, cross-sheet reasoning within one set (89 instances): cross-reference resolution (51), finding references that do not resolve to a valid target; cross-reference tracing (24), finding all source locations that reference a given detail; sheet index consistency (14), comparing index entries against title blocks. Intra-project, cross-document reasoning (64 instances): drawing navigation (12), locating the correct file, sheet and detail for a query; specification–drawing sync (16), identifying conflicts between specifications and drawings; submittal review (36), evaluating submittals for compliance with specifications and drawings. Documents are publicly available PDF construction document sets from public-sector projects, spanning architectural, structural, civil, mechanical, electrical and plumbing disciplines.

## Domains

Civil & Structural Engineering: the evaluated objects are real construction document sets — drawings, sheet indices, specifications and submittals — and the judgment-heavy families (detail technical review, specification–drawing sync, submittal review) require compliance verdicts against project specifications, which is construction-engineering review work. The document sets are multi-discipline (architectural, structural, civil, MEP), but the evaluated task is engineering document verification rather than architectural design, so no second canonical domain is claimed.

## Evaluation

- Agents run in sandboxed Docker containers through the Harbor evaluation framework, with per-task asset manifests specifying the documents to fetch, and emit findings into a standardized JSONL output file.
- Task-specific automatic verifiers grade the findings against known ground truth, awarding full credit for complete and correct findings, partial credit for partially correct output, and zero for incorrect or unsupported results. No LLM judge is used.
- **Reported.** GPT-5.4, GPT-5.2, Opus 4.6 and Sonnet 4.6 were evaluated under a base harness and under the harness augmented with Nomic document-parsing tools. Structured parsing improves retrieval-sensitive tasks by roughly 20–32% while slightly degrading visually grounded tasks. Drawing navigation reaches 100.0 reward (GPT-5.4 with Nomic tools), whereas submittal review tops out at 23.1 — the hardest family. The authors' conclusion is that general-purpose coding agents transfer only partially to construction-document work, struggling with spatial grounding and judgment-heavy review, and that on submittal review "correct outputs depend not only on retrieving evidence but also on applying domain-specific judgment and prioritization consistent with professional review standards."

## Typical Duration

N/A — the paper reports no runtime, token budget, or per-task agent-step counts.

## Main Contribution

An agentic, executably verified benchmark for AEC document work built on real project documents, with a scope-level taxonomy that distinguishes single-sheet, cross-sheet and cross-project reasoning, and a tool ablation showing which harness capabilities move which task families.

## Key Design Ideas

- Three scope levels (intra-sheet, intra-drawing, intra-project) make context assembly an explicit, measured axis rather than an implicit confound.
- Structured JSONL findings make automatic verification possible with graded partial credit, avoiding free-text judging.
- Agents get a terminal sandbox with CLI PDF tooling instead of pre-parsed inputs, so document navigation is part of the evaluated task.
- Holding models fixed while varying the tool layer (base harness vs. added parsing tools) isolates the contribution of document parsing from model capability.

## Strengths

- Real, publicly sourced multi-discipline construction document sets from public-sector projects rather than synthetic drawings.
- Deterministic verifiers with partial credit, no LLM-as-a-judge dependency.
- Apache-2.0 release of dataset, agent tools and evaluation harness.

## Limitations

- 196 instances is a small suite, and several families are unevenly sized (51 cross-reference-resolution instances against 12 drawing-navigation instances).
- Repository note: several families — cross-reference resolution and tracing, sheet index consistency, drawing navigation — measure document consistency and retrieval rather than engineering judgment; the substantive engineering verdicts sit in detail technical review, specification–drawing sync and submittal review.
- Repository note: no runtime, token, or step accounting is reported, so cost comparisons across harness configurations are not possible from the paper.
- Repository note: the name collides with AECBench (Liang et al., *Advanced Engineering Informatics* 2026); the two are unrelated works.

## Related Works

- [AECBench](./aecbench.md) — Similarly named but distinct: a five-level AEC knowledge-QA benchmark rather than an agentic document environment.
- [DrafterBench](./drafterbench.md) — Also agents on civil-engineering drawings, but editing them with tools instead of reviewing them for errors.
- [StructureClaw](./structureclaw.md) — Also engineering verification by executable checks, on structural models rather than construction documents.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also containerized agent tasks with deterministic programmatic verification.
