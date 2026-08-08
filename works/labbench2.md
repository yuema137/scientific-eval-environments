# LABBench2 (2026)

> **English** | [简体中文](../zh/works/labbench2.md)

## Overview

LABBench2 is an improved benchmark for AI systems performing biology research: nearly 1,900 tasks that reprise the LAB-Bench capability categories in more realistic contexts — answering from PDFs, images, and bioinformatics files — producing model-specific accuracy drops of 26–46% across subtasks relative to LAB-Bench.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.09554>
- **Code:** <https://github.com/EdisonScientific/labbench2>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/labbench2>
- **Venue:** arXiv preprint (cs.AI, cs.CL, cs.LG), 2026

## Summary

The abilities LAB-Bench measures have improved substantially since 2024, so LABBench2 rebuilds the suite at higher realism: subtasks (per the official repository) include cloning, dbqa2, figqa2 and tableqa2 in image and PDF variants, litqa3, patentqa, protocolqa2, seqqa2, sourcequality, suppqa2, and trialqa, with tasks grounded in the artifacts researchers actually handle. The added realism produces a meaningful jump in difficulty — model-specific accuracy differences range from −26% to −46% across subtasks — restoring headroom for the next model generation.

## Tasks

Nearly 1,900 tasks across subtask families spanning literature, databases, figures/tables (image and PDF variants), protocols, sequences, cloning, patents, source quality, and clinical trials; static, with a public evaluation harness.

## Domains

Biology research practice: molecular biology and cloning, genomics sequences, protocols, literature and patents, clinical-trial records.

## Evaluation

- Accuracy over subtask families via the released evaluation harness.
- **Reported.** Relative to LAB-Bench, model-specific accuracy differences range from −26% to −46% across subtasks.

## Typical Duration

Single-task answering over realistic artifacts (PDFs, images, data files); not an interactive environment.

## Main Contribution

Shows how much of measured "biology capability" was formatting convenience: keeping the capabilities but restoring realistic context costs models up to 46 points.

## Key Design Ideas

- Realistic artifacts (PDFs, images, raw files) replace pre-digested question contexts.
- Subtask continuity with LAB-Bench makes the difficulty jump directly attributable to realism.
- New families (patents, source quality, trials) extend coverage toward research judgment.

## Strengths

- A controlled realism upgrade over an established reference suite.
- The −26% to −46% drop quantifies benchmark-form inflation directly.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [LAB-Bench](./lab-bench.md) — The predecessor suite whose capability categories LABBench2 hardens.
- [GAIA](./gaia.md) — Also emphasizes realistic multi-source contexts against benchmark saturation, for general assistants.
- [BixBench](./bixbench.md) — Also realism-first biology evaluation, via open-ended analysis rather than hardened QA.
