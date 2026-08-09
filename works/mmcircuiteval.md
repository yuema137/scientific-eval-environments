# MMCircuitEval (2025)

> **English** | [简体中文](../zh/works/mmcircuiteval.md)

## Overview

MMCircuitEval is the first multimodal circuit-focused benchmark for evaluating LLMs: 3,614 curated question–answer pairs spanning digital and analog circuits across critical EDA stages — from general knowledge and specifications to front-end and back-end design — drawn from textbooks, question banks, datasheets, and real-world documentation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.19525>
- **Code:** <https://github.com/cure-lab/MMCircuitEval>
- **Venue:** ICCAD 2025

## Summary

MMCircuitEval organizes circuit evaluation along the design flow: its 3,614 QA pairs span digital and analog circuits across EDA stages from general knowledge and specifications to front-end and back-end design, sourced from textbooks, technical question banks, datasheets, and real-world documentation. Questions carry image inputs and come in multiple-choice, fill-in-the-blank, and open-ended formats, categorized by design stage, circuit type, tested ability (knowledge, comprehension, reasoning, computation), and difficulty. The evaluation surfaces significant performance gaps among current models, particularly in back-end design and complex computations.

## Tasks

3,614 multimodal QA pairs across digital and analog circuits and EDA stages; static multimodal QA in multiple-choice, fill-in-the-blank, and open-ended formats.

## Domains

Electrical Engineering — digital and analog circuit knowledge and design across EDA stages, with multimodal (image + text) inputs.

## Evaluation

- Accuracy categorized by design stage, circuit type, tested ability (knowledge/comprehension/reasoning/computation), and difficulty.
- **Reported.** Significant performance gaps among existing LLMs, particularly in back-end design and complex computations.

## Typical Duration

Single-turn multimodal questions; no interactive setting.

## Main Contribution

The first multimodal circuit benchmark structured along the EDA design flow — locating where model competence drops (back-end design, complex computation) rather than reporting one aggregate score.

## Key Design Ideas

- Organizing by EDA stage maps competence onto the real design pipeline.
- The ability taxonomy (knowledge/comprehension/reasoning/computation) separates failure types.
- Mixed question formats and difficulty levels give a graded, diagnostic picture.

## Strengths

- Venue-verified (ICCAD 2025) with a public release, spanning digital and analog.
- Stage- and ability-level breakdowns make the results actionable for circuit-LLM builders.

## Limitations

- Repository note: card compiled from the arXiv abstract, Comments, and official repository (August 2026); the number of evaluated models is not stated in the abstract.

## Related Works

- [EEE-Bench](./eee-bench.md) — Also multimodal EE evaluation, spanning 10 subdomains rather than EDA stages.
- [AnalogCoder](./analogcoder.md) — Also analog-circuit-focused, as an agentic design task rather than QA.
- [CVDP](./cvdp.md) — Also circuit-design evaluation across the flow, on RTL rather than multimodal QA.
