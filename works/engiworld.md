# EngiWorld (2026)

> **English** | [简体中文](../zh/works/engiworld.md)

> **First appeared:** 2026-09-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.37686)

## Overview

Engineering benchmarks for language models usually check a computed answer or a generated script. Professional engineering work instead ends in a file produced inside a specific tool: a solid model in SolidWorks, a mesh and load case in Abaqus, a board layout in KiCad. EngiWorld has agents operate 26 professional software applications through a GUI or a command line, and its verifiers open the resulting artifact to check geometry, physical feasibility, and design rules. A task counts as solved only if every acceptance criterion passes, so a run that ends with a plausible report but an invalid file scores zero.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?](https://arxiv.org/abs/2609.37686), 2026 preprint (v2 posted 2026-10-09).
- **Full text:** <https://arxiv.org/html/2609.37686v1>
- **Project:** <https://engiworld.github.io>
- **Venue:** arXiv preprint (cs.AI, cs.CL), 2026

## Summary

Domain experts take workflows from software documentation, tutorials, and engineering resources and turn them into executable task specifications; every final task is executed and reviewed in its software environment. An agent receives a specification and either drives the desktop through PyAutoGUI at 1920×1080 or works through terminal commands and scripts. When it declares completion, a programmatic verifier reads the artifact (for example with CadQuery/OCCT, IfcOpenShell, or Abaqus odbAccess) and checks dimensions, topology, material and load assignments, simulation outputs within error bounds, and cross-file consistency. Quantitative design tasks earn partial credit only after a feasibility gate. In the evaluated subset the best agent scores 44.3 of 100, and 6 of 168 multi-software attempts succeed.

## Tasks

1,301 expert-curated tasks over six domains (CAD, CAE, CAM, BIM, EDA, and 3D visualization) and 26 applications, with 1,723 task–software associations. 691 tasks are CLI and 610 GUI. Task types: single-software 931, multi-software 60, software selection 140, quantitative design 40, image-based modeling 120, open-ended 10. The software spans CAD (FreeCAD, AutoCAD, SolidWorks, BRL-CAD, OpenSCAD, LibreCAD, SolveSpace), CAE (ANSYS, Abaqus, OpenFOAM, FEniCS, CalculiX, FLORIS, OpenFAST), CAM (FreeCAD Path, SolidCAM), BIM (Archicad, Bonsai, OpenStudio, Revit), EDA (Cadence OrCAD, EAGLE, Altium Designer, KiCad), and 3D visualization (Blender, ZBrush). Models are evaluated on a 300-task subset (152 CLI, 148 GUI). TODO(reference): per-domain task counts and the number and qualifications of the experts.

## Domains

Mechanical engineering design and manufacturing (CAD solid modeling, CAM toolpaths), computer-aided engineering analysis (finite-element and CFD solvers), building information modeling, electronic design automation for circuit boards, and 3D visualization.

## Evaluation

- **Binary tasks:** success only if all acceptance criteria pass.
- **Quantitative tasks:** infeasible outputs score 0; feasible outputs score Qᵢ = clip₀₋₁((m − m_base) / (m_ref − m_base)).
- **EngiScore:** 100/|D| × (sum of binary successes + sum of quantitative scores) over the evaluated tasks.
- **No LLM or VLM judge.** Verifier validation: 96 of 96 reference artifacts accepted, 40 + 40 + 5 alternative valid artifacts accepted, and 21 + 21 defective submissions (empty or metrics-only) rejected. A second annotator reviews expected-outcome labels; no agreement statistic is reported.
- **Results (EngiScore overall / GUI / CLI):** Claude Opus 5 44.3 / 40.5 / 47.9; GPT-5.6 Sol 38.0 / 28.6 / 47.1; Qwen 3.8 Max 25.8 / 16.6 / 34.7; DeepSeek V4.1 Flash 25.5 / 2.0 / 48.3; Gemini 3.7 Flash 25.3 / 14.2 / 36.1; Kimi K3 24.1 / 16.7 / 31.3; Qwen 3.8 Flash 16.1 / 1.0 / 30.8. CAM is the hardest domain for every model.
- **Failure analysis:** failure classes are DONE with zero score, decision-turn exhaustion, explicit FAIL, runtime-limit violation, and unexpected desktop closure. DONE-with-zero-score and turn exhaustion together make up 94.1% of failures; DONE is 87.0% of GPT's failures and 73.9% of Claude's. Turn exhaustion is 55.3% of GUI failures and 36.6% of CLI failures.
- Repository note: the arXiv abstract page (current version) gives the best score as 44.7; the v1 results table gives 44.3.

## Typical Duration

Decision limits of 200 rounds (GUI) and 100 (CLI), raised to 300 and 150 for multi-software and open-ended tasks, with a five-hour runtime limit; 28 DeepSeek runs and 9 Claude runs hit that limit. Steps per task range from 54.9 (GPT) to 120.5 (Qwen 3.8 Flash), and cost per task from $0.45 (Qwen 3.8 Flash) to $19.02 (Claude).

## Main Contribution

A benchmark that scores agents on the engineering artifacts they produce inside professional GUI and CLI software, using domain verifiers instead of answer matching or judges.

## Key Design Ideas

- The same suite covers GUI and CLI access, so a model's score can be compared across the two interfaces.
- Verifiers check the artifact itself (solid validity, solid–void occupancy, boundary conditions, simulation outputs), not the agent's description of it.
- A feasibility gate precedes partial credit on quantitative design tasks.
- Multi-software and software-selection tasks test whether agents can carry work across tools.

## Strengths

- Verification is programmatic and checked against reference, alternative valid, and defective artifacts.
- GUI and CLI scores are reported separately, exposing large gaps for some models (DeepSeek V4.1 Flash: 2.0 GUI against 48.3 CLI).
- The failure breakdown shows that most failures are runs that declare success with an invalid artifact or run out of turns.

## Limitations

- Models are evaluated on a 300-task subset, not on all 1,301 tasks.
- The paper does not report per-domain task counts, a human baseline, or contamination measures.
- The paper notes that a visually correct artifact can still be unusable, so the verifiers' acceptance criteria bound what is measured.
- Repository note: no dedicated limitations section appears in the v1 full text.

## Related Works

- [EngDesign](./engdesign.md) — Also scores engineering design outputs with simulation-based checks, but through scripts rather than professional software.
- [AEC-Bench](./aec-bench.md) — Also evaluates agents on architecture, engineering, and construction artifacts.
- [PDAgent-Bench](./pdagent-bench.md) — Also evaluates agents operating EDA tooling.
