# The Tool Decathlon / Toolathlon (2025)

> **English** | [简体中文](../zh/works/toolathlon.md)

## Overview

The Tool Decathlon (Toolathlon) is a benchmark for language agents on diverse, realistic, long-horizon task execution: 108 tasks spanning 32 real software applications and 604 tools, with realistic initial environment states and strictly verifiable, state-based evaluation scripts.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.25726>
- **Project:** <https://toolathlon.xyz/>
- **Code:** <https://github.com/hkust-nlp/toolathlon>
- **Venue:** ICLR 2026

## Summary

Toolathlon targets the gap between narrow or simplified tool-use benchmarks and real-world workflows that switch across many applications. Tools are sourced from a curated set of 32 Model Context Protocol (MCP) servers — revised or implemented by the authors — plus 7 local toolkits, covering everyday platforms (Google Calendar, Notion, Gmail) and professional ones (Snowflake, Kubernetes, WooCommerce, BigQuery). Unlike prior work that ensures functional realism but limited environment-state diversity, environments are initialized with realistic states from real software (e.g., a Canvas course with dozens of students, real financial spreadsheets), combining remote applications with locally containerized open-source replacements (Poste.io for email, Canvas, Kubernetes, WooCommerce). Task instructions are deliberately fuzzy to mirror authentic user requests, but the intent is deterministically inferable from environment states.

## Tasks

108 manually sourced or crafted tasks across seven categories (Research, Campus, Finance, Tech, Business, Daily, E-commerce), requiring interaction with multiple applications over around 20 turns on average. Per-task tool exposure averages 69.9 tools (min 28, max 128); 72 of 108 tasks (67%) begin from an initialized environment state. Tasks were sourced by the authors under three principles — real user demands, multi-app orchestration, and two-stage diversity-driven sourcing — with implementation taking 4–6 hours of graduate-student work per task and quality-check rounds of about 5 hours of labor per task by 5–6 experienced authors.

## Domains

General-purpose software workflows: education/course management, finance, e-commerce, cluster and database operations, email and calendar coordination, research and daily productivity.

## Evaluation

- Each task has a unique, manually crafted, deterministic evaluation script that directly checks the final environment state — either robust matching against a static ground-truth snapshot or a reference execution workflow that dynamically retrieves real-time information (e.g., current NVIDIA shareholder data). The paper explicitly argues for state-based deterministic evaluation over LLM-as-judge scoring of trajectories.
- Each task exposes only the necessary MCP servers (fewer than 10), but all tools within each selected server are loaded, so agents must ignore distractor tools; the maximum allowed interaction is 100 turns.
- Metrics: pass@1 averaged over three runs (with standard deviation), pass@3, pass^3 (all three trajectories correct), and average number of turns.
- Execution and evaluation are isolated in separate containers, supporting parallel evaluation — a full 108-task run of Claude-4.5-Sonnet takes about 70 minutes with 10 parallel processes.
- Reported results: the best model, Claude-4.5-Sonnet, reaches 38.6% ± 2.7 pass@1 (51.9 pass@3, 20.4 pass^3) at 20.2 average turns; the best open-weights model, DeepSeek-V3.2-Exp, reaches 20.1% ± 1.2. Increased reasoning effort shows no benefit (GPT-5 vs. GPT-5-high), and 15–35% of trajectories encounter overlong tool outputs, which degrade most models' success rates.

## Typical Duration

Multi-turn tool-calling workflows of roughly 20 turns on average (up to a 100-turn cap); task difficulty groups by average execution turns span roughly 4 to 53 turns.

## Main Contribution

A language-agent benchmark that jointly delivers application diversity (32 apps / 604 tools), realistic environment-state initialization from real software, fuzzy but deterministically verifiable task instructions, and reliable execution-based evaluation — a combination the paper's comparison table shows no prior tool-use benchmark provides.

## Key Design Ideas

- Tools sourced from real MCP servers, curated and repaired by the authors, rather than mock implementations or simulated APIs.
- Realistic initial environment states, set up scalably by containerizing open-source counterparts of remote services (Poste.io for Gmail, WooCommerce for Shopify).
- Fuzzy task instructions that mimic authentic user requests while keeping the true intent deterministically inferable from environment state.
- State-based deterministic evaluation scripts per task, with dynamic ground-truth generation for tasks involving real-time information.
- POMDP task formulation with per-task tool configuration that includes distractor tools within each exposed MCP server.

## Strengths

- Combines diversity, realistic environment states, verifiable execution, cross-app tasks, and fuzzy prompts — dimensions the paper tabulates against 14 prior tool-use benchmarks.
- Deterministic, reproducible scoring with no LLM judge, including for tasks grounded in live real-world data.
- Substantial headroom: the best model stays below 40% pass@1, and the pass@3 / pass^3 gap exposes reliability (consistency) as a separate weakness.
- Fully open-sourced benchmark and environment; parallel containerized evaluation is fast enough for developer feedback loops.

## Limitations

- Repository note: The paper's own difficulty analysis finds no significant gap between its Medium and Hard turn-count groups, and attributes failures partly to premature task-ending rather than horizon length per se — success is driven by exploration of observations, tool-call error handling, and long-context management.
- Repository note: Average-turn statistics are measured using a single model (Claude-4-Sonnet) as a complexity proxy, so horizon estimates are model-dependent.

## Related Works

- [Gaia2](./gaia2.md) — Also scores agents in realistic multi-app environments with write-action verification, but in a simulated smartphone universe rather than real software applications.
- [AgentBench](./agentbench.md) — Earlier multi-environment agent evaluation under one harness; Toolathlon replaces distinct benchmark environments with real applications exposed through MCP tools.
