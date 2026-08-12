# Chinese mirror brief — <DOMAIN> backfill

Repo: `/home/yuema137/scientific-eval-environments`, branch `<BRANCH>`.
The English side is **frozen** and is the factual source of truth: never add a claim, number, or hedge that
is not in the English source, and never drop one.

## The central requirement

**Natural, idiomatic technical Chinese — not word-for-word translation.** Literal renderings, English
sentence architecture, awkward noun stacking, and unnatural 被-passives are defects, not stylistic quibbles.
A domain reader should experience the page as if it were written in Chinese. Restructure sentences freely —
break long subordinate chains into Chinese clause sequences, unstack premodifier piles, prefer active and
topic–comment constructions — as long as the facts are identical.

Keep in English: work and benchmark names, domain software names, metric and statistic symbols, model names,
code identifiers, and the canonical topic link text. Numbers and units exactly as in English.

## Verify conventions against the corpus, not from memory

**This brief has been wrong before.** In the reference run, translators correctly overrode it by grepping
`zh/works/`. Before writing, confirm each convention yourself, e.g.:

```bash
grep -rl "仓库注记" zh/works/ | wc -l      # vs
grep -rl "Repository note" zh/works/ | wc -l
```

If the corpus disagrees with this brief, **follow the corpus** and report the discrepancy.

### Conventions as last verified

**Work cards `zh/works/<slug>.md`**
- Switcher line exactly: `> [English](../../works/<slug>.md) | **简体中文**`
- **`## ` section headings stay in ENGLISH** (`## Overview`, `## Tasks`, `## Evaluation`, …), including
  `## Activities` — note `CLAUDE.md` documents `## 研究活动`, but the corpus uses `## Activities`.
- **`## Topics` link text stays ENGLISH.**
- **`## Activities` link text is CHINESE**, with these fixed labels:

  | slug | label |
  |---|---|
  | `literature_evidence_synthesis` | 文献检索与证据综合 |
  | `scientific_problem_solving_reasoning` | 科学问题求解与推理 |
  | `data_analysis_statistical_inference` | 数据分析与统计推断 |
  | `modeling_prediction` | 建模与预测 |
  | `simulation_scientific_computing` | 模拟与科学计算 |
  | `experiment_design_discovery` | 实验设计与科学发现 |
  | `laboratory_instrument_control` | 实验室与仪器控制 |
  | `optimization_engineering_design` | 优化与工程设计 |
  | `scientific_software_workflow_engineering` | 科学软件与工作流工程 |
  | `research_reproduction_replication` | 研究复现与重复 |
  | `end_to_end_research` | 端到端研究 |

- Link **paths identical** to the English card; topic/activity membership must match exactly (validator-enforced).
- `TODO(reference)` verbatim, explanation after it in Chinese.
- **`Repository note:` stays in English**, with the note text in Chinese after it.
- `**Reported.**` renders as `**报告。**`. Related Works separator is ` — `. `N/A — ` keeps its form
  (single em dash; the corpus is ~99:10 against `—— `).
- **Quoted source text uses corner quotes 「」**, not `"…"` — the corpus runs ~532 to 20 in their favour.
  Leave a genuinely English quoted string (a verbatim prompt, a flag) in ASCII quotes.
- When the English `Typical Duration` opens with a **backticked** `` `N/A — …` `` sentence, the corpus keeps
  that sentence in English verbatim and continues in Chinese; when it is unbackticked prose, translate it.
- **Do NOT translate institution names.** Universities, labs, companies and agencies stay in their original
  form (University of Toronto, Florida International University, FHWA). Some older cards translate them;
  that is not the convention to follow. Model, tool, metric and benchmark names likewise stay as-is.
- Long descriptive English work titles stay English in the `# ` heading.

**Axis pages under `zh/`**
- Page `# Title` stays English; **table column headers ARE translated** — read the existing Chinese page and
  reuse its exact header row rather than inventing one.
- The `Work` column keeps the English work name.
- Card column: topic and domain pages use `[→]`, activity pages use `[卡片]` — follow each page's own usage.
- Mirror any English `## Task Patterns` / `## Existing Approaches` prose extensions too.

## Do not

- Do not hand-edit any count cell — counts come from `scripts/update_counts.py`.
- Do not touch any English file, or any `zh/` file outside your assignment.
- Do not reorder or restructure pre-existing Chinese content the backfill did not add.

## Finish

Run `cd scripts/update_agent && python3 validators.py bilingual --slugs <your slugs>` and report the result,
plus any place where natural Chinese required notable restructuring of the English.
