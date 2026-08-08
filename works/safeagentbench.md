# SafeAgentBench (2024)

> **English** | [简体中文](../zh/works/safeagentbench.md)

## Overview

SafeAgentBench evaluates whether embodied LLM agents plan safely: 750 executable tasks covering 10 potential hazards and 3 task types, run in SafeAgentEnv — a universal embodied environment with a low-level controller and 17 high-level actions — where the most safety-conscious baseline rejects only 10% of detailed hazardous tasks.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.13178>
- **Code:** <https://github.com/shengyin1224/SafeAgentBench>
- **Dataset:** <https://huggingface.co/datasets/safeagentbench/SafeAgentBench>
- **Venue:** arXiv preprint (cs.CR), 2024

## Summary

An embodied agent that dutifully executes "heat the towel on the stove" is a hazard, not a helper. SafeAgentBench pairs hazardous and safe task variants — 750 tasks rigorously curated over 10 hazard categories and 3 task types — and executes plans in SafeAgentEnv with multi-agent support and 9 state-of-the-art baselines. Evaluation covers both execution and semantic perspectives. The findings are stark: the most safety-conscious baseline rejects only 10% of detailed hazardous tasks, and swapping the underlying LLM does not notably improve safety awareness.

## Tasks

750 executable embodied tasks (hazardous and safe; 10 hazard types, 3 task types) planned and executed in SafeAgentEnv over 17 high-level actions with a low-level controller. Interactive; simulation only.

## Domains

Embodied household simulation — outside the repository's science/engineering domain axis; documented for its safety-evaluation methodology.

## Evaluation

- Execution-perspective and semantic-perspective evaluation; task success rate and rejection rate as core metrics.
- **Reported.** Best baseline: only 10% rejection rate on detailed hazardous tasks; replacing the driving LLM yields no notable safety improvement.

## Typical Duration

Single planning-and-execution episodes per task.

## Main Contribution

Quantifying the safety-awareness gap of embodied LLM agents with executable (not hypothetical) hazards — and showing the gap is architectural, not fixed by model choice.

## Key Design Ideas

- Hazardous/safe task pairing separates refusal calibration from task competence.
- Executable hazards ground safety evaluation in what the agent actually does, not what it says.
- Dual execution/semantic evaluation catches both unsafe actions and unsafe intent.

## Strengths

- The reference hazard taxonomy for embodied LLM safety, with environment and dataset public.
- The model-swap negative result redirects safety effort from model selection to system design.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); no venue is verifiable from those sources. The repository README reports older baseline figures (69% safe-task success, 5% rejection) that differ from the current abstract; the abstract's numbers are treated as canonical.
- Simulation-only hazards; physical-world risk transfer is not evaluated.

## Related Works

- [BadRobot](./badrobot.md) — Also embodied LLM safety, from the attacker's side via jailbreaking into physical actions.
- [ASIMOV](./asimov.md) — Also robot safety evaluation, at the semantic-desirability level with constitutions.
- [EmbodiedBench](./embodiedbench.md) — Also multi-baseline embodied LLM evaluation, on capability rather than safety.
