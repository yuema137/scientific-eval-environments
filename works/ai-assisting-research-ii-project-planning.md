# AI's Capability in Assisting Scientific Research in Physics, Astrophysics and Cosmology II: Project Planning and Proposal Evaluation (2026)

> **English** | [简体中文](../zh/works/ai-assisting-research-ii-project-planning.md)

> **First appeared:** 2026-07-28 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.25881)

## Overview

A blind comparison of human-written and LLM-written research project proposals for eight real physics, astrophysics and cosmology projects, scored by four human reviewers and two frontier LLM reviewers against a shared four-aspect rubric, which also measures whether reviewers can tell the two apart and how strongly LLM judges favour LLM-written text.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.25881>
- **Venue:** arXiv preprint (July 2026), cs.CL with astrophysics cross-lists

## Summary

Using the same eight expert-designed projects as the companion literature-review study, the authors gave each project's title, background and goal to one human domain expert and to three LLMs, each of which produced a one-page project proposal on an identical template. The resulting 32 proposals (8 human, 24 AI) were anonymized and uniformly formatted, then given to four faculty or senior-postdoc reviewers and to two frontier LLM reviewers, who each performed two tasks: guess whether the proposal was human- or AI-written, and score it 1–5 on four rubric aspects. Human reviewers rated human and AI proposals about equally overall, while both LLM reviewers scored AI-written proposals roughly one full point higher — a self-preference effect absent from the human panel. Where AI proposals did win with human reviewers, it was concentrated on the projects where the human author had invested least effort, an anti-correlation the authors quantify at r ≈ −0.95.

## Tasks

32 one-page research project proposals over eight projects — AGN duty cycle with MaNGA, the Lyman-break-galaxy dark-matter-halo connection, intrinsic alignments, laser-ablation debris prediction, radio galaxies with HalfDome, the environment of gravitational-wave black-hole binaries, pulsar-timing-array sensitivity forecasting, and massive Yang–Mills theory. For each project one human expert and three LLMs each wrote one proposal from the same expert-supplied title, background and goal, following an identical structural template. Each of the six reviewers assessed all 32 proposals.

## Domains

Astronomy and astrophysics dominates: six of the eight projects are astrophysical or cosmological, covering AGN and galaxy evolution, large-scale structure, weak lensing, CMB foregrounds, gravitational-wave source environments, and pulsar timing arrays — and the proposals must plan real observational or survey analyses using named datasets and instruments. Physics is a co-domain through the massive Yang–Mills project and the laser-ablation instrumentation project.

## Evaluation

Blind rubric review by two reviewer populations. Proposals were anonymized, uniformly formatted and stripped of authorship cues. Each reviewer scored every proposal 1–5 (Poor to Excellent) on four aspects: **clarity and structure** (a clear logical sequence structured into coherent phases, down to chaotic or missing); **appropriateness of methods** (well-justified and state-of-the-art, down to incorrect or unworkable); **resource and tool planning** (specifies required datasets and software with precision, down to no mention of data or tools); and **feasibility, timeline and risk awareness** (realistic and well-paced with risks addressed, down to an infeasible timeline or no plan). Reviewers also made a binary human-versus-AI authorship judgment on each proposal. Human panel: four faculty or senior postdocs. AI panel: Claude Opus 4.8 and ChatGPT Pro 5.5, with supplementary runs using Codex 5.5 Pro and Claude Sonnet 4.6.

- **Reported (mean total score, human reviewers / Claude Opus 4.8 / ChatGPT Pro 5.5):** ChatGPT-written 3.25 ± 0.47 / 4.63 ± 0.52 / 4.66 ± 0.39; Claude-written 3.52 ± 0.43 / 4.25 ± 0.54 / 4.16 ± 0.42; DeepSeek-written 3.74 ± 0.52 / 4.53 ± 0.25 / 4.41 ± 0.39; human-written 3.52 ± 0.59 / 3.59 ± 0.61 / 3.47 ± 0.50.
- **Reported (authorship identification):** human reviewers 79% correct on AI-written and 72% on human-written proposals; both AI reviewers 100% correct on all proposals.
- **Reported (project-level):** human-written proposals scored higher on 5 of 8 projects, with the AI advantage concentrated where human effort was weakest (r ≈ −0.95).

## Typical Duration

One proposal-generation pass per project per system, with default tool access enabled; one review pass per reviewer over all 32 proposals. No wall-clock or token budgets are stated in the primary source. TODO(reference).

## Main Contribution

A controlled, rubric-based measurement of LLM research-planning quality against expert human proposals on real frontier projects, jointly with a direct measurement of LLM-as-judge self-preference — showing that human and AI reviewers agree on ranking human work but diverge by about a full rubric point on AI work.

## Key Design Ideas

- Hold the scientific problem fixed: every proposal starts from the same expert-written title, background and goal, so the comparison isolates planning quality from idea selection.
- Impose an identical one-page template on all authors, human and machine, removing format as a confound.
- Score with an explicit four-aspect, five-point rubric with written anchors at each level, published in the paper.
- Run the same rubric past both a human panel and an LLM panel, making judge-population bias directly measurable rather than assumed.
- Add an authorship-identification task, which turns "can you tell it is AI?" into a number and contextualizes the score gap.
- Correlate the human-versus-AI score margin with per-project human effort, exposing effort as the main driver of when AI proposals win.

## Strengths

- The rubric is published with level-by-level anchors, so the scoring protocol is reusable.
- Reviewers are genuine domain seniors (faculty and senior postdocs) and every reviewer sees every proposal, giving a fully crossed design.
- The parallel human and AI review panels turn LLM-judge self-preference into a measured effect within the same study, not a separate claim.
- Reporting per-project variation, rather than only pooled means, surfaces the effort anti-correlation that a single average would hide.

## Limitations

- Eight projects and 32 proposals is a small sample; the authors attribute the limit to coordination cost.
- Proposal writers are mid-2025 models the authors describe as already outdated at submission, while the AI reviewers are mid-2026 models — the generation and review conditions are not version-matched.
- Only one human proposal per project, so human variance is unestimated, and human effort was not controlled.
- The study evaluates methodology and planning quality explicitly, not the novelty of the underlying ideas.
- One-page proposals only; the authors flag full-length proposals, multi-round review and explicit novelty assessment as future work.
- No dataset or code release is stated in the primary source.
- Repository note: this is an evaluation study with a published rubric rather than a reusable named benchmark artifact; re-running it requires re-recruiting expert reviewers.

## Related Works

- [AI's Capability in Assisting Scientific Research I: Literature Review](./ai-assisting-research-i-literature-review.md) — the companion paper, evaluating literature search on the same eight projects.
- [IdeaBench](./ideabench.md) — also evaluates LLM research-idea quality, with automated LLM-based ranking rather than an expert review panel.
- [LiveIdeaBench](./liveideabench.md) — also scores generated scientific ideas on a multi-dimensional rubric, via an LLM panel across many domains.
- [ReplicationBench](./replicationbench.md) — also measures AI against expert astrophysics research practice, on replication rather than planning.
