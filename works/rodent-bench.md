# Rodent-Bench (2026)

> **English** | [简体中文](../zh/works/rodent-bench.md)

## Overview

Rodent-Bench evaluates multimodal LLMs on annotating rodent behavior video across neuroscience paradigms — social interactions, grooming, scratching, and freezing — over long recordings (10–35 minutes), finding that no current model performs well enough to serve as an annotation assistant.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.18540>
- **Venue:** arXiv preprint (cs.CV), 2026

## Summary

Behavioral annotation is a labor-intensive bottleneck in rodent neuroscience, and Rodent-Bench tests whether multimodal LLMs can help. It evaluates Gemini-2.5-Pro, Gemini-2.5-Flash, and Qwen-VL-Max on real rodent behavior footage spanning multiple paradigms (social interactions, grooming, scratching, freezing), with videos from 10 to 35 minutes and two benchmark versions. Scored on second-wise accuracy, macro F1, mean average precision, mutual information, and Matthews correlation coefficient, none of the models perform strongly enough to act as an assistant, with particular difficulty in temporal segmentation, long sequences, and subtle behavioral states.

## Tasks

Temporal segmentation and behavioral classification of real rodent behavior video across multiple paradigms; long recordings (10–35 min); two benchmark versions. Static multimodal annotation. Video/instance counts are TODO(reference) — not stated in the abstract.

## Domains

Neuroscience & Cognitive Science — behavioral neuroscience: annotation of rodent behavior video (social, grooming, scratching, freezing paradigms).

## Evaluation

- Second-wise accuracy, macro F1, mean average precision, mutual information, and Matthews correlation coefficient, over three MLLMs.
- **Reported.** No model performs strongly enough to be an assistant; modest performance on some datasets (e.g., grooming); difficulty with temporal segmentation, long sequences, and subtle states.

## Typical Duration

Per-video annotation over 10–35-minute recordings; static (no interaction).

## Main Contribution

A realistic test of multimodal LLMs as behavioral-annotation assistants for rodent neuroscience — showing current models fall short on exactly the temporal, long-context, and fine-distinction demands the task requires.

## Key Design Ideas

- Long real recordings (10–35 min) stress temporal and long-context handling, not single frames.
- Five metrics capture segmentation quality beyond frame accuracy.
- Multiple paradigms span the behaviors neuroscience annotation actually needs.

## Strengths

- Real rodent behavior data across genuinely different paradigms.
- The "not yet an assistant" finding is a concrete, decision-relevant result with rich metrics.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); video/instance counts and per-model numbers are in the paper body, and no code URL is confirmed from the arXiv page. No venue is stated in arXiv metadata.

## Related Works

- [BrainBench (EEG)](./brainbench-eeg.md) — Also multimodal neuroscience-data analysis, on EEG signals rather than behavior video.
- [SpatialBench](./spatialbench.md) — Also verifiable analysis of real biological data, in spatial transcriptomics.
- [BioXArena](./bioxarena.md) — Also agents analyzing multimodal biological data end to end.
