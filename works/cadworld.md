# CADWorld (2026)

> **English** | [简体中文](../zh/works/cadworld.md)

> **First appeared:** 2026-09-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.16251)

## Overview

Text-to-CAD benchmarks score a generated script or shape, which skips how engineers actually work: building a part step by step in a GUI, with sketches, constraints, assemblies, and analysis set-ups saved in a project file. CADWorld gives a computer-use agent that GUI. The agent reads an instruction and reference images, operates FreeCAD through screenshots and mouse and keyboard actions, and saves its work. Host-side scripts then open the saved `.FCStd` file and check its geometry, structure, and construction history; a task passes only if every check passes.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design](https://arxiv.org/abs/2609.16251), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.16251v1>
- **Project:** <https://cad-world.github.io>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

FreeCAD runs in an Ubuntu VM (8 cores, 8 GB RAM, 1920×1080 screen). At each step the agent receives the instruction, the current screenshot, optional reference images, and its last 10 turns, and issues allowlisted pyautogui-style actions or `WAIT`, `DONE`, or `FAIL`; FreeCAD scripting and direct filesystem access are blocked. After at most 100 steps, the evaluator reads the saved file. For a sketch task it checks entities, constraints, dimensions, profile area, perimeter, and center of mass; for an assembly, the joint types; for CAM, material removal and over- and undercut ratios; for FEM, the analysis objects, materials, boundary conditions, mesh, solver, and exported results. No LLM judge or human inspection is involved. Tasks have explicit goals and supplied assets, so open-ended design trade-offs are not tested.

## Tasks

200 tasks over 183 concepts in 11 workflow categories: Part 77, Sketch 63, Assembly 25, CAM 15, FEM 3, Appearance 3, point cloud 3, Macro 3, Measure 3, Mesh 3, and TechDraw 2. Tasks were authored from FreeCAD workbench capabilities, tutorials, documentation, and common mechanical-design workflows; authoring, precondition files, evaluator design, and manual checks took about three months and 1,300 person-hours. TODO(reference): number and background of task authors.

## Domains

Mechanical CAD: constrained sketching, part modeling (pad, pocket, revolve, loft, sweep, fillet), assemblies with revolute, slider, and rack-and-pinion joints, CAM toolpaths, finite-element analysis set-up (CalculiX via Gmsh), mesh processing, and technical drawing.

## Evaluation

- **Scorer:** deterministic checks on the saved project file and auxiliary outputs; binary success, with no partial credit. Continuous diagnostics (volume error, bounding-box IoU, center-of-mass distance) are logged but not scored. Each failed episode gets one of 11 deterministic failure reasons, such as no output file, wrong document structure, or wrong construction process.
- **Success / finish rate:** expert reference 87.0% / 100%; GPT-5.4 (CUA) 17.5% / 62.5%; Opus 4.8 (CUA) 16.0% / 49.5%; Kimi K2.6 7.5% / 20.5%; OpenCUA 1.5% / 8.0%; Holo 3.1 0.5% / 21.5%; Qwen3.6 0.0% / 3.0%; MiniMax M3 0.0% / 2.5%.
- Every model scores 0% on all CAM, FEM, and TechDraw tasks.
- **Failure pattern:** weaker agents mostly fail before saving a valid file, often in repeated action loops; stronger agents more often fail on structure, geometry, or construction process. Per-reason counts are given in figures.
- **Terminal-only ablation (50 tasks):** GPT-5.4 without the computer-use harness completes none; most failures are wrong document structure.
- Repository note: the v1 introduction reports 25.0% success for the strongest agent and mentions a 60-task budget-controlled subset, while the abstract and results table give 17.5% on the full benchmark; this card uses the table.

## Typical Duration

Up to 100 GUI steps per task, 512 output tokens per step by default. No wall-clock budget is specified. TODO(reference): average steps or time per task.

## Main Contribution

A long-horizon computer-use benchmark for mechanical CAD in FreeCAD, scored entirely by executable checks on saved project files across sketching, modeling, assembly, CAM, and FEM workflows.

## Key Design Ideas

- Grading reads the saved project file, so a task passes only if the model's structure and construction history, not just the final shape, are correct.
- Scripting and filesystem access are blocked, so the agent must reach the result through the GUI.
- Continuous geometric diagnostics are kept separate from the binary score for failure analysis.
- Failure reasons are assigned deterministically from the evaluator's output.

## Strengths

- Scoring is fully deterministic with no judge.
- A measured expert reference pass anchors the success rates.
- The failure taxonomy separates not saving a file from saving a structurally or geometrically wrong one.

## Limitations

- The authors state that tasks have explicit goals and supplied assets, so requirements elicitation and design trade-offs are not covered.
- Only FreeCAD is used; transfer to commercial CAD suites is untested.
- The human row is one expert reference pass, not a controlled human-subject study.
- FEM has 3 tasks and TechDraw 2, so per-category results there rest on very few items.
- Models differ in interfaces, context limits, and serving latency, which affects efficiency comparisons.

## Related Works

- [EngiWorld](./engiworld.md) — Also scores agents on CAD, CAM, and CAE work in professional software with programmatic artifact checks.
- [OSWorld](./osworld.md) — General computer-use environment with the same screenshot-and-pyautogui action interface.
- [OSWorld-Science](./osworld-science.md) — Also a computer-use benchmark on scientific and engineering software.
