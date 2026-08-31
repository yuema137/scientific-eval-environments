# Software & Systems Engineering

> **English** | [简体中文](../zh/domains/software_systems_engineering.md) · [← All domains](./README.md)

## Scope

Building and verifying software as engineering: code generation on real repositories, environment configuration, formal specification and verification. Web/UI agents and computer use are not software engineering.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| SWE-bench | 2023 | Resolve real GitHub issues by editing the codebase of one of 12 popular open-source Python repositories. | 2,294 issue–pull-request instances; the model produces a single patch per instance. | The repository's own test suite: every FAIL_TO_PASS and every PASS_TO_PASS test must pass after applying the patch; no partial credit. | [→](../works/swe-bench.md) |
| SWE-chat | 2026 | Real-world software engineering as actually practiced: in-the-wild human–agent coding sessions on open-source repositories, spanning code understanding, creation, git operations, and debugging. | ~6,000 logged sessions from 200+ public repositories with 13,000+ checkpoints and line-level human-vs.-agent authorship attribution; observational, no authored tasks. | Commit-grounded outcomes (survival of agent code into user commits), Semgrep security scans on pre/post-commit snapshots, and LLM annotations validated against human gold labels. | [→](../works/swe-chat.md) |
| Enconda-bench | 2025 | Diagnose and repair injected errors in repository setup documentation, then build the software environment and run its tests. | 4,201 erroneous-README tasks carrying 9,471 injected errors across 323 repositories pinned to fixed commits, stratified into difficulty levels 1–10. | Docker-executed Pass@1 (environment builds, tests execute, clean exit) plus per-capability precision/recall on diagnosis and repair; each injected error validated to actually break setup. | [→](../works/enconda-bench.md) |
| AgentLens | 2026 | Interactive Java coding-assistant work on real open-source Spring Boot projects: unit testing and test refactoring, legacy database-logic migration, API documentation and DTO cleanup. | 16 interview- and production-derived scenarios, each run under a relaxed and a mildly adversarial user persona (32 trajectories per agent). | Formal verification — tests, repository-state assertions, build execution, static analysis, all must pass — combined with five LLM-judge dimensions into a Quality Index. | [→](../works/agentlens.md) |
| SysMoBench | 2025 | Write formal TLA+ models of real concurrent and distributed systems — OS synchronization primitives, Raft implementations, ZooKeeper leader election — at a granularity fixed by the task. | 11 system artifacts spanning 175–5,360 source lines in Rust, Go, C, and Java; each task requires a TLA+ model plus its TLC configuration. | Four machine-checked, sequentially gated metrics: SANY syntax, TLC runtime, trace conformance against instrumented executions, and invariant model checking; explicitly no LLM judge. | [→](../works/sysmobench.md) |
| VCoT-Bench | 2026 | Complete deliberately removed blocks — lemmas, loop invariants, assertions — of the verification chain-of-thought behind verified Rust programs in Verus. | 1,988 completion tasks derived from 150 verified Verus programs, stratified by removal ratio, proof type, and proof location. | Verus syntax check plus semantic equivalence to the ground-truth chain judged by a protocol-guided LLM (94% agreement with author consensus), combined into a weighted accuracy. | [→](../works/vcot-bench.md) |
| Long-Horizon-Terminal-Bench | 2026 | Long-horizon terminal workflows including software engineering and scientific computing, alongside experiment reproduction, multimodal analysis, and interactive games. | 46 tasks across nine categories, each decomposed into fine-grained graded subtasks. | Dense graded subtask rewards with configurable pass thresholds (best model: 15.2% pass@1 at a 0.95 threshold, 10.9% at 1.0). | [→](../works/long-horizon-terminal-bench.md) |
| FrontierCode | 2026 | Produce maintainer-mergeable pull requests in real open-source repositories — an industry benchmark with no accompanying paper. | Maintainer-written tasks authored by 20+ experienced developers at 40+ hours per task; task counts unpublished. | Mergeability graded by an ensemble of unit tests, rubrics, and verifiers over correctness, test quality, scope discipline, and style; solution-consulting runs scored zero. | [→](../works/frontiercode.md) |
| SWE-Interact | 2026 | Complete software-engineering tasks whose requirements arrive progressively from a simulated user. | Multi-turn user-driven sessions paired with single-turn baselines on the same tasks. | Task success under the interactive protocol versus single-turn (~50% vs. ~25% for top models). | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | Collaborate with a user on repository-level coding tasks reconstructed from real sessions. | 109 tasks curated from 11,260 recorded sessions, replayed via an intent-preserving user simulator. | Final repository correctness plus the number of corrective feedback turns required. | [→](../works/swe-together.md) |
| AInsteinBench | 2025 | Maintain production-grade scientific software: resolve maintainer-PR-derived tasks in six widely used codebases. | Repository-level coding-agent tasks curated by multi-stage filtering and expert review. | Test-driven verification in executable environments with scientifically meaningful failure modes. | [→](../works/ainsteinbench.md) |
| SWE-Bench ProMax | 2026 | Perform large-scale code refactoring — coordinated, behavior-preserving changes spanning many files — in real multilingual open-source repositories (Python, Java, TypeScript, Go, C, C++, Rust). | 170 expert-curated real-commit refactoring instances averaging 11.4 modified files and 261.6 lines per instance; issue descriptions rewritten from scratch and test suites manually pruned of overly narrow/broad tests. | Execution-based resolve rate against the manually reviewed per-instance test suites; best evaluated model reaches 41.2%. | [→](../works/swe-bench-promax.md) |
| Plan Compliance in Programming Agents | 2026 | Measure whether coding agents given a task-specific plan actually follow it while resolving real GitHub issues, and how plan deviations relate to issue-resolution success. | 16,991 SWE-agent trajectories across four LLMs on SWE-bench Verified (500 instances) and SWE-bench Pro (266 Python instances) under eight plan settings (removal, augmentation, reordering, reminders, no-plan). | SWE-bench-style patch verification (issue-resolution success against the repository test suite) compared across plan settings, alongside plan-compliance metrics (Plan Phase Compliance, Plan Order Compliance, Plan Phase Fidelity). | [→](../works/from-plan-to-action.md) |
| RACE-Bench | 2026 | Repository-level feature addition — implement a new feature in a real open-source codebase so the associated tests pass — evaluated jointly on patch correctness and on how the agent's intermediate reasoning aligns with developer-accepted trajectories. | 528 real-world feature-addition instances from 12 open-source repositories, each paired with an executable patch-verification harness and structured reference reasoning (issue understanding, file localization, implementation tasks, step decomposition). | Dual-track: executable test-based Resolved Rate (29–70% across three agents) plus reasoning-alignment coverage against developer-accepted reference trajectories. | [→](../works/race-bench.md) |
| LoopsBench | 2026 | Sustained, multi-step software development ("loop engineering") — make forward progress on long-horizon coding work while avoiding regressions to earlier completed units. | 112 tasks from authentic sources spanning 8 programming languages and 9 domains, each a dependency DAG over 5,300+ separately testable development units with source-evidenced prerequisite edges. | Execution-based scoring via a Docker-backed flow-aware runtime that releases tests along the ready frontier and retains completed nodes as regression obligations; verifiers distinguish incomplete/partial/complete solutions. Best configuration resolves 25.0% of tasks. | [→](../works/loopsbench.md) |
| SWE-RPG | 2026 | Repository-level issue resolution — bug fixing and feature addition in real Python and Java projects — diagnosed across the full trajectory (requirement clarification → implementation planning → code generation → submission) rather than by pass/fail alone. | 163 tasks from 31 Python and Java repositories (113 bug fixes, 50 feature additions), each with an executable fail-to-pass/pass-to-pass harness plus validated intermediate ground truths for Requirement Clarification and Implementation Planning; three agents across six LLM backends. | Execution-based resolved rate (patch applies, all fail-to-pass pass, no pass-to-pass regresses; avg 31.5%, best 49.7%), plus LLM-judge stage attribution and per-stage coverage calibrated against human consensus (92%/96%). | [→](../works/a-unified-issue-resolution-benchmark-for-requireme.md) |
| EngDesign | 2025 | Operating system and computer architecture design delivered as a functional artifact — a system design that must work under its stated constraints rather than match a reference answer. | Operating System Design (8) and Computer Architecture Design (5) of 101 design tasks / 473 gradable items across nine engineering areas; single-turn by default plus an iterative protocol of up to 10 revision rounds on simulator feedback. | Per-task evaluation scripts execute the produced design and return a binary pass, a 0–100 partial-credit score and a log; over the whole benchmark the best model rises from a 34.38% first-attempt pass rate to almost 60% after ten iterations. | [→](../works/engdesign.md) |
| RigorBench | 2026 | Engineering process discipline in software work — multi-file feature implementation, diagnosis and repair of subtle bugs, recovery from failing first attempts, abstention on impossible or ambiguous specifications, and checkpointed multi-step refactoring — measured over how the solution was reached rather than by outcome alone. | 100 tasks, 20 in each of five categories, each shipping a starter repository in Node.js/Express, Python, Rust or Django; roughly 410 task executions across four agentic harnesses running on the same foundation model. | Trajectory-based scoring of seven pillars with published sub-metric formulas — planning fidelity, verification coverage, recovery efficiency, abstention quality, atomic transition integrity, test assertion density, exploration efficiency — combined into a composite RigorScore, with build and test health checked programmatically in an isolated Docker environment and only qualitative sub-metrics left to an LLM judge; an outcome score is measured separately on the same runs. | [→](../works/rigorbench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the software and systems engineering subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`MAINT` software maintenance & evolution (issue resolution, bug fixing, refactoring) · `FEAT` feature development & repository-level implementation · `TEST` software testing & quality assurance · `FV` formal specification & program verification · `DIST` distributed & concurrent systems · `OS` operating systems & systems programming · `ARCH` computer architecture & hardware design · `CFG` build, dependency & environment configuration · `REQ` requirements engineering & intent elicitation · `PROC` software process, planning & engineering discipline · `HAI` human–agent collaboration & developer interaction · `SCISW` scientific & research software engineering · `GEN` curriculum-wide or unspecified, no single subfield

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
| SWE-chat | HAI, MAINT | ✔ | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **4.5** | ✔ | ◐ | ◐ | 2 | 3 | 3 | **10** |
| Long-Horizon-Terminal-Bench | GEN | ? | ✘ | ◐ | ◐ | ◐ | ◐ | ✔ | **3** | ✘ | ✔ | ◐ | 3 | 1 | 3 | **8.5** |
| AgentLens | TEST, MAINT, HAI | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✔ | ◐ | 2 | 1 | 3 | **7.5** |
| Enconda-bench | CFG | ✔ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ✘ | ✔ | 2 | 3 | 3 | **9.5** |
| LoopsBench | FEAT, PROC | ✘ | ✘ | ◐ | ✘ | ◐ | ✘ | ✔ | **2** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| SWE-Together | HAI | ✘ | ◐ | ◐ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ✔ | ✘ | 2 | 2 | 2 | **7.5** |
| RigorBench | PROC, MAINT, TEST | ? | ✘ | ✔ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✔ | ◐ | 2 | 2 | 2 | **7.5** |
| SWE-Interact | HAI, REQ | ? | ◐ | ◐ | ✘ | ✘ | ✘ | ✔ | **2** | ◐ | ◐ | ✘ | 2 | 1 | 3 | **7** |
| FrontierCode | MAINT, TEST | ✔ | ✘ | ? | ? | ✘ | ✘ | ✔ | **2** | ◐ | ✔ | ✔ | 2 | ? | 0 | **4.5** |
| SWE-Bench ProMax | MAINT | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✔ | 3 | 2 | 3 | **9.5** |
| SWE-RPG | MAINT, FEAT, REQ | ? | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✔ | ◐ | 2 | 2 | 3 | **9** |
| EngDesign | OS, ARCH | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✔ | ◐ | 3 | 1 | 3 | **8.5** |
| RACE-Bench | FEAT | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ◐ | ✘ | 2 | 2 | 3 | **8** |
| Plan Compliance in Programming Agents | MAINT, PROC | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ◐ | 3 | 2 | 4 | **10** |
| SysMoBench | FV, DIST, OS | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | 1 | 3 | **7.5** |
| AInsteinBench | SCISW, MAINT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | 2 | 2 | **7.5** |
| SWE-bench | MAINT | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ◐ | ✘ | ◐ | 3 | 3 | 3 | **10** |
| VCoT-Bench | FV | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 3 | 3 | **8.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [SWE-Bench ProMax](../works/swe-bench-promax.md)
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md)
- [LoopsBench](../works/loopsbench.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [AgentLens](../works/agentlens.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
- [RigorBench](../works/rigorbench.md)
- [FrontierCode](../works/frontiercode.md)
- [SWE-chat](../works/swe-chat.md)
- [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md)
- [RACE-Bench](../works/race-bench.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [Enconda-bench](../works/enconda-bench.md)
- [SysMoBench](../works/sysmobench.md)
- [EngDesign](../works/engdesign.md)
- [SWE-bench](../works/swe-bench.md)
