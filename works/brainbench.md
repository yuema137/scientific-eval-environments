# BrainBench (2024)

> **English** | [简体中文](../zh/works/brainbench.md)

## Overview

BrainBench is a forward-looking benchmark for neuroscience, introduced in the paper "Large language models surpass human experts in predicting neuroscience results": given an original abstract from the Journal of Neuroscience and a version altered to change the result while maintaining coherency, the model must identify which reports the real outcome. It is a static two-alternative task, not an agent benchmark (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2403.03230>
- **Code:** <https://github.com/braingpt-lovelab/BrainBench>
- **Dataset:** <https://huggingface.co/datasets/BrainGPT>
- **Venue:** Nature Human Behaviour, 2024

## Summary

BrainBench tests whether a model has internalized how neuroscience experiments come out: 200 test cases (official dataset) pair real Journal of Neuroscience abstracts with coherently altered versions across five journal sections — behavioral/cognitive, systems/circuits, neurobiology of disease, cellular/molecular, and development/plasticity/repair. LLMs choose via perplexity comparison; human experts answer with confidence and expertise ratings. LLMs surpass the human experts at predicting experimental outcomes, their confidence is calibrated with accuracy, and BrainGPT — an LLM tuned on the neuroscience literature — performs better still.

## Tasks

Two-alternative forced choice over original-versus-altered neuroscience abstracts; 200 test cases per the official dataset; static, single-pass evaluation.

## Domains

Neuroscience across five Journal of Neuroscience sections: behavioral/cognitive, systems/circuits, neurobiology of disease, cellular/molecular, and developmental/plasticity/repair.

## Evaluation

- LLMs scored by perplexity over the paired abstracts; human experts by choice with confidence and expertise ratings; calibration analyzed.
- **Reported.** LLMs surpass human experts at predicting experimental outcomes; higher LLM confidence predicts higher accuracy; the neuroscience-tuned BrainGPT performs better yet. Numeric accuracies are TODO(reference).

## Typical Duration

Single forced-choice judgments; not an interactive agent setting.

## Main Contribution

Evaluates predictive rather than retrospective scientific knowledge — whether a model can anticipate what an experiment found — and shows generalist LLMs already beat domain experts at it.

## Key Design Ideas

- Result-altered abstract pairs test outcome prediction while controlling for style and coherence.
- Perplexity-based scoring needs no answer extraction or judge.
- Confidence calibration is analyzed as a first-class property, since a forecaster's confidence is only useful if calibrated.

## Strengths

- A rare benchmark of scientific foresight rather than recall, with a strong expert cohort.
- Nature Human Behaviour venue and wide discussion make it a reference point for "models as scientific forecasters."

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: BrainBench is a static forced-choice benchmark, not an agent evaluation; it is documented for its evaluation methodology (outcome prediction with calibration) relevant to judging scientific agents. BrainGPT, the paper's tuned model, is a modeling contribution out of scope.

## Related Works

- [MetaSyn](./metasyn.md) — Also anchors evaluation to published biomedical literature, via protocol-faithful synthesis.
- [Humanity's Last Exam](./hle.md) — Also frontier-expert comparison on closed-ended questions, across all academic subjects.
- [FormalRewardBench](./formalrewardbench.md) — Also evaluates a signal's ability to prefer true over corrupted artifacts, in formal proofs.
