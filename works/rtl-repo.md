# RTL-Repo (2024)

> **English** | [简体中文](../zh/works/rtl-repo.md)

## Overview

RTL-Repo benchmarks LLMs on large-scale RTL design projects: more than 4,000 Verilog samples extracted from public GitHub repositories, each providing the full context of its corresponding repository, testing multi-file repository-scale Verilog code completion.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.17378>
- **Code:** <https://github.com/AUCOHL/RTL-Repo>
- **Venue:** LAD 2024 (IEEE International Workshop on LLM-Aided Design)

## Summary

Most RTL benchmarks give a model a self-contained problem; real hardware lives in multi-file repositories. RTL-Repo tests that setting: over 4,000 Verilog samples from public GitHub projects, each accompanied by the full repository context, requiring the model to complete Verilog code that fits the surrounding cross-file design. It evaluates GPT-4, GPT-3.5, Starcoder2, and Verilog-specific models (VeriGen, RTLCoder), scoring edit similarity and exact match rather than simulation pass@k.

## Tasks

Repository-level Verilog code completion over 4,000+ samples, each with full-repository context; static completion scored by string-level similarity.

## Domains

Electrical Engineering — digital design: repository-scale RTL code completion in real projects.

## Evaluation

- Edit similarity and exact match against the reference completion (repository leaderboard metrics).
- **Reported.** GPT-4, GPT-3.5, Starcoder2, VeriGen, and RTLCoder are compared; the abstract gives no single headline value.

## Typical Duration

Single completion per sample, conditioned on full-repository context.

## Main Contribution

Bringing repository-scale, cross-file context into RTL evaluation — measuring whether models can write hardware that fits an existing project, not just isolated modules.

## Key Design Ideas

- Full-repository context tests long-context cross-file reasoning specific to real RTL.
- Public-GitHub sourcing gives authentic project structure at scale (4,000+ samples).
- Edit-similarity/exact-match scoring suits completion where simulation is impractical.

## Strengths

- The repository-scale angle that self-contained RTL benchmarks omit.
- Large sample count with Verilog-specialized models included in the comparison.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the venue is LAD'24 per the official repository (an "MLCAD 2024" attribution is incorrect). String-similarity metrics do not verify functional correctness.

## Related Works

- [VerilogEval](./verilogeval.md) — Also LLM Verilog generation, at self-contained problem scale with simulation.
- [RTLLM](./rtllm.md) — Also RTL generation, at full-design rather than repository scale.
- [CVDP](./cvdp.md) — Also large-scope RTL evaluation, spanning design and verification.
