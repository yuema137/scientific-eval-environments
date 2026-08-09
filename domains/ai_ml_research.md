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
