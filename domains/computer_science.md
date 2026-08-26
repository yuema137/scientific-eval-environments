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
| TCS-Bench | 2026 | Research-level theoretical computer science proof generation — proving results drawn from top TCS venues (FOCS, STOC, SODA). | 300 theorem-proving tasks, each a target statement plus assembled context extracted from FOCS/STOC/SODA papers (2020–2026); the model produces a self-contained proof. | Proofs checked by an automated verification agent (four Gemini 3.1 Flash calls, 3-of-4 majority vote), calibrated against a 100-item human-expert–labeled set at over 90% agreement. | [→](../works/tcs-bench.md) |
| EngDesign | 2025 | Operating system design and computer architecture design posed as engineering design specifications with stated goals, constraints and performance requirements. | Operating System Design (8) and Computer Architecture Design (5) within 101 design tasks carrying 473 gradable items across nine engineering areas; 12 chat and reasoning models. | Structured model output executed by a per-task evaluation script, returning a binary pass/fail, a 0–100 partial-credit score and a detailed log; 53 of the 101 tasks are licence-free and released separately as EngDesign-Open. | [→](../works/engdesign.md) |
| R³-Bench | 2026 | Allocate one shared budget across a six-problem competitive-programming suite. | 50 suites of 6 problems drawn from LiveCodeBench Pro, 300 problems in total, run both tool-free and inside a Terminus-2 shell. | Contest score against the same response-curve oracle; equal-allocation replay alone beats the model's own contest performance for 4 of 6 models at moderate pressure. | [→](../works/r3-bench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the computer science subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`THEO` theory of computation & computational complexity · `ALGO` algorithms & algorithmic problem solving · `OS` operating systems · `ARCH` computer architecture · `PL` programming languages & compilers · `SE` software engineering · `DB` databases & data management · `IR` information retrieval & search · `NET` networking & distributed systems · `SEC` security & cryptography · `HCI` human–computer interaction · `GRAPH` computer graphics & visualization · `AI` artificial intelligence & machine learning · `GEN` curriculum-wide or unspecified, no single subfield

**Two scores, not one.** The columns split into **coverage** — what the evaluation setup puts under test — and **rigor** — how far you can trust what it reports. They are summed separately because they pull against each other: a benchmark can put everything under test and verify none of it carefully, and a deliberately narrow one can be the most trustworthy thing on the page. Rows are ordered by `Cov`, highest first, and by `Rig` within equal coverage; remaining ties keep Comparison-table order. Coverage leads because it is the axis a reader scans for — *does this benchmark even put my problem under test* — and `Rig` then says how far to trust what it reports.

### Coverage (`Cov`, max 7)

Yes/no, ordered by rarity — the properties fewest works have come first, so the left of the group is where the field is thin. A property nearly every work satisfies does not earn a column: *writing and running code* was dropped on that ground.

- **Net** — network or live external retrieval permitted; a supplied fixed corpus does not count.
- **E2E** — end-to-end research: a question or goal only, with no source paper, reference implementation, or step-by-step specification supplied, and the agent drives the whole investigation.
- **Cost** — budget or resource cost is a scored or priced dimension, not merely a step cap.
- **MM** — multimodal content is load-bearing, either required as input or scored as an output artifact.
- **Repro** — grounded in a specific published result the agent must match or recover.
- **Real** — real experimental or observational data, as opposed to synthetic or simulated (a digital twin is simulated).
- **Inter** — interactive: the agent takes multiple actions against an environment, tool, or simulator and gets feedback that shapes the next one.

### Rigor (`Rig`, max 13)

- **Human** — a measured human-expert baseline or human reference performance anchors the scale. `◐` where the anchor is a published result or expert reference implementation rather than a measured human run.
- **Rubric** — an expert-authored rubric or official marking scheme with named criteria or weights; a continuous automatic metric is not a rubric.
- **Contam** — a deliberate mechanism makes the answer unmemorizable: post-cutoff sourcing, unpublished or newly authored problems, counterfactual alteration, on-demand generation, or screened leakage. Withholding a published paper at evaluation time is `◐` — it does not remove that paper from a pretraining corpus.
- **Verif** `0`–`3` — how far the score can be trusted without trusting a model. `0` scored only by an LLM judge or rubric, with no validation of that scorer · `1` judge or rubric scoring whose agreement with human experts is measured and reported · `2` deterministic checks alongside judge or rubric scoring · `3` fully deterministic — execution, tests, numerical comparison to a reference, symbolic checking, or a proof kernel, with no judge in the loop. This replaces a plain yes/no *deterministic verification* column, which 85% of works satisfied and which therefore separated nothing; as a ladder it separates a great deal. A separate `Judge` column was dropped as near-redundant with `Verif` < 2.
- **Scale** `0`–`3` — items evaluated **in this domain**: `0` fewer than 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 or more · `?` the source does not give a per-domain count. This counts items, not effort: 30 paper-reproduction tasks are far more work than 3,000 exam questions, and the column cannot see that.
- **Fail** `0`–`4` — how deep the failure analysis goes, because "reports a failure analysis" spans everything from a single remark to a controlled experiment. `0` nothing beyond headline scores · `1` narrative remarks on where models fall short, no classes named · `2` named error classes or illustrative case studies, but no counts or shares · `3` a quantified failure account: a taxonomy with per-class counts or shares, or measured breakdowns isolating specific failure conditions · `4` level 3 plus a controlled experiment or ablation built to test *why* the failures occur.

### Reading the two scores

Yes/no columns score `✔` 1, `◐` 0.5, `✘` 0, `?` 0; graded columns contribute their number, with `?` scoring 0. `Domain` does not score.

Three cautions. A `?` costs exactly what a `✘` costs, so both scores are floors on what a work *demonstrably* does, not verdicts on it. Neither score is a quality ranking: high `Cov` with low `Rig` describes a benchmark that reaches for everything and pins down little, while low `Cov` with high `Rig` describes one that measures a narrow thing carefully — and which of those is the right design depends entirely on the question being asked. And `Cov` is a property of the *evaluation setup*, not of the science: a work can sit at the bottom of this table and still be the most important paper in its subfield.

For multi-domain suites the row describes this domain's slice, as in the Comparison table.
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| CORE-Bench | GEN | ✘ | ✘ | ✘ | ◐ | ✔ | ✔ | ✔ | **3.5** | ◐ | ✘ | ✘ | 3 | 2 | 2 | **7.5** |
| AutoResearchBench | GEN | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ◐ | 3 | 3 | 2 | **8.5** |
| ScholarQuest | IR, AI | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | **2.5** | ✘ | ✘ | ✘ | 3 | 3 | 3 | **9** |
| R³-Bench | ALGO | ? | ✘ | ✔ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| EngDesign | OS, ARCH | ✘ | ✘ | ◐ | ? | ✘ | ✘ | ◐ | **1** | ◐ | ✔ | ✔ | 3 | 1 | 3 | **9.5** |
| TCS-Bench | THEO | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | **1** | ✘ | ✘ | ◐ | 1 | 2 | 2 | **5.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [TCS-Bench](../works/tcs-bench.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [ScholarQuest](../works/scholarquest.md)
- [CORE-Bench](../works/core-bench.md)
- [EngDesign](../works/engdesign.md)
- [R³-Bench](../works/r3-bench.md)
