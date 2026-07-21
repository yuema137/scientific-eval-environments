# Scientific Agent Benchmarks

## Definition

Scientific agent benchmarks evaluate AI agents on tasks drawn from scientific research and practice — computational workflows, parameter tuning, literature-grounded problems, or replication of published results. What distinguishes them from general-purpose agent benchmarks is the source of tasks (real scientific work) and the standard for correctness (matching published or expert-defined outcomes).

## Motivation

Scientific work has features that generic agent benchmarks under-model: intermediate evaluation may be expensive (simulations, experiments), tasks are often long-horizon, correctness must sometimes be validated against a published or expert reference rather than a synthetic ground truth, and workflows involve heterogeneous tools that require domain knowledge to sequence correctly. A separate topic exists because scoring scientific agents demands attention to these features.

## Existing Approaches

- **Executable scientific workflows.** [Terminal-Bench Science](../works/terminal-bench-science.md) evaluates AI agents on real computational workflows drawn from natural-science research, verified with pytest inside containers, across five scientific domains.
- **Publication-anchored difficulty.** [NatureBench](../works/naturebench.md) distills 90 tasks from Nature-family publications and asks whether coding agents can match the published SOTA. It exposes a gap: strongest models exceed published performance on only 17.8% of tasks.
- **Expert-validated, execution-based tasks.** [ScienceAgentBench](../works/scienceagentbench.md) extracts 102 tasks from 44 peer-reviewed publications across four disciplines, engages nine subject matter experts to validate them, and unifies every task's output to a self-contained Python program scored on program, execution result, and cost. It insists on assessing individual workflow tasks before claiming end-to-end automation, and reports a low best-agent solve rate (32.4% independently, 34.3% with expert-provided knowledge).
- **End-to-end research lifecycle.** [AIRS-Bench](../works/airs-bench.md) provides 20 frontier research-science tasks without baseline code, requiring agents to construct workflows from scratch across language modeling, mathematics, bioinformatics, and time-series forecasting.
- **Real research scenarios across scales.** [SciAgentArena](../works/sciagentarena.md) provides ~200 tasks from real-world scientific research scenarios with stepwise verification in an agent-agnostic environment, reporting that agents handle structured data-analysis workflows but struggle with novel insights, self-directed exploration, and open-ended questions.
- **A gymnasium of scientific environments.** [Aviary](../works/aviary.md) provides an extensible gymnasium of language-agent environments, three of them scientific (molecular cloning, scientific-literature research, protein engineering); its environments are reusable evaluation surfaces, though the paper's headline is a training framework rather than an evaluation contribution.
- **Cost-aware scientific simulation.** [SimulCost](../works/simulcost.md) extends cost-aware evaluation to physics-simulation parameter tuning across 13 simulators, explicitly accounting for simulation-time and experimental-resource costs.
- **Clinician-validated medical evaluation.** [MedHELM](../works/medhelm.md) extends Stanford CRFM's HELM to medical tasks with a 121-task clinician-validated taxonomy, aggregation across 35 benchmarks, and an LLM-jury evaluation methodology whose agreement against clinician ratings (ICC = 0.47) is explicitly measured.

## Comparison

| Benchmark | Year | Task source | Scientific scope | Verification | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | Domain-expert authored | Life / Physical / Earth / Math / Engineering Sciences | Deterministic pytest in containers | [→](../works/terminal-bench-science.md) |
| NatureBench | 2026 | Distilled from Nature-family papers | Cross-discipline (Nature editorial scope) | Comparison against published SOTA | [→](../works/naturebench.md) |
| ScienceAgentBench | 2024 | Extracted from 44 peer-reviewed papers (expert-validated) | Data-driven discovery (four disciplines) | Execution of unified Python program; program / result / cost metrics | [→](../works/scienceagentbench.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks | LM / math / bioinformatics / time-series | End-to-end research-lifecycle scoring | [→](../works/airs-bench.md) |
| SciAgentArena | 2026 | ~200 real research-scenario tasks | Multi-domain across scales (TODO ref) | Stepwise verification; agent-agnostic environment | [→](../works/sciagentarena.md) |
| Aviary | 2024 | 5-environment gymnasium (3 scientific) | Molecular biology (cloning / protein) + literature | Per-environment task success in POMDP environments | [→](../works/aviary.md) |
| SimulCost | 2026 | Parameter tuning across 13 simulators | Physics simulation | Success rate under budget; comparison against traditional methods | [→](../works/simulcost.md) |
| MedHELM | 2025 | Clinician-designed taxonomy (29 clinicians) | Medical / clinical | LLM-jury (ICC = 0.47 vs clinicians); aggregation across 35 benchmarks | [→](../works/medhelm.md) |

## Open Questions

- **Reference standards for correctness.** Scientific tasks admit multiple defensible reference standards — published SOTA (NatureBench), expert taxonomy (MedHELM), executable verification (Terminal-Bench Science), comparison against traditional methods (SimulCost). Should any one be canonical for cross-benchmark comparison?
- **Discovery vs. reproduction.** NatureBench distinguishes "matching SOTA" from "genuine methodological innovation." How should benchmarks operationalize discovery in a scoring metric?
- **Cost as an evaluation dimension.** Scientific workflows have real tool-use costs (simulation time, experimental resources). Should the scientific-agent topic converge on cost as a mandatory dimension, as SimulCost does?
- **Domain breadth vs. depth.** Cross-discipline benchmarks (NatureBench, AIRS-Bench, MedHELM) give breadth; single-simulator or single-domain benchmarks give depth. Which serves the field better as the primary evaluation surface?
- **Judge reliability.** MedHELM reports LLM-jury / clinician agreement of ICC = 0.47. Is this a floor that other scientific-domain benchmarks using LLM-judge scoring should be expected to report, and what value counts as adequate?

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [NatureBench](../works/naturebench.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SciAgentArena](../works/sciagentarena.md)
- [Aviary](../works/aviary.md)
- [AIRS-Bench](../works/airs-bench.md)
- [SimulCost](../works/simulcost.md)
- [MedHELM](../works/medhelm.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
