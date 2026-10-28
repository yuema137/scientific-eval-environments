# AutoDataBench (2026)

> **English** | [简体中文](../zh/works/autodatabench-auto-research.md)

> **First appeared:** 2026-09-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.40097)

## Overview

Agents for automated ML research are usually scored on changes to code, models, or hyperparameters, so their skill at improving the training data itself is mixed in with everything else. AutoDataBench holds the model, training pipeline, and evaluation fixed and lets the agent change only the data. In three tasks (repairing a corrupted tool-calling set, building contrastive pairs for an embedding model, and writing question–answer examples to inject post-cutoff knowledge) the agent edits data, trains, reads the in-distribution score, and repeats for up to 20 rounds. Its best checkpoint is then scored on a hidden out-of-distribution set.

## Topics

- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** [AutoDataBench: A Data-centric Testbed for Accelerating Auto Research](https://arxiv.org/abs/2609.40097), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.40097v1>
- **Code:** <https://github.com/AutoDataBench/AutoDataBench>
- **Data:** <https://huggingface.co/AutoDataBench>
- **Venue:** arXiv preprint (cs.CL), 2026
- **Name collision:** a different paper, arXiv:2609.35025, is also titled AutoDataBench; this card covers arXiv:2609.40097 only, hence the slug `autodatabench-auto-research`.

## Summary

In the tool-use task the agent receives a pool of about 40k single-turn function-calling examples derived from xLAM-function-calling-60k and damaged by seven corruption operators; it may filter, deduplicate, synthesize, and rebalance up to 16k examples, which a fixed LoRA pipeline trains into Qwen2-1.5B-Instruct. Each trained checkpoint is scored on 2,000 in-distribution examples by AST accuracy, and the agent sees that score before the next round. After the run, the best in-distribution checkpoint is evaluated on hidden BFCL subsets. Scores are reported against a baseline (random 16k from the corrupted pool) and an expert reference (schema validation, deduplication, and proportional selection on the pre-corruption pool).

## Tasks

Three optimization tasks, each with a fixed base model, training pipeline, and evaluation:

- **Tool use (diagnosis and repair):** Qwen2-1.5B-Instruct with LoRA; ID: 2,000 examples, macro-averaged AST accuracy; OOD: BFCL single-turn subsets (10 categories).
- **Retrieval (data organization):** a 6-layer MiniLM trained with InfoNCE on pairs drawn from the RLHN collection (over 818k pairs), 600k pairs per trial; ID: mean nDCG@10 on ArguAna, FEVERHardNegatives, FiQA2018, HotpotQAHardNegatives, SCIDOCS; OOD: ClimateFEVERHardNegatives, CQADupstackGamingRetrieval, CQADupstackUnixRetrieval, Touche2020Retrieval.v3, TRECCOVID.
- **Knowledge injection (data construction):** Talkie 13B with offline forward-KL distillation; up to 10k context–question–answer examples built from 1,000 post-cutoff facts; ID: Novel accuracy; OOD: Retention accuracy on pre-1930 knowledge.

Agents may not process examples one by one.

## Domains

Machine-learning research: training-data improvement for tool-calling language models, text-embedding retrieval models, and knowledge injection into a language model.

## Evaluation

- **Score:** absolute ID and OOD metrics ×100 from training runs; Overall is the unweighted mean of the three task ID means. Seven LLMs, three standard runs per LLM–task pair (63 runs).
- **Reference rows (Overall; tool ID/OOD; retrieval ID/OOD; knowledge ID/OOD):** baseline 47.98; 70.45/55.18; 34.38/31.13; 39.10/47.84. Expert 56.89; 81.65/60.23; 40.62/34.76; 48.40/48.55.
- **Agents (Overall):** Kimi-3 60.68, GLM-5.2 59.10, GPT-5.6-Sol 58.85, Qwen-3.8-Max 58.56, Claude-4.7 58.31, Qwen-3.7-Max 56.80, DeepSeek-V4-Flash 55.20. Tool ID means lie between 80.82 and 81.98. In retrieval, GPT-5.6-Sol leads ID (40.46) but is lowest on OOD (26.15).
- **Prediction check:** in one prediction-enabled run per task, GPT-5.6-Sol and Kimi-3 recorded a predicted score, uncertainty interval, and justification before each training evaluation; retrieval mean absolute errors were 0.64 and 1.55 points.
- **Trajectory reuse:** adding 8M tokens of AutoDataBench trajectories (upsampled to 80M, 1.6% of a 5.0B-token budget) to mid-training of Qwen2.5-Coder-14B, followed by identical SFT, changes MBPP Base 85.45 → 86.24, CRUXEval Input 72.00 → 74.12, LiveCodeBench v5 44.89 → 45.80, and SWE-bench Multilingual 27.67 → 33.33.

## Typical Duration

One NVIDIA A800 GPU and a 24-hour wall-clock limit per run, covering API calls, data processing, training, and evaluation; at most 20 training-and-evaluation rounds.

## Main Contribution

A testbed that isolates an agent's ability to diagnose, organize, and construct training data, by fixing every non-data factor and scoring the trained model on in-distribution feedback and hidden out-of-distribution sets.

## Key Design Ideas

- Only the data changes; base model, training recipe, and evaluation stay fixed in every task.
- The agent optimizes against the in-distribution score, while the reported OOD score is hidden, which exposes overfitting to the feedback signal.
- Baseline and expert pipelines bracket each task's score range.
- Agents can be asked to forecast each training outcome before seeing it.

## Strengths

- ID and OOD are reported separately, which reveals the retrieval rank reversal.
- Expert reference pipelines give each task a human-designed anchor.
- Every score comes from training and evaluating a model, without any judge.

## Limitations

- Only three tasks are covered.
- The authors state that trajectory gains and refinement examples do not isolate the causal contribution of each change, and that selected runs do not imply equal compute use.
- The reference results have no repeated-run uncertainty estimates, and the prediction analysis uses one run per model–task pair.
- Repository note: no dedicated limitations section appears in the v1 full text.

## Related Works

- [Curation-Bench](./curation-bench.md) — Also fixes model and recipe and lets an agent change only the training-data selection, for vision-language models.
- [PostTrainBench](./posttrainbench.md) — Agents post-train a base model with data as one of several allowed interventions.
- [MLAgentBench](./mlagentbench.md) — Also has agents iterate on an ML pipeline against a target metric, without isolating the data.
