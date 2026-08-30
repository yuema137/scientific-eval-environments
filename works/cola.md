# CoLA: Controlling Large Language Model with Latent Action (2025)

> **English** | [简体中文](../zh/works/cola.md)

## Overview

CoLA learns a compact latent action space for controlling an LLM, separating the policy's decision representation from the model's token vocabulary.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — general LLM and agent adaptation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://proceedings.mlr.press/v267/jia25e.html>
- **Model:** <https://huggingface.co/LAMDA-RL/Llama-3.1-CoLA-10B>
- **Venue:** ICML 2025

## Summary

CoLA uses an inverse-dynamics model conditioned on future tokens to extract latent actions, fine-tunes the LLM as an action-conditioned language world model, and trains a policy over the learned action space by behavior cloning or reinforcement learning. Experiments cover mathematics, preference control, ALFWorld, and ScienceWorld, including seen and unseen agent tasks.

## Tasks

Mathematical reasoning and search, controllable preference generation, and multi-turn interaction in ALFWorld and ScienceWorld.

## Domains

General language-model control and embodied/text-agent environments; not mapped to a canonical science domain because ScienceWorld is used as a simulated agent task rather than a scientific workflow.

## Evaluation

Math benchmark accuracy and pass@K, GPT-4 preference win rate, reward-hacking stress tests, and success on seen and unseen ALFWorld and ScienceWorld tasks. The paper reports 42.4 on MATH-500 for its RL setting and improved unseen-task agent performance over the base model.

## Typical Duration

No fixed wall-clock or per-episode duration is reported across the heterogeneous tasks.

## Main Contribution

A learned alternative to hand-authored action abstraction that makes the structure of an LLM's RL action space itself an optimization target.

## Key Design Ideas

- Infer actions from future-token-conditioned inverse dynamics.
- Separate a latent-action policy from an action-conditioned language world model.

## Strengths

- Tests the representation across reasoning, preference, and interactive agent settings.
- Includes seen/unseen task splits and reward-hacking probes.

## Limitations

- Latent actions are less directly interpretable than named semantic actions.
- Better downstream performance does not establish that the learned dimensions correspond to reusable human-level strategies.
- Comparisons do not hold every training and architectural choice fixed while changing only action granularity.

## Related Works

- [MA-RLHF](./ma-rlhf.md) — constructs macro-actions from token groups.
- [MetaAct-RL](./metaact-rl.md) — uses explicit named reasoning actions.
