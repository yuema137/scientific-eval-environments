# SimAgents (2025)

> **English** | [简体中文](../zh/works/simagents.md)

## Overview

SimAgents is a multi-agent LLM system that reads cosmological simulation papers and reconstructs the simulation's configuration parameters in a form the simulation software will accept, released together with a manually annotated evaluation dataset of more than 40 published simulations and a parameter-level scoring protocol against single-agent baselines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.08958>
- **Code:** <https://github.com/xwzhang98/SimAgents>
- **Demo:** <https://youtu.be/w1zLpm_CaWA>

## Summary

The paper starts from a concrete bottleneck in computational cosmology: the parameters needed to reproduce a published simulation are scattered through dense prose in different models and formats, and translating them into an executable configuration is slow and error-prone. SimAgents assigns the task to specialised agents that collaborate through structured discussion — a Physics Agent that interprets the paper with domain knowledge, a Software Agent that enforces the constraints written in the simulation code's user manual, and an Analysis Code Writer that produces visualisation and preliminary-analysis code once the configuration is fixed. To measure whether the extracted configurations are correct, the authors build an evaluation dataset by collecting more than 40 simulations from arXiv and from journals including ApJ and MNRAS and hand-annotating every relevant parameter/value pair, then score SimAgents against chain-of-thought and exchange-of-thought baselines under both human and automatic grading.

## Tasks

More than 40 simulations drawn from published papers on arXiv and in leading journals (ApJ, MNRAS are named), covering diverse simulation types. Each paper is manually annotated with all parameter/value pairs relevant to MP-Gadget: cosmological parameters (Ωm, Ωb, ΩΛ, h, σ8, ns), initial-condition settings (BoxSize, Ngrid, Redshift) and key model switches. The agent's task is to read the paper and emit the corresponding parameter set, subject to the constraints of the simulation software's user manual; a second module then generates Python code for power-spectrum visualisation, 3D density-field plotting and preliminary statistical analysis of the resulting simulation output. The released repository ships the annotations as a `golden_standard` directory covering validated parameters from major cosmological simulation projects including IllustrisTNG, Millennium, MTNG, Magneticum and SIMBA. MP-Gadget is the only simulation code supported in this work.

## Domains

Astronomy. The evaluated objective is the configuration of cosmological simulations: the annotated ground truth consists of cosmological parameters (matter, baryon and dark-energy density, Hubble parameter, σ8, spectral index) and initial-condition settings for MP-Gadget, and the reference simulations are established cosmological structure-formation suites. Physics is a secondary co-domain through the cosmological model the parameters describe.

## Evaluation

Scoring is at the parameter level. Extracted parameter/value pairs are matched against the manual annotations to give true positives, false positives and false negatives, from which precision, recall and micro-F1 are computed; a separate error taxonomy counts Value Errors, Type Errors and Hallucinations as an average number of errors per simulation. Two baselines are compared under identical conditions: zero-shot chain-of-thought prompting with a single LLM agent (CoT) and exchange-of-thought with two identically initialised agents in discussion (EoT). Under human evaluation (Table 1), SimAgents reaches 98.67% micro-F1 with 97.80% precision and 99.55% recall, against 93.64/92.46/94.84 for CoT and 94.95/93.87/96.05 for EoT. On the error taxonomy (Table 2), SimAgents averages 0.46 Value Errors, 0.02 Type Errors and 0.30 Hallucinations per simulation, against 0.97/0.51/0.21 for CoT and 1.21/0.21/0.34 for EoT. Automatic evaluation gives slightly lower figures for SimAgents: 98.13% micro-F1, 97.77% precision, 98.50% recall. GPT-4 is the primary backbone; a Qwen3-4B ablation degrades to 81.23% micro-F1 with 3.05 Value Errors and 2.59 Type Errors per simulation.

## Typical Duration

No wall-clock or token budget is reported. The interaction budget is instead reported as rounds of structured discussion between the Physics and Software agents: an ablation over one to four rounds finds that two iterations yield the highest micro-F1, with additional rounds not improving the result.

## Main Contribution

A task-specialised multi-agent decomposition for turning published cosmological simulation descriptions into software-compliant executable configurations, in which one agent carries physics reasoning and a separate agent enforces the simulation code's own constraints, together with a manually annotated cosmological parameter-extraction evaluation dataset and the measurement showing that this specialised division outperforms both single-agent chain-of-thought and symmetric two-agent discussion.

## Key Design Ideas

- The two extraction agents are asymmetric by construction: the Physics Agent supplies domain interpretation while the Software Agent supplies manual-derived validity constraints, which is the difference the exchange-of-thought baseline isolates.
- Structured multi-round communication rather than a single pass, with the number of rounds treated as a tunable and empirically settled at two.
- Software compliance is a scored property, not a post-hoc filter — Type Errors are counted separately from Value Errors so that physically plausible but software-invalid outputs are visible.
- Hallucination is counted as its own error class, distinguishing invented parameters from misread values.
- Ground truth is human-annotated per paper rather than derived from a model, and released alongside the system.
- Both human and automatic grading of the same outputs are reported, so the gap between them is measurable rather than assumed.
- The pipeline continues past configuration into generated analysis code (power spectra, 3D density fields), closing the loop from paper to runnable analysis.

## Strengths

- The evaluation dataset is manually annotated, publicly released and drawn from real published simulations rather than synthesised.
- Baselines are genuine external comparators (chain-of-thought and exchange-of-thought), not only ablations of the proposed system.
- The error taxonomy separates failure modes that a single F1 number would conflate, and the hallucination count is reported even where SimAgents is not the best performer on it.
- A small-backbone ablation (Qwen3-4B versus GPT-4) quantifies how much of the result depends on the frontier model rather than on the architecture.
- Human and automatic evaluation are both reported and agree closely, which supports the automatic protocol as a reusable scorer.

## Limitations

- The authors state that, due to time constraints, only one version of the executable files from the literature was annotated, and that more data points and executable versions remain to be added.
- Support is limited to a small number of pre-trained models and to MP-Gadget as the only simulation software; the authors list broader software and model coverage as future work.
- Repository note: the evaluation dataset is small — more than 40 simulations — and is not given a distinct name, so it functions as a validation set for this system rather than as a standing benchmark.
- Repository note: only parameter extraction is scored. The analysis-code-generation module and the correctness of any simulation actually run from the extracted configuration are demonstrated but not evaluated, so end-to-end reproduction of a published simulation is not measured.
- Repository note: reported micro-F1 values sit above 98% for the proposed system, leaving little headroom to discriminate future methods on this dataset.
- Repository note: no venue is recorded for the paper, and the released repository carries no link back to the publication.

## Related Works

- [CosmoPaperQA](./cosmopaperqa.md) — also evaluates LLM systems on extracting scientific content from cosmology papers, scored as question answering rather than as an executable configuration.
- [ReplicationBench](./replicationbench.md) — astrophysics replication tasks, sharing the goal of recovering a published result from its written description.
- [HiSciBench](./hiscibench.md) — includes literature-extraction and data-driven discovery levels over astronomy and other disciplines.
- [ScienceAgentBench](./scienceagentbench.md) — scores agents on producing runnable scientific analysis code from task descriptions.
- [gwBenchmarks](./gwbenchmarks.md) — another astrophysics setting where agents must satisfy domain software and precision constraints rather than produce prose.
