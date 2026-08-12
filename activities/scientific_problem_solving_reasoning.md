# Scientific Problem Solving & Reasoning

> **English** | [简体中文](../zh/activities/scientific_problem_solving_reasoning.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on producing an answer, derivation, proof, or solution to a scientific, mathematical, or theoretical problem, where the central deliverable is the solution itself rather than a software artifact, experiment, or research workflow.

## Scope

Includes scientific QA, quantitative and theoretical reasoning, symbolic manipulation, formal and mathematical proof, research-level calculation, multimodal problem solving, and diagnostic reasoning whose deliverable is a diagnosis. It is distinguished from tasks whose core is building software (→ Scientific Software & Workflow Engineering), running simulations (→ Simulation & Scientific Computing), or verifying other agents' reasoning steps (evaluation methodology, not an activity).

## Task Patterns

The largest cluster is **domain-knowledge QA**, where the deliverable is a correct answer to curated exam or textbook questions. Psychology dominates one strand — [ConceptPsy](../works/conceptpsy.md) annotates concepts to chapters, [CPsyExam](../works/cpsyexam.md) splits knowledge from case analysis, and [PsychCounsel-Bench](../works/psychcounsel-bench.md) anchors to a real certification pass threshold. Engineering-knowledge QA appears in [MaScQA](../works/mascqa.md) (materials), [TeleQnA](../works/teleqna.md) (telecom), and [ElecBench](../works/elecbench.md) (power dispatch), while [HLE](../works/hle.md) sets a deliberately broad frontier-of-knowledge ceiling. Civil and structural engineering contributes a licensure-and-standards strand of its own, running from the early [FE and PE structural exam study](../works/evaluating-the-performance-of-artificial-intellige.md) through the released licensure corpus of [PE Civil Bench](../works/pe-civil-bench.md) and the registration-examination items of [Civil-Eval](../works/civil-eval.md), and broadening into the cognition-level ladder of [AECBench](../works/aecbench.md), the standards-heavy subfields of [Hydro-SE Bench](../works/hydro-se-bench.md), the course-derived problems of [TransportBench](../works/transportbench.md), the estimating judgement probed by [CEQuest](../works/cequest.md), and the role-organised items of [TRIP-Evaluate](../works/trip-evaluate.md). Chemical and process engineering forms its own strand, running from the thermodynamics calculations of [Using LLMs for Solving Thermodynamic Problems](../works/llm-thermodynamics.md) and the tool-integrated textbook trajectories of [PEOA](../works/peoa.md) through the level-structured breadth of [ChemEBench](../works/chemebench.md) and the open-ended process-systems questions of [PSE-Bench](../works/pse-bench.md), with [ERI Benchmark](../works/eri-benchmark.md) placing chemical engineering as one field inside a nine-field engineering cross-product; the [HAZOP evaluation](../works/can-large-language-models-automate-the-hazop-proce.md) is the boundary case where the deliverable is a full professional worksheet rather than an answer, and it separates similarity to the expert reference from the semantic validity of what was written. Chemistry knowledge QA runs from [ChemBench](../works/chembench.md) and [ChemEval](../works/chemeval.md) through the quantitative-computation focus of [QCBench](../works/qcbench.md) and [ChemIQ](../works/chemiq.md).

A second cluster is **exam/olympiad and research-level quantitative physics reasoning**, where symbolic derivations are the deliverable and continuous or partial-credit metrics matter. [PHYBench](../works/phybench.md) and [HiPhO](../works/hipho.md) grade olympiad-style problems; [UGPhysics](../works/ugphysics.md) and [PHYSICS](../works/physics-benchmark.md) cover undergraduate breadth; and difficulty escalates through [CMPhysBench](../works/cmphysbench.md), [CMT-Benchmark](../works/cmt-benchmark.md), [TPBench](../works/tpbench.md), [CritPt](../works/critpt.md), and [PRL-Bench](../works/prl-bench.md) into genuinely research-level, contamination-controlled challenges. Applied-math analogues include [HARDMath](../works/hardmath.md) (asymptotics) and [PDE-Controller](../works/pde-controller.md).

A third cluster is **multimodal / vision-essential problem solving**, where the answer depends on reading a diagram, spectrum, or micrograph. Physics diagrams drive [SeePhys](../works/seephys.md); circuits and EE imagery drive [EEE-Bench](../works/eee-bench.md) and [MMCircuitEval](../works/mmcircuiteval.md); and materials-characterization imagery underpins [MatCha](../works/matcha.md), [MatVQA](../works/matvqa.md), [MatQnA](../works/matqna.md), [MatSciBench](../works/matscibench.md), and [MaCBench](../works/macbench.md). Chemistry structure elucidation is a recurring multimodal sub-theme, from staged spectra reading in [MolPuzzle](../works/molpuzzle.md) to agentic, experiment-planning elucidation in [MolQuest](../works/molquest.md). Structural mechanics adds [SoM-1K](../works/som-1k.md), where expert-written descriptions of a schematic turn out to be a more reliable input than the schematic itself, and [MMArch](../works/mmarch.md), whose items require composing evidence spread across one published engineering figure.

A fourth cluster is **structure/graph and reaction reasoning in chemistry**, where correctness is symbolically verifiable against the molecule itself: [MolLangBench](../works/mollangbench.md), [MolecularIQ](../works/moleculariq.md), [FGBench](../works/fgbench.md), [AtomWorld](../works/atomworld.md) (crystal geometry), plus reaction- and synthesis-oriented [ChemCoTBench](../works/chemcotbench.md), [FukuyamaBench](../works/fukuyamabench.md), [ChemCensor](../works/chemcensor.md), and [ChemCost](../works/chemcost.md). A related **formal-proof / verification** strand renders reasoning kernel-checkable: [Lean4Physics](../works/lean4physics.md), [FVEval](../works/fveval.md), and [VCoT-Bench](../works/vcot-bench.md).

A further strand asks for an **engineering verdict about a built asset or a document set** rather than a textbook answer. [DefectBench](../works/defectbench.md) escalates facade-defect diagnosis from naming a defect through locating it to delineating it; [BridgeEQA](../works/bridgeeqa.md) asks for a National Bridge Inventory condition rating from multi-view inspection imagery and separately scores which images were cited in support; [SGR-BIM](../works/sgr-bim.md) chains fire-safety code clauses against IFC geometry to a compliance verdict; [AEC-Bench](../works/aec-bench.md) reviews real construction document sets for cross-reference conflicts and submittal compliance; and [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) has a blinded certified inspector rate the agent's written justification separately from its ranking accuracy.

Finally, a **clinical-diagnosis and interactive biology-research** cluster treats the deliverable as a diagnosis or discovery reached under incomplete information: sequential diagnosis in [AgentClinic](../works/agentclinic.md) and [SDBench](../works/sdbench.md), and biology-research capability in [LAB-Bench](../works/lab-bench.md), [BAISBench](../works/baisbench.md), [BioProBench](../works/bioprobench.md), [BioKGBench](../works/biokgbench.md), and [Aviary](../works/aviary.md). Cross-cutting benchmarks like [SciCode](../works/scicode.md), [CFDLLMBench](../works/cfdllmbench.md), [PhySciBench](../works/physcibench.md), [SciConvBench](../works/sciconvbench.md), [BrainBench](../works/brainbench.md), [OpenXRD](../works/openxrd.md), and [onePot-Bench](../works/onepot-bench.md) round out the activity.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| ConceptPsy | 2023 | Answer psychology questions annotated by concept/chapter | Static QA, 12 subjects, 1,383 concepts | Per-concept accuracy | [card](../works/conceptpsy.md) |
| MaScQA | 2023 | Solve materials-science/metallurgy exam questions | Static QA, 650 GATE questions, 4 types, 14 topics | Answer accuracy (GPT-4 | [card](../works/mascqa.md) |
| TeleQnA | 2023 | Answer telecom knowledge questions | Static MCQ, 10,000 questions, 5 categories | Accuracy vs telecom professionals | [card](../works/teleqna.md) |
| AgentClinic | 2024 | Reach diagnoses via sequential patient interaction | Simulated clinic, 9 specialties, 7 languages, multimodal | Diagnostic accuracy | [card](../works/agentclinic.md) |
| Aviary | 2024 | Solve multi-step molecular-biology/literature research tasks | Language-agent envs (SeqQA, LitQA2, protein stability) | Task success vs experts | [card](../works/aviary.md) |
| BioKGBench | 2024 | Verify claims and find errors in biomedical KGs | SCV+KGQA (2,000+) plus agentic KGCheck (225) | Error-detection accuracy | [card](../works/biokgbench.md) |
| BrainBench | 2024 | Predict which neuroscience abstract reports real result | Two-alternative forced choice, 200 test cases | Prediction accuracy vs experts | [card](../works/brainbench.md) |
| ChemBench | 2024 | Answer chemistry knowledge/reasoning questions | Static QA, 2,700+ pairs, tool-free | Accuracy vs human chemists | [card](../works/chembench.md) |
| ChemEval | 2024 | Solve chemical tasks across capability dimensions | 42 tasks, 4 levels, 12 dimensions, static | Task accuracy | [card](../works/chemeval.md) |
| CPsyExam | 2024 | Answer psychology knowledge and case-analysis questions | Static QA, 4,000 exam questions | Answer accuracy | [card](../works/cpsyexam.md) |
| EEE-Bench | 2024 | Solve multimodal EE problems from circuit diagrams | 2,860 problems, 10 subdomains, image+text | Solution accuracy (19-47%) | [card](../works/eee-bench.md) |
| ElecBench | 2024 | Reason about power-grid dispatch scenarios | NL reasoning/decisions, general+business scenarios | Six-metric / 24-sub-metric scores | [card](../works/elecbench.md) |
| FE/PE Structural Exam Evaluation | 2024 | Answer NCEES civil and structural licensure exam questions | 79 FE + 39 PE practice questions, one per prompt, no tools | Correct/not-correct vs NCEES solutions (ChatGPT-4 70.9% FE, 46.2% PE) | [card](../works/evaluating-the-performance-of-artificial-intellige.md) |
| FVEval | 2024 | Generate SystemVerilog assertions/testbenches | Three sub-tasks, tool-validated | Jasper formal-tool validation | [card](../works/fveval.md) |
| HARDMath | 2024 | Solve applied-math asymptotic-approximation problems | Auto-generated, HARDMath-mini 366 + 40 word problems | Match to numerical ground truth | [card](../works/hardmath.md) |
| LAB-Bench | 2024 | Solve biology-research practice tasks | 2,400+ MCQ, 8 categories, tool-optional | Accuracy vs expert biologists | [card](../works/lab-bench.md) |
| MaCBench | 2024 | Interpret chemistry/materials lab imagery | Multimodal VLM, 3 aspects, static | Task accuracy across aspects | [card](../works/macbench.md) |
| MolPuzzle | 2024 | Elucidate molecular structure from spectra | 200 instances, 3 stages, multimodal | Exact structure match (GPT-4o 1.4%) | [card](../works/molpuzzle.md) |
| PEOA | 2024 | Solve chemical/process-engineering problems as tool-integrated trajectories | MathComp (8,500+) and ChemProc (7,000+) QA pairs, 70/15/15 split | Staged planning/selection/calling scores plus BLEU/ROUGE-L/EM | [card](../works/peoa.md) |
| SciCode | 2024 | Solve research-coding science problems | 80 main / 338 subproblems, 16 subfields | Pass gold tests (Claude 4.6%) | [card](../works/scicode.md) |
| TransportBench | 2024 | Solve undergraduate transportation-engineering problems | 140 problems (73 true/false), text-only, 10 topic areas | Human-expert-graded accuracy (best 67.1%) plus answer consistency | [card](../works/transportbench.md) |
| AtomWorld | 2025 | Manipulate crystalline atomic structures | 10 actions, 4 modelling categories, verifiable | Verified structure correctness | [card](../works/atomworld.md) |
| BAISBench | 2025 | Annotate cell types and answer discovery questions | 15 single-cell datasets + 193 MCQ | Annotation + discovery accuracy vs humans | [card](../works/baisbench.md) |
| BioProBench | 2025 | Reason over biological wet-lab protocols | 523,784 instances, 5 task types, static | Accuracy/F1/tau/BLEU metrics | [card](../works/bioprobench.md) |
| BridgeEQA | 2025 | Answer bridge-inspection questions from multi-view scene imagery | 2,200 QA pairs over 200 real bridge scenes (9,586 images) | Answer correctness, NBI rating within +/-1, image-citation relevance | [card](../works/bridgeeqa.md) |
| CEQuest | 2025 | Interpret construction drawings and perform quantity takeoff | 164 items (101 multiple-choice, 63 true/false), 5 subject areas | Exact-match accuracy (GPT-4.1 75.37%) | [card](../works/cequest.md) |
| CFDLLMBench | 2025 | Answer CFD knowledge, code solvers, run OpenFOAM | Three tiers, 240 tasks | Executability, numerical error, convergence | [card](../works/cfdllmbench.md) |
| ChemCoTBench | 2025 | Solve molecular tasks as modular operation chains | 1,495 samples, 22 tasks, static | Stepwise reasoning correctness | [card](../works/chemcotbench.md) |
| ChemEBench | 2025 | Answer chemical-engineering knowledge and professional-skill questions | 3 progressive levels, 15 dimensions, 101 tasks, static | Objective accuracy plus 0-5 rubric on the reasoning chain | [card](../works/chemebench.md) |
| ChemIQ | 2025 | Answer organic-chemistry constructed questions | 816 short-answer, 8 categories, tool-free | Programmatically verified accuracy | [card](../works/chemiq.md) |
| CMPhysBench | 2025 | Solve graduate condensed-matter calculation problems | 520+ problems, full-solution generation | SEED partial-credit score | [card](../works/cmphysbench.md) |
| CMT-Benchmark | 2025 | Solve expert-level condensed-matter-theory problems | 50 problems, symbolic operator handling | Programmatic grading vs ground truth | [card](../works/cmt-benchmark.md) |
| CritPt | 2025 | Solve research-level physics challenges | 71 challenges / 190 checkpoints, 11+ subfields | Machine-verified accuracy ( | [card](../works/critpt.md) |
| FGBench | 2025 | Reason about functional-group property effects | 625K problems (7K benchmark), 245 groups | Regression/classification accuracy | [card](../works/fgbench.md) |
| HiPhO | 2025 | Solve physics-olympiad exam problems | 13 recent olympiad exams, text+diagram | Official rubric grading, medal thresholds | [card](../works/hipho.md) |
| Humanity's Last Exam | 2025 | Answer frontier academic questions | 2,500 expert MCQ/short-answer, many subjects | Answer accuracy + calibration | [card](../works/hle.md) |
| Hydro-SE Bench | 2025 | Answer hydro-science and hydraulic-engineering questions | 4,000 Chinese items, 9 subfields, 3 cognitive levels | Accuracy (commercial 0.74-0.80, open-weight 0.41-0.68) | [card](../works/hydro-se-bench.md) |
| Lean4Physics / LeanPhysBench | 2025 | Produce formal Lean4 physics proofs | 200 hand-crafted statements, PhysLib support | Kernel-checked proof (best 35%) | [card](../works/lean4physics.md) |
| MatCha | 2025 | Answer materials-characterization imagery questions | 1,500 questions, 4 stages, 21 tasks | Accuracy vs human experts | [card](../works/matcha.md) |
| MatQnA | 2025 | Interpret ten materials-characterization methods | MCQ+subjective, multimodal | Accuracy (frontier | [card](../works/matqna.md) |
| MatSciBench | 2025 | Solve college-level materials-science problems | 1,340 problems (315 image), text+multimodal | Reasoning accuracy | [card](../works/matscibench.md) |
| MatVQA | 2025 | Reason over microscopy/diffraction imagery | 1,325 questions, 4 structure-property tasks | Shortcut-resistant accuracy | [card](../works/matvqa.md) |
| MiraMind | 2025 | Mental-health / clinical reasoning across six task families | 13 datasets; appraisal, diagnosis, intervention, QA, abstraction, verification | Per-family outcome metrics plus reasoning-trajectory reliability | [card](../works/miramind.md) |
| MMCircuitEval | 2025 | Answer circuit/EDA questions across design flow | 3,614 multimodal QA, digital+analog | Accuracy by design stage | [card](../works/mmcircuiteval.md) |
| MolLangBench | 2025 | Recognize, edit, generate molecular structures | 3 families over strings/images/graphs | Auto/expert-checked accuracy | [card](../works/mollangbench.md) |
| OpenXRD | 2025 | Answer XRD/crystallography questions | 217 questions, closed/open-book, 74 models | QA accuracy | [card](../works/openxrd.md) |
| PDE-Controller | 2025 | Autoformalize and reason for PDE control | Human cases + 2M synthetic, heat/wave systems | Utility gain over baselines | [card](../works/pde-controller.md) |
| PHYBench | 2025 | Solve original physics problems | 500 problems, HS-to-olympiad, symbolic | EED score / accuracy | [card](../works/phybench.md) |
| PHYSICS | 2025 | Solve university-level physics problems | 1,297 problems, six core areas | Automated answer validation | [card](../works/physics-benchmark.md) |
| PsychCounsel-Bench | 2025 | Answer counseling-certification questions |  | 2,252 NCE single-choice, static | [card](../works/psychcounsel-bench.md) |
| QCBench | 2025 | Solve quantitative chemistry computations | 350 problems, 7 subfields, 3 tiers, tool-free | Step-by-step numerical accuracy | [card](../works/qcbench.md) |
| SDBench | 2025 | Diagnose via budgeted sequential information-gathering | 304 NEJM-CPC cases, gatekeeper queries | Accuracy-vs-cost frontier | [card](../works/sdbench.md) |
| SeePhys | 2025 | Solve vision-essential physics problems | 2,000 questions, 7 domains, 21 diagram types | Accuracy (best sub-60%) | [card](../works/seephys.md) |
| SoM-1K | 2025 | Solve strength-of-materials problems from statement plus schematic | 1,065 annotated problems, 3 prompting strategies, 8 models | Expert-graded reasoning and answer accuracy (best 56.6%) | [card](../works/som-1k.md) |
| TPBench | 2025 | Solve novel theoretical-physics problems | 57 problems, HEP/cosmology, auto-verifiable | Verified answer accuracy | [card](../works/tpbench.md) |
| UGPhysics | 2025 | Solve undergraduate physics problems | 5,520 bilingual, 13 subjects, 7 answer types | MARJ-judged accuracy (best 49.8%) | [card](../works/ugphysics.md) |
| Using LLMs for Solving Thermodynamic Problems | 2025 | Compute numerical answers to chemical-engineering thermodynamics problems | 22 problems (13 simple / 9 advanced), 3 repetitions per model | Expert partial-credit score (advanced best 55.19%) | [card](../works/llm-thermodynamics.md) |
| AEC-Bench | 2026 | Review real construction document sets and report engineering findings | 196 instances, 9 families, 3 scope levels; Docker sandbox with CLI PDF tools | Verifier-graded findings with partial credit (submittal review tops 23.1) | [card](../works/aec-bench.md) |
| AECBench | 2026 | Answer AEC knowledge questions across five cognition levels | 4,800 Chinese questions, 23 tasks, multiple choice to 2,000-word documents | Accuracy plus calibrated LLM-judge rubric scores | [card](../works/aecbench.md) |
| Automating Structural Reliability Analysis | 2026 | Formulate a reliability problem, plan the method, interpret beta and P_f | 20 held-out component-level problems, five-agent pipeline | Reliability index within 0.1 of reference; method-category accuracy 60% | [card](../works/automating-structural-reliability-analysis-with-a.md) |
| ChemCensor / CREED | 2026 | Propose plausible retrosynthesis precursors | Single-step retrosynthesis, plausibility-scored | Chemical-plausibility metric | [card](../works/chemcensor.md) |
| ChemCost | 2026 | Price reactions via grounding and quote retrieval | 1,427 tasks, frozen snapshot, tool-using | Accuracy within 25% error (50.6%) | [card](../works/chemcost.md) |
| Civil-Eval | 2026 | Answer Chinese civil and transportation registration-examination questions | 517 items (426 single-choice, 91 multiple-choice), 8 subjects | Difficulty-weighted average accuracy (CivilGPT 73.0%) | [card](../works/civil-eval.md) |
| Cognitive Agents for Bridge Inspection Prioritization | 2026 | Justify a per-bridge inspection priority against inspection standards | 3,365 Connecticut bridge records, one agent call per bridge | Blind certified-inspector rubric on rationales (mean 2.77/3) | [card](../works/cognitive-agents-for-bridge-inspection-prioritizat.md) |
| DefectBench | 2026 | Diagnose building-facade structural defects from imagery | 487 samples, 5 questions each over 3 cognitive levels, multi-turn | Per-level identification, localization and segmentation metrics | [card](../works/defectbench.md) |
| ERI Benchmark | 2026 | Answer open-ended engineering instructions across nine fields | 57,750 records, 55 subdomains, 7 intents, 3 difficulty tiers | Three-provider judge-panel mean 1-5 score (GPT-5 4.48) | [card](../works/eri-benchmark.md) |
| FukuyamaBench | 2026 | Deduce elementary reaction-mechanism pathways | Stepwise mechanism tasks from textbook | Exact pathway match (8.3%) | [card](../works/fukuyamabench.md) |
| HAZOP Automation Evaluation | 2026 | Produce a complete HAZOP worksheet from a P&ID | One P&ID, standardized prompt, four multimodal LLMs | Similarity to expert reference (F1 >86%) vs valid-scenario share (0.19-0.37) | [card](../works/can-large-language-models-automate-the-hazop-proce.md) |
| LABBench2 | 2026 | Solve realistic biology-research tasks |  | 1,900 tasks, PDFs/images/bioinformatics files | [card](../works/labbench2.md) |
| LLM-Empowered Agent for Structural Analysis | 2026 | Compute beam support reactions under varied load configurations | 8 statically determinate beam problems, 500 runs per configuration | Reliability over repeated runs and robustness over a load-position sweep | [card](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| MMArch | 2026 | Compose distributed visual evidence in architecture/civil figures | 1,212 short-answer items from peer-reviewed paper figures | Normalised exact-match accuracy (best ~52% vs 94.57% expert panel) | [card](../works/mmarch.md) |
| MolecularIQ | 2026 | Reason over molecular graphs symbolically | Symbolically verifiable tasks, static | Verified correctness / fingerprints | [card](../works/moleculariq.md) |
| MolQuest | 2026 | Elucidate structures via multi-turn experiment planning | Interactive spectral-acquisition episodes | Structure accuracy ( | [card](../works/molquest.md) |
| Multi-Agent Systems for Automated Foundation Design | 2026 | Perform shallow-footing and pile foundation design calculations | 27 test cases, 7 categories, 3 trials each, 9 configurations | Four-criterion rubric grade (router with Grok 3: 95.00% / 90.63%) | [card](../works/large-language-model-based-multi-agent-systems-for.md) |
| onepot-Bench 0 | 2026 | Cheminformatics, refusal, reaction-outcome prediction | Three parts incl. private lab data, static | Accuracy / refusal behavior | [card](../works/onepot-bench.md) |
| PE Civil Bench | 2026 | Solve FE- and PE-style civil engineering licensure problems | 150 items (110 multiple-choice, 40 open numerical), 8 subdisciplines | Answer correctness under base, vector-RAG and agentic-RAG prompting | [card](../works/pe-civil-bench.md) |
| PhySciBench | 2026 | Answer physical-science deep-research questions | 200 curated, physics+chemistry, 6 categories | Answer correctness | [card](../works/physcibench.md) |
| PRL-Bench | 2026 | Solve frontier physics-research tasks | 100 tasks from recent PRL papers, 5 subfields | Verifiable score (best <50/100) | [card](../works/prl-bench.md) |
| PSE-Bench | 2026 | Answer open-ended process-systems-engineering questions | 200 questions, 4 PSE domains, single-turn zero-shot | Five-judge rubric composite; element coverage 60.8-78.1% | [card](../works/pse-bench.md) |
| SciConvBench | 2026 | Clarify ill-posed computational-science requests | Multi-turn dialogues, 4 domains | Disambiguation/consistency resolution (52.7%) | [card](../works/sciconvbench.md) |
| Science Edge Evaluation (SEE) | 2026 | Evidence-bounded reasoning over experimental data | 1,116 multimodal MCQ/numeric questions; chemistry, biology, materials | Expert-ground-truth accuracy (best 48.7%, 52.7% with tools) | [card](../works/science-edge-evaluation.md) |
| SGR-BIM | 2026 | Answer geometry-intensive building-code compliance queries over IFC models | 679 expert-verified queries, 5 IFC models, 4 question categories | Three-tier accuracy plus coherence/relevance/explainability (84.3 overall) | [card](../works/sgr-bim.md) |
| TCS-Bench | 2026 | Generate research-level theoretical-CS proofs | 300 theorem-proving tasks from FOCS/STOC/SODA (2020–2026) | Self-contained proof; verifier-agent accuracy (best 68%) | [card](../works/tcs-bench.md) |
| TRIP-Evaluate | 2026 | Answer transportation items across text, images and point clouds | 837 single-choice items, 4 roles, 16 task domains, 226 knowledge points | Accuracy by role, capability, difficulty and modality (best 88.8%) | [card](../works/trip-evaluate.md) |
| VCoT-Bench | 2026 | Complete Verus verification chain-of-thought | 1,988 tasks from 150 Verus programs | Proof-block completion accuracy | [card](../works/vcot-bench.md) |

## Related Works

- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [TCS-Bench](../works/tcs-bench.md)
- [MiraMind](../works/miramind.md)
- [ConceptPsy](../works/conceptpsy.md)
- [MaScQA](../works/mascqa.md)
- [TeleQnA](../works/teleqna.md)
- [AgentClinic](../works/agentclinic.md)
- [Aviary](../works/aviary.md)
- [BioKGBench](../works/biokgbench.md)
- [BrainBench](../works/brainbench.md)
- [ChemBench](../works/chembench.md)
- [ChemEval](../works/chemeval.md)
- [CPsyExam](../works/cpsyexam.md)
- [EEE-Bench](../works/eee-bench.md)
- [ElecBench](../works/elecbench.md)
- [FVEval](../works/fveval.md)
- [HARDMath](../works/hardmath.md)
- [LAB-Bench](../works/lab-bench.md)
- [MaCBench](../works/macbench.md)
- [MolPuzzle](../works/molpuzzle.md)
- [SciCode](../works/scicode.md)
- [AtomWorld](../works/atomworld.md)
- [BAISBench](../works/baisbench.md)
- [BioProBench](../works/bioprobench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [ChemIQ](../works/chemiq.md)
- [CMPhysBench](../works/cmphysbench.md)
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CritPt](../works/critpt.md)
- [FGBench](../works/fgbench.md)
- [HiPhO](../works/hipho.md)
- [Humanity's Last Exam](../works/hle.md)
- [Lean4Physics / LeanPhysBench](../works/lean4physics.md)
- [MatCha](../works/matcha.md)
- [MatQnA](../works/matqna.md)
- [MatSciBench](../works/matscibench.md)
- [MatVQA](../works/matvqa.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [MolLangBench](../works/mollangbench.md)
- [OpenXRD](../works/openxrd.md)
- [PDE-Controller](../works/pde-controller.md)
- [PHYBench](../works/phybench.md)
- [PHYSICS](../works/physics-benchmark.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
- [QCBench](../works/qcbench.md)
- [SDBench](../works/sdbench.md)
- [SeePhys](../works/seephys.md)
- [TPBench](../works/tpbench.md)
- [UGPhysics](../works/ugphysics.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [ChemCost](../works/chemcost.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [LABBench2](../works/labbench2.md)
- [MolecularIQ](../works/moleculariq.md)
- [MolQuest](../works/molquest.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [PhySciBench](../works/physcibench.md)
- [PRL-Bench](../works/prl-bench.md)
- [SciConvBench](../works/sciconvbench.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [PEOA](../works/peoa.md)
- [ChemEBench](../works/chemebench.md)
- [Using Large Language Models for Solving Thermodynamic Problems](../works/llm-thermodynamics.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Can Large Language Models Automate the HAZOP Process Without Human Intervention?](../works/can-large-language-models-automate-the-hazop-proce.md)
- [PSE-Bench](../works/pse-bench.md)
- [Evaluating the Performance of Artificial Intelligence Chatbots and Large Language Models in the FE and PE Structural Exams](../works/evaluating-the-performance-of-artificial-intellige.md)
- [TransportBench](../works/transportbench.md)
- [BridgeEQA](../works/bridgeeqa.md)
- [CEQuest](../works/cequest.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [SoM-1K](../works/som-1k.md)
- [AEC-Bench](../works/aec-bench.md)
- [AECBench](../works/aecbench.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [Civil-Eval](../works/civil-eval.md)
- [Cognitive Agents for Bridge Inspection Prioritization](../works/cognitive-agents-for-bridge-inspection-prioritizat.md)
- [DefectBench](../works/defectbench.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [MMArch](../works/mmarch.md)
- [Large Language Model-Based Multi-Agent Systems for Automated Foundation Design](../works/large-language-model-based-multi-agent-systems-for.md)
- [PE Civil Bench](../works/pe-civil-bench.md)
- [SGR-BIM](../works/sgr-bim.md)
- [TRIP-Evaluate](../works/trip-evaluate.md)
