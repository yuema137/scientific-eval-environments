# CATP-LLM / OpenCATP (2024)

## Overview

CATP-LLM (Cost-Aware Tool Planning with LLMs) is a framework for empowering LLMs to plan tool use while accounting for tool execution costs, accompanied by OpenCATP, described as the first dataset for cost-aware planning (11,100 evaluation samples). It is documented here for OpenCATP, its cost-aware *evaluation* contribution; the paper's headline contribution — the CATP-LLM planning method — is agent-planning work adjacent to this repository's evaluation focus (see the repository note under Limitations).

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.16313>
- **Venue:** ICCV 2025

## Summary

CATP-LLM argues that prior LLM tool-planning work overlooks tool execution costs (e.g., execution time), producing expensive plans whose costs outweigh their task-performance benefits. It proposes a coherent design for cost-aware tool planning: a tool planning language that lets the LLM create multi-branch, non-sequential plans for efficient concurrent tool execution, and a cost-aware offline reinforcement-learning algorithm that fine-tunes the LLM to optimize the performance–cost trade-off. To support evaluation in the absence of public cost-related datasets, it introduces OpenCATP, the first dataset for cost-aware planning, comprising 11,100 evaluation samples from diverse tasks.

## Tasks

OpenCATP comprises 11,100 evaluation samples from diverse tasks, where tools to be scheduled include external models such as vision models. Task taxonomy and per-category counts: TODO(reference) — not stated in the abstract.

## Domains

LLM tool planning with external tools (e.g., vision models). Specific task domains covered by OpenCATP: TODO(reference).

## Evaluation

- Measures the performance–cost trade-off of tool plans, with tool execution cost (e.g., execution time) treated as a first-class quantity rather than ignored.
- Exact metric definitions and verifier type: TODO(reference) — not detailed in the abstract.

## Typical Duration

TODO(reference): abstract does not state per-task duration or token budget.

## Main Contribution

The paper's stated contribution is CATP-LLM, described as the first coherent framework empowering LLMs for cost-aware tool planning, together with OpenCATP, described as the first dataset for cost-aware planning. Within this repository, the in-scope contribution is OpenCATP as a resource-aware evaluation dataset.

## Key Design Ideas

- Tool execution cost (e.g., execution time) is a planning consideration, not a post-hoc statistic.
- A tool planning language enables multi-branch, non-sequential plans for concurrent tool execution and cost reduction.
- A cost-aware offline RL algorithm fine-tunes the LLM to optimize the performance–cost trade-off.
- OpenCATP supplies a dedicated dataset (11,100 samples) for evaluating cost-aware planning where none previously existed publicly.

## Strengths

- Introduces a public dataset (OpenCATP) targeting cost-aware planning, a dimension prior tool-use datasets omit.
- Treats performance and cost jointly rather than optimizing task success alone.
- Non-sequential planning formulation aligns evaluation with concurrent, cost-reducing tool execution.

## Limitations

- Repository note: The paper's primary contribution is a tool-planning *method* (a tool planning language plus a cost-aware offline RL fine-tuning algorithm) — agent-planning / training work that sits outside this repository's evaluation-centric scope. It is included for OpenCATP, its cost-aware evaluation dataset; the method itself is not the reason for inclusion.
- Repository note: Task taxonomy, metric definitions, and verifier type for OpenCATP are not stated in the abstract and are marked `TODO(reference)` above pending verification from the paper or released dataset.

## Related Works

- [CostBench](./costbench.md) — Also makes tool-use cost a first-class quantity, but as a benchmark centered on dynamic replanning rather than a dataset paired with a planning method.
- [SimulCost](./simulcost.md) — Also cost-aware, extending tool-use cost to physics-simulation time and experimental resources.
