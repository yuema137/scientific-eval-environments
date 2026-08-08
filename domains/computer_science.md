# Computer Science

> **English** | [简体中文](../zh/domains/computer_science.md) · [← All domains](./README.md)

## Scope

Computer science as the studied field outside AI/ML research itself — see AI & Machine Learning Research for AI-paper reproduction, and Software & Systems Engineering for building and verifying software.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| AutoResearchBench | 2026 | Scientific literature discovery over eight core CS domains: track down one specific target paper through progressive multi-step probing (Deep Research), or comprehensively collect all papers satisfying given conditions (Wide Research). | 1,000 queries — 600 Deep Research + 400 Wide Research (avg. 9.23 valid answers each) — built by a full-text-first human–machine pipeline with citation-based multi-hop expansion. | Exact-match accuracy against the verified target paper (Deep); set-level IoU against rigorously audited answer sets requiring unanimous LLM consensus for admission (Wide). | [→](../works/autoresearchbench.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Information is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| ScholarQuest | 2026 | Search the computer science literature (information retrieval and AI focus) the way researchers actually do: method-oriented, setting-anchored, comparison-based, and scope-controlled queries. | Iterative literature-exploration episodes in open literature environments, with queries constructed from over 1,000 computer science topics across the four research intents. | Recall@100 and Recall@All against ground-truth paper sets, with analyses of search efficiency, intent-level robustness, and failure cases. | [→](../works/scholarquest.md) |
| CORE-Bench | 2024 | Reproduce published computational results from each paper's own code and data; computer science is one of its three disciplines. | 270 tasks from 90 papers at three difficulty levels, in language-only and vision-language forms. | Accuracy of reproduced results, checked by a fast, parallelizable evaluation harness. | [→](../works/core-bench.md) |

## Related Works

- [AutoResearchBench](../works/autoresearchbench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [ScholarQuest](../works/scholarquest.md)
- [CORE-Bench](../works/core-bench.md)
