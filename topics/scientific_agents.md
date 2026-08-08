# Scientific Agent Benchmarks

> **English** | [简体中文](../zh/topics/scientific_agents.md) · [← All topics](./README.md)

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
- **Reproducing published analyses under provenance audit.** [Collider-Bench](../works/collider-bench.md) asks agents to reproduce LHC analyses from public papers and open simulation software, scoring 10 CMS-search tasks by continuous histogram fidelity against hidden reference yields with an LLM judge auditing execution traces; across 364 judged runs 6% of submissions are flagged fabricated, and on average no agent reliably beats the physicist-in-the-loop solution.
- **Counterfactual law discovery.** [NewtonBench](../works/newtonbench.md) has agents run experiments on simulated physical systems to recover counterfactually shifted versions of 12 canonical physics laws, scoring its 324 tasks by LLM-judged symbolic equivalence.
- **Claim-level reproduction in computational materials science.** [AutoMat](../works/automat.md) packages 85 expert-curated claims from computational materials science papers into runnable HPC tasks and reports that the best-performing coding-agent setting reaches a 54.1% success rate, with near-zero success when workflows must be recovered from paper text alone.
- **Structured tool calling against a live geospatial API.** [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) runs 93 environmental-analysis tasks against an open, self-hostable API serving three indicators across Spain and Portugal, grading each case with mechanistic checks and no LLM judge while reporting capability and per-case cost as orthogonal axes; the best model reaches 60.8% ± 0.8% and close-value comparison tasks sit at 0% for every model.
- **End-to-end reproduction of published AI experiments.** [EXP-Bench](../works/exp-bench.md) curates 461 tasks from 51 NeurIPS 2024 and ICLR 2024 papers, requiring agents to design, implement, execute, and conclude full experiments; the best agent configuration completes only 0.5% of experiments in executable form.
- **Full-cycle insight rediscovery.** [FIRE-Bench](../works/fire-bench.md) gives agents only a high-level research question from a published machine-learning study and scores their conclusions by claim-level F1 against the study's documented findings, with the strongest evaluated agent, Claude Code (Sonnet-4), reaching 46.7 on the 30-task core set.
- **Hidden-paper re-discovery.** [ResearchClawBench](../works/researchclawbench.md) grounds each of 40 tasks in a real published paper that stays hidden during evaluation, with GPT-5.1 scoring agent research reports against expert-curated weighted rubrics on the 0–100 RADS scale.
- **Simulation-driven model fitting.** [Stargazer](../works/stargazer.md) evaluates agents on iterative radial-velocity model fitting with per-criterion physical-consistency feedback; across three difficulty tiers and 20 real archival systems, no evaluated frontier agent passes a single real task.
- **Paper reproduction as the unit of evaluation.** [PRBench](../works/prbench.md) asks agents to reproduce published physics papers end to end — 30 expert-curated tasks across 11 subfields, on which the best agent, OpenAI Codex (GPT-5.3-Codex), scores 34% with a zero end-to-end callback success rate.
- **Holistic cost-controlled research suite.** [AstaBench](../works/astabench.md) aggregates 2,400+ problems across 11 benchmarks covering literature understanding, code & execution, data analysis, and end-to-end discovery, scoring 57 agents under standard tools with time-invariant dollar-cost accounting.
- **Literature discovery as the evaluation target.** [AutoResearchBench](../works/autoresearchbench.md) isolates the literature-finding step of autonomous research with 1,000 queries in two task types — Deep Research (tracking down one target paper through progressive multi-step probing) and Wide Research (comprehensively collecting all papers satisfying given conditions) — and reports that the strongest models reach only 9.39% accuracy and 9.31% IoU respectively, despite having largely conquered general agentic browsing benchmarks such as BrowseComp.
- **Physical execution on a real instrument.** [AFMBench](../works/afmbench.md) holds agents to 100 curated tasks on an actual atomic force microscope rather than a simulator, and reports that materials-science question-answering proficiency does not transfer: Claude-3.5-Sonnet carries a 51.6% error rate while the best model reaches 65% overall task completion, falling to 23.3% where documentation and analysis are merged.
- **Tiered evaluation of one simulation discipline.** [CFDLLMBench](../works/cfdllmbench.md) fixes the domain to computational fluid dynamics and varies the depth of competence instead: 90 graduate-level questions, 24 PDE-solver coding problems, and 126 OpenFOAM cases, with physical accuracy graded by normalized error against reference solutions and by whether the solution converges under mesh and time-step refinement. Scores fall from 92% on knowledge to ~14% on solver coding and 34% / 25% on the OpenFOAM Basic / Advanced splits.
- **Iterative generative optimization under simulator feedback.** [Frontier-Eng](../works/frontier-eng.md) frames real-world engineering evaluation as a propose-execute-evaluate loop: across 47 tasks in 5 engineering categories, an industrial-grade simulator returns continuous reward under hard feasibility constraints and the agent revises within a fixed interaction budget. Across 8 frontier LLMs the paper reports a dual power-law decay in both improvement frequency and improvement magnitude, and finds that depth matters more than breadth for constrained engineering problems.

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
| Collider-Bench | 2026 | Derived from four published CMS supersymmetry searches (expert-solved first) | Experimental particle physics (LHC recasting) | Relative L² to hidden reference yields (τ = 0.33 pass threshold); LLM provenance judge | [→](../works/collider-bench.md) |
| NewtonBench | 2025 | 108 counterfactual shifts of 12 canonical physics laws, each in 3 simulated model systems | Interactive scientific law discovery in physics | LLM-judged symbolic equivalence plus RMSLE data fidelity | [→](../works/newtonbench.md) |
| AutoMat | 2026 | 85 claims curated by materials-science SMEs from recent publications | Computational materials science (Stat/ML, DFT, MD, DDD) | Artifact-grounded LLM evaluator agent scores 1–5 against hidden SME reproduction steps; success is a score of at least 4 | [→](../works/automat.md) |
| GeoNatureAgent Benchmark | 2026 | Tasks specified with domain-expert ground truth against a self-hostable geospatial API | Environmental geospatial analysis (Spain / Portugal) | Automated tool-call / keyword / numeric-tolerance checks; no LLM-as-judge | [→](../works/geonatureagent-benchmark.md) |
| EXP-Bench | 2025 | 461 tasks extracted from 51 NeurIPS 2024 / ICLR 2024 papers and their code | End-to-end AI research experiments: design, implementation, execution, conclusion | LLM-judge grading of design / implementation / conclusion plus containerized execution validation | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | One task per paper from 30 empirical LLM-analysis papers at ICLR, ICML, and NeurIPS 2024–2025, plus a 10-task cross-domain extension | Full cycle: plan → code → execute → conclude from a high-level research question | Claim-level precision, recall, and F1 against ground-truth findings via a fixed gpt-5.2 entailment judge | [→](../works/fire-bench.md) |
| ResearchClawBench | 2026 | 40 tasks expert-curated from real published papers, target paper hidden | 10 domains: astronomy, chemistry, earth, energy, information, life, material, math, neuroscience, physics | GPT-5.1 scores reports against weighted multimodal rubrics (RADS, 0–100) | [→](../works/researchclawbench.md) |
| Stargazer | 2026 | 100 seeded simulator tasks + 20 anonymized archival systems (NASA Exoplanet Archive, VizieR) | Astrophysics: exoplanet model fitting on RV time series | Four joint pass/fail criteria (residual RMS, ΔBIC, parameter match, planet count) | [→](../works/stargazer.md) |
| PRBench | 2026 | Published physics papers curated and reproduced by 20+ research groups at Peking University | 30 tasks across 11 physics subfields | Weighted four-dimension rubric scored by a green agent against expert ground truth; end-to-end callback rate | [→](../works/prbench.md) |
| AstaBench | 2025 | Author-built + adapted datasets, many from Asta user requests | Full pipeline: literature, code, data analysis, end-to-end discovery (CS-weighted) | LLM-judge rubrics + programmatic scoring with cost accounting | [→](../works/astabench.md) |
| AFMBench | 2025 | 100 expert-curated tasks, stratified by tool count, agent count, complexity and functional domain | Scanning-probe microscopy of materials | Physical execution on a Nanosurf DriveAFM; per-domain completion rate plus a named error taxonomy | [→](../works/afmbench.md) |
| AutoResearchBench | 2026 | 1,000 queries from a full-text-first human–machine pipeline over published papers and citation graphs | Scientific literature discovery (eight core CS domains) | Exact-match accuracy (Deep Research) and set-level IoU (Wide Research) against verified answer sets | [→](../works/autoresearchbench.md) |
| Frontier-Eng | 2026 | 47 real-world engineering tasks across 5 categories | Real-world engineering (industrial-grade simulators) | Continuous simulator reward under hard feasibility constraints; fixed interaction budget | [→](../works/frontier-eng.md) |
| CFDLLMBench | 2025 | 90 expert-written questions, 24 PDE coding problems, 126 OpenFOAM cases (110 tutorial-derived + 16 hand-crafted) | Computational fluid dynamics | Execution + normalized error vs. reference solution + convergence under mesh/time-step refinement | [→](../works/cfdllmbench.md) |

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
- [Collider-Bench](../works/collider-bench.md)
- [NewtonBench](../works/newtonbench.md)
- [AutoMat](../works/automat.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Stargazer](../works/stargazer.md)
- [PRBench](../works/prbench.md)
- [AstaBench](../works/astabench.md)
- [AFMBench](../works/afmbench.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [CFDLLMBench](../works/cfdllmbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
