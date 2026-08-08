# AI & Machine Learning Research

> **English** | [简体中文](../zh/domains/ai_ml_research.md)

## Scope

AI and machine learning as the science under study: reproducing, rediscovering, and extending published AI research.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| EXP-Bench | 2025 | Conduct complete research experiments from influential AI publications — formulate hypotheses, design and implement procedures, execute, and conclude — across computer vision, NLP, and reinforcement learning. | 461 tasks from 51 NeurIPS 2024 and ICLR 2024 papers, decomposed into 12,737 individually gradable subtasks, each with a research question and incomplete starter code. | LLM judges for design, implementation (vs. ground-truth git diffs), and conclusion, plus a containerized execution validator; All·E✓ requires all four (best reported: 0.5%). | [→](../works/exp-bench.md) |
| FIRE-Bench | 2026 | Rediscover established, verifiable findings from recent high-impact ML research — empirical studies of LLM behavior, plus a CV and neural-network-analysis extension — given only the high-level research question. | 40 fully executed tasks built from per-paper research-problem trees (root question → subproblems → leaf experiments); all compute-light (≤24 h on one 80GB A100). | Claim-level precision/recall/F1 by semantic entailment between atomic claims of the agent's conclusion and the ground-truth findings; judge validated at F1 0.89 against humans. | [→](../works/fire-bench.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks in language modeling and time-series forecasting (alongside mathematics and bioinformatics), covering the full research lifecycle with no baseline code. | 20 tasks; the agent submits held-out test-split predictions as a CSV. | Execution-based, outcome-only scoring by task-specific evaluators; SOTA-normalized score with a 'march of nines' transform near the ceiling. | [→](../works/airs-bench.md) |
| AstaBench | 2025 | Holistic scientific-research ability weighted toward computer science: literature understanding, code & execution, data analysis, and end-to-end discovery, with many problems from real user requests to deployed Asta agents. | 2,400+ problems across 11 benchmarks with a standard, reproducible tool environment and per-benchmark corpus date cutoffs; 57 agents scored. | Per-benchmark metrics (F1, recall@30, exact match, LLM-judged rubrics and hypothesis matching) with time-invariant dollar-cost accounting and score-vs-cost Pareto frontiers. | [→](../works/astabench.md) |

## Related Works

- [EXP-Bench](../works/exp-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
