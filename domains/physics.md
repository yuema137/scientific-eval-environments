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
| Gravity-Bench-v1 | 2025 | Discover the concealed — sometimes out-of-distribution — physics of a simulated two-body gravitational system from planned observations. | Interactive observation-planning-and-analysis episodes under an experimental budget (up to 100 observations per run, official project page). | Answers checked against reference solutions from rigorous gravitational-dynamics simulations, calibrated against human expertise. | [→](../works/gravity-bench.md) |
| PhysGym | 2025 | Discover underlying physical laws by probing interactive simulations, at four controlled levels of supplied prior knowledge. | 97 curated problems (sourced from PHYBench) run as sequential interactive episodes under a limited experimental budget. | Standardized protocols and metrics for hypothesis accuracy and model fidelity. | [→](../works/physgym.md) |
| DiscoverPhysics | 2026 | Uncover the laws of motion of N-body worlds whose physics deliberately deviates from ours — modified gravity, hidden particle species. | 22 counterfactual worlds generated on demand; iterative experiment proposal ending in a natural-language explanation plus a Python law. | Trajectory MSE on held-out particles plus a rubric-based LLM-judged explanation score. | [→](../works/discoverphysics.md) |
| FEABench | 2025 | Solve multiphysics problems end to end with finite element analysis by operating COMSOL Multiphysics through its API. | Natural-language problem descriptions; the agentic setting iterates API calls against software feedback. | Evaluation over generated API calls and computed answers, with executability of API calls as a headline metric. | [→](../works/feabench.md) |
| QMP-Bench | 2026 | Reproduce published quantum many-body simulation results end to end. | 100 research-level tasks extracted from 21 high-impact journals. | Programming verifiers for coding correctness plus scientific verifiers for principle-based physical validity. | [→](../works/qmp-bench.md) |
| gwBenchmarks | 2026 | Perform high-precision gravitational-wave science: waveform surrogates from numerical relativity, black-hole orbital dynamics, remnant fitting, template banks. | 8 tasks over data representing more than 10⁸ core-hours of compute; 12 coding agents evaluated. | External pre-defined evaluation framework with per-task physics metrics (frequency-domain mismatch, relative errors) against a ≲10⁻⁴ domain requirement. | [→](../works/gwbenchmarks.md) |
| PRL-Bench | 2026 | Carry out frontier physics research tasks derived from post-August-2025 Physical Review Letters papers across five subfields. | 100 expert-validated, long-horizon research tasks with exploration-oriented formulation. | Objectively verifiable outcomes scored on a 0–100 scale. | [→](../works/prl-bench.md) |
| EnvTrace | 2025 | Generate control code for synchrotron beamlines, whose correctness is its physical behavior over time. | Control-code generation evaluated on a beamline control-logic digital twin; over 30 LLMs evaluated. | Execution-trace alignment yielding a multi-faceted functional-correctness score. | [→](../works/envtrace.md) |
| CritPt | 2025 | Solve unpublished, research-entry-level physics challenges across 11+ subfields from condensed matter to biophysics. | 71 composite challenges plus 190 checkpoint tasks authored by 50+ active researchers, optionally with coding tools. | Guess-resistant, machine-verifiable answers graded by a physics-customized automated pipeline. | [→](../works/critpt.md) |
| TPBench | 2025 | Solve novel theoretical-physics problems in high-energy theory and cosmology, up to research level. | 57 novel problems from undergraduate to research difficulty; single-problem derivations. | Auto-verifiable answers with grading tailored to theoretical derivations. | [→](../works/tpbench.md) |
| SciCode | 2024 | Write research code for scientist-curated problems; physics is among the five main domains its 16 natural-science subfields span. | 80 main problems decomposed into 338 subproblems mixing knowledge recall, reasoning, and code synthesis. | Execution against scientist-annotated gold-standard solutions and test cases. | [→](../works/scicode.md) |
| Lean4Physics | 2025 | Prove college-level physics statements formally in Lean4. | 200 hand-crafted, peer-reviewed statements from university textbooks and competition problems, supported by the PhysLib foundation library. | Lean4 kernel proof checking — no judge in the loop. | [→](../works/lean4physics.md) |
| UGPhysics | 2025 | Solve undergraduate physics problems across 13 subjects and four physics reasoning skills. | 5,520 bilingual (EN/ZH) problems with seven answer types, rigorously screened for data leakage. | MARJ (Model-Assistant Rule-based Judgment) pipeline tailored to physics answer correctness. | [→](../works/ugphysics.md) |
| PHYBench | 2025 | Solve original physics problems requiring physical perception and multi-step, multi-condition reasoning, up to olympiad level. | 500 original problems with symbolic answers; measured human-expert baseline. | Expression Edit Distance (EED) score over mathematical expressions, plus accuracy. | [→](../works/phybench.md) |
| SeePhys | 2025 | Solve physics problems whose diagrams are essential — circuit schematics, Feynman diagrams, and 19 other diagram categories. | 2,000 validated multimodal questions (official page) from middle school to PhD qualifying level; 75% vision-essential. | Accuracy on multimodal problem solving, against a human-expert anchor. | [→](../works/seephys.md) |
| HiPhO | 2025 | Solve the latest high-school physics olympiad exams under contest-grade grading. | 13 exams from 2024–2025, international and regional, mixing text-only and diagram-based problems. | Official marking schemes at answer and step level; medals assigned by official thresholds. | [→](../works/hipho.md) |
| PHYSICS | 2025 | Solve university-level physics problems across six core areas: classical mechanics, quantum mechanics, thermodynamics and statistical mechanics, electromagnetism, atomic physics, and optics. | 1,297 expert-annotated problems; static single-problem solving. | Robust automated evaluation system for precise and reliable answer validation. | [→](../works/physics-benchmark.md) |

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
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [PhysGym](../works/physgym.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FEABench](../works/feabench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [PRL-Bench](../works/prl-bench.md)
- [EnvTrace](../works/envtrace.md)
- [CritPt](../works/critpt.md)
- [TPBench](../works/tpbench.md)
- [SciCode](../works/scicode.md)
- [Lean4Physics](../works/lean4physics.md)
- [UGPhysics](../works/ugphysics.md)
- [PHYBench](../works/phybench.md)
- [SeePhys](../works/seephys.md)
- [HiPhO](../works/hipho.md)
- [PHYSICS](../works/physics-benchmark.md)
