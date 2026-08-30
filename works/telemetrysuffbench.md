# TelemetrySuffBench (2026)

> **English** | [简体中文](../zh/works/telemetrysuffbench.md)

> **First appeared:** 2026-08-08 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.07899)

## Overview

A controlled benchmark that tests whether agent execution telemetry is *sufficient* to diagnose where a failure originated, separating three capabilities — failure detection, fault-origin localization, and safe abstention under insufficient evidence — over synthetic multi-component agent traces.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities


N/A — Agent-observability / fault-origin trajectory-diagnosis methodology over synthetic domain-agnostic traces; not a scientific/research task.

## Links

- **Paper:** https://arxiv.org/abs/2608.07899
- **Code:** https://anonymous.4open.science/r/TelemetrySuffBench-E635/README.md (anonymized repository referenced by the paper)
- **Venue:** arXiv preprint (submitted 8 August 2026)

## Summary

TelemetrySuffBench argues that telemetry which reveals *that* an agent failed may still be inadequate for identifying *where* the failure originated. It constructs canonical multi-component agent traces with delayed-binding faults (the injected fault activates later than where it is introduced) and renders each trace under controlled observability conditions: paired coarse views, seven-factor telemetry masks, and exact-equal ambiguous origin pairs. Five frontier language models are evaluated under unified protocols with explicit candidate sets, invalid-output accounting, subgroup analyses, and a frozen blind holdout. The central finding is a detection–localization gap: masked telemetry views preserve near-perfect failure detection while collapsing origin-step localization.

## Tasks

Synthetic multi-component execution traces with programmatically injected, delayed-binding faults. The paper reports a corpus of 312 traces split into a discovery split (96 traces) and a confirmation split (216 traces), with a frozen blind holdout used to reproduce the central pattern. Fault traces are organized as matched two-origin fault groups (exact-equal ambiguous origin pairs) alongside clean control traces. `TODO(reference)` — the exact holdout composition and the precise fault/clean counts per split could not be reconciled unambiguously from the primary source at the level of extraction available here.

Each trace is presented under three families of observability conditions:

- **Paired coarse views** — metadata, OpenTelemetry-compatible, and OpenInference-compatible renderings.
- **Seven-factor telemetry masks** — controlled removal of individual telemetry factors.
- **Exact-equal ambiguous origin pairs** — inputs where two candidate origins are indistinguishable, used to test abstention.

## Domains

Domain-agnostic. The traces are synthetic renderings of generic multi-component agent execution (identity/event semantics, tool inputs, state transitions, provenance mappings, verifier evidence, terminal status); the benchmark is not grounded in any scientific or engineering field. Repository note: this is an agent-observability / trajectory-diagnosis methodology contribution and carries no science or engineering domain assignment.

## Evaluation

Programmatic ground truth: hooks record the injected origin, reference activation, first visible wrong-target event, state-update symptom, and terminal failure, stored outside the model-visible trace. A localization answer is correct only when it matches the injected component and event identifiers. Reported metrics include:

- **Origin-step Top-1 accuracy** for fault localization.
- **Detection F1** and **fault-type Macro-F1** for failure detection.
- **False-answer rate (FAR)** and **unnecessary-abstention rate (UAR)** for the abstention research question, with coverage measured as the proportion of valid unique-origin answers.
- **Invalid-output accounting:** malformed, inconsistent, out-of-candidate, and out-of-taxonomy outputs remain in the denominator and receive no correctness credit.

Reported results: with full telemetry, origin-step Top-1 accuracy ranges from 33.8% to 97.2% across models. Metadata, OpenTelemetry-compatible, and OpenInference-compatible views retain 99.5% to 100% detection F1 while limiting origin-step accuracy to at most 0.5%. Removing decision content reduces origin-step accuracy to zero for every model; provenance removal also causes large, model-dependent losses. On ambiguous inputs requiring abstention, evidence gating reduces unsupported unique-origin answers by 12.5 to 48.6 percentage points for three models, while two models still answer every case.

## Typical Duration

N/A — single-shot diagnostic queries over pre-rendered static traces; the paper does not report per-instance wall-clock time or token budgets. `TODO(reference)`

## Main Contribution

A controlled benchmark that operationalizes the distinction between failure *detection* and fault-*origin* localization from agent telemetry, quantifying a detection–localization gap and showing that terminal status supports detection whereas reliable causal attribution requires explicit decision-to-provenance links. It additionally frames safe abstention under insufficient evidence as a measured capability with strong model dependence.

## Key Design Ideas

- **Delayed-binding faults.** Faults activate at a step later than where they are introduced, decoupling the observable symptom from the true origin.
- **Seven telemetry factors** subjected to ablation: identity and event semantics; decision and latent-reference content; registry and provenance mappings; propagation and handoff relations; tool inputs and state transitions; observation and verifier evidence; terminal failure status.
- **Standardized observability renderings** aligned to metadata, OpenTelemetry, and OpenInference views to test which real-world telemetry schemas suffice.
- **Exact-equal ambiguous origin pairs** that make abstention the correct behavior, separating calibrated abstention from guessing.
- **Programmatic, model-invisible ground truth** and an invalid-output accounting rule that keeps malformed answers in the denominator.
- **Frozen blind holdout** used to check that the central pattern reproduces outside the development splits.

## Strengths

- Isolates fault-origin localization from failure detection under matched conditions, directly exposing a detection–localization gap that a single accuracy number would hide (paper).
- Ties observability conditions to real telemetry schemas (OpenTelemetry, OpenInference), making the "is my telemetry enough?" question concrete for practitioners (paper).
- Rigorous protocol hygiene: explicit candidate sets, invalid-output accounting in the denominator, subgroup analyses, and a frozen blind holdout (paper).
- Treats safe abstention as a first-class measured capability rather than assuming models should always answer (paper).

## Limitations

- Traces are synthetic/canonical constructions rather than logs from deployed agent systems; the paper's canonical-trace design may not capture the full messiness of production telemetry (paper describes traces as controlled/canonical). Repository note: generalization to in-the-wild traces is not established by the reported experiments.
- Evaluation covers five frontier language models; results such as the abstention behavior are strongly model-dependent, so the reported ranges are specific to the tested set (paper).
- The code/data pointer given is an anonymized repository, consistent with a work under review; a canonical permanent artifact URL is not yet available. Repository note.

## Related Works

- [TRAJDEBUG](./trajdebug.md) — also separates failure-determining errors from recoverable ones in agent trajectories via error identification and localization.
- [SearchAuditor](./searchauditor.md) — benchmarks critical-step localization, root-cause attribution, and repair over failed agent trajectories.
- [AgentAtlas](./agentatlas.md) — diagnostic overlay providing control-decision and failure taxonomies across agent benchmarks.
- [Insights Generator](./insights-generator.md) — corpus-level trace diagnostics for agent failures.
- [AgentProcessBench](./agentprocessbench.md) — step-level effectiveness labeling and first-error localization over tool-use trajectories.
