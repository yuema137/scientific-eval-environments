# AnalogXpert (2024)

> **English** | [简体中文](../zh/works/analogxpert.md)

## Overview

AnalogXpert is an LLM agent for automating analog topology synthesis by incorporating circuit-design expertise: it represents topologies as SPICE code, decomposes design into block selection and block connection via chain-of-thought and in-context learning, and is evaluated on a benchmark of 30 real and 2,000 synthetic cases, reaching 40% / 23% success versus GPT-4o's 3%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.19824>
- **Venue:** arXiv preprint (cs.AR), 2024

## Summary

AnalogXpert encodes an analog designer's workflow into an LLM agent: analog topology is represented as SPICE code, a subcircuit library narrows the design space, and the task is decomposed into two sub-tasks — block selection and block connection — handled with chain-of-thought and in-context learning, followed by a proofreading strategy for incremental error correction. On a purpose-built benchmark of 30 real and 2,000 synthetic design cases, it reaches 40% success on synthetic and 23% on real designs, far above GPT-4o's 3% on both.

## Tasks

Analog topology synthesis over 30 real + 2,000 synthetic cases; the agent selects blocks and connects them (as SPICE code) with iterative proofreading — agentic, not static QA.

## Domains

Electrical Engineering — analog and mixed-signal design: circuit topology synthesis.

## Evaluation

- One-trial correctness: synthetic cases checked by automated structural-rule programs; real cases verified by human reviewers matching all blocks and connections to the requirements.
- **Reported.** 40% (synthetic) and 23% (real) success for AnalogXpert vs. 3% for GPT-4o on both.

## Typical Duration

Multi-step block-selection-and-connection episodes with proofreading, per design.

## Main Contribution

Encoding analog-design expertise — subcircuit libraries and a select-then-connect decomposition — into an LLM agent, with a benchmark large enough (2,000+ cases) to measure topology synthesis reliably.

## Key Design Ideas

- Representing topology as SPICE code gives the LLM an executable target.
- Decomposing into block selection and connection matches how analog designers work.
- The proofreading step corrects structural errors incrementally rather than in one shot.

## Strengths

- Large synthetic set plus real designs makes topology success measurable, not anecdotal.
- The 40%/23%-vs-3% gap shows expertise encoding, not raw scale, drives the gain.

## Limitations

- Repository note: card compiled from the arXiv abstract and full text (August 2026); no venue is stated in arXiv metadata, and no official code/dataset repository is verifiable from the arXiv page.

## Related Works

- [AnalogCoder](./analogcoder.md) — Also an LLM agent for analog design, via training-free Python code generation.
- [MMCircuitEval](./mmcircuiteval.md) — Also analog-inclusive circuit evaluation, as multimodal QA.
- [EEE-Bench](./eee-bench.md) — Also EE design evaluation including analog, as multimodal problem solving.
