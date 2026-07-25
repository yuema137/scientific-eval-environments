# Scientific Agent Benchmarks

## Definition

Scientific agent benchmarks evaluate AI agents on tasks drawn from scientific research and practice — computational workflows, parameter tuning, literature-grounded problems, or replication of published results. What distinguishes them from general-purpose agent benchmarks is the source of tasks (real scientific work) and the standard for correctness (matching published or expert-defined outcomes).

## Motivation

Scientific work has features that generic agent benchmarks under-model: intermediate evaluation may be expensive (simulations, experiments), tasks are often long-horizon, correctness must sometimes be validated against a published or expert reference rather than a synthetic ground truth, and workflows involve heterogeneous tools that require domain knowledge to sequence correctly. A separate topic exists because scoring scientific agents demands attention to these features.

## Existing Approaches

- **Executable scientific workflows.** [Terminal-Bench Science](../works/terminal-bench-science.md) evaluates AI agents on real computational workflows drawn from natural-science research, verified with pytest inside containers, across five scientific domains.
- **Publication-anchored difficulty.** [NatureBench](../works/naturebench.md) distills 90 tasks from Nature-family publications and asks whether coding agents can match the published SOTA. It exposes a gap: the strongest agent surpasses the published SOTA on only 17.8% of tasks (matching it on 47.8%).
- **Expert-validated, execution-based tasks.** [ScienceAgentBench](../works/scienceagentbench.md) extracts 102 tasks from 44 peer-reviewed publications across four disciplines, engages nine subject matter experts to validate them, and unifies every task's output to a self-contained Python program scored on program, execution result, and cost. It insists on assessing individual workflow tasks before claiming end-to-end automation, and reports a low best-agent solve rate (32.4% independently, 34.3% with expert-provided knowledge).
- **End-to-end research lifecycle.** [AIRS-Bench](../works/airs-bench.md) provides 20 frontier research-science tasks without baseline code, requiring agents to construct workflows from scratch across language modeling, mathematics, bioinformatics, and time-series forecasting.
- **Real research scenarios across scales.** [SciAgentArena](../works/sciagentarena.md) provides ~200 tasks from real-world scientific research scenarios with stepwise verification in an agent-agnostic environment, reporting that agents handle structured data-analysis workflows but struggle with novel insights, self-directed exploration, and open-ended questions.
- **A gymnasium of scientific environments.** [Aviary](../works/aviary.md) provides an extensible gymnasium of language-agent environments, three of them scientific (molecular cloning, scientific-literature research, protein engineering); its environments are reusable evaluation surfaces, though the paper's headline is a training framework rather than an evaluation contribution.
- **Cost-aware scientific simulation.** [SimulCost](../works/simulcost.md) extends cost-aware evaluation to physics-simulation parameter tuning across 13 simulators, explicitly accounting for simulation-time and experimental-resource costs.
- **Clinician-validated medical evaluation.** [MedHELM](../works/medhelm.md) extends Stanford CRFM's HELM to medical tasks with a 121-task clinician-validated taxonomy, aggregation across 35 benchmarks, and an LLM-jury evaluation methodology whose agreement against clinician ratings (ICC = 0.47) is explicitly measured.
- **Generated rather than authored benchmarks.** [HeurekaBench](../works/heurekabench.md) contributes a semi-automated pipeline that derives open-ended research questions from published studies and their code repositories, verifying candidate answers against the findings those studies reported. Its single-cell instantiation holds 50 open-ended and 50 multiple-choice questions from 41 insights across 13 papers, and the strongest existing agent reaches 2.34 out of 5 on open-ended correctness.
- **Simulation-grounded grading validity.** [GeneBench-Pro](../works/genebench-pro.md) builds 129 multistage genomics and quantitative-biology problems on constructively simulated data-generating processes rather than real datasets, so that a failure is attributable to a scientific error rather than to one of several defensible analyst choices. Each problem hides 3 to 13 dependent decision points and is graded by a single binary pass on the decision-relevant number; the best configuration measured reaches 28.7%.
- **Physical execution on a real instrument.** [AFMBench](../works/afmbench.md) holds agents to 100 curated tasks on an actual atomic force microscope rather than a simulator, and reports that materials-science question-answering proficiency does not transfer: Claude-3.5-Sonnet carries a 51.6% error rate while the best model reaches 65% overall task completion, falling to 23.3% where documentation and analysis are merged.

## Comparison

| Benchmark | Year | Task source | Scientific scope | Verification | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | Domain-expert authored | Life / Physical / Earth / Math / Engineering Sciences | Deterministic pytest in containers | [→](../works/terminal-bench-science.md) |
| NatureBench | 2026 | Distilled from Nature-family papers | Cross-discipline (Nature editorial scope) | Comparison against published SOTA | [→](../works/naturebench.md) |
| ScienceAgentBench | 2024 | Extracted from 44 peer-reviewed papers (expert-validated) | Data-driven discovery (four disciplines) | Execution of unified Python program; program / result / cost metrics | [→](../works/scienceagentbench.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks | LM / math / bioinformatics / time-series | End-to-end research-lifecycle scoring | [→](../works/airs-bench.md) |
| SciAgentArena | 2026 | ~200 real research-scenario tasks | Biomedical: 5 fields (molecular → population) | Per-domain stepwise verification (execution + expert criteria) | [→](../works/sciagentarena.md) |
| Aviary | 2024 | 5-environment gymnasium (3 scientific) | Molecular biology (cloning / protein) + literature | Per-environment task success in POMDP environments | [→](../works/aviary.md) |
| SimulCost | 2026 | Parameter tuning across 13 simulators | Physics simulation | Success rate under budget; comparison against traditional methods | [→](../works/simulcost.md) |
| MedHELM | 2025 | Clinician-designed taxonomy (29 clinicians) | Medical / clinical | LLM-jury (ICC = 0.47 vs clinicians); aggregation across 35 benchmarks | [→](../works/medhelm.md) |
| HeurekaBench | 2026 | Semi-automated pipeline over published studies and their code repositories | Single-cell biology (pipeline presented as domain-general) | G-Eval LLM judge (GPT-4o, 1–5) against published findings | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | Constructively simulated data-generating processes | Genomics / quantitative biology / translational biomedicine | Binary match to recoverable targets under calibrated tolerances | [→](../works/genebench-pro.md) |
| AFMBench | 2025 | 100 expert-curated tasks, stratified by tool count, agent count, complexity and functional domain | Scanning-probe microscopy of materials | Physical execution on a Nanosurf DriveAFM; per-domain completion rate plus a named error taxonomy | [→](../works/afmbench.md) |

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
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [AFMBench](../works/afmbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
