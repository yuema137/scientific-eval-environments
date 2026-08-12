---
name: domain-backfill
description: Run a targeted historical coverage backfill for one canonical domain of this knowledge base — broad multi-source discovery, parallel primary-source deep review, Topic/Domain/Activity integration, Chinese mirror with independent review, and one reviewable PR. Use when a domain page is thin and the maintainer asks to backfill, expand, or historically fill a domain. Not for the automated daily update.
---

# Domain Backfill

A targeted historical backfill of **one canonical domain**. Manual and maintainer-initiated, entirely
separate from the automated daily Update Agent.

**Reference implementation:** PR #35, Chemical Engineering, 1 → 12 works. Everything here was proven there.

## Hard boundaries

- **Never touch the Update Agent**: `.github/workflows/`, `automation/update_agent/`,
  `scripts/update_agent/` (except *running* `validators.py`), `runtime/`, its schedule, models,
  budgets, or watermark. Verify at the end: `git diff main -- .github/ automation/ runtime/` is empty.
- **The daily updater's top-N discovery budget does not apply.** This is a targeted backfill; control cost
  with batching and parallel waves, never by truncating the candidate list.
- Do not redesign any taxonomy, build new automation, or refactor the repository.
- Do not invent weak entries to raise a domain count. A smaller, well-evidenced set is the better outcome.

## Inputs

One **domain profile** — the only domain-specific input. See `profiles/_TEMPLATE.md`, and
`profiles/chemical_engineering.md` for a worked example. A profile supplies:

| Field | Purpose |
|---|---|
| Canonical domain name + page file | The target |
| Scope / what belongs | Positive definition |
| Boundaries vs neighbouring domains | The hard part — where misclassification happens |
| Search vocabulary | Terms beyond the literal domain name |
| Subfield query families | The breadth engine |
| Domain software / tools / simulators | Often the highest-signal queries |
| Snowball terms | Named benchmarks, groups, venues to chase |

If no profile exists for the requested domain, write one first and confirm the boundary rules against
`AGENT.md`'s domain taxonomy before searching.

## Phases

Run these in order. Later phases depend on earlier gates.

### 0. Repository state
Read `AGENT.md`, `CLAUDE.md`, `works/README.md` (card template), the target domain page, and
`domains/README.md`. Record: current card count, current domain membership, canonical topic/domain/activity
taxonomies, card template, reverse-index conventions. **Never trust counts from a prompt** — derive them:
`git ls-tree -r main --name-only works/ | grep -c '\.md$'`.

### 1. Broad historical discovery
Not a recency window. Search the full public record across **arXiv, OpenReview, GitHub, and general
scholarly/web search**, then **snowball** (related work, cited predecessors, citing works, author groups,
project orgs).

**The literal domain name is the weakest query.** Breadth comes from the profile's query families and from
snowballing. In the reference run, the single best find (ChemEBench) surfaced only via a citation chain, and
its real primary source was a journal article, not the arXiv paper citing it.

Collect only identity-level metadata per candidate: title, authors, year, source, canonical URL, project/repo
URL, one-line relevance reason. Do not deep-read yet.

### 2. Inventory, repo-wide dedup, freeze
Build an identity index over **all existing cards**, not just the target domain page — a relevant work may
already be carded under a neighbouring domain. Dedup by arXiv ID, DOI, OpenReview ID, repo URL, normalized
title, then title+author.

Classify: `NEW CANDIDATE` / `ALREADY INDEXED` / `NEEDS IDENTITY CHECK`. An already-indexed work that belongs
in this domain is an **axis correction, never a duplicate card**.

Run one gap-check pass over the inventory as a whole (are all subfields represented? tool-mediated work?
GitHub-only projects? publisher-only work?), then **freeze the list**. Stop searching.

Also run a **read-only existing-card audit** in parallel: extract every card's `## Domains` prose, sweep it
plus full card text for domain signals, read every hit. Output `ADD_DOMAIN` / `BORDERLINE` with evidence.
Finding nothing is a real result — report it rather than forcing members.

### 3. Parallel deep review
Partition into batches of **4–6 candidates**, dispatch **4–6 subagents concurrently**, in waves if needed.
Never hand one agent the whole list.

Give each subagent `references/deep_review_brief.md` filled in for the domain. Contract:

- Read the **primary source** — original paper, official repo, project page, publisher/OpenReview record.
  Secondary summaries may aid discovery but never supply facts.
- Verify canonical identity. Discovery metadata is often wrong: in the reference run, several batches had
  **fabricated arXiv IDs with genuine DOIs**. If no real primary source exists →
  `REJECT_INSUFFICIENT_PRIMARY_EVIDENCE`. Never reconstruct plausible details.
- Exactly one decision per candidate, from the enum (`ACCEPT_NEW_CARD`, `ALREADY_INDEXED_AXIS_UPDATE`,
  `REJECT_OUT_OF_SCOPE`, `REJECT_NOT_<DOMAIN>`, `REJECT_NOT_EVALUATION`, `REJECT_DUPLICATE`,
  `REJECT_INSUFFICIENT_PRIMARY_EVIDENCE`).
- On accept, write `works/<slug>.md` only. **Subagents never touch shared files** — no topic/domain/activity
  page, no README, no `zh/`. That is what makes concurrency safe.

**The decisive scope question is almost always "benchmark or system?"** In the reference run 23 of 48
rejections were in-domain papers contributing a *system* rather than an evaluation. A system paper that also
ships a **named** dataset with a scoring protocol can be accepted; a framework demonstrated on case studies
cannot.

### 4. Card gate
Centralized audit before any axis work. Every candidate has a decision; every accept has exactly one card;
no duplicate cards; template-conformant; links valid; no placeholders; filenames kebab-case.
Run `consolidate.py` (in `scripts/`) — it also flags cards on disk with no accept record.

Two failure modes seen in the reference run, both worth checking explicitly:
- A card written from an abstract alone carried **two fabricated limitations** that full text refuted.
- Two subagents independently carded the same work. Where independent write-ups **agree**, that is strong
  evidence; where they disagree, adjudicate from the primary source and merge — do not just pick one.

Commit accepted cards here so progress survives interruption.

### 5. English axis integration
Three specialists **in parallel on disjoint files**: `topics/`, `domains/`, `activities/`.

Give each `references/axis_brief.md`. Critical asymmetry:
- **Topics and activities are two-way** reverse indexes — card block ⇆ page `## Related Works`, exact
  agreement both directions, validator-enforced.
- **Domains are one-way**, maintained on domain pages only. **Never edit a card for the domain axis.**

Reviewer-recommended labels are *recommendations*; the card text is the evidence. A specialist that finds a
label unsupported should correct it and say so. In the reference run two labels were correctly removed for
confusing tool use with an evaluated activity.

Each page's comparison table has fixed columns — **read the page's actual header row**, do not assume.
Never hand-edit a count cell; counts come from `scripts/update_counts.py`.

### 6. English gate — freeze
```
cd scripts/update_agent && python3 validators.py axes && python3 validators.py cards --slugs <all>
python3 scripts/update_counts.py            # then --check
python3 -m pytest tests/ -q
```
Plus: internal links resolve (pending `zh/` mirrors are expected at this point), no positioning language, no
temporary files committed, updater untouched. **English must freeze before any Chinese work.**

### 7. Chinese mirror
Multiple translators on **disjoint** file sets, using `references/zh_mirror_brief.md`.

English is the factual source of truth: add nothing, drop nothing. The requirement is **natural idiomatic
technical Chinese, not word-for-word** — restructure freely for Chinese syntax.

**Verify conventions against the existing corpus, not from memory.** The reference run's brief was wrong
twice and translators correctly overrode it by grepping `zh/works/`. Current conventions: `## ` headings stay
English; `## Topics` link text English; `## Activities` link text Chinese; `Repository note:` stays English;
`TODO(reference)` verbatim; Related Works separator ` — `; topic/domain pages use `[→]` while activity pages
use `[卡片]`; page titles English, table headers translated.

### 8. Independent Chinese review
**Fresh reviewers — never the translators.** Use `references/zh_review_brief.md`.

Priority order: **factual drift from English first** (the reference run caught five, including a card claiming
human verification its own Limitations denied), then literal translation, English sentence architecture, noun
stacking, unnatural 被-passives, terminology inconsistency, punctuation.

Effective techniques from the reference run: multiset-diff every numeric token between each EN/ZH pair; check
terminology against repo-wide frequency before "fixing" it; respect per-page conventions (e.g. 仿真 vs 模拟).

### 9. Final validation and PR
`axes`, `cards`, `bilingual` validators; `update_counts.py --check`; `pytest tests/`; link check both
languages; confirm updater untouched; clean tree.

Open **one** PR. Commit structure: cards → English axes → Chinese mirror → Chinese review.

PR body must include: search funnel (raw → deduped → reviewed → accepted), batch/subagent structure, every
accepted work, existing-card corrections, rejection breakdown by reason, coverage after the backfill
including **thin or absent subareas**, axes changed, Chinese files and review results, validation results.

Describe the search as *"a reasonably comprehensive targeted search across the supported public sources"* —
never as exhaustive. **Do not merge** unless the maintainer explicitly asks.

## Judgement calls

Some decisions are genuinely borderline. Make them, do not defer — but write a short decision record
(scratchpad) with the evidence and an explicit **reversal condition**, and surface it in the report. The
reference run did this for a work excluded because its domain case rested on evidence found only in a
*different* paper, and for an accepted card later overridden to reject because no quantitative detail was
verifiable behind a paywall.

Prefer excluding a work you cannot evidence over including one you cannot check.

## Reusable assets

```
references/deep_review_brief.md   → Phase 3 subagents
references/axis_brief.md          → Phase 5 specialists
references/zh_mirror_brief.md     → Phase 7 translators
references/zh_review_brief.md     → Phase 8 reviewers
scripts/consolidate.py            → Phase 4 gate
profiles/                         → domain-specific inputs
```

Fill `<DOMAIN>` placeholders from the profile before dispatching. Write working files (inventory, batches,
results, decision records) to the session scratchpad, **never into the repository**.
