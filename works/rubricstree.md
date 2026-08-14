# RubricsTree (2026)

> **English** | [简体中文](../zh/works/rubricstree.md)

## Overview

RubricsTree is an evaluation framework for open-ended personal health agents that replaces a monolithic LLM judge with an expert-curated hierarchical taxonomy of over 100 atomic, clinically verifiable Boolean rubrics, activating only the relevant rubric subset per query through a context-aware adaptive router.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — evaluation methodology for consumer-facing health assistants; no scientific or research activity is itself the evaluated task.

## Links

- **Paper:** <https://arxiv.org/abs/2606.18203>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

Clinical deployment of LLM personal health agents is constrained by an evaluation bottleneck: physician annotation is reliable but unscalable, while LLM-as-a-judge is scalable but subjective, inconsistent and sometimes clinically misaligned. RubricsTree curates a hierarchical rubric taxonomy — a directed acyclic graph running from macro-level capabilities through intermediate sub-domains down to atomic Boolean leaf rubrics — through an iterative human-in-the-loop protocol led by an experienced physician, informed by roughly 4,000 real user queries. At evaluation time an adaptive router activates only the relevant, auto-weighted rubric subset for a given query, and the framework is validated by meta-evaluation against expert panels and by downstream use as instructions, feedback, and training rewards.

## Tasks

N/A — a judging framework rather than a task suite. Meta-evaluation uses an internal dataset of 532 real-world queries across four scenarios (Medical Explanation, Health Data, Advice/Action Plan, Symptoms) with controlled perturbations; downstream optimization is measured on the HealthBench-Hard subset (362 user-facing queries) with HealthBench-Consensus used for reinforcement-learning training. Taxonomy curation drew on approximately 4,000 real personal-health-agent user queries.

## Domains

Medicine & Health — consumer and clinical health question answering grounded in user health and wearable-sensor metrics, with rubrics authored and validated by a physician-led expert panel. The rubric scenarios span medical explanation, health-data interpretation, advice and action planning, and symptom handling.

## Evaluation

- **Atomic Boolean rubrics.** Over 100 clinically verifiable leaf rubrics organized in a hierarchical DAG from macro-level capabilities down to atomic leaves; each is a Boolean check rather than a graded opinion.
- **Adaptive routing and auto-weighting.** A context-aware router activates only the rubric subset relevant to a query, with weights assigned automatically, to keep throughput viable at scale.
- **Meta-evaluation against experts.** Agreement with an expert panel (1 experienced physician plus 5 health experts; the curation panel was 1 lead physician plus 8 health researchers) measured by ICC₃ and Cohen's κ, plus oracle-perturbation tests checking that contextually degraded responses are penalized.
- **Reported.** Overall ICC₃ of 0.876 and Cohen's κ of 0.787 for RubricsTree versus 0.291 and 0.431 for a principle-based baseline. Used as structured instructions, text feedback, or training rewards, it yields up to roughly 66% relative gains on HealthBench across the Gemini, GPT and Qwen families; RL-based training gains are reported as +66.7% (Qwen 0.6B), +55.3% (Qwen 1.7B) and +40.3% (Qwen 4B).

## Typical Duration

N/A — a per-response judging framework; the paper motivates adaptive routing by evaluation throughput but does not report per-query wall-clock or token budgets.

## Main Contribution

An expert-aligned, hierarchically decomposed rubric taxonomy that makes open-ended health-agent evaluation both auditable and scalable, with the taxonomy itself designed to evolve under a human-in-the-loop curation protocol rather than being fixed at publication.

## Key Design Ideas

- Evaluation is decomposed top-down from macro-level capabilities to atomic Boolean leaves, so a score is traceable to specific clinically checkable claims.
- Rubrics are Boolean and atomic by construction, which is what makes physician verification of each node feasible.
- Per-query routing activates only relevant rubrics, trading exhaustive scoring for throughput without abandoning the full taxonomy.
- The same rubrics serve three roles — judge, textual feedback, and RL reward — so evaluation quality is tested by whether it improves the systems it grades.
- Meta-evaluation includes deliberately degraded responses, testing that the judge penalizes what experts would penalize rather than only ranking good answers.

## Strengths

- Expert alignment is measured with standard reliability statistics (ICC₃, Cohen's κ) against a physician-led panel rather than asserted.
- The downstream-optimization results give an external check that the rubric signal carries usable information.
- Curation is grounded in a large pool of real user queries rather than synthesized scenarios.

## Limitations

- Code and rubrics are stated as forthcoming after official publication; the 532-query internal evaluation set cannot be released because of proprietary clinical content, so only aggregated statistics are reported.
- The exact depth of the taxonomy and the per-level category breakdown are not disclosed — TODO(reference).
- Rubric curation and the evaluation panel are both drawn from the authors' expert network, so alignment is measured against the same tradition that wrote the rubrics.
- Repository note: the object evaluated is a health-assistant response rather than an agent trajectory, so the framework's hierarchical decomposition sits on the judge side; per-step or per-tool-call scoring is not part of the protocol.

## Related Works

- [MedHELM](./medhelm.md) — Also pairs a clinician-validated taxonomy of medical work with an LLM-jury methodology whose agreement against clinician ratings is measured explicitly.
- [SkillCoach](./skillcoach.md) — Also builds and evolves rubrics from real rollouts under a validation gate, for agent process quality rather than clinical content.
- [AgentClinic](./agentclinic.md) — Also evaluates health agents in open-ended interaction rather than on fixed multiple-choice items.
- [MedAgentBench](./medagentbench.md) — Also targets health-agent evaluation, through executable clinical tasks rather than rubric judging.
