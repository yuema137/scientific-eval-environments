# NATURAL PLAN (2024)

> **English** | [简体中文](../zh/works/natural-plan.md)

> **First appeared:** 2024-06-06 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2406.04520)

## Overview

NATURAL PLAN is a 3,600-instance benchmark that evaluates natural-language planning across trip planning, meeting planning, and calendar scheduling while providing all required tool-derived information directly in the prompt.

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

N/A — general trip, meeting, and calendar planning; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2406.04520>
- **Code:** <https://github.com/google-deepmind/natural-plan>
- **Venue:** arXiv preprint (2024)

## Summary

NATURAL PLAN isolates planning from tool operation by placing Google Flights, Google Maps, and Google Calendar outputs in model context. Its three task families vary constraint complexity through city count, participants, schedules, and days, and use synthetic instances grounded in real tool data. In the five-shot evaluation, GPT-4 reaches 31.1% exact match on Trip Planning and Gemini 1.5 Pro reaches 34.8%; all evaluated models fall below 5% on ten-city trip instances.

## Tasks

3,600 test examples: 1,600 Trip Planning, 1,000 Meeting Planning, and 1,000 Calendar Scheduling. Trip Planning samples 3–10 European cities, visit durations, date constraints, and direct-flight connectivity. Meeting Planning asks for a route that maximizes meetings subject to participant availability and Google Maps driving times. Calendar Scheduling asks for a unique 30- or 60-minute meeting slot across attendee schedules, varying the number of attendees and workdays.

## Domains

Consumer travel, meeting, and calendar planning. The benchmark uses realistic geographic and schedule data but does not evaluate a canonical scientific or engineering domain.

## Evaluation

Model output is parsed into the benchmark's structured answer form and compared with a golden plan using exact match. Experiments vary constraint complexity and also test easy-to-hard and hard-to-easy few-shot generalization, prompted self-correction, and long-context in-context planning with as many as 800 examples.

## Typical Duration

One model response per problem after five in-context examples in the main setup; tool calls are not executed during evaluation. Prompt length and reasoning difficulty rise with 3–10 cities, 2–7 meeting participants, or 1–5 workdays, depending on the task family.

## Main Contribution

A realistic natural-language planning benchmark that holds information access fixed, allowing planning ability to be measured without confounding it with tool selection or tool execution.

## Key Design Ideas

- Supply tool-derived facts as context instead of requiring live tool calls.
- Control difficulty by changing constraint-bearing entities such as cities, people, and days.
- Ground synthetic problems in flight connectivity, travel times, and calendar schedules.
- Use ablations to test whether self-correction, example difficulty, or additional context improves planning.

## Strengths

- Removing tool execution gives planning failures a clearer interpretation.
- Three distinct task families test routing, scheduling, and constraint satisfaction under one protocol.
- Exact-match scoring is deterministic and the generators admit controlled complexity sweeps.

## Limitations

- Exact match can reject an alternative plan that is valid but differs from the single canonical representation.
- Supplying all information removes retrieval and environment adaptation, which are central to deployed agents.
- The benchmark measures plan production in one response rather than feedback-conditioned replanning.

## Related Works

- [PlanBench](./planbench.md) — also isolates planning, but uses formal action models and plan validators rather than realistic natural-language constraints.
- [TravelPlanner](./travelplanner.md) — requires agents to retrieve information through tools and produce plans inside a closed travel sandbox.
- [Agent Planning Benchmark](./agent-planning-benchmark.md) — separately measures complete-plan generation and feedback-conditioned next-step planning.
