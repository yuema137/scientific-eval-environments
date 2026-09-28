# AgentIdeaBench (2026)

> **English** | [简体中文](../zh/works/agentideabench.md)

> **First appeared:** 2026-09-07 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.07611)

## Overview

AgentIdeaBench tests whether an agent can propose a scientific hypothesis after gathering its own literature. It compares that workflow with receiving a curated reading list, using the same output format and literature-grounded critics.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** [AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era](https://arxiv.org/abs/2609.07611), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.07611v1>
- **Code and data:** <https://github.com/HKUST-KnowComp/AgentIdeaBench> (release announced September 11).

## Summary

The evaluator retrieves prior art before assessing originality, rather than relying only on the judge's memory. Active exploration improves feasibility, clarity, and specificity in the reported study; measured originality does not significantly improve. The paper distinguishes 35 evaluated models from 33 with matched Static–Active outputs and 28 matched primary-roster models used for headline analysis.

## Tasks

The suite contains 100 research subfields; 40, eight per discipline, receive dense scoring with three hypotheses per model and setting. Static supplies paper titles and abstracts. Active supplies a subfield and Semantic Scholar search/fetch tools. Both produce one 80–150-word hypothesis. A run therefore moves from a subfield, through evidence collection, to a proposal and its critic scores.

## Domains

Computer science, physics, biology, chemistry, and medicine. Each discipline has eight densely scored subfields; the task is literature-grounded hypothesis generation, not executing an experiment. The source does not provide a single canonical subfield label for each discipline's entire slice.

## Evaluation

Three critics score originality, feasibility, clarity, impact, and specificity. For each dimension, the highest score is dropped and the other two are averaged; weighted aggregation emphasizes originality. Human landmark papers provide reference anchors, rather than a timed human-agent competition. A preliminary human study on 100 computer-science hypothesis pairs finds 77% critic agreement with the human majority (Cohen kappa 0.55); it does not validate the other disciplines. The study also includes rubric calibration, replay controls, and quantified tool-protocol failures. Target literature is post-cutoff for nearly all evaluated models, not a guarantee for every model.

## Typical Duration

Active generation has a ten-call search/fetch budget and a 6,000-token limit. A standard wall-clock duration is not reported. The call cap is not a priced cost metric.

## Main Contribution

A matched evaluation of curated versus agent-controlled literature access, with originality judged against retrieved evidence.

## Key Design Ideas

- Hold the proposal format and scorer fixed across literature-access settings.
- Replay agent-retrieved references in the static format to separate evidence content from the retrieval process.
- Calibrate critic behavior against landmark papers and checks for incoherent or formulaic proposals.

## Strengths

- Separates published task coverage from the subset used for dense scoring.
- Reports controls and scoring boundaries alongside model differences.

## Limitations

- Scores remain model judgments; hypotheses are not experimentally validated.
- Active changes retrieval control, multi-turn interaction, and tool use together.
- The exploratory Scientific World Modeling gain does not survive both multiple-comparison correction and a compute-matched baseline.

## Related Works

- [IdeaBench](./ideabench.md)
- [LiveIdeaBench](./liveideabench.md)
