# Fisher-R1 / P-Bench (2026)

> **English** | [简体中文](../zh/works/fisher-r1.md)

## Overview

A benchmark (P-Bench) of 425 realistic hypothesis-testing tasks and an open-weight LLM agent (Fisher-R1) trained to perform statistically valid hypothesis testing, evaluating whether an agent selects an appropriate statistical method, computes a correct p-value, and draws a valid reject/fail-to-reject conclusion.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.07437
- **Code:** https://github.com/jmu27/FisherR1
- **Venue:** arXiv preprint (submitted 2026-08-07)

## Summary

The work targets a failure mode in which LLM agents execute statistical analyses correctly yet reach incorrect inferential conclusions, for example reporting a p-value that is not statistically valid given the assumptions underlying the data. To measure this, the authors build P-Bench, a benchmark of 425 open-ended hypothesis-testing tasks spanning economics, biology, and medicine, where each task provides only a scientific hypothesis and a dataset and requires the agent to select a statistical method, compute a p-value, and draw a conclusion. The authors also introduce Fisher-R1, an open-weight agent trained via supervised fine-tuning followed by reinforcement learning on synthetic hypothesis-testing tasks with a verified statistical reward. On P-Bench, Fisher-R1-14B is reported to improve over its backbone and to outperform proprietary and open-source baselines including GPT-5.4 and DeepSeek-V4-Pro.

## Tasks

425 open-ended hypothesis-testing tasks, stratified into an Easy split (203 tasks) and a Hard split (222 tasks). Each task derives from a real scientific analysis originally conducted by domain experts and is built through a three-stage pipeline: (1) reproduce the reference analysis on a clean machine and log the execution; (2) filter out analyses that could not be reproduced and ground each remaining claim in the execution log; and (3) generate a self-contained executable task paired with a structured answer key. Source datasets: economics from peer-reviewed papers in top journals with data on Harvard Dataverse; biology from peer-reviewed papers with data on cBioPortal; medicine/biostatistics from Vanderbilt Biostatistics teaching materials with datasets distributed through R packages. Tasks cover both randomized experiments and observational studies. The per-domain task-count breakdown is not stated in the abstract or the extracted text — TODO(reference).

## Domains

Economics, biology, and medicine.

## Evaluation

Every ground-truth p-value, test statistic, and decision is read off a logged run of canonical reference code. Two metrics are reported: **Raw** — whether the agent's final reject / fail-to-reject decision matches the ground-truth decision; and **Strict** — Raw ∧ |z(p̂) − z(p*)| < 0.5, additionally requiring the reported p-value to be close to ground truth within 0.5 z-score units. P-values are compared in z-space via the monotonic, distribution-free map z(p) = Φ⁻¹(1 − p/2). Success is reported as pass@1 (mean ± standard deviation over three independent runs) and pass@3 (success if any of three trials succeeds).

## Typical Duration

Not stated. Training hyperparameters report a maximum response length of 4096 tokens and maximum prompt length of 2048 tokens, but per-task trajectory lengths or wall-clock budgets are not reported — TODO(reference).

## Main Contribution

The authors' stated contributions are (1) P-Bench, a benchmark that assesses whether an agent's reported p-value is statistically valid given the assumptions underlying the data — a failure mode the authors argue existing benchmarks do not capture — and (2) Fisher-R1, an open-weight agent trained with reinforcement learning on synthetic tasks with verified statistical reward, reported to achieve a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks.

## Key Design Ideas

- Ground-truth answers are read off logged executions of canonical reference code rather than authored by hand, making the answer key verifiable.
- P-value comparison in z-space via z(p) = Φ⁻¹(1 − p/2), a monotonic distribution-free re-labeling used to score p-value closeness fairly.
- Two-tier scoring (Raw decision match; Strict decision match plus p-value closeness) to separate correct conclusions from correct magnitudes.
- Fisher-R1 backbones on Qwen2.5-Coder-7B and 14B, trained by supervised fine-tuning followed by reinforcement learning using Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO).
- Reward R(o) = I_valid(o)·(w_p·r_p(o) + w_c·r_c(o)) with w_p = 0.9, w_c = 0.1, where the p-value component r_p(o) = exp(−|min{z(p̂),5} − min{z(p*),5}|/σ) with σ = 1, gated by a validity indicator.
- Synthetic training corpus of 8,642 tasks generated by combining six independent factors: statistical method, domain scenario, sample size, effect size, prompt style, and random seed.

## Strengths

- Answer keys and rewards are grounded in logged executions of reference code, giving a verifiable rather than heuristic ground truth (paper).
- Targets a specific, under-measured failure mode — inferentially invalid conclusions despite correctly executed analyses (paper).
- Reproducibility filtering in construction removes analyses that could not be re-executed on a clean machine (paper).

## Limitations

- Repository note: the per-domain distribution of the 425 tasks across economics, biology, and medicine is not stated in the sources consulted.
- Repository note: coverage is limited to hypothesis-testing / p-value tasks in three fields (economics, biology, medicine) and does not address other forms of statistical inference or scientific analysis.
- Repository note: reported comparative gains are against a fixed set of contemporary baselines (e.g. GPT-5.4, DeepSeek-V4-Pro) and reflect those models at evaluation time.

## Related Works

- TODO(reference) — related benchmarks for data analysis and statistical inference by scientific agents.
