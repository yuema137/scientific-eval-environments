# ToolPRMBench (2026)

> **English** | [简体中文](../zh/works/toolprmbench.md)

## Overview

ToolPRMBench is a benchmark that evaluates process reward models (PRMs) for tool-using agents, recasting agent trajectories as step-level cases in which a correct action must be chosen over a plausible incorrect alternative. It draws 987 such cases from four tool-use benchmarks and ranks 17 large language models, general PRMs, and tool-specialized PRMs on step-level judgement accuracy.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.12294>
- **Code:** <https://github.com/David-Li0406/ToolPRMBench>

## Summary

ToolPRMBench addresses the absence of a systematic evaluation benchmark for PRMs in tool-using settings, where existing PRM benchmarks target general reasoning or web agents rather than structured tool calls. It converts trajectories from ToolTalk, GTA, BFCL, and ToolSandbox into single-decision-step samples, each carrying the interaction history, a correct action, a plausible incorrect alternative, and the available tool metadata, then filters them through a three-judge LLM verification pipeline. On the resulting leaderboard, ToolPRM-GRPO records the highest average accuracy at 78.6%, ahead of Claude-4.5-haiku at 75.1% and GPT-5 at 74.4%, while the four general PRMs fall in the 49.2–52.8% band.

## Tasks

987 step-level samples by the appendix breakdown — BFCL 354, ToolSandbox 429, GTA 118, ToolTalk 86 — each a tuple of interaction history, a chosen correct action, a rejected incorrect action, and the associated tool metadata. Samples are produced by two complementary strategies: offline sampling, which holds the policy to a golden trajectory prefix and resamples a single step so that errors stay local, and online sampling, which lets the policy generate a full trajectory, keeps only rollouts that fail the source benchmark's outcome metric, and has an annotator LLM locate the first incorrect step. The released split is 542 train / 445 test, with GTA and ToolTalk contributing no training samples.

## Domains

Tool-using agent interaction across information-seeking, multi-step reasoning, and interactive tool execution, over the API surfaces of ToolTalk, GTA, BFCL, and ToolSandbox.

## Evaluation

- **Forced-choice step accuracy.** Each case presents the interaction history, the tool description, and the two candidate actions, and the model must name the correct one; accuracy is the share of cases answered correctly.
- **Per-subset and average accuracy.** Scores are reported separately on GTA, ToolTalk, BFCL, and ToolSandbox, with an unweighted average across the four.
- **Meta-evaluation against reward-guided search.** Benchmarked models are used as reward functions for best-of-n search with n = 8 on GTA and BFCL, and their benchmark accuracy is correlated with the resulting gain; models below 50% accuracy often yield negative gains.
- **Cost analysis.** Estimated inference cost per call is plotted against average accuracy, using official API pricing for API-based models and Together.ai pricing for open-source models.
- **Reported (Table 2).** ToolPRM-GRPO leads at 78.6% average accuracy, then Claude-4.5-haiku at 75.1%, GPT-5 at 74.4%, and Gemini-2.5-flash at 73.2%; the strongest open-source LLM is Qwen3-14B at 63.0%, the four general PRMs span 49.2–52.8%, and no human performance baseline is reported.

## Typical Duration

Each case is a single decision-step judgement rather than an agent rollout, so no per-case wall-clock, step, or token budget is given. Not reported as wall-clock; the paper reports estimated inference cost per call instead.

## Main Contribution

A large-scale benchmark for systematic evaluation of process reward models in tool-using settings, pairing step-level forced-choice cases drawn from four tool-use benchmarks with a leaderboard over 17 large language models, general PRMs, and tool-specialized PRMs.

## Key Design Ideas

- Step-level case format: interaction history, a chosen action, a rejected action, and the available tool description.
- Offline sampling along golden trajectory prefixes to isolate single-step errors, paired with online sampling over failed rollouts to capture propagated multi-step failures.
- Multi-LLM verification with GPT-5, Gemini-3-flash, and Claude-4.5-haiku, retaining unanimously accepted cases, discarding unanimously rejected ones, and routing split votes to human verification.
- Four model families scored side by side: API-based LLMs, open-source LLMs, general PRMs, and tool-specialized PRMs trained on the benchmark's own BFCL and ToolSandbox training split.

## Strengths

- Pairwise forced-choice construction isolates a step-level judgement signal that outcome-only benchmarks cannot separate from final task success.
- Splitting offline from online sampling distinguishes injected local errors from naturally propagated ones, so a PRM's failure mode stays legible rather than aggregated.
- Meta-evaluation against best-of-n search connects benchmark accuracy to downstream search utility, including the finding that judges below 50% accuracy actively harm performance.

## Limitations

- Repository note: The main text gives 984 total samples while the appendix breakdown sums to 987 across both the four subsets and the train/test columns; this card follows the appendix figure, which is the internally consistent one.
- Repository note: The three ToolPRM variants are trained on 542 samples drawn only from BFCL and ToolSandbox, so two of their four subset scores in Table 2 are in-distribution while every other benchmarked model is out-of-distribution throughout; the paper reports the in-distribution and out-of-distribution comparison separately.

## Related Works

- [AgentBoard](./agentboard.md) — Also scores agent progress below end-task success, but through subgoal annotations traversed inside the agent's own run rather than by testing whether an external reward model can pick the correct action at a single step.
- [TRACE](./trace.md) — Also evaluates trajectories rather than final answers, but scores a completed trajectory on quality dimensions rather than benchmarking the judges that score individual steps.
