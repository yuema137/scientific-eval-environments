# Domain profile — <Canonical Domain Name>

> The **only** domain-specific input to the backfill workflow. Everything else is generic.
> Copy this file, fill every section from evidence, and check the boundary rules against `AGENT.md`.

## Identity

- **Canonical domain name:** `<exact name, as it appears as the domain page's # title>`
- **Domain page:** `domains/<file>.md` (Chinese mirror `zh/domains/<file>.md`)
- **Reject enum token:** `REJECT_NOT_<TOKEN>`
- **Current membership:** `<N works — derive from the page, do not trust a prompt>`

## Scope — what belongs

One paragraph defining the domain positively, then the concrete subareas that count. Be specific enough that
a reviewer can test a paper against it.

- <subarea>
- <subarea>

## Boundaries — where misclassification happens

The hard part. For each neighbouring domain, state what falls on each side and give a discriminating test.

| Neighbour | Belongs to neighbour | Belongs here |
|---|---|---|
| `<domain>` | <…> | <…> |

Generic rules worth restating for this domain:
- <e.g. "a generic <tool> benchmark is not automatically this domain — the evaluated objective must be …">

**Co-domains that are legitimate** (list the pairings the evaluated tasks can genuinely support):
<…>

## Search vocabulary

Terms a relevant work is likely to use **instead of** the literal domain name — this is where breadth comes
from.

<…>

## Subfield query families

Group queries by subfield so coverage is auditable. Each family is a minimum, not an exhaustive list; expand
synonyms when results reveal new terminology.

### <Subfield>
- `<query>`
- `<query>`

## Domain software, tools, simulators

Often the highest-signal queries, because tool-mediated work rarely names the domain in its title.
Pair each with an agent/benchmark/evaluation term.

<…>

**Caution:** naming one of these tools does not make a work in-domain. The evaluated objective must be a
domain task, not tool operation.

## Snowball terms

Named benchmarks, research groups, labs, project orgs, and venues to chase through citations and related work.

<…>

## Known traps

Anything a reviewer is likely to get wrong for this domain — near-duplicate artifacts, papers whose title
suggests the wrong field, publishers that block fetching, families of works that look in-scope but are not.

<…>
