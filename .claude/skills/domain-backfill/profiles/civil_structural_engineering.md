# Domain profile — Civil & Structural Engineering

## Identity

- **Canonical domain name:** `Civil & Structural Engineering`
- **Domain page:** `domains/civil_structural_engineering.md`
- **Reject enum token:** `REJECT_NOT_CIVIL_STRUCTURAL`
- **Membership before backfill:** 3 works (Terminal-Bench Science, StructureClaw, ERI Benchmark)

## Scope — what belongs

Engineering of the built environment and of load-bearing structures: buildings, bridges, dams, tunnels,
foundations, and civil infrastructure. A work belongs when its evaluated objective is a civil or structural
engineering decision — analysing, designing, verifying, assessing, or planning a physical structure or
infrastructure system.

- Structural analysis and structural modelling (statics, mechanics of materials, structural dynamics)
- Structural design: steel, reinforced/prestressed concrete, timber, composite members and systems
- Seismic and earthquake **engineering** — response, demand, detailing, retrofit of structures
- Finite-element analysis where the modelled object is a civil/structural system
- Design-code compliance and code checking (Eurocode, ACI, AISC, ASCE 7, IBC, GB, JIS …)
- Geotechnical engineering: soil mechanics, foundations, retaining structures, slope stability
- Bridge engineering: design, load rating, inspection
- Structural health monitoring, damage assessment, post-disaster/defect inspection
- Construction engineering, planning, scheduling, quantity/cost estimation
- BIM / IFC / digital-twin workflows where the evaluated task is engineering design or verification
- Transportation and infrastructure engineering where the object is physical infrastructure

## Boundaries — where misclassification happens

This domain has more adjacency traps than Chemical Engineering. Test the **evaluated object**, not the method.

| Neighbour | Belongs to neighbour | Belongs here |
|---|---|---|
| Mechanical & Aerospace | Machine parts, vehicles, airframes, generic solid mechanics, fatigue of components | The same mechanics applied to buildings, bridges, foundations, civil structures |
| Earth Science | Seismology, ground-motion/hazard science, geology, hydrology as earth process | Seismic *structural* response and design; geotechnical engineering of foundations |
| Robotics | Construction robots, autonomous machinery, drone control policies | Inspection/assessment tasks judged by an engineering verdict, not by robot control |
| Architecture / AEC-only | Space planning, aesthetics, generic layout generation, BIM authoring for its own sake | BIM/AEC tasks whose evaluated objective is structural or civil engineering design/verification |
| Environmental Science | Water quality, air quality, ecology, environmental impact assessment | Water/wastewater or hydraulic **infrastructure** engineering |
| Materials Science | Material discovery, concrete chemistry, alloy design | Structural performance of members and systems built from those materials |
| Software & Systems | Generic CAD/CAE tooling, generic solver engineering | Engineering tasks solved through those tools |

Restated rules:
- **A generic FEM benchmark is not automatically Civil & Structural.** The modelled object must be a civil or
  structural system. Generic PDE/FEM suites and generic CFD are out.
- **Naming OpenSees/SAP2000/ETABS/Abaqus/ANSYS/Revit does not place a work here** — the evaluated objective
  must be a civil/structural engineering task, not tool operation.
- **Earthquake science vs earthquake engineering** is the sharpest line: predicting ground motion or seismic
  hazard is Earth Science; computing or designing a structure's response to it is here.
- Structural mechanics must be **grounded in building / bridge / civil structures** to count.
- Construction *management* counts only when the evaluated task is engineering planning, not generic project
  management or business process.

**Legitimate co-domains:** Mechanical & Aerospace (shared solid mechanics), Earth Science (seismic,
geotechnical), Materials Science (structural materials), Environmental Science (infrastructure and water),
Robotics (automated inspection), Software & Systems (engineering toolchains), Energy Systems (offshore/wind
support structures).

## Search vocabulary

structural engineering · structural analysis · structural design · structural dynamics · seismic · earthquake
engineering · finite element · FEM/FEA · steel design · concrete design · reinforced concrete · bridge ·
geotechnical · soil mechanics · foundation · retaining wall · slope stability · civil infrastructure ·
construction engineering · construction planning · BIM · IFC · digital twin · structural health monitoring ·
damage assessment · load rating · design code · code compliance · Eurocode · ACI · AISC · ASCE

## Subfield query families

### Structural engineering
`"structural engineering" agent benchmark` · `"structural engineering" LLM benchmark` ·
`"structural analysis" LLM agent` · `"structural design" agent evaluation` ·
`"structural dynamics" LLM agent` · `"structural engineering" LLM evaluation`

### Design and codes
`"steel design" LLM agent` · `"reinforced concrete" design LLM benchmark` ·
`"design code" compliance LLM agent` · `Eurocode LLM benchmark` · `"building code" LLM agent evaluation` ·
`"code checking" structural agent`

### Seismic / earthquake engineering
`"earthquake engineering" LLM agent` · `"seismic design" agent benchmark` ·
`"seismic assessment" LLM evaluation` · `"seismic response" LLM agent`

### Finite element / simulation-mediated
`"finite element" agent benchmark` · `OpenSees LLM agent` · `OpenSees benchmark LLM` ·
`SAP2000 LLM agent` · `ETABS agent` · `Abaqus LLM agent` · `ANSYS structural LLM agent` ·
`"structural simulation" agent evaluation`

### Civil engineering / infrastructure
`"civil engineering" LLM benchmark` · `"civil engineering" agent evaluation` ·
`"civil engineering" agent benchmark` · `"infrastructure" engineering agent benchmark` ·
`"transportation engineering" agent benchmark` · `"bridge engineering" LLM agent` ·
`"bridge inspection" LLM evaluation`

### Geotechnical
`"geotechnical engineering" LLM agent` · `"soil mechanics" LLM benchmark` ·
`"foundation design" LLM agent` · `"slope stability" LLM agent`

### Construction / BIM / AEC
`"construction engineering" agent benchmark` · `"construction planning" LLM agent` ·
`"construction scheduling" LLM benchmark` · `BIM LLM agent benchmark` · `IFC LLM agent` ·
`Revit agent evaluation` · `"digital twin" civil infrastructure agent` · `AEC LLM benchmark`

### Inspection / monitoring / assessment
`"structural health monitoring" LLM agent` · `"damage assessment" LLM benchmark` ·
`"defect detection" structural agent evaluation` · `"post-earthquake" damage LLM`

### Cross-searches
`"scientific agent benchmark" "civil engineering"` · `"engineering agent benchmark" structural` ·
`"agent benchmark" OpenSees` · `"LLM benchmark" structural engineering` ·
`"engineering reasoning" benchmark civil`

## Domain software, tools, simulators

OpenSees / OpenSeesPy · SAP2000 · ETABS · SAFE · Abaqus · ANSYS Mechanical · ADINA · LS-DYNA ·
STAAD.Pro · RISA · Robot Structural Analysis · Tekla · Revit · AutoCAD Civil 3D · IFC / buildingSMART ·
PLAXIS · GeoStudio · FLAC (geotechnical) · Perform-3D

**Caution:** these are discovery signals only. Tool use never establishes domain membership by itself.

## Snowball terms

StructureClaw · ERI Benchmark (its civil field) · Terminal-Bench Science (Engineering Sciences track) ·
any "engineering reasoning" or multi-field engineering benchmark with a civil/structural field ·
NEHRP / PEER / FEMA benchmark structures · SAC steel-frame benchmarks ·
Journal of Structural Engineering · Computers & Structures · Automation in Construction ·
Engineering Structures · Journal of Computing in Civil Engineering

## Known traps

- **Generic FEM/PDE benchmarks.** Expect several to surface; most are Mechanical/Aerospace or pure numerics.
  Check whether the modelled object is a civil structure.
- **Earthquake science vs earthquake engineering** — likely the most common misclassification here.
- **AEC/BIM papers** are frequently document-processing or layout-generation work with no engineering
  verification; those are out.
- **Vision-only crack/defect detection** is ordinary computer vision, not an agent evaluation, unless an agent
  is evaluated on an engineering verdict.
- **Construction-management LLM papers** are often business-process work.
- **Multi-field engineering benchmarks** (like ERI) may include a civil field — those are legitimate
  multi-domain members, and existing cards may need a domain correction rather than a new card.
- **StructureClaw and ERI Benchmark are already carded** — check `works/` before creating anything.
