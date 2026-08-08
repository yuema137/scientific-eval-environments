# Software & Systems Engineering

> **English** | [简体中文](../zh/domains/software_systems_engineering.md) · [← All domains](./README.md)

## Scope

Building and verifying software as engineering: code generation on real repositories, environment configuration, formal specification and verification. Web/UI agents and computer use are not software engineering.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| SWE-bench | 2023 | Resolve real GitHub issues by editing the codebase of one of 12 popular open-source Python repositories. | 2,294 issue–pull-request instances; the model produces a single patch per instance. | The repository's own test suite: every FAIL_TO_PASS and every PASS_TO_PASS test must pass after applying the patch; no partial credit. | [→](../works/swe-bench.md) |
| SWE-chat | 2026 | Real-world software engineering as actually practiced: in-the-wild human–agent coding sessions on open-source repositories, spanning code understanding, creation, git operations, and debugging. | ~6,000 logged sessions from 200+ public repositories with 13,000+ checkpoints and line-level human-vs.-agent authorship attribution; observational, no authored tasks. | Commit-grounded outcomes (survival of agent code into user commits), Semgrep security scans on pre/post-commit snapshots, and LLM annotations validated against human gold labels. | [→](../works/swe-chat.md) |
| Enconda-bench | 2025 | Diagnose and repair injected errors in repository setup documentation, then build the software environment and run its tests. | 4,201 erroneous-README tasks carrying 9,471 injected errors across 323 repositories pinned to fixed commits, stratified into difficulty levels 1–10. | Docker-executed Pass@1 (environment builds, tests execute, clean exit) plus per-capability precision/recall on diagnosis and repair; each injected error validated to actually break setup. | [→](../works/enconda-bench.md) |
| AgentLens | 2026 | Interactive Java coding-assistant work on real open-source Spring Boot projects: unit testing and test refactoring, legacy database-logic migration, API documentation and DTO cleanup. | 16 interview- and production-derived scenarios, each run under a relaxed and a mildly adversarial user persona (32 trajectories per agent). | Formal verification — tests, repository-state assertions, build execution, static analysis, all must pass — combined with five LLM-judge dimensions into a Quality Index. | [→](../works/agentlens.md) |
| SysMoBench | 2025 | Write formal TLA+ models of real concurrent and distributed systems — OS synchronization primitives, Raft implementations, ZooKeeper leader election — at a granularity fixed by the task. | 11 system artifacts spanning 175–5,360 source lines in Rust, Go, C, and Java; each task requires a TLA+ model plus its TLC configuration. | Four machine-checked, sequentially gated metrics: SANY syntax, TLC runtime, trace conformance against instrumented executions, and invariant model checking; explicitly no LLM judge. | [→](../works/sysmobench.md) |
| VCoT-Bench | 2026 | Complete deliberately removed blocks — lemmas, loop invariants, assertions — of the verification chain-of-thought behind verified Rust programs in Verus. | 1,988 completion tasks derived from 150 verified Verus programs, stratified by removal ratio, proof type, and proof location. | Verus syntax check plus semantic equivalence to the ground-truth chain judged by a protocol-guided LLM (94% agreement with author consensus), combined into a weighted accuracy. | [→](../works/vcot-bench.md) |
| Long-Horizon-Terminal-Bench | 2026 | Long-horizon terminal workflows including software engineering and scientific computing, alongside experiment reproduction, multimodal analysis, and interactive games. | 46 tasks across nine categories, each decomposed into fine-grained graded subtasks. | Dense graded subtask rewards with configurable pass thresholds (best model: 15.2% pass@1 at a 0.95 threshold, 10.9% at 1.0). | [→](../works/long-horizon-terminal-bench.md) |
| FrontierCode | 2026 | Produce maintainer-mergeable pull requests in real open-source repositories — an industry benchmark with no accompanying paper. | Maintainer-written tasks authored by 20+ experienced developers at 40+ hours per task; task counts unpublished. | Mergeability graded by an ensemble of unit tests, rubrics, and verifiers over correctness, test quality, scope discipline, and style; solution-consulting runs scored zero. | [→](../works/frontiercode.md) |
| SWE-Interact | 2026 | Complete software-engineering tasks whose requirements arrive progressively from a simulated user. | Multi-turn user-driven sessions paired with single-turn baselines on the same tasks. | Task success under the interactive protocol versus single-turn (~50% vs. ~25% for top models). | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | Collaborate with a user on repository-level coding tasks reconstructed from real sessions. | 109 tasks curated from 11,260 recorded sessions, replayed via an intent-preserving user simulator. | Final repository correctness plus the number of corrective feedback turns required. | [→](../works/swe-together.md) |

## Related Works

- [SWE-bench](../works/swe-bench.md)
- [SWE-chat](../works/swe-chat.md)
- [Enconda-bench](../works/enconda-bench.md)
- [AgentLens](../works/agentlens.md)
- [SysMoBench](../works/sysmobench.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FrontierCode](../works/frontiercode.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
