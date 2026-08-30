# PlanBench (2023)

> **English** | [简体中文](../zh/works/planbench.md)

> **First appeared:** 2022-06-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2206.10498)

## Overview

PlanBench is an extensible benchmark for testing whether large language models can generate and verify plans, reason about state changes, replan after unexpected events, and distinguish valid from invalid action sequences in formal planning domains.

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — general planning and reasoning benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2206.10498>
- **Code:** <https://github.com/karthikv792/LLMs-Planning>
- **Venue:** NeurIPS 2023 Datasets and Benchmarks Track

## Summary

PlanBench translates classical planning problems into natural language while retaining explicit action models, initial states, goals, and machine-checkable semantics. It was designed to separate planning from retrieval of familiar commonsense patterns: the released suite begins with Blocksworld and Logistics, includes misleading and random-symbol obfuscations, and uses planners and plan validators to generate reference information and check model outputs. The paper reports that GPT-4 solves 34.3% of the 600 Blocksworld plan-generation instances and 33.0% of the corresponding cost-optimal planning instances.

## Tasks

Approximately 26,250 prompts across eight test cases and original or obfuscated planning domains. The eight cases cover plan generation, cost-optimal planning, plan verification, reasoning about the state produced by an action sequence, replanning after an unexpected state change, plan generalization, plan reuse, and reasoning about partially specified goals. The initial release contains 600 main Blocksworld instances, a separate 500-instance Blocksworld generalization set, and 285 Logistics instances; prompts and transformations expand these source problems across test cases and domain variants.

## Domains

Formal classical planning in the Blocksworld and Logistics domains. These are controlled AI planning environments rather than scientific or engineering application domains, so the work has no canonical domain-page assignment.

## Evaluation

Generated action sequences are parsed back into formal plans and checked by a domain-independent plan validator for executability and goal satisfaction. Cost-optimal planning additionally compares the generated plan cost with the optimal cost. Auxiliary tasks are scored against formal state-transition or validity checks. The reported Blocksworld evaluation compares GPT-4 and InstructGPT across the test cases, with results reported as the number and percentage of correct instances.

## Typical Duration

Single-response, few-shot planning prompts. Problem difficulty varies through the number of objects and optimal plan length; no wall-clock or token budget is defined.

## Main Contribution

An extensible, automatically verifiable evaluation framework that imports formal planning domains into natural-language LLM evaluation and uses obfuscation to probe whether apparent planning performance depends on familiar names and world knowledge.

## Key Design Ideas

- Separate domain-independent generation and verification machinery from domain-specific models, generators, and natural-language translators.
- Include explicit action preconditions and effects so answers can be checked against formal transition semantics.
- Evaluate planning and related reasoning capabilities separately rather than reporting one aggregate task-success number.
- Obfuscate predicate and action names with misleading words or random strings while leaving the underlying planning problem unchanged.

## Strengths

- Deterministic plan validation makes correctness independent of an LLM judge.
- Formal domains support controlled changes to problem size, plan length, action cost, and unexpected events.
- Obfuscated variants directly test sensitivity to lexical familiarity.

## Limitations

- The initial benchmark is concentrated in two classical planning domains and does not include perception, live tools, or uncertain environment dynamics.
- Exact validity and optimality are well defined in these formal environments but do not capture the ambiguity and competing objectives of real-world planning.
- The reported experiments focus primarily on Blocksworld rather than evaluating every released domain and test-case combination equally.

## Related Works

- [NATURAL PLAN](./natural-plan.md) — removes tool execution while replacing formal action languages with realistic natural-language constraints.
- [TravelPlanner](./travelplanner.md) — evaluates executable travel plans under tool retrieval and heterogeneous real-world constraints.
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — extends planning diagnosis to multimodal agent tasks, feedback-conditioned next steps, broken tools, distractors, and infeasible goals.
