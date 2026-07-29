# SysMoBench (2025)

> **English** | [简体中文](../zh/works/sysmobench.md)

## Overview

SysMoBench is a benchmark that evaluates AI's ability to write formal models of large, complex computer systems in TLA+. It covers eleven concurrent and distributed system artifacts and scores generated models with four automatically checked metrics rather than human or LLM judgement.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.23130>
- **Project:** <https://sysmobench.com>
- **Code:** <https://github.com/specula-org/SysMoBench>
- **Venue:** ICLR 2026

## Summary

SysMoBench addresses the limitation that existing AI specification benchmarks target small code fragments — function-level pre- and post-conditions, or logic puzzles — rather than complete systems, whose complex behavioral properties must be abstracted into a formal model. The authors build a benchmark over real-world concurrent and distributed system artifacts, use TLA+ as the specification language, and automate the quality metrics so that no human or LLM judge sits in the scoring loop. Across eleven system artifacts the reported results show that agents model the simplest artifacts well, while a Raft implementation such as Etcd Raft exceeds their ability.

## Tasks

Eleven system artifacts, each a task to generate a TLA+ system model together with its TLC configuration. Four are concurrent primitives from the Asterinas operating system (Spinlock, Mutex, Rwmutex, Ringbuffer, all in Rust) and seven are distributed systems (Etcd Raft in Go, Redis Raft in C, Xline CURP in Rust, ZooKeeper leader election in Java, and the PGo-synthesized dqueue, locksvc, and raftkvs in Go), spanning 175 to 5,360 source lines. Each task lists the mandatory core actions that must be modeled and the implementation details that should be excluded, so granularity is fixed by the task rather than chosen by the agent.

## Domains

Formal specification of concurrent and distributed systems: operating-system synchronization primitives, consensus implementations, replication, leader election, and distributed data structures.

## Evaluation

Four metrics, applied in a fixed order in which each stage gates the next:

- **Syntax correctness.** The TLA+ SANY Syntactic Analyzer checks the whole model, and a per-action pass encapsulates each action separately for partial scoring; the two are weighted equally, so a model that fails the full check while passing every per-action check earns 50%. Only models scoring 100% are evaluated on the later metrics.
- **Runtime correctness.** TLC performs bounded model checking and simulation with invariant checking switched off, and the score is the number of covered actions that raise no runtime error divided by the total number of actions in the model. Only models free of runtime errors are evaluated for conformance and invariant correctness.
- **Conformance to system implementation.** Trace validation replays execution traces collected from instrumented system code against the model's state space, and the score is the fraction of instrumented code actions covered without a conformance error.
- **Invariant correctness.** Each system-specific safety and liveness invariant is model-checked in a separate TLC run, and the score is the fraction of invariants that hold across the explored state space.
- **Reported (Table 3).** On the Asterinas Spinlock every LLM reaches 100.00% syntax and runtime under the basic modeling agent, with conformance 100.00% for Claude-Sonnet-4 and 80.00% for GPT-5, Gemini-2.5-Pro, and DeepSeek-R1. On Etcd Raft only Claude-Sonnet-4 clears the syntax gate under that agent, then reaches 25.00% runtime, 7.69% conformance, and 69.23% invariant correctness; the code translation agent with Claude-Sonnet-4 reaches 66.67%, 15.38%, and 92.31%. Among invariants, 8.3% of safety properties and 41.9% of liveness properties are violated.

## Typical Duration

Each agent is run five times per artifact and the best output model is evaluated, with up to three feedback-loop iterations allowed when a generated model fails compilation or raises runtime errors. Not stated: no per-task wall-clock, step, or token budget is given.

## Main Contribution

A benchmark for evaluating AI on formally modeling real-world concurrent and distributed systems in TLA+, with four quality metrics — syntax, runtime, conformance, and invariant correctness — that can be checked automatically without human or LLM judgement.

## Key Design Ideas

- Real system artifacts as task sources — production code from Etcd, Redis, Xline, ZooKeeper, and the Asterinas OS rather than synthetic programs or logic puzzles.
- A gated metric chain in which syntax gates runtime and runtime gates both conformance and invariant correctness, so a model that cannot execute is never scored on behavior.
- Partial scoring inside every metric, normalized to percentages, including a per-action syntax analysis that separates a wholly malformed model from one carrying a single bad action.
- Conformance measured by trace validation against logs from instrumented system code, grounding the score in the implementation rather than in a human-written reference specification.

## Strengths

- Machine-checked metrics keep scoring reproducible and independent of any judge model, a choice the authors make after finding LLM-as-a-judge unreliable and difficult to interpret.
- The gating order yields a diagnostic profile rather than a single score, separating syntactic competence from the ability to reason about system behavior.
- Grounding conformance in execution traces of the real implementation avoids comparison against reference specifications, which rarely exist for real-world systems.

## Limitations

- Repository note: Eleven artifacts is a small task pool, and three of them are PGo-synthesized rather than human-written system code — the paper reports that agents also do poorly there, so part of the measured difficulty tracks machine-generated code style rather than system complexity.
- Repository note: LLM-as-a-judge is excluded from scoring, but LLMs remain inside the pipeline — mapping model elements to system-log elements for trace validation, and concretizing invariant templates — so the metrics are not entirely LLM-free; the authors check this with gold models on two of the eleven systems.

## Related Works

- [TRACE](./trace.md) — Also scores a multi-dimensional quality profile instead of a single pass/fail, but composes accuracy, efficiency, and reasoning quality over a deep-research trajectory rather than checker verdicts over a generated formal model.
- [Traxgen](./traxgen.md) — Also removes the LLM from the evaluation loop, but at the ground-truth generation step rather than at the scoring step, which SysMoBench closes off by making every metric machine-checkable.
- [Enconda-bench](./enconda-bench.md) — Also decomposes one task into four graded stages, but along the agent subprocesses of planning, diagnosis, repair, and execution rather than gated correctness properties of the produced artifact.
