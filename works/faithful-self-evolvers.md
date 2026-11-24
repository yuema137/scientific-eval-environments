# LLM Agents Are Not Always Faithful Self-Evolvers (2026)

> **English** | [简体中文](../zh/works/faithful-self-evolvers.md)

> **First appeared:** 2026-01-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2601.22436)

## Overview

Self-evolving agents store experience from earlier episodes and insert it into later prompts. The usual evaluation reports whether success rises after experience is added, which assumes the agent's decisions actually depend on that experience. This study checks the assumption directly. It perturbs or removes the inserted experience while leaving everything else fixed, then measures whether the agent's performance moves. If performance does not move when the experience is emptied or replaced, the agent was not using it.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities


N/A — Diagnostic study of whether self-evolving agents faithfully use their memory, run across general QA, reasoning, embodied, and web environments; evaluates an agent meta-property, not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2601.22436>
- **Code:** <https://github.com/Dreamcatcher0622/Faithfulness>
- **Venue:** ICML 2026

## Summary

The authors define *experience faithfulness* as whether an agent's behavior causally changes in response to the experience it is given. They split experience into two kinds: *raw* experience (for example, full successful trajectories reused as demonstrations) and *condensed* experience (natural-language insights, heuristics, or memory items distilled from trajectories). For each kind they apply controlled interventions, such as emptying the content while keeping its formatting, shuffling trajectory steps, swapping in experience from unrelated tasks, corrupting key components, or replacing condensed text with filler tokens, inside four existing self-evolving frameworks. Across the tested backbones and environments, perturbing raw experience changes performance, while perturbing condensed experience often has little effect, even when condensed experience is the only experience supplied. The study diagnoses whether experience is used; it does not propose a new self-evolving method.

## Tasks

N/A — diagnostic study, not a new benchmark. Interventions are run on 9 existing environments: HotpotQA, FEVER, GPQA-Diamond, MMLU-Pro (engineering), AIME 2024, Game of 24, ALFWorld, WebArena, and WebShop. Reported sample sizes include 100 HotpotQA questions, 198 GPQA-Diamond questions, and 812 WebArena tasks; an additional check uses 100 examples each from 2WikiMultiHopQA and Musique.

The four frameworks are ExpeL (offline, single-agent; raw = successful trajectories, condensed = extracted insights), Dynamic Cheatsheet (online, single-agent), ReasoningBank (online, single-agent; condensed memory items with title, description, and content), and G-Memory (online, multi-agent; two raw experience types plus one condensed type). The abstract reports 13 LLM backbones; Section 3.1 of the v3 HTML states 10. Named backbones include GPT-4o, GPT-4o-mini, GPT-5.2, Gemini-2.5-Flash, Gemini-3-Pro, Claude-Sonnet-4.6, and Qwen3 models from 1.7B to 235B-A22B.

## Domains

Multi-hop and fact-verification question answering, graduate-level science and engineering multiple-choice questions, competition mathematics, arithmetic puzzles, embodied household tasks (ALFWorld), and web navigation and shopping (WebArena, WebShop).

## Evaluation

- **Intervention arms.** Raw experience: Empty, Shuffle, Irrelevant, plus removal ("w/o Raw"). Condensed experience: Empty, Corrupt, Irrelevant, Filler, plus removal ("w/o Cond").
- **Faithfulness signal.** The paper gives no single faithfulness formula. An agent is treated as faithful to an experience channel when its task score (success rate or exact match, per environment) changes under perturbation of that channel. A trace: ExpeL with Qwen3-32B scores 62 exact match on 2WikiMultiHopQA with intact experience and 63 to 65 under every raw and condensed perturbation, so on this task the inserted experience does not drive the answer.
- **Failure analysis.** On WebArena with ReasoningBank, cases where the agent succeeds without condensed experience but fails with it are labeled as distraction, over-reliance on incorrect priors, or premature inference (for example, Gemini-2.5-Flash on Shopping: 45.2% distraction, 32.3% reliance, 22.6% premature).
- **Attribution analysis.** Integrated Gradients per attention head and layer, aggregated over prompt segments, on ALFWorld with Qwen3-32B; condensed experience receives consistently low attribution, and the current trajectory dominates later layers.

## Typical Duration

Inherited from the underlying environments and frameworks; the study does not set its own step, time, or token budget. TODO(reference)

## Main Contribution

The authors present the first systematic study of experience faithfulness in self-evolving LLM agents. Their causal interventions show that agents depend on raw experience but often ignore or misread condensed experience. They attribute the gap to three factors: the limited specificity of condensed content, internal processing biases that favor the current context, and tasks where pretrained knowledge already suffices.

## Key Design Ideas

- Separate the experience channel into raw and condensed parts and perturb each independently, so a score change can be traced to one channel.
- Use content-free controls (Empty keeps the formatting; Filler keeps the length) to separate the effect of content from the effect of prompt structure.
- Repeat the same intervention set across offline and online, and single- and multi-agent, frameworks.
- Pair behavioral interventions with gradient-based attribution to locate where condensed experience is down-weighted inside the model.

## Strengths

- Interventions are applied inside four existing frameworks rather than a single custom agent, so the finding is not tied to one memory design.
- The study covers reasoning, embodied, and web environments and both proprietary and open-weight backbones across scales.
- Code for the interventions is released.

## Limitations

- Knowledge-intensive tasks (HotpotQA, GPQA, MMLU-Pro, FEVER) show low sensitivity to any experience perturbation, which the authors attribute to pretrained priors; on those tasks, insensitivity cannot be read only as unfaithfulness to condensed experience.
- Repository note: The paper's backbone count differs between the abstract (13) and Section 3.1 (10), and most per-condition results are reported in figures rather than tables.
- Repository note: The faithfulness signal is a change in aggregate task score, so it detects whether an experience channel affects outcomes, not whether individual decisions consulted it.

## Related Works

- [SkillEvolBench](./skillevolbench.md) — Also tests whether distilled experience helps agents, but scores whether agents can form reusable skills rather than whether supplied experience causally changes behavior.
- [SkillMisevo-Bench](./skillmisevo-bench.md) — Also examines what self-improving agents store from past episodes, but focuses on unsafe content entering a skill library.
- [SkillLearnBench](./skilllearnbench.md) — Also evaluates experience-derived skills, scoring generated skill quality alongside task success.
