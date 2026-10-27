# AgentProofBench (2026)

> **English** | [简体中文](../zh/works/agentproofbench.md)

> **First appeared:** 2026-10-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.34634)

## Overview

AgentProofBench tests reusable verifiers for Web agents. A model writes an acceptance program once; the program is then frozen and judges task completion from before and after states. The benchmark asks two questions. Does the program stay correct when the starting state changes what the same instruction requires? Does gating an agent on the program's verdict improve what the agent finally delivers?

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — evaluates verifiers for general Web-service agents; no scientific or research activity is evaluated.

## Links

- **Paper:** [AgentProofBench: Benchmarking Reusable Verifiers for Web Agents](https://arxiv.org/abs/2610.34634)
- **Full text:** <https://arxiv.org/html/2610.34634v1>
- **Venue:** arXiv preprint (2026)

## Summary

The public instruction stays fixed, but which entities, values, or collections it requires can depend on the initial state. A checker built from the instruction alone can therefore accept the wrong outcome. At the requirement level, each frozen program is run on panels of terminal states from three initial conditions. Source is the original. Background changes data outside the requested work. Related changes a required entity binding, initial value, collection, or preservation condition. Reused source programs are compared with programs rebuilt for the changed state. At the policy level, four delivery policies branch from identical saved openings. A verifier is then judged by whether gating on it changes correct delivery.

## Tasks

97 tasks in 79 families on four Web services: Linear, Slack, Box, and Calendar. Environments are Agent-Diff enterprise-service replicas. The matched reuse study uses 48 tasks from 48 families (18 Linear, 10 Slack, 19 Box, 1 Calendar). It has 576 frozen programs and 558 terminal states (270 valid, 288 failed). The natural acceptance panel has 556 states (452 successes, 104 failures). The execution study has 44 trajectories from 22 families, 88 saved openings, and 352 policy outcomes. Three tasks are excluded from the explicit-acceptance view after inspection.

## Domains

N/A — the tasks run on general Web services, not a science or engineering field.

## Evaluation

- A program implements `verify(task, before, after)` and returns Pass, Fail, or Unknown. It runs read-only in a fresh sandbox with one CPU, 1 GB of memory, 60 seconds, 80 business operations, and no model calls. Unknown and Error receive no correctness credit.
- Metrics: balanced accuracy (BA) over valid and failed states, plus complete-panel correctness. A decision-replay witness replays an earlier valid decision under a changed condition. A joint pass requires both the panel and the witness to be correct.
- Reuse: related-state BA for source programs is 93.23% (Flash) and 90.36% (Pro). Reuse-minus-rebuild BA intervals from 10,000 family-bootstrap resamples are [−5.47, 1.57] and [−10.16, 0.00] points. Joint correctness is 82/96 reused vs. 82/96 rebuilt (Flash) and 79/96 vs. 86/96 (Pro).
- Programs vs. online judgments: on the natural panel, twelve-call programs reach 92.1% BA and fresh twelve-call online judgments 99.0%. In a 135-state collection comparison, false acceptance on its 99 failed states is 3.5% vs. 31.7%.
- Execution: 32 of 33 assignments with error-free related panels deliver both openings correctly, against 1 of 11 with panel errors. At checkpoints, correct delivery is 20/22 and 22/22 for neutral continuation, 17/22 and 16/22 for the program gate, and 20/22 and 21/22 for the online gate.
- A GPT-6 Astra audit agrees with 191 of 192 resolved reference labels (κ = 0.989).

## Typical Duration

Each verifier assessment is capped at 60 seconds. Median construction cost is USD 0.0173 (Flash) and 0.0765 (Pro). Median break-even against fresh online judging is 12 and 10 assessments. Agent task wall-clock time is not reported.

## Main Contribution

A benchmark that tests frozen Web-agent verifiers when the initial state changes the requirement, and links verifier correctness to delivery outcomes from identical saved openings.

## Key Design Ideas

- Freeze the program once, then compare reuse with rebuilding on the same changed states.
- Change required bindings separately from irrelevant background data.
- Branch all policies from the same saved opening, including original state, current state, and interaction history.
- Use neutral continuation as the baseline for what a verification gate adds.

## Strengths

- Paired reuse-versus-rebuild comparisons with family-bootstrap intervals.
- Verifier verdicts are tied to downstream delivery, not only panel accuracy.
- Reports program construction and online-judging costs.

## Limitations

- Generator, judge, and actor results use only DeepSeek Flash and Pro, with thinking disabled.
- The panel-to-delivery link is exploratory and rests on 44 assignments from 22 families.
- Gate results hold for the tested generic feedback message.
- Reference development used an LLM, and the label audit is also LLM-based; no human annotation is reported.
- Repository note: the paper states that its original code and annotations use the MIT license, but neither the arXiv record nor the v1 full text links a code or data release, and none was found by web search on 2026-10-27.

## Related Works

- [AgentRewardBench](./agentrewardbench.md) — Compares automatic Web-agent evaluators with expert labels.
