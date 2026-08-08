# Domains

> **English** | [简体中文](../zh/domains/README.md)

One reference page per canonical science or engineering domain — the **field axis** of the repository, co-equal with the methodology axis in [`topics/`](../topics/): topics group works by evaluation *methodology*, domains by *field*. The full rules live in [`AGENT.md`](../AGENT.md).

## Domain page template

- **Scope** — one or two sentences: what counts, including fold rules.
- **Comparison** — a factual table with **fixed columns, identical on every domain page**:
  `Work | Year | Scientific problem | Task form & scale | Domain verification | Card`.
  *Scientific problem* states what science question the work actually tackles; *Task form & scale* states what the agent concretely does and how many tasks fall in this domain; *Domain verification* states how scientific correctness is checked (numerical error vs. reference, expert labels, execution, physical criteria, LLM judge, …).
- **Related Works** — bare links to the work cards (the mapping list).

Domain pages are **factual reference pages, not literature reviews** — co-equal with topic pages as an entry point, different in kind: the table describes each work in this domain, but methodology synthesis, topic-specific comparison dimensions, and open questions stay in topic pages.

## Rules

- **Language switcher and breadcrumb.** Every page carries one quote line directly under the H1 combining the switcher and a link back to this index: `> **English** | [简体中文](../zh/domains/<file>.md) · [← All domains](./README.md)` on English pages, and `> [English](../../domains/<file>.md) | **简体中文** · [← 全部 domains](./README.md)` on the Chinese mirror.
- Narrower fields **fold** into canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, formal software verification → Software & Systems Engineering, …).
- A work may belong to **multiple domains**; multi-domain suites appear in every domain they cover, with the table row slanted to this domain's slice.
- **No catch-all.** Works without a science or engineering domain — web/UI agents, computer use, generic tool use, evaluation methodology, surveys — do not appear here. UI and computer-use environments are not science or engineering domains.
- The mapping is **one-way, maintained on domain pages only**. Cards are never modified for this axis; a card's `## Domains` prose section is the evidence for assignment, and every table cell must be verifiable from the card.
- Assignment must be **verifiable** from the card (backed by the paper). Unnamed categories are not force-assigned.

## Canonical domain taxonomy

| Group | Domain | Works |
|---|---|---|
| Science | [Physics](./physics.md) | 35 |
| Science | [Astronomy](./astronomy.md) | 5 |
| Science | [Mathematics](./mathematics.md) | 12 |
| Science | [Chemistry](./chemistry.md) | 10 |
| Science | [Biology](./biology.md) | 25 |
| Science | [Neuroscience & Cognitive Science](./neuroscience_cognitive_science.md) | 5 |
| Science | [Medicine & Health](./medicine_health.md) | 12 |
| Science | [Earth Science](./earth_science.md) | 5 |
| Science | [Environmental Science](./environmental_science.md) | 2 |
| Science | [Materials Science](./materials_science.md) | 7 |
| Science | [Computer Science](./computer_science.md) | 4 |
| Science | [AI & Machine Learning Research](./ai_ml_research.md) | 5 |
| Engineering | [Mechanical & Aerospace Engineering](./mechanical_aerospace_engineering.md) | 9 |
| Engineering | [Electrical Engineering](./electrical_engineering.md) | 1 |
| Engineering | [Energy Systems](./energy_systems.md) | 2 |
| Engineering | [Chemical Engineering](./chemical_engineering.md) | 1 |
| Engineering | [Civil & Structural Engineering](./civil_structural_engineering.md) | 2 |
| Engineering | [Robotics](./robotics.md) | 0 |
| Engineering | [Software & Systems Engineering](./software_systems_engineering.md) | 11 |
