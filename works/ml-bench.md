# ML-Bench (2023)

> **English** | [简体中文](../zh/works/ml-bench.md)

## Overview

ML-Bench evaluates LLMs and agents on machine-learning tasks at repository-level code: 9,641 examples across 18 GitHub repositories, split into ML-LLM-Bench (generate code from a task description in repository context) and ML-Agent-Bench (execute tasks end to end autonomously in a Linux sandbox).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.09835>
- **Code:** <https://github.com/gersteinlab/ML-bench>
- **Project:** <https://ml-bench.github.io/>
- **Venue:** arXiv preprint (cs.CL), 2023

## Summary

ML-Bench measures whether models can use real ML repositories, not just write isolated snippets: 9,641 examples across 18 GitHub repositories, in two tracks. ML-LLM-Bench is static text-to-code — given a task description and repository context (with retrieval or oracle configurations), the LLM generates runnable code, scored by Pass@5. ML-Agent-Bench is agentic — an autonomous agent executes the task end to end in a Linux sandbox (OpenDevin integration), scored by success rate. GPT-4o surpasses 50% Pass@5 on the LLM track and reaches 76.47% success on the agent track.

## Tasks

9,641 repository-level ML tasks across 18 GitHub repos, in two tracks: ML-LLM-Bench (static text-to-code with repo context) and ML-Agent-Bench (autonomous end-to-end execution in a Linux sandbox).

## Domains

AI & Machine Learning Research — repository-level ML code: using real ML codebases to accomplish tasks.

## Evaluation

- Pass@5 for the LLM code-generation track; success rate for the agentic execution track.
- **Reported.** GPT-4o: Pass@5 above 50% on ML-LLM-Bench and 76.47% success on ML-Agent-Bench.

## Typical Duration

Single generations (LLM track) or multi-step sandboxed execution episodes (agent track).

## Main Contribution

Bringing repository-level context to ML-task evaluation — separating text-to-code competence from autonomous end-to-end execution over the same real codebases.

## Key Design Ideas

- Repository context tests whether models can navigate and use real ML code, not just recall APIs.
- The LLM/agent two-track split isolates code generation from autonomous execution.
- Retrieval and oracle configurations vary how much context the model is given.

## Strengths

- Large (9,641 examples) with a two-track design over authentic ML repositories.
- Public repo and project site with both tracks released.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is stated in arXiv metadata.

## Related Works

- [ResearchCodeBench](./researchcodebench.md) — Also ML-implementation-from-description, on translating recent paper contributions to code.
- [SUPER](./super.md) — Also executing tasks from research repositories, focused on setup and reproduction.
- [MLAgentBench](./mlagentbench.md) — Also agentic ML tasks, on improve-the-metric experimentation.
