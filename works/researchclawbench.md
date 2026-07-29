# ResearchClawBench (2026)

> **English** | [简体中文](../zh/works/researchclawbench.md)

## Overview

ResearchClawBench is a benchmark for end-to-end autonomous scientific research in which agents must re-discover the findings of a hidden published paper from a task description, related literature, and raw data. It comprises 40 expert-curated tasks across 10 scientific domains, scored against weighted multimodal rubrics anchored to the target paper's artifacts.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.07591>
- **Project:** <https://internscience.github.io/ResearchClawBench-Home/>
- **Code:** <https://github.com/InternScience/ResearchClawBench>

## Summary

ResearchClawBench addresses the difficulty of verifying the end-to-end autonomous research capability of AI coding agents. Each task grounds a real published paper, supplying related literature and raw data while hiding the paper itself, and expert-curated multimodal rubrics decompose the target's scientific artifacts into weighted criteria so that target-paper-level re-discovery can be scored while leaving room for new discovery. Across seven autonomous research agents evaluated under a unified protocol and seventeen native LLMs run through the lightweight ResearchHarness, the strongest agent, Claude Code, averages 21.5, the strongest harness LLM, Claude-Opus-4.7, averages 20.7, and the LLM frontier mean is only 26.5.

## Tasks

40 tasks, each grounded in a real published paper and packaged with a task description, related literature, and raw data; the target paper stays hidden during evaluation. Experts construct tasks in a six-step pipeline: screening papers with clear questions, accessible data, and high research value; rewriting the core question into an executable task description; organizing related literature and raw data; building rubrics from key target-paper artifacts; packaging materials into standardized tasks; and cross-checking to fix issues and filter unsuitable samples.

## Domains

10 scientific domains: Astronomy, Chemistry, Earth, Energy, Information, Life, Material, Math, Neuroscience, and Physics.

## Evaluation

- **Reference-Anchored Discovery Score (RADS).** A rubric-based score on a 0–100 scale where 50 denotes reference-level scientific evidence; scores below 50 indicate insufficient discovery potential, and scores above 50 indicate reference-surpassing evidence.
- **Expert-curated multimodal rubrics.** Each rubric item is built around a concrete scientific artifact in the hidden target paper, is typed as text or image, and specifies criteria, technical keywords for the judge to verify, and a weight reflecting the item's importance; GPT-5.1 scores the final report against the rubrics.
- **Additional report dimensions.** Beyond the rubrics, reports are evaluated along four additional dimensions: Comprehensiveness, Depth, Instruction Following, and Professionalism.
- **Error taxonomy.** Six failure types: Experiment Design Mismatch, Evidence Mismatch, Scientific Core Missing, Goal Misalignment, Reliability / Reporting Failure, and Execution Failure; failures concentrate in the first three.
- **Reported.** The strongest autonomous agent, Claude Code (Claude-Opus-4.6), averages 21.5; the strongest ResearchHarness LLM, Claude-Opus-4.7, averages 20.7; the LLM frontier mean is 26.5.

## Typical Duration

No per-task step, token, or wall-clock cap is stated; the paper characterizes resource use through mean task cost and runtime plotted against mean rubric score, noting that Claude Code combines a high score with high cost and long runtime. ResearchHarness applies automatic context compaction for long multi-step tasks, triggered by default at 128k tokens.

## Main Contribution

A paper-grounded benchmark for end-to-end autonomous scientific research whose Reference-Anchored Discovery Score measures target-paper-level re-discovery against expert-curated weighted rubrics while leaving room for new discovery.

## Key Design Ideas

- Tasks grounded in real published papers that supply related literature and raw data while the target paper stays hidden during evaluation.
- Multimodal rubrics whose text- and image-type items anchor concrete target-paper artifacts, each carrying criteria, technical keywords, and an importance weight.
- A reference anchor at 50 on the 0–100 RADS scale, separating insufficient discovery potential from reference-surpassing evidence.
- ResearchHarness, a lightweight ReAct-style harness with web, local-file, and execution tools plus automatic context compaction, letting native LLMs run the benchmark alongside full autonomous agents.

## Strengths

- Hiding the target paper while supplying its inputs turns published findings into concrete re-discovery targets instead of open-ended report prompts.
- A unified protocol spanning seven autonomous agents and seventeen harness-run LLMs enables direct comparison between agent scaffolds and native models on the same 40 tasks.
- The six-type error taxonomy locates failures — experiment design, evidence, and scientific core — rather than reporting only an aggregate score.

## Limitations

- Repository note: Rubric scoring hinges on a single proprietary judge, GPT-5.1, so score reproduction is tied to that model's availability and behavior.
- Repository note: Target papers are published works, and hiding them at evaluation time does not remove them from a model's pretraining corpus; the described curation pipeline screens for question clarity, data accessibility, and research value rather than publication recency.

## Related Works

- [NatureBench](./naturebench.md) — Also distills tasks from real published papers, but scores agents against each source paper's reported state of the art rather than judging full research reports with paper-anchored rubrics.
- [ScienceAgentBench](./scienceagentbench.md) — Also draws tasks from peer-reviewed publications, but scores generated standalone programs with execution-based metrics rather than judging end-to-end re-discovery of a hidden target paper.
- [AIRS-Bench](./airs-bench.md) — Also measures end-to-end research capability, but over 20 tasks sourced from state-of-the-art machine-learning papers rather than 40 hidden-target tasks across 10 scientific domains.
