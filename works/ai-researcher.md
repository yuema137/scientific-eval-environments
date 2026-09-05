# AI-Researcher (2025)

> **English** | [简体中文](../zh/works/ai-researcher.md)

> **First appeared:** 2025-03-04 · **Source:** [Official repository release announcement](https://github.com/HKUDS/AI-Researcher)

## Overview

AI-Researcher pairs an autonomous research system with Scientist-Bench, the benchmark it is measured on. Systems that automate one research stage — ideation, or implementation, or writing — were each scored by their own ad-hoc yardstick, so nobody could say whether an end-to-end run had produced work of publishable quality. Scientist-Bench fixes a comparison target instead of a metric: every task is anchored to a real paper written by human researchers, and the agent's generated manuscript is placed against that paper in a randomized pairwise review by an LLM reviewer scoring on ICLR criteria. The reviewer is not assumed to be trustworthy — the authors validate it separately on 32 accepted/rejected ICLR pairs before using it to rate agent output.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.18705>
- **Project:** <https://autoresearcher.github.io>
- **Code:** <https://github.com/HKUDS/AI-Researcher>
- **Venue:** NeurIPS 2025

## Summary

From the University of Hong Kong, the work states a discovery task as: given reference papers *R* (15–20 references selected by LLMs from a target paper *y*), a research instruction *I*, and datasets *D*, produce implementation code *C* and a technical report *p*. Scientist-Bench builds those inputs from 22 papers published between 2022 and 2024, at two difficulty levels — Level-1 supplies the research instruction extracted from *y*, Level-2 withholds it and leaves the agent to formulate its own direction from references and data alone. Scoring runs in two stages: a code-review agent checks whether the implementation executes and whether it faithfully realizes the described method, and a review agent compares the generated manuscript against *y* on a −3 to +3 scale with the presentation order randomly swapped. The AI-Researcher system, a three-stage multi-agent pipeline, is the reference implementation evaluated on it: with Claude-series backbones it reaches 93.8% implementation completeness and 2.65 of 5 on correctness, and its manuscripts rate below the human papers on every evaluator, by −0.53 to −1.70 on the guided level.

## Tasks

**22 target papers, 22 Level-1 tasks and 6 Level-2 tasks.** Papers were collected from 2022–2024 in two steps: LLMs generated domain-specific keywords across 16 research areas — including Computer Vision, Graph Learning, Recommender Systems, Vector Quantization, Image Processing, Self-Supervised Learning, and Contrastive Learning — and the top-cited arXiv papers per domain (10 per keyword) were retrieved and filtered by citation-based metrics. The resulting distribution is Diffusion Models 4 papers, Vector Quantization 6, Graph Neural Networks 7, and Recommender Systems 5; two papers (one GNN, one recommender) were rejected from full evaluation.

- **Level-1, guided innovation.** The agent receives explicit research instructions extracted from the target paper alongside the references, testing whether it can execute a given idea. All 22 papers are covered.
- **Level-2, autonomous exploration.** The instruction is omitted and only references and datasets are supplied, so the agent must identify a gap and formulate a direction itself. Six tasks are built from five ground-truth papers chosen in distinct research domains to limit citation overlap between them.

Two construction steps are meant to stop recall from standing in for reasoning. The instruction generator is prompted to exclude technical specifications, model identifiers, quantitative results, and architectural details from the research directive. On top of that, an anonymization protocol masks method and model names with generic identifiers, abstracts implementation specifics away from core concepts, standardizes dataset naming, and anonymizes citations and institutional markers.

## Domains

AI & Machine Learning Research — four subfields, named by the paper as Computer Vision (diffusion models), Signal Processing (vector quantization), Graph Learning (graph neural networks), and Information Retrieval (recommender systems).

## Evaluation

- **Stage 1, technical execution validation.** A code-review agent performs static analysis and runtime verification over algorithm correctness, computational efficiency, and adherence to specified constraints. *Completeness* records whether the agent produced executable code within the allocated inference budget, using an explicit termination protocol in which the agent signals `case_resolved` or `case_not_resolved`. *Correctness* is a 5-point score: an Advisor Agent writes a detailed analysis report identifying potential issues, and a Judge Agent turns that report into a score; the reported figure is the mean over multiple independent judgments.
- **Stage 2, scientific contribution evaluation.** For a generated report *p* and the ground-truth paper *y*, the protocol computes `r, J = PaperReview(RandomSwap(p, y); g)`, where *g* is a set of review guidelines derived from ICLR standards covering innovation and novelty, theoretical and methodological rigor, and empirical validation and experimental design quality. The comparative rating *r* runs from −3 to +3, with positive values meaning the generated paper exceeds the human one, zero meaning parity. Two debiasing mechanisms are applied: the presentation order of the two papers is randomly swapped, and five LLMs (GPT-4o, o1-mini, o3-mini, Claude-sonnet-3.5, Claude-sonnet-3.7) each produce 16 independent assessments per paper at temperature 1. Results are summarized as a mean rating and a *Comparable(%)*, the share of generated papers scoring at or above −1.0.
- **Reviewer validation.** The review agent is checked against human expert judgment on 32 paper pairs sampled from ICLR proceedings for 2021–2023, each pair holding one accepted and one rejected submission with high TF-IDF content similarity. Measured by acceptance-prediction accuracy — the share of pairs where the accepted paper received the higher rating — the evaluators identify the superior paper in 65.62% to 90.62% of cases, with four of the five at or above 81.25%. Gemini-2.0-flash is the weakest at 65.62% and is excluded from the primary experiments for that reason.
- **Reported.** With Claude-series backbones the system reaches 93.8% completeness and an average correctness of 2.65 of 5 across the benchmark, with correctness varying by domain from 3.22 (vector quantization) to 2.20 (recommender systems). On a balanced subset, Claude-series backbones reach 87.5% completeness and 2.75 correctness against 50.0% and 1.00 for 4o-series backbones. On Level-1, mean ratings against human papers run from −0.53 (GPT-4o evaluator) to −1.70 (Claude-3.7), with Comparable(%) from 81.82% down to 13.64%. On Level-2 the same system rates higher, from −0.23 to −1.22 with Comparable(%) from 100.00% to 50.00% — the paper's most notable finding, since it means prescriptive instructions did not help.

## Typical Duration

Not reported. The paper gives no wall-clock, token, or monetary accounting; the only stated budget is the "allocated inference budget" within which completeness is measured. The implementation stage does describe a staged compute pattern: prototype implementations are first tested on minimal data, typically 1–2 epochs or small dataset subsets, and only successful prototypes advance to full-scale experiments.

## Main Contribution

Scientist-Bench, presented as the first benchmark to assess autonomous research systems on both guided innovation and open-ended exploration against human-authored target papers, together with a two-stage evaluation protocol whose review agent is validated against real conference accept/reject decisions.

## Key Design Ideas

- The comparison target is the human paper itself rather than a threshold, so the score reads directly as how far the generated work sits from published work in the same domain.
- Two difficulty levels isolate execution from formulation: the same target paper yields a Level-1 task with its research idea supplied and a Level-2 task with it withheld.
- Anonymization is applied to the task inputs — method names, technical specifics, dataset names, citations — to separate genuine problem solving from recall of a memorized paper.
- Order swapping plus five independent LLM reviewers at temperature 1 makes the review a panel rather than a single verdict, and the spread across evaluators is reported rather than averaged away.
- The reviewer is validated on pairs of real ICLR submissions with known outcomes and matched by content similarity, so the test is discrimination between close papers rather than between obviously different ones.
- Implementation quality is split into completeness and correctness, which separates "the code ran" from "the code implements the described method" — the paper's own example is a 4o-series run that produced a plain Vision Transformer while claiming a Diffusion Transformer.

## Strengths

- The evaluator is validated before it is used, and the validation is reported per model with its weakest case named and excluded.
- Reporting each evaluator separately exposes reviewer divergence directly: Comparable(%) on Level-1 spans 13.64% to 81.82% across the five judges for the same generated papers, which is itself the evidence against relying on a single LLM reviewer.
- The Level-1 versus Level-2 contrast is a controlled comparison on the same target papers, and it produces a counterintuitive result the authors report rather than smooth over.
- Implementation completeness and correctness are separated, so a high completion rate is not mistaken for faithful implementation.

## Limitations

- Small scale: 22 target papers, 22 Level-1 and 6 Level-2 tasks, over four subfields.
- Only the authors' own system is evaluated on the benchmark; the comparisons vary the backbone LLM rather than the agent system, so nothing external is scored against these tasks.
- The authors state that their evaluation framework does not adequately capture idea quality — novelty, feasibility, impact — that LLM reviewers overvalue presentation over substantive contribution, and that code assessment needs to go beyond basic functionality.
- The system has no dedicated external memory; it relies on the LLM context window, so fine-grained details compress into abstract summaries over long workflows.
- The paper reports no contamination measurement. The target papers were published in 2022–2024 and the anonymization protocol removes identifiers from the task inputs, but it cannot remove those papers from a pretraining corpus.
- Repository note: the paper contributes both the AI-Researcher system and the Scientist-Bench benchmark with its evaluation protocol; this card centers the benchmark and the protocol, and describes the system as the reference implementation evaluated on them.
- Repository note: Appendix A.7.2 describes the reviewer validation as showing that the judgments "perfectly align" with ICLR's final decisions, while Appendix A.9 and Table 6 give acceptance-prediction accuracies of 65.62% to 90.62%. The quantified figures are used here.

## Related Works

- [MLR-Bench](./mlr-bench.md) — Also scores full-pipeline ML research with an LLM reviewer validated against human experts.
- [PaperBench](./paperbench.md) — Also grades agent output against recent papers, but asks for replication of a known result rather than comparison of scientific merit.
- [MLGym](./mlgym.md) — Also pairs an AI-research system with the benchmark it is measured on, over open-ended research tasks.
