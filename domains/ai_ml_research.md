# AI & Machine Learning Research

> **English** | [简体中文](../zh/domains/ai_ml_research.md) · [← All domains](./README.md)

## Scope

AI and machine learning as the science under study: reproducing, rediscovering, and extending published AI research.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| EXP-Bench | 2025 | Conduct complete research experiments from influential AI publications — formulate hypotheses, design and implement procedures, execute, and conclude — across computer vision, NLP, and reinforcement learning. | 461 tasks from 51 NeurIPS 2024 and ICLR 2024 papers, decomposed into 12,737 individually gradable subtasks, each with a research question and incomplete starter code. | LLM judges for design, implementation (vs. ground-truth git diffs), and conclusion, plus a containerized execution validator; All·E✓ requires all four (best reported: 0.5%). | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | Rediscover established, verifiable findings from recent high-impact ML research — empirical studies of LLM behavior, plus a CV and neural-network-analysis extension — given only the high-level research question. | 40 fully executed tasks built from per-paper research-problem trees (root question → subproblems → leaf experiments); all compute-light (≤24 h on one 80GB A100). | Claim-level precision/recall/F1 by semantic entailment between atomic claims of the agent's conclusion and the ground-truth findings; judge validated at F1 0.89 against humans. | [→](../works/fire-bench.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks in language modeling and time-series forecasting (alongside mathematics and bioinformatics), covering the full research lifecycle with no baseline code. | 20 tasks; the agent submits held-out test-split predictions as a CSV. | Execution-based, outcome-only scoring by task-specific evaluators; SOTA-normalized score with a 'march of nines' transform near the ceiling. | [→](../works/airs-bench.md) |
| AstaBench | 2025 | Holistic scientific-research ability weighted toward computer science: literature understanding, code & execution, data analysis, and end-to-end discovery, with many problems from real user requests to deployed Asta agents. | 2,400+ problems across 11 benchmarks with a standard, reproducible tool environment and per-benchmark corpus date cutoffs; 57 agents scored. | Per-benchmark metrics (F1, recall@30, exact match, LLM-judged rubrics and hypothesis matching) with time-invariant dollar-cost accounting and score-vs-cost Pareto frontiers. | [→](../works/astabench.md) |
| PaperBench | 2025 | Replicate state-of-the-art AI research — 20 ICML 2024 Spotlight and Oral papers — from understanding contributions to executing experiments. | From-scratch replication decomposed into 8,316 gradable rubric tasks; ML-PhD human baseline recruited. | LLM judge grading against author-co-developed hierarchical rubrics, with the judge assessed on a separate judge benchmark. | [→](../works/paperbench.md) |
| MLE-bench | 2024 | Perform end-to-end machine-learning engineering on real competitions. | 75 curated Kaggle competitions with real datasets; agents train models and submit solutions (OpenAI). | Kaggle medal thresholds (bronze/silver/gold) against public-leaderboard human baselines. | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | Iteratively build and improve ML solutions in an interactive environment. | 200+ Kaggle challenges in a Gym-style environment supporting SFT/RL of agents. | Iterative improvement, long-horizon solution quality, and error-resolution efficiency across 8 LLMs. | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | Improve model performance through iterative ML experimentation. | 13 tasks (CIFAR-10 to BabyLM); agents read/write files, run code, inspect outputs, iterate. | Success rate (>10% improvement over starter-code baseline) and average improvement. | [→](../works/mlagentbench.md) |
| ML-Bench | 2023 | Accomplish ML tasks using real repository-level code. | 9,641 examples over 18 GitHub repos; ML-LLM-Bench (text-to-code) + ML-Agent-Bench (sandbox). | Pass@5 for code generation; success rate for autonomous execution. | [→](../works/ml-bench.md) |
| DSBench | 2024 | Perform data analysis and predictive modeling on realistic tasks. | 540 tasks (466 analysis + 74 modeling) with long context, multimodal, multi-table data. | Task-solve rate for analysis; relative performance gap for modeling. | [→](../works/dsbench.md) |
| DA-Code | 2024 | Write executable data-science code for wrangling and analytics. | Agentic data-science coding tasks in a controllable Docker sandbox. | Execution-based accuracy; best LLMs 30.5%. | [→](../works/da-code.md) |
| BLADE | 2024 | Make sound analytical decisions in open-ended data-driven science. | 12 datasets with research questions and independent expert reference analyses. | Multifaceted automatic grading of analytical decisions vs. expert ground truth. | [→](../works/blade.md) |
| MLRC-Bench | 2025 | Propose and implement novel methods to win ML research competitions. | 7 competition tasks; agents submit solutions scored against baseline and top humans. | Objective gap-closed metric; best agent closes 9.3% of the baseline-to-human gap. | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | Set up and execute tasks from real research repositories to reproduce results. | 45 end-to-end + 152 sub-problem + 602 auto-generated tasks from ML/NLP GitHub repos. | End-to-end and scenario (landmark) success; GPT-4o 16.3% end-to-end. | [→](../works/super.md) |
| MLR-Bench | 2025 | Conduct open-ended ML research from idea to paper. | 201 tasks across idea generation, proposal, experimentation, and paper writing (workshops). | MLR-Judge (LLM reviewers + rubrics), validated against experts; ~80% fabricated results. | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | Do frontier AI R&D / research engineering under time budgets. | 7 open-ended research-engineering environments; 71 8-hour attempts by 61 human experts (METR). | Best-of-k against reference solutions under 2/8/32-hour budgets; direct human comparison. | [→](../works/re-bench.md) |
| MLGym | 2025 | Carry out open-ended AI research across CV, NLP, RL, and game theory. | MLGym-Bench: 13 tasks in a Gym environment supporting RL training of agents (Meta). | Task performance across the 13 tasks over five frontier models. | [→](../works/mlgym.md) |
| ResearchCodeBench | 2025 | Implement the novel contributions of recent ML papers as code. | 212 challenges from top 2024–2025 papers; a 13-paper contamination-safe subset. | Success rate with contamination and error-pattern analyses; best 37.3%. | [→](../works/researchcodebench.md) |
| IdeaBench | 2024 | Generate novel research ideas grounded in scientific context. | Idea generation from influential-paper titles/abstracts and their references. | Two-stage GPT-4o ranking on novelty/feasibility plus a relative Insight Score. | [→](../works/ideabench.md) |
| LiveIdeaBench | 2024 | Generate scientific ideas from minimal (single-keyword) context. | 1,180 keywords across 22 domains; 40+ models scored by an LLM panel. | Five creativity dimensions (originality, feasibility, fluency, flexibility, clarity). | [→](../works/liveideabench.md) |
| DevAI / Agent-as-a-Judge | 2024 | Autonomously develop AI/ML projects meeting hierarchical requirements. | 55 automated-AI-development tasks with 365 hierarchical user requirements. | Requirement-level, process-aware Agent-as-a-Judge evaluation, as reliable as humans. | [→](../works/devai.md) |
| Replica | 2026 | Reproduce a redacted results figure from a published ML or AI-for-science paper by re-running the experiment behind it. | 310 tasks (242 train / 68 test) auto-generated from 100 papers published 1990–2026; 60 minutes on a one-seventh MIG slice of an H200. | Five-dimension rubric judge generated with the gold plot hidden; two judge draws agree at τ = 0.66, against τ = 0.30 between two human raters. | [→](../works/replica.md) |
| Beyond Final Scores | 2026 | Improve a correct but deliberately suboptimal ML or systems artifact over a long run. | 36 AutoLab tasks in four families (Model Development 7, System Optimization 15, Puzzle & Challenge 10, CUDA 4); 756 rollouts across seven models. | Automated per-task verifier with scores normalised to [0, 1]; a manual audit found only 1.2% of solutions genuinely novel and 6.3% exploiting evaluation-specific shortcuts. | [→](../works/beyond-final-scores.md) |
| AutoWorldModel-Bench | 2026 | Autonomously improve a provided world model with no improvement direction specified in advance. | 64 sessions (2 agents × 8 games × 4 base architectures), 6 hours on one H100 per session, 10-minute cap per training run. | Held-out composite of Position L1 and Alive F1 at h ∈ {1, 10, 20}; 33 of 64 sessions reach Δ ≥ +0.10 and 91% of winning edits are substantive rather than hyperparameter tweaks. | [→](../works/autoworldmodel-bench.md) |
| AI Research Preference Models | 2026 | Decide which of an AI research agent's candidate ML solutions are worth spending GPU time to execute. | Two frozen-LM preference models (plan/code reasoning; and pilot experiments under a 5-minute cap) inserted into AIRA-dojo's child-creation step over 20 AIRS-Bench tasks; 24 h on one H200 per task, 10 seeds, 200 GPU-hours total. | AIRS-Bench normalized score: 0.684 unguided -> 0.711 inference-only -> 0.729 agentic, against a 0.748 validation-oracle ceiling; new SOTA on WinoGrande (94.1%) and SVAMP (95.7%). | [→](../works/ai-research-preference-models.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the AI and machine learning research subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`LM` language modeling & NLP · `CV` computer vision & vision-language modeling · `RL` reinforcement learning · `GT` game theory & multi-agent decision making · `TS` time-series forecasting · `WM` world modeling & learned dynamics · `INTERP` neural-network analysis & interpretability · `MLE` machine-learning engineering & model development · `SYS` ML systems, kernels & performance engineering · `DS` data science & statistical data analysis · `CODE` research-code implementation, setup & reproduction · `IDEA` research ideation & hypothesis generation · `GEN` curriculum-wide or unspecified, no single subfield

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
| MLR-Bench | GEN | ✔ | ✔ | ◐ | ✔ | ✘ | ✔ | ✔ | **5.5** | ✘ | ✔ | ✘ | 1 | 2 | 3 | **7** |
| AIRS-Bench | LM, TS | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| PaperBench | GEN | ✔ | ✘ | ◐ | ◐ | ✔ | ✔ | ✔ | **5** | ✔ | ✔ | ◐ | 1 | 1 | 3 | **7.5** |
| AI Research Preference Models | GEN | ? | ✔ | ✔ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| Replica | GEN | ? | ✘ | ✔ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ◐ | 1 | 2 | 2 | **7** |
| DevAI / Agent-as-a-Judge | MLE | ✔ | ◐ | ◐ | ✔ | ✘ | ✔ | ✔ | **5** | ✘ | ✔ | ◐ | 1 | 1 | 3 | **6.5** |
| FIRE-Bench | LM, CV, INTERP | ? | ✔ | ◐ | ? | ✔ | ✔ | ✔ | **4.5** | ◐ | ✘ | ◐ | 1 | 1 | 3 | **6** |
| AstaBench | GEN | ◐ | ◐ | ✔ | ? | ◐ | ✔ | ✔ | **4.5** | ◐ | ✔ | ◐ | 2 | ? | 1 | **5** |
| MLE-bench | MLE | ◐ | ◐ | ◐ | ? | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 3 | 1 | 3 | **9** |
| EXP-Bench | CV, LM, RL | ? | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ◐ | ◐ | 2 | 2 | 3 | **8.5** |
| MLRC-Bench | GEN | ? | ◐ | ◐ | ◐ | ✘ | ✔ | ✔ | **3.5** | ✔ | ◐ | ✔ | 3 | 0 | 3 | **8.5** |
| Beyond Final Scores | MLE, SYS | ? | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **3.5** | ◐ | ✘ | ✘ | 3 | 1 | 4 | **8.5** |
| DSBench | DS | ? | ◐ | ◐ | ◐ | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 2 | 2 | 2 | **7** |
| MLGym | CV, LM, RL, GT | ✔ | ◐ | ◐ | ✘ | ✘ | ◐ | ✔ | **3.5** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| SUPER | CODE | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | ✔ | **3** | ◐ | ✘ | ✘ | 3 | 3 | 3 | **9.5** |
| MLE-Dojo | MLE | ✘ | ◐ | ◐ | ✘ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | 1 | 3 | **8** |
| DA-Code | DS | ? | ◐ | ✘ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| MLAgentBench | MLE | ✘ | ◐ | ◐ | ? | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ✔ | 2 | 1 | 3 | **7.5** |
| RE-Bench | SYS, MLE | ? | ◐ | ✔ | ? | ✘ | ◐ | ✔ | **3** | ✔ | ✘ | ✔ | 2 | 0 | 2 | **6** |
| ResearchCodeBench | CODE | ? | ✘ | ✘ | ? | ✔ | ✔ | ✘ | **2** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| BLADE | DS | ? | ◐ | ✘ | ✘ | ✘ | ✔ | ◐ | **2** | ◐ | ◐ | ✘ | 2 | 1 | 3 | **7** |
| IdeaBench | IDEA | ✘ | ✘ | ✘ | ? | ✔ | ✔ | ✘ | **2** | ◐ | ◐ | ✔ | 0 | 3 | 2 | **7** |
| ML-Bench | CODE | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✔ | ✘ | ✔ | 3 | 3 | 3 | **11** |
| AutoWorldModel-Bench | WM | ? | ◐ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| LiveIdeaBench | IDEA | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 1 | 3 | 2 | **7.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
- [PaperBench](../works/paperbench.md)
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
- [Replica](../works/replica.md)
- [Beyond Final Scores](../works/beyond-final-scores.md)
- [AutoWorldModel-Bench](../works/autoworldmodel-bench.md)
- [AI Research Preference Models](../works/ai-research-preference-models.md)
