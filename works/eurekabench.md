# EurekaBench (2026)

> **English** | [简体中文](../zh/works/eurekabench.md)

> **First appeared:** 2026-09-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.00492)

## Overview

EurekaBench asks whether an agent that can fit observations has also found the mechanism behind them. The agent runs experiments in a scientific simulator for up to four hours and then submits a mechanism as prose, executable code, and an experiment log. Judges score predictive accuracy, adherence to known scientific constraints, and whether the mechanism answers expert-written insight questions. The headline score gives accuracy and insight credit only when every constraint passes, so a model tuned to match the data but violating a known constraint scores 0.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** [EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights](https://arxiv.org/abs/2610.00492), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.00492v1>
- **Project:** <https://eurekabench.github.io/>
- **Code:** <https://github.com/EurekaBench/EurekaBench> (README lists 2026/10/02 as the initial release)
- **Venue:** arXiv preprint (cs.CL, cs.AI), 2026

## Summary

Each problem starts from initial observations that human scientists have already partly explained. The agent gets a workspace with the task description, a command-line interface to an environment such as a C. elegans simulator or a tokamak transport code, and, for some problems, training data. It submits `mechanism.md`, `mechanism.py`, and `experiments.log`. Two agentic judges can run extra experiments against the environment but may not change the mechanism. The design separates fitting the data from explaining it: the best agents come within 1.4 points of the human reference on predictive accuracy but trail it by 27.3 points on insights.

## Tasks

26 expert-verified problems with 306 scientific insight questions. By domain: neuroscience 10, astrophysics 7, plasma physics 3, computer science 3, geophysics 2, chemistry 1. Ten of 15 consulted PhD scientists from 10 universities collaborated on the benchmark. They refined each task specification and evaluation criterion over several rounds and verified each insight as scientifically important. Insight questions draw on recent human work, open questions in the source studies, and insights the experts proposed. Environments include c302 (six C. elegans problems), TRIBE v2 (four human-brain problems), CAMELS and DREAMS simulation suites, TORAX (with TokaMaker and GPEC for one edge problem), FEniCSx, an HBV model driven by CAMELS-US forcing, LoRA fine-tuning and TransformerLens on open-weight language models, and AIMNet2-rxn. Each environment is packaged as an Apptainer image. The paper does not give per-domain insight counts.

## Domains

Six fields: neuroscience (C. elegans neural circuits and behaviour; human brain responses to visual and language input), astrophysics (galaxies, galaxy environments, gravitational waves, the Milky Way, baryonic feedback, and warm-dark-matter merger trees and populations from simulation suites), plasma physics (ARC tokamak and negative-triangularity core and edge scenarios), computer science (three problems on language-model behaviour: stated belief shift, subliminal learning, and circuit discovery), geophysics (ice-shelf flow laws; catchment properties in hydrology), and chemistry (reaction discovery). Most environments are simulators; the catchment problem adds noise to simulated streamflow driven by CAMELS-US meteorological inputs.

## Evaluation

- **Scientific constraints (SC):** each constraint test scores 1 or 0, and a mechanism passes only if every test passes.
- **Predictive accuracy (PA):** each criterion scores in [0, 1] from running `mechanism.py` on held-out test data, which comes from the original studies or task-specific simulators.
- **Scientific insights (SI):** each insight question scores 1 or 0, and credit requires complete supporting evidence.
- **Conditioned score:** if all SC tests pass, (PA points + SI points) / (PA criteria + SI criteria); otherwise 0. The reported score averages the conditioned scores from Claude Opus 4.8 and GPT 5.6 Sol, both run as agentic judges.
- **Human reference:** the progress human scientists have already made on each problem is scored as a human solution: conditioned 63.7%, PA 48.8%, SI 69.7%, 0/26 SC failures.
- **Results (Table 2, conditioned %):** Claude Code with Claude Fable 5.1 29.8, Opus 5 27.3, and Opus 4.8 18.4; Codex with GPT 6 Astra 28.7 and GPT 5.6 Sol 19.4; OpenHands with DeepSeek V4 Flash 14.6 and Kimi K3 12.9. All models ran at maximum reasoning effort. SC failures range from 10/26 (GPT 6 Astra) to 17/26 (GPT 5.6 Sol). Top PA is 47.4% (Fable 5.1 and GPT 6 Astra), close to the human 48.8%, while top SI is 42.4% against the human 69.7%. Table 2 also reports a call count and a dollar cost per agent, from $1.24 (DeepSeek V4 Flash) to $24.62 (GPT 6 Astra).
- **Failure analysis:** expert review of logs names four failure types: relying on preselected hypotheses, treating task optimization as mechanism discovery, not using experiments to resolve uncertainty, and stopping at observations. An appendix lists ten finer failure modes without per-mode counts. In 6.7% of cases, judges credited insights found in the experiment log that the submitted mechanism did not support. Claude Fable 5.1 scores 22.7% on insights credited from experimentation against 42.4% from its mechanism.
- **Guidance experiment:** on two problems (neural dynamics and ARC tokamak) with Claude Fable 5.1, a prompt stating the scientific goal raises the SI contribution by 10.0 and 7.9 points, and giving the insight questions as targets raises it by 32.5 and 15.8 points. The authors call the second setting unnatural.
- Repository note: the abstract says agents outperform human scientists on predictive accuracy; in the aggregate PA column of Table 2, no agent exceeds the human 48.8%.
- Repository note: the paper reports no agreement statistic between the two judges or between the judges and the experts.

## Typical Duration

One H100 GPU, up to 1,000 iterations, and four hours per run. Whether the call and cost figures in Table 2 are per problem or totals is not stated.

## Main Contribution

Makes the scientific-constraint check a gate on the headline score, and scores mechanisms on insight questions separately from predictive accuracy. Fitting held-out data well therefore does not count as a discovery on its own.

## Key Design Ideas

- Three deliverables keep the causal account (`mechanism.md`), the testable implementation (`mechanism.py`), and the experiment record (`experiments.log`) separate, so judges can check whether an insight follows from the mechanism or only appears in the log.
- Web search is allowed, but the original publications and literature aggregators behind each problem are blocked.
- Judges are agents that can run new experiments on the environment, not single-pass readers of the submission.

## Strengths

- The same table reports PA, SI, and SC failures separately, which shows that agents can approach the human PA while trailing far behind on SI.
- The human-progress reference puts each score next to what scientists have already established on the same problem.
- The guidance experiment tests one explanation for the low SI scores directly: whether agents miss insights because the goal was never stated.

## Limitations

- The authors note that the insight questions reflect research directions chosen with the experts, so valid findings outside the rubric earn no SI credit.
- SI depends on judge reasoning. The authors note that judges may accept confidently stated conclusions, and that expert reviews of selected submissions suggest some automated assessments are too generous.
- Web restrictions limit access during evaluation but, as the authors state, do not rule out exposure to the source research during pretraining.
- Coverage is uneven: neuroscience has 10 problems and chemistry 1.
- Repository note: the number of runs per problem is not stated in the paper.

## Related Works

- [HeurekaBench](./heurekabench.md) — Similar name; also evaluates scientific insight generation, but from real single-cell data analyses.
- [DiscoverPhysics](./discoverphysics.md) — Also has agents run experiments in simulated worlds and submit an explanation scored apart from prediction.
- [Into the Unknown](./into-the-unknown.md) — From an overlapping author group; agents write follow-up papers on open directions instead of explaining known observations.
