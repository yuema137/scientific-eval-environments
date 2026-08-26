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
| CodePDE | 2025 | Generate numerical solvers for representative PDE problems governing physical systems. | Solver code generation with iterative refinement; reasoning, debugging, self-refinement, test-time scaling evaluated. | Generated-solver accuracy against reference solutions. | [→](../works/codepde.md) |
| PDEAgent-Bench | 2026 | Produce finite-element solvers for PDEs across 6 mathematical categories and 11 families. | 645 specification-to-code instances targeting DOLFINx, Firedrake, or deal.II. | Staged executability, numerical-accuracy (reference solutions on prescribed grids), and efficiency checks. | [→](../works/pdeagent-bench.md) |
| MooseBench | 2026 | Generate multiphysics simulation code that solves the intended PDE, not merely code that runs. | 220 MOOSE cases with PDE-level mathematical ground truth. | Intent Fidelity Score via deterministic reconstruction of governing terms, BCs, ICs, coefficients, and time scheme. | [→](../works/moosebench.md) |
| SciConvBench | 2026 | Turn ill-posed computational-science requests — fluid mechanics, solid mechanics, materials, PDEs — into well-posed specifications through dialogue. | Multi-turn disambiguation and inconsistency-resolution dialogues. | Rubric scoring of clarification behavior, grounding, and final-specification fidelity. | [→](../works/sciconvbench.md) |
| AInsteinBench | 2025 | Resolve maintainer-PR tasks in production scientific codebases, including numerical relativity and fluid dynamics. | Repository-level coding-agent tasks across six scientific repositories. | Test-driven verification in executable environments. | [→](../works/ainsteinbench.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of physics data — one of its seven application domains — turning natural-language intent into executable visualization operations (volume rendering, field computation, insight derivation). | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| An LLM-driven framework for cosmological model-building and exploration | 2025 | Implement dark-energy field theories — Thawing Quintessence and Early Dark Energy — inside the CLASS Boltzmann solver, then explore their parameter space against observations. | Three sequential stages (model implementation, computing observables, parameter exploration) per model instance in a containerized CLASS 3.3.0 environment; two ground-truth models plus two hypothesis-generation runs, with a single agent configuration evaluated. | Binary execution milestones, maximum fractional deviation of Ω_X and the matter power spectra against ground-truth reference implementations, and likelihood/BIC, Hubble/M_B tension and CMB C_ℓ consistency rewards computed from DESI, Planck, Pantheon+ and SH0ES data. | [→](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope | 2026 | Build and run a matched-filter gravitational-wave search: Welch PSD estimation from raw strain, geometric template-bank generation with the IMRPhenomD approximant at 0.97 minimum match, and recovery of injected binary-black-hole waveforms. | One written specification executed autonomously four times — two agents (Claude Code, Codex) × two injection-loudness runs — over 100 BBH injections in simulated Einstein Telescope E1 noise on identical hardware. | Measured pipeline outputs — template-bank size, detection efficiency above ρ = 8, recovered SNR statistics, wall-clock runtime and peak memory — reported beside counted process behaviours (restarts, silent deviations, unsolicited optimisations). | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SimAgents | 2025 | Recover the cosmological model a published simulation assumes — matter, baryon and dark-energy densities, Hubble parameter, σ8 and spectral index — from the paper text, in a form MP-Gadget will accept. | More than 40 published simulations from arXiv, ApJ and MNRAS, each hand-annotated for every relevant parameter/value pair; compared against chain-of-thought and exchange-of-thought baselines. | Parameter-level precision, recall and micro-F1 against the manual annotations, plus a Value / Type / Hallucination error taxonomy counted per simulation, reported under both human and automatic grading. | [→](../works/simagents.md) |
| Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities | 2025 | Distinguish damped from chirped harmonic-oscillator dynamics in generated time-series data. | Two of the ten benchmark tasks are oscillator-dynamics problems, each pairing an author-generated dataset with a natural-language prompt; three coding agents and two judge models compared. | pass@1 on whether the system identifies the correct underlying model, with a vision-language plot judge grading the produced figure — code withheld — against a rubric generated per task from the task prompt. | [→](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| AI's Capability in Assisting Scientific Research I: Literature Review | 2026 | Assemble the literature for the physics projects among the eight: pulsar-timing-array sensitivity to deviations from general relativity, massive Yang–Mills theory, and debris emergence on laser-ablated sub-wavelength shapes. | One literature-search pass per project per system, capped at 50 papers sorted into four categories; three AI systems against one human expert per project, producing 701 AI and 194 human references. | Overlap with the expert's list counted only when title and assigned category both match, with relevance judged by the project's domain expert; every AI reference separately verified by a DOI → link → title-search cascade and classed perfect / metadata mismatch / fabrication. | [→](../works/ai-assisting-research-i-literature-review.md) |
| AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation | 2026 | Write a one-page research plan for the physics projects among the eight — massive Yang–Mills theory and laser-ablation debris prediction — specifying methods, datasets, tools, timeline and risks. | 32 one-page proposals (8 human, 24 from three LLMs) written from an identical expert-supplied brief and template; every one of the six reviewers assessed all 32. | Blind 1–5 rubric scoring on clarity and structure, appropriateness of methods, resource and tool planning, and feasibility/timeline/risk awareness, by four faculty or senior-postdoc reviewers and two frontier LLM reviewers, plus a binary human-versus-AI authorship judgment per proposal. | [→](../works/ai-assisting-research-ii-project-planning.md) |
| Imaging-101 | 2026 | Physics computational imaging — one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| SciVQR | 2026 | Multimodal scientific reasoning in physics, one of six top-level scored subjects and — with mathematics — one of the two hardest. | 3,254 image-paired competition and exam questions across six subjects and 54 subfields (2,545 multiple-choice, 709 free-form; easy/medium/hard tiers); 15 multimodal models zero-shot, with and without CoT. Per-subject item counts are not published. | Zero-shot accuracy reported per subject, plus a five-dimension rubric (faithfulness, informativeness, redundancy, hallucination, missing steps) scoring the generated reasoning against expert-authored solution traces. | [→](../works/scivqr.md) |
| HiSciBench | 2025 | Literature-facing physics work: parsing, translating, answering questions about and generating reviews from physics papers sourced from arXiv. | 2,306 physics instances within 8,735 — 200 general scientific QA, 357 literature OCR, 357 translation, 1,025 monolingual literature QA, 357 cross-lingual literature QA and 10 review topics; physics contributes no data-driven-discovery instances. 18 models evaluated. | Level-appropriate metrics: accuracy at the QA levels, word-level accuracy for literature OCR, BLEU for translation, and at the review level an LLM-judge 1–5 rubric over Coverage, Structure, Relevance, Synthesis and Critical Analysis plus citation verifiability, metadata accuracy, faithfulness and recency. | [→](../works/hiscibench.md) |
| LQCDMaster | 2026 | Compute lattice-QCD observables from first principles — meson and baryon two-point functions, nonlocal Wilson-line correlators, meson and baryon three-point functions with sequential sources, and Wilson loops — by turning a natural-language research request into an executable PyQUDA measurement workflow. | 70 LQCD computing tasks (20 local 2PTs, 10 nonlocal 2PTs, 13 meson 3PTs, 15 baryon 3PTs, 12 Wilson loops), each paired with a hand-written expert reference implementation for the same observable, ensemble and kinematic setup; workflows executed through the PyQUDA/QUDA GPU stack with SLURM job submission. | Direct numerical comparison against the expert reference at machine precision, labelled Matched (absolute deviation ≲ 10⁻¹²), Convention Mismatch (a global sign or phase difference), or Failure; GPT-5.4 reaches 63/70 Matched (90.0%), DeepSeek-V4-Pro 56/70 (80.0%). | [→](../works/lqcdmaster.md) |
| PACE-Bench | 2026 | Repair a working mechanism design after the physics underneath it is mutated — friction, material strength, gravity or force limits. | 144 source-to-target pairs from 36 base tasks over six physics families at 6 tasks each; 20 attempts per pair with non-prescriptive diagnostic feedback. | Box2D rigid-body simulation; constraint-satisfaction fraction and task score in [−100, 100], reported as Pass@2 — best full-benchmark result 35.9%. | [→](../works/pace-bench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the physics subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`CLA` classical mechanics & dynamics · `STAT` statistical physics & thermodynamics · `CM` condensed matter · `AMO` atomic, molecular & optical · `QM` quantum mechanics (general) · `QI` quantum information & computing · `HEP` high-energy & particle · `NUC` nuclear · `PLA` plasma · `GR` gravitation, relativity & gravitational waves · `COS` cosmology & astrophysics · `FLU` fluid dynamics · `COMP` computational & numerical physics (PDE, FEM, solvers) · `INSTR` instrumentation & experimental infrastructure · `GEN` curriculum-wide or unspecified, no single subfield

**Two scores, not one.** The columns split into **coverage** — what the evaluation setup puts under test — and **rigor** — how far you can trust what it reports. They are summed separately because they pull against each other: a benchmark can put everything under test and verify none of it carefully, and a deliberately narrow one can be the most trustworthy thing on the page. Rows are ordered by `Cov`, highest first, and by `Rig` within equal coverage; remaining ties keep Comparison-table order. Coverage leads because it is the axis a reader scans for — *does this benchmark even put my problem under test* — and `Rig` then says how far to trust what it reports.

### Coverage (`Cov`, max 7)

Yes/no, ordered by rarity — the properties fewest works have come first, so the left of the group is where the field is thin. A property nearly every work satisfies does not earn a column: *writing and running code* was dropped on that ground.

- **Net** — network or live external retrieval permitted; a supplied fixed corpus does not count.
- **E2E** — end-to-end research: a question or goal only, with no source paper, reference implementation, or step-by-step specification supplied, and the agent drives the whole investigation.
- **Cost** — budget or resource cost is a scored or priced dimension, not merely a step cap.
- **MM** — multimodal content is load-bearing, either required as input or scored as an output artifact.
- **Repro** — grounded in a specific published result the agent must match or recover.
- **Real** — real experimental or observational data, as opposed to synthetic or simulated (a digital twin is simulated).
- **Inter** — interactive: the agent takes multiple actions against an environment, tool, or simulator and gets feedback that shapes the next one.

### Rigor (`Rig`, max 13)

- **Human** — a measured human-expert baseline or human reference performance anchors the scale. `◐` where the anchor is a published result or expert reference implementation rather than a measured human run.
- **Rubric** — an expert-authored rubric or official marking scheme with named criteria or weights; a continuous automatic metric is not a rubric.
- **Contam** — a deliberate mechanism makes the answer unmemorizable: post-cutoff sourcing, unpublished or newly authored problems, counterfactual alteration, on-demand generation, or screened leakage. Withholding a published paper at evaluation time is `◐` — it does not remove that paper from a pretraining corpus.
- **Verif** `0`–`3` — how far the score can be trusted without trusting a model. `0` scored only by an LLM judge or rubric, with no validation of that scorer · `1` judge or rubric scoring whose agreement with human experts is measured and reported · `2` deterministic checks alongside judge or rubric scoring · `3` fully deterministic — execution, tests, numerical comparison to a reference, symbolic checking, or a proof kernel, with no judge in the loop. This replaces a plain yes/no *deterministic verification* column, which 85% of works satisfied and which therefore separated nothing; as a ladder it separates a great deal. A separate `Judge` column was dropped as near-redundant with `Verif` < 2.
- **Scale** `0`–`3` — items evaluated **in this domain**: `0` fewer than 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 or more · `?` the source does not give a per-domain count. This counts items, not effort: 30 paper-reproduction tasks are far more work than 3,000 exam questions, and the column cannot see that.
- **Fail** `0`–`4` — how deep the failure analysis goes, because "reports a failure analysis" spans everything from a single remark to a controlled experiment. `0` nothing beyond headline scores · `1` narrative remarks on where models fall short, no classes named · `2` named error classes or illustrative case studies, but no counts or shares · `3` a quantified failure account: a taxonomy with per-class counts or shares, or measured breakdowns isolating specific failure conditions · `4` level 3 plus a controlled experiment or ablation built to test *why* the failures occur.

### Reading the two scores

Yes/no columns score `✔` 1, `◐` 0.5, `✘` 0, `?` 0; graded columns contribute their number, with `?` scoring 0. `Domain` does not score.

Three cautions. A `?` costs exactly what a `✘` costs, so both scores are floors on what a work *demonstrably* does, not verdicts on it. Neither score is a quality ranking: high `Cov` with low `Rig` describes a benchmark that reaches for everything and pins down little, while low `Cov` with high `Rig` describes one that measures a narrow thing carefully — and which of those is the right design depends entirely on the question being asked. And `Cov` is a property of the *evaluation setup*, not of the science: a work can sit at the bottom of this table and still be the most important paper in its subfield.

For multi-domain suites the row describes this domain's slice, as in the Comparison table.

| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| Imaging-101 | COMP | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| PhySciBench | GEN | ◐ | ◐ | ◐ | ✔ | ✘ | ✔ | ✔ | **4.5** | ✘ | ✔ | ✘ | 2 | 2 | 1 | **6** |
| Collider-Bench | HEP | ? | ✘ | ✔ | ✘ | ✔ | ◐ | ✔ | **3.5** | ✔ | ✘ | ◐ | 2 | 1 | 4 | **8.5** |
| NatureBench | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 2 | 1 | 2 | **7** |
| MetaSyn | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 2 | ? | 3 | **6** |
| An LLM-driven framework for cosmological model-building and exploration | COS | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ✘ | ◐ | 2 | 0 | 3 | **6** |
| SciVisAgentBench | GEN | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| Gravity-Bench-v1 | GR, CLA | ? | ✔ | ✔ | ✘ | ✘ | ✘ | ✔ | **3** | ✔ | ✘ | ✔ | 3 | ? | 4 | **9** |
| MaD Physics | CLA, FLU, QM | ? | ✔ | ✔ | ✘ | ✘ | ✘ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 0 | 1 | **5** |
| PACE-Bench | CLA, FLU | ? | ✘ | ✔ | ◐ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✘ | ✔ | 3 | 2 | 4 | **10** |
| AI's Capability in Assisting Scientific Research I: Literature Review | GR, HEP, INSTR | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **2.5** | ✔ | ✘ | ✔ | 2 | 0 | 4 | **8** |
| First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope | GR | ? | ✘ | ✔ | ◐ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✘ | ◐ | 3 | 0 | 4 | **7.5** |
| Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities | CLA | ? | ◐ | ✘ | ✔ | ✘ | ✘ | ✔ | **2.5** | ✘ | ◐ | ✔ | 0 | 0 | 1 | **2.5** |
| NewtonBench | GEN | ? | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✔ | 2 | 2 | 4 | **9** |
| HiSciBench | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| SimulCost | GEN | ? | ✘ | ✔ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| SimAgents | COS | ? | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| DiscoverPhysics | CLA, GR | ? | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✔ | ✔ | 2 | 1 | 2 | **7** |
| PhysGym | GEN | ? | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ◐ | 2 | 1 | 3 | **6.5** |
| PRBench | HEP, AMO, NUC, PLA, CM | ? | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | **2** | ✘ | ✔ | ✘ | 2 | 1 | 2 | **6** |
| QMP-Bench | CM, COMP | ? | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | **2** | ◐ | ✔ | ✘ | 2 | 2 | 0 | **5.5** |
| LQCDMaster | HEP, NUC | ? | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✔ | ✘ | ◐ | 3 | 1 | 3 | **8.5** |
| SeePhys | GEN | ? | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✔ | ✘ | ✘ | 2 | 3 | 3 | **9** |
| MooseBench | COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| PDEAgent-Bench | COMP | ? | ✘ | ✔ | ✘ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| PRL-Bench | COS, CM, HEP, QI, STAT | ✘ | ◐ | ✘ | ✘ | ✘ | ✘ | ◐ | **1** | ✘ | ✔ | ✔ | 0 | 2 | 3 | **7** |
| gwBenchmarks | GR | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | 0 | 3 | **6.5** |
| SciVQR | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| SciConvBench | FLU, COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✔ | ◐ | 1 | ? | 3 | **5.5** |
| AInsteinBench | GR, FLU | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| FEABench | COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 2 | ? | 3 | **5** |
| CodePDE | COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| RealPDEBench | FLU | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| CritPt | GEN | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✔ | 3 | 1 | 3 | **8** |
| PHYSICS | GEN | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ✘ | 2 | 3 | 2 | **7** |
| AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation | HEP, INSTR | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0.5** | ✔ | ✔ | ✔ | 1 | 0 | 3 | **7** |
| HiPhO | GEN | ? | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ✔ | ✔ | ✔ | 0 | 1 | 0 | **4** |
| PHYBench | GEN | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✔ | ✘ | ✔ | 3 | 2 | 4 | **11** |
| UGPhysics | GEN | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 2 | 3 | 3 | **9** |
| CMPhysBench | CM | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| TPBench | HEP, COS | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 1 | 2 | **7** |
| CMT-Benchmark | CM, STAT | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 1 | 2 | **6.5** |
| SciCode | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| EnvTrace | INSTR | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✔ | ✘ | ✘ | 3 | ? | 1 | **5** |
| Lean4Physics | GEN | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 0 | **5** |

Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.
## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
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
- [CodePDE](../works/codepde.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [MooseBench](../works/moosebench.md)
- [SciConvBench](../works/sciconvbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [SimAgents](../works/simagents.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [AI's Capability in Assisting Scientific Research I: Literature Review](../works/ai-assisting-research-i-literature-review.md)
- [AI's Capability in Assisting Scientific Research II: Project Planning and Proposal Evaluation](../works/ai-assisting-research-ii-project-planning.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
- [LQCDMaster](../works/lqcdmaster.md)
- [PACE-Bench](../works/pace-bench.md)
