# Plan-RewardBench (2026)

## Overview

Plan-RewardBench is a benchmark that measures how well reward models and LLM judges identify the preferred agent trajectory in tool-integrated scenarios. It contains 1,171 pairwise trajectory-preference instances spanning seven evaluation splits and four scenario families.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.08178>
- **Code:** <https://github.com/wyy-1112/Plan-RewardBench>
- **Venue:** ACL 2026

## Summary

Plan-RewardBench argues that existing reward-model benchmarks score single responses or isolated tool calls in short contexts, leaving no way to assess reward models on the multi-turn, tool-executed trajectories that agentic systems actually produce. The authors assemble preference pairs in which the tool environment and user intent are held fixed and only the agent's trajectory varies, matching a validated chosen trajectory against a confusable hard negative. Across 21 evaluated systems the best macro-average is 69.96% (Qwen-Plus), and accuracy degrades in the long-horizon regime beyond 32k tokens, most steeply for pairwise LLM judges and more gradually for pointwise reward models.

## Tasks

1,171 preference pairs across seven evaluation splits: Tool-Irrelevance / Unavailable 275, Robust Recovery 361, Planning-Single (Easy) 144, Planning-Single (Hard) 158, Planning-Multi (Easy) 109, Planning-Multi (Hard) 73, and Safety Refusal 51. Those splits roll up into four scenario families — Safety Refusal, Tool-Irrelevance / Unavailability, Complex Planning, and Robust Error Recovery — with Complex Planning stratified by horizon (single- vs. multi-turn) and by difficulty. Seed tasks and MCP tool registries come from Toucan, and candidates are expanded by re-running rollouts under the Qwen-Agent and OpenAI-Agent runtimes while varying base model, system prompt, temperature and seed, yielding a trajectory pool that is 70% natural rollouts, 22% perturbations, and 8% rule-based injections.

## Domains

Text-only, tool-augmented agent trajectories over MCP-style tool registries, covering safety refusal, tool irrelevance and unavailability, multi-step planning, and error recovery.

## Evaluation

- **Pairwise accuracy.** The primary metric is the share of pairs on which an evaluator selects the gold-preferred trajectory, and the headline score is the macro-average across the seven evaluation splits.
- **Order-swap protocol.** Each pair is judged twice with the candidate order reversed and the average correctness is reported, controlling positional bias for pairwise evaluators; pointwise discriminative reward models score each trajectory independently and are unaffected.
- **Unified input.** Every evaluator receives the same context — the tool registry schemas, the multi-turn conversation, and the full interleaved trajectory of reasoning, tool calls, and execution outputs — so only the trajectory differs within a pair.
- **Human audit.** Two annotators independently pick the preferred trajectory on a stratified subset of 51–80 pairs per family, with a third senior annotator resolving disagreements; pre-adjudication Cohen's κ runs 0.71–0.86 across the four families.
- **Reported.** Macro-average accuracy across 21 evaluators spans 50.67% (Llama-3.2-8B-Instruct) to 69.96% (Qwen-Plus), with Inf-ORM-Llama3.1-70B the strongest discriminative reward model at 69.21%. Per-family peaks fall to different systems — GPT-5 on Safety Refusal at 84.80% and Gemini-3-Flash (preview) on Tool-Irrelevance at 75.55% — and no evaluator exceeds 70% on Multi-turn Hard planning. No human accuracy baseline is reported.

## Typical Duration

Offline judging over pre-recorded trajectory pairs — the release requires no tool re-execution or external-service access — so no per-task step or wall-clock budget is defined. Trajectory scale is reported instead: 2–64 turns (mean 10.6, median 9.0), per-split average input from 1,186 tokens on Planning-Single (Easy) to 6,554 on Planning-Multi (Hard), and a longest single instance of 29,622 tokens.

## Main Contribution

A trajectory-level preference benchmark for complex tool-integrated scenarios, pairing validated positive trajectories with confusable hard negatives so that discriminative reward models, generative reward models, and LLM judges can be compared under one pairwise protocol.

## Key Design Ideas

- Fixed tool environment and user intent within each pair, so the agent's trajectory is the only variable an evaluator sees.
- Three hard-negative sources: multi-model natural rollouts, rule-based perturbations, and minimal-edit rewrites that alter only assistant-visible text while preserving the recorded tool calls and outputs.
- Pair assembly under difficulty and bias control: near-miss and discriminative score gaps, stratification by length and tool-token ratio, and style-controlled negatives.
- Two-stage labeling in which a three-judge panel scores each candidate on a 1–5 family-specific rubric with median aggregation, meta-review resolves wide or conflicting scores, and a separate pairwise post-check confirms the preference direction; the generator set is disjoint from the judge set.

## Strengths

- Holding the tool environment and user intent fixed inside each pair isolates trajectory quality from an evaluator's ability to handle varied prompts.
- Minimal-edit hard negatives preserve the recorded tool calls and the surface style of the source trajectory, so a pair cannot be separated on verbosity or formatting alone.
- Reporting seven splits rather than a single aggregate shows that the best overall evaluator is not the best on safety refusal or on tool irrelevance.

## Limitations

- Repository note: Gold preference labels are produced by an LLM judge panel and confirmed by an automated pairwise post-check; direct human verification covers a stratified 51–80 pairs per family, so the large majority of the 1,171 labels rest on model judgement.
- Repository note: Split sizes are deliberately non-uniform — Safety Refusal holds 51 pairs against Robust Recovery's 361 — and the headline score is a macro-average over the seven splits, so the smallest split carries the same weight as the largest.

## Related Works

- [TRACE](./trace.md) — Also evaluates whole agent trajectories rather than final answers, but scores a single trajectory against multi-dimensional rubrics rather than asking an evaluator to choose between a chosen and a rejected trajectory.
- [FinTrace](./fintrace.md) — Also multi-dimensional trajectory evaluation, but grades the agent's own trajectory in finance rather than measuring how accurately reward models and judges rank tool-use trajectories.
- [AgentAtlas](./agentatlas.md) — Also concerned with what evaluation misses inside a trajectory, but applies a control-decision taxonomy over existing benchmarks rather than scoring judges on trajectory preference pairs.
