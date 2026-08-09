# ChemIQ (2025)

> **English** | [简体中文](../zh/works/chemiq.md)

## Overview

ChemIQ assesses the chemical intelligence of LLMs with 816 short-answer questions on core organic chemistry — including NMR structure elucidation — answered directly without tools: reasoning models solve 50–57% in their highest reasoning modes, while non-reasoning models manage only 3–7%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.07735>
- **Code:** <https://github.com/oxpig/ChemIQ>
- **Venue:** Journal of Chemical Information and Modeling, 2026 (per the official repository; arXiv metadata carries no venue)

## Summary

Published as "Assessing the Chemical Intelligence of Large Language Models", ChemIQ poses 816 constructed-response questions — no multiple choice, no external tools — spanning organic chemistry from SMILES/IUPAC manipulation to structure elucidation from 1D and 2D ¹H/¹³C NMR. Reasoning models (o3-mini, Gemini Pro 2.5, DeepSeek R1) reach 50–57% in their highest reasoning modes versus 3–7% for non-reasoning models; Gemini Pro 2.5 generates correct SMILES for around 90% of molecules up to 10 heavy atoms and in one case solved a 25-heavy-atom structure.

## Tasks

816 short-answer organic-chemistry questions in 8 categories, answered directly without tool assistance; static, constructed-response format.

## Domains

Chemistry — organic chemistry: molecular representation (SMILES/IUPAC), reaction questions, and NMR-based structure elucidation.

## Evaluation

- Judge-free programmatic checking: exact integer match, OPSIN-parsed IUPAC name validation, canonical-SMILES matching for reactions and NMR answers, and order-insensitive tuple matching for atom mapping.
- **Reported.** 50–57% accuracy for reasoning models at highest reasoning modes vs. 3–7% for non-reasoning models; ~90% correct SMILES generation up to 10 heavy atoms (Gemini Pro 2.5).

## Typical Duration

Single-turn short-answer questions; explicitly non-agentic (no tools).

## Main Contribution

A clean measurement of the reasoning-model jump in chemistry: constructed-response, tool-free, programmatically verified questions on which the reasoning/non-reasoning gap is roughly an order of magnitude.

## Key Design Ideas

- Constructed responses eliminate the multiple-choice guessing floor.
- Every answer type has a canonical checker (OPSIN, canonical SMILES), so no LLM judge is needed.
- NMR elucidation probes multi-constraint structural inference, not recall.

## Strengths

- The 3–7% → 50–57% contrast is one of the sharpest documented reasoning-mode effects in a science domain.
- Public questions, checking scripts, and model outputs; the set is actively extended (2D NMR additions).

## Limitations

- Repository note: card compiled from the arXiv abstract, full text, and official repository (August 2026); the JCIM venue is stated by the repository BibTeX, not arXiv metadata.
- Tool-free by design — measures internal chemical reasoning, not tool-augmented practice.

## Related Works

- [ChemBench](./chembench.md) — Also human-expert-oriented chemistry QA, at broader scope with a chemist baseline.
- [MolPuzzle](./molpuzzle.md) — Also spectrum-based structure elucidation, as a staged multimodal benchmark.
- [QCBench](./qcbench.md) — Also judge-free chemistry evaluation, on quantitative calculation rather than structure.
