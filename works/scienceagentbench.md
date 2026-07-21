# ScienceAgentBench (2024)

## Overview

ScienceAgentBench is a benchmark for evaluating language agents on individual tasks within data-driven scientific-discovery workflows. It extracts 102 tasks from 44 peer-reviewed publications across four disciplines, unifies every task's target output to a self-contained Python program, and scores generated programs, execution results, and costs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.05080>
- **Venue:** ICLR 2025

## Summary

ScienceAgentBench argues that agents should be rigorously assessed on individual tasks in a scientific workflow before claims of end-to-end automation of scientific discovery. To ensure scientific authenticity and real-world relevance, it extracts 102 tasks from 44 peer-reviewed publications in four disciplines and engages nine subject matter experts to validate them. Every task's target output is unified to a self-contained Python program file, and an array of metrics examines the generated programs, execution results, and costs. Each task undergoes multiple rounds of manual validation by annotators and subject matter experts, and the benchmark proposes two strategies to mitigate data-contamination concerns.

## Tasks

102 tasks extracted from 44 peer-reviewed publications across four scientific disciplines. Each task's target output is unified to a self-contained Python program file. Discipline names: TODO(reference) — not stated in the abstract.

## Domains

Data-driven scientific discovery across four disciplines (specific disciplines: TODO(reference)).

## Evaluation

- Target output unified to a self-contained Python program per task.
- An array of metrics examines the generated programs, execution results, and costs.
- Multiple rounds of manual validation by annotators and subject matter experts.
- Two strategies proposed to mitigate data-contamination concerns.
- Reported: with three attempts per task, the best-performing agent solves 32.4% of tasks independently and 34.3% with expert-provided knowledge. OpenAI o1-preview (direct prompting + self-debug) reaches 42.2%, at more than 10× the cost of the other LLMs.

## Typical Duration

TODO(reference): abstract does not state per-task duration or token budget.

## Main Contribution

A rigorously validated benchmark for data-driven scientific discovery that assesses agents on individual scientific-workflow tasks — with expert-validated tasks drawn from real publications and a unified Python-program output target — rather than assuming end-to-end automation.

## Key Design Ideas

- Tasks extracted from real peer-reviewed publications and validated by subject matter experts for scientific authenticity.
- Unified target output (a self-contained Python program) makes heterogeneous scientific tasks comparably gradable.
- Evaluation spans generated program, execution result, and cost rather than a single accuracy metric.
- Two explicit data-contamination-mitigation strategies.
- Evaluation across five open-weight and proprietary LLMs under three agent frameworks: direct prompting, OpenHands CodeAct, and self-debug.

## Strengths

- Publication-grounded, expert-validated tasks give ecological validity to scientific-discovery evaluation.
- Unified Python-program output enables execution-based, comparable grading across disciplines.
- Reports cost alongside accuracy, surfacing the inference-time-compute trade-off (o1-preview reaches 42.2% at >10× cost).
- Explicit data-contamination mitigation strengthens benchmark integrity.

## Limitations

- Repository note: Low best-agent solve rate (32.4% independently, 34.3% with expert knowledge) indicates the benchmark is far from saturated — a strength for headroom, but per-task diagnostic signal beyond pass/fail is not the benchmark's focus.
- Repository note: Scope is data-driven discovery expressed as Python programs; scientific tasks that are not reducible to a program artifact are out of scope.

## Related Works

- [NatureBench](./naturebench.md) — Also anchors scientific tasks to peer-reviewed publications, but scores by comparison against published SOTA rather than execution of a unified Python program.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also uses execution-based verification of scientific-computing workflows, via containerized pytest rather than a unified Python-program output.
- [AIRS-Bench](./airs-bench.md) — Also targets research-science tasks, but evaluates an end-to-end research lifecycle rather than individual workflow tasks.
