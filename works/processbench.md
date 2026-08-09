# ProcessBench (2024)

> **English** | [简体中文](../zh/works/processbench.md)

## Overview

ProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, where a judge must return the index of the earliest erroneous step in a step-by-step solution or conclude that all steps are correct. It consists of 3,400 test cases drawn from four math datasets and focused primarily on competition- and Olympiad-level problems, each pairing a problem with a model-generated solution whose error location was annotated by human experts.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2412.06559>
- **Code:** <https://github.com/QwenLM/ProcessBench>
- **Venue:** ACL 2025

## Summary

ProcessBench addresses the limitation that existing benchmarks for reasoning-process assessment either cover problems that have become too easy for recent language models, or label only the correctness of final answers without annotating specific erroneous steps. The benchmark pairs competition- and Olympiad-level math problems with model-generated step-by-step solutions whose earliest error location is annotated by human experts, and evaluates two families of judge on them: process reward models (PRMs) and general language models prompted as critic models. Averaged over the four subsets, o1-mini reaches 87.9 F1, the best open-source model, QwQ-32B-Preview, reaches 71.5, and the best existing open-source PRM reaches 42.1.

## Tasks

3,400 test cases across four subsets — 400 from GSM8K and 1,000 each from MATH, OlympiadBench, and Omni-MATH — each pairing a math problem with one model-generated step-by-step solution. Solutions come from twelve open-source generators in the Qwen and LLaMA series and are reformatted by Qwen2.5-72B-Instruct into uniform paragraph-level steps before annotation. Sampling was balanced between correct and incorrect final answers — 200 each for GSM8K and 500 each for the other three subsets — but expert annotation found process errors in 3.5% of the answer-correct GSM8K solutions, 18.8% on MATH, 32.2% on OlympiadBench, and 51.8% on Omni-MATH.

## Domains

Mathematical reasoning, from grade-school problems in GSM8K to competition- and Olympiad-level problems in MATH, OlympiadBench, and Omni-MATH.

## Evaluation

- **Earliest-error index.** Given a problem and a solution of n steps, the judge outputs an index i ∈ {−1, 0, …, n−1}, where −1 asserts that every step is correct and a non-negative value locates the earliest erroneous step.
- **F1 score.** Accuracy is computed separately over erroneous and over correct samples in each subset, and the two are combined as their harmonic mean, which balances being overly critical against being unable to identify errors.
- **Two judge families.** Process reward models are scored by extracting the earliest step their per-step correctness predictions mark as wrong, with scalar-output PRMs thresholded first; general language models are prompted to critique the solution step by step and return the index as a boxed final answer.
- **Reported (Table 3, average over the four subsets).** o1-mini 87.9, QwQ-32B-Preview 71.5, GPT-4o-0806 61.9, the authors' fine-tuned Qwen2.5-Math-7B-PRM800K 56.5, and Skywork-PRM-7B 42.1 as the strongest existing open-source PRM. Open-source models are evaluated under majority voting over eight samplings, GPT-4o-0806 under greedy decoding, and o1-mini under single sampling.

## Typical Duration

Single-pass scoring of one static solution rather than an interactive rollout; solutions run to 5.1–8.9 steps on average depending on subset and label. Not stated: no wall-clock, step, or token budget is given for the judge, though the protocol fixes majority voting over eight samplings for open-source models.

## Main Contribution

A 3,400-case benchmark for identifying the earliest erroneous step in mathematical reasoning, built from competition- and Olympiad-level problems with model-generated solutions and expert step-level error annotation, and applied to both process reward models and prompted critic models.

## Key Design Ideas

- Earliest-error-index output format, a single-integer protocol under which both process reward models and prompted critic models can be scored.
- Problem difficulty raised beyond GSM8K and MATH to competition- and Olympiad-level sources, with twelve distinct solution generators for solution diversity.
- Solution reformatting by Qwen2.5-72B-Instruct to unify step granularity before annotation, discarding solutions whose final answer changes under reformatting.
- Three-annotator agreement requirement, escalating to five annotators when consensus fails and discarding the sample otherwise, at an overall ~30% discard rate.

## Strengths

- Expert annotation over naturally generated solutions gives error locations that do not depend on a synthetic error-injection procedure.
- A single-integer output format lets process reward models and prompted general language models be compared on one scale.
- Balanced sampling of answer-correct and answer-incorrect solutions makes the rate at which correct final answers rest on flawed steps directly measurable, separating process quality from outcome correctness.

## Limitations

- Repository note: The paper states that error-location labels may remain inaccurate on the harder Olympiad-level problems, and that the ~30% of solutions discarded when annotators could not agree may bias the problem distribution toward cases experts could resolve.
- Repository note: The judged unit is a static, pre-generated text solution rather than an agent trajectory, so the earliest-error index localizes a reasoning error inside one solution and carries no notion of tool calls, environment state, or actions across turns.

## Related Works

- [AgentBoard](./agentboard.md) — Also scores below end-task success, but tracks progress along annotated subgoals across multi-turn environment interaction rather than locating the single earliest erroneous step in a static solution.
- [TRACE](./trace.md) — Also evaluates the reasoning process rather than the final answer alone, but scores whole trajectories on continuous quality dimensions rather than reducing the verdict to a single expert-annotated error index.
