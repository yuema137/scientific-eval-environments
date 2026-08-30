# LLM4Mat-Bench (2024)

> **English** | [简体中文](../zh/works/llm4mat-bench.md)

> **First appeared:** 2024-10-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2411.00177)

## Overview

LLM4Mat-Bench benchmarks large language models for materials property prediction: about 1.9M crystal structures from 10 data sources with 45 properties, encoded in three text modalities (composition, CIF, crystal text description), evaluating both generative chat LLMs and fine-tuned language models — with the finding that task-specific models still dominate generative LLMs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.00177>
- **Code:** <https://github.com/vertaix/LLM4Mat-Bench>
- **Venue:** NeurIPS 2024 AI4Mat Workshop

## Summary

LLM4Mat-Bench asks how well language models predict materials properties from text encodings of crystals. It assembles ~1.9M structures across 10 public sources and 45 properties, with three input modalities — composition, CIF, and crystal text description (4.7M, 615.5M, and 3.1B tokens). Two model families are compared: generative chat LLMs (Llama, Gemma, Mistral) prompted zero-shot and few-shot, and fine-tuned language models (LLM-Prop, MatBERT) against a CGCNN baseline. The headline is sobering for the generative side — chat LLMs perform near-randomly on classification, while task-specific fine-tuned models dominate.

## Tasks

Property prediction from text-encoded crystals: regression over 45 properties and classification (stability, gap-direct), across ~1.9M structures and three modalities; static prediction, not interactive.

## Domains

Materials science — crystal property prediction from composition, CIF, and text descriptions.

## Evaluation

- Regression by MAD:MAE ratio (higher is better); classification by AUC.
- **Reported.** Fine-tuned LLM-Prop and MatBERT lead; generative chat LLMs are near-random (AUC ≈ 0.5) on classification; task-specific models dominate.

## Typical Duration

Single-prediction queries; no interactive setting.

## Main Contribution

A large, multi-modality measurement of where language models stand on materials property prediction — documenting that prompting generative LLMs does not yet rival fine-tuned task-specific models.

## Key Design Ideas

- Three text modalities (composition/CIF/description) separate what encoding the model can exploit.
- MAD:MAE ratio makes regression quality comparable across properties of different scales.
- Pairing generative LLMs with fine-tuned baselines frames the current capability gap honestly.

## Strengths

- Scale (1.9M structures, 45 properties, 10 sources) and modality breadth in one suite.
- The generative-vs-fine-tuned comparison is directly decision-relevant.

## Limitations

- Repository note: card compiled from the arXiv abstract, Comments, and official repository (August 2026); the benchmark evaluates both generative chat LLMs and fine-tuned encoder models (LLM-Prop/MatBERT), and is included here for the former. Per-model result tables beyond the repository leaderboard await full-paper validation.

## Related Works

- [MatText](./mattext.md) — Also LLM materials property prediction from crystal text, analyzing the LLM-vs-GNN gap.
- [MaScQA](./mascqa.md) — Also LLM materials evaluation, on knowledge QA rather than property regression.
- [MatTools](./mattools.md) — Also LLMs over materials computation, via tool-use rather than direct prediction.
