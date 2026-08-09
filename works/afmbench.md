# AFMBench (2025)

> **English** | [简体中文](../zh/works/afmbench.md)

## Overview

AFMBench is an evaluation suite of 100 expertly curated tasks that requires LLM agents to operate a real atomic force microscope rather than a simulator, spanning the workflow from experimental design through results analysis. It is documented here for AFMBench, the paper's *evaluation* contribution; the accompanying AILA framework is agent-implementation work adjacent to this repository's evaluation focus (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Laboratory & Instrument Control](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** <https://www.nature.com/articles/s41467-025-64105-7>
- **Venue:** Nature Communications 16:9104

## Summary

The authors argue that domain question-answering benchmarks do not establish whether a model can run a laboratory instrument, and that simulation-based evaluation omits the temporal constraints and experimental variability of real hardware. AFMBench therefore holds the agent to physical execution on a Nanosurf DriveAFM reached through a Python API, with four interchangeable LLMs swapped into a fixed harness and every task run three times. The headline result supports the authors' concern: Claude-3.5-Sonnet, strong on materials-science question answering, carries a 51.6% error rate here, and the best model reaches 65% overall task completion while dropping to 23.3% on tasks that merge documentation with analysis.

## Tasks

100 expertly curated experimental tasks, stratified along four independent axes: tool coordination (69% requiring multiple tools, 31% single-tool), agent requirement (83% single-agent, 17% multi-agent), complexity (56% basic operations, 44% advanced procedures), and functional domain (50 documentation tasks, 14 analysis tasks, 10 calculation tasks, with the remainder integrating more than one domain). Task content ranges over microscope calibration, feature detection, mechanical-property measurement, graphene layer counting, and indenter detection.

## Domains

Scanning-probe microscopy of materials — operating an atomic force microscope for imaging, mechanical characterization, and image analysis.

## Evaluation

- **Physical execution on real hardware.** Tasks are performed on a Nanosurf DriveAFM through a Python-based API; the paper distinguishes this from conventional LLM benchmarks and simulation-based evaluation on the grounds that hardware imposes real temporal constraints and experimental variability.
- **Task completion success rate**, reported per functional domain and for merged multi-domain tasks, over three independent trials per model–task pair.
- **A named failure taxonomy.** Errors are classified as sleepwalking (performing unauthorized actions beyond the specified instructions), code-generation errors, agent-selection errors, tool-selection errors, and instruction-adherence failures that exceed stated operational limits.
- **Operational metrics reported alongside success.** AFM-handler and data-handler calls, number of steps, total, prompt and completion tokens, tokens per stage, latency, time per step, and latency per thousand tokens.
- **Reported.** GPT-4o leads with 65% overall task completion and a 29% error rate — 88.3% on documentation, 56.7% on calculations, 33.3% on analysis, falling to 23.3% on merged documentation-and-analysis tasks. GPT-3.5-turbo-0125 reaches 32.8% overall with a 66.6% error rate and 3.3% on mathematical operations; Claude-3.5-Sonnet-20241022 scores 85.3% on standalone documentation but carries a 51.6% error rate, records the highest mean response time at 17.31 seconds, and fails all three trials involving the data-handler agent; Llama-3.3-70B-versatile carries a 60.6% error rate with 32% code-generation errors. The authors also report that multi-agent configurations outperform single-agent ones and that both remain sensitive to prompt variation.

## Typical Duration

No per-task step, token, or wall-clock budget is imposed. The paper instead reports observed cost as an outcome: mean steps per task range from 6 for GPT-4o to 10 for Llama-3.3-70B, and mean response time from 7 seconds for Llama-3.3-70B to 17.31 seconds for Claude-3.5-Sonnet. Because the tasks execute on an instrument, elapsed time reflects physical operations rather than inference alone.

## Main Contribution

An evaluation suite that holds LLM agents to physical execution on a real scanning-probe microscope across a full experimental workflow, together with a failure taxonomy for laboratory settings in which exceeding an instruction is a distinct and consequential error class.

## Key Design Ideas

- Physical execution on an instrument as a requirement rather than a simulated stand-in, so that temporal constraints and experimental variability are part of what the benchmark measures.
- Task composition stratified along four orthogonal axes — tool count, agent count, complexity, and functional domain — which lets a failure be attributed to a specific dimension rather than to task difficulty in general.
- Merged multi-domain tasks reported separately from their single-domain components, isolating a composition penalty that per-domain rates conceal.
- Over-execution treated as a first-class failure mode under the name sleepwalking, on the reasoning that an agent exceeding its instructions on an actuator is a safety concern rather than a scoring nuisance.

## Strengths

- The design directly tests a claim the field usually assumes: the paper shows that materials-science question-answering proficiency does not transfer to operating the instrument, with Claude-3.5-Sonnet as the specific counterexample.
- Reporting an error taxonomy rather than a single success rate separates models that fail by writing broken code from those that fail by choosing the wrong agent or tool.
- Operational cost is reported per model as steps, tokens, and latency, so capability and expense are visible together rather than requiring a separate study.

## Limitations

- Repository note: The paper's other contribution is AILA, an LLM-powered framework for automating atomic force microscopy — agent-implementation work that sits outside this repository's evaluation-centric scope. It is included for AFMBench, its evaluation suite; the framework itself is not the reason for inclusion.
- Repository note: Evaluation runs on a single instrument in a single laboratory at three trials per task, so the reported rates cannot be reproduced without that hardware, and physical execution bounds how much statistical power is affordable. The paper does not state a criterion for judging task success, so what counts as a completed task is not recoverable from the reported material.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also scores scientific workflows by execution rather than by answer matching, but verifies deterministically with pytest inside containers, where AFMBench's outcome depends on an instrument and is therefore not deterministic.
- [ScienceAgentBench](./scienceagentbench.md) — Also draws tasks from real scientific practice and grades by running the agent's output, but its tasks resolve to self-contained Python programs, so nothing physical is exercised.
- [Aviary](./aviary.md) — Also offers laboratory-flavored scientific environments including molecular cloning and protein engineering, but those environments are computational surfaces rather than a controlled physical instrument.
