# AgentProcessBench (2026)

> **English** | [简体中文](../zh/works/agentprocessbench.md)

## Overview

AgentProcessBench is a benchmark for evaluating the step-level effectiveness of a tool-using agent's intermediate actions in realistic, multi-turn trajectories. It comprises 1,000 trajectories sampled from five policy models across four tool-use benchmarks, with 8,509 human-labeled step annotations under a ternary +1 / 0 / −1 scheme at 89.1% inter-annotator agreement.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2603.14465>
- **Project:** <https://huggingface.co/datasets/LulaCola/AgentProcessBench>
- **Code:** <https://github.com/RUCBM/AgentProcessBench>

## Summary

AgentProcessBench argues that existing process-level benchmarks are confined to closed-world mathematical reasoning and fail to capture the dynamic, open-ended nature of tool execution, where failures frequently cause irreversible side effects. To close this gap, the authors build what they describe as the first benchmark dedicated to step-level effectiveness evaluation in tool-augmented trajectories, pairing a ternary labeling scheme that captures exploration with an error-propagation rule that reduces labeling ambiguity. The resulting benchmark holds 1,000 trajectories and 8,509 human-labeled steps at 89.1% inter-annotator agreement (Cohen's κ 0.767), and is used to evaluate 20 LLMs as step-level verifiers.

## Tasks

1,000 tool-use agent trajectories over 200 unique tasks, evenly drawn from four established benchmarks — HotpotQA (multi-hop reasoning), GAIA (deep research), BFCL (multi-turn function calling), and τ²-Bench (dual-control conversational tool use). For every task, trajectories are rolled out by five policy models (Qwen3-4B-Instruct-2507, Qwen3-30B-A3B-Instruct-2507, DeepSeek-V3.2, GPT-5-mini, GPT-5) and all five are kept for cross-model comparison, with tasks chosen by maximizing pairwise E5-embedding distance for diversity.

## Domains

Open-world tool use across web (search / browsing), command-line file access, and function-calling APIs, spanning multi-hop QA, deep-research information seeking, and conversational customer-service tasks.

## Evaluation

- **Ternary step labels.** Each assistant step is labeled +1 (correct and effective), 0 (neutral or exploratory), or −1 (incorrect or harmful) with respect to overall task progress.
- **Error-propagation rule.** Once a step is erroneous, every later step that causally depends on it is labeled −1 until the agent explicitly corrects the error or transitions to an independent subtask.
- **Step Accuracy (StepAcc).** Micro-averaged agreement between predicted and human step labels, pooled over all assistant steps so that longer trajectories contribute proportionally more.
- **First-Error Accuracy (FirstErrAcc).** Fraction of trajectories whose first −1 step matches the human-annotated first error, with trajectories that neither side marks erroneous counted as correct.
- **Reported.** Across 20 evaluated LLMs, average StepAcc ranges from 35.3% (LLaMA-3.2-3B-Instruct) to 81.6% (Gemini-3-Flash-Preview-Thinking), the strongest open-source model (Qwen3-30B-A3B-Thinking-2507) reaches 68.5%, and StepAcc tracks FirstErrAcc at Pearson r = 0.90.

## Typical Duration

The benchmark scores pre-collected trajectories, so it fixes no per-task step, wall-clock, or token budget of its own. Trajectory length varies by subset: mean assistant steps per trajectory run from 2.7 (successful HotpotQA) to 15.8 (unsuccessful τ²-Bench), and 28.2% of unsuccessful τ²-Bench trajectories exceed 16 steps.

## Main Contribution

The first human-annotated benchmark for step-level effectiveness evaluation in tool-using agent trajectories, coupling a ternary +1 / 0 / −1 labeling protocol with an error-propagation rule over 1,000 trajectories and 8,509 annotated steps.

## Key Design Ideas

- Ternary step labeling: +1 correct and effective, 0 neutral or exploratory, −1 incorrect or harmful, crediting necessary exploration rather than penalizing it.
- An error-propagation rule that labels every step causally downstream of a mistake as −1 until the agent explicitly corrects it or moves to an independent subtask.
- Cross-model trajectory sampling: five policy models of differing scale and family are rolled out on every task, exposing policy-dependent failure and early-termination behavior.
- Two complementary verifier metrics: StepAcc for global step-labeling reliability and FirstErrAcc for earliest-error localization.

## Strengths

- High-reliability ground truth: every trajectory is independently dual-annotated by trained experts at 89.1% inter-annotator agreement (Cohen's κ 0.767), and the released labels are shown to be largely uninfluenced by the LLM references shown to annotators.
- First process-level benchmark to move step verification out of closed-world mathematics into open-world, multi-turn tool use over web, CLI, and API environments.
- A neutral label and an explicit error-propagation rule that together cut annotation ambiguity while separating benign exploration from genuinely harmful actions.

## Limitations

- Repository note: The benchmark scores static, pre-collected trajectories, so it measures a model's ability to judge steps as a verifier rather than to generate better ones, and it does not exercise an agent in a live environment.
- Repository note: Annotators labeled with predictions from three reference LLMs in view, which the authors flag as possible anchoring bias; a reference-free control re-annotation agrees with the released labels at 84.06%, but the reference-conditioned labels remain the ground truth.

## Related Works

- [AgentBoard](./agentboard.md) — Also decomposes agent evaluation below end-task success, but tracks automatic subgoal progress rather than human-labeled step-effectiveness signals.
- [T-Eval](./t-eval.md) — Also scores tool use below the final answer, but along fixed capability subprocesses in short instances rather than free-form step effectiveness across full trajectories.
- [TRACE](./trace.md) — Also evaluates trajectories below the outcome, but aggregates a multi-dimensional cognitive-quality rubric over deep-research runs rather than assigning ternary effectiveness labels to individual tool-use steps.