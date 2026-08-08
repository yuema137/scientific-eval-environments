# SMDD-Bench (2026)

> **English** | [简体中文](../zh/works/smdd-bench.md)

## Overview

SMDD-Bench asks whether LLMs can solve real-world small-molecule drug design tasks: 502 guaranteed-solvable instances over 102 unique protein targets in five task types — 2D pharmacophore identification, interaction point discovery, scaffold hopping, lead optimization, and fragment assembly — as a multi-turn, long-horizon agentic benchmark.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.21740>
- **Leaderboard:** <http://smddbench.com>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

SMDD-Bench requires strong chemical and biological reasoning, 3D intuition, specialized tool use, and planning expertise over a limited number of oracle calls — the oracle budget makes each query a spent resource, so the agent must plan its exploration rather than brute-force it. Every instance is constructed guaranteed-solvable, which turns failure into evidence about the agent rather than the task. Across seven frontier open- and closed-source LLMs, even the most performant, GPT-5.4, solves only 40.2% of tasks.

## Tasks

502 guaranteed-solvable, multi-turn drug-design task instances over 102 protein targets in five types: 2D pharmacophore identification, interaction point discovery, scaffold hopping, lead optimization, and fragment assembly.

## Domains

Small-molecule drug design: medicinal and computational chemistry over protein targets — pharmacophores, scaffolds, lead optimization, and fragment assembly.

## Evaluation

- Solve rate over guaranteed-solvable instances under a limited oracle-call budget; oracle and verifier implementation details are TODO(reference).
- **Reported.** Seven frontier LLMs evaluated; the best, GPT-5.4, solves only 40.2% of tasks.

## Typical Duration

Multi-turn, long-horizon design episodes bounded by the oracle-call budget.

## Main Contribution

Drug design posed as budgeted search: guaranteed solvability plus an oracle-call limit make both success and query efficiency attributable to the agent's planning.

## Key Design Ideas

- Guaranteed-solvable construction removes "the task was impossible" as an excuse.
- The oracle-call budget prices exploration, importing resource-awareness into molecular design.
- Five task types ladder from perception (pharmacophores) to synthesis-level planning (fragment assembly).

## Strengths

- Realistic target diversity (102 proteins) with verifiable solvability.
- The 40.2% frontier ceiling under budget documents substantial headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. The leaderboard site was unreachable at validation time, and no code release is verifiable from the paper's arXiv page.

## Related Works

- [MDArena](./mdarena.md) — Also molecular-level scientific workflows for agents, in simulation rather than design.
- [MaD Physics](./mad-physics.md) — Also prices queries under a per-task budget, for physical-law discovery.
- [SciAgentArena](./sciagentarena.md) — Also includes computational drug-discovery tasks among biomedical research scenarios.
