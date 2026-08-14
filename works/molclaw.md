# MolClaw (2026)

> **English** | [简体中文](../zh/works/molclaw.md)

## Overview

MolClaw is an autonomous agent for drug-molecule evaluation, screening, and optimization built on a three-tier hierarchical skill architecture, released together with **MolBench**, a benchmark of molecular screening, molecular optimization, and end-to-end discovery challenges spanning 8 to 50+ sequential tool calls.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.21937>
- **Venue:** arXiv preprint, April 2026 (v2 revised May 2026)

## Summary

Computational drug discovery requires orchestrating dozens of specialized tools across multi-step workflows, and the paper reports that current AI agents consistently underperform in these high-complexity settings. MolClaw unifies over 30 specialized domain resources behind a hierarchical skill architecture of 70 skills: tool-level skills standardize atomic operations, workflow-level skills compose them into validated pipelines with quality checks and reflection, and a discipline-level skill supplies the scientific principles that govern planning and verification across scenarios. The accompanying MolBench evaluation suite is organized into three tiers — screening, optimization, and end-to-end discovery — so that ad-hoc scripting competence can be separated from workflow-orchestration competence. Ablations reported by the authors show gains concentrate on tasks demanding structured workflows and vanish on tasks solvable by ad-hoc scripting, which they take as evidence that workflow orchestration is the primary capability bottleneck.

## Tasks

MolBench has three tiers:

- **MolBench-MS (molecular screening)** — three subtasks: property filtering (n = 50, constraint satisfaction over RDKit descriptors), binding-affinity comparison (n = 37, ranking molecule pairs by Ki values drawn from ACNet), and docking screening (n = 25, virtual screening scored by Hits@3). Screening items derive from a CARA ChEMBL subset and the ACNet database.
- **MolBench-MO (molecular optimization)** — two subtasks: functional-group modification (n = 39) and physicochemical property optimization toward QED, LogP, and LogS targets. Optimization items are adapted from ChemCoTBench with ill-defined entries removed. `TODO(reference)` — the item count for the property-optimization subtask is not stated in the sources consulted.
- **MolBench-E2E (end-to-end)** — three multi-phase discovery challenges requiring 8 to 50+ sequential tool invocations: coarse-grained conformational sampling with all-atom reconstruction; multi-round QED optimization (up to five rounds); and structure-guided lead optimization of Erlotinib (up to fifteen rounds).

## Domains

Chemistry and Medicine & Health — computational drug discovery: molecular property computation, binding-affinity reasoning, molecular docking and virtual screening, molecular editing and property optimization, and structure-guided lead optimization of a named drug molecule.

## Evaluation

Each tier has its own protocol:

- **MolBench-MS** — accuracy (%) for property filtering and for binding-affinity comparison; **Hits@3**, the average number of ground-truth active molecules appearing in the top three ranked results, for docking screening.
- **MolBench-MO** — operational accuracy for molecule editing; property deltas (Δ) and success rate (%) for property optimization.
- **MolBench-E2E** — task-specific weighted rubrics decomposing each challenge into criteria spanning correct tool selection and invocation sequence, scientific validity of intermediate reasoning, data integrity and parameter consistency across workflow steps, appropriate termination behavior, and completeness of output deliverables. `TODO(reference)` — the individual rubric weights and the identity of the rubric judge are not specified in the sources consulted.

Baselines span nine LLMs (GPT 5.2, Claude Sonnet 4.6, Gemini 3, DeepSeek v3.2, Kimi 2.5, GLM 5, Minimax 2.5, Qwen 3.5, Intern S1), the Biomni agent, and vanilla Claude Code and OpenClaw harnesses. Reported results for MolClaw on Claude Code include 81.1% binding-affinity accuracy (a 24.3 percentage-point gain over the non-MolClaw baseline, Fisher's exact P = 0.043), a docking hit count of 0.80 against 0.56 for Claude Code and 0.20 for OpenClaw, and a property-optimization delta of 1.724 at a 100% success rate.

## Typical Duration

MolBench-E2E challenges require 8 to 50+ sequential tool invocations per task, with the optimization challenges running up to five and up to fifteen rounds respectively. `TODO(reference)` — wall-clock time and token budgets per task are not reported in the sources consulted.

## Main Contribution

A hierarchical skill architecture that raises agent reliability on multi-tool drug-discovery workflows, paired with MolBench — a named, tiered evaluation suite for molecular screening, optimization, and end-to-end discovery — and an ablation-supported claim that workflow-orchestration competence, not chemical knowledge or scripting ability, is the primary bottleneck for AI-driven drug discovery.

## Key Design Ideas

- Three-tier skill hierarchy: tool-level skills standardize atomic operations, workflow-level skills compose them into validated pipelines with quality checks and reflection, and a discipline-level document supplies field-wide scientific principles for planning and verification.
- Fine-grained tool-level skill templates deliberately decomposed to limit context pollution when many skills are loaded.
- A benchmark tiering (screening → optimization → end-to-end) chosen so that ablations can distinguish tasks solvable by ad-hoc scripting from tasks requiring structured workflows.
- Rubric-based scoring for the end-to-end tier that credits process properties — invocation sequence, parameter consistency, termination behavior — not just final deliverables.
- Screening and optimization items sourced from existing curated chemistry resources (CARA/ChEMBL, ACNet, ChemCoTBench) rather than authored from scratch.
- A skill-crystallization procedure that converts novel execution traces into persistent reusable skills carrying an initially unvalidated confidence rating, promoted through successive verified executions.

## Strengths

- Ships a named benchmark with a documented scoring protocol alongside the agent, so the system's claims are checkable rather than demonstrated only on case studies (paper).
- The ablation design directly tests the paper's central claim: gains concentrate where structured workflows are required and vanish where they are not (paper).
- Broad baseline set spanning nine LLMs plus a domain agent (Biomni) and two general coding harnesses (paper).
- End-to-end tier evaluates genuinely long tool-call chains (8 to 50+ invocations) rather than single-shot chemistry QA (paper).

## Limitations

- The authors state all end-to-end results are purely computational; docking-score improvements do not guarantee experimental affinity gains, and wet-lab validation remains essential.
- The three E2E challenges are a limited sample; the authors name expansion to diverse target classes (GPCRs, ion channels, proteases) as necessary for generalizability.
- The authors report an attentional-bias failure: an AMES mutagenicity deterioration of +180% went unflagged in one challenge despite the agent tracking 13 ADMET endpoints.
- The skill layer is static — the authors note the agent does not learn from prior executions, citing a recurring "ethynyl fixation" as a failure to generalize from negative feedback — and the 70 skill documents required expert curation, so scalability depends on automated skill discovery the paper does not deliver.
- Context-window constraints may prevent simultaneous loading of all skill tiers, and convergence criteria for the optimization loops remain heuristic (paper).
- `Repository note:` no public repository or data URL for MolBench is given in the sources consulted, so the benchmark's reusability by third parties could not be verified.
- `Repository note:` the skill hierarchy is an *architecture* of the agent, not an evaluation decomposition — MolBench does not report a per-skill capability profile, so this card is not indexed under Skill Hierarchy.

## Related Works

- [ChemCoTBench](./chemcotbench.md) — source of MolBench-MO's molecular-optimization items, and the closest prior benchmark framing molecular transformation as modular chemical operations.
- [MolQuest](./molquest.md) — another agentic, multi-turn chemistry benchmark, targeting structure elucidation rather than screening and optimization.
- [TOMG-Bench](./tomg-bench.md) — text-based open molecule generation, a single-step counterpart to MolBench's multi-round optimization.
- [BioAgent Bench](./bioagent-bench.md) — multi-tool biomedical agent evaluation with a comparable long tool-call horizon.
- [AtomWorld](./atomworld.md) — agent evaluation over atomistic and molecular structure manipulation.
