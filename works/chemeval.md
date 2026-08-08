# ChemEval (2024)

> **English** | [简体中文](../zh/works/chemeval.md)

## Overview

ChemEval is a multi-level chemical evaluation for LLMs built around what chemical research professionals actually need: 4 progressive levels in chemistry, assessing 12 dimensions across 42 distinct tasks drawn from open-source data and expert-crafted material.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.13989>
- **Code:** <https://github.com/USTC-StarTeam/ChemEval>
- **Dataset:** <https://huggingface.co/datasets/Ooo1/ChemEval>
- **Project:** <https://ustc-starteam.github.io/ChemEval/>
- **Venue:** ICLR 2026 (per the official repository; arXiv metadata carries no venue)

## Summary

ChemEval organizes chemical capability into 4 progressive levels and evaluates 12 dimensions of LLMs over 42 tasks, combining open-source data with tasks crafted by chemical experts for practical value. Evaluating 12 mainstream LLMs under zero-shot and few-shot settings, the paper finds a split: general models like GPT-4 and Claude-3.5 excel at literature understanding and instruction following but fall short on advanced chemical knowledge, while specialized chemistry LLMs show the reverse trade-off.

## Tasks

42 distinct chemical tasks across 4 progressive levels and 12 capability dimensions (arXiv version); static QA/task evaluation under zero- and few-shot prompting. The ICLR 2026 version reported by the official repository expands this to 62 textual and multimodal tasks over 13 dimensions.

## Domains

Chemistry — capability levels designed around the requirements of chemical research professionals, from literature understanding to advanced chemical knowledge.

## Evaluation

- Zero-shot and few-shot evaluation with curated demonstration examples and designed prompts across the task suite.
- **Reported.** General LLMs (GPT-4, Claude-3.5) excel in literature understanding and instruction following but lag on tasks demanding advanced chemical knowledge; specialized LLMs show enhanced chemical competence with reduced literary comprehension.

## Typical Duration

Single-turn tasks; no interactive or agentic setting.

## Main Contribution

A professional-requirements-first taxonomy of chemical capability — progressive levels and explicit dimensions rather than a flat QA pool — that exposes the general-vs-specialized model trade-off.

## Key Design Ideas

- Levels are progressive: the taxonomy encodes that some chemical capabilities presuppose others.
- Expert-crafted tasks anchor the suite to what practitioners need, not what data is easy to scrape.
- Separate dimensions let the general/specialist trade-off show up as a profile, not a single score.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The arXiv and ICLR versions differ (42 tasks/12 dimensions vs. 62 tasks/13 dimensions, with a changed title); numbers above state their source version.

## Strengths

- The level/dimension structure produces capability profiles that are directly actionable for model selection.
- Documents the general-vs-specialized split with a consistent protocol across 12 models.

## Related Works

- [ChemBench](./chembench.md) — Also broad chemical capability measurement, human-baselined rather than level-structured.
- [ChemCoTBench](./chemcotbench.md) — Also moves beyond flat chemical QA, via step-wise chemical operations.
- [PhySciBench](./physcibench.md) — Also expert-curated chemistry evaluation organized by task categories, on the deep-research side.
