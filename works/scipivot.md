# SciΠvot (2026)

> **English** | [简体中文](../zh/works/scipivot.md)

> **First appeared:** 2026-10-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.21082)

## Overview

Research-agent benchmarks usually score finished outputs, so they cannot show the moment when a principal investigator looks at an agent's plan and says "no, do this instead". SciΠvot is built from those moments. Over about six months, senior researchers ran LLM agents on 26 real research projects and corrected their judgments. Each case freezes the project record from just before a correction and asks a model to choose between the agent's original plan and the human-corrected one. The benchmark then measures how often models pick the correction, with and without the project record.

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [Sci$\Pi$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.21082v1>
- **Code / data:** <https://github.com/AutoResearch-Factory/SciPIvot> (248 cases, prompts, aggregate results; project records to follow)
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

A case contains the pre-intervention project record (code, experimental logs, progress notes), the original LLM plan, and the human-corrected alternative reconstructed from the project history. The model sees either the plans with the record ("project" condition) or the plans alone ("options only"), at one of five reasoning-effort settings, and chooses one. Each case is run twice with the option order reversed, the two scores are averaged, and unparsed answers count as wrong; chance is 50%. In two further stages the model is asked to reconsider without being told whether it was right. Cases were kept only if five models' 120 responses per case were split between the two plans, so the scores diagnose judgment on contested decisions and do not estimate how often agents err in general.

## Tasks

248 cases from 26 projects in six fields: applied mathematics and scientific computing (8 projects, 85 cases), robotics and control (4, 58), AI and machine learning (9, 59), biological imaging (1, 21), mechanics and materials (2, 20), and Earth sciences (2, 5). Judgment labels, primary and secondary, are planning 123, focus 122, anomaly awareness 88, adapting 65, evidence sufficiency 47, and repetition 4. Grok 4.6 wrote the cases; a pilot on 13 shared cases found no writer advantage. TODO(reference): number of senior researchers supervising the projects.

## Domains

Applied mathematics and scientific computing, robotics and control, AI and machine learning, biological imaging, mechanics and materials, and Earth sciences; theoretical and computational research on CPUs and GPUs.

## Evaluation

- **Accuracy at medium effort, project / options only:** GPT-6 Astra 59.5% / 63.7%, Claude Opus 5 38.9% / 58.9%, GPT-5.6 Sol 35.1% / 46.8%, Grok 4.6 33.1% / 54.0%, GPT-5.6 Terra 29.2% / 55.8%. Four of five models are below chance with the record; the five-model mean is 39.2% with the record and 55.8% without it.
- **Best project-condition score:** 63.5% (GPT-6 Astra at xhigh effort).
- **Human baseline:** 73.4% for 13 PhD students and postdocs new to the projects, reading the record with an agent assistant available.
- **Reconsideration:** mean accuracy goes 39.2%, 44.0%, 42.3% over the initial answer and two review stages; the first review fixes 422 errors and introduces 302, the second fixes 264 and introduces 305.
- **By judgment type (Astra):** 72.2% on anomaly-awareness cases, 56.1% on planning, 54.9% on focus.
- **Statistics:** 95% intervals from 10,000 paired bootstrap samples of cases, plus project-clustered intervals.

## Typical Duration

One binary choice per case plus up to two reconsideration turns; effort settings are provider reasoning levels, not matched token budgets.

## Main Contribution

A benchmark of real principal-investigator corrections from agent-run research projects that tests whether models recognize the corrective decision, and a measurement that adding the project record lowers model accuracy at medium effort.

## Key Design Ideas

- Each case is cut at the commit before a human correction, so the model sees only what was known then.
- The two plans are presented in both orders and averaged, removing position bias.
- The project-versus-options comparison isolates the effect of the inherited record on the choice.
- Reconsideration stages measure how often extra deliberation fixes or breaks an answer.

## Strengths

- Cases come from real project histories rather than constructed scenarios, with a measured human baseline.
- Scoring is a deterministic binary choice, with bootstrap and project-clustered intervals.
- The failure analysis is quantified by condition, review stage, and judgment type.

## Limitations

- The authors state that the benchmark measures recognition of corrective decisions, not plan generation or execution.
- Model-in-the-loop case selection means scores do not estimate general failure rates.
- Wet-lab work and specialized commercial software are excluded.
- Several cases share a project; Earth sciences has 5 cases and biological imaging one project.
- Effort settings are not equal compute budgets, and client tools differ across providers.
- Repository note: per-model response logs are not released, and the frozen project records are to be added later.

## Related Works

- [AI's Capability in Assisting Scientific Research II](./ai-assisting-research-ii-project-planning.md) — Also evaluates research planning on real projects against human judgment.
- [Labference](./labference.md) — Also scores a single next-decision choice under a fixed information set.
