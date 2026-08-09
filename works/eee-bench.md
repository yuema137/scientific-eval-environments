# EEE-Bench (2024)

> **English** | [简体中文](../zh/works/eee-bench.md)

## Overview

EEE-Bench is a comprehensive multimodal electrical and electronics engineering benchmark: 2,860 curated problems spanning 10 essential subdomains (analog circuits, control systems, and more) that require understanding intricate images like abstract circuits and system diagrams alongside professional instructions — where 17 LLMs and LMMs average only 19.48%–46.78%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.01492>
- **Venue:** CVPR 2025

## Summary

EEE-Bench measures whether multimodal foundation models can solve real electrical-engineering problems, where the answer depends on reading a circuit or system diagram, not just text. Its 2,860 curated problems span 10 essential EE subdomains — analog circuits, control systems, and others — each pairing intricate imagery (abstract circuits, system diagrams) with professional instructions. Evaluating 17 open and closed LLMs and LMMs reveals notable deficiencies, with average performance between 19.48% and 46.78%, and the paper identifies a "laziness" failure mode: models lean on text and overlook the visual context that the problem actually hinges on.

## Tasks

2,860 multimodal EE problems across 10 subdomains (analog circuits, control systems, signals, digital, and more); static problem solving requiring joint image-and-text understanding.

## Domains

Electrical Engineering — broad multimodal coverage across 10 EE subdomains, grounded in real circuit and system-diagram imagery.

## Evaluation

- Accuracy across subdomains over 17 LLMs and LMMs, with fine-grained analysis and the "laziness" (text-over-vision) finding.
- **Reported.** Average performance ranges from 19.48% to 46.78%, indicating notable deficiencies in current foundation models on EE.

## Typical Duration

Single-turn multimodal problems; no interactive setting.

## Main Contribution

The broadest multimodal EE benchmark by subdomain coverage — and the "laziness" diagnosis showing models systematically underuse the circuit and diagram imagery that EE problems depend on.

## Key Design Ideas

- Ten-subdomain span makes it representative of EE rather than a single niche.
- Real circuit/diagram imagery forces genuine visual understanding, not caption reading.
- The "laziness" analysis names a concrete, general multimodal failure mode.

## Strengths

- Venue-verified (CVPR 2025) with wide model coverage (17) and broad EE scope.
- The 19–47% band gives a clear capability marker for multimodal EE.

## Limitations

- Repository note: card compiled from the arXiv abstract and Comments (August 2026); CVPR 2025 is confirmed via Comments. No official code/project URL is verifiable from the arXiv page.

## Related Works

- [MMCircuitEval](./mmcircuiteval.md) — Also multimodal EE/circuit QA, organized by design stage and circuit type.
- [AnalogXpert](./analogxpert.md) — Also covers analog design, as an agentic synthesis task rather than QA.
- [MatSciBench](./matscibench.md) — Also a multimodal engineering/science reasoning benchmark, in materials.
