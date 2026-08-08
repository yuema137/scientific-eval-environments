# MedAgentBench (2025)

> **English** | [简体中文](../zh/works/medagentbench.md)

## Overview

MedAgentBench is a realistic virtual EHR environment to benchmark medical LLM agents: 300 patient-specific, clinically derived tasks from 10 categories written by human physicians, over realistic profiles of 100 patients with more than 700,000 data elements, in a FHIR-compliant interactive environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.14654>
- **Code:** <https://github.com/stanfordmlgroup/MedAgentBench>
- **Publication:** <https://ai.nejm.org/doi/full/10.1056/AIdbp2500144>
- **Venue:** NEJM AI, 2025

## Summary

MedAgentBench evaluates agents against the interfaces hospitals actually run: agents plan and call tools through the standard FHIR APIs and communication infrastructure of modern EMR systems, on physician-written tasks over realistic patient profiles. Task success is checked programmatically against reference solutions in the environment. The best model, Claude 3.5 Sonnet v2, achieves a 69.67% success rate, with significant variation across task categories.

## Tasks

300 patient-specific tasks in 10 physician-written categories over 100 realistic patient profiles (700,000+ data elements), executed in a Dockerized FHIR-compliant virtual EHR.

## Domains

Clinical informatics: electronic health records, EMR interoperability (FHIR), and clinical task automation.

## Evaluation

- Programmatic success-rate checking against reference solutions inside the FHIR environment (reference solutions access-gated per the official repository).
- **Reported.** Best model Claude 3.5 Sonnet v2 at 69.67% success, with significant variation across task categories.

## Typical Duration

Multi-step tool-calling episodes against the virtual EHR per task.

## Main Contribution

Moves medical-agent evaluation onto production healthcare standards: if an agent cannot operate FHIR, it cannot operate a hospital, whatever its exam scores say.

## Key Design Ideas

- FHIR compliance makes the benchmark environment isomorphic to deployed EMR systems.
- Physician-written tasks anchor difficulty to clinical reality rather than API coverage.
- Programmatic verification keeps grading independent of judges.

## Strengths

- Realistic scale (100 patients, 700K+ elements) behind every task.
- Per-category variation identifies which clinical workflows remain unautomated.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The NEJM AI venue is cited by the official repository (under a marginally shortened title); arXiv metadata carries no venue.

## Related Works

- [MedAgentGym](./medagentgym.md) — Also sandboxed biomedical agent evaluation, centered on code-based data-science tasks.
- [AgentClinic](./agentclinic.md) — Also interactive clinical evaluation, via simulated encounters rather than EHR APIs.
- [Gaia2](./gaia2.md) — Also verifies agent write-actions programmatically in a stateful app environment.
