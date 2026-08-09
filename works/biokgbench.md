# BioKGBench (2024)

> **English** | [简体中文](../zh/works/biokgbench.md)

## Overview

BioKGBench is a knowledge-graph checking benchmark for biomedical AI agents: two atomic tasks — scientific claim verification (SCV) and knowledge-graph question answering (KGQA) — compose into the agentic KGCheck task, in which an agent uses KGQA and domain-based retrieval-augmented generation to identify factual errors in large-scale biomedical knowledge graphs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.00466>
- **Code:** <https://github.com/westlake-autolab/BioKGBench>
- **Venue:** arXiv preprint (cs.CL, cs.AI), 2024

## Summary

BioKGBench treats "understanding the literature" as checkable behavior: can an agent verify scientific claims and interrogate a knowledge graph well enough to find where the graph itself is wrong? It provides over two thousand instances for the atomic tasks and 225 high-quality annotated instances for the agent-level KGCheck task, over biomedical resources including UniProt, STRING, Reactome, and DisGeNET (per the official repository). State-of-the-art agents — general and biomedical — fail or underperform on the benchmark, and the paper's baseline agent (BKGAgent) discovers over 90 factual errors in existing knowledge-graph databases.

## Tasks

Two atomic tasks (scientific claim verification; KGQA) with 2,000+ instances, plus the agentic KGCheck task with 225 annotated instances: interactively query a biomedical knowledge graph to locate factual errors.

## Domains

Biomedical knowledge graphs covering proteins and interactions, pathways, diseases, genes, and tissues (UniProt, STRING, Reactome, DisGeNET per the official repository).

## Evaluation

- Correctness on claim verification and KGQA; agent-level scoring on annotated KGCheck instances. Detailed metric definitions are TODO(reference).
- **Reported.** State-of-the-art agents fail or show inferior performance; over 90 factual errors discovered in existing knowledge-graph databases.

## Typical Duration

Interactive KG-interrogation episodes for KGCheck; single-instance answering for the atomic tasks.

## Main Contribution

Turns knowledge-base quality control into an agent benchmark — and demonstrates the payoff by surfacing 90+ real errors in production biomedical databases.

## Key Design Ideas

- Atomic tasks (verify, query) are evaluated separately from their agentic composition (audit).
- The evaluation target is the knowledge graph itself, so success produces scientific value (found errors), not just scores.
- Domain RAG grounds verification in biomedical sources rather than parametric memory.

## Strengths

- Dual-level design localizes whether failures are atomic or compositional.
- Discovered errors give rare external validation of the benchmark's realism.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: BKGAgent, the paper's baseline agent, is agent implementation and out of this repository's scope; the card documents the benchmark.

## Related Works

- [LAB-Bench](./lab-bench.md) — Also database-navigation evaluation for biology, in MCQ form.
- [MetaSyn](./metasyn.md) — Also evidence-faithfulness evaluation over biomedical literature, via systematic review.
- [MedBrowseComp](./medbrowsecomp.md) — Also multi-hop fact synthesis over live biomedical knowledge bases.
