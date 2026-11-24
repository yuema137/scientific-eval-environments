# TRACE for Tool-Augmented Agents (2025)

> **English** | [简体中文](../zh/works/trace-tool-augmented-agents.md)

> **First appeared:** 2025-10-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.02837)

## Overview

Tool-use benchmarks such as GTA usually score an agent by matching its final answer, so two agents with the same answer receive the same score even if one made unnecessary tool calls or reasoned from facts it never retrieved. Comparing each trajectory to a reference trajectory would catch this, but many different tool orderings can be valid, and annotating all of them is costly. TRACE (Trajectory-based Reasoning Assessment and Comprehensive Evaluation) removes the reference: an LLM judge scores efficiency, hallucination, and adaptivity against an *evidence bank* built from the agent's own tool calls. A meta-evaluation set of deliberately flawed trajectories tests whether the judge detects the inserted flaws. This work is distinct from the deep-research [TRACE](./trace.md) card.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities


N/A — Trajectory meta-evaluation framework for general tool-augmented question answering (GTA, m&m's, GAIA); no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.02837>
- **Code:** <https://github.com/wonjoong-kim/TRACE>
- **Venue:** ICML 2026

## Summary

For a ReAct-style trajectory, TRACE records each step as an evidence entry e<sub>t</sub> = (action, input, observation) and accumulates the entries into a bank E<sub>t</sub>. The judge then checks each thought against the evidence available before it (hallucination), checks each step that follows a failed tool call for a sensible alternative (adaptivity), and, after a correct answer, finds the smallest subset of evidence that supports the answer (efficiency). On synthetic meta-evaluation sets built from GTA and m&m's, TRACE raises judge accuracy over a plain LLM-as-a-judge baseline for most judges, with the largest gain for the smallest judge. The flaws in the meta-evaluation sets are inserted synthetically, so judge accuracy on naturally occurring errors is not directly measured.

## Tasks

Meta-evaluation datasets:

- **Meta-GTA:** 761 trajectories (168 correct, 171 with inefficiency, 251 with hallucination, 171 involving adaptivity), built from GTA.
- **Meta-m&m's:** 735 trajectories (374 correct, 361 inefficient), built from the human-verified filtered test split of m&m's. Hallucination and adaptivity are not labeled because m&m's trajectories contain no thoughts.

Construction: GPT-4o augments each ground-truth trajectory into multiple valid tool orderings; inefficient steps and hallucinated thoughts are inserted; adaptivity cases are created by making a tool unavailable and adding look-alike tools (FastCalculator, FastOCR, ImageDescriptor, WebSearch). Outputs were checked by Claude Sonnet 4, GPT-4o, and Gemini Pro; only items all three marked valid were kept, and manual inspection of 100 samples per model gave 98.79% agreement.

Application study: 9 agent backbones on GTA, plus a Magentic-One multi-agent run on GAIA in the appendix.

## Domains

General tool-augmented question answering with multimodal and web tools (GTA, m&m's, GAIA).

## Evaluation

- **Efficiency.** Eff(T) = |E<sub>min</sub>| / |E<sub>n</sub>|, where E<sub>n</sub> is the full evidence bank and E<sub>min</sub> the minimal subset that supports the final answer; computed only for correct answers.
- **Hallucination.** H(s<sub>t</sub>) = 1 if the thought at step t is not grounded in E<sub>t−1</sub>; the first step is judged against an empty bank, and use of internal knowledge absent from the bank also counts. H(T) = Σ H(s<sub>t</sub>) / n.
- **Adaptivity.** For each failed tool call, score 1 if the next thought acknowledges the failure and the next action is a sensible alternative, otherwise 0.
- **Trace.** In a GTA case, GPT-4.1 and Qwen-72B both answer correctly, but GPT-4.1 already holds the key fact ("Regency Cafe") and still makes an extra tool call; that call falls outside E<sub>min</sub>, so GPT-4.1 receives the lower efficiency score.
- **Meta-evaluation (accuracy, LLM-as-a-judge baseline → TRACE, Meta-GTA).** Efficiency: Claude-Sonnet-4 86.08 → 94.64, GPT-4.1 81.45 → 94.24, Llama-3.1-8B 55.67 → 70.46. Hallucination: Llama-3.3-70B 88.95 → 95.97. On multiple valid trajectories, TRACE reaches 98.68 ± 1.26 with Claude against 77.31 ± 9.96 for the PIPA baseline.
- **Application.** Overall accuracy on GTA ranges from 0.5767 (Claude-Sonnet-4) to 0.0154 (Mistral-7B); Qwen-7B (0.3904) exceeds Llama-3.3-70B (0.3738). Adaptivity separates agents with similar accuracy: GPT-4.1 scores 0.8056 and o3-mini 0.6250, against 0.8750 for Claude-Sonnet-4.

## Typical Duration

The paper reports that Llama-3.3-70B as judge matches larger proprietary judges on accuracy while running up to about 3× faster; absolute times and costs are not reported. TODO(reference)

## Main Contribution

A reference-free framework that scores tool-augmented agent trajectories on efficiency, hallucination, and adaptivity using an evidence bank, together with meta-evaluation datasets of flawed trajectories showing that the framework evaluates trajectories accurately even with small open-source judges.

## Key Design Ideas

- Replace a reference trajectory with the agent's own accumulated evidence, so any valid tool ordering can be judged without enumerating it.
- Store evidence as structured (action, input, observation) records rather than passing the raw dialogue to the judge.
- Score adaptivity only at tool-failure events, so it measures recovery rather than general behavior.
- Validate the judge on trajectories with known inserted flaws before applying it to agents.

## Strengths

- TRACE improves judge accuracy over the plain baseline for every judge on Meta-GTA efficiency, and the largest gains occur for the smallest judge (Llama-3.1-8B).
- The meta-evaluation includes multiple valid orderings of the same solution, testing that correct but non-reference trajectories are not penalized.
- Code is released.

## Limitations

- Efficiency flags unnecessary tools among those used; it does not identify the optimal tool path, which the authors describe as intractable without ground truth.
- Repository note: Meta-evaluation flaws are inserted synthetically, and adaptivity is tested with synthetic tool unavailability; accuracy on naturally occurring errors is not separately measured.
- Repository note: Claude-Sonnet-4 and GPT-4.1 serve both as evaluated agents and as judges in the application study.
- Repository note: Counting any use of internal knowledge as hallucination makes the hallucination score strict for steps that rely on correct background knowledge.

## Related Works

- [TRACE](./trace.md) — Different work with the same acronym; scores deep-research trajectories with a hierarchical utility function.
- [AgentProcessBench](./agentprocessbench.md) — Also evaluates tool-use trajectories below the final answer, with human step labels rather than evidence-bank judging.
- [T-Eval](./t-eval.md) — Also scores tool use below the final answer, but along fixed capability subprocesses.
- [ToolPRMBench](./toolprmbench.md) — Also evaluates step-level judges of tool-using agents, as process reward models choosing between correct and incorrect actions.
