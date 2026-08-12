# Axis-integration brief — <DOMAIN> backfill

Repo: `/home/yuema137/scientific-eval-environments`, branch `<BRANCH>`.

The English work cards are **already written, verified and committed**. Your job is to wire them into
**one axis**. Three specialists run concurrently on disjoint files — stay strictly inside your axis.

## Inputs

- `<SCRATCH>/accepts_final.json` — the authoritative frozen accept list. Each element carries
  `slug_if_accepted`, `topics[]`, `domains[]`, `activities[]`.
  These labels are **recommendations from the deep reviewer**. Verify each against the card text and correct
  it where the card does not support it. **The card is the evidence.**
- `<SCRATCH>/existing_domain_audit.json` — (domain specialist) already-indexed cards that should gain
  membership. May be empty; an empty audit is a real finding, not a reason to hunt further.
- Any decision records in `<SCRATCH>/*_DECISION.md` — **already-settled calls. Do not reopen them.**
- The cards themselves under `works/<slug>.md`.

## Hard rules (all specialists)

- **Never redesign a taxonomy.** Canonical labels only. Never create a topic, domain, or activity.
- **Never touch `zh/`.** The Chinese mirror is a later phase, after the English freeze.
- **Never hand-edit a count cell** in any README or index table. Counts come from
  `python scripts/update_counts.py`, which the coordinator runs at the end.
- Do not rewrite existing cards or existing rows beyond what your axis requires.
- Every cell you write must be **verifiable from the card**. Read each card before writing its row.
  No invention, no marketing language, no positioning.
- **Read each page's actual table header row and match it exactly.** Column sets differ between pages and
  between axes; do not assume the set given in any brief.
- Match the surrounding style: row phrasing, tense, level of detail, and ordering convention.

## Reverse-index contract — note the asymmetry

- **Topics and activities are TWO-WAY**: the card's `## Topics` / `## Activities` block and the page's
  `## Related Works` must agree exactly, in both directions. A validator enforces this.
- **Domains are ONE-WAY**, maintained on domain pages only. **Never modify a card for the domain axis.**
  A card's `## Domains` prose is the assignment evidence, not a link block.

## Per-axis instructions

### Topic specialist — owns `topics/*.md`
Confirm each work's topic labels from its card, then add it to every claimed topic page: a row in
`## Comparison` and a link in `## Related Works`. Where a page carries a synthesis section
(`## Existing Approaches`), add bullets **only** for works contributing a distinct angle the section lacks —
a small number of strong bullets, never one per work. If a work merely instantiates an existing bullet,
extend that bullet with a clause instead. Keep the established bullet style. Do not touch `topics/README.md`.

### Domain specialist — owns `domains/*.md`
Usually the highest-value axis for a backfill.
- Add every accepted work whose card evidence supports the target domain, plus every `ADD_DOMAIN` entry from
  the audit. Treat `BORDERLINE` entries as judgement calls — include only with card evidence, and report
  what you included and excluded.
- Add accepted works to any **other** domain pages their card evidence supports. Co-domains are expected.
- **Do not force works into the target domain because this is that domain's backfill.** If a card's evidence
  says otherwise, leave it out and say so.
- Keep `## Related Works` in sync with your table rows on every page you touch.
- If the target page's `## Scope` is a bare one-liner, you may expand it into a short factual paragraph
  grounded in the actual member works, with an explicit boundary against the nearest neighbouring domain.
  No speculation, no positioning.

### Activity specialist — owns `activities/*.md`
Confirm each work's activity labels against the card **and against the target page's own `## Scope` rules** —
those scopes contain the decisive tests (for example, a benchmark does not earn a simulation activity merely
because a simulator runs somewhere inside it; the evaluated agent must substantially construct, configure,
execute, or debug it). Add a row to each claimed page's `## Comparison` and a link in `## Related Works`.
Extend `## Task Patterns` only where a work genuinely adds a pattern the section does not describe.

If a card's activity label is unsupported by its own evidence, you **may** edit that card's `## Activities`
block — but the page and card must still agree exactly afterwards, and you must report the change and your
reasoning. Do not touch `activities/README.md`.

## Finish

Run `cd scripts/update_agent && python3 validators.py axes`. Errors owned by the other two specialists may
appear while they are still working — report them but do **not** fix them.

Report: pages changed, rows added per page, any label you corrected away from the reviewer's recommendation
and why, and anything you deliberately did not do.
