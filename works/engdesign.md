# EngDesign (2025)

> **English** | [简体中文](../zh/works/engdesign.md)

> **First appeared:** 2025-07-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2509.16204)

## Overview

EngDesign is a benchmark of 101 real-world engineering **design** tasks across nine engineering areas in which an LLM must produce a functional design artifact that is then verified by domain simulators rather than checked against a reference answer.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.16204>
- **Code:** <https://github.com/AGI4Engineering/EngDesign>
- **Dataset:** <https://huggingface.co/datasets/opt1zer/EngDesign>
- **Project:** <https://agi4engineering.github.io/Eng-Design/>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track

## Summary

EngDesign is built on the argument that existing engineering evaluations measure textbook recall, whereas real engineering asks for a design that satisfies stated goals, constraints, and performance requirements. Each task therefore gives the model a design specification and expects a structured design output, which an automated pipeline feeds to a domain-specific simulator (MATLAB, SPICE/Cadence, finite element analysis, or a hand-written evaluation script) for functional verification. Every task returns a binary pass/fail verdict, a 0–100 numerical score, and an evaluation log, and the harness additionally supports an iterative protocol in which the model receives simulator feedback and revises its design. The authors evaluate 12 chat and reasoning LLMs and report that even the strongest model passes only a minority of tasks on a first attempt.

## Tasks

101 design tasks carrying 473 gradable items, distributed over nine areas: Operating System Design (8), Computer Architecture Design (5), Control Design (18), Mechanical Systems (7), Structure Design (13), Digital Hardware Design (17), Analog IC Design (5), Robotics (10), and Signal Processing (18). 23 tasks include images as part of the task input. 48 tasks require proprietary domain software (for example MATLAB or Cadence) for evaluation; the remaining 53 are fully open and evaluated with manually authored scripts, and are released separately as EngDesign-Open. Each task folder in the released repository ships an LLM prompt, an output-structure specification, an evaluation script, optional images, and logs. Structure Design tasks include compliance-minimising topology optimisation on loaded 2-D design domains with pin and roller supports under a volume-fraction constraint (for example a 6×1 m domain with a volume fraction ≤ 0.25 solved with SIMP), Michell-structure layout, a pre-cracked fracture-mechanics domain, sizing the cross-sectional area of a truss member by finite-element analysis in MATLAB, and selecting the thickness of a rectangular steel beam under two point loads via 3-D structural simulation.

## Domains

The benchmark is explicitly multi-domain. **Civil & Structural Engineering** is represented by the Structure Design area, whose tasks size structural members (truss member area, steel beam thickness) and lay out load-carrying structure under support and volume constraints using finite-element and topology-optimisation verification. Co-domains: Mechanical & Aerospace (Mechanical Systems, and the solid-mechanics content shared with Structure Design), Electrical (Control Design, Digital Hardware Design, Analog IC Design, Signal Processing), Robotics (robot design and planning tasks), and Computer Science / Software & Systems (Operating System Design, Computer Architecture Design). The paper does not tie the Structure Design tasks to any building or bridge design code.

## Evaluation

Model output is parsed into predefined structured fields and then executed by a task-specific evaluation script that runs the relevant simulator. Each task yields a binary pass/fail status, a 0–100 partial-credit score derived from its gradable items, and a detailed log. For Structure Design, the checks are compliance, volume-fraction satisfaction, and symmetry classification computed from the finite-element/topology-optimisation solution. Aggregate reporting uses pass rate and mean score, separately for chat and reasoning models. In the iterative-design protocol the model is given its previous performance metrics as feedback and allowed to resubmit.

## Typical Duration

Single-turn generation per task in the default protocol; the iterative-refinement protocol allows up to 10 improvement rounds per task. Prompts are short — the Structure Design area averages 345.31 prompt tokens (range 186–483), the lowest of the nine areas. No wall-clock or total token budget is reported.

## Main Contribution

The authors frame EngDesign as the first benchmark to evaluate LLM engineering **design** ability through simulation-driven functional verification across nine engineering areas, shifting evaluation away from static answer checking toward whether a produced design actually works under its stated constraints.

## Key Design Ideas

- Tasks are specified as design problems with goals, constraints, and performance requirements, not as questions with reference answers.
- Verification is executed by the domain's own tools — MATLAB, SPICE/Cadence, finite element analysis, topology-optimisation solvers — via per-task evaluation scripts.
- Structured output schemas per task make free-form LLM text machine-gradable.
- Dual reporting of a binary pass and a 0–100 partial-credit score over 473 gradable items.
- An iterative protocol that returns simulator feedback to the model for up to ten revision rounds, separating one-shot design ability from refinement ability.
- An EngDesign-Open subset of 53 licence-free tasks so results are reproducible without proprietary software.

## Strengths

- Verification is functional and executable rather than answer-matching, which is difficult to game.
- Nine areas with per-area scores expose where capability is uneven; the paper reports analog IC design as particularly weak.
- Both one-shot and feedback-driven regimes are measured, quantifying how much iteration recovers (the best model rises from a 34.38% first-attempt pass rate to almost 60% after ten iterations).
- Task assets (prompt, output schema, evaluation script, logs) are released per task, making the harness inspectable.

## Limitations

- Roughly half the tasks (48 of 101) need proprietary software, so the fully reproducible subset is smaller than the headline count.
- The nine areas are unevenly sized (5 to 18 tasks), and 13 Structure Design tasks is a thin sample of structural engineering.
- Repository note: the Structure Design tasks are grounded in generic structural mechanics — topology optimisation, member sizing, fracture — rather than in building, bridge, or foundation systems, and no design code (AISC, ACI, Eurocode) is checked, so civil/structural coverage is narrower than the area name suggests.
- Repository note: the reported model set is from 2025 and the pass-rate figures will age quickly relative to the fixed task set.

## Related Works

- [ERI Benchmark](./eri-benchmark.md) — another multi-field engineering benchmark that includes a civil field alongside mechanical, electrical, and chemical.
- [Frontier-Eng](./frontier-eng.md) — also scores engineering designs by simulator reward under an iterative interaction budget.
- [StructureClaw](./structureclaw.md) — structural-engineering-specific agent benchmark with solver-verified structural models.
- [FEABench](./feabench.md) — finite-element analysis driven through a commercial simulator as the verification mechanism.
- [EEE-Bench](./eee-bench.md) — multimodal electrical and electronics engineering benchmark covering overlapping subdomains.
