# Gaia2 (2026)

> **English** | [简体中文](../zh/works/gaia2.md)

## Overview

Gaia2 is a benchmark for LLM agents in asynchronous environments, where the world evolves on its own clock rather than only when the agent acts. Its 1,120 scenarios run in a simulated smartphone universe and are scored by a verifier that checks every state-changing action against oracle annotations, making the benchmark directly usable for reinforcement learning from verifiable rewards.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2602.11964>
- **Venue:** ICLR 2026

## Summary

The authors observe that most agent benchmarks are static or synchronous — environments change only when the agent acts, and evaluation ignores intermediate actions — so challenges that dominate real deployments, such as asynchronous events and operating under temporal constraints, go untested. Gaia2 addresses this by running scenarios in event-driven environments that advance independently of the agent, and by scoring trajectories against a minimal oracle sequence of state-changing actions rather than a final answer. Across seven capability splits, GPT-5 (high) leads with 42.1% pass@1 overall while scoring 0.0 on the Time split, and no evaluated system dominates across all capabilities.

## Tasks

1,120 scenarios spanning seven capability splits. Five are core — Execution, Search, Ambiguity, Adaptability, and Time — comprising 800 unique human-authored scenarios, each instantiated with its own event DAG and initial environment state. The remaining two, Noise and Agent2Agent, are environment-level augmentations applied to base scenarios: Noise injects tool anomalies and irrelevant environment events, while Agent2Agent replaces apps with app-agents the main agent must coordinate with by messaging. Annotators build scenarios through the ARE annotation interface over a generated mobile universe, authoring DAGs of write actions and environment events as ground truth, followed by rounds of independent validation, automated structural guardrails, and post-hoc difficulty calibration against a baseline agent.

## Domains

A simulated consumer smartphone environment of twelve stateful apps — messaging, email, calendar, contacts, files, chats, cabs, shopping, city information, rentals, and a system app — rather than a scientific domain.

## Evaluation

- **ARE Verifier over write actions.** Trajectories are checked against a minimal oracle sequence and judged goal-oriented rather than path-optimal: read actions are unlimited and unpenalized, only state-changing write actions count toward goals, and independent goals are order-agnostic.
- **Four verification dimensions.** Consistency (tool names and counts must match; exact matching for rigid fields such as IDs and LLM rubrics for free-text ones, with anti-hacking checks), Causality (actions must respect dependency DAGs), Timing (enforced through tolerance windows), and Completeness (success requires matching every oracle write action).
- **Verifier validation.** On 450 hand-labeled validation trajectories the ARE Verifier reaches 0.98 agreement, 0.99 precision, and 0.95 recall, against 0.72, 0.53, and 0.83 for an in-context LLM-judge-only baseline. The verifier itself runs Llama-3.3-70B-Instruct at temperature 0.
- **Cost-conditioned scoring.** Results are also reported as budget scaling curves — pass@1 counted only for scenarios solved below a maximum per-scenario dollar budget swept from roughly 0.01 to 10 USD, priced from third-party model-pricing data.
- **Reported.** GPT-5 (high) leads at 42.1% pass@1 overall, with 69.2 on Execution and 79.6 on Search but 0.0 on Time; Claude-4-Sonnet Thinking reaches 37.8 overall and Kimi-K2 leads the open-weight models at 20.1. Every model scores below 9 on Time, and the authors report that instruction-following and search are largely solved while robustness, ambiguity resolution, and collaboration remain open.

## Typical Duration

A scenario terminates on whichever comes first of 200 steps, context overflow, verification completion, or timeout. Models are run at full context length with a 16,000-token generation limit per turn and temperature 0.5, and every scenario is run three times to account for variance. Because the environment advances on its own clock, the harness simulates generation time — pausing during responses and resuming with a matching time offset — so that wall-clock latency affects task outcomes rather than only cost.

## Main Contribution

A benchmark that makes environment asynchrony a scored dimension of agent evaluation, paired with a write-action verifier that the authors present as a standalone, reusable mechanism for fine-grained credit assignment and verifiable-reward training beyond Gaia2 itself.

## Key Design Ideas

- Event-driven environments that advance on their own clock, so temporal awareness and latency become measured failure modes rather than incidental costs.
- A read/write action distinction: exploration through read actions is unlimited and unpenalized, while only state-changing write actions are credited, separating information gathering from commitment.
- Capability splits designed as dominant flavors rather than orthogonal dimensions, with a deliberate decision not to add a compositional split after early attempts at artificially combining three or more capabilities produced unnatural tasks without a clear evaluation signal.
- Environment-level augmentations for Noise and Agent2Agent that reuse base-scenario annotations, because the verifier checks state changes rather than specific tool traces.

## Strengths

- The verifier is validated rather than asserted: 450 hand-labeled trajectories put its agreement at 0.98 against 0.72 for an LLM-judge-only baseline, so the credit signal has a measured reliability figure.
- Crediting write actions against a dependency DAG rather than matching a reference path admits multiple valid orderings while still catching missing or causally misplaced steps.
- The Time split produces a near-total failure across every evaluated model despite strong overall scores, isolating a capability that aggregate pass rates hide entirely.

## Limitations

- Repository note: The environment is a simulated consumer smartphone universe, so the benchmark measures asynchronous coordination in a domain with no scientific content; its design ideas transfer to scientific settings but its tasks do not.
- Repository note: Verification depends on human-authored oracle DAGs plus LLM rubrics for free-text fields, so both the ground truth and part of the scoring inherit annotator and judge decisions, and the reported reliability figures come from the authors' own validation set.

## Related Works

- [GAIA](./gaia.md) — Also poses tasks that are simple for humans and hard for models, but evaluates correctness at the final output level by exact match, which the Gaia2 authors identify as the limitation their action-level verifier addresses.
- [TRACE](./trace.md) — Also credits a trajectory below the final outcome, but aggregates a hierarchical utility function over reasoning quality and efficiency rather than checking state-changing actions against an oracle dependency graph.
- [OSWorld](./osworld.md) — Also scores execution against real environment state, but in a synchronous operating system that changes only when the agent acts rather than on an independent clock.
