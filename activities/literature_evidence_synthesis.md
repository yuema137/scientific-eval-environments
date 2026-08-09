# Literature Search & Evidence Synthesis

> **English** | [简体中文](../zh/activities/literature_evidence_synthesis.md) · [← All activities](./README.md)

## Definition

Evaluates an agent's ability to find, retrieve, and synthesize the scientific literature and evidence base — locating relevant publications, selecting studies, extracting structured evidence, and combining sources into grounded scientific answers or reviews.

## Scope

Includes targeted paper-finding, open-ended literature collection, systematic review and meta-analysis, evidence-grounded QA, and literature-grounded structured data extraction. It is **not** assigned merely because an agent reads one supplied paper as instructions for a different task (e.g. paper reproduction) — the literature or evidence step must itself be the evaluated capability.

## Task Patterns

The most direct instantiation of this activity is agentic paper-finding, where the deliverable is a set of publications rather than a written answer. [AutoResearchBench](../works/autoresearchbench.md) splits this cleanly into targeted retrieval of one known paper (Deep Research, 600 queries) and open-ended collection of all papers meeting conditions (Wide Research, 400 queries), while [ScholarQuest](../works/scholarquest.md) organizes iterative CS paper search around four research-intent categories and reports recall that stays low even for the best agents. [AstaBench](../works/astabench.md) covers the same territory at suite scale with a literature-understanding category (PaperFindingBench, LitQA2 variants, table generation) backed by date-restricted production search tools, and [SciExplore](../works/sciexplore.md) arranges retrieval as a progression from database navigation through ambiguous retrieval and missing-reference completion to cross-source synthesis.

A second cluster tests evidence-grounded QA and multi-hop synthesis over the literature. [Aviary](../works/aviary.md) contributes the LitQA2/PaperQA literature-research environment, and both [LAB-Bench](../works/lab-bench.md) and its successor [LABBench2](../works/labbench2.md) embed literature recall and reasoning within broader biology-capability suites, with LABBench2 restoring realism by grounding answers in PDFs and images. [MedBrowseComp](../works/medbrowsecomp.md) pushes multi-hop synthesis onto live, fragmented medical sources where freshness and reconciliation are the tested skills, and [DeepResearch Bench](../works/deepresearch-bench.md) evaluates end-to-end deep-research report generation and citation grounding via its RACE and FACT frameworks. [BioKGBench](../works/biokgbench.md) reframes literature understanding as checkable behavior — claim verification and KGQA composed into finding factual errors in biomedical knowledge graphs.

A third cluster is literature-grounded structured extraction: turning papers into structured records. [MatViX](../works/matvix.md) extracts compositions and property curves from full-length materials articles into JSON (grading the curves in figures, not just entities), and [ChemX](../works/chemx.md) does expert-validated chemical extraction from documents across nanomaterials and small-molecule datasets. [MetaSyn](../works/metasyn.md) is the systematic-review / meta-analysis endpoint, asking agents to select the eligible study set from a corpus with distractors under the PI/ECO protocol and synthesize.

Boundary cases: Aviary, LAB-Bench, LABBench2, and AstaBench are multi-capability suites where only their literature, QA, and extraction components fall squarely in scope (sequence, cloning, protocol, and code subtasks do not). [MOOSE-Chem](../works/moose-chem.md) uses inspiration retrieval over a 3,000-paper corpus, but in service of hypothesis rediscovery rather than evidence synthesis, so it sits primarily under Experiment Design & Scientific Discovery.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| Aviary | 2024 | Answer research questions from literature via PaperQA environment | LitQA2/PaperQA env, 248 questions (49 held-out); multi-step | Correct literature-grounded answers | [card](../works/aviary.md) |
| BioKGBench | 2024 | Verify claims and query KG to find factual errors | SCV + KGQA (2,000+) composed into KGCheck (225 instances) | Locate factual errors in biomedical KGs | [card](../works/biokgbench.md) |
| LAB-Bench | 2024 | Literature recall/reasoning plus database access QA | MCQs across 8 categories (2,400+); static, tool-use optional | Accuracy vs expert biologist baselines | [card](../works/lab-bench.md) |
| MatViX | 2024 | Extract structured data from full-text materials articles | Zero-shot multimodal extraction, 324 articles to 1,688 JSON records | Compositions and property-curve fidelity | [card](../works/matvix.md) |
| MOOSE-Chem | 2024 | Retrieve inspirations to rediscover chemistry hypotheses | 51 annotated papers over 3,000-paper inspiration corpus; agentic pipeline | Hypotheses matching ground truth | [card](../works/moose-chem.md) |
| AstaBench | 2025 | Literature understanding: paper-finding, QA, table generation | Lit-understanding benchmarks within 2,400+ problem suite; date-restricted tools | Cost-controlled scores vs baselines | [card](../works/astabench.md) |
| ChemX | 2025 | Extract structured chemical data from documents | Agentic document extraction against 10 curated datasets | Structured records vs expert-validated truth | [card](../works/chemx.md) |
| DeepResearch Bench | 2025 | Conduct end-to-end deep research and cited report | 100 expert tasks, 22 domains (50 EN/50 ZH) | Report quality (RACE) and citation grounding (FACT) | [card](../works/deepresearch-bench.md) |
| MedBrowseComp | 2025 | Retrieve and synthesize multi-hop facts from live sources | 1,000+ curated questions; deep-research and computer-use | Correct up-to-date reconciled answer | [card](../works/medbrowsecomp.md) |
| AutoResearchBench | 2026 | Find target paper and collect all qualifying papers | 1,000 queries: Deep Research (600) + Wide Research (400) | Located target / complete paper set | [card](../works/autoresearchbench.md) |
| LABBench2 | 2026 | Literature/patent/trial QA in realistic artifact contexts |  | 1,900 tasks over PDFs, images, files; static harness | [card](../works/labbench2.md) |
| MetaSyn | 2026 | Select eligible studies and synthesize systematic review | 422 expert meta-analyses; PubMed corpus with distractors | Correct eligible set and protocol-faithful synthesis | [card](../works/metasyn.md) |
| ScholarQuest | 2026 | Iterative academic paper search by research intent | 1,000+ CS topics, four intent categories | Recall@100/@All (best | [card](../works/scholarquest.md) |
| SciExplore | 2026 | Navigate databases and integrate cross-source evidence | 103 expert tasks, four progressive types, 10+ disciplines | Correct retrieval, grounding, and synthesis | [card](../works/sciexplore.md) |

## Related Works

- [Aviary](../works/aviary.md)
- [BioKGBench](../works/biokgbench.md)
- [LAB-Bench](../works/lab-bench.md)
- [MatViX](../works/matvix.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [AstaBench](../works/astabench.md)
- [ChemX](../works/chemx.md)
- [DeepResearch Bench](../works/deepresearch-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [LABBench2](../works/labbench2.md)
- [MetaSyn](../works/metasyn.md)
- [ScholarQuest](../works/scholarquest.md)
- [SciExplore](../works/sciexplore.md)
