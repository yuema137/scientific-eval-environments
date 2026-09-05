# InnovatorBench (2025)

> **English** | [简体中文](../zh/works/innovatorbench.md)

> **First appeared:** 2025-10-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.27598)

## Overview

InnovatorBench changes the target of an AI-research benchmark from *reproduce this result* to *beat it*. Reproduction suites hand an agent a paper and score how closely it recovers the published number, which rewards fidelity and says nothing about whether the agent can invent a better method. InnovatorBench strips the key novelty and the commit history out of a published paper's own codebase, gives the agent the leftover repository, the data, and a task description with no step-by-step instructions, and calibrates the score so that reapplying the original method lands near 80 — the agent has to design something of its own to go higher. The companion environment, ResearchGym, exists because that target needs runs that last hours across several GPU machines, so the agent must launch background jobs, poll them, and manage a time budget rather than issue one blocking command at a time.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.27598>
- **Code:** <https://github.com/GAIR-NLP/InnovatorBench>
- **Dataset:** <https://huggingface.co/datasets/GAIR/InnovatorBench>
- **Venue:** ICLR 2026

## Summary

From Shanghai Jiao Tong University, the Shanghai Innovation Institute, and GAIR, InnovatorBench is a benchmark–platform pair: 20 LLM-research tasks derived from 14 influential papers, and ResearchGym, the environment the tasks run in. Each task supplies a starter workspace — a pre-built conda environment, the datasets and checkpoints, and the original paper's repository (most often LlamaFactory or Verl) with both the implementation of its key novelty and its git commit history removed, but still runnable — plus a task description that states the objective without prescribing a procedure. The agent submits an artifact through an `eval` action; an external scoring server checks the submission format, returns 0 with an error message when it fails, and otherwise applies a task-specific function calibrated so that a baseline sits near 0 and the annotators' reference reimplementation near 80. Because scoring runs outside the workspace, an agent cannot reach the reference data or edit the scorer. Across five frontier models driving a lightweight ReAct agent, Claude Sonnet 4 leads with a weighted average final score of 24.01, and no model comes close to the reference.

## Tasks

**20 tasks drawn from 14 influential papers** published at NeurIPS, ICLR, COLM, EMNLP, and ACL, spanning six LLM-research areas: Data Construction, Data Filtering, Data Augmentation, Loss Design, Reward Design, and Scaffold Construction. Concrete examples include building a medical English–Tamil parallel corpus and fine-tuning Llama-3.1-8B-Instruct for translation; implementing a GRPO variant in Verl that avoids entropy collapse during RL while maximizing accuracy on mathematical reasoning; designing a reward function in Verl to train Qwen2.5-3B for search-augmented reasoning; and building a prompt-based deep-research agent on GPT-4.1 with web tools.

Each task entry contains seven parts — motivation, task, data, constraints, evaluations, environment, and scripts — plus a starter workspace, evaluation scripts, and a hidden reference solution derived from the original research artifacts. Constraints are operational: a working time limit, a GPU quota, and an output file format. A hint exists for every task but is not placed in the workspace: the agent would have to request it through a `view_hint` tool and pay a deduction from its final score. The main evaluation disables that tool, and the ablation study instead supplies the hint immediately after the task description.

Tasks were built on four principles: the task can be reapplied and its result aligns with the original paper; the result can be improved significantly within two days; the set of tasks exercises different agent abilities; and tasks use common models such as Llama-3.1, Qwen2.5, and Qwen2.5-VL. Each task takes 2–36 hours to complete.

Repository note: the paper's Figure 6 and Table 4 disagree on how the 20 tasks divide between Data Construction and Data Filtering (Figure 6 shows 3 and 4; the itemized Table 4 lists 4 and 3). The other four areas agree at Data Augmentation 5, Loss Design 3, Scaffold Construction 3, and Reward Design 2.

## Domains

AI & Machine Learning Research — LLM research itself: training-data construction, filtering, and augmentation; loss-function design for supervised and RL fine-tuning; reward design for reinforcement learning with verifiable rewards; and agent scaffold construction. Several tasks are multimodal, including augmenting scientific image–text data for Qwen2.5-VL-7B-Instruct and building visual reasoning workflows on GPT-4o.

## Evaluation

- **Kaggle-style submission with a calibrated score.** The agent may call `eval` up to four times; the system finishes the task automatically once the limit is reached. Each submission is first checked for format validity — a failure returns 0 and an error message — and a valid submission is then scored by linear interpolation between a baseline anchored near 0 and the reference solution anchored near 80. Both the final score (last submission) and the best score are reported.
- **One item, end to end.** In the GRPO loss-design task, the agent must implement a Verl loss variant that keeps entropy from collapsing during RL while raising mathematical-reasoning accuracy. The evaluation script reads the agent's output, computes an accuracy score and an entropy score, and returns `accuracy × entropy × 100`; the whole evaluation runs outside the writable workspace against hidden reference data, so a formatting trick or a rewritten scorer cannot lift the number.
- **Reported.** With a ReAct-style agent, Claude Sonnet 4 reaches a weighted average final score of 24.01 and best score of 24.54, leading on four of six areas; GPT-5 scores 12.04 / 12.52, GLM-4.5 11.85 / 13.35, Kimi-K2 5.35 / 5.45, and Qwen3-32b 0.00 / 0.00 because its context window is too small. GPT-5 is the exception on Scaffold Construction, scoring 60.07. All models score higher on data-related areas than on algorithm-related ones, which the authors attribute to data tasks tolerating minor noise while an imperfect loss or reward can cause gradient explosion or systematically flawed policies.
- **Hint ablation.** Supplying the ground-truth hint raises Loss Design (12.98 → 22.65 final) and Reward Design (11.56 → 15.06) but lowers Data Construction, Filtering, and Augmentation, so the weighted average falls from 24.01 to 13.88. The authors read this as coding proficiency, not idea supply, being the binding constraint on the data tasks.
- **Failure case study.** Four failure modes are documented with trace excerpts: impatience (killing a training job with 21 hours of budget left), resource mismanagement (launching a full-GPU training script while an inference job still holds the GPUs, hitting CUDA OOM), selection of a suboptimal library (staying on Transformers instead of vLLM because the time-budget constraint provides no learnable efficiency signal), and template-based reasoning (batch-concatenating a vacuous chain-of-thought pattern onto every item after failing to synthesize real rationales).

## Typical Duration

2–36 hours of agent working time per task, with per-task working-time limits and GPU quotas stated in the task constraints. Test-time scaling curves show agents reaching their best InnovatorBench score after more than 11 hours, against roughly 1.75 hours on PaperBench — about 6.5× longer to saturation. Per-task monetary cost and execution time are reported: Claude Sonnet 4 averages 5.13 hours and $32.92 per task without hints, and 4.87 hours and $30.86 with them.

## Main Contribution

A benchmark whose objective is to surpass, not reproduce, a published reference solution, paired with ResearchGym — a research environment that supports the long-duration, multi-machine, asynchronous execution such tasks require, and that the authors present as reusable beyond this benchmark.

## Key Design Ideas

- The reference solution is anchored near 80 rather than at the top of the scale, so the scoring function has room above the original paper and the agent is asked for innovation rather than replication.
- The starter repository keeps the original project runnable but removes both the implementation of the paper's key novelty and the git commit history, so the agent inherits infrastructure without inheriting the answer or a trail leading back to it.
- Evaluation runs entirely outside the agent's writable workspace, with reference data hidden, which closes the usual routes of editing the scorer or matching the expected output format.
- ResearchGym exposes 42 primitive actions in five families — Command, File, Parse, Web Search, and Web Browse — and decouples action execution from action selection: a command bound to a session keeps running while the agent plans, and its output is retrieved later through `get_session_output`. A dedicated `sleep` action exists so that the agent does not fill the wait with nonsensical actions while a training job runs.
- The agent can drive several machines or Docker containers concurrently over HTTP, each running an HTTP server that receives and executes terminal commands, which is what makes distributed training tasks expressible.
- Snapshots record the task specification, the agent's context, the final workspace state, and the remaining time budget; the system can restore from any snapshot, and snapshots branch, so an experiment can resume from different points.
- Web search and browsing are enabled only for Data Construction and Data Augmentation; the paper states they are disabled for the other tasks without giving a reason.

## Strengths

- Scoring is fully deterministic: task-specific metrics such as accuracy, F1, BLEU, and entropy computed by external scripts, with no LLM judge in the loop.
- The hint ablation is a controlled experiment rather than a commentary — it separates "the agent does not know what to do" from "the agent cannot implement what it knows", and the two answers differ by task area.
- Wall-clock and dollar cost are reported per model and per research area alongside the scores, and the test-time-scaling comparison against PaperBench quantifies the horizon difference rather than asserting it.
- The environment is released separately from the benchmark and documented as extensible, so new tasks and evaluation protocols can be contributed against the same substrate.

## Limitations

- 20 tasks over six areas is small, and per-area counts run from 2 to 5, so an area-level score rests on a handful of tasks.
- No measured human baseline. The anchor is the annotators' reimplementation of the original paper, not a timed expert attempt.
- The source papers are published, and the paper states no contamination-control mechanism beyond removing the key implementation and the commit history from the starter repository and hiding the reference solution.
- All reported results come from one lightweight ReAct-style agent, so model and harness effects are not separated.
- Repository note: the calibration that anchors the reference near 80 is task-specific and the paper does not publish the per-task interpolation constants, so scores are comparable across models on this suite but not directly interpretable as a fraction of the reference's performance.

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — Also scores novel-method proposals objectively, against the gap between a baseline and top human competitors.
- [MLGym](./mlgym.md) — Also a Gym-style environment paired with an open-ended AI-research benchmark, but with shorter tasks and no distributed execution.
- [PaperBench](./paperbench.md) — The reproduction-oriented benchmark against which InnovatorBench measures its test-time-scaling horizon.
- [AI4AI-Bench](./ai4ai-bench.md) — Also asks agents to redesign learning algorithms inside frozen research repositories under an explicit compute budget.
