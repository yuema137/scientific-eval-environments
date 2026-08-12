# Domain profile — Chemical Engineering

> **Reference implementation.** This profile drove PR #35 (1 → 12 works, 59 primary-source decisions,
> 13 deep-review batches). Kept as the worked example for writing new profiles.

## Identity

- **Canonical domain name:** `Chemical Engineering`
- **Domain page:** `domains/chemical_engineering.md`
- **Reject enum token:** `REJECT_NOT_CHEMICAL_ENGINEERING`
- **Membership before backfill:** 1 work (Terminal-Bench Science) → 12 after

## Scope — what belongs

Engineering of chemical and process **systems**, as distinct from Chemistry the science. A work belongs when
its evaluated objective is a process or plant decision.

- Process systems engineering (PSE); process design, synthesis, simulation
- Flowsheeting; unit-operation selection, topology, specification closure
- Process control, plant operations, supervisory fault recovery
- Reactor engineering; separations, distillation, extraction, heat exchange
- Chemical process optimization; process scheduling; scale-up
- Process safety (HAZOP, LOPA), process monitoring and fault diagnosis
- Engineering use of process simulators
- Chemical-engineering knowledge and calculation (balances, thermodynamics, transport, kinetics)

## Boundaries — where misclassification happens

| Neighbour | Belongs to neighbour | Belongs here |
|---|---|---|
| Chemistry | Molecular property QA, retrosynthesis, reaction prediction, quantum chemistry, lab-bench chemistry agents | Reaction/process engineering evaluated as a *process* objective |
| Mechanical & Aerospace | Generic CFD, turbulence, thermal transport with no process unit | Process-unit thermal/fluid tasks inside a flowsheet |
| Materials Science | Materials discovery, ALD, alloy design | Process routes for producing materials at plant scale |
| Energy Systems | Grid, power markets | Chemical process energy integration, pinch analysis |
| Robotics | Lab automation, self-driving labs | Plant operations and supervisory control |

Restated rules:
- Involving chemicals does not make a work Chemical Engineering.
- Calling Aspen/HYSYS/a simulator/Python does not make a task Chemical Engineering — the evaluated objective must be.
- An ML benchmark about chemical processes is not automatically an agent benchmark.

**Legitimate co-domains:** Chemistry, Energy Systems, Environmental Science, Materials Science,
Mechanical & Aerospace.

## Search vocabulary

process systems engineering · PSE · process engineering · chemical process · flowsheet · flowsheeting ·
unit operation · plant · process simulator · process control · distillation · separations · reactor design ·
process safety · HAZOP · P&ID · PFD · process synthesis · process intensification · plantwide control · FEED

## Subfield query families

### General
`"chemical engineering" agent benchmark` · `"chemical engineering" LLM agent evaluation` ·
`"chemical engineering" scientific agent` · `"chemical engineering" agent environment`

### Process systems engineering
`"process systems engineering" LLM agent` · `"process systems engineering" agent benchmark` ·
`"process engineering" agent evaluation` · `"chemical process" agent benchmark` · `"process design" LLM agent`

### Simulation / flowsheeting
`Aspen agent benchmark` · `"Aspen Plus" LLM agent` · `HYSYS agent` · `DWSIM agent benchmark` ·
`"process simulator" LLM agent` · `flowsheet agent benchmark` · `flowsheeting LLM agent`

### Control / operations
`"process control" LLM agent benchmark` · `"plant operation" LLM agent` · `"process monitoring" LLM agent` ·
`"fault diagnosis" chemical process agent` · `"process safety" LLM agent benchmark` · `HAZOP LLM`

### Design / optimization
`"process optimization" LLM agent` · `"process synthesis" LLM agent` · `"reactor design" LLM agent` ·
`distillation agent benchmark` · `"chemical engineering design" agent benchmark`

### Cross-searches
`"scientific agent benchmark" "chemical engineering"` · `"agent benchmark" Aspen` ·
`"LLM benchmark" process systems engineering` · `"autonomous scientist" process engineering`

## Domain software, tools, simulators

Aspen Plus · Aspen HYSYS · DWSIM · IDAES / Pyomo · gPROMS · Chemasim · AVEVA Process Simulation ·
Tennessee Eastman Process (benchmark plant) · DEXPI (P&ID exchange)

## Snowball terms

CeProBench · Simona · OpenIDAES-450 · PSE-Bench · ChemEBench / ChemELLM · ChemProc / MathComp ·
Computers and Chemical Engineering · Chemical Engineering Journal Advances · ESCAPE / PSE conference ·
AIChE Annual Meeting

## Known traps

- **System-vs-benchmark is the dominant boundary.** 23 of 48 rejections were in-domain papers contributing a
  framework rather than an evaluation.
- **Near-duplicate artifacts.** One paper reused PEOA's exact ChemProc/MathComp datasets and metrics; another
  ran on the very repository already carded as `ctrl-alt-recover`. Only primary-source reading caught these.
- **Fabricated arXiv IDs with genuine DOIs** appeared in several batches.
- **Publisher blocks:** IEEE, MDPI, ScienceDirect and ChemRxiv return 403/CAPTCHA — fall back to Crossref or
  OpenAlex, and reject rather than reconstruct when only an abstract is reachable.
- **PSE surveys are usually out.** "Opportunities and challenges" perspectives are not surveys *of agent
  evaluation*.
- **RL-only process-control gyms** (pc-gym, CSTR/distillation RL environments) are not LLM/agent benchmarks.
