# FIRE-Bench (2026)

> **English** | [简体中文](../zh/works/fire-bench.md)

## Overview

FIRE-Bench (Full-cycle Insight Rediscovery Evaluation) is a benchmark that asks agents to rediscover established, verifiable findings from recent, high-impact machine learning research, given only a high-level research question from the published study. It comprises 40 fully executed tasks together with 60 additional papers released for community evaluation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.02905>
- **Project:** <https://firebench.github.io>
- **Code:** <https://github.com/maitrix-org/FIRE-Bench>
- **Venue:** ICML 2026

## Summary

FIRE-Bench argues that because novel findings demand costly real-world validation, existing benchmarks fall back on LLM-as-judge scoring of generated papers or single leaderboard metrics, both coarse proxies for scientific reasoning. It instead asks agents to rediscover established findings: given only a high-level research question from a published study, an agent must independently design experiments, run them, and draw evidence-backed conclusions, scored against the study's documented findings. Across state-of-the-art coding agents with frontier backbones, even the strongest reaches limited rediscovery success (below 50 F1), with high run-to-run variance and recurring failures in experimental design, execution, and evidence-based reasoning.

## Tasks

40 fully executed tasks — a core set of 30 built one per paper from empirical studies of LLM behavior published at ICLR, ICML, and NeurIPS in 2024 and 2025, plus a 10-task cross-domain extension (5 papers from computer vision and vision-language modeling, 5 from neural network analysis) — together with a parsed pool of 60 additional papers released for community evaluation. Source papers must satisfy three criteria — open inputs (publicly available datasets and models only), compute-light execution (runnable within 24 hours on an 80GB A100 GPU), and non-trivial, verifiable insights — and final candidates are manually reviewed by two authors. Each paper is parsed by gpt-5 Pro into a research-problem tree of root research question, intermediate subproblems, and leaf experiments grounded in reported figures or tables; the task prompt is the parent node of a target leaf, giving the agent a research question while withholding the original experimental design.

## Domains

Machine learning research: LLM behavior analysis in the executed core; computer vision, vision-language modeling, and neural network analysis in the extension; code generation, RAG, agents and tool use, safety and alignment, and multilingual modeling in the community pool.

## Evaluation

- **Claim-level precision, recall, and F1.** Each agent's final conclusion and the ground-truth text are decomposed into sets of atomic, verifiable claims following RAGChecker; a semantic-entailment classifier matches them, counting generated claims unsupported by ground truth as false positives and unmatched ground-truth claims as false negatives.
- **Judge reliability.** The same judge model (gpt-5.2) is used for all agents; human validation on 33% of reference instances yields precision 0.95, recall 0.86, and F1 0.89.
- **Diagnostic error framework.** Failures are attributed to four research-workflow stages — Research Planning, Implementation, Experimental Execution, and Conclusion Formation — through 16 error categories.
- **Reported.** On the core 30-task set, Claude Code (Sonnet-4) reaches F1 46.7±23.4, Codex (gpt-5-medium) 41.9±25.4, OpenHands (gpt-5) 37.9±23.0, and OpenHands (o4-mini) 31.9±17.6; failures are dominated by Research Planning and Conclusion Formation, and Codex attains its score at $2.21 in total API cost versus $12.67 for Claude Code.

## Typical Duration

No hard runtime limit is imposed, and most runs complete within one hour; each task-agent pair is executed three times, with mean and standard deviation reported. No per-task step or token budget is stated; tasks are filtered at construction to run within 24 hours on an 80GB A100 GPU, and agents execute in a CLI sandbox on a node with eight such GPUs.

## Main Contribution

An evaluation paradigm for research agents combining full-cycle execution, insight-driven evaluation, grounded reference-based scoring, and methodological exploration, with the rediscovery of published, verified findings as the scoring target.

## Key Design Ideas

- Research-problem tree abstraction parsing each paper into a root research question, intermediate subproblems, and leaf experiments grounded in reported figures or tables, extracted automatically by gpt-5 Pro at temperature 0.
- Constrained rediscovery prompts built from the parent node of a target leaf, withholding the original design so the task shifts from direct replication toward exploration.
- Claim-centric scoring following RAGChecker, with a single fixed gpt-5.2 extractor and entailment judge applied to every agent.
- Living-benchmark release with versioned additions, a public leaderboard, a community submission form, and the 60-paper parsed pool beyond the 40 executed tasks.

## Strengths

- Ground truth is anchored in peer-reviewed published findings rather than free-form LLM judgment of novel outputs, making rediscovery success objectively checkable.
- Three runs per task-agent pair with reported standard deviations expose run-to-run variance directly.
- Contamination analysis stratified by task difficulty and model knowledge cutoff finds no strong evidence of systematic contamination.

## Limitations

- Repository note: The executed core covers only empirical LLM-analysis papers, and the compute-light filter caps reference experiments at 24 hours on a single 80GB A100 GPU, so rediscovery outside recent compute-light machine-learning research is untested.
- Repository note: Claim extraction and entailment judging both run on a single fixed model (gpt-5.2), so all scores inherit that judge's error profile; the paper's own human validation places the protocol at F1 0.89.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also builds tasks from peer-reviewed publications, but targets one self-contained Python program per task rather than a full research cycle from question to evidence-backed conclusion.
- [Aviary](./aviary.md) — Also evaluates language agents on scientific tasks, but through interactive gymnasium environments with terminal rewards rather than open-ended rediscovery of published findings.