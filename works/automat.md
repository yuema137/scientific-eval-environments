# AutoMat (2026)

## Overview

AutoMat is a benchmark that evaluates whether LLM-based coding agents can reproduce claims from computational materials science papers end-to-end. It comprises 85 expert-curated claims executed in a resource-controlled environment representative of modern HPC workflows, on which the best-performing agent setting reaches a 54.1% success rate.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.00803>
- **Project:** <https://jhu-clsp.github.io/AutoMat>
- **Code:** <https://github.com/JHU-CLSP/AutoMat>

## Summary

The authors observe that coding agents perform strongly on software engineering benchmarks, but that it is unclear whether this success transfers to computational scientific workflows, which require navigating domain-specific procedures and interpreting results in the context of scientific claims. AutoMat packages 85 claims curated by subject matter experts from computational materials science papers into runnable tasks: the agent must recover the computational procedure, execute it with specialized toolchains, and produce evidence supporting or undermining the claim. Across five agent settings, the strongest configuration, Claude Code with Claude Opus 4.6, reaches a mean reproducibility score of 3.52 and a 54.1% success rate, and all systems show near-zero success when workflows must be reconstructed from paper text alone.

## Tasks

85 claim-reproduction tasks spanning three types that differ in how much procedural recovery is required: from-paper reproduction (generic tools and public resources described in the source paper), from-artifact reproduction (custom codebases, pretrained models, or datasets essential to the reproduction path), and from-artifact interpretation (post-hoc analysis of provided simulation outputs). Subject matter experts (SMEs) — senior Ph.D. students and postdoctoral researchers who have published at least one first-author peer-reviewed materials science journal paper — selected claims centered on numerical results that serve as critical evidence for each paper's conclusions, annotating them with provenance, expected outcome, and a step-by-step reproduction procedure hidden from the agent; each task packages the claim text, source paper, a metadata file, and optional artifacts.

## Domains

Computational materials science, spanning Statistical/Machine Learning methods, Density Functional Theory, Molecular Dynamics, and Discrete Dislocation Dynamics.

## Evaluation

- **Overall reproducibility score.** A separate LLM-based evaluator agent — given the SME-annotated ground-truth reproduction steps, reference code when available, the claim, the paper, and the full execution trace — assigns a five-point score from 5 (fully reproduced) to 1 (failed); unlike a fixed-prompt judge, it can navigate the artifact directory, inspect files, and use tools.
- **Success rate.** The fraction of runs scoring at least 4, with dimension-level scores for methodological fidelity, execution competence, result accuracy, completeness, and scientific rigor.
- **Judge calibration.** On a stratified subset of 40 runs scored blind by qualified SMEs, the evaluator reaches a quadratic-weighted kappa of 0.69 and a within-1 difference accuracy of 0.80.
- **Reported.** Claude Code with Claude Opus 4.6 is the strongest of five settings at a 3.52 mean score and 54.1% success rate, while Codex CLI with GPT-5.4 is the weakest at 2.44 and 23.5%; from-paper reproduction is by far the hardest type, with mean scores of 1.5–2.2 and near-zero success across all systems, versus mean scores of 3.1–4.1 and success rates between 39% and 77% for from-artifact reproduction.

## Typical Duration

The paper states no per-task step or token budget; the experimental setup and runtime appendix specify only hardware-level limits. Jobs run on Slurm-managed nodes capped at 96 CPU cores, with an NVIDIA A100 GPU for Statistical/Machine Learning claims, and a maximum wall-clock timeout of 72 hours unless otherwise noted.

## Main Contribution

A benchmark of 85 SME-curated computational materials science claims for evaluating end-to-end scientific reproducibility with LLM agents, serving both as a reproducibility benchmark and as a diagnostic for where agentic systems fail in AI-for-science settings.

## Key Design Ideas

- Claim-level task unit: each task packages a claim, its source paper, a metadata file, and optional artifacts, with the SME-written reproduction procedure reserved for evaluation and hidden from the agent.
- Three reproduction types graded by how much of the procedure must be recovered, crossed with five verification categories: scalar metric match, comparative/ordering, structural/qualitative, range/bound verification, and figure reproduction.
- Execution in a resource-controlled environment representative of modern HPC workflows, with a preinstalled simulation stack including Quantum ESPRESSO and LAMMPS.
- An evaluator that is itself an agent: it gathers evidence from the produced artifact directory and execution trace with tools, and is calibrated against blinded SME scoring on the same five-point scale.

## Strengths

- Claims come from real papers and are curated by researchers with first-author materials science publications, targeting numerical results that serve as critical evidence for each paper's conclusions.
- The three task types separate failure sources: recovering an underspecified workflow from text, adapting provided artifacts, and judging whether existing outputs actually support a claim.
- Full trajectories — logs, commands, intermediate outputs, and reports — are preserved, enabling the failure-mode analysis that identifies procedural incompleteness and methodological deviation as the dominant errors.

## Limitations

- Repository note: The authors state that coverage is 85 claims from a single (albeit broad) domain, that the claim-type distribution reflects the practical realities of expert data collection, and that the benchmark contains only claims already identified as reproducible, so it does not test whether agents can recognize non-reproducible claims.
- Repository note: Scoring rests on an LLM evaluator agent that the authors describe as a scalable approximation to expert assessment rather than a replacement; exact scores for settings other than the best and worst configurations appear only in figures, not in the text.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also curates tasks from peer-reviewed publications with subject-matter-expert validation, but unifies every task into a self-contained Python program scored by program- and output-level metrics rather than end-to-end claim reproduction judged by an artifact-grounded LLM evaluator.
- [Aviary](./aviary.md) — Also targets multi-step scientific tasks for language agents, but provides gymnasium environments for training agents on molecular cloning, scientific literature research, and protein stability engineering rather than a fixed set of expert-curated reproduction claims.
