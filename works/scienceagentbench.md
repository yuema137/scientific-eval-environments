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

102 tasks curated from 44 peer-reviewed publications in four disciplines — Bioinformatics, Computational Chemistry, Geographical Information Science, and Psychology & Cognitive Neuroscience. Per-discipline counts (from the authors' released dataset): Bioinformatics 27, Computational Chemistry 20, Geographical Information Science 27, Psychology & Cognitive Science 28. Each task's target output is unified to a self-contained Python program file.

## Domains

Data-driven scientific discovery across four disciplines: Bioinformatics, Computational Chemistry, Geographical Information Science, and Psychology & Cognitive Neuroscience.

## Evaluation

Each generated standalone program is scored on four metrics:

- **Valid Execution Rate (VER)** — whether the program runs without error and saves its output under the correct filename (binary).
- **Success Rate (SR)** — whether the output meets task-specific success criteria (e.g., "≥ 0.77 ROC-AUC on the test set", prediction–answer matches, visualization quality), implemented as a hand-written executable checker per task; SR is conditioned on execution (0 if the program errors or mis-saves). Figure outputs are judged by GPT-4o against the ground truth, averaged over 3 samples.
- **CodeBERTScore (CBS)** — F1 over contextual token embeddings measuring similarity to the annotated reference program (set to 1.0 when SR = 1).
- **API Cost** — average USD to complete one task.

A separate expert **rubric** (five stages: Data Loading, Data Processing, Modeling/Visualization, Output Formatting, Output Saving; normalized 0–100) is used for human evaluation as a complement to the stricter outcome metrics, but is not part of the automatic SR. Tasks also undergo multiple rounds of manual validation, with two strategies to mitigate data contamination.

Reported (three attempts per task): the best agent (Claude-3.5-Sonnet + Self-Debug) solves 32.4% independently and 34.3% with expert-provided knowledge; o1-preview + Self-Debug reaches 42.2% (at > 10× the API cost of the cheaper models). Self-Debug solves 10.8 points more than OpenHands CodeAct (21.6 → 32.4 SR) at 17× lower cost ($0.958 → $0.057 per task).

## Typical Duration

Not reported as wall-clock; the paper reports per-task API cost instead — from ~$0.017 (Claude-3.5 direct prompting) to ~$1.09 (GPT-4o OpenHands CodeAct) per task, with o1-preview self-debug at $0.64–0.71.

## Main Contribution

A rigorously validated benchmark for data-driven scientific discovery that assesses agents on individual scientific-workflow tasks — with expert-validated tasks drawn from real publications and a unified Python-program output target — rather than assuming end-to-end automation.

## Key Design Ideas

- Tasks extracted from real peer-reviewed publications and validated by subject matter experts for scientific authenticity.
- Unified target output (a self-contained Python program) makes heterogeneous scientific tasks comparably gradable.
- Four automatic metrics — VER, SR (via per-task executable criteria), CodeBERTScore, and API cost — complemented by a five-stage expert rubric for human evaluation.
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
