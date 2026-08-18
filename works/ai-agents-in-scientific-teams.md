# Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems (2026)

> **English** | [简体中文](../zh/works/ai-agents-in-scientific-teams.md)

## Overview

A position paper arguing that research on "AI Scientists" has concentrated on autonomous capability and thereby overlooked the social reality of scientific teamwork. It proposes that the unit of analysis should be the human-agent pair rather than the agent, assembles evidence that ignoring human-agent dynamics carries near-term risks, and sketches a decision-theoretic frame for measuring human-AI synergy.

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — a position paper. It argues for a change in how scientific agents should be studied and evaluated rather than evaluating agents on any research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2608.14667>
- **Venue:** Accepted at the COLM 2nd Workshop on Language Models for Scientific Discovery; 15 pages.

## Summary

A human-agent system (HAS) is defined by four components — agents, human participants, an interface mediating interaction through actions, and the environment the system sits in — and its defining commitment is that the *pair* is what gets studied. The authors argue that current AI-Scientist work supports human participation mainly at two points, setting goals and verifying finished work, with few systems supporting the sustained, iterative, joint collaboration typical of human teams; and that the HAS literature has largely stayed isolated from the socio-technical realities of science. The paper builds its case in three moves. It surveys accruing evidence that deploying AI in science at scale carries risks that are invisible to autonomy-focused evaluation. It then analyses two published accounts of working scientists collaborating with agents, drawing out reciprocal augmentation — humans supplying conceptual framing, domain judgment and epistemic verification; agents compressing implementation while occasionally contributing conceptually. Finally it introduces a toy utility model and a set of open questions, and reports a small preliminary experiment on feedback-seeking behaviour. It also acknowledges that complementarity has empirically appeared rarely, suggesting this may reflect structural barriers — incentives favouring autonomy research, and the cost of rigorous human studies.

## Tasks

N/A — no task suite is contributed. The paper's empirical component is a preliminary probe reported in one table: a ReAct GPT-5-mini agent on the **End-to-End Discovery (E2E) split of AstaBench**, over **10 development-set tasks**, under three conditions — (1) the stock AstaBench planning-centric ReAct harness, (2) adding an `ask_user` tool plus the paper's HAS human-feedback taxonomy to the system prompt, and (3) adding explicit guidance to call `ask_user` before every action, serving as an upper bound on agent disengagements.

## Domains

No canonical domain is assigned. The paper's subject is the methodology of studying scientific agents rather than any scientific field; its two case studies happen to sit in complexity theory and plasma physics, but they are illustrative accounts rather than evaluated tasks.

## Evaluation

The preliminary probe classifies the agent's questions under the paper's human-feedback taxonomy using **LLM-as-a-judge**, reporting dimension-wise percentages — counts across the 10 E2E tasks normalized by total questions asked — **averaged across three judges for robustness**. The reported findings: without per-step instruction the agent does not know when to ask, preferring to make assumptions about ambiguous situations even when critical resources are unavailable; under per-step enforcement the dominant feedback type is **evaluative** and generally **mid-task**, with **guidance-seeking** second most common and concentrated **pre-task**; **corrective** feedback is rarely requested.

The risk evidence is drawn from prior work rather than measured here: AI-augmented research producing **three times as many papers at a 5% reduction in the diversity of explored topics**; NeurIPS and ICLR submissions rising **10.4× from 2014 to 2024** without commensurate reviewer growth; and an expert review finding **36% of LLM- and AI-Scientist-generated papers contained noticeable plagiarism**.

For synergy the paper offers a toy decision-theoretic model rather than a metric: team utility **U(H, A) = CA(H, A) − CD(H, A)**, where the collaboration advantage CA measures team performance against the best individual member (complementarity) and the collaboration disadvantage CD ≥ 0 captures the cost of collaborating — communication and coordination overhead, tokens spent on messages, and cognitive load on the human.

## Typical Duration

N/A — no agent evaluation protocol with a budget is defined. The preliminary probe runs over 10 tasks; no per-task budget is reported.

## Main Contribution

The argument that scientific-agent research should take the human-agent pair as its unit of analysis, supported by risk evidence, two case studies of reciprocal augmentation, and a decomposition of team utility into a complementarity term and an explicit cost-of-collaboration term — the latter being the part autonomy-focused evaluation systematically omits.

## Key Design Ideas

- The unit of analysis is the pair, which reframes evaluation questions from "how capable is the agent" to "what does this pair achieve that neither member would alone".
- Making CD(H, A) an explicit term means coordination overhead — tokens, turns, human cognitive load — counts against a collaboration rather than being invisible.
- The distinction between complementarity (team beats its best member) and the weaker human augmentation (AI helps a person without proof it could not do better alone) lets the paper argue for HAS research without overclaiming.
- Both case studies are read in both directions, asking how the agent augmented the human *and* how the human augmented the agent, which is what surfaces the expert-dependence finding.
- The feedback-seeking probe uses a deliberately over-instructed third condition as an upper bound, so the gap between natural and enforced asking is measurable.
- The paper argues end-of-process review is inadequate and that asynchronous interaction at multiple granularities — including audits of trace logs and code — is needed to surface problems earlier.

## Strengths

- The two case studies are drawn from published accounts of working scientists rather than constructed demonstrations, and both report the agent's failure modes (premature confidence, smoothing over thorny issues) alongside its contributions.
- The complexity-theory case is explicit that the workflow succeeded *because* an expert could diagnose omissions and correct an erroneous lemma assumption, and states that without that expertise the same workflow would likely produce a misleading paper.
- The paper reports evidence against its own optimism, noting that empirical complementarity appears rarely.
- The risk section is specific and cited rather than speculative, with named quantities for output volume, review load, de-skilling and plagiarism.
- Including a small preliminary experiment gives the position a testable edge rather than leaving it purely argumentative.
- It engages alternative views in a dedicated section rather than only arguing its own case.

## Limitations

- The empirical component is explicitly preliminary: 10 development-set tasks, one agent, one backbone, with question classification performed by LLM judges rather than humans.
- The utility model is described by the authors as a toy model; CA and CD are not operationalised into measurable quantities, and no instrument for estimating either is provided.
- The two case studies are qualitative single instances in different fields, and both involve expert users, so they cannot speak to how the same workflows behave in less expert hands — which is precisely the population the paper's de-skilling concern is about.
- The headline risk figures are inherited from cited studies rather than established here.
- No benchmark, protocol or dataset is released, so the position's prescriptions are not directly actionable as an evaluation.
- Repository note: this card is indexed under Survey because the topic collects position papers alongside surveys; the work contributes no task suite or scoring protocol.

## Related Works

- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](./ara-survey.md) — Surveys the same class of systems along a verifiability axis, sharing the concern that autonomy-focused evaluation leaves something essential unmeasured.
- [From Chatbot to Digital Colleague](./from-chatbot-to-digital-colleague.md) — Position paper on the shift toward persistent autonomous AI collaborators, arguing from the autonomy side this paper pushes back on.
- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — Taxonomy of agent evaluation perspectives, into which the human-agent pair is the axis this paper argues is missing.
- [AutoResearchEval](./autoresearcheval.md) — Diagnoses autonomous research agents on their own, empirically locating failures this paper argues human collaborators would catch.
