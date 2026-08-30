# MatText (2024)

> **English** | [简体中文](../zh/works/mattext.md)

> **First appeared:** 2024-06-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2406.17295)

## Overview

MatText is a benchmarking framework for predicting materials properties with large language models from text representations of crystals: across nine representations and model scales up to 70B parameters and 2M structures, it documents a persistent "geometric blindness" — LLMs capture category patterns but miss coordinate information, and specialized geometric architectures outperform them by significant margins.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.17295>
- **Code:** <https://github.com/lamalab-org/MatText>
- **Project:** <https://lamalab-org.github.io/MatText/>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2024

## Summary

Published in its current version as "Less can be more for predicting properties with large language models," this work introduces the MatText benchmarking framework to test whether LLMs can predict crystal properties from text encodings. It spans nine text representations (composition/Hill, SLICES, CIF P1, crystal-text-llm, atom sequences, Z-matrix, local-env, and others), model scales up to 70B parameters, and datasets up to 2M structures, evaluating Llama-3-8B (LoRA-fine-tuned) and custom BERT-based models against geometric GNN baselines. The conclusion is a "GNN-LM wall": LLMs consistently fail to capture coordinate information while excelling at category patterns, and geometric architectures outperform them by significant margins.

## Tasks

Property regression from text-encoded crystals across nine representations (MatBench tasks — shear/bulk modulus, perovskite formation energy — plus synthetic tunable datasets); static prediction, not interactive.

## Domains

Materials science — crystal property prediction from text representations, contrasted against geometric graph neural networks.

## Evaluation

- Property-prediction error (regression) across representations and scales, compared against GNN baselines.
- **Reported.** LLMs capture category patterns but miss coordinate information; geometric architectures outperform LLMs by significant margins ("GNN-LM wall").

## Typical Duration

Single-prediction queries; no interactive setting.

## Main Contribution

Isolating "geometric blindness" as a structural limitation of text-based LLM materials modeling — a framework-plus-finding showing where the text-encoding approach hits a wall against geometry-aware models.

## Key Design Ideas

- Nine representations turn "how you encode structure as text" into a measured variable.
- Sweeping scale (to 70B, to 2M structures) tests whether the limitation is just capacity.
- Synthetic tunable datasets isolate coordinate vs. category information directly.

## Strengths

- The representation sweep is broader than any single-encoding study.
- The geometric-blindness diagnosis is a concrete, actionable limitation, not a leaderboard.

## Limitations

- Repository note: the paper's contribution is the MatText framework plus an analysis/position finding; this card centers the benchmarking framework. The paper was retitled to "Less can be more for predicting properties with large language models"; no venue is stated in arXiv metadata.

## Related Works

- [LLM4Mat-Bench](./llm4mat-bench.md) — Also LLM materials property prediction from text, at larger property/source breadth.
- [AtomWorld](./atomworld.md) — Also probes LLM crystal-geometry understanding, via structure manipulation.
- [MatTools](./mattools.md) — Also LLMs over materials computation, through tool-use.
