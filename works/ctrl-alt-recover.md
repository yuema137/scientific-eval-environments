# A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents (2026)

> **English** | [简体中文](../zh/works/ctrl-alt-recover.md)

> **First appeared:** 2026-06-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.31635)

## Overview

A tutorial paper on using LLM agents as constrained supervisory planners for fault recovery in process plants, released with two openly available executable Python environments — a modular mixing module and a continuous stirred-tank reactor — that expose configurable faults and pluggable interfaces for custom recovery and validation methods.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.31635
- **Code:** https://github.com/AISL-at-Imperial-College-London/ctrl-alt-recover
- **Venue:** arXiv preprint (eess.SY), submitted 30 June 2026

## Summary

Fault recovery in process plants still depends on operators who read alarms, procedures, P&IDs, interlocks, and process trends and then decide how to move the plant to a safe operating mode without triggering a shutdown. The paper frames the LLM as a constrained supervisory planner: it proposes recovery actions from plant-specific knowledge, and every proposal is checked by an external validator — symbolic or simulation-based — before actuation. Around that framing it develops three design dimensions: the recovery patterns for which LLM agents are useful, the validation strategies that separate admissible from inadmissible proposals, and the deployment constraints imposed by latency, knowledge engineering, safety integration, and model lifecycle management. To make the framework directly usable, the paper ships two executable environments that re-implement established case studies with configurable faults and defined interfaces for plugging in custom recovery and validation logic.

## Tasks

Two executable environments, distributed as a single repository. The **mixing module** is a discrete supervisory-routing problem over three batch tanks (B201–B203) and a collection tank (B204) modelled as a state machine with on–off valves and two pumps; observable signals are tank levels, current state, and active actuator configuration, and the recovery interface consumes a typed fault and returns a target state with an actuator set. Its injectable faults are pump failure, pump degradation, a clogged main line, a leak, and a sensor fault — the first four render the main-pump emptying path unusable while a sensor fault leaves the main route valid. The **continuous stirred-tank reactor** is a continuous setpoint-adaptation problem; observable signals are temperature, level, inlet/outlet/cooling flows, actuator positions, and a mass-balance residual, and the recovery interface consumes a process snapshot plus fault context and returns a setpoint triple. Its injectable faults are fouling (gradual loss of heat-transfer capability), pump degradation (reduced outlet-flow authority causing the level to drift), and a cooling valve constrained near its closed position. The paper does not define a fixed task list or split — the environments are parameterised generators of fault scenarios rather than a frozen task set.

## Domains

Chemical Engineering — process-plant operations and process control: supervisory fault handling and recovery on a modular batch mixing unit and on a continuous stirred-tank reactor, with faults (clogging, leakage, pump degradation, heat-exchanger fouling, cooling-valve saturation) drawn from process-equipment failure modes and recovery expressed as operating-mode changes and setpoint adjustments.

## Evaluation

Correctness is judged per proposed action rather than by a task score. A **symbolic validator** checks a proposal against plant structure — whether the next state is reachable and whether the named actuators exist — and is deterministic and catches all admissibility violations, but does not see dynamics. A **simulation-based validator** clones the plant state into a digital twin, applies the action, and rolls the dynamics forward, accepting only if the rollout meets criteria such as bounded unsafe exposure. Runtime monitoring is added to detect deviations between the predicted and the actual trajectory. Both environments record the fault context, the proposed action, the validator verdict, and the resulting trajectory, so runs are auditable. The paper reports no quantitative model scores: it states that "rather than reporting performance figures, this paper focuses on what must be considered and tested when adapting such a framework to one's own application," and names no evaluated LLMs.

## Typical Duration

No per-task token or wall-clock budget is reported. Latency is treated as a deployment constraint set by process dynamics rather than by the model: the paper notes that batch and slow supervisory tasks, with per-decision latency budgets of tens of seconds, tolerate cloud LLMs comfortably, while cloud hosting adds network latency that on-premise or edge models remove at the cost of lower reasoning capability.

## Main Contribution

A tutorial treatment of LLM agents for autonomous fault-tolerant control that organises the design space into three dimensions — recovery patterns, validation strategies, and deployment constraints — and grounds it in two openly available executable environments extended with configurable faults and defined interfaces so that custom recovery and validation methods can be plugged in and tested.

## Key Design Ideas

- The LLM is a constrained supervisory planner, never the execution authority: every proposal passes through a validator before actuation, and every proposal is logged as a structured action so the decision trace can be audited.
- Recovery is classified into Pattern A (discrete supervisory routing — selecting a discrete operating mode from a finite state machine, where route selection benefits from natural-language fault semantics), Pattern B (continuous setpoint adaptation — adjusting a small set of supervisory setpoints over bounded ranges and discrete increments rather than reconfiguring low-level loops), and Pattern C (hybrid recovery, where a fault first triggers a mode change and then requires re-tuning setpoints within the new mode).
- Two complementary validator classes with an explicit trade-off: symbolic validation is deterministic and complete on admissibility but blind to dynamics; simulation-based validation rolls the dynamics forward in a digital twin and accepts only bounded unsafe exposure.
- The two shipped environments instantiate Pattern A and Pattern B respectively, so each design dimension has a runnable counterpart.
- Deployment is treated as first-class: the knowledge graph grounding the LLM is identified as the dominant deployment cost for a new plant, and model lifecycle management pins and logs the model identifier with every decision while replaying a regression suite of recorded fault scenarios on every update.

## Strengths

- The environments are openly available under an MIT license with a documented CLI, recorded decision traces, and per-run result files, making the fault scenarios re-runnable by third parties.
- Fault injection is explicit and typed, and the paper states which faults invalidate the nominal route and which do not — the ground truth for a recovery decision is therefore derivable rather than judgemental.
- Validation is separated from generation through a defined interface, so alternative recovery policies and alternative validators can be swapped in independently.
- Two structurally different control regimes (discrete state-machine routing and continuous setpoint adaptation) are covered rather than one.

## Limitations

- No performance figures, metrics, task counts, or evaluated models are reported; the paper is explicit that this is out of its scope, so it supplies an environment and a methodology but no leaderboard or reference results.
- Only two case studies, both small single units, and both re-implementations of previously published case studies rather than plant-scale settings.
- Repository note: because no fixed task list, split, or scoring protocol is defined, results produced in these environments are not automatically comparable across papers — the scenario configuration and acceptance criteria have to be fixed by whoever runs them.
- Repository note: the shipped repository requires a GraphDB instance with the supplied knowledge graphs and an external `mixer_module` package in addition to an LLM endpoint, which raises the setup cost relative to a self-contained benchmark harness.
- Repository note: the same repository is cited by the authors' companion framework paper (arXiv:2606.28011), so the environments and the system evaluated in them share an implementation lineage rather than being independent.

## Related Works

- [CRAFTS](./crafts.md) — chemical-process-simulation agent evaluation on IDAES/Pyomo, the model-construction counterpart to this work's plant-operation setting.
- [ControlAgent / ControlEval](./controleval.md) — LLM agents evaluated on control-system design tasks, a design-time analogue to this work's run-time supervisory recovery.
