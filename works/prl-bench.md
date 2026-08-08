# PRL-Bench (2026)

> **English** | [简体中文](../zh/works/prl-bench.md)

## Overview

PRL-Bench (Physics Research by LLMs) is a benchmark for frontier physics research capability, constructed from 100 curated papers from the latest issues of Physical Review Letters since August 2025 and validated by domain experts, with tasks characterized by exploration-oriented formulation, long-horizon workflows, and objective verifiability.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.15411>
- **Dataset:** <https://huggingface.co/datasets/AdrianMiao/PRL_Bench>
- **Venue:** arXiv preprint (cs.LG, cs.AI, physics.data-an), 2026

## Summary

PRL-Bench derives long-horizon, autonomous-exploration research tasks from very recent PRL papers across five theory- and computation-intensive subfields: astrophysics, condensed matter physics, high-energy physics, quantum information, and statistical physics. Using post-August-2025 papers keeps tasks past most training cutoffs. Six frontier LLMs are evaluated; performance remains limited, with the best overall score below 50 (on a 0–100 scale).

## Tasks

100 research tasks curated from post-August-2025 Physical Review Letters papers and validated by domain experts, spanning five subfields; tasks emphasize exploration-oriented formulation and long-horizon workflows.

## Domains

Frontier physics research across astrophysics, condensed matter physics, high-energy physics, quantum information, and statistical physics.

## Evaluation

- Objectively verifiable task outcomes, expert-validated; overall performance reported on a 0–100-style score.
- **Reported.** Six frontier LLMs evaluated; the best overall score remains below 50.

## Typical Duration

Long-horizon research workflows per task; budgets are TODO(reference).

## Main Contribution

Turns the running front of a flagship physics journal into a continuously refreshable benchmark, with recency serving as contamination control.

## Key Design Ideas

- Sourcing exclusively from post-cutoff PRL issues keeps tasks unmemorizable at construction time.
- Exploration-oriented task formulation targets research behavior, not exam answers.
- Expert validation plus objective verifiability keeps grading mechanical despite research-level content.

## Strengths

- Recency-based contamination control that can be refreshed with every journal issue.
- Five-subfield coverage of theory- and computation-intensive physics.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- Repository note: PRL-Bench is distinct from [PRBench](./prbench.md) — different team, different construction (100 PRL-derived tasks vs. 30 expert-curated reproduction tasks); the near-identical names invite confusion.

## Related Works

- [PRBench](./prbench.md) — Also physics paper-derived evaluation; end-to-end reproduction of 30 expert-curated papers rather than 100 PRL-derived research tasks.
- [CritPt](./critpt.md) — Also frontier research-level physics evaluation, via unpublished challenges with guess-resistant answers.
- [ResearchClawBench](./researchclawbench.md) — Also anchors tasks to recent publications kept beyond the model's reach, via hidden papers.
