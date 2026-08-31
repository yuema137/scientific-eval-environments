# End-to-End Research

> **English** | [简体中文](../zh/activities/end_to_end_research.md) · [← All activities](./README.md)

## Definition

Evaluates the agent across a broad, multi-stage research lifecycle rather than one isolated stage — spanning several of problem formulation, literature review, hypothesis generation, methodology, experimentation, analysis, interpretation, and reporting.

## Scope

Assigned conservatively, only when the benchmark explicitly evaluates a substantial multi-phase research process across several major research phases. Long-horizon difficulty or the use of many tools alone does not qualify.

## Task Patterns

These benchmarks evaluate agents across the full arc of scientific research rather than any single stage. [MLGym](../works/mlgym.md) and [MLR-Bench](../works/mlr-bench.md) exercise the complete ML-research loop — idea and hypothesis generation, data creation, method implementation, experimentation, analysis, and paper writing — with MLR-Bench making its four stages (idea, proposal, experimentation, writing) explicit. [AIRS-Bench](../works/airs-bench.md) and [ResearchClawBench](../works/researchclawbench.md) push further by withholding baseline code or the target paper, forcing agents to formulate problems, review literature, design methodology, and run experiments from scratch. [AstaBench](../works/astabench.md) situates end-to-end discovery (E2E-Bench, E2E-Bench-Hard) alongside literature, code, and data-analysis benchmarks, isolating the multi-phase discovery capability within a broader suite.

What distinguishes these from single-stage tasks is that success depends on chaining several research phases where each depends on the last: an agent cannot succeed by tuning hyperparameters or answering one retrieval query, but must formulate a problem, generate hypotheses, build and run experiments, and interpret or report results — often graded against expert rubrics, hidden target papers, or automated reviewers that judge the whole pipeline rather than an isolated output.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AstaBench | 2025 | End-to-end discovery within a broader research-assistance suite | 11-benchmark suite, 2,400+ problems; E2E-Bench/E2E-Bench-Hard for discovery | Cost-controlled holistic scores on public leaderboard | [card](../works/astabench.md) |
| MLGym | 2025 | Ideation, data, method implementation, experimentation, analysis, iteration | Gym environment, MLGym-Bench: 13 open-ended AI-research tasks (CV/NLP/RL/game theory) | Improve over provided baselines across full research loop | [card](../works/mlgym.md) |
| MLR-Bench | 2025 | Idea generation, proposal, experimentation, paper writing | 201 open-ended ML tasks from NeurIPS/ICLR/ICML; MLR-Agent scaffold | MLR-Judge rubric scores, stepwise and end-to-end | [card](../works/mlr-bench.md) |
| AIRS-Bench | 2026 | Full research lifecycle, no baseline code, workflows from scratch | 20 frontier tasks across language modeling, math, bioinformatics, time-series | Design and execute end-to-end research workflows | [card](../works/airs-bench.md) |
| ResearchClawBench | 2026 | Problem formulation, literature review, experimentation, re-discovery from raw data | 40 expert-curated tasks, 10 domains; hidden target paper, related literature, raw data | Reference-Anchored Discovery Score vs weighted multimodal rubrics | [card](../works/researchclawbench.md) |
| AutoResearchEval | 2026 | Carry a task through ideation, retrieval, execution, analysis, writing and self-review | 100 tasks grounded in published frontier science; 8 harness-model combinations producing 800 trajectories | Process-level failure attribution against ARFT's 45 patterns rather than a performance score | [card](../works/autoresearcheval.md) |
| AI Research Preference Models | 2026 | Steer an AI research agent's search by choosing which candidate solutions get executed | Frozen-LM preference models in AIRA-dojo's tree search over 20 AIRS-Bench ML-research tasks; 24 h per task on one H200 | Normalized score 0.684 -> 0.729 while using under two-thirds of the execution budget | [card](../works/ai-research-preference-models.md) |
| Curation-Bench | 2026 | Iteratively research and revise a training-data selection policy from downstream evaluation | Fixed VLM, training recipe and evaluator; executable policy edited for up to 10 rounds | A data policy that improves downstream quality under a controlled data budget | [card](../works/curation-bench.md) |
| PostTrainBench | 2026 | Autonomously choose data, training method, compute allocation and experiments to post-train a base LLM | Seven targets; four base models; one H100 for 10 hours per task | Highest held-out benchmark score from the submitted trained model | [card](../works/posttrainbench.md) |
| ASI-Bench | 2026 | Select the method, build the workflow, run it and produce verifiable results within one research project, at four guidance levels (B1–B4) | 60 project-level tasks across 11 scientific domains; sandboxed, agent-neutral harnesses | Task score 0–100 at each guidance level; macro means B1 50.91 / B2 29.10 / B3 26.62 across 18 agent–model configurations | [card](../works/asi-bench.md) |

## Related Works

- [AstaBench](../works/astabench.md)
- [MLGym](../works/mlgym.md)
- [MLR-Bench](../works/mlr-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [AI Research Preference Models](../works/ai-research-preference-models.md)
- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
- [ASI-Bench](../works/asi-bench.md)
