# WebArena (2023)

> **English** | [简体中文](../zh/works/webarena.md)

> **First appeared:** 2023-07-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2307.13854)

## Overview

WebArena is a realistic, reproducible web environment for building and evaluating autonomous agents. It hosts fully functional websites across four common domains and evaluates language-guided agents on long-horizon web tasks by functional correctness.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2307.13854>
- **Code:** <https://github.com/web-arena-x/webarena>

## Summary

WebArena argues that current agents are mostly created and tested in simplified synthetic environments, creating a disconnect with real-world scenarios. It builds a highly realistic and reproducible environment of fully functional websites drawn from four common domains — e-commerce, social forum discussions, collaborative software development, and content management — and evaluates agents that perform diverse, long-horizon tasks via natural-language commands. Success is judged by functional correctness. The best GPT-4-based agent achieves a 14.41% end-to-end task success rate, far below the human benchmark of 78.24%.

## Tasks

812 instantiated task intents from 241 templates (averaging 3.3 instantiations per template), issued as natural-language commands. Some intents are deliberately unachievable and labeled N/A — the agent must recognize infeasibility rather than hallucinate a result.

## Domains

Four fully functional, self-hosted websites — e-commerce (an OneStopShop/Magento storefront), a content-management/admin site, a social forum (Postmill/Reddit-style), and collaborative software development (GitLab) — plus supporting tools (map, calculator, scratchpad) and knowledge resources (Wikipedia, manuals).

## Evaluation

Success is judged by programmatic reward functions on the resulting website state, not by trajectory matching, across two task families:

- **Information-seeking** — the agent's textual answer is scored by `exact_match` (identical to the reference), `must_include` (contains required facts/keywords), or `fuzzy_match` (GPT-4 judges semantic equivalence).
- **Site-navigation / configuration** — a locator retrieves the intent-critical state via a database query, a site API call, or JavaScript element selection, and annotated required contents are verified there (exact / must_include, plus URL and element-state checks).
- **Unachievable tasks** are included and labeled N/A; the agent must respond that the task is not possible, testing whether it avoids unfounded claims.

Execution allows at most **30 state transitions** per task, halting early if an action repeats more than three times or the agent emits three consecutive invalid actions. Reported: the best GPT-4 configuration reaches 14.41% end-to-end success (11.70% with the unachievable-task hint) vs. 78.24% for humans (74.68% on information-seeking, 81.32% on navigation/configuration).

## Typical Duration

Long-horizon multi-step web interactions, capped at 30 state transitions per task (with early stopping on repeated or invalid actions). In the human study, five CS graduate students averaged ~110 seconds per task over 170 sampled tasks.

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

- Repository note: The paper reports 812 total intents but gives the per-website distribution only as a chart (Figure 6), not exact per-site counts; cross-site tasks exist as a category without a stated count.

## Related Works

- [OSWorld](./osworld.md) — Also an interactive, execution-evaluated environment, but spanning whole operating systems and desktop applications rather than web sites only.
- [GAIA](./gaia.md) — Also requires real web interaction, but scored by answer correctness rather than functional website state.
