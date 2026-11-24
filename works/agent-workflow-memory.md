# Agent Workflow Memory (2024)

> **English** | [简体中文](../zh/works/agent-workflow-memory.md)

> **First appeared:** 2024-09-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2409.07429)

## Overview

Agent Workflow Memory (AWM) extracts reusable sub-routines ("workflows") from a web agent's past trajectories and adds them to the agent's memory to guide later tasks. A web agent without it solves each task from scratch. AWM adds an induction step: an LM abstracts common sub-routines out of solved examples, replacing example-specific values with placeholders. In the online setting, which trajectories feed that step is decided by an LM-based evaluator that labels each of the agent's own test-time trajectories as success or failure; only predicted successes become workflows. The paper measures the effect on WebArena and Mind2Web, including cross-website and cross-domain splits.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities


N/A — Workflow-memory method evaluated on general web navigation (WebArena, Mind2Web); no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2409.07429>
- **Code:** <https://github.com/zorazrw/agent-workflow-memory>
- **Venue:** ICML 2025, PMLR 267:63897–63911 (<https://proceedings.mlr.press/v267/wang25bx.html>)

## Summary

A workflow is a textual description plus a sequence of steps, each giving an environment-state description, the agent's reasoning, and an executable action. In the offline setting, workflows are induced once from annotated training examples and a fixed memory serves all test tasks. In the online setting, the agent processes test queries in a stream; after each task, the LM-based evaluation model of Pan et al. (2024) assigns a binary success label, and a predicted success is converted into workflows that are added to memory before the next query. Workflows can build on earlier ones: a "find a place by its name" workflow becomes a sub-goal inside a later "get the zip code of a place" workflow. Because selection depends on a model evaluator, wrongly accepted trajectories can produce incorrect workflows, a point the paper notes.

## Tasks

N/A — method paper; it introduces no new task suite. Experiments use WebArena (812 tasks across shopping, CMS, Reddit, GitLab, and maps websites, plus a 197-example cross-template subset) and Mind2Web (cross-task, cross-website, and cross-domain test splits; split sizes `TODO(reference)`). The abstract describes the two benchmarks together as over 1,000 tasks from more than 200 domains.

## Domains

General web navigation (shopping, content management, forums, code hosting, maps, and other websites); no canonical science or engineering domain is evaluated.

## Evaluation

On WebArena, one task is run until the model predicts a stop action or reaches a pre-set step maximum, and WebArena's execution-based checker decides success; the paper reports success rate and number of steps. AWM's online workflow selection uses the LM evaluator, but the reported scores use the benchmark checker. On Mind2Web, predictions are scored by element accuracy, action F1, step success rate, and task success rate.

Reported results:

- **WebArena (GPT-4, gpt-4-0613):** total success rate 35.5 (Shopping 30.8, CMS 29.1, Reddit 50.9, GitLab 31.8, Maps 43.3), against SteP 33.0, BrowserGym 23.5, AutoEval 20.2, and the WebArena baseline 14.9. The paper reports a 51.1% relative gain over BrowserGym and about 2.0 fewer steps.
- **Mind2Web cross-task (GPT-4):** offline AWM 50.6 element accuracy, 57.3 action F1, 45.1 step SR, 4.8 SR; MindAct step SR 36.2 (24.6% relative gain). Online AWM: 50.0 / 56.4 / 43.6 / 4.0.
- **Generalization (step SR over MindAct):** online AWM +7.4 cross-task, +3.8 cross-website, +16.9 cross-domain; offline AWM +14.0 cross-domain.

Ablations: rule-based versus LM-based induction (WebArena SR 35.6 versus 35.5; Mind2Web cross-task step SR 43.4 versus 45.1); text versus code workflows (step SR 45.4 versus 45.1; SR 3.6 versus 4.8); workflows exposed as callable actions (AWM-AS: step SR 46.4, agents called workflow actions in 18.5% of tasks).

## Typical Duration

WebArena episodes end at a stop action or a pre-set step maximum (value `TODO(reference)`); Mind2Web tasks have a fixed number of steps per task.

## Main Contribution

A method for inducing reusable, composable workflows from agent experience, usable offline from training data or online from the agent's own test-time trajectories filtered by an automatic evaluator.

## Key Design Ideas

- Abstract example-specific values into placeholders (for example, `{product-name}`) so a workflow applies across tasks.
- Target sub-task granularity (for example, "search for a product") rather than whole-task instructions.
- In the online setting, gate memory updates on an LM evaluator's binary success judgment.
- Let later workflows reuse earlier workflows as sub-goals.
- Compare workflow representations (text versus code; natural-language state descriptions versus filtered HTML) and use as context versus as callable actions.

## Strengths

- Evaluates both offline induction and online induction without ground-truth labels (paper).
- Tests generalization across tasks, websites, and domains on Mind2Web (paper).
- WebArena scores come from the benchmark's execution-based checker, independent of the evaluator used for workflow selection (paper).

## Limitations

- The paper notes that online AWM induces workflows from model-predicted trajectories that are not always correct.
- Workflows can push the agent toward actions that do not fit the current state, which lowered action F1 relative to MindAct in some settings (paper).
- Agents rarely called workflow actions (18.5% of tasks), and fixed workflow actions struggle with dynamic page changes such as pop-ups (paper).
- Repository note: the paper does not measure the accuracy of the LM evaluator or compare online induction under ground-truth labels.
- The paper's text and tables report slightly different values in places (for example, 7.9% versus 7.6% relative gain over SteP; AWM-AS SR 3.2 versus 3.6).

## Related Works

- [MACLA](./macla.md) — also stores reusable procedures from trajectories, selecting them by per-procedure Bayesian reliability instead of an evaluator gate on whole trajectories.
- [STAIR](./stair.md) — abstracts past coding-agent repairs into multi-level plans and compares abstraction levels.
- [Trace2Tower](./trace2tower.md) — induces a three-level skill hierarchy from trajectories using success and failure evidence.
- [SkillEvolBench](./skillevolbench.md) — benchmarks whether agents can distil episodic trajectories into reusable skills.
