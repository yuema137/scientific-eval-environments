# Into the Unknown (2026)

> **English** | [简体中文](../zh/works/into-the-unknown.md)

> **First appeared:** 2026-10-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.19159)

## Overview

Into the Unknown asks whether an agent can carry out a research direction that nobody has pursued yet. A research benchmark usually grades against something a human has already done: a published result, a reference solution, or a medal threshold. Here the author of a science paper proposes an unpublished follow-up direction and writes down the conditions a successful follow-up must meet. The agent receives the paper, its code and data, and that specification, and must deliver a follow-up paper with code and logs. An agentic judge then checks the submission against the scientist's conditions, split into integrity, completeness, and sufficiency.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** [Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159), 2026 preprint (arXiv comment: "preprint under review").
- **Code:** <https://github.com/prometheus-eval/into-the-unknown>
- **Data:** <https://huggingface.co/datasets/prometheus-eval/into-the-unknown> (tasks, agent trajectories, the 135 agent-written papers)
- **Leaderboard:** <https://prometheus-eval.github.io/into-the-unknown/viewer/>
- **Venue:** arXiv preprint (cs.AI, cs.CL, cs.LG), 2026

## Summary

Each instance pairs an original paper with a task specification and two rubrics. The direction-specific rubric turns the scientist's success conditions and required deliverables into leaf-level questions. The integrity rubric lists what would make a submission untrustworthy whatever it reports, such as numbers in the paper that trace to no log entry. A submission counts as valid only if it passes every node for integrity (C1), completeness (C2), and sufficiency (C3). All conditions are stated in the task specification, so the difficulty comes from doing the work, not from hidden criteria. None of 135 submissions is valid, so the strict metric is 0% for every agent; node-level pass rates are what separate the agents.

## Tasks

15 open problems from 10 scientists currently or formerly affiliated with US Department of Energy national laboratories (LANL, SNL, LBNL, LLNL, PPPL, Ames). One paper has no national-laboratory author and was added to cover physics-informed neural networks. Group A has 8 papers published in 2024 or earlier; Group B has 7 papers submitted in 2026. Selection required a first or last author who could take part and computational experiments, so that a follow-up can be done in code alone. About half the directions are exploratory: for example, stress-testing variational lattice scalar QED in valid and invalid regimes (P6), or finding where Vlasov theory stops predicting MagCBET particle-in-cell behaviour (P13). Others are optimization targets, such as cutting the stochastic probes that Projected Hessian Learning needs (P11). Claude-Opus-5 drafted the specifications and rubrics from the scientists' answers, and the scientists then made 112 edits. The workspace contains the original paper converted to Markdown, plus its code and data.

## Domains

By Table 1 labels: quantum computing (4: P5, P9, P10, P14), plasma physics (2: P6, P13), computational chemistry (2: P1, P11), materials science (2: P2, P15), scientific machine learning (3: P4 autonomous-experimentation acquisition, P8 parameterized PINNs, P12 exact large-scale Gaussian processes), computational imaging (1: P3) and color science (1: P7, perceptual color space).

## Evaluation

- A grading agent answers each rubric's leaf questions. The node pass fraction is computed for each condition. Strict grading requires every node to pass and "almost" grading at least 90%. The main metric is the fraction of submissions passing C1, C2, and C3 under strict grading.
- The judge is GPT-6-Astra in the Codex SDK at maximum reasoning effort. Each submission is judged four times and combined by per-node majority (3 of 4; a 2–2 tie fails).
- Nine agents, each in its native harness at maximum reasoning effort and 1M context: Claude-Opus-4.8, Opus-5, Fable-5, and Opus-5.5 (claude-agent-sdk); GPT-5.6-Sol and GPT-6-Astra (codex-sdk); DeepSeek-V4-Pro-0813 (deepseek-harness); Kimi-K3 (kimi-agent-sdk); GLM-5.3 (software-agent-sdk).
- Results (Table 2): strict validity is 0.00% for all nine. Integrity / direction node pass rates range from GPT-6-Astra's 97.77% / 83.62%, then Claude-Opus-5.5's 90.38% / 80.00%, down to GLM-5.3's 54.41% / 44.25%. Only three agents pass strict C1 on any paper: GPT-6-Astra on 11 of 15, GPT-5.6-Sol on 6, Claude-Opus-5.5 on 4. One submission (GPT-6-Astra) is both honest and complete.
- Failure accounting (Figure 3): 114 of 135 submissions fail integrity. The most frequent violations are paper–code mismatches (90), numbers contradicting the evidence (85), and false claims of completed work (68). 128 submissions lack required files or records, 120 miss method or protocol requirements, and 83 miss the scientist's targets. An audit of 64 trajectories finds lenient self-verification in 58, insufficient backtracking in 34, and self-directed scope reduction in 21.
- Judge validation (Appendix A): each original author reviewed three blind follow-ups, by Claude-Opus-5, Claude-Fable-5, and GPT-5.6-Sol. Their criticisms were split into items. The rubrics cover all 41 judgments on meeting the direction, and the pipeline agrees on all of them. For major reviewer weaknesses, coverage is 96.97% and agreement 80.34% (paper-averaged); for scientific quality and impact, 89.05% and 68.68%.
- Judge consistency (Appendix B, 52 submissions judged four times each): the GPT-6-Astra judge gives the same overall grade in 86.5% of cases against 57.7% for a Claude-Opus-5.5 judge, which is why GPT-6-Astra is the default.
- Repository note: GPT-6-Astra is both the default judge and one of the evaluated agents, and it has the highest node pass rates. The consistency study compares judges with each other, not with self-preference.

## Typical Duration

No time limit is imposed; agents run until they end their own session, with up to five relaunches (a "Ralph Wiggum" loop). Six GPU papers get one 8×H200 node, and the other nine get a 32-vCPU Xeon node with 61 GiB of usable RAM; 1 TB of storage is provided. The 135 submissions took 1,942.81 hours to generate and 62.95 hours to evaluate in wall-clock time. Median execution time per agent ranges from 1.3 hours (GPT-6-Astra) to 19.5 hours (DeepSeek-V4-Pro-0813). Internet access is unrestricted.

## Main Contribution

Grades open research, which has no reference answer, against necessary conditions written in advance by the original paper's author. A separate integrity rubric exposes submissions that look like follow-ups but report unperformed or unsupported work.

## Key Design Ideas

- Fixing the direction and the scientist's bar narrows the space of acceptable follow-ups to one that a rubric can check.
- Pre-staging the original code and data separates pursuing a new direction from reimplementing old work.
- Directions are verified by the original authors as having no known published counterpart, so internet access is not restricted.
- Reporting both strict and almost grading, plus node-level rates, keeps agents distinguishable when every strict score is zero.

## Strengths

- The expert meta-verification measures where the rubrics stop. Agreement falls from 100% on the question the rubrics target to 68.68% on scientific merit.
- Failure categories, trajectory behaviours, and integrity violations are counted per submission rather than described anecdotally.
- Trajectories, papers, file systems, and judge verdicts are released.
- A bootstrap analysis with Holm correction finds no evidence that longer execution yields better submissions, either across agents or within an agent.

## Limitations

- 15 problems, with at most four in any one field.
- The authors note that rubrics check necessary conditions; they do not capture narrative quality or whether prior work actually motivates the method, which remain for expert review.
- Repository note: the paper's own numbers do not always agree. The trajectory audit samples "64 of the 105 submissions" and Figure 6 covers "all 105 submissions", while the benchmark has 135. Section 5.2 says GPT-5.6-Sol passes the most nodes and is the only agent with passing integrity checks; Table 2 gives GPT-6-Astra the highest node rates, and three agents pass integrity. The card follows Table 2.
- Repository note: the paper states no per-run token or dollar cost.

## Related Works

- [PaperBench](./paperbench.md) — Grades replication of a published paper against author co-developed rubrics; Into the Unknown grades follow-ups no one has done.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also uses tasks contributed by practising scientists, but each task ships with an oracle solution and tests.
- [MLR-Bench](./mlr-bench.md) — Open-ended research papers scored by LLM reviewers rather than author-specified conditions.
- [EurekaBench](./eurekabench.md) — From an overlapping author group; explains known observations rather than extending a paper.
