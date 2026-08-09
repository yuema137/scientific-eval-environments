# TRAJDEBUG (2026)

> **English** | [简体中文](../zh/works/trajdebug.md)

## Overview

TRAJDEBUG is an error-lifecycle tracing framework for identifying critical failures in long-horizon agent trajectories, released together with TrajErrBench, a benchmark of 486 manually annotated failed trajectories drawn from Tau2Bench and SWE-Bench Pro.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.06346>
- **Venue:** arXiv preprint, 2026

## Summary

TRAJDEBUG addresses error discovery in long trajectories through multi-granularity history compression and evidence-based error identification, and supports critical attribution by tracing each error's resolution status and terminal impact — distinguishing errors an agent later recovers from errors that actually determine the failure. TrajErrBench supplies 486 manually annotated failed trajectories over tool-use and coding scenarios.

## Tasks

TrajErrBench: 486 manually annotated failed trajectories, sourced from Tau2Bench and SWE-Bench Pro, covering tool-use and coding scenarios.

## Domains

Tool-use and coding agent trajectories.

## Evaluation

- Evidence-based error identification over multi-granularity compressed histories.
- Critical attribution: each error is traced for resolution status and terminal impact, separating recovered errors from failure-determining ones.
- Detailed metric definitions beyond the abstract are TODO(reference).

## Typical Duration

Post-hoc analysis of long-horizon failed trajectories.

## Main Contribution

Makes the error lifecycle — occurrence, resolution, terminal impact — the unit of trajectory failure analysis, rather than treating every detected error as equally responsible.

## Key Design Ideas

- Multi-granularity history compression makes very long trajectories tractable for error discovery.
- Resolution-status tracing prevents blaming errors the agent already recovered from.
- The annotated benchmark pairs each failure with its critical error, enabling measurable attribution.

## Strengths

- Targets the practically dominant case — failed long-horizon runs — with manual annotation.
- The authors pledge to release code and data.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [TELBench](./telbench.md) — Also localizes the earliest harmful commitment in long trajectories, over deep-research rather than tool-use/coding runs.
- [Who&When Pro](./who-and-when-pro.md) — Also attributes failure to a decisive step, via controlled error injection rather than annotation of natural failures.
- [SearchAuditor](./searchauditor.md) — Also audits failed long-horizon trajectories with expert-annotated critical steps, for search agents.
