# SWE-chat (2026)

> **English** | [简体中文](../zh/works/swe-chat.md)

## Overview

SWE-chat is a large-scale, continually growing dataset of real human–coding-agent interactions collected from open-source developers in the wild, pairing complete session transcripts (prompts, tool calls, agent responses) with line-level human-vs.-agent code authorship attribution. It is a dataset and observational-analysis contribution, not a task-suite benchmark.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2604.20779>
- **Project:** <https://swe-chat.com>
- **Code:** <https://github.com/SALT-NLP/SWE-chat>

## Summary

SWE-chat collects coding-agent session transcripts from public GitHub repositories whose developers opt into Entire.io's CLI checkpoint logging, which links each checkpoint to a commit with line-level human-vs.-agent code attribution. The dataset covers sessions with five coding agents (Claude Code, OpenCode, Gemini CLI, Cursor, Factory AI Droid; ~85% from Claude Code) and is positioned as a living dataset whose collection pipeline continually discovers new sessions. On top of the raw traces, the paper contributes an empirical characterization of real-world usage and failure modes — coding modes, code survival, cost efficiency, security effects, and user pushback — framed as an empirical foundation for moving beyond curated benchmarks.

## Tasks

N/A — observational dataset, not an authored task suite. At time of writing the dataset contains ~6,000 coding sessions from 200+ public repositories, comprising 13,000+ checkpoints, 63,000+ user prompts, 355,000+ agent tool calls, and 2.7M logged events (including a small set of reasoning traces from 200 sessions with extended thinking).

## Domains

Real-world software engineering on open-source repositories, across diverse programming languages and task intents — understanding existing code is the most common specific user intent (19.0% of prompts), ahead of creating new code (13.4%), git operations (13.4%), and debugging (13.0%); about one third of all agent tool calls are bash commands.

## Evaluation

- **No agent leaderboard or scoring protocol** — trajectories are characterized rather than agents ranked. The paper defines a metric suite over real trajectories:
  - **Code survival rate and coding efficiency** — the fraction of agent-produced code that survives into user commits. Overall coding efficiency is 44.3% (survival rate 50.3%); vibe-coding sessions reach 59.0% / 64.6%.
  - **Cost, token, and time efficiency per committed line** — vibe-coding sessions consume a median of 204K tokens per 100 committed lines, roughly 3× collaborative sessions ($0.13 vs. $0.05 per 100 lines; $0.07 for human-only).
  - **Security effects** — Semgrep is run on pre- and post-commit snapshots; vibe-coded commits introduce 0.76 vulnerabilities per 1,000 committed lines, roughly 9× the human-only rate (0.08) and 5× the collaborative rate (0.14).
  - **LLM-judge annotations** — session success (0–100; mean 75.7, median 82, 90% of sessions rated 50+), user persona, prompt intent, and pushback categories, each validated against human gold labels with moderate-to-high inter-annotator agreement.
- **Key reported findings:** coding is bimodal — 40.8% of sessions are "vibe coding" (agent authors >99% of committed code) vs. 22.7% human-only and 36.5% collaborative; 55.8% of all committed lines are agent-written; users push back after 39% of turns and interrupt in 3.3–6.0%, while Claude Code asks a clarifying question in only 1.1–2.6% of turns.

## Typical Duration

Multi-turn sessions; most Claude Code turns are short — the median turn lasts under one minute and the 90th percentile stays below seven minutes, but the 99.9th-percentile turn duration exceeds 100 minutes, with a clear upward trend over the collection period.

## Main Contribution

The first large-scale dataset combining real user interactions with full coding-agent tool-call trajectories, code diffs, and line-level human-vs.-agent code authorship attribution — plus an initial empirical characterization of in-the-wild usage and failure modes intended as an evidence base beyond curated benchmarks.

## Key Design Ideas

- Opt-in git-hook logging (Entire.io CLI) ties every session transcript to real commits, so trajectory metrics are grounded in what users actually keep rather than in synthetic verifiers.
- Line-level authorship attribution separates agent-written, human-written, self-overwritten, and human-deleted code within each commit.
- A living-dataset pipeline continually ingests new sessions, enabling longitudinal analysis (e.g., the vibe-coding share doubled from 20% to over 40% during the three-month observation window).
- LLM-judge annotation rubrics (session success, persona, intent, pushback) are validated against human expert labels before being applied at scale.
- Privacy pipeline: PII redaction with named-entity recognition, credential removal, and IRB-exempt review of the study procedure.

## Strengths

- Captures the human-agent interaction dimension — prompting, steering, overriding, discarding — that curated benchmarks with fixed instructions do not model.
- Outcome grounding in real commits gives a usefulness signal (code survival) that no synthetic ground truth provides.
- Cross-agent coverage with detailed cost, token, and security accounting per coding mode.
- The authors position it as raw material for realistic benchmarks, adaptive interaction design, and user simulators trained on real trajectories.

## Limitations

- The authors note the population is early adopters of one open-source logging tool on public repositories — proprietary enterprise codebases are absent, a large fraction of data comes from Entire.io's own repository, and findings may not generalize.
- The authors note abandoned sessions are often never committed and thus invisible, likely overestimating session success and agent efficiency, while line-level attribution misses semantically surviving code (e.g., a user rewriting an agent suggestion elsewhere).
- The authors caution that LLM annotations are imperfect and should be further validated before downstream use, and that efficiency metrics are proxies that omit time users spend reviewing output.

## Related Works

- [SWE-bench](./swe-bench.md) — The curated GitHub-issue benchmark paradigm whose fixed, verifiable tasks SWE-chat explicitly contrasts with in-the-wild iterative usage.
- [AgentProcessBench](./agentprocessbench.md) — Also step/turn-level signal over multi-turn tool-use trajectories, but via expert annotation of curated trajectories rather than commit-grounded logs from real users.
- [Insights Generator](./insights-generator.md) — Corpus-level trace diagnostics that presuppose exactly the kind of large real-trajectory corpus SWE-chat provides.
