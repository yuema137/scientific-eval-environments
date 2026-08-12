# Optimization & Engineering Design

> **English** | [简体中文](../zh/activities/optimization_engineering_design.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on searching for configurations, parameters, materials, structures, or designs that satisfy scientific or engineering objectives and constraints.

## Scope

Includes parameter and controller tuning, engineering and inverse design, materials and molecular design, and simulation-guided design-space search. It is **not** assigned simply because an underlying ML model is trained via optimization — optimization must be part of the evaluated agent task.

## Task Patterns

A large cluster targets **electronic and hardware design**. Analog work is covered by [AnalogCoder](../works/analogcoder.md) (training-free code-generation agent for analog circuits) and [AnalogXpert](../works/analogxpert.md) (SPICE-based topology synthesis via block selection and connection). Digital and hardware-code design spans [CVDP](../works/cvdp.md) (comprehensive RTL design, verification, and debugging) and [HLS-Eval](../works/hls-eval.md) (natural-language-to-HLS generation and optimization edits). Adjacent engineering-control and grid work includes [ControlAgent / ControlEval](../works/controleval.md) (iterative controller tuning to stability/performance specs) and [PowerAgentBench-SS](../works/poweragentbench-ss.md) (steady-state power-grid contingency screening and mitigation).

A second cluster is **molecular and drug design**, where instructions or targets admit many valid structures: [TOMG-Bench](../works/tomg-bench.md) (open-domain molecule editing, optimization, customized generation) and [SMDD-Bench](../works/smdd-bench.md) (budgeted multi-turn small-molecule drug design over protein targets). [Aviary](../works/aviary.md) contributes protein-engineering and molecular-cloning environments, and [SciAgentArena](../works/sciagentarena.md) includes optimization and drug-discovery task categories across biomedical fields.

A third cluster is **simulation-guided parameter tuning and iterative engineering design under simulator feedback**: [HydroAgent](../works/hydroagent.md) (calibrating an operational hydrologic model to maximize NSE), [SimulCost](../works/simulcost.md) (cost-aware parameter tuning across physics simulators), [Frontier-Eng](../works/frontier-eng.md) (iterative generative design under industrial-grade simulator reward and interaction budgets), [RE-Bench](../works/re-bench.md) (open-ended ML research-engineering optimization against reference solutions), and [EngDesign](../works/engdesign.md) (design artifacts across nine engineering areas checked by each area's own simulator, with up to ten feedback rounds).

A fourth cluster is **chemical-process design and plant-operation decisions**, where the design space is a flowsheet or an operating point rather than a controller or a molecule. [Simona](../works/simona.md) has agents choose unit operations and tune their configuration until the flowsheet converges, and the Parameter dimension of [CeProBench](../works/ceprobench.md) refines operating parameters against yield, purity, and cost objectives inside Aspen Plus. Two works move the decision from design time to run time, where a proposal is admissible only if an external validator clears it: the [fault-tolerant-control tutorial environments](../works/ctrl-alt-recover.md) ask for a recovery mode or a setpoint triple after an injected plant fault, and the [AAE framework](../works/aae-framework.md) grades proposed control actions by traversal of the plant's P&ID topology.

A fifth cluster is **civil and structural component design against codes and solvers**, where the deliverable is a member size or a foundation dimension that has to satisfy a design standard. [PE Civil Bench](../works/pe-civil-bench.md) proportions reinforced-concrete beams and columns and correlates the result against ETABS finite-element output; [the router multi-agent foundation study](../works/large-language-model-based-multi-agent-systems-for.md) sizes shallow footings and piles under given soil profiles, loads and safety factors; and [MASSE](../works/masse.md) determines section properties and returns a structural-adequacy verdict inside a consulting workflow.

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
| EngDesign | 2025 | Produce design artifacts verified by each area's own simulator | 101 tasks / 473 gradable items, 9 areas, up to 10 feedback rounds | Binary pass plus 0-100 score (34.38% first attempt, near 60% after 10) | [card](../works/engdesign.md) |
| HLS-Eval | 2025 | LLM generates and optimizes synthesizable HLS code | 94 HLS designs, NL-to-code and optimization edits | Parseable/compilable/runnable/synthesizable on Vitis HLS (pass@k) | [card](../works/hls-eval.md) |
| MASSE | 2025 | Determine section properties and verify structural adequacy | 100 racking-system problems, per-role rubric benchmarks, 10 trials each | SDAB rubric score (o4-mini 91.4) and pass/fail adequacy verdict | [card](../works/masse.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | Propose plant control actions checked against P&ID topology | 5 process-plant scenarios (3 Tennessee Eastman), B0-B3 context ladder, N=50 runs | Structurally admissible action; validator recall on 43 injected proposals | [card](../works/aae-framework.md) |
| Autonomous Fault-Tolerant Control Tutorial | 2026 | Select recovery mode and adapt setpoints after injected plant faults | Two executable environments (mixing module, CSTR) with typed fault injection | Validator-admissible recovery action; no reference scores reported | [card](../works/ctrl-alt-recover.md) |
| CeProBench | 2026 | Closed-loop optimization of process operating parameters | 20 Aspen Plus parameter files, 91 adjustable parameters, 65 objectives | Yield/purity/cost, Effective and Comprehensive Score, convergence iterations | [card](../works/ceprobench.md) |
| EnergyBridge | 2026 | Generate constraint-aware residential demand-response plans | VPP workflow over EnergyPlus models (Tianjin, Berlin) | Authorization rate plus capacity-commitment reliability | [card](../works/energybridge.md) |
| Frontier-Eng | 2026 | Iterative generative design under simulator feedback | 47 tasks, 5 engineering categories, bounded budget | Continuous reward under hard feasibility constraints | [card](../works/frontier-eng.md) |
| HydroAgent | 2026 | Agents calibrate operational CREST hydrologic model | 4 held-out gauges (329-40,792 km2), best-of-20 rounds | Nash-Sutcliffe Efficiency vs human-expert reference | [card](../works/hydroagent.md) |
| Multi-Agent Systems for Automated Foundation Design | 2026 | Size shallow footings and piles under given soils, loads and safety factors | 27 cases, 7 categories, router vs sequential workflows, 3 trials each | Four-criterion rubric grade (router with Grok 3: 95.00% / 90.63%) | [card](../works/large-language-model-based-multi-agent-systems-for.md) |
| PDAgent-Bench | 2026 | VLSI physical-design optimization under constraints | Full-flow implementation plus tasks; Innovus/ICC2/OpenROAD EDA | Timing closure and DRC-clean layout; pass@1/5 | [card](../works/pdagent-bench.md) |
| PE Civil Bench | 2026 | Design reinforced-concrete beams and columns for design-code compliance | 33 beam configurations plus a column extension; ETABS ground truth | Code compliance with r >= 0.90 agreement against finite-element results | [card](../works/pe-civil-bench.md) |
| PowerAgentBench-SS | 2026 | Agents screen contingencies and propose grid mitigations | IEEE 39-bus DC thermal N-2 search under validation budget | Hidden-evaluator recall, severity regret, residual violation | [card](../works/poweragentbench-ss.md) |
| SciAgentArena | 2026 | Biomedical research tasks including optimization and design |  | 200 stepwise-verified tasks across five biomedical fields | [card](../works/sciagentarena.md) |
| Simona | 2026 | Design flowsheet topology and tune unit-operation configurations | 1,000 expert-written process descriptions; simulator over HTTP APIs | Simulation Convergence Rate (80.3%) and design time | [card](../works/simona.md) |
| SimulCost | 2026 | Cost-aware parameter tuning of physics simulations | 2,947 single-round + 1,931 multi-round tasks, 13 simulators | Tuning quality under simulation-time/resource budget | [card](../works/simulcost.md) |
| SMDD-Bench | 2026 | Budgeted multi-turn small-molecule drug design | 502 solvable instances, 102 targets, five task types | Solve rate under oracle-call limit (GPT-5.4: 40.2%) | [card](../works/smdd-bench.md) |

## Related Works

- [PDAgent-Bench](../works/pdagent-bench.md)
- [EnergyBridge](../works/energybridge.md)
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
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [CeProBench](../works/ceprobench.md)
- [Simona](../works/simona.md)
- [EngDesign](../works/engdesign.md)
- [MASSE](../works/masse.md)
- [Large Language Model-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md)
- [PE Civil Bench](../works/pe-civil-bench.md)
