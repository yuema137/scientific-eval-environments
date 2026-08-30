# TransportBench (2024)

> **English** | [简体中文](../zh/works/transportbench.md)

> **First appeared:** 2024-08-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2408.08302)

## Overview

TransportBench is a dataset of 140 undergraduate transportation-engineering problems drawn from two University of Illinois civil-engineering courses, used with human-expert grading to measure the accuracy, answer consistency and reasoning behaviour of seven commercial and open-weight LLMs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2408.08302>
- **Code:** <https://github.com/AGI4Engineering/TransportBench>
- **Dataset:** <https://huggingface.co/datasets/usyed3/TransportBench>
- **Project:** <https://agi4engineering.github.io/TransportBench/>

## Summary

The paper asks how far current LLMs can go on the planning, design, management and control problems taught in an undergraduate transportation-engineering curriculum, and treats the question as a measurement problem rather than an application demonstration. Problems are taken from two courses taught repeatedly at UIUC, converted to text-only form, and answered zero-shot by seven models whose responses are then checked by human domain experts. Beyond single-shot accuracy, the study adds two further axes: answer consistency across repeated trials and under a "carefully check your solutions" follow-up, and a qualitative analysis of the reasoning chains behind both wrong and right answers. The authors report that the highest-scoring model still solves only about two thirds of the set, and that accuracy and consistency dissociate — the most accurate model is also the one most easily talked out of a correct answer.

## Tasks

140 problems in two formats: 73 true-or-false problems and the remainder general open-ended Q&A. The per-topic breakdown reported in the paper is Facts 22, Transportation economics 5, Driver characteristics 5, Vehicle motion 11, Geometry design 10, Traffic flow/control 15, Transportation planning 8, Utility and modal split 6, Transportation networks 3, and Public transit systems 55. Problems were sourced from two courses taught by one of the authors at the University of Illinois Urbana-Champaign — CEE 310 (Introduction to Transportation Engineering, a junior-level course taught 14 times) and CEE 418 (Public Transportation Systems, a senior-level course taught 11 times), with many CEE 418 items derived from a textbook co-authored by the same instructor. Any figure in an original problem was replaced by a language description, so the released set is text-only and no multimodal input is required.

## Domains

Civil & Structural Engineering: the subject matter is transportation systems engineering as taught inside a civil-engineering department, and the problems concern physical transportation infrastructure and its operation — highway geometric design, vehicle motion and stopping/rolling-resistance mechanics, traffic flow and control, transportation network analysis, transportation planning and modal split, and public transit system design. No other canonical domain is a substantive component; the transit-planning and modal-split items lean on operations-research style modelling but the object of every problem remains a transportation facility or service, which the domain profile places under civil/infrastructure engineering rather than a separate field.

## Evaluation

Model responses are collected zero-shot through the models' web interfaces and their correctness is judged by human annotation from domain experts, who examine both the final answer and the reasoning presented. Overall accuracy across the 140 problems is reported as a count of correctly solved problems: Claude 3.5 Sonnet 67.1% (94/140), Gemini 1.5 Pro 63.6% (89/140), GPT-4o 60.0% (84/140), Claude 3 Opus 59.3% (83/140), GPT-4 55.0% (77/140), Llama 3.1 55.0% (77/140), Llama 3 42.1% (59/140). A separate consistency study runs five independent trials of each of the 73 true/false problems and reports a Mixed Response Rate — the fraction of problems on which a model does not give the same answer every time. Claude 3.5 Sonnet has the highest true/false accuracy (75.6%) and the lowest mixed-response rate (8.2%), while GPT-4 and GPT-4o show a much higher zero-shot mixed-response rate (23.3%). A second, self-checking consistency protocol re-prompts the model with a request to check its solution: Claude 3.5 Sonnet flips 16 previously correct answers to incorrect, whereas GPT-4 and GPT-4o flip only 4–6, which the authors use to argue that zero-shot consistency and self-checking consistency are distinct properties. The reasoning analysis is qualitative and identifies recurring behaviours including correct conclusions reached through flawed reasoning (for example computing a bus fleet requirement from a steady-state argument that ignores vehicle circulation), sensitivity to whether reasoning is requested before the conclusion, and subtle conceptual confusions such as space versus time headway, harmonic versus arithmetic mean speed, and ignoring speed-dependent rolling resistance.

## Typical Duration

N/A — items are single-turn question answering with no interactive environment or tool use; the paper reports no per-problem wall-clock, trajectory-length or token-budget figures. The only repetition budget stated is five independent trials per true/false problem for the consistency study.

## Main Contribution

The authors present TransportBench as the first benchmark dataset assembled specifically to test LLMs on transportation-systems engineering, and frame the contribution as a three-part evaluation — accuracy, consistency and reasoning behaviour — rather than a single leaderboard number. They emphasise the finding that a model's headline accuracy does not predict its behavioural stability, exhibited most sharply by Claude 3.5 Sonnet's combination of best-in-class accuracy with a pronounced tendency to abandon correct answers when asked to double-check.

## Key Design Ideas

- Problems taken from long-running university courses (taught 14 and 11 times respectively) rather than written for the benchmark, so item difficulty is calibrated against real undergraduate coursework.
- Two answer formats deliberately kept separate: true/false items support cheap repeated-trial consistency measurement, while open-ended Q&A items force a full worked solution.
- Figures replaced by textual descriptions, making the benchmark a pure language-reasoning test and removing diagram-parsing ability as a confound.
- Human expert grading of both the answer and the reasoning, instead of automatic string matching or LLM-as-judge.
- Consistency measured in two distinct ways — repeated independent sampling (Mixed Response Rate) and answer stability under a self-checking follow-up — which the paper shows are not interchangeable.
- Reasoning-behaviour analysis reported alongside accuracy, including cases where the right answer follows from wrong reasoning.

## Strengths

- Ten labelled topic categories make it possible to see which parts of the curriculum models fail on rather than reporting one aggregate score.
- Grading is by human domain experts on a benchmark small enough (140 items) for that to be feasible, avoiding judge-model bias.
- The self-checking protocol probes a failure mode invisible to single-shot accuracy — degradation under ordinary human follow-up — and produces a concrete counter-ranking to the accuracy table.
- Problem statements, answers and evaluation materials are publicly released on GitHub and Hugging Face with a project page.
- The error analysis names specific domain confusions (space vs. time headway, harmonic vs. arithmetic mean speed, speed-dependent rolling resistance) rather than reporting generic "reasoning errors".

## Limitations

- The authors note the set is undergraduate-level only, so it may understate the gap on graduate or professional transportation-engineering work, and that single-trial accuracy for the open-ended items carries sampling randomness.
- Topic coverage is heavily unbalanced: public transit systems accounts for 55 of 140 problems, while transportation networks contributes only 3, so the aggregate score is dominated by one course's material.
- Repository note: this is a static text question-answering benchmark, not an agent evaluation — no tool calls, code execution, traffic simulator or design software is in the loop, and the authors list tool-using LLM agents backed by external coding and simulation platforms as future work rather than as part of this benchmark.
- Repository note: replacing figures with language descriptions removes the diagram interpretation that is intrinsic to geometric design and network problems, so scores are not directly comparable to how the same problems are posed to students.
- Repository note: responses were collected through the models' public web interfaces, so decoding settings such as temperature are not stated and the results are tied to model snapshots available in mid-2024. TODO(reference)
- Repository note: the paper's prose count of general Q&A problems does not reconcile exactly with its per-topic table, which sums to 140 with 73 true/false items; the topic table is the internally consistent figure. TODO(reference)
- Repository note: the arXiv version is a preprint with no confirmed journal or conference venue located at the time of carding. TODO(reference)

## Related Works

- [ERI Benchmark](./eri-benchmark.md) — multi-field engineering instruction benchmark that also carries a civil-engineering field, but scored by an LLM judge panel rather than human experts.
- [MaScQA](./mascqa.md) — exam-derived engineering question-answering dataset built on the same premise that curriculum problems probe domain competence.
- [EEE-Bench](./eee-bench.md) — single-discipline engineering benchmark with an explicit subdomain-coverage design, retaining the diagrams that TransportBench converts to text.
- [StructureClaw](./structureclaw.md) — civil/structural benchmark at the opposite end of the spectrum, scoring executable solver-verified agent workflows instead of textbook answers.
