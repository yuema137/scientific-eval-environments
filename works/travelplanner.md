# TravelPlanner (2024)

> **English** | [简体中文](../zh/works/travelplanner.md)

## Overview

TravelPlanner is a real-world planning benchmark with 1,225 curated travel intents, a closed sandbox containing nearly four million records, and tools for constructing multi-day itineraries under environment, commonsense, and user constraints.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — general travel planning; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://proceedings.mlr.press/v235/xie24j.html>
- **Code:** <https://github.com/OSU-NLP-Group/TravelPlanner>
- **Venue:** ICML 2024

## Summary

TravelPlanner asks language agents to search a static sandbox for flights, driving routes, restaurants, attractions, and accommodation, retain relevant findings, and deliver feasible three-, five-, or seven-day plans. It evaluates environment constraints such as unavailable transport, eight commonsense requirements, and explicit user constraints covering budget, rooms, cuisine, and transport. In the paper's test results, GPT-4 with ReAct achieves a 0.6% final pass rate, despite much higher rates of merely delivering an answer.

## Tasks

1,225 intents divided into nine groups by trip duration and constraint count: 45 training queries with human-annotated plans, 180 validation queries, and 1,000 test queries. Three-day tasks cover one city, five-day tasks two cities, and seven-day tasks three cities. The tool database contains 3,827,361 flight records plus city, distance, restaurant, attraction, and accommodation data.

## Domains

Travel planning in a closed consumer-services sandbox. It is a realistic application environment but not a canonical scientific or engineering domain.

## Evaluation

Deterministic scripts report Delivery Rate, Commonsense Constraint Pass Rate across eight criteria, Hard Constraint Pass Rate, and Final Pass Rate requiring all applicable checks to pass. The environment supplies feedback when searches fail, making successful completion depend on both information collection and adjustment to unavailable options. Experiments cap agents at 30 steps.

## Typical Duration

Interactive trajectories of up to 30 steps, producing itineraries covering three, five, or seven days.

## Main Contribution

A tool-using, execution-grounded benchmark for testing whether language agents can assemble complete real-world plans while satisfying heterogeneous constraints in a reproducible closed sandbox.

## Key Design Ideas

- Freeze a large multi-source database so every agent plans against the same information.
- Separate environment, commonsense, and explicit user constraints.
- Vary horizon and difficulty through trip duration, city count, party size, and hard-constraint count.
- Score constraint satisfaction programmatically rather than relying on surface similarity or an LLM judge.

## Strengths

- Tool retrieval and environment feedback expose failures hidden by static prompt-only planning tests.
- Final Pass requires simultaneous satisfaction of multiple constraint families.
- The closed sandbox improves reproducibility while retaining realistic records and tool interfaces.

## Limitations

- The sandbox is static and restricted to travel, so it does not capture open-world changes or other planning domains.
- Final Pass is strict and sparse; the component metrics are needed to distinguish retrieval, completion, and constraint failures.
- The released plans are evaluated for feasibility under encoded rules, not through real bookings or human traveler outcomes.

## Related Works

- [NATURAL PLAN](./natural-plan.md) — tests travel and schedule planning with all information supplied in context and no tool execution.
- [PlanBench](./planbench.md) — provides formally specified planning domains with solver-backed validity checks.
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — diagnoses planning separately from execution across broader tool-use and multimodal settings.
