# Cognitive Agents for Bridge Inspection Prioritization (2026)

> **English** | [简体中文](../zh/works/cognitive-agents-for-bridge-inspection-prioritizat.md)

> **First appeared:** 2026-07-29 · **Source:** [engrxiv public posting](https://engrxiv.org/preprint/view/7703)

## Overview

An empirical evaluation that places a standards-grounded LLM agent for highway-bridge inspection prioritization against three non-LLM baselines on six consecutive annual National Bridge Inventory (NBI) snapshots, scoring every method against observed future bridge deterioration and adding an independent blind rating of the agent's written rationales by a licensed bridge inspector.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://engrxiv.org/preprint/view/7703>
- **Venue:** engrXiv preprint (posted 2026-07-29; submission date given in the manuscript as 2026-07-23)

## Summary

The study asks two questions about an LLM agent applied to a regulated civil-infrastructure decision: how much of sustained bridge deterioration is predictable from inventory data at all, and what auditable reasoning contributes when that predictive signal is weak. Four prioritization methods — the fixed 24-month calendar cycle that represents present practice, a transparent weighted rule-based risk index, a cross-validated gradient-boosted ensemble, and a retrieval-grounded LLM agent — are run on an identical analytic sample of Connecticut bridges and scored against three progressively more specific definitions of observed future deterioration. The agent matches the transparent index on ranking performance (per-bridge priority scores correlate at r = 0.85) and trails the statistical learner on the two outcomes where the learner recovers signal, while both interpretable methods beat the opaque learner on the policy-relevant poor-condition outcome. The authors frame the contribution as a reproducible benchmark of how outcome definition governs predictability, and position language-model agents in a measured accuracy-versus-transparency tradeoff rather than claiming predictive superiority.

## Tasks

The evaluated task is per-bridge inspection prioritization from a structured NBI record. The agent receives one bridge record as a structured prompt and returns three fields: a priority score on a 0–100 scale, a recommended inspection interval expressed relative to the default 24-month cycle, and a written rationale naming the driving condition and exposure factors and referencing the governing standard; scores are additionally binned into high, medium and low tiers. Inputs are a fixed set of NBI data items — deck, superstructure and substructure condition ratings (Items 58, 59, 60), average daily traffic (Item 29), year built (Item 27), year reconstructed (Item 106), percent truck traffic (Item 109), scour-critical rating (Item 113), and structure type, deck type and deck protection (Items 43A, 107, 108C). Task instances come from six annual FHWA NBI releases (2020–2025) filtered to Connecticut (state code 09), which contain 4,353–4,365 bridge records per year. Bridges were matched across releases on structure number (Item 8): 4,383 unique structure numbers appear, of which 4,331 (98.8%) appear in all six years. Restricting to structures present in all six years with valid ratings on all three components in both the 2020 pre-period year and the 2021 decision year yields an analytic sample of 3,389 bridges (mean age 55 years at the decision year, range from new construction to 180 years, median average daily traffic 8,100). Culverts, which carry no separate component ratings, are excluded — Connecticut contained 676 in 2021. The agent produced a recommendation for 3,365 of the 3,389 bridges, the remainder excluded for non-numeric condition codes, and all four methods are compared on that common set.

## Domains

Civil & Structural Engineering — highway bridge inspection and infrastructure asset management. The evaluated objective is a regulated civil-engineering decision: which physical bridges an agency should inspect first and at what interval, judged against recorded deterioration of deck, superstructure and substructure components on the FHWA zero-to-nine condition scale, with the agent's reasoning grounded in the National Bridge Inspection Standards and the AASHTO *Manual for Bridge Element Inspection* (2nd ed., 2019). No co-domain is claimed; the deterioration modelling is applied to bridge structures rather than to an earth-science or generic-ML object.

## Evaluation

Two independent evaluation channels are used. **Ranking performance:** ground truth is sustained deterioration — a condition-rating drop from the 2021 decision year that persists to the final observed year 2025, rather than a single-year change that reverses — under three outcome definitions of increasing specificity: a decline of at least one point in any of the three components (base rate 0.246), a decline of at least one point in the deck rating specifically (0.111), and a bridge crossing from fair or better into poor condition (0.022). Each method's ranking is scored by area under the ROC curve, average precision, and precision at fixed list depths (precision@300 is tabulated). Reported AUCs are: any-component — calendar 0.485, rule-based index 0.476, statistical learner 0.594, agent 0.471; deck-only — 0.486, 0.472, 0.615, 0.471; crossing into poor — 0.500, 0.709, 0.521, 0.705. Agent and rule-based index priority scores correlate at r = 0.85 across the inventory. **Rationale quality:** a licensed bridge engineer holding National Highway Institute inspection certification independently reviewed a stratified sample of 100 agent rationales drawn across the full range of assigned priority scores, blind to each bridge's predictive outcome, judging only whether the stated reasoning was sound, identified the governing condition or exposure factor, and was consistent with the priority score and interval produced. Each rationale received a single 0–3 rating on a poor/weak/good/excellent rubric; the mean was 2.77, with 79 rated excellent, 19 good, 2 weak and none poor.

## Typical Duration

TODO(reference) — the paper reports no wall-clock, token or trajectory-length budget. The only structural statement is that the agent is invoked once per bridge record through a programmatic interface, producing 3,365 independent single-record recommendations; a design in which one model call ranks the whole inventory was explicitly rejected as unscalable and untraceable.

## Main Contribution

The authors state three contributions: a fully reproducible benchmark showing that the predictability of bridge deterioration from inventory data depends strongly on how the outcome is defined — ranging from near-random for a vague target to substantial for specific, policy-relevant targets; a positioning of language-model agents within a measured tradeoff between predictive accuracy and transparency rather than an assertion of predictive superiority the data do not support; and a connection of the empirical results to the human-oversight, integration and trust requirements that govern whether such an agent could be deployed.

## Key Design Ideas

- A baseline ladder that brackets the agent from both sides: the calendar cycle fixes present practice, the transparent rule-based index isolates what an auditable hand-written formula achieves, and the gradient-boosted ensemble (five-fold stratified cross-validation, so no bridge contributes to its own prediction) isolates the predictive ceiling available without a transparency constraint.
- Outcome definition is treated as an experimental variable rather than a fixed choice — the same inputs and methods are re-scored under three targets, exposing that ranking quality is governed largely by how the target is posed.
- "Sustained" deterioration (a decline that persists to the final observed year) is required, explicitly to blunt the known inter-inspector variability in NBI condition ratings.
- The agent is grounded by retrieval over federal and AASHTO bridge-inspection standards, constraining it to reason within established engineering guidance rather than unconstrained prior knowledge.
- Per-bridge independent scoring keeps every recommendation auditable at the asset level at which a state DOT acts.
- Rationale quality is measured separately from ranking accuracy, by a blinded certified practitioner against a written rubric, so that transparency is evaluated as an outcome in its own right rather than asserted.

## Strengths

- Ground truth is observed future condition over a four-year forward window rather than a held-out label from the same snapshot, and all four methods are scored on one identical common set of 3,365 bridges.
- The expert-review protocol is unusually well specified for this kind of study: certified reviewer, stratified sample across the priority range, blinding to outcome, an explicit four-level rubric, and a reported rating distribution rather than only a mean.
- The paper reports a negative result about its own proposed method — the agent shows no predictive advantage over a simple weighted index — and diagnoses why, showing that subsequent deterioration rate is nearly flat (about 0.24 to 0.27) across decision-year condition ratings 5 through 8 and that no single input variable exceeds AUC 0.53 on the broad outcome.
- The expert's substantive criticisms are reported rather than summarized away: underweighting of scour vulnerability, inconsistent application of risk-based interval logic, and the point that an interval may be lengthened or shortened but never eliminated, with any interval beyond 24 months requiring evidence-based justification under the National Bridge Inspection Standards.
- Inputs are public FHWA data identified by NBI item number, and the sample construction is described step by step, so the setup is reconstructible.

## Limitations

- Coverage is a single state over a six-year window; the authors note that predictability may differ across inventories, climates and inspection practices.
- Ground truth is the coded condition rating, a human judgment subject to inter-inspector variability, so the study measures prediction of *recorded* rather than physical deterioration.
- The statistical learner was not exhaustively tuned, which bounds the strength of the accuracy comparison.
- The specific language model backing the agent is not identified in the manuscript — TODO(reference). The acknowledgement records only that Claude was used to support drafting of the paper.
- No code, prompt, retrieval corpus or result artifact is released with the preprint, and no release statement is made; only the underlying NBI data is public. The "reproducible benchmark" claim therefore rests on the described procedure rather than on a distributed harness.
- Repository note: the manuscript is internally inconsistent about the statistical learner's headline numbers — the Conclusion states areas under the curve of 0.68 and 0.83 for the deck and poor-condition outcomes, which contradicts Table 5 (0.615 for deck-only, and 0.521 for crossing into poor). This card reports the Table 5 values.
- Repository note: this is an unrefereed preprint; no peer-reviewed version was located at review time.

## Related Works

- [StructureClaw](./structureclaw.md) — the other agent evaluation whose scored object is a civil/structural engineering result rather than a document operation.
- [AEC-Bench](./aec-bench.md) — agentic evaluation over real construction document sets, graded by task-specific verifiers on structured engineering findings.
- [SGR-BIM](./sgr-bim.md) — also pairs a civil-engineering agent with an expert-verified evaluation set and a multi-dimension rubric, for code compliance rather than inspection prioritization.
