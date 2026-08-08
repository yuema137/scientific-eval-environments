# Energy Systems

> **English** | [简体中文](../zh/domains/energy_systems.md) · [← All domains](./README.md)

## Scope

Energy systems engineering: power, renewables, and energy research.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Energy is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| PowerAgentBench-SS | 2026 | Run power-system steady-state studies: contingency screening and admissible mitigations on grid cases. | Agentic tool-use studies over IEEE 39-bus operating-point variants with a DC thermal N-2 contingency-search pilot, under a validation budget. | A hidden evaluator recomputes physical validity; recall variants, false-safe penalties, severity regret, action cost, tool-use efficiency. | [→](../works/poweragentbench-ss.md) |

## Related Works

- [ResearchClawBench](../works/researchclawbench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
