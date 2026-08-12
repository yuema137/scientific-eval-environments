# Independent Chinese editorial review brief — <DOMAIN> backfill

Repo: `/home/yuema137/scientific-eval-environments`, branch `<BRANCH>`.

You are a **fresh reviewer**. You did not write these translations and you are not here to rubber-stamp them.
Read every assigned Chinese page **as a domain specialist who reads Chinese natively**, and **edit the Chinese
directly** wherever it can be better. Finding nothing is valid only if the prose genuinely reads as native
technical Chinese.

## What to look for, in priority order

1. **Factual drift from English — the highest-severity class.** Any number, unit, model name, metric, task
   count, claim, or hedge that differs from the English, or a claim present in only one language. English is
   the source of truth: fix the Chinese, never the English. Watch especially for
   *strengthened or weakened claims* ("unacceptable" → "impossible"), *invented provenance*
   ("spot-verified" → "human-verified"), added or dropped hedges, and one-way checks upgraded to mutual ones.
2. **Word-by-word translation** — Chinese tracking English word order instead of Chinese syntax.
3. **English sentence architecture** — long subordinate chains, fronted participials, stacked relative clauses.
4. **Awkward noun stacking** — modifier piles before a head noun; common in dense table cells.
5. **Unnatural passive voice** — English passives rendered with 被 where Chinese prefers active or topic–comment.
6. **Terminology inconsistency** — the same term rendered differently across pages, or clashing with
   established usage. **Check against repo-wide frequency and the source card before "fixing" anything**, and
   respect per-page conventions (a page may legitimately be uniformly 模拟 where others use 仿真).
7. **Unnatural punctuation** — English comma habits, missing 、 in lists, half-width punctuation in CJK runs.
8. **Stiff or machine-translated phrasing** generally.

## Useful technique

Verify numeric parity mechanically rather than by eye: extract every numeric token from each English/Chinese
pair and diff the multisets. Expect legitimate deltas only for Chinese numeral-scale conversions
(1 billion → 10 亿) and date forms.

## Do NOT "correct" these established conventions

Verified across the existing Chinese corpus:
- `## ` section headings stay English on work cards; `## Topics` link text English; `## Activities` link text Chinese.
- `Repository note:` stays English with Chinese text after it. `TODO(reference)` verbatim.
- Work/benchmark/metric/model/software names stay English.
- Related Works separator ` — `. Page `# Title` English; table headers translated.
- Card column: `[→]` on topic/domain pages, `[卡片]` on activity pages.
- **Never edit a count cell.** Never touch switcher lines or link paths.

## Also verify

- Topic/activity membership on each card matches its English card exactly.
- Every number in every table cell matches the English cell.
- Nothing was silently omitted from a translated section.
- Any label deliberately removed during English integration is **absent** on the corresponding Chinese page.

## Do not

- Do not touch any English file, or any file outside your assignment — other reviewers work concurrently.
- Do not restructure pre-existing Chinese content the backfill did not add.

## Report

Files reviewed; edits made with concrete before/after examples of the most substantive fixes; **any factual
drift found, flagged prominently**; and what you judged acceptable as-is. Note anything out of scope you
noticed but did not change.
