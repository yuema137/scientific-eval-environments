# MedBrowseComp (2025)

> **English** | [简体中文](../zh/works/medbrowsecomp.md)

## Overview

MedBrowseComp benchmarks medical deep research and computer use: more than 1,000 human-curated questions requiring agents to retrieve and synthesize multi-hop medical facts from live, domain-specific knowledge bases — clinical trials, primary studies, regulatory documents, and cost data.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.14963>
- **Code:** <https://github.com/shan23chen/MedBrowseComp>
- **Dataset:** <https://huggingface.co/datasets/AIM-Harvard/MedBrowseComp>
- **Project:** <https://moreirap12.github.io/mbc-browse-app/>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

Real clinical questions rarely live in one source: MedBrowseComp's physician-curated questions force agents to reconcile fragmented or conflicting information across live knowledge bases — trials registries, primary literature, FDA approval and exclusivity records, drug patents, and health-cost data — to reach an up-to-date conclusion. The released splits (official dataset) comprise MedBrowseComp-50, MedBrowseComp-605, and a computer-use split MedBrowseComp-CUA (484). Agent performance shows shortfalls reaching as low as ten percent.

## Tasks

1,000+ human-curated multi-hop questions over live medical knowledge bases, in deep-research and computer-use settings (splits of 50, 605, and 484 per the official dataset).

## Domains

Clinical and regulatory medicine: clinical trials, pharmacology, FDA approvals and exclusivity, drug patents, and health-cost data.

## Evaluation

- Multi-hop retrieval and synthesis scored against human-curated gold answers; judge implementation details are TODO(reference).
- **Reported.** Agent performance shortfalls reach as low as ten percent on the hardest settings.

## Typical Duration

Live browsing / computer-use episodes per question.

## Main Contribution

Grounds medical deep-research evaluation in the live, fragmented sources clinicians actually consult, where freshness and reconciliation — not recall — are the tested skills.

## Key Design Ideas

- Live knowledge bases make answers time-dependent, so retrieval cannot be replaced by memorization.
- Multi-hop construction forces cross-source reconciliation, including conflicting records.
- The CUA split extends the same questions to computer-use agents.

## Strengths

- Physician curation over regulatory and economic sources most benchmarks ignore.
- Live-source design doubles as a continuous contamination control.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [BioKGBench](./biokgbench.md) — Also verification-oriented navigation of biomedical knowledge sources, over curated KGs.
- [AutoResearchBench](./autoresearchbench.md) — Also open-web multi-hop discovery evaluation, for scientific literature.
- [MedHELM](./medhelm.md) — Also clinician-anchored medical evaluation, over static task suites.
