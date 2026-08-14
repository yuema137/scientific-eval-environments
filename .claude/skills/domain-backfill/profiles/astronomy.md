# Domain profile — Astronomy

## Identity

- **Canonical domain name:** `Astronomy`
- **Domain page:** `domains/astronomy.md` (Chinese mirror `zh/domains/astronomy.md`)
- **Reject enum token:** `REJECT_NOT_ASTRONOMY`
- **Membership before backfill:** 6 works — Stargazer, Terminal-Bench Science, ResearchClawBench,
  gwBenchmarks, ReplicationBench, SciVisAgentBench

## Scope — what belongs

Astronomy and astrophysics: scientific inference from astronomical observations, modelling of astronomical
objects and systems, and astronomy-specific research workflows. A work belongs when its evaluated objective
is an astronomical or astrophysical research task — reasoning about celestial objects, observational data,
surveys, or the instruments and software that produce them.

- Observational data analysis: source detection and classification, catalog work, photometry, astrometry
- Time-series and light-curve analysis; time-domain and transient astronomy
- Spectral analysis and parameter estimation from astronomical spectra
- Exoplanets: detection, radial velocity, transits, atmospheric retrieval, orbital inference
- Stellar astrophysics: stellar structure and evolution, asteroseismology, stellar population modelling
- Galactic and extragalactic astronomy: galaxy morphology and properties, redshift, survey analysis
- Cosmology: cosmological inference and parameter estimation, large-scale structure
- High-energy astrophysics: X-ray and gamma-ray source and spectral analysis
- Radio astronomy: interferometry, data reduction, radio source analysis
- Gravitational-wave astronomy where the task is astrophysical source science
- Telescope, observatory and instrument workflows: observation planning, scheduling, proposal preparation,
  instrument or pipeline operation — **only with a substantive evaluation contribution**
- Astronomy scientific software and archive workflows (Astropy, CASA, HEASoft/XSPEC, MESA, archive queries)

## Boundaries — where misclassification happens

Test the **evaluated objective**, not the vocabulary or the dataset.

| Neighbour | Belongs to neighbour | Belongs here |
|---|---|---|
| Physics | Generic gravitation, particle physics, theoretical field calculations, generic numerical relativity, lab/condensed-matter physics | The same physics applied to astronomical objects, observations, or survey inference |
| Earth Science | Heliophysics, magnetospheric physics, space weather, geospace, planetary geology of Earth | Solar physics framed as stellar astrophysics; planetary science framed as observational astronomy |
| AI & Machine Learning Research | A vision/ML method paper that happens to use an astronomical dataset as a testbed | An evaluation whose objective is an astronomical result |
| Mathematics / Computer Science | Generic numerical methods, generic simulation infrastructure | Astronomy-specific pipelines and solvers where the scored output is astronomical |
| Robotics | Generic autonomous platform control | Telescope/observatory control evaluated on an observing objective |

Restated rules:
- **Using an astronomical dataset does not make a work Astronomy.** Gaia, SDSS, LSST, ZTF, TESS and Kepler
  appear constantly in ML papers; the evaluated objective must be an astronomical one.
- **An astronomy QA benchmark is not automatically an agent benchmark** — it must still meet the
  repository's evaluation scope, and the exam-derived-QA precedent applies (`mascqa`, `eee-bench`).
- **Gravitational waves need care.** Waveform modelling and compact-binary source science are astrophysics;
  generic numerical relativity or detector engineering is Physics. `gwBenchmarks` is already carded — check
  before creating anything adjacent.
- **Tool use is not an Activity and not an evaluation contribution.** Driving Astropy, CASA or XSPEC does
  not by itself qualify.

**Legitimate co-domains:** Physics (shared astrophysics), Earth Science (solar/planetary boundary cases),
AI & Machine Learning Research (methodology benchmarks with a real astronomy slice), Computer Science /
Software & Systems (astronomy pipeline engineering), Mathematics (inference methodology).

## Search vocabulary

astrophysics · observational astronomy · celestial · telescope · observatory · survey · catalog · photometry ·
astrometry · spectroscopy · light curve · transient · variable star · supernova · exoplanet · radial velocity ·
transit · stellar · galaxy · galactic · extragalactic · redshift · cosmology · cosmological · large-scale
structure · interferometry · radio astronomy · X-ray astronomy · gamma-ray · gravitational wave · waveform ·
asteroseismology · spectral energy distribution · source classification · alert broker

## Subfield query families

### General astronomy / astrophysics agents
`astronomy agent benchmark` · `astrophysics agent benchmark` · `astronomy LLM agent evaluation` ·
`astrophysics LLM agent evaluation` · `scientific agent astronomy` · `autonomous astronomy agent` ·
`astronomical research agent` · `astronomy evaluation environment` · `tool-using agent astronomy`

### Observational data analysis
`astronomical data analysis agent` · `astronomy data analysis benchmark` · `observational astronomy LLM agent` ·
`astronomical image analysis agent` · `astronomical source detection agent` ·
`astronomical source classification agent` · `astronomical catalog analysis agent` ·
`astronomy time-series agent` · `light curve agent benchmark` · `spectral analysis astronomy agent` ·
`astronomical inference benchmark` · `astronomical parameter estimation agent`

### Surveys and catalogs
`Gaia LLM agent` · `SDSS agent benchmark` · `LSST agent evaluation` · `Rubin observatory agent` ·
`ZTF agent` · `TESS agent benchmark` · `Kepler light curve agent` · `DESI agent` ·
`astronomical catalog agent benchmark` · `survey astronomy research agent` · `SIMBAD VizieR agent`
*(dataset use alone is not inclusion evidence)*

### Exoplanets
`exoplanet agent benchmark` · `exoplanet inference LLM agent` · `radial velocity agent benchmark` ·
`transit analysis agent` · `exoplanet retrieval agent` · `orbital inference agent astronomy`

### Stellar astrophysics
`stellar astrophysics agent benchmark` · `stellar evolution LLM agent` · `stellar modeling agent` ·
`MESA LLM agent` · `stellar spectra agent benchmark` · `asteroseismology agent`

### Galactic / extragalactic
`galaxy analysis agent benchmark` · `galaxy morphology LLM agent` · `galactic astronomy agent` ·
`extragalactic astronomy agent` · `galaxy survey agent evaluation` · `redshift analysis agent`

### Cosmology
`cosmology agent benchmark` · `cosmological inference LLM agent` · `cosmology research agent` ·
`cosmological parameter estimation agent` · `large-scale structure agent benchmark`

### Time-domain and transients
`transient astronomy agent` · `supernova agent benchmark` · `variable star agent` ·
`astronomical transient classification agent` · `time-domain astronomy LLM` · `alert broker agent astronomy`

### High-energy
`X-ray astronomy agent` · `gamma-ray astronomy agent` · `high-energy astrophysics benchmark` ·
`X-ray spectral analysis LLM agent` · `astronomical source spectroscopy agent`

### Radio
`radio astronomy agent benchmark` · `interferometry LLM agent` · `radio telescope agent` ·
`CASA LLM agent` · `radio data reduction agent` · `radio source analysis benchmark`

### Gravitational-wave
`gravitational-wave agent benchmark` · `gravitational wave data analysis agent` ·
`waveform analysis LLM agent` · `compact binary inference agent`

### Telescope / observatory / instrument
`telescope agent benchmark` · `observatory agent` · `telescope scheduling LLM agent` ·
`observation planning agent astronomy` · `astronomical observing agent` ·
`telescope control agent evaluation` · `astronomical instrument agent` · `observation proposal agent benchmark`

### Cross-searches
`"scientific agent benchmark" astronomy` · `"agent benchmark" astrophysics` ·
`"LLM benchmark" observational astronomy` · `"autonomous scientist" astronomy` ·
`multi-domain science benchmark astronomy subset`

## Domain software, tools, simulators

Astropy · CASA · HEASoft / XSPEC / Sherpa · MESA · IRAF · CIAO · Montage · TOPCAT · astroquery ·
Astro Data Lab · JWST/HST calibration pipelines · Rubin Science Pipelines · emcee / dynesty (inference) ·
GADGET / AREPO / Enzo (simulation) · scheduling tools (e.g. astroplan)

**Caution:** these are discovery signals only. Tool use never establishes domain membership by itself.

## Snowball terms

Stargazer · ReplicationBench · gwBenchmarks · SciVisAgentBench · ResearchClawBench · AstroBench ·
AstroMLab · pathfinder/AstroPT-style astronomy foundation models · MMLU-style astronomy subsets ·
"astronomy" tracks inside multi-domain science suites (HLE, SciCode, ScienceAgentBench, CORE-Bench,
AstroBench-like) · NeurIPS/ICML ML4PS and "Machine Learning for Astrophysics" workshops ·
Astronomy & Computing · RAS Techniques and Instruments · ApJ Supplement software papers

## Known traps

- **The dataset trap.** Astronomy datasets are a favourite ML testbed. A galaxy-morphology CNN benchmark is
  AI/ML research, not an astronomy agent evaluation.
- **Astronomy subsets inside multi-domain suites.** Several already-carded works (Terminal-Bench Science,
  ResearchClawBench, SciVisAgentBench) reach this domain through a track. Expect more such cases; they are
  usually **axis corrections on existing cards**, not new cards.
- **Physics/Astronomy overlap is the most common misclassification** — check the evaluated object.
- **Heliophysics and space weather** read as astronomy but generally fold to Earth Science.
- **Astronomy chatbots and QA assistants** are abundant and mostly fail the evaluation-contribution test.
- **Already carded — check before creating:** stargazer, replicationbench, gwbenchmarks, scivisagentbench,
  researchclawbench, terminal-bench-science.
