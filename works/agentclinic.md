# AgentClinic (2024)

> **English** | [简体中文](../zh/works/agentclinic.md)

## Overview

AgentClinic is a multimodal agent benchmark for AI in simulated clinical environments: a doctor agent must reach diagnoses through sequential patient interactions, multimodal data collection under incomplete information, and tool use — across nine medical specialties and seven languages.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.07960>
- **Code:** <https://github.com/samuelschmidgall/agentclinic>
- **Project:** <https://agentclinic.github.io/>
- **Publication:** <https://www.nature.com/articles/s41746-026-02674-7>
- **Venue:** npj Digital Medicine, 2026

## Summary

AgentClinic converts static medical QA into sequential decision-making: the environment supplies patient, measurement, and moderator agents (four agents and 24 modeled biases per the official project page), and the evaluated doctor agent must elicit history, order measurements, and commit to a diagnosis with tools including experiential learning, adaptive retrieval, reflection cycles, and a persistent cross-case notebook. Diagnostic accuracy can drop to below a tenth of the static-QA figure once the same questions become sequential; Claude 3.5-sourced agents lead most settings, and Llama-3 gains up to 92% relative improvement from the notebook tool. The benchmark is supported by real EHRs and a clinical reader study.

## Tasks

Sequential doctor-patient encounters in simulated clinical environments across nine medical specialties and seven languages, with multimodal data collection and tool use; case counts are TODO(reference).

## Domains

Clinical medicine across nine specialties; multilingual clinical care; EHR-supported case material.

## Evaluation

- Diagnostic accuracy in moderated multi-agent encounters, with bias perturbations of patient and doctor agents and patient-centric metrics; supported by real electronic health records and a clinical reader study.
- **Reported.** Sequential interaction drops diagnostic accuracy to below a tenth of static-QA levels; Claude 3.5-based agents lead most settings; the notebook tool yields up to 92% relative improvement for Llama-3.

## Typical Duration

Multi-turn clinical encounters per case.

## Main Contribution

Demonstrated that static medical QA scores are an order of magnitude too optimistic: the same knowledge, evaluated as sequential clinical work under incomplete information, mostly collapses.

## Key Design Ideas

- Patient, measurement, and moderator agents make the environment — not a question — the unit of evaluation.
- Modeled cognitive and implicit biases turn robustness to bias into a measurable axis.
- Persistent tools (the cross-case notebook) let the benchmark measure learning across cases.

## Strengths

- The static-to-sequential collapse is among the most cited findings in clinical-agent evaluation.
- Multilingual and multi-specialty breadth with a clinical reader study behind it.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The npj Digital Medicine venue is stated by the official project page; arXiv metadata carries no venue.

## Related Works

- [MedAgentBench](./medagentbench.md) — Also interactive clinical-agent evaluation, against a FHIR virtual EHR rather than simulated encounters.
- [SDBench](./sdbench.md) — Also sequential diagnosis, with information gating and explicit cost accounting.
- [MedHELM](./medhelm.md) — The static clinician-validated counterpart whose scores AgentClinic's design challenges.
