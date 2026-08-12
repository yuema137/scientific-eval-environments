# Energy Systems

> **English** | [简体中文](../zh/domains/energy_systems.md) · [← All domains](./README.md)

## Scope

Energy systems engineering: power, renewables, and energy research.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Energy is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| PowerAgentBench-SS | 2026 | Run power-system steady-state studies: contingency screening and admissible mitigations on grid cases. | Agentic tool-use studies over IEEE 39-bus operating-point variants with a DC thermal N-2 contingency-search pilot, under a validation budget. | A hidden evaluator recomputes physical validity; recall variants, false-safe penalties, severity regret, action cost, tool-use efficiency. | [→](../works/poweragentbench-ss.md) |
| ElecBench | 2024 | Reason about power-grid operation and dispatch under stability, security, and economic constraints. | Power-dispatch evaluation across general-knowledge and professional-business scenarios; 8 LLMs. | Six metrics (factuality, logicality, stability, security, fairness, expressiveness) / 24 sub-metrics. | [→](../works/elecbench.md) |
| EnergyBridge | 2026 | Residential virtual-power-plant operation and demand response — convert household physical flexibility into dependable, authorized grid capacity by coupling capacity reporting, household authorization, and physical execution of HVAC/EV/appliance load shifting. | 50 seven-day EnergyPlus building-energy simulations across five households, two regions (Tianjin, Berlin), and five methods (350 household-day episodes; one 18:00–19:00 demand-response event each), plus a held-out capacity-reporting audit; an LLM User Participation Simulator decides authorization. | Physical outcomes metered from EnergyPlus 24.1.0 — gate-acceptance (authorization) rate, event-window energy, and capacity-commitment reliability (accepted ∧ delivery within ±20% of the commitment); the authorization simulator validated against 584 human role-play responses (5.3-pp mean absolute acceptance error). | [→](../works/energybridge.md) |

## Related Works

- [EnergyBridge](../works/energybridge.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [ElecBench](../works/elecbench.md)
