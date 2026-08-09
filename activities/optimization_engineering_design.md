# Optimization & Engineering Design

> **English** | [简体中文](../zh/activities/optimization_engineering_design.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on searching for configurations, parameters, materials, structures, or designs that satisfy scientific or engineering objectives and constraints.

## Scope

Includes parameter and controller tuning, engineering and inverse design, materials and molecular design, and simulation-guided design-space search. It is **not** assigned simply because an underlying ML model is trained via optimization — optimization must be part of the evaluated agent task.

## Task Patterns

A large cluster targets **electronic and hardware design**. Analog work is covered by [AnalogCoder](../works/analogcoder.md) (training-free code-generation agent for analog circuits) and [AnalogXpert](../works/analogxpert.md) (SPICE-based topology synthesis via block selection and connection). Digital and hardware-code design spans [CVDP](../works/cvdp.md) (comprehensive RTL design, verification, and debugging) and [HLS-Eval](../works/hls-eval.md) (natural-language-to-HLS generation and optimization edits). Adjacent engineering-control and grid work includes [ControlAgent / ControlEval](../works/controleval.md) (iterative controller tuning to stability/performance specs) and [PowerAgentBench-SS](../works/poweragentbench-ss.md) (steady-state power-grid contingency screening and mitigation).

A second cluster is **molecular and drug design**, where instructions or targets admit many valid structures: [TOMG-Bench](../works/tomg-bench.md) (open-domain molecule editing, optimization, customized generation) and [SMDD-Bench](../works/smdd-bench.md) (budgeted multi-turn small-molecule drug design over protein targets). [Aviary](../works/aviary.md) contributes protein-engineering and molecular-cloning environments, and [SciAgentArena](../works/sciagentarena.md) includes optimization and drug-discovery task categories across biomedical fields.

A third cluster is **simulation-guided parameter tuning and iterative engineering design under simulator feedback**: [HydroAgent](../works/hydroagent.md) (calibrating an operational hydrologic model to maximize NSE), [SimulCost](../works/simulcost.md) (cost-aware parameter tuning across physics simulators), [Frontier-Eng](../works/frontier-eng.md) (iterative generative design under industrial-grade simulator reward and interaction budgets), and [RE-Bench](../works/re-bench.md) (open-ended ML research-engineering optimization against reference solutions).

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AnalogCoder | 2024 | Training-free LLM agent designs analog circuits via Python code | Analog circuit design, self-correcting flow (24 tasks) | Successfully design circuits; 20 of 24 vs GPT-4o's 15 | [card](../works/analogcoder.md) |
| AnalogXpert | 2024 | Analog topology synthesis via block selection and connection | SPICE-code topology synthesis (30 real + 2,000 synthetic) | 40% synthetic / 23% real success vs GPT-4o's 3% | [card](../works/analogxpert.md) |
| Aviary | 2024 | Scientific agent environments for cloning and protein engineering | Language-grounded POMDP environments (SeqQA, protein stability, 40 proteins) | Match/exceed frontier agents and human experts | [card](../works/aviary.md) |
| ControlAgent / ControlEval | 2024 | Multi-agent LLM iteratively tunes controller parameters | 500 control-system design tasks across system types | High success rate meeting settling-time/phase-margin specs | [card](../works/controleval.md) |
| RE-Bench | 2024 | Agents optimize ML research-engineering code and kernels | 7 open-ended ML R&D environments, 2/8/32h budgets | Score vs reference solutions and human experts | [card](../works/re-bench.md) |
| Speak-to-Structure / TOMG-Bench | 2024 | Natural-language-driven open-domain molecule generation | MolEdit/MolOpt/MolCustom, 5,000 samples per subtask | Instruction-satisfying valid molecule (one-to-many) | [card](../works/tomg-bench.md) |
| CVDP | 2025 | RTL design, verification, and debugging of Verilog | 783 problems, 13 categories, agentic and non-agentic | Pass@1 on generation (SOTA <=34%) | [card](../works/cvdp.md) |
| HLS-Eval | 2025 | LLM generates and optimizes synthesizable HLS code | 94 HLS designs, NL-to-code and optimization edits | Parseable/compilable/runnable/synthesizable on Vitis HLS (pass@k) | [card](../works/hls-eval.md) |
| Frontier-Eng | 2026 | Iterative generative design under simulator feedback | 47 tasks, 5 engineering categories, bounded budget | Continuous reward under hard feasibility constraints | [card](../works/frontier-eng.md) |
| HydroAgent | 2026 | Agents calibrate operational CREST hydrologic model | 4 held-out gauges (329-40,792 km2), best-of-20 rounds | Nash-Sutcliffe Efficiency vs human-expert reference | [card](../works/hydroagent.md) |
| PowerAgentBench-SS | 2026 | Agents screen contingencies and propose grid mitigations | IEEE 39-bus DC thermal N-2 search under validation budget | Hidden-evaluator recall, severity regret, residual violation | [card](../works/poweragentbench-ss.md) |
| SciAgentArena | 2026 | Biomedical research tasks including optimization and design |  | 200 stepwise-verified tasks across five biomedical fields | [card](../works/sciagentarena.md) |
| SimulCost | 2026 | Cost-aware parameter tuning of physics simulations | 2,947 single-round + 1,931 multi-round tasks, 13 simulators | Tuning quality under simulation-time/resource budget | [card](../works/simulcost.md) |
| SMDD-Bench | 2026 | Budgeted multi-turn small-molecule drug design | 502 solvable instances, 102 targets, five task types | Solve rate under oracle-call limit (GPT-5.4: 40.2%) | [card](../works/smdd-bench.md) |

## Related Works

- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [Aviary](../works/aviary.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [RE-Bench](../works/re-bench.md)
- [Speak-to-Structure / TOMG-Bench](../works/tomg-bench.md)
- [CVDP](../works/cvdp.md)
- [HLS-Eval](../works/hls-eval.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [HydroAgent](../works/hydroagent.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [SciAgentArena](../works/sciagentarena.md)
- [SimulCost](../works/simulcost.md)
- [SMDD-Bench](../works/smdd-bench.md)
