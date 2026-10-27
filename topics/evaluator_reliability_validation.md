# Evaluator Reliability & Validation

> **English** | [简体中文](../zh/topics/evaluator_reliability_validation.md) · [← All topics](./README.md)

## Start Here

An evaluator is another measurement system, not an oracle. If an LLM judge gives a trajectory 8/10, the important next question is whether that score agrees with experts, ranks better runs above worse ones, and stays stable when wording or candidate order changes.

Take 100 expert-labeled trajectories, score them with the judge, then separate false passes from false failures and test a swapped presentation order. This evaluates the evaluator before using it to rank agents or supply rewards. High agreement on this set still does not guarantee reliability after the agent changes its behavior to exploit the judge.

## Definition

An evaluator turns an agent run into a score, ranking, or reward. It may be a deterministic verifier, an expert rubric, a reward model, an LLM judge, or a combination of them. This topic tests whether that mechanism gives the right verdict, expresses uncertainty honestly, survives irrelevant changes, and remains suitable for the decision that consumes its output.

## Motivation

A score inherits the evaluator's mistakes. A judge can agree with experts on easy examples yet reverse a ranking when answer order changes, reward verbosity, or fail on trajectories unlike its validation set. Before its scores guide a leaderboard or training loop, the evaluator needs its own expert ground truth, calibration checks, and adversarial failure tests.

## Existing Approaches

- **Expert-labeled trajectory benchmarks.** [AgentRewardBench](../works/agentrewardbench.md) and [MobileJudgeBench](../works/mobilejudgebench.md) compare automatic trajectory judges with expert outcomes across web and mobile agents.
- **Pairwise preference validation.** [Plan-RewardBench](../works/plan-rewardbench.md) controls candidate order and asks evaluators to distinguish preferred tool-use trajectories from confusable negatives.
- **Skill-aware judging.** [SkillTV-Bench](../works/skilltv-bench.md) tests whether judges can verify trajectories whose correctness depends on task-specific skill knowledge.
- **Hybrid verification.** [AgentLens](../works/agentlens.md) combines formal checks with multiple judge dimensions and evidence-linked reviews.
- **Domain calibration.** [AstroVisBench](../works/astrovisbench.md), [PSE-Bench](../works/pse-bench.md), and [FIRE-Bench](../works/fire-bench.md) report human agreement for judges used on scientific outputs. [DiscoveryBench](../works/discoverybench.md) audits its hypothesis-matching evaluator twice: step by step on 200 extraction and matching decisions, then end to end against three annotators ranking predicted hypotheses. [QFT-Bench](../works/qft-bench.md) checks two judge tasks against the same three QFT experts: answer correctness reaches 98% agreement for Opus-5, while derivation faithfulness reaches 73%, so the faithfulness rates rest on a weaker check than the accuracy scores.
- **Conference decisions as the anchor.** [AI-Researcher](../works/ai-researcher.md) tests its paper-review agent on content-matched pairs of accepted and rejected ICLR submissions, and drops the evaluator that separates them worst before rating any generated paper.
- **Domain calibration.** [AstroVisBench](../works/astrovisbench.md), [PSE-Bench](../works/pse-bench.md), and [FIRE-Bench](../works/fire-bench.md) report human agreement for judges used on scientific outputs.
- **A judge with its own benchmark.** [PaperBench](../works/paperbench.md) hand-grades the rubric leaf nodes of partial paper replications, then scores candidate judge backends as binary classifiers against those labels and selects the one with the best F1 per dollar rather than the highest F1.
- **Experts and alternate judges on the same answers.** [HeurekaBench](../works/heurekabench.md) checks its judge twice before using it: eleven domain experts rate the same 25 open-ended answers, and two other frontier models re-score the same agent runs, so rater disagreement and judge-model disagreement are reported separately.
- **Reusable verifiers under shifted requirements.** [AgentProofBench](../works/agentproofbench.md) freezes a Web-agent acceptance program and reruns it on initial states that change what the same instruction requires, comparing reuse against rebuilding. It then branches delivery policies from identical saved openings, so a verifier's panel errors can be read against what the agent finally delivers.

These additions test different measurement objects: [AgentIdeaBench](../works/agentideabench.md) calibrates critics, [AgentActionBench](../works/agentactionbench.md) compares scores from generated and human rubrics, and [PTA-IRT](../works/pta-irt.md) measures how accurately a subset predicts a full suite. Agreement at one level should not be read as validation at all three levels.

[AlphaIdeaBench](../works/alphaideabench.md) checks only the novelty half of its judge: reviewer comments are converted into scores by the same model that serves as judge, and agreement drops on scenario novelty. Its validity and feasibility scores have no human reference.

[Into the Unknown](../works/into-the-unknown.md) validates rubric grading of open research against the scientists who wrote the rubrics. Each original author reviews three blind follow-up papers, and their criticisms are split into items. The rubrics cover all 41 judgments on whether the direction was met, and the judge agrees with every one. Agreement falls to 80.34% on reviewer-style weaknesses and 68.68% on scientific quality and impact, so the rubrics are trusted for necessary conditions, not for merit. A separate four-run study picks the GPT-6-Astra judge for consistency (86.5% against 57.7% same overall grade), although GPT-6-Astra is also one of the evaluated agents.

## Comparison

| Work | Evaluator under test | Ground truth | Reliability signal | Downstream validation |
|---|---|---|---|---|
| [AutoResearchEval](../works/autoresearcheval.md) | Artifact-aware agent judge versus a single-call transcript-only judge | 50 human-labeled research trajectories | Pattern κ 0.75 vs. 0.53; root-category κ 0.83 vs. 0.62; recall 80.7% vs. 63.5% | Failure annotation across 800 trajectories; no per-pattern agreement or isolated artifact-access ablation |
| AgentRewardBench | LLM and rule-based web-agent evaluators | Expert trajectory labels | Precision, recall, agreement across benchmarks | Agent evaluation |
| MobileJudgeBench | Six mobile-agent judge methods × five backends | 931 human-labeled trajectories | Classification metrics, ranking correlation, rate error | Agent ranking and on-policy reward |
| Plan-RewardBench | Reward models and LLM judges | Validated pairwise preferences | Order-swapped pairwise accuracy | No |
| SkillTV-Bench | LLM-as-a-Judge and Agent-as-a-Judge | Skill-aware trajectory labels | Judge accuracy and best-of-N selection | Trajectory selection |
| AgentLens | Hybrid judge plus formal verifier | Executable checks and review evidence | Multi-dimensional quality index | Coding-agent diagnosis |
| AstroVisBench | Multimodal visualization judges | Professional astronomer annotations | Rank correlation and inter-annotator agreement | Judge selection |
| DiscoveryBench | GPT-4 hypothesis-matching evaluator (HMS) | Gold hypotheses replicated from published papers; three annotators' preference rankings over 100 pairs | 95% agreement with human rankings, Fleiss κ = 0.91; 94-99% correct on the extraction and matching steps over 200 examples | Benchmark scoring |
| AI-Researcher | Five LLM paper-review agents in order-swapped pairwise comparison | ICLR accept/reject decisions on 32 content-matched paper pairs (2021-2023) | Acceptance-prediction accuracy 65.62-90.62%; comparable-quality detection (share of pairs rated above -1.0) 93.75-100% | Evaluator selection: the weakest model is dropped from the main experiments |
| PaperBench | SimpleJudge over rubric leaf nodes, five model backends | Hand-graded leaf nodes from partial replications of five papers | Macro-averaged binary F1 (0.59-0.84) reported against cost per paper | Judge backend chosen for the main leaderboard |
| HeurekaBench | G-Eval judge with GPT-4o | 11 single-cell experts on 25 open-ended answers; two alternate judge models | Spearman 0.93 / 0.90 and Cohen's κ 0.85 against expert aggregates; inter-judge Spearman 0.84 / 0.79 | Judge selection and planner-model ranking |
| [AgentIdeaBench](../works/agentideabench.md) | Literature-grounded critics | Landmark anchors; human judgments on 100 CS pairs | 77% human-majority agreement; calibration controls | Static/Active comparisons |
| [AgentActionBench](../works/agentactionbench.md) | Generated paper-specific rubrics | Human rubrics on 15 papers | Pearson 0.93; Spearman 0.88 between rubric-source scores | Reproduction-stage breakdown; not item-level judge accuracy |
| [PTA-IRT](../works/pta-irt.md) | Subset-to-full estimator | Full-suite outcomes of held-out agents | MAE; Kendall tau; Spearman rho | Four-fold validation and trajectory ablations |
| [QFT-Bench](../works/qft-bench.md) | Opus-5 and GPT-5.6 judges for answer correctness and derivation faithfulness | Three QFT experts on 60 responses from 15 models | Correctness agreement 98% / 92%; faithfulness agreement 73% / 67% | Opus-5 used for correctness fallback, faithfulness rates, and error categories |
| [AgentProofBench](../works/agentproofbench.md) | Frozen Web-agent acceptance programs written by DeepSeek Flash/Pro, reused or rebuilt; fresh online judgments for comparison | Reference rules over 556 natural terminal states and 558 states from source, background, and related initial conditions; LLM audit agrees on 191/192 | Balanced accuracy; complete-panel and decision-replay joint pass; reuse-minus-rebuild BA with family bootstrap | Delivery from identical saved openings: 32/33 panel-correct vs. 1/11 panel-error assignments deliver correctly; program gate below neutral continuation |
| [AlphaIdeaBench](../works/alphaideabench.md) | Gemini 3.7 Flash judge on four novelty axes | Reviewer comments on 600 ICLR 2026 / NeurIPS 2025 / ICML 2025 papers, mapped to 1–5 scores by Gemini 3.7 Flash | Within-±1 agreement ~94.5–97.4% (problem), 95.9–96.8% (method), 80.6–87.5% (scenario); GPT-5 mini re-score Spearman ρ 0.81 / 0.83 | Harness and backbone rankings; validity and feasibility have no human reference |
| [Into the Unknown](../works/into-the-unknown.md) | GPT-6-Astra agentic judge applying author-specified integrity and direction rubrics (Codex SDK, four runs, node majority) | Criticisms from each original paper's author on three blind follow-ups; a Claude-Opus-5.5 judge for the consistency comparison | Coverage / matching 100% / 100% (direction met), 96.97% / 80.34% (reviewer weaknesses), 89.05% / 68.68% (quality and impact); same overall grade in 86.5% vs. 57.7% of four-run repeats | GPT-6-Astra chosen as default judge for all 135 submissions |

## Open Questions

- Which judge metrics predict ranking fidelity, reward usefulness, and deployment decisions?
- How should evaluator uncertainty propagate into benchmark leaderboards and statistical comparisons?
- How can verifier coverage and false-negative surfaces be measured when no complete oracle exists?
- When do pairwise, pointwise, rubric, and deterministic evaluators fail differently?
- How should benchmarks defend evaluators against reward hacking, style bias, contamination, and adaptive optimization?

## Related Works

- [AgentProofBench](../works/agentproofbench.md)
- [AlphaIdeaBench](../works/alphaideabench.md)
- [QFT-Bench](../works/qft-bench.md)
- [Into the Unknown](../works/into-the-unknown.md)
- [AgentIdeaBench](../works/agentideabench.md)
- [PTA-IRT](../works/pta-irt.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [AgentLens](../works/agentlens.md)
- [AgentActionBench](../works/agentactionbench.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [PSE-Bench](../works/pse-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [HeurekaBench](../works/heurekabench.md)
- [AstroVisBench](../works/astrovisbench.md)
- [AgentRewardBench](../works/agentrewardbench.md)
- [PaperBench](../works/paperbench.md)
- [AI-Researcher](../works/ai-researcher.md)
- [DiscoveryBench](../works/discoverybench.md)
