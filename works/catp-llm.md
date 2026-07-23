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

OpenCATP comprises 111 compositional tasks — 87 sequential (reused from OpenAGI; 69 train / 18 test) and 24 non-sequential (12 train / 12 test) — each paired with 100 input data samples, giving the 11,100 evaluation samples (experiments randomly sample 40 inputs per task). The tools to be scheduled are external expert models (vision and NLP).

## Domains

Compositional vision + NLP tool use, built on OpenAGI's toolkit — e.g., object detection, image super-resolution, colorization, deblurring, denoising, classification, and machine translation, with image and/or text outputs.

## Evaluation

- **Quality of Plan (QoP)** — the headline metric: QoP = α · P_task(p) − (1 − α) · C_price(p), with min–max normalization so performance and cost share a scale and α = 0.5 by default (equal weight on performance and cost).
- **Plan performance P_task** — ViT Score (cosine similarity between the plan's generated image and the ground-truth image) for image-output tasks, BERT Score (cosine similarity of texts) for text-output tasks; multi-output tasks average the per-output scores.
- **Plan cost C_price** — a normalized monetary price (USD) from an AWS-Lambda-inspired model in which tool execution time and constant/instant CPU–GPU memory are priced; a plan's price sums its per-tool prices, and parallel branches take the max of per-branch execution times. Execution time is an input to the price, not the metric itself.
- **Reported:** with a Llama2-7B backbone, CATP-LLM beats GPT-4, improving plan quality by 1.5–93.9% overall; on sequential planning it gains 16.5–34.6% QoP over GPT-3.5/GPT-4, and on non-sequential planning 28.4–30.2% higher performance, 24.7–45.8% lower execution price, 67.0–78.3% lower execution time, and 129.4–683.0% higher QoP.

## Typical Duration

Not stated: OpenCATP defines a cost metric (an execution-time-based price) but imposes no per-task time, token, or cost budget limit.

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
- Repository note: OpenCATP's tasks are compositional vision/NLP pipelines built on OpenAGI's toolkit; transfer of the cost model and QoP metric to other tool ecosystems is not evaluated.

## Related Works

- [CostBench](./costbench.md) — Also makes tool-use cost a first-class quantity, but as a benchmark centered on dynamic replanning rather than a dataset paired with a planning method.
- [SimulCost](./simulcost.md) — Also cost-aware, extending tool-use cost to physics-simulation time and experimental resources.
