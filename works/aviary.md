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

Five environments — two non-scientific (**GSM8K** grade-school math; **HotpotQA** multi-hop Wikipedia QA) and three scientific: **SeqQA / molecular cloning** (DNA-construct manipulation; 500 train / ~140 test questions), **LitQA2 / PaperQA** (answering research questions from the literature; 248 questions, 49 held-out test), and **Protein Stability** (proposing stabilizing mutations on 40 proteins from the megascale stability dataset).

## Domains

Molecular biology (molecular cloning, protein engineering) and scientific-literature research, alongside two non-scientific reasoning environments (GSM8K math, HotpotQA multi-hop QA).

## Evaluation

Agents act as policies in language-grounded POMDP environments; each environment supplies a terminal reward:

- **SeqQA & LitQA2** (multiple-choice): +1 correct, −1 incorrect, +0.1 for "unsure" — a sparse terminal reward; accuracy is the headline metric, with majority@k for multi-sample inference.
- **Protein Stability:** binary reward = 1 if the Rosetta ΔΔG of the proposed mutation < 0 (stabilizing), else 0; reported as a pass rate.
- **GSM8K:** +1 correct, −1 invalid tool call, 0 otherwise. **HotpotQA:** +1 correct, 0 otherwise.

Reported: a Llama-3.1-8B agent trained by expert iteration reaches 0.89 accuracy on SeqQA (majority voting; ≈0.86 single-sample), matching or exceeding Claude 3.5 Sonnet (≈0.87); on LitQA2 both exceed the prior best of 0.67, with Claude 3.5 Sonnet reaching 0.89 via majority voting. Cost: ≈$0.07 per Claude SeqQA trajectory vs. ≈$0.00066 for the Llama-8B agent (~100× cheaper), against $4–$12 per question for human PhD contractors.

## Typical Duration

Agents are rolled out for at most 10 steps per environment, except PaperQA / LitQA2, which allows up to 18 steps.

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
- Repository note: The released code has since diverged from the paper's five environments (the repo now packages GSM8K, HotpotQA, LFRQA, a Notebook environment, and LAB-Bench, with LitQA merged into LAB-Bench).

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also evaluates agents on scientific tasks, but as a fixed benchmark of expert-validated tasks rather than an extensible training-and-evaluation gymnasium.
- [SciAgentArena](./sciagentarena.md) — Also an interactive scientific-research environment for agents, with stepwise verification across scales.
