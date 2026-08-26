# Energy Systems

> **English** | [简体中文](../zh/domains/energy_systems.md) · [← All domains](./README.md)

## Scope

Energy systems engineering: power, renewables, and energy research.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Energy is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| PowerAgentBench-SS | 2026 | Run power-system steady-state studies: contingency screening and admissible mitigations on grid cases. | Agentic tool-use studies over IEEE 39-bus operating-point variants with a DC thermal N-2 contingency-search pilot, under a validation budget. | A hidden evaluator recomputes physical validity; recall variants, false-safe penalties, severity regret, action cost, tool-use efficiency. | [→](../works/poweragentbench-ss.md) |
| ElecBench | 2024 | Reason about power-grid operation and dispatch under stability, security, and economic constraints. | Power-dispatch evaluation across general-knowledge and professional-business scenarios; 8 LLMs. | Six metrics (factuality, logicality, stability, security, fairness, expressiveness) / 24 sub-metrics. | [→](../works/elecbench.md) |
| EnergyBridge | 2026 | Residential virtual-power-plant operation and demand response — convert household physical flexibility into dependable, authorized grid capacity by coupling capacity reporting, household authorization, and physical execution of HVAC/EV/appliance load shifting. | 50 seven-day EnergyPlus building-energy simulations across five households, two regions (Tianjin, Berlin), and five methods (350 household-day episodes; one 18:00–19:00 demand-response event each), plus a held-out capacity-reporting audit; an LLM User Participation Simulator decides authorization. | Physical outcomes metered from EnergyPlus 24.1.0 — gate-acceptance (authorization) rate, event-window energy, and capacity-commitment reliability (accepted ∧ delivery within ±20% of the commitment); the authorization simulator validated against 584 human role-play responses (5.3-pp mean absolute acceptance error). | [→](../works/energybridge.md) |
| Hydro-SE Bench | 2025 | Power systems as one of the nine subfields of hydro-science and engineering, reflecting the hydropower side of water-conservancy works. | 4,000 Chinese-language single- and multi-choice questions across nine subfields including Power Systems, each labelled by cognitive level (conceptual / engineering application / reasoning and calculation); 16 models, ten commercial and six open-source. Per-subfield question counts are given only as a figure in the paper. | Accuracy reported overall and by subfield, question type and cognitive level, queried zero-shot with chain-of-thought at temperature 0 and the choice letter extracted by a separate LLM; commercial models fall in the 0.74–0.80 band and open-source models in 0.41–0.68. | [→](../works/hydro-se-bench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the energy systems subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`PWR` power-system operation & dispatch · `GRID` transmission & distribution grid planning and reliability · `MKT` electricity markets & energy economics · `REN` renewable generation (wind, solar) · `HYD` hydropower · `NUC` nuclear energy engineering · `THERM` thermal power & combustion generation · `STOR` energy storage & batteries · `PE` power electronics & conversion · `DR` demand response & virtual power plants · `BLDG` building energy & HVAC systems · `EV` transport electrification & EV charging · `H2` hydrogen & alternative fuels · `POL` energy-system planning & policy modeling · `GEN` curriculum-wide or unspecified, no single subfield

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
| EnergyBridge | DR, BLDG | ✘ | ✘ | ◐ | ✘ | ✘ | ◐ | ✔ | **2** | ✘ | ✘ | ✘ | 2 | 2 | 4 | **8** |
| PowerAgentBench-SS | PWR, GRID | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ◐ | 3 | 0 | 2 | **5.5** |
| Hydro-SE Bench | HYD, PWR | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 2 | ? | 3 | **6** |
| ElecBench | PWR | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✘ | 1 | ? | 0 | **2** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [EnergyBridge](../works/energybridge.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [ElecBench](../works/elecbench.md)
