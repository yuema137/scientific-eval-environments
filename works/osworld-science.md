# OSWorld-Science (2026)

> **English** | [简体中文](../zh/works/osworld-science.md)

> **First appeared:** 2026-09-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.39903)

## Overview

General computer-use benchmarks test agents on office, browser, and file-management tasks, so they say little about whether an agent can operate the software scientists actually use: a chemical drawing editor, a pathology viewer, a CFD package, a statistics suite. OSWorld-Science moves the OSWorld setup into that software. An agent reads a scientific task, sees the screen, and acts through pyautogui code or the command line inside a domain-specific Ubuntu image. After the episode, a task-specific evaluator inspects the application state and the files the agent produced and awards full or partial credit.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](https://arxiv.org/abs/2609.39903), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.39903v1>
- **Project:** <https://discoailab.github.io/osworld-science-page/>
- **Code:** <https://github.com/DiscoAILab/OSWorld-Science>
- **Data:** <https://huggingface.co/datasets/SciAILab/OSWorld-Science-data> (questions and Docker images)
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Each task runs in an Ubuntu image built for its domain, with the scientific application installed and any input files in place. At every step the agent receives the current screenshot and its last five screenshot–response pairs, and returns one block of pyautogui code or `<WAIT>`, `<DONE>`, or `<FAIL>`; 122 of the 146 tasks also allow command-line actions. When the episode ends, only the collected application state and output files are graded. A retrosynthesis task in ASKCOS, for example, is scored by checking the saved result against the task's requirements; single-answer tasks use exact matching with partial credit for completed steps, and simulation tasks pass if the reported parameter falls within a set error range. The benchmark measures use of existing software on specified tasks; the title's "learning" refers to how tasks were designed from tutorials, and no experiment isolates how agents learn unfamiliar software.

## Tasks

146 tasks across seven domains: chemistry 43, physics 31, medicine 26, statistics 20, biology 18, geographic information 6, and linguistics 2. The largest software sets are QuPath 23, ChemDraw 21, ASKCOS 21, and SAS/R 20; the remaining 61 tasks use OpenFOAM, ANSYS, EEGLAB, PyMOL and MestReNova, QGIS, CIAO with DS9, Weasis, 3D Slicer, Praat, and a PDF viewer. Tasks were written either by domain experts with PhD-level knowledge from a template, or through an AI-assisted route that starts from an anchor tutorial and is refined with humans. TODO(reference): number of experts. Repository note: the paper's environment section counts 17 software packages while the results use 14 configurations, and its Section 3 lists neuroscience where Section 4 lists statistics.

## Domains

Chemistry (molecular drawing, retrosynthesis), physics (CFD and finite-element simulation in OpenFOAM and ANSYS, X-ray data analysis in CIAO/DS9), medicine (pathology image analysis in QuPath, radiology viewers), statistics (statistical computing in SAS and R), biology (structural biology in PyMOL, NMR in MestReNova, drug-synergy analysis, EEG analysis), geographic information (QGIS), and linguistics (Praat).

## Evaluation

- **Scorer:** execution-based, task-specific evaluators read the post-episode application state and artifacts; reward lies in [0, 1], with 1 for all requirements met. No LLM judge is used. No human baseline is reported.
- **Models:** 12 vision-language models in a modified OSWorld PromptAgent harness (Kimi K3 in its own official design).
- **Mean task score, partial credit included (cost per task):** Claude Fable 5.1 73.7% ($6.5), Claude Opus 5 57.9% ($6.7), GPT-6 Astra 57.4% ($7.7), GPT-5.6 Sol 50.1% ($2.79), GPT-5.6 Terra 31.8% ($2.0), Kimi K3 30.2% ($11.7), Claude Sonnet 5 26.3% ($3.6), GPT-5.6 Luna 22.6% ($0.23).
- **By domain:** chemistry is hardest (Fable 5.1 about 44%, Opus 5 about 39%); Fable 5.1 reaches about 96% in biology.
- **Failure accounting over 1,530 released runs:** 402 (26.3%) earn full credit. Of the 1,100 that do not (after excluding 20 harness-terminated and 8 unresolved runs), 667 produce no graded artifact, 613 of them after exhausting the step budget; 400 produce wrong content and 33 an invalid artifact. GPT models produce 78 of the 84 placeholder-only artifacts, 77 of them in chemistry.
- **Ablations (23 QuPath tasks, one run per cell):** Opus 5's mean score moves from 35.2 with a one-step history window to 57.0 with ten steps; task language changes Opus 5's score between 29.7 (Chinese) and 53.1 (Japanese). No cell differs significantly from its default after Bonferroni correction.

## Typical Duration

100 steps for most tasks, a 16k-token reply limit per step, and at most 10 actions per reply. Wall-clock time per task is not reported. TODO(reference): time per task.

## Main Contribution

A computer-use benchmark and set of reproducible environments built on real scientific applications across seven domains, with execution-based evaluators that check application state and output files and give partial credit.

## Key Design Ideas

- Each domain has its own Docker image, so commercial and open scientific packages run in a fixed starting state.
- Grading uses only the state and files collected after the episode, not the agent's claims.
- Agents may use the command line where a task allows it, so the benchmark measures task completion rather than GUI clicking alone.
- Released data carry a contamination watermark for detecting later training use.

## Strengths

- Scoring is execution-based with no judge, and partial credit is defined per task.
- Per-task API cost is reported for each model next to its score.
- The failure accounting counts outcomes over all released runs, separating budget exhaustion, wrong content, and invalid artifacts.

## Limitations

- The authors state that the domain distribution is uneven; geographic information has 6 tasks and linguistics 2.
- Ablations use one run per cell on QuPath tasks only, and none is significant after correction.
- Some trajectories are not released because the software requires a license.
- Several tasks depend on online services (SAS OnDemand, SynergyFinder, the RCSB API, AlphaFold DB); the paper notes that local hosting would remove this dependence.
- Repository note: results are reported from one run per model and task, with no variance estimate.

## Related Works

- [OSWorld](./osworld.md) — The general computer-use environment whose harness and setup this benchmark extends to scientific software.
- [EngiWorld](./engiworld.md) — Also scores agents operating professional software through GUI or CLI with programmatic artifact checks.
- [CADWorld](./cadworld.md) — Also a computer-use benchmark on a single scientific-engineering application, FreeCAD.
