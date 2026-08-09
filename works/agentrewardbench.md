# AgentRewardBench (2025)

> **English** | [简体中文](../zh/works/agentrewardbench.md)

## Overview

AgentRewardBench is a benchmark that measures how well automatic evaluators — LLM judges and the rule-based scorers shipped with web agent benchmarks — reproduce expert judgements of agent trajectories. It contains 1,302 trajectories drawn from 5 web benchmarks and 4 agent LLMs, each reviewed by an expert annotator for success, side effects, and repetition.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2504.08942>
- **Project:** <https://agent-reward-bench.github.io/>
- **Code:** <https://github.com/McGill-NLP/agent-reward-bench>
- **Venue:** COLM 2025

## Summary

AgentRewardBench argues that rule-based evaluation is hard to extend to new tasks and may fail to recognize successful trajectories, while human review is slower and more expensive, leaving it unclear how effective LLM judges are as a replacement. The authors collect 1,302 web agent trajectories and have expert annotators label each one for task success, unintended side effects, and repetition cycles, then use those labels to score both LLM judges and the environments' own scorers. Across 12 LLM judges no single model excels on all benchmarks, and the rule-based evaluation used by the source benchmarks underreports web agent success rates relative to expert annotation.

## Tasks

351 unique tasks across 8 environments and 66 websites, separated into 51 development and 300 test tasks: 100 each from WebArena, VisualWebArena and WorkArena++, 33 from AssistantBench, and 18 from WorkArena. Tasks are sampled from 5 existing web agent benchmarks rather than newly authored, drawing up to 8 tasks per domain-evaluation group for WebArena and up to 9 for VisualWebArena, and restricting WorkArena++ to Level 2. Running 4 agent LLMs over these tasks produces 1,302 trajectories, 196 in the development split and 1,106 in the test split.

## Domains

Web agent trajectories on self-hosted and live websites: general-purpose browsing, visually grounded tasks, open-web information seeking, and enterprise IT, HR and customer-management workflows on ServiceNow.

## Evaluation

- **Expert annotation as ground truth.** A team of 6 expert annotators answers three binary questions per trajectory — whether the action sequence achieved the goal, whether unnecessary actions risked unintended side effects, and whether the agent looped without making progress — yielding 3,906 binary annotations, with 89.3% inter-annotator agreement on success on the GPT-4o trajectories from WebArena.
- **Precision against the expert success label.** Judges are ranked by precision on the argument that false positives corrupt rejection finetuning and reward modeling; recall and F1 are reported as auxiliary scores.
- **Success-rate reconstruction.** Agent success rates computed from expert annotation, from a GPT-4o judge reading accessibility trees, and from the benchmark's own rule-based scorer are placed side by side to expose where the three disagree.
- **Reported (Table 1).** Rule-based evaluation reaches 83.8% precision at 55.9% recall, while the highest-precision LLM judge — the authors' simplified GPT-4o judge reading the accessibility tree — reaches 69.8% precision at 83.1% recall, and no judge exceeds 70% precision. Against expert annotation, rule-based scoring places GPT-4o 16.7% lower on WebArena and 18.5% lower on VisualWebArena.

## Typical Duration

Agents are configured with a maximum of 40K input tokens and 8,192 output tokens. Not stated: no per-task step cap, wall-clock limit, or trajectory-length distribution is reported.

## Main Contribution

A benchmark of 1,302 expert-annotated web agent trajectories for measuring how closely LLM judges and rule-based scorers reproduce expert judgements of task success, side effects, and repetition.

## Key Design Ideas

- Trajectories pooled from 5 existing web benchmarks and 4 agent LLMs rather than a single environment, so judge quality can be compared across task types.
- Three-part binary annotation schema covering task success, unintended side effects, and repetition cycles.
- Precision on the success label as the headline metric, selected for downstream rejection finetuning and reward modeling rather than for balanced accuracy.
- A simplified judge that answers the three annotation questions directly from either the final accessibility tree or the final screenshot, removing the captioning and change-summarization stages that prior judges require.

## Strengths

- Expert labels on every trajectory give a ground truth independent of the environments' own scoring rules, which is what makes the rule-based scorers themselves measurable.
- Pooling 5 benchmarks and 4 agent backbones separates judge quality from the quirks of any single environment.
- Annotating side effects and repetition alongside success captures failure modes that a single success bit cannot express.

## Limitations

- Repository note: The headline judge ranking scores only the success label; side-effect and repetition predictions are reported separately in an appendix table, so the main comparison does not reflect two of the three dimensions the annotators label — and the two behave differently, with repetition precision running above success precision and side-effect precision far below it.
- Repository note: Coverage is web browsing throughout — 8 environments behind 5 web benchmarks — so the judge rankings do not carry over to agent trajectories in other substrates.

## Related Works

- [AgentAtlas](./agentatlas.md) — Also an audit of existing benchmarks rather than a new task suite, but taxonomizing control decisions inside trajectories rather than measuring how faithfully automatic scorers reproduce expert success labels.
- [AgentBoard](./agentboard.md) — Also scores trajectories below end-task success, but through authored subgoal progress rather than by benchmarking the evaluators that emit the success label.
- [FinTrace](./fintrace.md) — Also multi-dimensional trajectory evaluation, but scoring agents on financial workflows rather than scoring the judges that grade web agents.
