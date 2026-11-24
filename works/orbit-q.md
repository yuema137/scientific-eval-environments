# ORBIT-Q (2026)

> **English** | [简体中文](../zh/works/orbit-q.md)

> **First appeared:** 2026-07-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.03105)

## Overview

ORBIT-Q evaluates coding agents on research-level quantum programming, where a script that runs is not enough: the result must be physically correct, use the required framework's native and differentiable features, and run fast enough. It varies two things separately. On one axis the framework is fixed (TensorCircuit-NG) and the agent-model pair changes; on the other the agent is fixed (Codex with GPT-5.5) and the quantum framework changes. A solution counts only after functional tests, static policy checks, an LLM source audit, and expert review all accept it.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities


- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** [ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming](https://arxiv.org/abs/2607.03105), Shi-Xin Zhang and Yu-Qin Chen, 2026 preprint.
- **Full text:** <https://arxiv.org/html/2607.03105v1>
- **Code:** <https://github.com/sxzgroup/ORBIT-Q> (Apache-2.0, Harbor-based)
- **Venue:** arXiv preprint (quant-ph), 2026

## Summary

Each of 12 framework-neutral tasks is turned into a framework-specific run by appending a framework prompt, choosing an execution image, and applying a verifier policy. The agent has 30 minutes to write a `run_solution(config)` implementation. The verifier then runs numerical tests, rejects solutions that exceed 200 non-empty, non-comment Python lines or that import forbidden libraries or tamper with tests, asks GPT-5.5 to audit the source for framework bypasses (for example a hand-written NumPy/JAX simulator), and sends borderline cases to an expert. Passed solutions are timed against an expert TensorCircuit-NG reference. On TensorCircuit-NG, Codex with GPT-5.5 passes 10 of 12 tasks with a geometric-mean slowdown of about 2.2× versus the expert reference; no configuration matches the reference on both pass rate and runtime.

## Tasks

12 tasks condensed from research scenarios in variational and differentiable quantum workflows. Examples named in the paper: MPS input with variational refinement (Task 1), post-selected cooling with success-rate tracking (Task 3), trainable Kraus-channel calibration (Task 4), non-unitary imaginary-time evolution (Task 5), measurement-feedback ground-state optimization (Task 7), sampling from a 7 × 7 two-dimensional circuit (Task 8), local-observable optimization in a 512-qubit shallow circuit (Task 9), and spin-1 Haldane-chain state preparation with string-order verification (Task 11). Tasks are packaged as containerized Harbor tasks.

Frameworks compared: TensorCircuit-NG (TC), PennyLane, TorchQuantum, and MindQuantum. Qiskit, Cirq, and TensorFlow Quantum were excluded because their standard workflows lack the end-to-end automatic differentiation the tasks require.

## Domains

Quantum physics and quantum computing: quantum circuit simulation, variational algorithms, open-system (Kraus-channel) modeling, tensor-network state input, and many-body ground-state and state-preparation problems.

## Evaluation

- **Tier 1, functional verification:** numerical correctness against the task evaluator, plus static policy checks (line-count limit, required and forbidden framework imports, test or reward manipulation). Per-task numerical tolerances are TODO(reference).
- **Tier 2, LLM semantic audit:** GPT-5.5 reads the source and returns structured fields such as `uses_required_framework` and `raw_numpy_jax_quantum_simulator_bypass`, checking framework use and fidelity to the stated problem.
- **Tier 3, expert review:** resolves ambiguous framework-fidelity cases.
- **Artifact runtime:** submitted runtime divided by the expert TC reference runtime on the same task; geometric means are taken over passed, timed tasks. `run_solution(config)` must finish within 300 s; runtime score is lost after 180 s and is zero at 300 s.
- **Framework axis (Codex, GPT-5.5):** TC 10/12, PennyLane 8/12, TorchQuantum 4/12, MindQuantum 4/12. Geometric-mean slowdown ranges from about 2.2× (TC) to about 10.1× (MindQuantum); individual tasks exceed 40×.
- **Agent axis (TC):** Codex GPT-5.5 10/12, Claude Code with Opus-4.8 9/12, Sonnet-4.6 7/12, GLM-5.2 6/12.
- **Failure attribution (TC agent axis):** GPT-5.5 failures were 1 missing artifact and 1 framework bypass; Opus-4.8 had 1 timeout/OOM and 2 safety refusals; GLM-5.2 had 3 missing artifacts, 1 runtime/API exception, and 2 problem mismatches; Sonnet-4.6 had 2 missing artifacts, 1 runtime/API exception, 1 framework bypass, and 1 problem mismatch.
- **Agent-side resources (Table S2):** on TC, total tokens over 12 tasks range from 12,203,758 (Opus-4.8) to 21,268,795 (Sonnet-4.6), and cost per pass from $1.80 (GPT-5.5) to $2.16 (GLM-5.2). Across frameworks under Codex GPT-5.5, cost per pass rises from $1.80 (TC) to $7.26 (MindQuantum). A TC-specific performance-checklist prompt kept 10/12 passes and about 2.2× slowdown while cutting tokens from 14,241,691 to 8,205,577 and cost from $17.99 to $13.29. Agent-side costs exclude the verifier's audit usage.

## Typical Duration

30 minutes of agent solve time per task (1800 s), 1200 s verifier time, and up to 300 s for the submitted solution to run. Total agent wall time over 12 tasks ranges from about 1.5 h (GPT-5.5 with checklist) to about 3.8 h (GLM-5.2, Sonnet-4.6). The number of runs per configuration is not stated.

## Main Contribution

A dual-axis design that separates agent capability from framework usability in scientific quantum programming, scored with a multi-tier verifier that rejects numerically correct code that bypasses the required framework, and with runtime measured against expert reference implementations.

## Key Design Ideas

- Framework-neutral task statements made framework-specific only at run time (prompt, image, verifier policy), so the same task can be compared across frameworks.
- Validity requires functional, static-policy, semantic-audit, and human-review acceptance together.
- Efficiency is reported relative to expert TC references, not only as pass/fail.
- Agent-side tokens, wall time, and cost are reported per configuration alongside artifact runtime.

## Strengths

- Failure attribution distinguishes missing artifacts, framework bypasses, problem mismatches, timeouts, and safety refusals instead of a single failure count.
- The framework axis holds the agent constant, so differences across frameworks reflect agent-mediated usability under one agent.
- Code and tasks are released.

## Limitations

- The authors state that the semantic audit depends on GPT-5.5 and on human adjudication for borderline cases.
- The framework comparison measures agent-mediated usability and performance, not the best possible expert implementation in each framework; expert references exist only for TC.
- 12 tasks is a finite sample.
- The authors develop TensorCircuit-NG, one of the evaluated frameworks, and declare this as a competing interest.
- Some failures reflect deployed-agent safety classifiers rather than model capability.
- Repository note: each configuration is reported as one set of 12 task outcomes; the paper does not state repeated runs, so run-to-run variance is not reported.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also evaluates agents on containerized scientific-computing tasks with programmatic verification, across several natural-science domains rather than one programming area.
- [ScienceAgentBench](./scienceagentbench.md) — Also scores agent-written scientific code by execution, without a framework-fidelity audit or framework axis.
