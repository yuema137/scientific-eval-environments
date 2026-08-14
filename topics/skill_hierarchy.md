# Skill Hierarchy

> **English** | [简体中文](../zh/topics/skill_hierarchy.md) · [← All topics](./README.md)

## Definition

Skill hierarchy refers to the decomposition of a complex agent capability into a structured set of narrower capabilities or subskills, together with evaluation protocols that score each subskill separately. Benchmarks in this space share the design commitment that a single aggregate score conflates too much: to understand what an agent can and cannot do, evaluation must probe multiple levels of the capability tree.

## Motivation

Aggregate leaderboards obscure the shape of an agent's competence. Two agents with the same overall score may fail on entirely different subskills, and a single-metric ranking does not tell a downstream user which agent to trust for which sub-task. Skill-hierarchy benchmarks address this by producing a per-capability profile.

Skill hierarchy is closely related to but distinct from [Credit Assignment](./credit_assignment.md). Skill hierarchy asks *which subskill an agent has*; credit assignment asks *which step of a trajectory drove a success or failure*. They can be pursued together — score each subskill along the trajectory — but they answer different questions.

## Existing Approaches

- **Task-subgoal decomposition.** [AgentBoard](../works/agentboard.md) annotates every task with a chain of subgoals and reports a progress rate — effectively a per-subgoal capability signal.
- **Capability-subprocess decomposition (tool use).** [T-Eval](../works/t-eval.md) decomposes tool use into six subprocesses (instruction following, planning, reasoning, retrieval, understanding, review) and evaluates each on isolated tasks.
- **Capability-subprocess decomposition (environment configuration).** [Enconda-bench](../works/enconda-bench.md) decomposes software environment configuration into planning / error diagnosis / repair / execution.
- **Capability axes as an organizing principle.** [UniClawBench](../works/uniclawbench.md) structures its 400-task benchmark around five capability axes (Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination) and uses these axes as the primary reporting dimension.
- **Cross-benchmark control-decision taxonomy.** [AgentAtlas](../works/agentatlas.md) does not decompose per-task or per-capability but instead classifies the *control decisions* an agent makes into a six-way taxonomy applied across 15 benchmarks — providing a skill-hierarchy signal that transfers across the tasks it audits.
- **Competence-depth tiers within one domain.** [CFDLLMBench](../works/cfdllmbench.md) decomposes CFD competence by *depth* rather than by subprocess: knowledge (CFDQuery), numerical and physical reasoning (CFDCodeBench), and practical workflow implementation (FoamBench), each a separate task set. Because the tiers are nested in difficulty rather than parallel, the profile they produce reads as a ceiling — strong knowledge scores coexist with near-zero end-to-end simulation success.
- **Tool-evolution framework (out-of-scope placement).** [GATE](../works/gate.md) is included here for completeness but its actual subject is graph-based tool making for LLMs, not skill decomposition. See the card for a full explanation.
- **Facet-decomposed skill use.** [Skill-Use](../works/skill-use.md) splits using a skill into three separable facets — triggering the relevant skill, complying with its prescribed procedure, and respecting its boundaries — over 79 real skills and 177 sandboxed executable tasks. Triggering and compliance emerge as independent bottlenecks, and the strongest configuration reaches an SU score of only 0.613.
- **Valuing a skill's internal structure.** [SkillSV](../works/skillsv.md) compiles a skill into units, dependencies, and hierarchy and assigns each unit a structure-aware Shapley value, making skill libraries auditable — which units earn their context cost — and guiding pruning and compression without losing aggregate skill lift.
- **The judge's skill knowledge as the measured object.** [SkillTV-Bench](../works/skilltv-bench.md) evaluates trajectory judges on skill-augmented executions, where verifying correctly requires knowing the skill, and shows the missing verification knowledge can itself be externalized as a reusable JudgeSkill worth +14.8 accuracy points.
- **Organization treated as a variable independent of content.** [SkillJuror](../works/skilljuror.md) holds a skill's task knowledge fixed and varies only its layout — a concise root file pointing to supporting resources on demand, against a normalized flat baseline — over 410 matched trials. The effect shows up in the trajectory before it shows up in the score: distinct resources touched rise from 1.18 to 3.85 and uptake events from 1.33 to 3.92, for 17 extra verifier-passing trials. The decomposition here is of the *artifact*, not of the capability, and it establishes that the two are separable.
- **Adequacy and dependency inside the skill text.** Two works take the units of decomposition from the skill's own instructions rather than from a designer's taxonomy. [Skill Coverage](../works/skill-coverage.md) compiles instructions into conditionally scoped behavior constraints and asks, per constraint, whether a trajectory covered it and whether the behavior passed — importing test adequacy from software testing, and finding that leaderboard trajectories exercise only 38.66 to 45.51% of a skill's constraints. [SLBench](../works/slbench.md) extracts the *relations between* instructions instead — preconditions, constraints, fallbacks and five further types, present in 70% of over 5,000 public skills — and compiles the locally testable ones into 86 executable cases, where unsafe rates reach 70%.
- **Atoms measured apart from their composition.** [ATOM-Bench](../works/atom-bench.md) factorizes real-robot manipulation into motor atoms and instruction atoms, fine-tunes only on the atoms, and holds the compositional tasks out — then subtracts the failure that weak atoms already predict, so its Compositional Failure Share isolates composition as its own failure source. [TS-Skill](../works/ts-skill.md) obtains the same separation by construction rather than by attribution: its three signal-level skills are specified at question-generation time and all seven non-empty combinations are covered, so single-skill and compositional demands are distinguishable in the profile itself.
- **The cost of switching, rather than the possession of a skill.** [Skill²-Bench](../works/skill2-bench.md) measures a quantity the per-subskill profile does not contain: skill entropy, a directed pairwise measure of how hard it is to move from one reasoning skill to another, derived once against a fixed reference model so the difficulty scale does not move as new models are evaluated. Querying every model twice — each step in isolation, then the full chain — separates switching cost from per-skill competence.
- **The skill layer as an attack surface, decomposed.** Where the works above decompose competence, a security line decomposes exposure. [SkillSec-Eval](../works/skillsec-eval.md) splits the skill lifecycle into five stages with independent trust boundaries — repository admission, semantic retrieval, planner selection, runtime execution, and evolution — and reports attack and defense separately at each, establishing that failures begin well before execution. [SCR-Bench](../works/scr-bench.md) decomposes by composition mechanism instead, giving capability flow, trust transfer and authorization confusion their own sub-benchmarks with matched isolated controls, so the reported risk is attributable to composition rather than to the skills. [HarmfulSkillBench](../works/harmfulskillbench.md) locates harm in a skill's intended functionality and separates the effect of installation from the effect of stated intent across four conditions.
- **The artifact, rather than the capability, as the object.** A cluster of works scores the skill itself instead of decomposing what an agent can do. On the construction side, [SkillLearnBench](../works/skilllearnbench.md) grades automatically generated skills on functional coverage, executability and safety alongside trajectory and outcome, and [SkillEvolBench](../works/skillevolbench.md) freezes the induced library at deployment, finding that the raw traces frequently beat the skills distilled from them. On the adoption side, [SkillAudit](../works/skillaudit.md) and [A Framework for Evaluating Agentic Skills at Scale](../works/a-framework-for-evaluating-agentic-skills-at-scale.md) abandon the fixed suite altogether and generate tasks and rubrics from an authored skill package, so coverage follows that skill's declared scope; both measure a with-skill versus no-skill delta on matched runs. Several of these cards note in their own repository notes that this is not the decomposition pattern the topic was defined around; they are filed here as the nearest existing home, alongside [GATE](../works/gate.md), whose placement note records the same mismatch.

## Comparison

| Benchmark | Year | Decomposition granularity | Axes | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | Per-task subgoal chain | Task-specific (annotated) | [→](../works/agentboard.md) |
| T-Eval | 2023 | Cross-task capability subprocesses | 6 tool-use subprocesses | [→](../works/t-eval.md) |
| Enconda-bench | 2025 | Cross-task capability subprocesses | 4 env-configuration subprocesses | [→](../works/enconda-bench.md) |
| UniClawBench | 2026 | Benchmark-level organizing axes | 5 proactive-agent capabilities | [→](../works/uniclawbench.md) |
| AgentAtlas | 2026 | Per-control-decision (cross-benchmark overlay) | 6 control-decision types | [→](../works/agentatlas.md) |
| GATE | 2026 | *Tool-evolution framework, not skill decomposition — see card* | Hierarchical tool graph | [→](../works/gate.md) |
| CFDLLMBench | 2025 | Nested competence tiers within one domain | 3 depth tiers (knowledge / numerical reasoning / workflow implementation) | [→](../works/cfdllmbench.md) |
| Skill-Use | 2026 | Per-skill facet decomposition | 3 facets: trigger / compliance / boundary | [→](../works/skill-use.md) |
| SkillSV | 2026 | Within-skill unit decomposition (units / dependencies / hierarchy) | Structure-aware Shapley value per unit | [→](../works/skillsv.md) |
| SkillTV-Bench | 2026 | Judge-side skill knowledge, externalized as a reusable JudgeSkill | Judge accuracy + rollout-selection lift | [→](../works/skilltv-bench.md) |
| PEOA | 2024 | Cross-task stage decomposition of tool learning | 4 stages: task planning / tool selection / tool calling / response generation, each with its own metric family | [→](../works/peoa.md) |
| ChemEval | 2024 | Professional-requirements capability taxonomy in one domain | 4 progressive levels × 12 dimensions over 42 tasks | [→](../works/chemeval.md) |
| MaCBench | 2024 | Three core aspects of laboratory and characterization work | Data extraction / experimental understanding / results interpretation, reported as per-aspect breakdowns | [→](../works/macbench.md) |
| ChemEBench | 2025 | Progressive competence levels within one domain | 3 levels (foundational knowledge / advanced knowledge / professional skill) covering 15 dimensions and 101 tasks | [→](../works/chemebench.md) |
| HiSciBench | 2025 | Nested competence levels across six disciplines | 5 ascending levels: factual literacy → literature parsing → literature QA → review generation → data-driven discovery, each with its own scoring protocol | [→](../works/hiscibench.md) |
| EmbodiedBench | 2025 | Benchmark-level curated capability subsets | 6 subsets spanning commonsense reasoning, complex instruction understanding, spatial awareness, visual perception and long-term planning | [→](../works/embodiedbench.md) |
| RoboFAC | 2025 | Failure understanding decomposed into QA dimensions | 8 QA dimensions, scored per dimension with failure-analysis accuracy as the headline | [→](../works/robofac.md) |
| VIKI-Bench | 2025 | Three-level hierarchy of embodied multi-agent cooperation | Agent activation / task planning / trajectory perception, each with its own metrics | [→](../works/viki-bench.md) |
| AECBench | 2026 | Nested cognition levels within one domain | 5 levels (memorization / understanding / reasoning / calculation / application) over 23 tasks | [→](../works/aecbench.md) |
| Gaia2 | 2026 | Benchmark-level capability splits | 7 splits: Execution, Search, Ambiguity, Adaptability, Time, plus Noise and Agent2Agent augmentations | [→](../works/gaia2.md) |
| LabRobFail | 2026 | Failure analysis decomposed into separately scored capabilities | 6: task understanding, failure detection, temporal localization, severity assessment, failure classification, actionable correction | [→](../works/labrobfail.md) |
| SciExplore | 2026 | Progressive task types within scientific information seeking | 4: database navigation, ambiguous literature retrieval, missing reference completion, cross-source structured synthesis | [→](../works/sciexplore.md) |
| PDAgent-Bench | 2026 | Task-level capability dimensions plus a workflow-level tier | 5 dimensions (foundational knowledge, report comprehension, root cause analysis, static timing analysis, script generation) with per-dimension pass@1, plus full-flow execution | [→](../works/pdagent-bench.md) |
| DefectBench | 2026 | Three escalating cognitive levels over one harmonized corpus | Semantic perception / spatial localization / generative geometry segmentation, each with its own metric family | [→](../works/defectbench.md) |
| SkillJuror | 2026 | Skill-artifact organization, held apart from skill content | Progressive Disclosure vs. normalized flat layout; resources touched and uptake events per trajectory | [→](../works/skilljuror.md) |
| Skill Coverage | 2026 | Per-constraint decomposition of a skill's own instructions | Coverage of extracted behavior constraints × Pass/Fail on the covered ones | [→](../works/skill-coverage.md) |
| SLBench | 2026 | Per-relation decomposition of the dependencies between a skill's instructions | 8 relation types (preconditions, constraints, fallbacks, …); unsafe rate per harness and backbone | [→](../works/slbench.md) |
| SkillLearnBench | 2026 | Three-level decomposition of what a skill-learning method produces | Skill quality (functional coverage / executability / safety), trajectory quality, task outcome | [→](../works/skilllearnbench.md) |
| SkillEvolBench | 2026 | Phase decomposition: acquisition vs. frozen deployment | LSR / RSR / ESR, with ESR split into context shift, adversarial shortcuts and composition | [→](../works/skillevolbench.md) |
| SkillAudit | 2026 | Per-package audit generated from the skill artifact itself | Utility (pass-rate gain) / efficiency-cost gain / safety score | [→](../works/skillaudit.md) |
| A Framework for Evaluating Agentic Skills at Scale | 2026 | Two rubric families per generated task, scored as a with-skill vs. without-skill delta | Instruction following vs. goal completion | [→](../works/a-framework-for-evaluating-agentic-skills-at-scale.md) |
| Agent Skill Evaluation and Evolution | 2026 | *Survey — a taxonomy of the space rather than a scored decomposition* | 4 evolution paradigms × 6 categories of skill-centric benchmark | [→](../works/agent-skill-evaluation-survey.md) |
| SkillCoach | 2026 | Four-dimension process decomposition of skill-use, with rubrics induced from rollouts | Skill selection / skill following / skill composition / skill-grounded reflection | [→](../works/skillcoach.md) |
| BACKROOMBench | 2026 | Five-axis intervention on a skill, separating claimed use from measured influence | Meaning / wording / identity / content / assignment; reliance, signed utility, Attribution Fidelity Score, Backroom Gap | [→](../works/backroombench.md) |
| SkillShapley | 2026 | Per-step decomposition inside a single skill | Shapley value per skill step under a boundary-adaptive sampling budget | [→](../works/skillshapley.md) |
| Skill²-Bench | 2026 | Pairwise skill-transition decomposition over a 558-skill bank | Directed skill entropy per ordered skill pair; single-skill vs. cross-skill score gap | [→](../works/skill2-bench.md) |
| RigorBench | 2026 | Seven-pillar decomposition of engineering process discipline | Planning fidelity / verification coverage / recovery efficiency / abstention quality / atomic transition integrity / test assertion density / exploration efficiency, weighted into RigorScore | [→](../works/rigorbench.md) |
| ATOM-Bench | 2026 | Manipulation factorized into atoms, with compositions held out | 6 motor atoms × 7 instruction atoms; Atomic Score vs. Compositional Failure Share | [→](../works/atom-bench.md) |
| TS-Skill | 2026 | Signal-level skills labelled at construction time, covering all combinations | 3 skills: temporal scale selection / temporal localization / cross-interval integration, over all 7 non-empty combinations | [→](../works/ts-skill.md) |
| RubricsTree | 2026 | Top-down rubric DAG from macro capabilities to atomic Boolean leaves | 100+ clinically verifiable leaf rubrics, routed and auto-weighted per query | [→](../works/rubricstree.md) |
| HarmfulSkillBench | 2026 | Harm taxonomy over the skill layer, crossed with an installation-condition decomposition | 20 policy categories in 2 tiers; passive exposure / active invocation / safeguard ablation / no-skill baseline | [→](../works/harmfulskillbench.md) |
| SCR-Bench | 2026 | Composition mechanisms given separate sub-benchmarks, each with a matched isolated control | Capability flow / trust transfer / authorization confusion | [→](../works/scr-bench.md) |
| SkillSec-Eval | 2026 | Skill lifecycle split into stages with independent trust boundaries | 5 stages: repository admission / semantic retrieval / planner selection / runtime execution / skill evolution, attack vs. defense at each | [→](../works/skillsec-eval.md) |

## Open Questions

- **Task-specific vs. cross-task decomposition.** AgentBoard decomposes each task individually into subgoals; T-Eval / Enconda-bench decompose the capability itself into subprocesses shared across tasks; AgentAtlas decomposes across benchmarks via control-decision types. Which yields more transferable capability profiles?
- **Choice of axes.** T-Eval's six, Enconda-bench's four, UniClawBench's five, and AgentAtlas's six axes all reflect legitimate decompositions. Is there a canonical minimal set, or is the axis choice necessarily domain-dependent?
- **Composition.** The question as originally posed was how per-subskill scores should be composed into an overall capability estimate. Two results now bear on it, and both indicate that they cannot be. ATOM-Bench measures atomic and compositional competence separately on the same policies and reports Pi0.5 holding an Atomic Score of 83.3% on the atoms a task requires while succeeding on only 15.8% of held-out compositional tasks; its Compositional Failure Share exists precisely to quantify the failure that weak atoms do *not* explain. Skill²-Bench finds accuracy falling by roughly 4 to 13 points when a skill is exercised inside a cross-skill chain rather than as an isolated question, and reports that per-domain switching difficulty is largely decoupled from per-domain difficulty — science being an easy domain with the highest switching entropy. Composition therefore behaves as a capability in its own right rather than as a function of the profile, and the open question becomes how to measure it directly.
- **Decomposition vs. induction.** The page now holds two structurally different things: benchmarks that decompose a capability and score its parts, and benchmarks that score a skill an agent *produced* (SkillLearnBench, SkillEvolBench, SkillAudit, A Framework for Evaluating Agentic Skills at Scale, and GATE, whose card records the mismatch). Several of those cards carry repository notes saying as much. Do the two belong under one heading, and does the second group cohere into a line of its own?
- **Overlay vs. embedded decomposition.** Should skill-hierarchy signal be produced by the underlying benchmark (embedded, as in AgentBoard/T-Eval/Enconda-bench/UniClawBench) or applied as an overlay across benchmarks (as in AgentAtlas)?

## Related Works

- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Enconda-bench](../works/enconda-bench.md)
- [UniClawBench](../works/uniclawbench.md)
- [AgentAtlas](../works/agentatlas.md)
- [GATE](../works/gate.md) — Included for completeness; its actual subject is tool making for LLMs, not skill-hierarchy evaluation.
- [CFDLLMBench](../works/cfdllmbench.md)
- [Skill-Use](../works/skill-use.md)
- [SkillSV](../works/skillsv.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [PEOA](../works/peoa.md)
- [ChemEval](../works/chemeval.md)
- [MaCBench](../works/macbench.md)
- [ChemEBench](../works/chemebench.md)
- [HiSciBench](../works/hiscibench.md)
- [EmbodiedBench](../works/embodiedbench.md)
- [RoboFAC](../works/robofac.md)
- [VIKI-Bench](../works/viki-bench.md)
- [AECBench](../works/aecbench.md)
- [Gaia2](../works/gaia2.md)
- [LabRobFail](../works/labrobfail.md)
- [SciExplore](../works/sciexplore.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [DefectBench](../works/defectbench.md)
- [SkillJuror](../works/skilljuror.md)
- [Skill Coverage](../works/skill-coverage.md)
- [SLBench](../works/slbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillAudit](../works/skillaudit.md)
- [A Framework for Evaluating Agentic Skills at Scale](../works/a-framework-for-evaluating-agentic-skills-at-scale.md)
- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](../works/agent-skill-evaluation-survey.md)
- [SkillCoach](../works/skillcoach.md)
- [BACKROOMBench](../works/backroombench.md)
- [SkillShapley](../works/skillshapley.md)
- [Skill²-Bench](../works/skill2-bench.md)
- [RigorBench](../works/rigorbench.md)
- [ATOM-Bench](../works/atom-bench.md)
- [TS-Skill](../works/ts-skill.md)
- [RubricsTree](../works/rubricstree.md)
- [HarmfulSkillBench](../works/harmfulskillbench.md)
- [SCR-Bench](../works/scr-bench.md)
- [SkillSec-Eval](../works/skillsec-eval.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
