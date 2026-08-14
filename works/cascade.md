# CASCADE (2025)

> **English** | [简体中文](../zh/works/cascade.md)

## Overview

CASCADE is a self-evolving agentic framework in which an agent acquires and accumulates executable skills for scientific work through two meta-skills — continuous learning and self-reflection — and ships SciSkillBench, a 116-task materials-science and chemistry benchmark used to measure what the accumulated skills are worth.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.23880>
- **Code:** <https://github.com/CederGroupHub/CASCADE>
- **Data:** <https://doi.org/10.6084/m9.figshare.30924998>

## Summary

The paper frames current scientific agents as limited by dependence on predefined tools or early-stage tool generation, and proposes a transition from "LLM + tool use" to "LLM + skill acquisition". CASCADE gives an agent two meta-skills: continuous learning, via web search, code extraction from documentation, and memory utilization; and self-reflection, via introspection and knowledge-graph exploration. Skills learned this way are persisted and reused across sessions and can be shared between agents and human scientists. To measure the effect, the authors introduce SciSkillBench, a curated benchmark of 116 materials-science and chemistry research tasks, and compare the full system against configurations with the evolution mechanisms removed. Beyond the benchmark, the paper demonstrates computational analysis, autonomous laboratory experiments, and selective reproduction of published papers as applications.

## Tasks

SciSkillBench comprises 116 tasks for materials science and chemistry research, split into 76 data-oriented tasks (data retrieval, analysis, management, and processing) and 40 computation-oriented tasks (simulations and problems requiring specialized models or toolkits). Tasks are also split by specification detail into 58 Level 0 tasks, where the user can specify the key functions to use, and 58 Level 1 tasks, where only a high-level objective is given. The paper describes the set as "carefully curated" but does not detail the sourcing procedure in the sections consulted. Benchmark runs of the DeepSolver agent are reported as executed with all memory tools disabled and without human intervention.

## Domains

Materials Science and Chemistry. The tasks require operating specialized materials and chemistry toolkits, retrieving and processing materials data, and running simulations; the paper's arXiv categories are cs.AI and cond-mat.mtrl-sci. The autonomous-laboratory demonstration additionally touches experimental chemistry, but it is a demonstration rather than part of the scored benchmark.

## Evaluation

Outcome-based automated scoring: the agent's processed output is compared automatically against the ground-truth answer within a predefined tolerance threshold, and success rate is the reported metric. Each system configuration is run with three independent repetitions, for 16,008 experiments in total. Compared configurations are Native (no evolution mechanisms), Search & Debug (S&D), DeepSolver (the paper's four-step sequential workflow with conditional parallel debugging), and a Claude Code baseline. Backbones evaluated include GPT-5, GPT-5-mini, GPT-5-nano, O3, O4-mini, GPT-4.1, GPT-4.1-mini, GPT-4.1-nano, Qwen3-Coder-30B-A3B-Instruct-FP8, and Claude-Sonnet-4.5. With GPT-5, DeepSolver reaches a 93.26% success rate against 35.36% for Native; O3 reaches 91.84%. Ablations remove each meta-skill — continuous learning and self-reflection — individually.

## Typical Duration

TODO(reference) — per-task step, token, and wall-clock budgets are not reported in the sections consulted; the only aggregate resource figure given is the 16,008 total experiment runs across configurations and repetitions.

## Main Contribution

An early instantiation, in the authors' framing, of the shift from tool use to skill acquisition for scientific agents: an agent that codifies knowledge into executable, persistent, shareable skills through continuous learning and self-reflection, together with SciSkillBench as the instrument for showing that the accumulated skills, rather than the backbone model, drive the gain.

## Key Design Ideas

- Two meta-skills rather than a fixed tool set: continuous learning (web search, code extraction, memory use) and self-reflection (introspection, knowledge-graph exploration).
- A hybrid dual-store skill and knowledge memory — a Supabase-hosted PostgreSQL store for vector-based semantic search, and a Neo4j graph database capturing entity relationships across materials, properties, and computational tools.
- Separation of session-wise memory (referencing previous conversations) from consolidated memory (retaining and retrieving key information, experience, and skill sets).
- DeepSolver, a four-step sequential problem-solving workflow with conditional parallel debugging, as the agent that consumes the accumulated skills.
- A two-axis task split in SciSkillBench — data-oriented versus computation-oriented, and Level 0 versus Level 1 specification detail — so results separate tool competence from goal interpretation.
- Skills are represented as executable artifacts intended to be shared across agents and with human scientists, not as free-text notes.

## Strengths

- The evolution mechanisms are isolated by ablation against a Native baseline on the same tasks, so the 93.26% versus 35.36% gap is attributable to the accumulated skills rather than to the backbone.
- Broad backbone sweep across ten models, including an open-weight model, supports the claim that scaling the backbone yields less than the framework does.
- Three independent repetitions per configuration guard against single-run variance on an execution-based benchmark.
- Automated tolerance-based checking against ground truth avoids reliance on an LLM judge for the headline metric.
- Code and benchmark data are both released, with a DOI-archived data record.

## Limitations

- The paper acknowledges that the workflow remains distant from autonomous end-to-end discovery with truly novel insights, and that identifying optimal tools and their correct sequencing within workflows remains an open challenge.
- SciSkillBench task sourcing is described only as careful curation; the construction procedure and the provenance of the ground-truth answers are not detailed in the sections consulted.
- The benchmark scores task success, not the induced skills themselves — skill correctness, redundancy, and reuse rate are not measured directly, so the value of the skill library is inferred from downstream success only.
- Backbone coverage is dominated by one vendor's models, with a single open-weight and a single Anthropic model.
- The laboratory-automation and paper-reproduction results are demonstrations outside the scored benchmark and carry no comparative baseline.
- Repository note: the work sits awkwardly on the existing topic axis — its subject is constructing reusable skills from experience rather than decomposing a capability into scored subskills, which is what the Skill Hierarchy topic covers.

## Related Works

- [MatTools](./mattools.md) — Materials-science tool competence with a fixed, pre-authored toolkit (pymatgen), the setting CASCADE argues against.
- [GATE](./gate.md) — The other framework in the corpus that builds and evolves a reusable tool structure rather than scoring a fixed capability decomposition.
- [SkillSV](./skillsv.md) — Values the internal units of an agent skill, the complementary question to whether an agent can create the skill in the first place.
- [MatSciBench](./matscibench.md) — Materials-science reasoning at the question-answering level, without execution or skill accumulation.
- [AlchemyBench](./alchemybench.md) — End-to-end materials-synthesis benchmark in the same domain, judged by an LLM rather than by execution against ground truth.
