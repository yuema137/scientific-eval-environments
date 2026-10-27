# EmbodiedCLBench (2026)

> **English** | [简体中文](../zh/works/embodiedclbench.md)

> **First appeared:** 2026-10-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.13021)

## Overview

EmbodiedCLBench tests whether an embodied agent can learn from basic household tasks and recombine what it learned on unseen, more complex ones. Agents first attempt basic tasks, then face an advanced task that composes skills from two to four basic-task categories. The benchmark compares no prior experience, full earlier trajectories kept in context, and a written skill summary distilled from them. Advanced-task success is 3–12% zero-shot and 16–52% with either form of experience, but adding more learning samples beyond one brings no consistent further gain.

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — general embodied household-task benchmark; the evaluated agents perform household object manipulation in simulation, not a scientific or research activity.

## Links

- **Paper:** [EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://arxiv.org/abs/2610.13021), 2026 preprint (Peking University, BIGAI, University of Hong Kong).
- **Full text:** <https://arxiv.org/html/2610.13021v1>
- **Code:** <https://github.com/PKU-VaLuE-Lab/EmbodiedCLBench> (the README states no license)
- **Data:** <https://huggingface.co/datasets/PKU-VaLuE-Lab/EmbodiedCLBench>
- **Project:** <https://pku-value-lab.github.io/EmbodiedCLBench-homepage>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Tasks come from indoor household scenes in the closed-source version of the TongSim simulator, chosen for its wider action set. Because online simulation of that version is not practical for evaluation, each task is turned into a pre-built state-transition graph: every node pairs a first-person image with four candidate actions, which are optimal, suboptimal (an executable detour), or invalid. The agent observes the current image and picks one action per step. A task succeeds when the agent reaches the goal node within the step budget, its shortest path plus 3 extra steps at test time (6 during learning). In the In-Context Learning (ICL) setting, the agent first completes two related basic tasks and keeps the full interaction history in context. In the Skill Learning setting, it writes a concise Markdown skill summary after the same basic tasks, and only that summary is available at test time.

## Tasks

268 tasks: 168 basic and 100 advanced. Basic tasks fall into six categories: Object Manipulation, Spatial Placement, Accessibility Control, Appliance Operation, Activity-Driven Scene Configuration, and Household State Restoration. A basic task combines 2 atomic actions (a 6-step shortest path); an advanced task combines 4 atomic actions (12 steps) drawn from 2 to 4 basic-task categories. Atomic actions are discrete primitives such as walk to, look at, pick up, put down, open, close, and switch on. An LLM (Qwen3.7-Plus) generated task descriptions and per-state action options in a three-stage pipeline, breadth-first search found shortest paths, and a sample was kept only if three annotators independently approved its images, descriptions, and options.

## Domains

Embodied household simulation (TongSim), solved by choosing among discrete high-level actions; outside the repository's science/engineering domain axis, and the paper evaluates no robot platform or robot control.

## Evaluation

- **Metric:** Success Rate (SR), the fraction of tasks that reach the goal node within the step budget. Action-selection rates (optimal, suboptimal, invalid) are analyzed separately. No LLM or VLM judge is used.
- **Systems:** Qwen3.8-Flash and GPT5.6-Terra, each in four harnesses (Hermes, OpenClaw, Codex, Claude Code): eight configurations.
- **Results (Table 1, SR %):** basic tasks zero-shot 42.9–58.9. Advanced tasks zero-shot 3.0–12.0, with ICL 16.0–52.0, with Skill Learning 22.0–38.0. Highest with experience: Codex with GPT5.6-Terra under ICL, 52.0; OpenClaw with Qwen3.8-Flash under Skill Learning, 38.0. Neither setting is consistently better: ICL leads in five of the eight configurations and Skill Learning in three.
- **Complexity (Hermes, Qwen3.8-Flash, 3 to 6 atomic actions):** zero-shot SR falls from 28.0% to 4.0%; ICL falls from 72.0% at 3 actions to 42.0% at 4 and is 32.0% at 6, where Skill Learning is 26.0%.
- **Learning samples:** going from 0 to 1 learning sample raises SR from 8.0–10.0% to 28.0–40.0%; from 1 to 6 samples there is no consistent upward trend (Hermes and OpenClaw with Qwen3.8-Flash).
- **Step budget:** with no extra steps, SR is 0.0% zero-shot, 15.0% with ICL, and 7.0% with Skill Learning.
- **Action selection:** relative to zero-shot, experience lowers invalid-action selection by 13–20% and raises suboptimal-action selection by 3–8%; shifts under Skill Learning are smaller.

## Typical Duration

Basic tasks have 6-step and advanced tasks 12-step shortest paths, with a test budget of 3 extra steps. Token counts, dollar costs, and wall-clock time are not reported.

## Main Contribution

Measures continual learning in an embodied setting as transfer from basic tasks to unseen compositions of them, and compares raw trajectories with distilled skill summaries as the carrier of experience.

## Key Design Ideas

- Build advanced tasks by composing atomic actions from several basic-task categories, so that success requires recombining skills rather than repeating one.
- Hold the learning tasks fixed and vary only what the agent keeps (nothing, the full trajectory, or a written skill summary).
- Pre-compute state graphs with explicit optimal, suboptimal, and invalid options, so that both success and the quality of each action choice can be scored deterministically.

## Strengths

- The same eight model–harness configurations are evaluated in all four settings, so the gain from experience can be read per configuration.
- Every sample passed independent checks by three annotators.
- Complexity, number of learning samples, and step budget are each varied in separate experiments.

## Limitations

- Evaluation is offline over pre-built graphs with four candidate actions per state, so the agent selects actions rather than generating them and cannot leave the graph.
- Only two backbone models are evaluated.
- The paper states that ICL and Skill Learning raise advanced-task success "from around 10% to above 30%"; five of the sixteen experience cells in Table 1 are below 30% (for example Hermes with GPT5.6-Terra under ICL, 16.0%).
- Repository note: the paper reports no repeated runs or variance, and the complexity and learning-sample experiments use one harness or two.

## Related Works

- [EmbodiedBench](./embodiedbench.md) — Embodied agents across high-level and atomic action levels, evaluated without a learning phase.
- [SkillEvolBench](./skillevolbench.md) — Also compares learned skills with raw trajectory reuse, on non-embodied tasks.
- [PhysRSI-eval](./physrsi-eval.md) — Also measures improvement from earlier attempts, with full physical rounds on simulated robot manipulation.
