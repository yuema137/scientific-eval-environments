# Physics

> **English** | [简体中文](../zh/domains/physics.md) · [← All domains](./README.md)

## Scope

Evaluation environments grounded in physical laws, physical simulation, or experimental physics. Particle, nuclear, quantum, and fluid physics fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| MaD Physics | 2026 | Infer an unknown — and sometimes deliberately altered — physical law governing a simulated system, across classical mechanics (N particles in D dimensions), a 2D incompressible viscous fluid, and two quantum particles in a 2D box. | Interactive experimentation in three simulated environments; each observation costs 2 / 5 / 10 by fidelity level under a fixed per-trial budget. | Prediction error against the true future state: normalized RMSE (classical) and L2 error on vorticity / probability density (fluid / quantum), averaged over 33 random initializations. | [→](../works/mad-physics.md) |
| NewtonBench | 2025 | Rediscover a hidden physical law that has been counterfactually shifted from one of 12 canonical laws (gravitation, Coulomb, Fourier, Snell, …) by mutating its expression tree. | 324 interactive tasks (108 shifted laws × 3 model systems); the agent designs experiments via a `run_experiment` tool and submits the law as a symbolic expression. | Binary symbolic equivalence to the ground-truth law (LLM judge; 98.3% agreement with human experts) plus RMSLE of the discovered equation's predictions. | [→](../works/newtonbench.md) |
| PRBench | 2026 | Reproduce published physics research end to end — comprehend a paper's methodology, implement its algorithms from scratch, and match its quantitative results — across 11 subfields from QCD to condensed matter. | 30 expert-curated paper-reproduction tasks contributed by 20+ research groups, run in a sandboxed execution environment with standardized CSV outputs. | Expert-written weighted rubric per task (Data Reproduction Accuracy weighted 0.60); end-to-end success requires >0.9 on every dimension — currently zero for all agents. | [→](../works/prbench.md) |
| Collider-Bench | 2026 | Reproduce LHC experimental analyses: generate signal events for CMS supersymmetry searches through the public simulation stack (MadGraph5, Pythia, Delphes) and implement the published event selection. | 10 Simulation tasks from four CMS SUSY searches at 13 TeV; the agent submits a binned histogram of predicted signal yields plus analysis code and a methodological report. | Relative L² distance to hidden reference histograms, pass threshold set by a physicist-in-the-loop baseline; an LLM provenance judge additionally flags fabricated workflows. | [→](../works/collider-bench.md) |
| SimulCost | 2026 | Tune simulation parameters to reach target physical outcomes across 13 physics simulators, accounting for simulation-time and experimental-resource costs. | 2,947 single-round and 1,931 multi-round parameter-tuning tasks. | Success rate under budget constraints, with stricter accuracy tiers reported separately. | [→](../works/simulcost.md) |
| NatureBench | 2026 | Match the published state of the art of Nature-family Physical Modeling studies — 13 of its 90 tasks — given the target algorithm's inputs but none of its operations or outputs. | Code-agent tasks built by a review-gated pipeline with an information firewall; ~3.7 primary metrics per task. | SOTA-normalized relative gap g on each paper's own primary metric; Match-SOTA (g ≥ 0) and Surpass-SOTA (g > 0.1) rates, with a judge flagging shortcut runs. | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | Physics tasks within the Physical Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Physics is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| CMT-Benchmark | 2025 | Solve expert-researcher-level condensed matter theory problems — quantum many-body systems and classical statistical mechanics — spanning Hartree-Fock, exact diagonalization, quantum/variational Monte Carlo, DMRG, and statistical mechanics. | 50 single-problem theoretical and computational derivations authored by expert researchers at the level of their own work; not an interactive agent setting. | Programmatic checking against expert-supplied ground truth, with machine grading that includes normal-ordered symbolic handling of non-commuting operators. | [→](../works/cmt-benchmark.md) |
| CMPhysBench | 2025 | Carry out graduate-level condensed matter physics calculations across magnetism, superconductivity, strongly correlated systems, and foundational theoretical frameworks. | More than 520 curated calculation problems, each requiring an independently generated full solution; single-problem derivations, not an interactive agent setting. | SEED (Scalable Expression Edit Distance) partial credit over solution expressions, plus accuracy as the percentage of correct solutions. | [→](../works/cmphysbench.md) |
| PhySciBench | 2026 | Answer expert-curated deep-research questions on the physics side of a physics/chemistry-balanced set, targeting fragile reasoning chains, limited cross-step knowledge transfer, and missing physics-grounded self-verification. | 200 expert-curated questions balanced between physics and chemistry, organized into six task categories reflecting real-world scientific workflows. | Accuracy-based evaluation comparing state-of-the-art models and agent systems, with cost reported alongside accuracy. | [→](../works/physcibench.md) |
| MetaSyn | 2026 | Conduct protocol-faithful systematic review and meta-analysis; physics is among the subjects its 422 expert-curated meta-analyses span. | Multi-stage systematic-review workflows: identify the eligible studies for a research question with structured PI/ECO criteria within a shared PubMed-anchored corpus containing ineligible distractors. | Study identification against the original expert reviewers' included set, with stage-wise evaluation locating failures along the meta-analysis pipeline. | [→](../works/metasyn.md) |
| RealPDEBench | 2026 | Predict the evolution of complex physical systems — fluid–structure interaction, cylinder and foil flows, and combustion — from real-world measurements paired with numerical simulations. | Five real-world measured datasets with paired simulated datasets and three sim-vs-real tasks; evaluates scientific ML surrogate models rather than LLM agents. | Eight metrics spanning data-oriented and physics-oriented measures, over ten baselines including pretrained PDE foundation models and a traditional method. | [→](../works/realpdebench.md) |

## Related Works

- [MaD Physics](../works/mad-physics.md)
- [NewtonBench](../works/newtonbench.md)
- [PRBench](../works/prbench.md)
- [Collider-Bench](../works/collider-bench.md)
- [SimulCost](../works/simulcost.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CMPhysBench](../works/cmphysbench.md)
- [PhySciBench](../works/physcibench.md)
- [MetaSyn](../works/metasyn.md)
- [RealPDEBench](../works/realpdebench.md)
