# Hard2Verify (2025)

> **English** | [简体中文](../zh/works/hard2verify.md)

> **First appeared:** 2025-10-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.13744)

## Overview

Hard2Verify is a benchmark that scores step-level verifiers on their ability to grade the individual steps of frontier-model proofs to recent, open-ended Olympiad mathematics problems. It comprises 1,860 expert-labeled steps across 200 model-generated solutions to 80 competition problems, produced with over 500 hours of human labor.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.13744>
- **Code:** <https://github.com/SalesforceAIResearch/Hard2Verify>
- **Venue:** ACL 2026

## Summary

Hard2Verify argues that existing step-level verification benchmarks sit below the frontier, drawing on easy or short-answer questions and on human-written or synthetically corrupted solutions rather than on naturally occurring frontier-model errors. The authors curate 80 problems from ten recent Olympiads, sample one solution per problem from GPT-5, Gemini 2.5 Pro, and Claude Sonnet 4, and have mathematical experts label every step of the 200 surviving responses under strict grading that treats any step derived from an earlier mistake as incorrect. Across 29 evaluated generative critics and process reward models, GPT-5 leads with 86.53 Balanced Accuracy on step-level correctness but only 70.61 on first-error identification, and open-source verifiers lag closed-source models beyond a few standouts.

## Tasks

1,860 annotated steps across 200 model-generated solutions to 80 problems drawn from ten Olympiads dated 2024 and later, among them the IMO Shortlist, Putnam, EGMO, and USAMO. Solutions come from GPT-5 (high reasoning), Gemini 2.5 Pro, and Claude Sonnet 4 (Thinking) under a shared exam-style proof prompt with web search and code interpreters disabled, one solution per problem per model; 78.5% of samples are open-ended. Official competition solutions were parsed from PDFs with MathPix into LaTeX, image-dependent problems were excluded, and responses with degenerate outputs or a small number of long, dense steps were filtered out before annotation.

## Domains

Open-ended competition mathematics: Olympiad-style proof problems in English, text-only, with image-dependent questions excluded.

## Evaluation

- **Step-Level.** The verifier emits a binary correct/incorrect label for every step of a solution; PRM step scores are converted to binary labels via a threshold tuned on a random 100-response subset.
- **Response-Level.** A response counts as correct only if every step in it is labeled correct, giving an outcome-level judgement derived from the step labels.
- **ErrorID.** The verifier outputs the index of the first step containing a mistake, or −1 for no error; for PRMs the first step below the correctness threshold is taken.
- **Balanced Accuracy and Balanced F1.** The mean and the harmonic mean of the verifier's true positive rate and true negative rate; the former reflects average performance across both modes, the latter penalizes imbalanced performance.
- **Reported (Table 2).** GPT-5 leads all three tasks with 86.53 Step-Level, 89.69 Response-Level, and 70.61 ErrorID Balanced Accuracy; gpt-oss-120B is the strongest open-weight verifier at 78.10 Step-Level and 63.97 ErrorID Balanced Accuracy; on ErrorID Balanced F1, Qwen2.5-Math-PRM-72B reaches 37.28 and Llama-3.3-70B-Instruct 2.50.

## Typical Duration

Single-pass verification of a fixed response rather than an interactive rollout, with all evaluated verifiers capped at 32K output tokens. No per-instance wall-clock budget is given for verifiers; on the human side, a response took an average of 90 minutes to grade and 63 minutes to review, with the longest taking up to 4 hours.

## Main Contribution

A human-annotated step-level verification benchmark built from naturally occurring frontier-model solutions to recent open-ended Olympiad problems, together with an evaluation of 29 generative critics and process reward models across step-level, response-level, and first-error-identification tasks.

## Key Design Ideas

- Questions curated from Olympiads dated 2024 and later, prioritizing open-ended proof problems so that verifiers cannot fall back on a known ground-truth final answer.
- Responses sampled from frontier generators and left unedited, so the errors a verifier faces arise naturally rather than being injected into correct solutions or drawn from human-written proofs.
- Strict grading with no "Error Carried Forward" allowance — any step that contains a mistake or is derived from an earlier one is labeled incorrect, and a claim invoking an insufficiently justified prior result earns no credit.
- Four rounds of annotation by 52 mathematical experts, 35 of them holding at least a graduate degree in mathematics or a related field, comprising one labeling pass and three review rounds.

## Strengths

- Grading naturally occurring frontier-model errors keeps the error distribution close to the one a verifier meets in application settings rather than to an injected-error distribution.
- Separating true positive from true negative rate exposes verifiers whose true negative rate collapses toward zero while their true positive rate approaches one, a pattern raw agreement would hide.
- Deriving three tasks from a single annotation layer lets step-level, response-level, and first-error-identification ability be compared on identical data.

## Limitations

- Repository note: 80 problems and 200 solutions — the paper itself calls the benchmark modest in scale and warns that this may introduce variance in measured performance.
- Repository note: The judged subject is a verifier scoring a static solution transcript, not an agent acting in an environment; credit is assigned to proof steps rather than to actions with downstream consequences.

## Related Works

- [AgentBoard](./agentboard.md) — Also assigns credit below end-task success, but against annotated subgoals in an interactive environment rather than against expert step labels on a static proof transcript.
- [TRACE](./trace.md) — Also scores a trajectory step by step rather than by outcome alone, but evaluates the agent that produced the trajectory rather than the verifier grading it.
- [FinTrace](./fintrace.md) — Also scores intermediate process quality rather than final answers alone, but across multi-dimensional financial-workflow metrics rather than binary per-step correctness in mathematics.
