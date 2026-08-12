# Can Large Language Models Automate the HAZOP Process Without Human Intervention? (2026)

> **English** | [简体中文](../zh/works/can-large-language-models-automate-the-hazop-proce.md)

## Overview

A comparative evaluation of four multimodal large language models on the Hazard and Operability (HAZOP) study, in which each model generates a complete HAZOP worksheet from the same piping and instrumentation diagram (P&ID) under a standardized prompt and is scored against an expert-prepared reference worksheet. The paper's stated contribution is a structured framework for evaluating LLMs on HAZOP rather than a HAZOP automation system.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://doi.org/10.1016/j.ssci.2025.107039
- **Venue:** Safety Science, Volume 194, article 107039 (2026)

## Summary

HAZOP is the standard structured hazard-identification method in the process industries, and the paper asks whether current multimodal LLMs can execute the whole procedure end to end with no human in the loop, and whether the resulting worksheets are usable for risk-based decision-making. Four models — GPT-4o, GPT-4o-mini, LLaMA, and Gemini — are each given the same P&ID and the same standardized prompt and asked to produce a full HAZOP worksheet. The generated worksheets are compared against an expert-prepared reference worksheet along two separate axes: model performance (output similarity and cost) and HAZOP performance (validity of the generated scenarios and diversity of the proposed safeguards). The paper concludes that LLMs are useful as assistive tools but that unsupervised LLM HAZOP output is not reliable.

## Tasks

A single evaluation task instantiated once per model: generate a complete HAZOP worksheet — spanning dozens of pages — from one identical P&ID using a standardized prompt, with no human intervention during generation. Four multimodal LLMs are compared under identical conditions (GPT-4o, GPT-4o-mini, LLaMA, Gemini). The ground truth is an expert-prepared reference HAZOP worksheet for the same diagram. The evaluation is a controlled model comparison on one process rather than a multi-process benchmark suite.

## Domains

Chemical Engineering — process safety in the process industries. The evaluated object is a HAZOP study over a piping and instrumentation diagram, covering process deviations, causes, consequences, and safeguards; the task is process-engineering hazard analysis, not chemistry knowledge or molecular reasoning. No co-domain is assigned.

## Evaluation

Generated worksheets are benchmarked against the expert reference along two aspects. *Model performance* is measured by similarity to the reference — reported as F1, with all four models above 86% — and by computational cost, reported as dollars per generated worksheet (LLaMA the most cost-efficient at $0.011 per worksheet). *HAZOP performance* is measured by the validity of the generated scenarios and the diversity of the proposed safeguards: the proportion of semantically valid scenarios ranged from 0.19 to 0.37, and safeguards were heavily skewed toward procedural/administrative measures. Gemini produced the most scenarios per worksheet (34.3) and the most safeguards per deviation (1.79). The separation of surface similarity from semantic validity is the core of the scoring protocol: high textual overlap with the reference coexists with low proportions of genuinely valid scenarios.

## Typical Duration

Each worksheet is produced in a single generation pass from one standardized prompt, so there is no multi-step trajectory budget. The paper reports monetary cost per worksheet (as low as $0.011) rather than wall-clock time or a token budget. `TODO(reference)` for per-task latency, which the abstract does not state.

## Main Contribution

In the authors' framing, the paper provides a structured framework for evaluating LLMs in HAZOP — separating model-level performance (similarity, cost) from HAZOP-level performance (scenario validity, safeguard diversity) — and uses it to answer whether LLMs can automate HAZOP without human intervention. The reported answer is that they cannot: worksheets that look close to the expert reference by similarity metrics contain a low proportion of semantically valid scenarios, so LLMs are positioned as assistive tools within expert-led HAZOP.

## Key Design Ideas

- Holds the input fixed (one P&ID, one standardized prompt) so that differences in output are attributable to the model rather than to prompt or process variation.
- Uses an expert-prepared reference HAZOP worksheet as ground truth instead of an automatically constructed key.
- Splits scoring into two independent axes — model performance and HAZOP performance — so that textual agreement with the reference cannot substitute for domain validity.
- Measures semantic validity of generated scenarios as a distinct quantity from similarity, exposing the gap between the two.
- Includes safeguard diversity as a metric, capturing the tendency of models to propose procedural rather than engineered protection layers.
- Reports monetary cost per worksheet alongside quality, making cost-efficiency an explicit comparison dimension.

## Strengths

- Evaluates four models under identical conditions, which makes the reported cross-model differences interpretable as model effects.
- The similarity/validity split is the paper's most informative result: F1 above 86% against the reference alongside a 0.19–0.37 valid-scenario proportion shows directly that similarity-style metrics overstate HAZOP competence.
- Grounds the evaluation in an expert-prepared reference worksheet from real process-safety practice rather than a synthetic key.
- Reports cost per worksheet, which is rarely quantified in process-safety LLM studies.
- Published in a peer-reviewed process-safety venue (Safety Science), so the HAZOP methodology is reviewed by domain readers rather than only by an ML audience.

## Limitations

- The evaluation uses a single P&ID, so the results characterize model behavior on one process rather than across a range of unit operations or plant configurations.
- No named, released benchmark artifact is described in the abstract; the contribution is an evaluation protocol plus a comparative study. `TODO(reference)` for whether the reference worksheet or generated outputs are publicly released.
- Repository note: with one process and four models, the design does not support statistical claims about model ranking; the reported per-model differences are single-instance observations.
- Repository note: scenario validity is a judged quantity, and the abstract does not state who judged it or what inter-rater agreement was obtained. `TODO(reference)`.
- Repository note: the setting is single-turn worksheet generation, not an interactive or tool-using agent, so it does not evaluate agentic behavior such as querying a simulator or iterating on a design.

## Related Works

- [PSE-Bench](./pse-bench.md) — process systems engineering question benchmark whose process-design subset includes HAZOP and LOPA.
- [CeProBench](./ceprobench.md) — chemical process development benchmark covering PFD parsing and Aspen Plus parameter optimization.
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](./ctrl-alt-recover.md) — LLM agents for safety-constrained fault recovery in process plants.
