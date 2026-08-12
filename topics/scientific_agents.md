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
- **Machine-graded expert-level theory.** [CMT-Benchmark](../works/cmt-benchmark.md) poses 50 condensed-matter-theory problems authored by expert researchers at the level of their own work — single-problem derivations rather than an interactive agent setting — and grades them programmatically against expert-supplied ground truth, including normal-ordered symbolic comparison of non-commuting operators. The best model, GPT-5, solves 30%; 18 of the 50 problems are solved by none of the 17 evaluated models.
- **Partial credit for graduate-level derivations.** [CMPhysBench](../works/cmphysbench.md) curates more than 520 graduate-level condensed-matter-physics calculation problems that require independently generating a full solution, and scores them with SEED (Scalable Expression Edit Distance), a fine-grained non-binary partial-credit measure over solution expressions; even the best model, Grok-4, reaches only a 36 average SEED score and 28% accuracy.
- **Containerized molecular-dynamics workflows.** [MDArena](../works/mdarena.md) packages 50 tasks sourced from active research projects — trajectory analysis, system preparation, free-energy calculations, and enhanced sampling across 29 molecular systems and 14 research protocols — into containers, scoring Strict-Pass@1 alongside process-level partial credit; the best configuration, Codex GPT-5.5 (extra-high reasoning), solves 48%.
- **Protocol-faithful evidence synthesis.** [MetaSyn](../works/metasyn.md) anchors 422 tasks to expert-conducted meta-analyses drawn from over 34,000 Nature Portfolio articles: given a research question with structured eligibility criteria (PI/ECO), agents must identify the originally included studies within a shared PubMed-anchored corpus salted with ineligible distractors, and stage-wise evaluation localizes where systems break down along the review pipeline.
- **Physical-science deep research.** [PhySciBench](../works/physcibench.md) curates 200 expert questions balanced between physics and chemistry in six task categories, targeting a diagnosed failure profile — fragile reasoning chains, limited cross-step knowledge transfer, and missing physics-grounded self-verification; the Gemini Deep Research baseline reaches 33.5% accuracy.
- **Intent-structured literature search.** [ScholarQuest](../works/scholarquest.md) organizes agentic paper search by four research intents — method-oriented, setting-anchored, comparison-based, and scope-controlled — over 1,000+ computer science topics; agentic methods beat single-shot baselines, yet the best agent reaches only 0.314 Recall@100.
- **Progressive information-seeking tiers.** [SciExplore](../works/sciexplore.md) grades scientific information seeking across four progressive task types — database navigation, ambiguous literature retrieval, missing reference completion, and cross-source structured knowledge synthesis — over 103 expert-curated tasks in more than ten disciplines, with performance degrading sharply as task complexity increases.
- **Real-world data for physical-system prediction.** [RealPDEBench](../works/realpdebench.md) pairs five real-world measured datasets with numerical simulations of the same complex physical systems, making the sim-to-real gap itself the measured object across three tasks and eight data- and physics-oriented metrics. Its subject is scientific ML surrogate models rather than LLM agents — documented here for its evaluation methodology; experiments over ten baselines show significant sim-vs-real discrepancies, with simulated-data pretraining consistently improving accuracy and convergence.
- **Budgeted gravitational discovery.** [Gravity-Bench-v1](../works/gravity-bench.md) has agents plan observations of a simulated two-body gravitational system within an experimental budget and analyze the data to uncover concealed — sometimes out-of-distribution — physics; per the official project page, the top model drops from 74% with full data access to 49% under the budget.
- **Prior-knowledge-controlled discovery.** [PhysGym](../works/physgym.md) poses 97 interactive physics-discovery problems at four controlled levels of supplied priors, separating what an agent discovers from what it was told; per the official repository, o4-mini falls from 62.89% to 31% as priors are removed.
- **Counterfactual-world discovery.** [DiscoverPhysics](../works/discoverphysics.md) asks agents to run experiments in 22 simulated worlds whose physics deliberately deviates from ours and submit both an explanation and a Python law, scored by held-out trajectory MSE plus a rubric-based LLM-judged explanation score; the strongest agents pass only half the worlds.
- **Operating professional FEA software.** [FEABench](../works/feabench.md) has LLM agents solve multiphysics problems end to end by driving COMSOL Multiphysics through its API; the best strategy generates executable API calls 88% of the time.
- **Quantum many-body reproduction.** [QMP-Bench](../works/qmp-bench.md) extracts 100 research-level, end-to-end quantum many-body simulation tasks from 21 high-impact journals, verified by paired programming and scientific verifiers.
- **Precision-referenced gravitational-wave tasks.** [gwBenchmarks](../works/gwbenchmarks.md) stress-tests twelve coding agents on eight gravitational-wave tasks whose data represent over 10⁸ core-hours, scoring through an external framework because agents fabricated or partially evaluated results; on hard tasks all agents fall 1–2 orders of magnitude short of the ≲10⁻⁴ domain requirement.
- **Author-co-developed paper replication.** [ReplicationBench](../works/replicationbench.md) splits astrophysics papers into 111 replication tasks co-developed with the original authors (official repository), scoring faithfulness to method and correctness of result separately; even the best models score under 20%.
- **Journal-fresh research tasks.** [PRL-Bench](../works/prl-bench.md) derives 100 expert-validated, long-horizon research tasks from post-August-2025 Physical Review Letters papers across five subfields, with recency as contamination control; the best of six frontier LLMs scores below 50 of 100.
- **Trace-aligned instrument control.** [EnvTrace](../works/envtrace.md) evaluates LLM-generated synchrotron-beamline control code by executing it against a digital twin and aligning execution traces — semantic correctness for code whose meaning is physical behavior — across 30+ LLMs.
- **How far do agent benchmarks generalize?** [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md) runs 1,949 tests over 53 microscopy benchmark tests and 105 agent configurations, and finds that surrogate models trained on the results do not reliably predict performance on unseen tasks.
- **Unpublished research-level challenges.** [CritPt](../works/critpt.md) has 50+ physicists author 71 unpublished, guess-resistant research challenges (decomposed into 190 checkpoint tasks) across 11+ subfields, auto-graded by a physics-customized pipeline; the best base model reaches 5.7%, rising to about 10% with coding tools.
- **Novel theory problems.** [TPBench](../works/tpbench.md) poses 57 novel, auto-verifiable theoretical-physics problems from undergraduate to research level in high-energy theory and cosmology; research-level problems remain mostly unsolved.
- **Scientist-curated research code.** [SciCode](../works/scicode.md) decomposes 80 real research coding problems into 338 subproblems across 16 natural-science subfields; the best model tested solves only 4.6% of main problems in the most realistic setting.
- **Kernel-checked formal physics.** [Lean4Physics](../works/lean4physics.md) contributes LeanPhysBench — 200 peer-reviewed Lean4 physics statements — plus the PhysLib foundation library; best results are 16% for an expert prover and 35% for Claude Sonnet 4, with PhysLib worth an average +11.75%.
- **Memorization-proof equation discovery.** [LLM-SRBench](../works/llm-srbench.md) builds 239 equation-discovery problems that either transform known physical models into unfamiliar representations or synthesize discovery-driven problems outright; the best system reaches 31.5% symbolic accuracy.
- **Undergraduate-breadth problem solving.** [UGPhysics](../works/ugphysics.md) spans 5,520 leakage-screened bilingual problems over 13 subjects, judged by its MARJ pipeline; the best of 31 LLMs reaches 49.8%.
- **Original problems with a continuous metric.** [PHYBench](../works/phybench.md) writes 500 original high-school-to-olympiad problems and grades symbolic answers by Expression Edit Distance; Gemini 2.5 Pro reaches 36.9% versus 61.9% for human experts.
- **Vision-essential physics.** [SeePhys](../works/seephys.md) makes 75% of its middle-school-to-PhD problems unanswerable without the diagram, across 21 diagram categories; top visual reasoning models stay below 60% accuracy.
- **Official olympiad marking.** [HiPhO](../works/hipho.md) grades 30 (M)LLMs on the 13 latest high-school physics olympiad exams using official marking schemes and medal thresholds; closed-source reasoning MLLMs reach 6–12 gold medals while most models remain far from full marks.
- **The frontier academic reference point.** [Humanity's Last Exam](../works/hle.md) sets 2,500 globally expert-authored questions across dozens of subjects at the frontier of human knowledge — retrieval-resistant, automatically gradable, and calibration-scored. A general academic benchmark rather than an agent benchmark, it is the difficulty ceiling that research-level scientific benchmarks position themselves against.
- **University-curriculum problem solving.** [PHYSICS](../works/physics-benchmark.md) curates 1,297 expert-annotated university-level problems across six core physics areas with a robust automated evaluation system; the most advanced model tested, o3-mini, reaches only 59.9%.
- **Rubric-decomposed AI-paper replication.** [PaperBench](../works/paperbench.md) has agents replicate 20 ICML 2024 Spotlight and Oral papers from scratch, graded by an LLM judge against author-co-developed hierarchical rubrics totaling 8,316 gradable tasks — with the judge itself separately benchmarked; the best agent scores 21.0% and ML PhDs still lead.
- **Reproducibility from provided artifacts.** [CORE-Bench](../works/core-bench.md) isolates computational reproducibility — rerunning 90 papers from their own code and data across three disciplines and 270 tasks; the best baseline agent reaches 21% on the hardest level.
- **Expert-anchored genomics pipelines.** [GenoTEX](../works/genotex.md) evaluates agents on gene-trait association analysis — dataset selection, preprocessing, statistics — against expert-curated reference pipelines from bioinformaticians (1,384 problems over 911 datasets per the official repository).
- **Real-notebook bioinformatics scenarios.** [BixBench](../works/bixbench.md) turns 50+ published analyses into open-ended exploratory agent tasks with containerized execution; frontier models reach only 17% open-answer accuracy and no better than random on multiple choice.
- **Pipelines with perturbation robustness.** [BioAgent Bench](../works/bioagent-bench.md) grades end-to-end bioinformatics pipelines (RNA-seq, variant calling, metagenomics) from output artifacts and stresses agents with corrupted inputs, decoy files, and prompt bloat; correct pipeline construction does not guarantee reliable step-level reasoning.
- **Sandboxed biomedical coding at scale.** [MedAgentGym](../works/medagentgym.md) executes 72,413 verifiable coding task instances across 129 categories from 12 real biomedical scenarios, benchmarking 29 LLMs (and doubling as an RL training environment).
- **Deterministic single-cell grading.** [scBench](../works/scbench.md) hands agents pre-step snapshots of real scRNA-seq data across six platforms and grades result recovery deterministically; accuracy spans 29–53% and platform choice matters as much as model choice.
- **Long-horizon single-cell discovery.** [scBench-Long](../works/scbench-long.md) asks agents to recover published conclusions from near-raw data with no prescribed methods, graded via controlled answer vocabularies; the best model-harness pair passes 25.4% of runs.
- **Spatial biology with the harness as a variable.** [SpatialBench](../works/spatialbench.md) applies the same deterministic-snapshot design to five spatial technologies (base models 20–38%) and argues harness design must be evaluated as a first-class object.
- **AI-scientist tasks with a human baseline.** [BAISBench](../works/baisbench.md) scores cell-type annotation on 15 expert-labeled datasets and 193 discovery MCQs from 41 published studies against six graduate-level bioinformaticians.
- **Agents as biomedical ML engineers.** [BioXArena](../works/bioxarena.md) runs 76 end-to-end ML tasks across 9 biomedical domains under a standardized 2h/1-GPU budget with hidden labels; the best of 11 configurations averages 0.666 and none dominates everywhere.
- **Protocol reasoning at corpus scale.** [BioProBench](../works/bioprobench.md) expands 22,413 wet-lab protocols into 523,784 instances over five task types; models drop sharply where deep reasoning, quantitative precision, or safety awareness is demanded.
- **A systems-biology dry lab.** [SciGym](../works/scigym.md) has agents iteratively design experiments on hidden SBML-encoded systems and submit mechanistic hypotheses; performance declines significantly with system complexity.
- **Research-practice biology QA.** [LAB-Bench](../works/lab-bench.md) measures the daily verbs of biology research — literature, figures, databases, protocols, sequences, cloning — over 2,400+ questions with human-expert baselines.
- **The realism-hardened successor.** [LABBench2](../works/labbench2.md) reprises those capabilities over real PDFs, images, and data files; restoring realistic context costs models 26–46 accuracy points.
- **Budgeted molecular design.** [SMDD-Bench](../works/smdd-bench.md) poses 502 guaranteed-solvable, multi-turn drug-design tasks over 102 protein targets under a limited oracle-call budget; GPT-5.4 solves only 40.2%.
- **Knowledge-graph auditing.** [BioKGBench](../works/biokgbench.md) composes claim verification and KGQA into the agentic KGCheck task — interrogating biomedical KGs for factual errors — and surfaces 90+ real errors in production databases.
- **Live-source medical deep research.** [MedBrowseComp](../works/medbrowsecomp.md) requires multi-hop synthesis across live trials registries, regulatory records, patents, and cost data on 1,000+ physician-curated questions.
- **Sequential clinical encounters.** [AgentClinic](../works/agentclinic.md) converts medical QA into moderated doctor-patient interaction with tools and modeled biases; accuracy drops below a tenth of static-QA levels.
- **A FHIR virtual EHR.** [MedAgentBench](../works/medagentbench.md) runs 300 physician-written tasks against production healthcare APIs over 100 realistic patient profiles; the best model reaches 69.67%.
- **Costed sequential diagnosis.** [SDBench](../works/sdbench.md) recasts 304 NEJM-CPC cases as gatekeeper-mediated encounters scored on the accuracy-cost frontier, with a 21-physician baseline at 20% mean accuracy.
- **Predicting experimental outcomes.** [BrainBench](../works/brainbench.md) tests whether models can tell real from result-altered neuroscience abstracts by perplexity; LLMs surpass human experts, with calibrated confidence — a static benchmark documented for its forecasting methodology.
- **The solver as the generated artifact.** [CodePDE](../works/codepde.md) frames PDE solving as LLM code generation and evaluates reasoning, debugging, self-refinement, and test-time scaling on representative PDE problems — the founding evaluation of the LLM-writes-the-solver paradigm.
- **Staged solver-generation gates.** [PDEAgent-Bench](../works/pdeagent-bench.md) poses 645 PDE-to-solver instances across 11 PDE families and three FEM libraries, with sequential executability → accuracy → efficiency checks; pass rates drop substantially once accuracy and efficiency are enforced.
- **Runs but solves the wrong physics.** [MooseBench](../works/moosebench.md) supplies 220 multiphysics cases with PDE-level ground truth; its Intent Fidelity Score reconstructs the encoded PDE and shows 39–40% of cases stay runnable-but-wrong under execution-only repair.
- **Digital twins from dialogue.** [SimBench](../works/simbench.md) compares 33+ simulator-oriented LLMs on multi-turn digital-twin generation for the Chrono multi-physics simulator, judged under rules with human-in-the-loop guidance.
- **Coding agents on scientific repositories.** [AInsteinBench](../works/ainsteinbench.md) derives tasks from maintainer-authored pull requests in six production scientific codebases — quantum chemistry to numerical relativity and fluid dynamics — with test-driven verification in executable environments.
- **Engineering E2E versus artifact plausibility.** [StructureClaw](../works/structureclaw.md) runs 150 structural-engineering scenarios against frozen reference solver responses; generic execution passes the model-artifact check 87.0% of the time but reaches only 22.0% end-to-end success.
- **Coursework-calibrated FEM coding.** [FEM-Bench](../works/fem-bench.md) verifies function and unit-test writing on 33 graduate-course computational-mechanics tasks over five attempts each; the best model completes 26/33 all five times.
- **Clarification before computation.** [SciConvBench](../works/sciconvbench.md) scores multi-turn disambiguation and inconsistency resolution of ill-posed simulation requests across fluid mechanics, solid mechanics, materials science, and PDEs; the best model resolves only 52.7% of fluid-mechanics disambiguation cases.
- **From intent to PDE control.** [PDE-Controller](../works/pde-controller.md) evaluates autoformalization (natural language to signal temporal logic), reasoning, and program synthesis for controlling heat- and wave-equation systems, with human-written cases plus 2M synthetic samples.
- **Approximation as the tested skill.** [HARDMath](../works/hardmath.md) auto-generates graduate asymptotics problems validated against numerical ground truth; GPT-4 reaches only 43.8% with few-shot chain-of-thought.
- **Recomputed grid studies.** [PowerAgentBench-SS](../works/poweragentbench-ss.md) has agents run power-system contingency studies whose reports a hidden evaluator re-derives, with false-safe penalties and severity regret pricing unsupported "all clear" claims.
- **Calibrating an operational forecast model.** [HydroAgent](../works/hydroagent.md) benchmarks nine frontier agents on calibrating the NWS-operational CREST hydrologic model by Nash–Sutcliffe Efficiency; only one model on one gauge reaches the human-expert reference.
- **Chemist-baselined QA at scale.** [ChemBench](../works/chembench.md) scores LLMs on 2,700+ curated chemistry QA pairs against a recruited chemist cohort; the best models beat the best human chemists on average while remaining overconfident on basic tasks.
- **A professional-requirements taxonomy.** [ChemEval](../works/chemeval.md) organizes chemical capability into 4 progressive levels and 12 dimensions over 42 tasks, exposing the trade-off between general models (literature, instructions) and chemistry-specialized ones (deep knowledge).
- **Operations, not answers.** [ChemCoTBench](../works/chemcotbench.md) frames molecular transformations as modular add/delete/substitute operations so intermediate reasoning steps are evaluable, over 1,495 samples in property optimization and reaction prediction.
- **Symbolically verifiable structure reasoning.** [MolecularIQ](../works/moleculariq.md) admits only tasks checkable against the molecular graph itself, eliminating literature-label leakage and localizing failures to specific structures.
- **The reasoning-mode jump, measured.** [ChemIQ](../works/chemiq.md) poses 816 tool-free organic-chemistry short answers with programmatic checking; reasoning models reach 50–57% where non-reasoning models manage 3–7%.
- **Functional-group-level attribution.** [FGBench](../works/fgbench.md) asks which of 245 functional groups drives a property difference, across 625K generated problems with a 7K curated benchmark subset.
- **Quantitative chemistry, shortcut-proofed.** [QCBench](../works/qcbench.md) spans 350 calculation problems in 7 subfields and 3 tiers; 24 LLMs degrade consistently as complexity rises.
- **Spectra-to-structure as a staged puzzle.** [MolPuzzle](../works/molpuzzle.md) decomposes elucidation into understanding, spectrum interpretation, and construction; GPT-4o exactly matches ground truth just 1.4% of the time, far below humans.
- **Elucidation as experiment planning.** [MolQuest](../works/molquest.md) makes agents choose which spectra to acquire in a multi-turn abductive loop; SOTA models reach only about 50% accuracy.
- **One-to-many molecule generation.** [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md) checks open-domain molecule editing, optimization, and generation for instruction satisfaction rather than match to a single reference, across 31 LLMs.
- **The read–modify–write gradient.** [MolLangBench](../works/mollangbench.md) shows GPT-5 at 86.2% on structure recognition and 85.5% on editing but 43.0% on generation, with recognition tasks verifiable by construction.
- **Mechanism-level reaction reasoning.** [FukuyamaBench](../works/fukuyamabench.md) demands full elementary-step pathways for problems from a graduate mechanism textbook; the best reported system solves 8.3% exactly.
- **Fixing the retrosynthesis metric.** [ChemCensor / CREED](../works/chemcensor.md) replaces exact-match Top-K with a chemical-plausibility metric and uses the same validator to build a millions-scale training dataset.
- **Contamination-controlled hypothesis rediscovery.** [MOOSE-Chem](../works/moose-chem.md) has a pre-2024-cutoff LLM rediscover the hypotheses of 51 post-2024 chemistry papers annotated by PhD chemists into background, inspirations, and hypothesis.
- **Literature-to-database extraction.** [ChemX](../works/chemx.md) benchmarks agentic extractors against 10 expert-validated chemistry datasets, finding persistent failures on domain terminology, complex tables, and ambiguity.
- **Pricing a reaction.** [ChemCost](../works/chemcost.md) makes agents ground identities, retrieve supplier quotes, and compute reaction cost against a frozen snapshot; the strongest agents reach 50.6% within 25% relative error and degrade under noise.
- **Leakage-proof by privacy.** [onepot-Bench 0](../works/onepot-bench.md) anchors reaction-outcome and catalyst-selection evaluation to private lab-generated data, alongside cheminformatics-literacy and refusal sub-suites.
- **The VLM bottleneck in the lab.** [MaCBench](../works/macbench.md) finds vision-language models near-perfect at equipment identification and data extraction but fundamentally limited in spatial reasoning and cross-modal synthesis.
- **Failure analysis for self-driving labs.** [LabRobFail](../works/labrobfail.md) builds a failure-centric benchmark for chemical self-driving laboratories — 20,000+ trajectories with control-, physics-, and semantic-level failure injection — where a domain-specialized VLM reaches 90.83% detection and improves downstream task success as a real-time supervisor.
- **Materials-knowledge exam QA.** [MaScQA](../works/mascqa.md) tests LLM materials knowledge on 650 GATE-exam questions, with GPT-4 at ~62% and conceptual errors dominating over computational ones.
- **College-level materials reasoning.** [MatSciBench](../works/matscibench.md) poses 1,340 problems with reference solutions and images; DeepSeek-R1 reaches 75.22% on text but the best image score is 53.02%, marking multimodal reasoning as the harder frontier.
- **LLMs as property predictors.** [LLM4Mat-Bench](../works/llm4mat-bench.md) benchmarks generative chat LLMs and fine-tuned models on materials property prediction over ~1.9M crystals and 45 properties, finding task-specific models still dominate.
- **The geometric blind spot.** [MatText](../works/mattext.md) benchmarks LLMs on nine text representations of crystals and documents a "GNN-LM wall": models capture category patterns but miss coordinate information.
- **Crystal-structure spatial reasoning.** [AtomWorld](../works/atomworld.md) scores LLMs on ten verifiable atomic-structure operations, with rotation success below 12% exposing a geometric deficit.
- **Crystallography QA at model breadth.** [OpenXRD](../works/openxrd.md) evaluates 74 LLMs/MLLMs on 217 expert-curated XRD questions, showing expert-curated context beats AI-generated context at matched token counts.
- **Shortcut-resistant characterization VQA.** [MatVQA](../works/matvqa.md) tests 17 MLLMs on 1,325 questions over real microscopy and diffraction imagery, with textual shortcuts iteratively removed.
- **Stage-structured characterization.** [MatCha](../works/matcha.md) spans 1,500 questions across four research stages and 21 tasks, finding a significant human-expert gap that prompting does not close.
- **Method-organized characterization QA.** [MatQnA](../works/matqna.md) covers ten characterization methods (XPS, XRD, SEM, TEM…); frontier MLLMs already reach ~90% on objective questions.
- **Figure-level materials extraction.** [MatViX](../works/matvix.md) benchmarks multimodal extraction over 324 full-length articles into 1,688 JSON targets, grading property curves (CSS, CAS), not just entities.
- **Materials tool-use.** [MatTools](../works/mattools.md) tests whether LLMs can understand and program pymatgen — 69,225 comprehension QA plus 49 execution tasks — finding generalists beat specialists.
- **Autonomous DFT orchestration.** [AutoDFT / VASPBench](../works/vaspbench.md) benchmarks closed-loop DFT agents over 34 tasks across 9 calculation types, with AutoDFT reaching 94.1% task-level success.
- **Synthesis planning at recipe scale.** [AlchemyBench](../works/alchemybench.md) turns 17,000 expert-verified synthesis recipes into end-to-end prediction, graded by an expert-agreement-validated LLM judge.
- **Hypothesis generation for discovery.** [Materials Hypothesis Generation](../works/materials-hypothesis.md) evaluates goal-driven, constraint-guided LLM agents on materials-design hypotheses with an expert-emulating metric.
- **Verilog code generation, the canonical task.** [VerilogEval](../works/verilogeval.md) scores LLM Verilog generation on 156 HDLBits problems by simulating against golden solutions; its v2 adds spec-to-RTL, where GPT-4o reaches 63%.
- **Design-level RTL from natural language.** [RTLLM](../works/rtllm.md) grades full-design RTL generation on syntax, functionality, and design quality over 29 hand-crafted designs (50 in v2), and introduces self-planning prompting.
- **Repository-scale RTL.** [RTL-Repo](../works/rtl-repo.md) tests multi-file Verilog completion with full-repository context over 4,000+ real GitHub samples, scored by edit similarity and exact match.
- **The other HDL.** [VHDL-Eval](../works/vhdl-eval.md) benchmarks VHDL generation on 202 problems and finds Verilog-centric models transfer poorly, requiring VHDL-specific fine-tuning.
- **Comprehensive RTL design and verification.** [CVDP](../works/cvdp.md) (NVIDIA) spans 783 problems / 13 categories in both non-agentic and agentic formats; state-of-the-art models reach no more than 34% pass@1 on code generation.
- **Assertion generation, formally grounded.** [AssertionBench](../works/assertionbench.md) measures LLM hardware assertion generation on 100 OpenCores designs against formally verified references.
- **Formal-verification capabilities.** [FVEval](../works/fveval.md) (NVIDIA) decomposes hardware formal verification into three sub-tasks, validating generated assertions with the Cadence Jasper tool.
- **High-level synthesis.** [HLS-Eval](../works/hls-eval.md) evaluates LLM HLS code generation and optimization on 94 designs, graded by parseability, compilability, runnability, and synthesizability on Vitis HLS.
- **Analog design, training-free.** [AnalogCoder](../works/analogcoder.md) is an LLM agent that designs analog circuits via Python code generation, solving 20 circuits — five more than GPT-4o — over a curated benchmark.
- **Analog topology synthesis.** [AnalogXpert](../works/analogxpert.md) encodes design expertise into an LLM agent that reaches 40%/23% success on synthetic/real topology benchmarks versus GPT-4o's 3%.
- **Multimodal EE breadth.** [EEE-Bench](../works/eee-bench.md) poses 2,860 problems across 10 EE subdomains requiring circuit and diagram understanding; 17 models average 19–47%, with a "laziness" (text-over-vision) failure mode.
- **Circuit QA along the EDA flow.** [MMCircuitEval](../works/mmcircuiteval.md) organizes 3,614 multimodal QA pairs by design stage and ability, locating weakness in back-end design and complex computation.
- **Telecom knowledge.** [TeleQnA](../works/teleqna.md) benchmarks LLMs on 10,000 telecom questions from 3GPP/IEEE standards, rivaling professionals on general knowledge but faltering on standards specifications.
- **Control-system design.** [ControlAgent](../works/controleval.md) automates controller design with cooperating LLM agents, evaluated on ControlEval (500 tasks) and beating toolbox-plus-human baselines.
- **Power-grid dispatch.** [ElecBench](../works/elecbench.md) evaluates LLMs on power-dispatch scenarios with a six-metric / 24-sub-metric framework centered on grid stability and security.
- **Comprehensive EEG understanding.** [BrainBench (EEG)](../works/brainbench-eeg.md) evaluates LLMs on instruction-conditioned EEG analysis across four subsets and 17 datasets, scoring execution-grounded reports under autonomous-code and agentic paradigms (distinct from the earlier result-prediction BrainBench).
- **Rodent behavior annotation.** [Rodent-Bench](../works/rodent-bench.md) tests multimodal LLMs on annotating real rodent behavior video across neuroscience paradigms, finding no model strong enough to serve as an annotation assistant.
- **Chinese psychology examinations.** [CPsyExam](../works/cpsyexam.md) distills 4,000 questions from a 22,000-question pool along psychological-knowledge and case-analysis axes.
- **Concept-level psychology.** [ConceptPsy](../works/conceptpsy.md) annotates psychology questions to 1,383 concepts across 12 subjects, surfacing per-concept performance variation an aggregate score would hide.
- **Professional counseling knowledge.** [PsychCounsel-Bench](../works/psychcounsel-bench.md) scores LLMs on ~2,252 U.S. National Counselor Certification Exam questions against the exam's ~70% pass threshold.
- **ML engineering on Kaggle.** [MLE-bench](../works/mle-bench.md) (OpenAI) evaluates agents on 75 curated Kaggle competitions with medal-anchored scoring; o1-preview with AIDE reaches bronze in 16.9%.
- **A trainable ML-engineering gym.** [MLE-Dojo](../works/mle-dojo.md) turns 200+ Kaggle challenges into an interactive environment supporting SFT/RL, measuring iterative improvement and error-resolution efficiency.
- **ML experimentation.** [MLAgentBench](../works/mlagentbench.md) has agents read/write files, run code, and iterate to beat starter-code baselines across 13 tasks; Claude 3 Opus tops at 37.5% average success.
- **Repository-level ML code.** [ML-Bench](../works/ml-bench.md) splits 9,641 examples over 18 repos into a text-to-code track (Pass@5) and an autonomous sandbox-execution track.
- **Data-science expertise.** [DSBench](../works/dsbench.md) poses 540 multimodal, multi-table analysis and modeling tasks; the best agent solves only 34.12% of analysis tasks.
- **Data-science coding.** [DA-Code](../works/da-code.md) grades agentic data-wrangling and analytics code in an executable sandbox, where the best LLMs reach 30.5%.
- **Analytical judgment.** [BLADE](../works/blade.md) grades data-driven-science agents' choices of constructs, transformations, and models against independent expert analyses over 12 datasets.
- **Novel-method ML research.** [MLRC-Bench](../works/mlrc-bench.md) scores agents on 7 competition tasks by the fraction of the baseline-to-top-human gap they close; the best closes only 9.3%.
- **Repository reproduction.** [SUPER](../works/super.md) benchmarks setting up and executing tasks from real research repos; GPT-4o solves 16.3% end to end.
- **Full-pipeline ML research.** [MLR-Bench](../works/mlr-bench.md) evaluates 201 open-ended tasks across idea, proposal, experiment, and paper stages, and finds agents fabricate results ~80% of the time.
- **AI R&D vs human experts.** [RE-Bench](../works/re-bench.md) (METR) compares agents to 61 experts on 7 research-engineering environments under time budgets — agents 4x at 2h, humans 2x at 32h.
- **An RL gym for AI research.** [MLGym](../works/mlgym.md) (Meta) pairs a Gym environment with 13 open-ended research tasks, finding frontier agents tune hyperparameters but do not innovate.
- **Implementing novel research code.** [ResearchCodeBench](../works/researchcodebench.md) asks models to code the contributions of 2024–2025 papers; the best (Gemini-2.5-Pro) reaches 37.3%.
- **Research idea generation.** [IdeaBench](../works/ideabench.md) grounds LLMs in influential-paper context and scores generated ideas by novelty and feasibility via a two-stage framework.
- **Divergent scientific thinking.** [LiveIdeaBench](../works/liveideabench.md) evaluates single-keyword idea generation across 1,180 keywords and 22 domains, finding creativity is poorly predicted by general intelligence.
- **AI-development agents, judged by agents.** [DevAI / Agent-as-a-Judge](../works/devai.md) provides 55 AI-development tasks with 365 hierarchical requirements, evaluated by an agentic judge as reliable as humans.
- **Expert-grade neuroscience pipeline.** [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) decomposes a real fly-optogenetics research pipeline into seven expert-scored stages, finding that agents solve individual stages but not correct end-to-end discovery.
- **End-to-end data science in real environments.** [DSAgentBench](../works/dsagentbench.md) evaluates whether agents can automate the full data-science life-cycle across 275 tasks inside real computer environments (notebooks, IDEs, terminals, browsers, databases), each paired with a deterministic evaluator.
- **Scientific visualization agents.** [SciVisAgentBench](../works/scivisagentbench.md) grades 108 expert-crafted SciVis cases across seven science domains with a multimodal outcome-centric pipeline combining image metrics, code/rule verifiers, and a human-validated LLM judge.
- **Research-level proof generation.** [TCS-Bench](../works/tcs-bench.md) assembles 300 theorem-proving tasks from FOCS/STOC/SODA papers (2020–2026) and grades them with an automated verifier agent calibrated to over 90% expert agreement.
- **Evidence-bounded experimental reasoning.** [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md) tests multimodal inference over real experimental figures and data across chemistry, biology, and materials science, isolating evidence-bounded reasoning discipline from information access.
- **Statistically valid hypothesis testing.** [Fisher-R1 / P-Bench](../works/fisher-r1.md) scores whether agents select an appropriate statistical method, compute a valid p-value, and reach a correct reject/fail-to-reject conclusion on 425 tasks grounded in logged reference-code executions.
- **Human-authorized physical energy agents.** [EnergyBridge](../works/energybridge.md) couples capacity reporting, household authorization, and physical execution for residential virtual power plants, metering outcomes from region-specific EnergyPlus models.
- **VLSI physical design.** [PDAgent-Bench](../works/pdagent-bench.md) unifies task-level assessment (353 curated EDA problems) with workflow-level closed-loop physical-design flows, finding models competitive on concepts but weak on tool-centric, long-horizon execution.
- **Reliability-scored mental-health reasoning.** [MiraMind](../works/miramind.md) evaluates mental-health reasoning across six task families and 13 datasets, scoring not only outcomes but the reliability of the evidence-to-judgment reasoning trajectory.
- **Chemical process development end to end.** [CeProBench](../works/ceprobench.md) organizes process-development evaluation around knowledge, concept, and parameter: six task classes over 243 questions and 235 tasks, built from 70 technical documents (4,406 entities / 4,967 relations), 113 competition-derived process flow diagrams (986 equipment units, 1,172 connections), and 20 Aspen Plus parameter files, with the parameter tasks scored by executing candidate operating settings in Aspen Plus so that thermodynamic feasibility rather than text similarity determines the score.
- **Convergence as the pass criterion, timed against experts.** [Simona](../works/simona.md) scores 1,000 expert-written process descriptions by Simulation Convergence Rate — a design counts only if the generated flowsheet actually converges in the simulator — and reports design time on the same axis, with a human-expert baseline at 100% SCR and 8,301.91 s giving both quality and time an interpretable upper reference against the evaluated systems (80.3% for the proposed workflow, 23.4% for GPT-4o).
- **Similarity is not domain validity.** [Can Large Language Models Automate the HAZOP Process?](../works/can-large-language-models-automate-the-hazop-proce.md) separates model-level performance from process-safety performance on the same generated worksheets: all four multimodal models exceed 86% F1 against an expert-prepared HAZOP reference, yet only 0.19–0.37 of the scenarios they generate are semantically valid, and their proposed safeguards skew to procedural rather than engineered protection layers.
- **Judge ensembles calibrated against process engineers.** [PSE-Bench](../works/pse-bench.md) scores 200 open-ended process-systems-engineering questions with five independent LLM judges against seven-element rubrics, then has three domain experts re-grade the answers: agreement is Spearman rs = 0.416 with ICC = 0.793, and the judges are systematically lenient by +0.85 points on the 0–7 scale — an offset the paper reports as a calibration constant rather than leaving implicit.
- **The solver holds the ground truth in structural analysis.** A cluster of structural-engineering work grades the model the agent builds rather than the text it writes, against a reference produced by software the agent does not control. [Agentic LLMs for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md) counts a trial correct only when *every* monitored response of the generated SAP2000 model falls within 1% of a hand-built reference model — its decomposed pipeline averages 90% across ten irregular frames while GPT-5.4 and Gemini-3.1 Pro score 0% on all of them. [Toward Responsible AI in High-Stakes Domains](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) applies the same relative-error test against ETABS and keeps the bare model as a deliberate control: unaided GPT-4o lands at roughly 230–270% relative error, the same model driving OpenSeesPy through an MCP server below 1.427%. [Automating Structural Reliability Analysis with a Multi-Agent LLM Framework](../works/automating-structural-reliability-analysis-with-a.md) turns the arrangement into an architectural rule — the reliability index and failure probability are emitted only by a deterministic runner executing validated solvers, never by a language model — and [AutoBM / BMEval](../works/autobm.md) fixes the tolerance quantitatively, requiring the first-order natural period of the generated OpenSeesPy model to land within 0.30 relative error of an expert-validated reference.
- **Run-to-run stability as the metric, not an error bar.** [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md) defines its two measures over repetition itself: reliability is the correct fraction over 500 independent runs of an identical prompt, and robustness is (1 + CV)⁻¹ over the reliability values obtained as the load is walked along the beam. Llama-3.3 70B holds 93.6% reliability on a simply supported beam but falls below 10.0% on an overhang under combined loads, whereas the code-generating agent exceeds 99.0% reliability and 99.6% robustness. The surrounding cluster shares the instinct at smaller scale — ten trials per frame in [Lightweight Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md), five in [Integrating LLMs for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md), triple-trial in [LLM-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md) — and [TransportBench](../works/transportbench.md) shows accuracy and stability dissociating outright: its most accurate model, Claude 3.5 Sonnet, is also the one that abandons 16 previously correct answers when asked to double-check.
- **An industrial civil task released at scale.** [DrafterBench](../works/drafterbench.md) takes technical-drawing revision — identified as labour-intensive through interviews with more than ten North American construction companies — and builds 1,920 tasks over 46 custom drawing-manipulation tools from 100+ real revision files. Its generator crosses twelve revision task types with five binary instruction controllers (structured vs. unstructured phrasing, precise vs. vague values, complete vs. incomplete information, object and operation cardinality), so instruction quality is a controlled variable and a score drop is attributable to a specific defect; dual functions log the operation path without touching files, making the trajectory rather than the rendered drawing the scored artifact.
- **Code-compliance verdicts as the scored output.** Where a regulation governs the answer, several benchmarks score whether the agent reaches the regulator's conclusion and for the stated reason. [SGR-BIM](../works/sgr-bim.md) poses 679 expert-verified fire-safety queries over five IFC building models on a three-tier accuracy scale that withholds full credit from a correct conclusion reached without naming the governing variables and boundary conditions; the graph-based system reaches 84.3 overall against 75.7 for a single agent holding the identical toolset and 64.9–73.2 for CAMEL, AutoGen and MetaGPT, so generic multi-agent coordination is shown not to be what closes the gap. [AutoBM / BMEval](../works/autobm.md) makes an explicit design-verification conclusion one of three gates conjoined by Pass@k_strict, and [AEC-Bench](../works/aec-bench.md) finds the judgment-heavy end of the work hardest — drawing navigation reaches 100.0 reward while submittal review tops out at 23.1.
- **Professional inspection records as the answer standard.** [BridgeEQA](../works/bridgeeqa.md) grounds 2,200 questions over 200 real bridge scenes in Vermont Agency of Transportation inspection reports, scores condition verdicts on the NBI 0–9 scale with a within-±1 band because expert inspectors themselves agree only that closely, and adds Image Citation Relevance so an agent reaching the right rating from irrelevant imagery is penalised. [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) scores against deterioration actually observed across six annual National Bridge Inventory releases and treats outcome definition as an experimental variable — the agent is near-random (AUC 0.471) on a vague target but reaches 0.705 on crossing into poor condition, where an opaque gradient-boosted learner manages 0.521 — with a certified inspector blind-rating 100 of its written rationales at a mean 2.77 of 3. [DefectBench](../works/defectbench.md) escalates facade pathology through naming, locating and segmenting the defect, conditioning each question on the model's own prior answer so error propagation is exposed rather than hidden.
- **Professional licensure as the difficulty scale.** [Evaluating AI Chatbots on the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md) put NCEES practice questions to ChatGPT-4 and Bard under the exams' own binary no-partial-credit scheme, reporting 70.9% / 46.2% and 39.2% / 41% on the FE and PE respectively — plausibly passing the FE, far from the PE. [PE Civil Bench](../works/pe-civil-bench.md) turns that source into a released 150-problem corpus over eight subdisciplines and makes augmentation strategy a first-class factor, running the same items under base prompting, vector RAG and agentic RAG. [Civil-Eval](../works/civil-eval.md) does the same for the Chinese national registration examinations, weighting each subject by its share of calculation-heavy questions, and [AECBench](../works/aecbench.md) draws part of its 4,800 items from licensure examinations while arranging all 23 tasks along five cognition levels, so a single score becomes a degradation curve from above 95% on terminology to below 60% on document creation.

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
| CMT-Benchmark | 2025 | 50 problems authored by expert researchers at the level of their own work | Condensed matter theory: quantum many-body and classical statistical mechanics | Programmatic checking against expert ground truth; normal-ordered symbolic comparison of non-commuting operators | [→](../works/cmt-benchmark.md) |
| CMPhysBench | 2025 | 520+ curated graduate-level calculation problems | Condensed matter physics: magnetism, superconductivity, strongly correlated systems | SEED expression edit distance (partial credit) plus binary accuracy | [→](../works/cmphysbench.md) |
| MDArena | 2026 | 50 containerized tasks sourced from active research projects | Molecular dynamics: 29 molecular systems, 14 research protocols | Strict-Pass@1 plus correctness and process-reward partial credit | [→](../works/mdarena.md) |
| MetaSyn | 2026 | 422 expert-conducted meta-analyses from 34,000+ Nature Portfolio articles | Systematic review spanning physics, chemistry, psychology, medical science | Study identification against the original reviewers' included set; stage-wise pipeline evaluation | [→](../works/metasyn.md) |
| PhySciBench | 2026 | 200 expert-curated deep-research questions | Physical sciences: physics and chemistry, six task categories | Accuracy-based comparison of models and agent systems | [→](../works/physcibench.md) |
| ScholarQuest | 2026 | Queries from 1,000+ computer science topics across four research intents | Computer science literature search | Recall@100 and Recall@All against ground-truth paper sets | [→](../works/scholarquest.md) |
| SciExplore | 2026 | 103 expert-curated tasks in four progressive task types | Scientific information seeking across 10+ disciplines | Accuracy across progressive task types, from database navigation to structured synthesis | [→](../works/sciexplore.md) |
| RealPDEBench | 2026 | 5 real-world measured datasets with paired numerical simulations | Complex physical systems (fluid–structure interaction, cylinder/foil flows, combustion); scientific ML models, not LLM agents | 8 data-oriented and physics-oriented metrics over 3 sim-vs-real tasks; 10 baselines | [→](../works/realpdebench.md) |
| Gravity-Bench-v1 | 2025 | Simulated two-body systems incl. out-of-distribution physics | Gravitational-physics discovery under an observation budget | Reference solutions from rigorous dynamics simulations, calibrated against human expertise | [→](../works/gravity-bench.md) |
| PhysGym | 2025 | 97 problems sourced from PHYBench, run as interactive simulations | Physics discovery under four controlled prior-knowledge levels | Standardized protocols for hypothesis accuracy and model fidelity | [→](../works/physgym.md) |
| DiscoverPhysics | 2026 | 22 counterfactual N-body worlds generated on demand | Laws of motion in deliberately non-standard physics | Held-out trajectory MSE + rubric-based LLM-judged explanation score | [→](../works/discoverphysics.md) |
| FEABench | 2025 | Multiphysics problems solved via the COMSOL Multiphysics API | Finite-element multiphysics simulation | Evaluation over generated API calls and computed answers; executability metric | [→](../works/feabench.md) |
| QMP-Bench | 2026 | 100 tasks extracted from 21 high-impact journals | Quantum many-body simulation | Programming verifiers plus principle-based scientific verifiers | [→](../works/qmp-bench.md) |
| gwBenchmarks | 2026 | 8 tasks over data representing 10⁸+ core-hours of compute | Gravitational-wave astronomy at ≲10⁻⁴ relative error | External pre-defined evaluation framework with per-task physics metrics | [→](../works/gwbenchmarks.md) |
| ReplicationBench | 2025 | 111 tasks from 20 papers, co-developed with the original authors | Astrophysics paper replication | Objective per-task scoring of faithfulness and correctness | [→](../works/replicationbench.md) |
| PRL-Bench | 2026 | 100 curated post-Aug-2025 PRL papers, expert-validated | Frontier physics research across 5 subfields | Objectively verifiable outcomes; 0–100 scoring | [→](../works/prl-bench.md) |
| EnvTrace | 2025 | Beamline control-code generation at synchrotron facilities | Instrument control for experimental physics | Execution-trace alignment against a digital twin | [→](../works/envtrace.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | 53 microscopy tests × 105 agent configurations | Self-driving microscopy / materials characterization | Trace-logged benchmark tests; latency, cost, and failure-mode comparison | [→](../works/agentic-microscopy-benchmarks.md) |
| CritPt | 2025 | 71 unpublished challenges + 190 checkpoints by 50+ physicists | Research-entry physics across 11+ subfields | Guess-resistant, machine-verifiable answers; customized automated grading | [→](../works/critpt.md) |
| TPBench | 2025 | 57 novel problems, undergraduate to research level | Theoretical physics: high-energy theory and cosmology | Auto-verifiable answers with tailored grading | [→](../works/tpbench.md) |
| SciCode | 2024 | 80 main / 338 subproblems curated by scientists | 16 natural-science subfields (math, physics, chemistry, biology, materials) | Execution against scientist-annotated gold solutions and tests | [→](../works/scicode.md) |
| Lean4Physics | 2025 | 200 peer-reviewed Lean4 statements from textbooks and competitions | College physics as formal theorem proving | Lean4 kernel proof checking; no judge in the loop | [→](../works/lean4physics.md) |
| LLM-SRBench | 2025 | 239 problems in two classes: LSR-Transform and LSR-Synth | Scientific equation discovery across four domains | Symbolic accuracy against ground-truth equations | [→](../works/llm-srbench.md) |
| UGPhysics | 2025 | 5,520 bilingual undergraduate problems, leakage-screened | Undergraduate physics across 13 subjects | MARJ model-assistant rule-based judgment | [→](../works/ugphysics.md) |
| PHYBench | 2025 | 500 original problems, high school to olympiad | Physics problem solving with symbolic answers | Expression Edit Distance (EED) plus accuracy; human-expert baseline | [→](../works/phybench.md) |
| SeePhys | 2025 | 2,000 validated questions (official page), middle school to PhD | Vision-essential physics: 7 domains, 21 diagram types | Accuracy on multimodal problem solving | [→](../works/seephys.md) |
| HiPhO | 2025 | 13 latest (2024–25) olympiad exams, international and regional | High-school olympiad physics, mixed modalities | Official marking schemes at answer and step level; medal thresholds | [→](../works/hipho.md) |
| Humanity's Last Exam | 2025 | 2,500 questions by global subject-matter experts | Frontier academic knowledge across dozens of subjects; not agent-specific | Automated grading of unambiguous solutions; accuracy and calibration | [→](../works/hle.md) |
| PHYSICS | 2025 | 1,297 expert-annotated university problems | University physics: six core areas | Robust automated evaluation system | [→](../works/physics-benchmark.md) |
| PaperBench | 2025 | 20 ICML 2024 Spotlight/Oral papers, author-co-developed rubrics | AI-research replication; 8,316 gradable rubric tasks | LLM judge against hierarchical rubrics, with the judge separately benchmarked | [→](../works/paperbench.md) |
| CORE-Bench | 2024 | 270 tasks from 90 papers with provided code and data | Computational reproducibility: computer science, social science, medicine | Accuracy of reproduced results via a parallelizable harness | [→](../works/core-bench.md) |
| GenoTEX | 2024 | Expert-curated gene-trait association pipelines (1,384 problems / 911 datasets, official repository) | Computational genomics and bioinformatics | Comparison against bioinformatician-curated reference analyses | [→](../works/genotex.md) |
| BixBench | 2025 | 50+ scenarios from published analyses, ~300 open-answer questions | Computational biology data analysis | LLM-graded open answers + exact-match MCQ, containerized execution | [→](../works/bixbench.md) |
| BioAgent Bench | 2026 | Manually curated end-to-end pipelines (RNA-seq, variant calling, metagenomics) | Bioinformatics workflows | LLM grader over output artifacts; perturbation robustness suite | [→](../works/bioagent-bench.md) |
| MedAgentGym | 2025 | 72,413 instances / 129 categories from 12 real biomedical scenarios | Biomedical data-science coding | Verifiable ground truth in executable sandboxes | [→](../works/medagentgym.md) |
| scBench | 2026 | 394 verifiable problems, six platforms, seven categories | Single-cell RNA-seq analysis | Deterministic grading of biological-result recovery | [→](../works/scbench.md) |
| scBench-Long | 2026 | 21 evaluations from raw or near-raw data, no prescribed methods | Long-horizon single-cell biology | Controlled answer vocabularies; deterministic grading + trajectory rubrics | [→](../works/scbench-long.md) |
| SpatialBench | 2025 | 146 verifiable problems, five spatial technologies | Spatial transcriptomics analysis | Deterministic grading of biological-result recovery | [→](../works/spatialbench.md) |
| BAISBench | 2025 | 15 expert-labeled datasets + 193 MCQs from 41 published studies | Single-cell omics discovery | Hierarchical cell-type-tree annotation scoring + MCQ vs. published conclusions | [→](../works/baisbench.md) |
| BioXArena | 2026 | 76 end-to-end ML tasks across 9 biomedical domains | Multi-modal biomedical machine learning | Hidden labels, held-out graders, biology-aware 0–1 metrics; 2h/1-GPU budget | [→](../works/bioxarena.md) |
| BioProBench | 2025 | 523,784 instances from 22,413 human-written protocols | Wet-lab protocol understanding and reasoning | Task-specific metrics incl. step recall/precision and Kendall's tau | [→](../works/bioprobench.md) |
| SciGym | 2025 | 137 evaluated (350 released) hidden SBML systems | Systems-biology experiment design | Recovered models compared against hidden ground-truth systems | [→](../works/scigym.md) |
| LAB-Bench | 2024 | 2,400+ MCQs in 8 categories incl. ProtocolQA and CloningScenarios | Biology research practice | MCQ scoring against human-expert baselines | [→](../works/lab-bench.md) |
| LABBench2 | 2026 | ~1,900 tasks over realistic PDFs, images, and data files | Biology research practice, hardened | Accuracy via released harness; −26% to −46% vs. LAB-Bench | [→](../works/labbench2.md) |
| SMDD-Bench | 2026 | 502 guaranteed-solvable tasks over 102 protein targets | Small-molecule drug design | Solve rate under a limited oracle-call budget | [→](../works/smdd-bench.md) |
| BioKGBench | 2024 | 2,000+ atomic instances + 225 annotated KGCheck instances | Biomedical knowledge graphs | Claim verification, KGQA, and agentic error-finding | [→](../works/biokgbench.md) |
| MedBrowseComp | 2025 | 1,000+ physician-curated multi-hop questions | Live medical knowledge bases | Gold-answer checking over live retrieval | [→](../works/medbrowsecomp.md) |
| AgentClinic | 2024 | Simulated encounters, nine specialties, seven languages | Clinical diagnosis as sequential decision-making | Diagnostic accuracy under moderated multi-agent dialogue with bias perturbations | [→](../works/agentclinic.md) |
| MedAgentBench | 2025 | 300 physician-written tasks over 100 patient profiles | FHIR virtual EHR operation | Programmatic success checking against reference solutions | [→](../works/medagentbench.md) |
| SDBench | 2025 | 304 NEJM-CPC cases as gatekeeper-mediated encounters | Sequential clinical diagnosis with costs | Diagnostic accuracy paired with cost of visits and tests | [→](../works/sdbench.md) |
| BrainBench | 2024 | 200 original-vs-altered neuroscience abstract pairs (official dataset) | Neuroscience outcome prediction | Two-alternative forced choice; perplexity for LLMs, expert humans with confidence | [→](../works/brainbench.md) |
| CodePDE | 2025 | Representative PDE problems posed as solver-generation tasks | LLM-written numerical PDE solvers | Generated-solver accuracy vs. reference solutions; reasoning/debugging/refinement/scaling axes | [→](../works/codepde.md) |
| PDEAgent-Bench | 2026 | 645 instances, 6 math categories, 11 PDE families, 3 FEM libraries | Finite-element solver generation | Staged executability → numerical accuracy → efficiency checks with case-specific targets | [→](../works/pdeagent-bench.md) |
| MooseBench | 2026 | 220 MOOSE multiphysics cases with PDE-level ground truth | Multiphysics simulation-code generation | Intent Fidelity Score via deterministic PDE reconstruction | [→](../works/moosebench.md) |
| SimBench | 2024 | 102 demonstration tasks over 34 physical systems (official repository) | Digital-twin generation for the Chrono simulator | LLM-judge scoring with predefined rules and human-in-the-loop guidance | [→](../works/simbench.md) |
| AInsteinBench | 2025 | Maintainer-PR tasks from 6 production scientific repositories | Scientific software engineering (quantum chemistry to fluid dynamics) | Test-driven verification in executable environments | [→](../works/ainsteinbench.md) |
| StructureClaw | 2026 | 150 controlled scenarios: standard, interactive, multimodal reconstruction | Structural-engineering workflows | Strict model matching + numerical agreement with frozen reference solver responses (E2E Success) | [→](../works/structureclaw.md) |
| FEM-Bench | 2025 | 33 graduate-course tasks, function and unit-test tracks, five attempts | Computational mechanics code generation | Objective verification; Average Joint Success Rate | [→](../works/fem-bench.md) |
| SciConvBench | 2026 | Ill-posed simulation requests in four computational-science domains | Multi-turn clarification for task formulation | Rubric framework: clarification behavior, grounding, final-specification fidelity | [→](../works/sciconvbench.md) |
| PDE-Controller | 2025 | Human-written cases + 2M synthetic samples for heat/wave control | PDE control via STL autoformalization | Metrics over reasoning, autoformalization, program synthesis; utility gain | [→](../works/pde-controller.md) |
| HARDMath | 2024 | Auto-generated asymptotics problems; 366-problem mini test set | Graduate applied mathematics (approximation techniques) | Accuracy vs. numerically validated ground truths | [→](../works/hardmath.md) |
| PowerAgentBench-SS | 2026 | IEEE 39-bus variants; DC thermal N-2 contingency-search pilot | Power-system steady-state agent studies | Hidden evaluator recomputes physical validity; recall variants, false-safe penalties, severity regret | [→](../works/poweragentbench-ss.md) |
| HydroAgent | 2026 | Calibration of the operational CREST model on 4 held-out gauges | Hydrologic model calibration by agents | Nash–Sutcliffe Efficiency vs. a human-expert reference | [→](../works/hydroagent.md) |
| ChemBench | 2024 | 2,700+ expert-curated question–answer pairs | Chemical knowledge and reasoning vs. human chemists | Automated framework scoring with a human-chemist baseline and confidence analysis | [→](../works/chembench.md) |
| ChemEval | 2024 | Open-source data plus expert-crafted tasks | Chemistry: 4 progressive levels, 12 dimensions, 42 tasks | Zero-/few-shot evaluation with curated prompts | [→](../works/chemeval.md) |
| ChemCoTBench | 2025 | 1,495 samples across 22 tasks as modular chemical operations | Molecular property optimization and reaction prediction | Structured step-wise evaluation over annotated operation workflows | [→](../works/chemcotbench.md) |
| MolecularIQ | 2026 | Symbolically verifiable molecular-graph tasks | Molecular structure reasoning | Symbolic verification against the molecular graph | [→](../works/moleculariq.md) |
| ChemIQ | 2025 | 816 short-answer organic-chemistry questions | Organic chemistry incl. NMR structure elucidation | Judge-free programmatic checking (exact match, OPSIN, canonical SMILES) | [→](../works/chemiq.md) |
| FGBench | 2025 | 625K generated problems; 7K curated evaluation subset | Functional-group-level molecular property reasoning | Regression and classification against dataset labels | [→](../works/fgbench.md) |
| QCBench | 2025 | 350 quantitative problems across 7 chemistry subfields | Quantitative and computational chemistry | Tiered accuracy on shortcut-resistant stepwise calculation | [→](../works/qcbench.md) |
| MolPuzzle | 2024 | 200 elucidation instances, 23,678 examples in 3 stages | Structure elucidation from IR/MS/NMR spectra | Exact-match accuracy per stage with a human baseline | [→](../works/molpuzzle.md) |
| MolQuest | 2026 | Multi-turn interactive elucidation episodes | Structure elucidation with model-planned experiments | Accuracy of final structures (SOTA ≈50%) | [→](../works/molquest.md) |
| Speak-to-Structure (TOMG-Bench) | 2024 | Open-domain molecule-generation instructions (MolEdit/MolOpt/MolCustom) | Natural-language-driven molecule design | One-to-many instruction-satisfaction checking | [→](../works/tomg-bench.md) |
| MolLangBench | 2025 | Cheminformatics-constructed and expert-annotated tasks | Language-prompted structure recognition, editing, generation | Per-task accuracy; recognition verifiable by construction | [→](../works/mollangbench.md) |
| FukuyamaBench | 2026 | Problems from Fukuyama's Advanced Organic Reaction Mechanism book | Hierarchical reaction-mechanism reasoning | Exact pathway match (best reported 8.3%) | [→](../works/fukuyamabench.md) |
| ChemCensor / CREED | 2026 | Millions of validated reaction records | Single-step retrosynthesis evaluation | ChemCensor chemical-plausibility metric instead of exact-match Top-K | [→](../works/chemcensor.md) |
| MOOSE-Chem | 2024 | 51 post-2024 chemistry papers annotated by PhD chemists | Chemistry hypothesis rediscovery | Similarity to ground-truth hypotheses under a knowledge-cutoff control | [→](../works/moose-chem.md) |
| ChemX | 2025 | 10 expert-validated extraction datasets | Chemical information extraction (nanomaterials, small molecules) | Extraction quality against expert-validated records | [→](../works/chemx.md) |
| ChemCost | 2026 | 1,427 reactions over a frozen pricing snapshot (230,775 supplier quotes) | Chemical procurement and cost reasoning | Judge-free exact ground truth with stage-level failure diagnosis | [→](../works/chemcost.md) |
| onepot-Bench 0 | 2026 | Proprietary suite incl. private lab-generated data | Cheminformatics literacy, refusal behavior, reaction-outcome prediction | Per-suite scoring against private experimental ground truth | [→](../works/onepot-bench.md) |
| MaCBench | 2024 | Multimodal chemistry and materials tasks | Data extraction, experimental understanding, results interpretation | Accuracy via the ChemBench pipeline | [→](../works/macbench.md) |
| LabRobFail | 2026 | Simulated chemical self-driving-lab failure trajectories (Isaac Sim) | Laboratory-robot failure analysis for self-driving chemistry | Six capabilities incl. detection (90.83%) and temporal localization | [→](../works/labrobfail.md) |
| MaScQA | 2023 | 650 GATE-exam materials & metallurgy questions | Materials-science knowledge QA | Accuracy with a conceptual-vs-computational error taxonomy; GPT-4 ~62% | [→](../works/mascqa.md) |
| MatSciBench | 2025 | 1,340 college-level problems (946 solved, 315 with images) | Materials reasoning across subdisciplines | Accuracy on text and image questions; DeepSeek-R1 75.22% / GPT-5 53.02% | [→](../works/matscibench.md) |
| LLM4Mat-Bench | 2024 | ~1.9M crystals, 45 properties, 3 text modalities | Materials property prediction | MAD:MAE (regression) and AUC (classification); generative LLMs near-random | [→](../works/llm4mat-bench.md) |
| MatText | 2024 | 9 crystal text representations, up to 70B params / 2M structures | Crystal property prediction from text | Regression error vs. GNN baselines; the "GNN-LM wall" | [→](../works/mattext.md) |
| AtomWorld | 2025 | 10 atomic-structure actions across 4 modelling categories | Crystal-structure spatial reasoning | Verifiable structure checks; rotation success below 12% | [→](../works/atomworld.md) |
| OpenXRD | 2025 | 217 expert-curated XRD questions, 74 models | Crystallography (XRD) QA | Closed- vs open-book accuracy; expert vs AI-generated context | [→](../works/openxrd.md) |
| MatVQA | 2025 | 1,325 questions, 17 MLLMs, real microscopy/diffraction | Materials characterization visual reasoning | Accuracy across 4 SPP tasks with shortcut removal | [→](../works/matvqa.md) |
| MatCha | 2025 | 1,500 questions across 4 stages / 21 tasks | Materials characterization understanding | Accuracy with a human-expert baseline; prompting does not close the gap | [→](../works/matcha.md) |
| MatQnA | 2025 | 10 characterization methods (XPS/XRD/SEM/TEM…) | Materials characterization and analysis | Objective + subjective QA; frontier MLLMs ~90% objective | [→](../works/matqna.md) |
| MatViX | 2024 | 324 full-length articles → 1,688 structured JSON | Materials data extraction (text/tables/figures) | F1 for compositions; Curve Similarity/Alignment scores for property curves | [→](../works/matvix.md) |
| MatTools | 2025 | 69,225 comprehension QA + 49 tasks / 138 subtasks | Materials computational tool-use (pymatgen) | Tool-comprehension accuracy + execution-verified code generation | [→](../works/mattools.md) |
| AutoDFT / VASPBench | 2026 | 34 tasks across 9 DFT calculation types | Autonomous DFT workflow orchestration | Task-level success (94.1% with GPT-5.2) + property accuracy vs databases | [→](../works/vaspbench.md) |
| AlchemyBench | 2025 | 17,000 expert-verified synthesis recipes | Materials synthesis planning | Expert-agreement-validated LLM-as-a-Judge over free-form predictions | [→](../works/alchemybench.md) |
| Materials Hypothesis Generation | 2025 | Goals/constraints/methods curated from recent publications | Materials-discovery hypothesis generation | A scalable expert-emulating evaluation metric | [→](../works/materials-hypothesis.md) |
| VerilogEval | 2023 | 156 HDLBits Verilog problems | Verilog RTL code generation | Simulation vs. golden solution; pass@k | [→](../works/verilogeval.md) |
| RTLLM | 2023 | 29 hand-crafted RTL designs (50 in v2) | Design-level RTL generation from natural language | Three goals: syntax, functionality, design quality | [→](../works/rtllm.md) |
| RTL-Repo | 2024 | 4,000+ Verilog samples with full-repo context | Repository-scale RTL code completion | Edit similarity and exact match | [→](../works/rtl-repo.md) |
| VHDL-Eval | 2024 | 202 VHDL problems with self-verifying testbenches | VHDL code generation | Functional correctness across zero-shot / ICL / PEFT | [→](../works/vhdl-eval.md) |
| CVDP | 2025 | 783 problems / 13 categories, non-agentic + agentic (NVIDIA) | RTL design, verification, and debugging | pass@1 in a containerized OSS-EDA environment; SOTA ≤34% | [→](../works/cvdp.md) |
| AssertionBench | 2024 | 100 OpenCores designs, formally verified assertions | Hardware assertion generation | Fraction of functionally correct assertions | [→](../works/assertionbench.md) |
| FVEval | 2024 | 3 formal-verification sub-tasks (NVIDIA) | Formal verification of digital hardware | Cadence Jasper formal-tool validation | [→](../works/fveval.md) |
| HLS-Eval | 2025 | 94 HLS designs + testbenches | High-level-synthesis code generation and optimization | Parseability / compilability / runnability / synthesizability + pass@k | [→](../works/hls-eval.md) |
| AnalogCoder | 2024 | Curated analog-design task set (24 tasks) | Analog circuit design via code generation | Pass@1/Pass@5 by tasks solved; 20 circuits vs. GPT-4o's 15 | [→](../works/analogcoder.md) |
| AnalogXpert | 2024 | 30 real + 2,000 synthetic topology cases | Analog topology synthesis | One-trial correctness; 40%/23% vs. GPT-4o 3% | [→](../works/analogxpert.md) |
| EEE-Bench | 2024 | 2,860 multimodal problems across 10 EE subdomains | Multimodal electrical & electronics engineering | Accuracy over 17 LLMs/LMMs; avg 19.48–46.78% | [→](../works/eee-bench.md) |
| MMCircuitEval | 2025 | 3,614 multimodal QA across digital + analog, EDA stages | Circuit knowledge and design across the EDA flow | Accuracy by design stage, circuit type, ability, difficulty | [→](../works/mmcircuiteval.md) |
| TeleQnA | 2023 | 10,000 telecom questions from 3GPP/IEEE + research | Telecommunications knowledge | Multiple-choice accuracy vs. a telecom-professional baseline | [→](../works/teleqna.md) |
| ControlAgent / ControlEval | 2024 | 500 control-design tasks (ControlEval) | Control-system design and tuning | Average and agent success rates vs. toolbox+human baselines | [→](../works/controleval.md) |
| ElecBench | 2024 | Power-dispatch scenarios, 8 LLMs | Power-grid operation and dispatch | Six metrics / 24 sub-metrics (stability, security, ...) | [→](../works/elecbench.md) |
| BrainBench (EEG) | 2026 | Instruction-conditioned EEG analysis; 4 subsets, 17 datasets, 100K+ executions | Comprehensive EEG understanding | Numerical/categorical/set/sequence/semantic/artifact validation (CodeAct + BrainAgent) | [→](../works/brainbench-eeg.md) |
| Rodent-Bench | 2026 | Rodent behavior video (10–35 min) across paradigms; 3 MLLMs | Behavioral-neuroscience video annotation | Second-wise accuracy, macro F1, mAP, mutual information, MCC | [→](../works/rodent-bench.md) |
| CPsyExam | 2024 | 4,000 questions (from a 22,000 pool); knowledge + case-analysis axes | Psychology examination knowledge | Accuracy across subjects and both axes | [→](../works/cpsyexam.md) |
| ConceptPsy | 2023 | 12 subjects, 1,383 concepts; chapter-annotated | Concept-level psychology knowledge | Overall plus chapter-wise (per-concept) accuracy | [→](../works/conceptpsy.md) |
| PsychCounsel-Bench | 2025 | ~2,252 U.S. counselor-certification questions | Professional counseling psychology | Accuracy against the exam's ~70% pass threshold | [→](../works/psychcounsel-bench.md) |
| MLE-bench | 2024 | 75 curated Kaggle ML-engineering competitions (OpenAI) | Machine-learning engineering | Kaggle medal thresholds vs. leaderboard human baselines | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | 200+ Kaggle challenges in an interactive Gym environment | ML engineering (trainable environment) | Iterative improvement, long-horizon quality, error-resolution efficiency | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | 13 ML-experimentation tasks (CIFAR-10 to BabyLM) | ML experimentation | Success rate (>10% over starter-code baseline) and average improvement | [→](../works/mlagentbench.md) |
| ML-Bench | 2023 | 9,641 examples over 18 GitHub repos | Repository-level ML code | Pass@5 (LLM track) and success rate (agent track) | [→](../works/ml-bench.md) |
| DSBench | 2024 | 540 analysis + modeling tasks (multimodal, multi-table) | Data science | Task-solve rate and relative performance gap | [→](../works/dsbench.md) |
| DA-Code | 2024 | Agentic data-science coding in an executable sandbox | Data science (code) | Execution-based accuracy; best LLM 30.5% | [→](../works/da-code.md) |
| BLADE | 2024 | 12 datasets with research questions and expert analyses | Data-driven scientific analysis | Multifaceted grading of analytical decisions vs. expert ground truth | [→](../works/blade.md) |
| MLRC-Bench | 2025 | 7 ML research-competition tasks | ML research (novel methods) | Gap-closed vs. top human participants (objective); best 9.3% | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | 45 e2e + 152 sub + 602 auto tasks from research repos | Research reproduction | End-to-end and scenario success; GPT-4o 16.3% e2e | [→](../works/super.md) |
| MLR-Bench | 2025 | 201 open-ended ML research tasks (workshops) | Full-pipeline ML research | MLR-Judge (LLM reviewers + rubrics); ~80% fabricated results | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | 7 research-engineering environments vs. 61 human experts | AI R&D / research engineering | Best-of-k vs. reference under time budgets; direct human comparison | [→](../works/re-bench.md) |
| MLGym | 2025 | 13 open-ended AI-research tasks in a Gym (Meta) | Open-ended AI research | Task performance in the Gym over five frontier models | [→](../works/mlgym.md) |
| ResearchCodeBench | 2025 | 212 challenges implementing 2024–25 paper contributions | ML research-code implementation | Success rate with contamination controls; best 37.3% | [→](../works/researchcodebench.md) |
| IdeaBench | 2024 | Research idea generation grounded in influential papers | Research ideation | Two-stage GPT-4o ranking + relative Insight Score | [→](../works/ideabench.md) |
| LiveIdeaBench | 2024 | Single-keyword ideation; 1,180 keywords, 22 domains, 40+ models | Scientific idea generation | LLM-panel scoring on five creativity dimensions | [→](../works/liveideabench.md) |
| DevAI / Agent-as-a-Judge | 2024 | 55 AI-development tasks, 365 hierarchical requirements | Automated AI development | Requirement-level, process-aware Agent-as-a-Judge evaluation | [→](../works/devai.md) |
| A Case Study on a Neuroscience Data-to-Discovery Pipeline | 2026 | Real fly-optogenetics pipeline decomposed into 7 stages (9 released tasks) | Neuroscience (Drosophila behavior analysis) | Expert-defined per-stage criteria vs. human annotations and legacy code; Mann–Whitney U for the statistical stage | [→](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| DSAgentBench | 2026 | 275 tasks over the full data-science life-cycle in real computer environments | Data science (wrangling → modeling → validation) | Deterministic per-task evaluator of analytical correctness, visual outputs, and model performance | [→](../works/dsagentbench.md) |
| SciVisAgentBench | 2026 | 108 expert-crafted scientific-visualization cases (four-dimension taxonomy) | Scientific visualization across 7 science domains | Multimodal outcome-centric pipeline: image metrics + code/rule verifiers + human-validated LLM judge | [→](../works/scivisagentbench.md) |
| TCS-Bench | 2026 | 300 theorem-proving tasks from FOCS/STOC/SODA papers (2020–2026) | Theoretical computer science / mathematics (proof generation) | Automated verifier agent (4× Gemini 3.1 Flash, 3-of-4 vote); >90% expert agreement | [→](../works/tcs-bench.md) |
| Science Edge Evaluation (SEE) | 2026 | 1,116 expert-curated multimodal questions from literature and first-hand experimental data | Chemistry, biology, materials science | Exact-match / tolerance scoring against expert ground truth; strict binary LLM judge | [→](../works/science-edge-evaluation.md) |
| Fisher-R1 / P-Bench | 2026 | 425 hypothesis-testing tasks reproduced from expert analyses | Economics, biology, medicine (statistical inference) | Decisions and p-values checked against logged reference-code executions (Raw / Strict) | [→](../works/fisher-r1.md) |
| EnergyBridge | 2026 | Residential VPP demand-response workflow over region-specific EnergyPlus models | Energy systems (household grid flexibility) | Metered EnergyPlus outcomes: authorization rate + capacity-commitment reliability within ±20% | [→](../works/energybridge.md) |
| PDAgent-Bench | 2026 | 353 curated tasks + 10 full-flow designs from real industrial EDA artifacts | VLSI physical design / EDA | pass@1/@5 with execution-checked scripts and expert references; full-flow timing-closure / DRC outcomes | [→](../works/pdagent-bench.md) |
| MiraMind | 2025 | Six task families over 13 mental-health datasets | Mental health / psychiatry (Medicine & Health; Neuroscience & Cognitive Science) | Per-family outcome metrics plus human-validated LLM-judged reasoning-trajectory scoring | [→](../works/miramind.md) |
| CeProBench | 2026 | 6 task classes (243 questions / 235 tasks) from 70 technical documents, 113 competition-derived PFDs, and 20 Aspen Plus parameter files | Chemical process development: knowledge, concept (PFD), parameter | Aspen Plus execution for parameter tasks; entity F1 and MEC/MED, equipment and connection accuracy, Valid / Correct Rate; judged Correctness / Rationality / Clarity / Completeness | [→](../works/ceprobench.md) |
| Simona | 2026 | 1,000 process descriptions written by chemical engineering experts | Chemical process simulation: description to converging flowsheet | Simulation Convergence Rate in an in-house simulator plus design time, against LLM, multi-agent, and human-expert baselines | [→](../works/simona.md) |
| CRAFTS | 2026 | OpenIDAES-450: 450 requests paired with executable IDAES models, 82 frozen as held-out | Chemical process simulation (IDAES/Pyomo equation-oriented flowsheeting) | Staged Workflow Success contract behind deterministic IDAES/Pyomo promotion gates, plus macro-F1 on units, streams, and directed connections | [→](../works/crafts.md) |
| A Tutorial on Autonomous Fault-Tolerant Control | 2026 | Two openly released executable environments (batch mixing module, CSTR) with typed injectable faults | Process-plant fault recovery and supervisory control | Per-proposal symbolic validation (state reachability, actuator existence) and simulation-based validation in a digital twin; no model scores reported | [→](../works/ctrl-alt-recover.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | Five process-plant scenarios (three from the Tennessee Eastman Process) plus 43 crafted invalid proposals | Industrial process control and functional safety | Deterministic P&ID graph traversal per proposed action (tag existence, actuatability, fail-state, downstream impact); error-injection recall, N = 50 robustness runs, B0–B3 context ladder | [→](../works/aae-framework.md) |
| PSE-Bench | 2026 | 200 open-ended questions, 50 in each of four process-systems-engineering domains, with released ground truths and rubrics | Process systems engineering: modeling and simulation, optimization, ML for processes, design | Five-judge ensemble on a seven-element rubric with a composite ROUGE / cosine / element-coverage score; human-expert calibration (rs = 0.416, ICC = 0.793, +0.85 leniency) | [→](../works/pse-bench.md) |
| Can Large Language Models Automate the HAZOP Process? | 2026 | One expert-referenced P&ID and a standardized prompt, run once per model across four multimodal LLMs | Process safety: HAZOP hazard identification | Similarity (F1) and cost per worksheet against an expert reference, scored separately from scenario validity and safeguard diversity | [→](../works/can-large-language-models-automate-the-hazop-proce.md) |
| ChemEBench | 2025 | 101 chemical-engineering tasks over 15 dimensions in three progressive levels | Chemical engineering: foundational knowledge, molecular-level tasks, professional engineering skill | Accuracy on objective items; 0–5 rubric on completeness / clarity with step-by-step reasoning-chain checking for subjective items; 14-model comparison | [→](../works/chemebench.md) |
| ERI Benchmark | 2026 | 57,750 generated records as a controlled cross-product of 9 engineering fields, 55 subdomains, 7 intents, and 3 difficulty tiers | Engineering reasoning and instruction (chemical engineering one of nine fields) | Automatic output checks beneath a rubric layer judged by a three-provider panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3); 115,962 judgments averaged 1–5 | [→](../works/eri-benchmark.md) |
| PEOA | 2024 | MathComp (8,500+ pairs) and ChemProc (7,000+ pairs) compiled from scholarly sources and textbooks | Chemical and process engineering problem solving with mathematical modeling and numerical methods | Stage-decomposed tool-learning metrics (planning, tool selection Recall/NDCG/COMP@K, tool calling, BLEU/ROUGE-L/EM) plus an eight-aspect human study | [→](../works/peoa.md) |
| Using Large Language Models for Solving Thermodynamic Problems | 2025 | 22 author-written problems (13 simple, 9 advanced), each posed three times per model | Chemical-engineering thermodynamics | Trained human experts grading exam-style, 0.5 points per correctly executed step; answer consistency across repetitions | [→](../works/llm-thermodynamics.md) |
| LLM-Empowered Agent for Reliable and Robust Structural Analysis | 2026 | 8 author-constructed statically determinate beam problems (2 beam types × 4 load conditions) plus 3 extended generalization tasks | Structural analysis: support reactions under static equilibrium | Reliability over 500 independent runs of an identical prompt and robustness = (1 + CV)⁻¹ over a 1 m-interval load sweep; generated OpenSeesPy code executed automatically | [→](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| Lightweight Multi-Agent System for 2D Frame Structural Analysis | 2025 | 20 author-designed 2D building frames, mixing topologies abstracted from real buildings with sampled story profiles | Structural analysis: finite-element modeling of plane frames | Proportion of correctly generated OpenSeesPy programs over 10 independent trials per problem, with an error taxonomy by source (node / element / support / material) | [→](../works/a-lightweight-large-language-model-based-multi-age.md) |
| Agentic LLMs for Automated Structural Analysis of 3D Frame Systems | 2026 | 10 irregular 3D frame systems specified by gridlines and a matrix of number of stories | Structural analysis: 3D building-frame modeling in SAP2000 | All monitored structural responses within 1% relative error of a manually built ground-truth SAP2000 model, over 10 trials per problem | [→](../works/agentic-large-language-models-for-automated-struct.md) |
| Integrating LLMs for Automated Structural Analysis | 2025 | 20 hand-designed structural analysis word problems on 2D frames with ground-truth schematics | Structural analysis: deformations and internal forces in 2D frames | Best-of-three correctness across four base models plus a five-run generative-stability study; OpenSeesPy execution and an expert-authored instruction ablation | [→](../works/integrating-large-language-models-for-automated-st.md) |
| MASSE | 2025 | 100 problems reorganized from real racking-system project records in British Columbia, with expert-validated ground truth | Structural engineering workflow: analysis, design, load transformation, end-to-end execution | GPT-5 judge reading a complete analysis log against expert ground truth under four explicit point rubrics (SAAB / SDAB / LAB / MASEB), with token usage and time reported | [→](../works/masse.md) |
| AutoBM / BMEval | 2026 | 128 expert-validated building samples generated across a building-attribute space, with empirical-formula reference periods | Automatic building modeling: OpenSeesPy code from a structural specification | Sandbox-execution pass@k, plus first-order period within 0.30 relative error and an explicit design-code compliance conclusion; Pass@k_strict conjoins all three | [→](../works/autobm.md) |
| PE Civil Bench | 2026 | 150 FE- and PE-style licensure problems curated by professional engineers, plus 33 ETABS-referenced beam design cases | Civil engineering across eight subdisciplines; reinforced-concrete component design | Answer correctness under base prompting / vector RAG / agentic RAG; design track correlated against ETABS finite-element output (r ≥ 0.90) | [→](../works/pe-civil-bench.md) |
| DrafterBench | 2025 | 1,920 tasks summarized from 100+ real revision files supplied by design and construction firms | Civil-engineering technical drawing revision | Two-level automatic scoring (code executability + target completeness) with operation-chain intersection-over-union against a reference chain | [→](../works/drafterbench.md) |
| AECBench | 2026 | 4,800 Chinese questions across 23 tasks, authored by domain engineers and drawn from licensure examinations | Architecture, engineering and construction knowledge across five cognition levels | Accuracy on objective items; LLM judge against expert-predefined rubrics for open-ended items, recalibrated to expert scores (MAE 2.947 → ~1.93–2.02) | [→](../works/aecbench.md) |
| AEC-Bench | 2026 | 196 task instances over publicly available construction document sets from public-sector projects | Construction document work: detail review, cross-referencing, specification–drawing sync, submittal review | Task-specific automatic verifiers grading structured JSONL findings in Dockerized sandboxes with graded partial credit; no LLM judge | [→](../works/aec-bench.md) |
| SGR-BIM | 2026 | 679 expert-verified fire-safety compliance queries over five IFC building models | Geometry-intensive building-code compliance checking on BIM models | Human-scored three-tier accuracy that withholds full credit unless governing variables and boundary conditions are identified, plus anonymized LLM-judged coherence / relevance / explainability, human-audited | [→](../works/sgr-bim.md) |
| SoM-1K | 2025 | 1,065 problems from university textbooks and mechanics competitions, each with an expert-written description of its diagram | Strength of materials (mechanics of materials) | Manual expert grading of every response for reasoning validity and final answer, over majority votes of five samples | [→](../works/som-1k.md) |
| EngDesign | 2025 | 101 real-world engineering design tasks carrying 473 gradable items across nine areas | Engineering design, including 13 Structure Design tasks | Domain simulators (MATLAB, SPICE/Cadence, finite element analysis, topology optimisation) return a binary pass/fail plus a 0–100 partial-credit score | [→](../works/engdesign.md) |
| MMArch | 2026 | 1,212 items generated from figures in a pool of roughly 10,000 peer-reviewed architecture and civil-engineering papers | Architecture and civil engineering across ten subdomains (multimodal) | Accuracy against a frozen ≤10-token reference answer with unit / synonym / tolerance normalisation; human expert panel as upper reference | [→](../works/mmarch.md) |
| Evaluating AI Chatbots on the FE and PE Structural Exams | 2024 | 79 FE and 39 PE questions from the official NCEES practice examinations | Civil (FE) and structural (PE) licensure examination content | Binary correct/not-correct against the recommended NCEES solutions, no partial credit or curving, aggregated per topic area | [→](../works/evaluating-the-performance-of-artificial-intellige.md) |
| Civil-Eval | 2026 | 517 objective items from the May 2024 sitting of Chinese national registration examinations | Civil and transportation engineering knowledge across 8 examination subjects | Exam-faithful option scoring (exact set match for multiple-choice) with subject weights assigned by hard-question share | [→](../works/civil-eval.md) |
| DefectBench | 2026 | 487 benchmark samples harmonized from 12 building-defect datasets under one four-class ontology | Building-facade structural pathology: semantic perception, spatial localization, generative segmentation | Per-level metric families against expert-verified annotations (F1 / MAE, mAP50-95, mIoU) under a zero-shot multi-turn protocol | [→](../works/defectbench.md) |
| Cognitive Agents for Bridge Inspection Prioritization | 2026 | Six annual FHWA National Bridge Inventory releases (2020–2025) filtered to an analytic sample of 3,389 Connecticut bridges | Highway-bridge inspection prioritization | AUC / average precision / precision@300 against observed sustained deterioration under three outcome definitions, plus blind 0–3 rating of 100 rationales by a certified bridge inspector | [→](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) |
| Toward Responsible AI in High-Stakes Domains | 2025 | Four reinforced-concrete building frames, each analysed under four computational groups | Structural static analysis of reinforced-concrete building frames | Relative error against a manually built ETABS reference model on inter-storey drift, maximum displacement, base shear and period | [→](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) |
| TransportBench | 2024 | 140 problems from two long-running University of Illinois transportation-engineering courses | Transportation engineering: planning, design, management and control | Human expert grading of both answer and reasoning; repeated-trial Mixed Response Rate and answer stability under a self-checking follow-up | [→](../works/transportbench.md) |
| BridgeEQA | 2025 | 2,200 QA pairs extracted from Vermont Agency of Transportation inspection reports over 200 real bridge scenes | Bridge inspection embodied question answering | LLM-judged answer correctness, exact and within-±1 NBI condition-rating accuracy, and Image Citation Relevance (Spearman 0.817 with human annotations) | [→](../works/bridgeeqa.md) |
| LLM-EPANET | 2025 | 69 curated natural-language queries over Net1, Net3 and L-Town in five complexity categories | Water distribution system modeling (EPANET / EPyT) | Functional equivalence to a hand-written deterministic reference script executed in advance, with expert adjudication of borderline equivalence | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | 4,000 Chinese multiple-choice items from textbooks, industry standards, laws and regulations, and statistical yearbooks | Hydro-science and hydraulic engineering across nine subfields | Accuracy at temperature 0 with a separate LLM extracting the final choice, reported by subfield, question type and cognitive level | [→](../works/hydro-se-bench.md) |
| LLM-Based Multi-Agent Systems for Automated Foundation Design | 2026 | 27 author-defined foundation-design cases (15 shallow-foundation, 12 pile) across seven categories | Geotechnical engineering: shallow-footing and pile foundation design | Four-criterion rubric on a four-point scale — calculation accuracy, chain-of-thought reasoning, complex-scenario handling, output structure — with triple-trial execution per case | [→](../works/large-language-model-based-multi-agent-systems-for.md) |
| CEQuest | 2025 | 164 questions authored by domain experts from construction estimating textbooks and drawing-interpretation guides | Construction drawing interpretation and cost estimation | Exact answer match over five repeated runs reported as mean ± standard deviation, alongside evaluation time and model size | [→](../works/cequest.md) |
| Automating Structural Reliability Analysis with a Multi-Agent LLM Framework | 2026 | 20 hand-authored component-level reliability problems held out from the fine-tuning set | Structural reliability analysis: reliability index and failure probability | β and P_f produced only by deterministic execution of validated solvers and compared against Monte Carlo / subset-simulation references; method-category accuracy against a deterministic labeling rule | [→](../works/automating-structural-reliability-analysis-with-a.md) |
| TRIP-Evaluate | 2026 | 837 single-choice items (596 text, 198 image, 43 point-cloud) under a role–task–knowledge taxonomy | Transportation engineering, including a planning-and-design role | Single-letter accuracy under a fixed prompt and decoding settings, reported by role, task domain, capability, difficulty and modality | [→](../works/trip-evaluate.md) |

## Open Questions

- **Reference standards for correctness.** Scientific tasks admit multiple defensible reference standards — published SOTA (NatureBench), expert taxonomy (MedHELM), executable verification (Terminal-Bench Science), comparison against traditional methods (SimulCost). Should any one be canonical for cross-benchmark comparison?
- **Discovery vs. reproduction.** NatureBench distinguishes "matching SOTA" from "genuine methodological innovation." How should benchmarks operationalize discovery in a scoring metric?
- **Cost as an evaluation dimension.** Scientific workflows have real tool-use costs (simulation time, experimental resources). Should the scientific-agent topic converge on cost as a mandatory dimension, as SimulCost does?
- **Domain breadth vs. depth.** Cross-discipline benchmarks (NatureBench, AIRS-Bench, MedHELM) give breadth; single-simulator or single-domain benchmarks give depth. Which serves the field better as the primary evaluation surface?
- **Judge reliability.** MedHELM reports LLM-jury / clinician agreement of ICC = 0.47. Is this a floor that other scientific-domain benchmarks using LLM-judge scoring should be expected to report, and what value counts as adequate?

## Related Works

- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [MASSE](../works/masse.md)
- [AutoBM / BMEval](../works/autobm.md)
- [PE Civil Bench](../works/pe-civil-bench.md)
- [DrafterBench](../works/drafterbench.md)
- [AECBench](../works/aecbench.md)
- [AEC-Bench](../works/aec-bench.md)
- [SGR-BIM](../works/sgr-bim.md)
- [SoM-1K](../works/som-1k.md)
- [EngDesign](../works/engdesign.md)
- [MMArch](../works/mmarch.md)
- [Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md)
- [Civil-Eval](../works/civil-eval.md)
- [DefectBench](../works/defectbench.md)
- [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md)
- [Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)
- [TransportBench](../works/transportbench.md)
- [BridgeEQA](../works/bridgeeqa.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [Large Language Model-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md)
- [CEQuest](../works/cequest.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [TRIP-Evaluate](../works/trip-evaluate.md)
- [CeProBench](../works/ceprobench.md)
- [Simona](../works/simona.md)
- [CRAFTS](../works/crafts.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [PSE-Bench](../works/pse-bench.md)
- [Can Large Language Models Automate the HAZOP Process Without Human Intervention?](../works/can-large-language-models-automate-the-hazop-proce.md)
- [ChemEBench](../works/chemebench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [PEOA](../works/peoa.md)
- [Using Large Language Models for Solving Thermodynamic Problems](../works/llm-thermodynamics.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [TCS-Bench](../works/tcs-bench.md)
- [MiraMind](../works/miramind.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [DSAgentBench](../works/dsagentbench.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [EnergyBridge](../works/energybridge.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
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
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CMPhysBench](../works/cmphysbench.md)
- [MDArena](../works/mdarena.md)
- [MetaSyn](../works/metasyn.md)
- [PhySciBench](../works/physcibench.md)
- [ScholarQuest](../works/scholarquest.md)
- [SciExplore](../works/sciexplore.md)
- [RealPDEBench](../works/realpdebench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [PhysGym](../works/physgym.md)
- [DiscoverPhysics](../works/discoverphysics.md)
- [FEABench](../works/feabench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [ReplicationBench](../works/replicationbench.md)
- [PRL-Bench](../works/prl-bench.md)
- [EnvTrace](../works/envtrace.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [CritPt](../works/critpt.md)
- [TPBench](../works/tpbench.md)
- [SciCode](../works/scicode.md)
- [Lean4Physics](../works/lean4physics.md)
- [LLM-SRBench](../works/llm-srbench.md)
- [UGPhysics](../works/ugphysics.md)
- [PHYBench](../works/phybench.md)
- [SeePhys](../works/seephys.md)
- [HiPhO](../works/hipho.md)
- [Humanity's Last Exam](../works/hle.md)
- [PHYSICS](../works/physics-benchmark.md)
- [PaperBench](../works/paperbench.md)
- [CORE-Bench](../works/core-bench.md)
- [GenoTEX](../works/genotex.md)
- [BixBench](../works/bixbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SpatialBench](../works/spatialbench.md)
- [BAISBench](../works/baisbench.md)
- [BioXArena](../works/bioxarena.md)
- [BioProBench](../works/bioprobench.md)
- [SciGym](../works/scigym.md)
- [LAB-Bench](../works/lab-bench.md)
- [LABBench2](../works/labbench2.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [BioKGBench](../works/biokgbench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AgentClinic](../works/agentclinic.md)
- [MedAgentBench](../works/medagentbench.md)
- [SDBench](../works/sdbench.md)
- [BrainBench](../works/brainbench.md)
- [CodePDE](../works/codepde.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [MooseBench](../works/moosebench.md)
- [SimBench](../works/simbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [StructureClaw](../works/structureclaw.md)
- [FEM-Bench](../works/fem-bench.md)
- [SciConvBench](../works/sciconvbench.md)
- [PDE-Controller](../works/pde-controller.md)
- [HARDMath](../works/hardmath.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [HydroAgent](../works/hydroagent.md)
- [ChemBench](../works/chembench.md)
- [ChemEval](../works/chemeval.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [MolecularIQ](../works/moleculariq.md)
- [ChemIQ](../works/chemiq.md)
- [FGBench](../works/fgbench.md)
- [QCBench](../works/qcbench.md)
- [MolPuzzle](../works/molpuzzle.md)
- [MolQuest](../works/molquest.md)
- [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md)
- [MolLangBench](../works/mollangbench.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [ChemX](../works/chemx.md)
- [ChemCost](../works/chemcost.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [MaCBench](../works/macbench.md)
- [LabRobFail](../works/labrobfail.md)
- [MaScQA](../works/mascqa.md)
- [MatSciBench](../works/matscibench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatText](../works/mattext.md)
- [AtomWorld](../works/atomworld.md)
- [OpenXRD](../works/openxrd.md)
- [MatVQA](../works/matvqa.md)
- [MatCha](../works/matcha.md)
- [MatQnA](../works/matqna.md)
- [MatViX](../works/matvix.md)
- [MatTools](../works/mattools.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [AlchemyBench](../works/alchemybench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [VerilogEval](../works/verilogeval.md)
- [RTLLM](../works/rtllm.md)
- [RTL-Repo](../works/rtl-repo.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [CVDP](../works/cvdp.md)
- [AssertionBench](../works/assertionbench.md)
- [FVEval](../works/fveval.md)
- [HLS-Eval](../works/hls-eval.md)
- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [EEE-Bench](../works/eee-bench.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [TeleQnA](../works/teleqna.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [ElecBench](../works/elecbench.md)
- [BrainBench (EEG)](../works/brainbench-eeg.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [CPsyExam](../works/cpsyexam.md)
- [ConceptPsy](../works/conceptpsy.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
- [MLE-bench](../works/mle-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLAgentBench](../works/mlagentbench.md)
- [ML-Bench](../works/ml-bench.md)
- [DSBench](../works/dsbench.md)
- [DA-Code](../works/da-code.md)
- [BLADE](../works/blade.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [SUPER](../works/super.md)
- [MLR-Bench](../works/mlr-bench.md)
- [RE-Bench](../works/re-bench.md)
- [MLGym](../works/mlgym.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [IdeaBench](../works/ideabench.md)
- [LiveIdeaBench](../works/liveideabench.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
