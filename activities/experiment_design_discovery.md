# Experiment Design & Scientific Discovery

> **English** | [简体中文](../zh/activities/experiment_design_discovery.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on deciding how to obtain scientific information or infer new scientific structure — designing experiments, planning observations, selecting measurements, generating and testing hypotheses, and discovering laws.

## Scope

Includes interactive and simulated experimentation where the agent chooses experiments or observations, symbolic law discovery, and hypothesis or idea generation. It is distinguished from Laboratory & Instrument Control (deciding *what* to test versus physically *executing* the apparatus); a simulated environment alone does not make a task Simulation & Scientific Computing.

## Task Patterns

A large cluster casts discovery as **interactive experimentation in simulated worlds with hidden physics**, where the agent iteratively proposes experiments, observes outputs, and submits a governing law. [NewtonBench](../works/newtonbench.md) uses a run_experiment tool over counterfactually shifted physics laws, [PhysGym](../works/physgym.md) adds controlled prior-knowledge levels, [Gravity-Bench-v1](../works/gravity-bench.md) probes simulated two-body systems, [DiscoverPhysics](../works/discoverphysics.md) asks for both an explanation and a Python law over N-body worlds, and [SciGym](../works/scigym.md) runs a systems-biology dry lab over hidden SBML systems. Several tie discovery explicitly to a **resource/measurement budget**: [MaD Physics](../works/mad-physics.md) prices each observation by fidelity under a fixed cap, and [Gravity-Bench-v1](../works/gravity-bench.md) constrains data collection.

A **symbolic equation / hypothesis rediscovery** group evaluates recovering laws or hypotheses while suppressing memorization. [LLM-SRBench](../works/llm-srbench.md) recasts equations into unfamiliar forms and adds synthetic problems, while [MOOSE-Chem](../works/moose-chem.md) rediscovers post-cutoff chemistry hypotheses. Full-cycle rediscovery of published findings appears in [EXP-Bench](../works/exp-bench.md) and [FIRE-Bench](../works/fire-bench.md), where agents design and execute experiments to reproduce documented results.

**Idea and hypothesis generation** is scored by expert-emulating or panel metrics: [IdeaBench](../works/ideabench.md) grounds ideation in influential-paper context, [LiveIdeaBench](../works/liveideabench.md) tests divergent thinking from single keywords, and [Materials Hypothesis Generation](../works/materials-hypothesis.md) generates goal- and constraint-guided materials hypotheses. Related planning-oriented prediction appears in [AlchemyBench](../works/alchemybench.md) (synthesis recipes) and [MLRC-Bench](../works/mlrc-bench.md) (proposing novel ML methods).

A final cluster frames discovery as **sequential information acquisition toward a conclusion**, often under cost. Clinical-diagnosis benchmarks [AgentClinic](../works/agentclinic.md) and [SDBench](../works/sdbench.md) require iteratively eliciting findings and ordering costed tests before committing to a diagnosis; [MolQuest](../works/molquest.md) makes chemical structure elucidation an abductive loop of choosing which spectra to acquire; and [SciAgentArena](../works/sciagentarena.md) spans real biomedical discovery and optimization tasks with stepwise verification.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AgentClinic | 2024 | Sequential clinical diagnosis under incomplete information | Simulated doctor-patient encounters, 9 specialties, 7 languages, multimodal | Commit to correct diagnosis via history/measurement gathering | [card](../works/agentclinic.md) |
| IdeaBench | 2024 | Research idea generation grounded in paper context | Static single-turn generation from influential titles/abstracts + references | Novel ideas scored by GPT-4o ranking + Insight Score | [card](../works/ideabench.md) |
| LiveIdeaBench | 2024 | Divergent-thinking scientific ideation from minimal context | Single-keyword prompts, 1,180 keywords, 22 domains, 40+ models | Ideas scored on 5 creativity dimensions by LLM panel | [card](../works/liveideabench.md) |
| MOOSE-Chem | 2024 | Rediscovering unseen chemistry hypotheses | 51 post-2024 annotated papers, 3,000-paper inspiration corpus | Regenerate paper's hidden hypothesis, high similarity to ground truth | [card](../works/moose-chem.md) |
| AlchemyBench | 2025 | End-to-end materials synthesis planning | Static prediction over 17,000 expert-verified recipes | Materials/procedure/characterization graded by LLM-as-Judge | [card](../works/alchemybench.md) |
| EXP-Bench | 2025 | Conducting complete AI research experiments | 461 tasks from 51 NeurIPS/ICLR 2024 papers, incomplete starter code | Design, implement, execute, analyze; 12,737 gradable subtasks | [card](../works/exp-bench.md) |
| Gravity-Bench-v1 | 2025 | Budgeted observation planning for gravity discovery | Interactive simulated two-body systems, OOD physics, | 100-point budget | [card](../works/gravity-bench.md) |
| LLM-SRBench | 2025 | Memorization-resistant symbolic equation discovery | 239 problems (LSR-Transform, LSR-Synth), four domains | Recover governing equations; best 31.5% symbolic accuracy | [card](../works/llm-srbench.md) |
| Materials Hypothesis Generation | 2025 | Goal-driven constraint-guided hypothesis generation | Static generation over curated recent journal-publication dataset | Hypotheses scored by scalable expert-emulating metric | [card](../works/materials-hypothesis.md) |
| MLRC-Bench | 2025 | Proposing and implementing novel ML research methods | 7 competition tasks under a scaffold | Close baseline-to-human gap; best agent closes 9.3% | [card](../works/mlrc-bench.md) |
| NewtonBench | 2025 | Interactive scientific law discovery | 324 tasks, shifted laws, run_experiment tool, difficulty tiers | Submit hidden target law as symbolic expression | [card](../works/newtonbench.md) |
| PhysGym | 2025 | Interactive physics discovery with controlled priors | 97 curated problems, 100-experiment budget, four prior-knowledge levels | Submit hypotheses about governing physical laws | [card](../works/physgym.md) |
| SciGym | 2025 | Iterative experiment design in systems-biology dry lab | Hidden SBML systems; 137 small evaluated, 350 released | Submit hypothesized SBML mechanism against ground truth | [card](../works/scigym.md) |
| SDBench | 2025 | Budgeted sequential diagnosis | 304 NEJM-CPC cases, gatekeeper reveals findings on request | Commit diagnosis scored on accuracy-cost frontier | [card](../works/sdbench.md) |
| DiscoverPhysics | 2026 | Discovering laws of counterfactual simulated worlds | 22 N-body worlds, iterative experiments, raw trajectory data | Submit explanation plus Python law; trajectory MSE + rubric | [card](../works/discoverphysics.md) |
| FIRE-Bench | 2026 | Full-cycle rediscovery of published ML findings | 40 executed tasks + 60-paper pool, research question only | Design/run experiments to rediscover findings; best <50 F1 | [card](../works/fire-bench.md) |
| MaD Physics | 2026 | Budgeted measurement planning and law inference | Three JAX simulators (classical/fluid/quantum), altered-physics variants | Infer law under fidelity-priced budget to predict future state | [card](../works/mad-physics.md) |
| MolQuest | 2026 | Agentic chemical structure elucidation | Multi-turn spectra acquisition (NMR/MS), iterative refinement | Correct structure; SOTA | [card](../works/molquest.md) |
| SciAgentArena | 2026 | Real-world scientific research across scales |  | 200 stepwise-verified tasks, five biomedical fields, agent-agnostic | [card](../works/sciagentarena.md) |

## Related Works

- [AgentClinic](../works/agentclinic.md)
- [IdeaBench](../works/ideabench.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [AlchemyBench](../works/alchemybench.md)
- [EXP-Bench](../works/exp-bench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [LLM-SRBench](../works/llm-srbench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [NewtonBench](../works/newtonbench.md)
- [PhysGym](../works/physgym.md)
- [SciGym](../works/scigym.md)
- [SDBench](../works/sdbench.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FIRE-Bench](../works/fire-bench.md)
- [MaD Physics](../works/mad-physics.md)
- [MolQuest](../works/molquest.md)
- [SciAgentArena](../works/sciagentarena.md)
