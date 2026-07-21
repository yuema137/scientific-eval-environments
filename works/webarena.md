# WebArena (2023)

## Overview

WebArena is a realistic, reproducible web environment for building and evaluating autonomous agents. It hosts fully functional websites across four common domains and evaluates language-guided agents on long-horizon web tasks by functional correctness.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2307.13854>
- **Code:** <https://github.com/web-arena-x/webarena>

## Summary

WebArena argues that current agents are mostly created and tested in simplified synthetic environments, creating a disconnect with real-world scenarios. It builds a highly realistic and reproducible environment of fully functional websites drawn from four common domains — e-commerce, social forum discussions, collaborative software development, and content management — and evaluates agents that perform diverse, long-horizon tasks via natural-language commands. Success is judged by functional correctness. The best GPT-4-based agent achieves a 14.41% end-to-end task success rate, far below the human benchmark of 78.24%.

## Tasks

Diverse, long-horizon web tasks mirroring routine internet activities, issued as natural-language commands. Task count: TODO(reference) — not stated in the abstract.

## Domains

Fully functional websites across four domains: e-commerce, social forum discussions, collaborative software development, and content management.

## Evaluation

- Functional correctness: task completions are checked programmatically against the resulting state of the websites.
- Reported: best GPT-4-based agent reaches 14.41% end-to-end success vs. 78.24% for humans.

## Typical Duration

Long-horizon multi-step web interactions per task. Per-task step budget: TODO(reference) — not stated in the abstract.

## Main Contribution

A realistic, reproducible web environment of fully functional real-world websites, enabling functional-correctness evaluation of autonomous agents on long-horizon tasks rather than in simplified synthetic settings.

## Key Design Ideas

- Fully functional, self-hosted websites for reproducibility and realism.
- Four everyday web domains for breadth of routine tasks.
- Functional-correctness evaluation on end state rather than surface string matching.
- Long-horizon tasks that require multi-step navigation and action.

## Strengths

- High realism and reproducibility via self-hosted functional websites.
- Functional-correctness scoring reflects real task outcomes.
- Large human-model gap (78.24% vs. 14.41%) gives clear headroom.

## Limitations

- Repository note: Task count and per-domain distribution are not stated in the abstract and are marked `TODO(reference)`.

## Related Works

- [OSWorld](./osworld.md) — Also an interactive, execution-evaluated environment, but spanning whole operating systems and desktop applications rather than web sites only.
- [GAIA](./gaia.md) — Also requires real web interaction, but scored by answer correctness rather than functional website state.
