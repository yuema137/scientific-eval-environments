# AutoBM / BMEval (2026)

> **English** | [简体中文](../zh/works/autobm.md)

> **First appeared:** 2026-02-06 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2602.07083)

## Overview

AutoBM defines the task of generating executable, physically consistent OpenSeesPy building-model code from a
natural-language structural specification, and BMEval is the accompanying verification-driven benchmark of
128 expert-validated modelling tasks scored by sandbox execution, fundamental-period agreement, and
design-code compliance.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2602.07083
- **Code:** https://github.com/Jovanqing/AutoBM
- **Venue:** KDD 2026 (32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining), DOI
  10.1145/3770855.3818987

## Summary

The paper formalizes Automatic Building Modeling (AutoBM) as conditional program synthesis: given a
structural description (building function, plan dimensions, storey heights, seismic intensity), a set of
physical and engineering constraints, and a target modelling API, a model must emit OpenSeesPy code whose
execution yields a physically valid structural response. Around this task it releases three artefacts — the
CivilInstruct instruction corpus, the BMEval evaluation benchmark, and RLA-SPC, a two-stage supervised
fine-tuning plus physics-constrained GRPO alignment procedure. Sixteen open-source and commercial LLMs are
scored on BMEval under a unified protocol, and the fine-tuning results are reported as before/after
comparisons on the same benchmark.

## Tasks

BMEval contains 128 labelled evaluation samples. Construction proceeded in three stages: building samples
were randomly generated across a diverse attribute space (building function, floor height, plan dimensions)
within a reasonable structural parameter range; an expert-driven mechanism then optimized and validated every
design solution in strict accordance with seismic design codes to guarantee structural feasibility; and
empirical formulas supplied the fundamental period of each structure as the ground-truth reference value.
Each sample carries complete building information plus its corresponding structural period. The separate
CivilInstruct training corpus is built in four parts — roughly 3,800 API-learning samples synthesized from
OpenSeesPy documentation, 3,100 expert-level instruction–code instances, 3,500 execution-error debugging
chain-of-thought samples, and 512 physics-informed expert samples scoring above 90/100 and annotated with
finite-element structural periods. Generated programs typically run to about 600 lines covering modelling,
analysis, and validation.

## Domains

Civil & Structural Engineering. Every evaluated instance is a building: the model must lay out nodes and
elements for a reinforced-concrete frame, assign sections and materials, apply loads consistent with the
stated seismic intensity, run modal analysis to obtain the first-order natural vibration period, and print a
verification conclusion against design specifications. Domain knowledge from Chinese seismic and concrete
design codes — GB 50011-2010, GB 50010-2010 and JGJ 3-2010 — is embedded in the prompt template, and
JGJ/T 415-2017 informs the data-construction practice. This is earthquake engineering applied to a structure,
not seismic hazard science; no co-domain is claimed, since the code-generation framing serves a structural
objective rather than being a general software-engineering task.

## Evaluation

Each test sample is attempted with n independently generated candidate programs, executed sequentially in a
restricted sandbox; a program counts as successful if it terminates normally within the prescribed time
limit. The unbiased pass@k estimator from HumanEval/MBPP is applied, and three task-specific variants are
layered on top. Pass@k_period requires the first-order natural vibration period extracted from program output
by deterministic rule-based matching to fall within a relative error threshold of 0.30 against the
ground-truth value. Pass@k_compliance requires the output to state an explicit conclusion satisfying design
verification criteria, detected by a conservative keyword-matching strategy with negation handling.
Pass@k_strict requires all three simultaneously: clean execution, period within tolerance, and an explicit
compliance conclusion. Results are averaged over five perturbed evaluations of BMEval with standard
deviations reported. Best reported scores are Claude-Sonnet-4.5 at 52.34 Pass@1, 80.16 Pass@5 and 17.97
Pass@5_strict, and Gemini-3-pro-Preview at 32.03 Pass@5_period; every code-specialist 7B–8B model scores
below 3.0 on the engineering-level average, and GLM-4.6 records 0.00 Pass@5_strict.

## Typical Duration

N/A — the paper reports no per-task wall-clock or token budget. The only stated execution constraint is a
prescribed sandbox time limit after which a run is scored as a timeout, and generated programs are
characterized as roughly 600 lines each.

## Main Contribution

The authors propose a physics-aware LLM framework for automatic building modelling comprising the
CivilInstruct domain dataset, a two-stage fine-tuning strategy guided by structural and physical constraints,
and BMEval as a verification-driven benchmark providing engineering-relevant assessment of executability and
structural dynamics consistency through closed-loop validation.

## Key Design Ideas

- Correctness is defined by closed-loop simulation rather than text similarity: the generated program is
  actually executed in an OpenSees sandbox and its modal output compared against a reference period.
- The metric ladder separates three distinct failure surfaces — does it run, is it numerically right, does it
  reach a compliance verdict — and Pass@k_strict conjoins all three.
- Ground-truth periods come from expert-validated designs computed with empirical formulas, giving a
  quantitative physical target rather than a rubric judgement.
- The tolerance-based period reward mirrors engineering practice, awarding graded credit at 10%, 20% and 40%
  relative-error bands rather than a single pass/fail cut.
- Training rewards decompose into format compliance (weight 0.05), a hierarchical-AST logical-completeness
  term over three tiers of OpenSeesPy APIs — topology, boundary/load, analysis/solver — (0.25), and
  sandbox execution (0.70).
- Debugging data is bug-driven: 3,500 chain-of-thought samples are derived from real execution failures
  arising from coupled OpenSeesPy API, solver, and modelling-logic interactions rather than synthetic defects.

## Strengths

- Grounds scoring in an executed physical quantity — the fundamental period — instead of judging generated
  code by textual or LLM-judge proxies.
- Wide model coverage: sixteen systems spanning code specialists, open-weight generalists, and frontier
  reasoning models, each with standard deviations over five perturbed evaluations.
- The benchmark clearly separates model capability from framework capability, since it is applied identically
  to untuned baselines and to the fine-tuned checkpoints.
- Failure-mode analysis is reported by category, identifying unterminated string literals as 95.7% of
  executability failures and drift-limit violations as the dominant compliance failure.
- Design-code provenance is explicit, naming the specific Chinese standards embedded in the task.

## Limitations

- The framework is restricted to elastic structural analysis and simplified 2D reinforced-concrete frames;
  nonlinear analysis and 3D interaction are not incorporated.
- Development is anchored on Chinese seismic design specifications, and generalizability to other
  international design codes is not systematically validated.
- Compliance detection relies on conservative keyword matching over the program's printed conclusion, so it
  scores whether a verdict is stated in recognizable terms rather than independently recomputing the check.
- The authors note that hidden engineering defects may still arise under complex conditions and position
  AutoBM as assisting rather than replacing professional design, expert review, or regulatory verification.
- Repository note: the paper's own naming is inconsistent, using BMEval, MBEval and BMBench for the same
  benchmark in the abstract, section heading and body; BMEval is the form used in the results tables.
- Repository note: absolute scores are low across the board — the strongest model reaches 17.97 on the strict
  joint metric — so the benchmark currently discriminates mainly at the bottom of the difficulty range.

## Related Works

- [MASSE](./masse.md) — also evaluates LLM-driven OpenSeesPy structural modelling, but scores rubric-graded
  workflow logs via an LLM judge rather than executed modal output.
- [StructureClaw](./structureclaw.md) — structural-engineering agent benchmark verifying structural-model
  matching and numerical agreement against frozen reference solver responses.
- [FEM-Bench](./fem-bench.md) — code-generating LLM benchmark in computational mechanics with objective
  unit-test verification.
- [FEABench](./feabench.md) — finite-element agent benchmark operating COMSOL through its API.
- [CodePDE](./codepde.md) — executable scientific-code generation scored by running the produced solver.
