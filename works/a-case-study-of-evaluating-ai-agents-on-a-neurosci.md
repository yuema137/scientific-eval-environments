# A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline (2026)

> **English** | [简体中文](../zh/works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)

> **First appeared:** 2026-06-05 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.07718)

## Overview

An empirical case study that evaluates general-purpose coding agents on a real fly-optogenetics "data-to-discovery" pipeline, assessing whether agents can automate the software-engineering stages scientists normally build by hand, using evaluation criteria grounded in domain-expert standards.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.07718
- **Code:** https://github.com/kaihorstmann/neuro-d2d-eval
- **Venue:** Third Conference on Language Modeling (COLM 2026)

## Summary

The work studies whether coding agents can build the computational stages of a neuroscience research pipeline that analyzes fly walking behavior under optogenetic perturbation. Agents must produce correct, robust code on tasks and datasets substantially larger than those in existing agent benchmarks, judged against expert human annotations and trusted legacy codebases. The study finds that agents can solve several individual pipeline stages but cannot yet compose them into a correct end-to-end discovery, and it identifies failure modes — reasoning without a predefined success criterion, weak visual self-evaluation, computational resource management, and generalization to held-out data — that are largely absent from prior benchmarks. The authors distill principles for constructing scientific tasks and rigorous evaluation criteria for open-ended problems.

## Tasks

The pipeline is decomposed into seven single-stage tasks, in order: Body Tracking, Registration, Keypoint Tracking, Behavior Feature Computation, Walking Behavior Classification, Gait Segmentation, and Statistical Comparisons. In addition to the seven single-stage tasks, the study runs end-to-end pipeline variants with differing levels of prompt guidance (a minimal and a maximal prompt); the released harness comprises nine computational tasks in total. Each agent–task pair was run for 3 trials. The tasks and evaluation harness are released and stated to be compatible with the Harbor agent-evaluation framework.

## Domains

Neuroscience — analysis of *Drosophila* (fruit fly) walking behavior under optogenetic perturbation, spanning video-based body/keypoint tracking, behavior classification, gait analysis, and statistical comparison across genetic driver (GAL4) lines and a genetic control group.

## Evaluation

Each stage carries success criteria grounded in domain-expert standards; agent solutions are compared against both expert human annotations and trusted legacy (scientist-authored) codebases. For the statistical-comparison stage, outputs are assessed using Mann–Whitney U tests comparing each experimental neuron type against a genetic control. Evaluation is run per stage in the single-stage setting and independently for the constituent stages in the end-to-end setting. Across the reported runs, 73% of agent–task pairs yielded unanimous pass/fail verdicts across the 3 trials. Repository note: some finer-grained per-stage pass counts reported in the paper could not be transcribed with confidence from the primary source and are left as TODO(reference).

## Typical Duration

The task prompt template includes a stated time limit for task completion, and the paper reports per-task token usage and runtimes in an appendix; exact budgets are not transcribed here. TODO(reference).

## Main Contribution

An empirical evaluation of general-purpose coding agents on a realistic, expert-grade neuroscience data-to-discovery pipeline — using tasks and datasets larger than existing benchmarks and criteria grounded in domain-expert standards — showing that stage-level automation is tractable while correct end-to-end discovery is not, and distilling principles for constructing scientific tasks and rigorous evaluation criteria for open-ended problems.

## Key Design Ideas

- Decompose a genuine scientific pipeline into ordered stages, each with an expert-defined success criterion, enabling both stage-level and end-to-end evaluation.
- Ground correctness in expert human annotations and trusted legacy codebases rather than agent self-report.
- Use datasets substantially larger than prior agent benchmarks (~47 GB of fly-behavior data released via HuggingFace) to expose computational resource management and held-out-data generalization as evaluation dimensions.
- Evaluate multiple agent scaffolds and backing models: Claude Code (claude-opus-4-6), Codex (gpt-5.4), and Terminus-2 (with claude-opus-4-6 and with gpt-5.4).
- Analyze agents' code-iteration trajectories to characterize *how* they succeed or fail, including attempts at visual inspection of intermediate outputs for self-evaluation.

## Strengths

- Tasks and datasets are drawn from a real research pipeline and are larger than those in existing agent benchmarks, with criteria set by domain experts.
- Separately measures single-stage and end-to-end performance, isolating composition/integration as a distinct failure mode.
- Surfaces evaluation dimensions largely absent from prior benchmarks: reasoning without a predefined success criterion, visual self-evaluation, computational resource management, and generalization to held-out data.
- Releases the tasks, evaluation harness, and dataset publicly.

## Limitations

- A single-pipeline case study in one subfield (fly-behavior neuroscience); generalization to other scientific pipelines is not established by the study itself.
- Reported per-stage pass rates depend on a small number of trials (3 per agent–task pair), and some detailed per-stage numbers are not transcribed here (TODO(reference)).
- Repository note: the specific neurobiological hypothesis (which neuron types / how many GAL4 lines) is described operationally rather than as a stated scientific question in the accessible text; exact counts are left as TODO(reference).

## Related Works

- [BixBench](./bixbench.md) — another data-analysis / discovery-style agent evaluation in the life sciences.
- [ScienceAgentBench](./scienceagentbench.md) — evaluates coding agents on data-driven scientific tasks with expert-grounded criteria.
