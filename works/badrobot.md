# BadRobot (2024)

> **English** | [简体中文](../zh/works/badrobot.md)

## Overview

BadRobot jailbreaks embodied LLM agents in the physical world: an attack paradigm exploiting three vulnerabilities of LLM-robot stacks, evaluated with a companion benchmark of 277 malicious physical-action queries across six harm categories against frameworks like Code as Policies, ProgPrompt, and VoxPoser — reaching an average manipulate success rate of 68.57%, with demonstrations on real UR3e and myCobot robots.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — evaluates an agent meta-property (cost, safety, or robustness), not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2407.20242>
- **Code:** <https://github.com/Rookie143/BadRobot>
- **Project:** <https://Embodied-LLMs-Safety.github.io>
- **Venue:** ICLR 2025

## Summary

Chat-side jailbreak research asks whether a model will say something harmful; BadRobot asks whether it will do something harmful. The attack paradigm targets embodied LLM/VLM frameworks receiving voice or text queries and producing executable action plans or code, using a benchmark of 277 malicious queries spanning physical harm, privacy violence, pornography, fraud, illegal activity, and hateful conduct (paper body). Across targets including GPT-4-class and open VLMs, the method achieves an average Manipulate Success Rate of 68.57%, with the loop closed on physical UR3e and myCobot 280-Pi platforms — establishing that language-level safety training does not reliably survive the translation into action.

## Tasks

Adversarial episodes: malicious queries (277, six categories) issued to embodied LLM frameworks whose generated actions are executed in digital environments, simulators, and on real robot arms.

## Domains

Robotics — attacks on LLM-driven robot control with executed physical actions on real UR3e and myCobot platforms.

## Evaluation

- Manipulate Success Rate (MSR) and harmfulness scores over the query benchmark.
- **Reported.** Average MSR of 68.57% (paper body); abstract carries no numbers.

## Typical Duration

Single query-to-action episodes per attack attempt.

## Main Contribution

Moving jailbreak evaluation across the say/do boundary: demonstrating, with executed robot actions, that embodied deployment creates attack surfaces language-level alignment does not cover.

## Key Design Ideas

- Three identified vulnerability classes structure the attack space rather than ad-hoc prompting.
- The 277-query benchmark spans harm categories, making refusal behavior comparable across frameworks.
- Real-robot demonstrations close the "it would never actually execute" objection.

## Strengths

- Venue-verified (ICLR 2025 on arXiv, including Journal-ref) with physical validation.
- The framework-level attack scope covers the embodied stacks practitioners actually deploy.

## Limitations

- Repository note: the paper's primary contribution is the attack paradigm; the 277-query benchmark is its paired evaluation set, and this card covers the benchmark side. Query counts and MSR figures come from the paper body, not the abstract.
- Repository note: card compiled from the arXiv abstract, paper body, and official pages (August 2026).

## Related Works

- [SafeAgentBench](./safeagentbench.md) — Also embodied LLM safety, from the defender's side via hazard-task rejection.
- [ASIMOV](./asimov.md) — Also robot-safety evaluation, at the level of constitutional judgment rather than attack.
- [EmbodiedBench](./embodiedbench.md) — Also evaluates the embodied LLM stacks that BadRobot attacks.
