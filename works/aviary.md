# Aviary (2024)

## Overview

Aviary is an extensible gymnasium for language agents that formalizes agents as policies solving language-grounded partially observable Markov decision processes. It implements five environments, three of them scientific — DNA construct manipulation (molecular cloning), scientific literature research, and protein engineering — providing reusable multi-step scientific task environments. It is documented here for these scientific evaluation environments; the paper's training-framework contribution is agent-construction work adjacent to this repository's scope (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.21154>
- **Code:** <https://github.com/Future-House/aviary>

## Summary

Aviary formalizes language agents as policies acting in language-grounded partially observable Markov decision processes and provides an extensible gymnasium of environments in which to run them. It implements five environments, including three challenging scientific environments focused on DNA construct manipulation (molecular cloning), answering research questions via scientific-literature access, and protein-stability engineering, all emphasizing multi-step reasoning relevant to contemporary biology research. The paper reports that language agents backed by open-source, non-frontier LLMs can match and exceed both frontier LLM agents and human experts on multiple tasks at up to 100× lower inference cost.

## Tasks

Five environments, three of them scientific: DNA construct manipulation / molecular cloning, scientific-literature research question answering, and protein (stability) engineering. Exact environment names, task counts, and the two non-scientific environments: TODO(reference) — not specified in the abstract.

## Domains

Scientific task environments in molecular biology (molecular cloning, protein engineering) and scientific-literature research, alongside two non-scientific environments (unspecified in the abstract).

## Evaluation

- Agents act as policies in language-grounded POMDP environments; performance is measured per environment on task success.
- Exact metrics and per-environment task counts: TODO(reference) — not stated in the abstract.
- Reported: open-source, non-frontier-LLM agents match or exceed frontier LLM agents and human experts on multiple tasks at up to 100× lower inference cost.

## Typical Duration

Multi-step reasoning episodes per environment. Per-task step/time budget: TODO(reference) — not stated in the abstract.

## Main Contribution

The paper's stated contribution is Aviary as a gymnasium for language agents plus training/inference-time-compute methods that let small-model agents rival frontier agents and human experts. Within this repository, the in-scope contribution is Aviary's scientific environments as reusable evaluation environments.

## Key Design Ideas

- Agents formalized as policies over language-grounded partially observable MDPs.
- An extensible gymnasium hosting multiple environments under one abstraction.
- Three scientific environments (molecular cloning, literature research, protein engineering) emphasizing multi-step reasoning.
- Demonstrates a strong cost-performance trade-off (up to 100× lower inference cost) via online training and inference-time-compute scaling.

## Strengths

- Provides reusable, extensible scientific task environments under a common agent abstraction.
- Scientific environments are grounded in contemporary biology research problems.
- Reports a striking cost-performance result that reframes the frontier-vs-open-source comparison.

## Limitations

- Repository note: The paper's primary framing is *training* language agents (online training, inference-time-compute scaling) — agent-construction work outside this repository's evaluation-centric scope. It is included for Aviary's scientific environments as evaluation environments, not for the training method.
- Repository note: Exact environment names, task counts, and per-environment evaluation metrics are not stated in the abstract and are marked `TODO(reference)` pending verification from the paper or code.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also evaluates agents on scientific tasks, but as a fixed benchmark of expert-validated tasks rather than an extensible training-and-evaluation gymnasium.
- [SciAgentArena](./sciagentarena.md) — Also an interactive scientific-research environment for agents, with stepwise verification across scales.
