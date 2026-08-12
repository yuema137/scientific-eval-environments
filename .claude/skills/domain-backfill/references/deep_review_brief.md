# Deep-review brief — <DOMAIN> backfill

> Fill every `<...>` placeholder from the domain profile before dispatching. Give each subagent this brief,
> its batch file path, and its results path.

You deep-review a small batch of candidate works for the knowledge base at
`/home/yuema137/scientific-eval-environments` (branch `<BRANCH>`).
The repo catalogs how AI/LLM **agents are EVALUATED** on scientific/engineering tasks.

## For EACH candidate in your batch

1. **Find and read the PRIMARY source.** Use WebFetch and WebSearch. For an arXiv id fetch
   `https://arxiv.org/abs/<id>`; also fetch the GitHub repo / project page / OpenReview / publisher record
   where relevant. **Verify canonical identity** — candidate metadata is frequently wrong, and fabricated
   arXiv IDs alongside genuine DOIs are common. If you cannot locate a real primary source, decide
   `REJECT_INSUFFICIENT_PRIMARY_EVIDENCE`. Never invent facts; never judge from the title alone.
   If a publisher blocks fetching (403/CAPTCHA), try Crossref, OpenAlex, Semantic Scholar, or an author copy
   before giving up — but an abstract alone is not a basis for a card's statistics.
2. **Decide scope** using the rules below.
3. Return exactly one decision from the enum with a concise evidence-based reason.
4. For `ACCEPT_NEW_CARD`, WRITE the full English card AND return axis recommendations.

## Scope — IN

The work's **substantive contribution** is an agent benchmark, evaluation environment, executable task
environment, evaluation methodology, or benchmark suite, AND its evaluated tasks are materially **<DOMAIN>**:

<DOMAIN_SCOPE — the profile's positive definition, listing real subareas>

Evaluation-focused RL on agents is in scope only if evaluation itself is the primary contribution.

## Scope — boundaries (reject when these apply)

- **Application, not evaluation:** a paper that merely *uses* an LLM/agent to solve a domain problem, or
  proposes an architecture / multi-agent system with **no benchmark or evaluation contribution** →
  `REJECT_NOT_EVALUATION`. A system paper that ALSO contributes a **named** benchmark/dataset with a scoring
  protocol can be `ACCEPT`. **This is the single most common rejection** — apply it carefully in both
  directions.
- **Ordinary ML:** prediction/modeling or an ML benchmark with no agent-evaluation component →
  `REJECT_OUT_OF_SCOPE`.
- **Pure training:** RL/controller policy training with no evaluation contribution → `REJECT_OUT_OF_SCOPE`.
- **Neighbouring domain:** <BOUNDARY_RULES — the profile's boundary table, e.g. "generic FEM is not
  automatically <DOMAIN>"> → `REJECT_NOT_<DOMAIN_TOKEN>`.
- **Survey/position:** a pure survey or perspective is `REJECT_OUT_OF_SCOPE` UNLESS it is a substantive,
  citable survey specifically about **agent/LLM evaluation** in this domain — then `ACCEPT_NEW_CARD` with
  Topic = Survey, `N/A` Tasks/Evaluation, and a single `N/A — <reason>` Activities line. A general
  "opportunities and challenges" applications review does **not** qualify.
- Tool use does NOT by itself place a work in this domain — the evaluated **objective** must be a domain task.

Cross-domain membership is allowed and expected when the evaluated tasks genuinely support it.

## Decision enum (exactly one per candidate)

`ACCEPT_NEW_CARD` · `ALREADY_INDEXED_AXIS_UPDATE` · `REJECT_OUT_OF_SCOPE` · `REJECT_NOT_<DOMAIN_TOKEN>` ·
`REJECT_NOT_EVALUATION` · `REJECT_DUPLICATE` · `REJECT_INSUFFICIENT_PRIMARY_EVIDENCE`

## Card template (COPY VERBATIM — do not add or remove sections)

Write to `works/<slug>.md`. `<slug>` = kebab-case of the work's canonical short name (`ceprobench`,
`pse-bench`). If a work has no short name, the repo also accepts a truncated-title slug (50-char stem).
First run `ls works/` to confirm the slug is free and to pick Related Works links that actually exist.

```markdown
# <Work Name> (<Year>)

> **English** | [简体中文](../zh/works/<slug>.md)

## Overview

One or two sentences describing what the work is.

## Topics

- [<Topic Name>](../topics/<topic_file>.md)

## Activities

- [<Activity Name>](../activities/<activity_file>.md)

## Links

- **Paper:** <verified URL>
- **Code:** <verified URL or omit>
- **Venue:** <verified venue or omit>

## Summary

Two to four sentences: overall design and goals.

## Tasks

Task count, task types, how tasks were constructed. `N/A — <reason>` for surveys/position papers.

## Domains

Domains covered, in prose. This is the evidence for the Domain axis — state <DOMAIN> explicitly and
name any co-domains.

## Evaluation

How answers/trajectories are scored. `N/A — <reason>` for surveys.

## Typical Duration

Trajectory length / wall-clock / token budget per task (or `N/A — <reason>`).

## Main Contribution

The work's stated novelty, in the authors' framing.

## Key Design Ideas

- bulleted concrete design choices

## Strengths

- bullet list, grounded in the paper/project

## Limitations

- bullet list; repository-added observations must be prefixed `Repository note:`

## Related Works

- [<Other Work>](./<other-card>.md) — one-line reason (link only cards that exist)
```

### Card rules

- Language switcher line mandatory, exactly as shown. Do **not** create the Chinese file (later phase).
- **Topics** — canonical only: General Long-Horizon Agent Benchmarks (`long_horizon_evaluation`), Scientific
  Agent Benchmarks (`scientific_agents`), Trajectory Evaluation (`trajectory_evaluation`), Skill Hierarchy
  (`skill_hierarchy`), Credit Assignment (`credit_assignment`), Resource-aware Evaluation
  (`resource_aware_evaluation`), Survey (`survey`).
- **Activities** (mandatory block) — canonical only: `literature_evidence_synthesis`,
  `scientific_problem_solving_reasoning`, `data_analysis_statistical_inference`, `modeling_prediction`,
  `simulation_scientific_computing`, `experiment_design_discovery`, `laboratory_instrument_control`,
  `optimization_engineering_design`, `scientific_software_workflow_engineering`,
  `research_reproduction_replication`, `end_to_end_research`. Assign 1–3 conservatively, only where the
  activity is a **meaningful evaluated component**. Incidental tool use does not qualify. For a work that
  evaluates no scientific/research task, use a single `N/A — <reason>` line with no links.
- Statistics, task counts and metrics come from the **primary source only**. Unverifiable → `TODO(reference)`.
  Never guess. A card whose every quantitative field is unknown is a candidate for rejection, not a thin card.
- Forbidden: `TODO(card)`, `<placeholder>`, `FILL_ME`, `{{...}}`, unfilled `**Field:** TBD`.
- No positioning or marketing language. Do **not** edit any Topic/Domain/Activity page, README, or `zh/` file.

## OUTPUT

Write a JSON array to the results path given in your prompt. One element per candidate:

```json
{"candidate_title","decision","canonical_id","canonical_url","slug_if_accepted",
 "topics":[...],"domains":["<DOMAIN>",...],"activities":[...],
 "one_line_reason","evidence_note"}
```

For every `ACCEPT` you must also have written `works/<slug>.md`. Return a one-line accept/reject summary,
and flag any candidate you consider a close call so the coordinator can adjudicate.
