# ScienceBoard (2025)

> **English** | [简体中文](../zh/works/scienceboard.md)

> **First appeared:** 2025-05-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.19897)

## Overview

ScienceBoard is a computer-use agent benchmark that places multimodal agents inside a real Ubuntu desktop
running professional scientific applications and scores them on 169 human-curated workflow tasks spanning
six scientific domains, including astronomy via the Celestia planetarium software.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2505.19897
- **Code:** https://github.com/OS-Copilot/ScienceBoard
- **Project:** https://qiushisun.github.io/ScienceBoard-Home/
- **Venue:** ICLR 2026

## Summary

ScienceBoard builds a realistic, executable environment in which agents drive genuine scientific desktop
software through GUI interaction, command-line interaction, or a mix of both, with an HTTP server exposing
internal application state so that outcomes can be checked programmatically. Six applications instantiate six
domains: UCSF ChimeraX (biochemistry), KAlgebra (algebra), Lean 4 (theorem proving), GRASS GIS
(geographic information systems), Celestia (astronomy), and TeXstudio (scientific documentation). The
benchmark's stated purpose is to measure whether current multimodal agents can carry out end-to-end
scientific workflows rather than isolated question answering, and the reported results are low across the
board.

## Tasks

169 human-curated real-world tasks. By interaction modality the split is 38 GUI-only tasks (22.5%), 33
CLI-only tasks (19.5%), and 98 hybrid GUI+CLI tasks (58.0%). By difficulty the split is easy 53.8%, medium
28.4%, hard 16.6%, and open problems 1.2% (2 tasks). Tasks were built through an annotation pipeline in
which annotators first learned each application from its documentation, curated candidate tasks with an
assigned difficulty, standardised the wording, and wrote configuration functions that initialise the virtual
machine; cross-validation was performed by having each task executed by two randomly selected annotators.
The number of tasks assigned specifically to the astronomy (Celestia) environment is `TODO(reference)` — the
paper and project page report the 169-task total and per-domain results but do not publish a per-application
task count.

## Domains

Astronomy is one of the six evaluated domains, instantiated by the Celestia planetarium application, where
the paper describes tasks that require temporal-spatial awareness of real astronomical scenarios and reports
astronomy as one of the weakest domains for every evaluated agent. Co-domains follow directly from the other
five applications: Biology (structural/molecular work in UCSF ChimeraX), Mathematics (KAlgebra computer
algebra and Lean 4 theorem proving), and Earth Science (GRASS GIS geospatial analysis). The TeXstudio
scientific-documentation environment is domain-neutral.

## Evaluation

Each task is scored by inspecting both the correctness of key intermediate input/output during the workflow
and the final state of the virtual machine, using evaluation templates that support exact matching,
range-based assessment, and numerical tolerance. Task outcome is binary (success or failure) and the headline
metric is success rate, reported overall and per domain. An episode ends when the agent emits a `DONE` or
`FAIL` signal or reaches the predefined attempt limit. In the current version the best overall result is GPT-5
at 24.20% in the screenshot + accessibility-tree observation setting, followed by Gemini-2.5-Pro at 16.98% and
Claude-3.7-Sonnet at 15.79%; open-source backbones average below 12%. Per-domain results place biochemistry
and algebra highest (up to 62.07% for GPT-5) and GIS and astronomy lowest.

## Typical Duration

Reported averages are 9.0 steps and 124 seconds of wall-clock time per task. The paper states that rollouts
terminate at a predefined attempt limit but does not give the numeric cap; the exact maximum step budget is
`TODO(reference)`.

## Main Contribution

The authors frame ScienceBoard as the first benchmark to evaluate multimodal autonomous agents inside
realistic, executable scientific workflows in professional software, rather than on static question-answer
pairs, and use it to show that state-of-the-art agents remain unreliable assistants for scientific work.

## Key Design Ideas

- A single Ubuntu virtual machine hosting six real scientific applications, with each application modified to
  expose internal state over HTTP for programmatic verification.
- Dual interaction channels — GUI control and application CLI — with most tasks deliberately requiring both.
- Outcome checking that combines intermediate I/O correctness with final VM state, not just a final answer
  string.
- An observation-setting ablation (screenshot only, accessibility tree, screenshot + accessibility tree) to
  isolate how much perception modality contributes to agent success.
- An annotation protocol with documentation-based annotator training and two-annotator cross-execution of
  every task.

## Strengths

- Real professional software in a real desktop environment, so success requires operating the tools
  scientists actually use rather than answering about them.
- Six genuinely distinct domains inside one harness, which makes cross-domain difficulty directly comparable
  under a shared protocol.
- State-based verification rather than text matching, which is robust to differences in how an agent phrases
  its result.
- Open release: code under MIT license, plus a published virtual-machine snapshot, so the environment is
  reproducible.

## Limitations

- Per-application task counts are not published, so the size of the astronomy slice cannot be verified from
  the paper or project page.
- Success is binary with no partial credit, so an agent that completes most of a long workflow scores the
  same as one that fails immediately.
- Task difficulty skews easy (53.8%) with only 2 open problems, so headroom at the hard end is thin.
- Repository note: with an average of 9.0 steps per task, the environment tests realistic tool operation more
  than long-horizon planning; it is not a long-horizon benchmark in the sense of multi-hour research
  trajectories.

## Related Works

- [OSWorld](./osworld.md) — the general computer-use environment whose VM-and-state-verification design
  ScienceBoard adapts to scientific applications.
- [ScienceAgentBench](./scienceagentbench.md) — code-centric scientific agent tasks, contrasted with
  ScienceBoard's GUI-plus-CLI desktop setting.
- [Terminal-Bench Science](./terminal-bench-science.md) — another multi-domain scientific agent suite that
  reaches astronomy through a domain track.
- [SciVisAgentBench](./scivisagentbench.md) — evaluates agents driving scientific visualization software, a
  closely related tool-operation setting.
