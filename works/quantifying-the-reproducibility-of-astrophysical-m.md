# Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory (2026)

> **English** | [简体中文](../zh/works/quantifying-the-reproducibility-of-astrophysical-m.md)

> **First appeared:** 2026-05-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.11154)

## Overview

An information-theoretic evaluation methodology that treats LLM reconstructions of a published astrophysics method as samples from a distribution over algorithms, measuring with Shannon entropy and Jensen–Shannon divergence how strongly a manuscript's text constrains the space of valid implementations, and scoring the executable pipelines that frontier models produce against a four-level Hierarchy of Scientific Validity.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.11154>
- **Venue:** Accepted for publication in PASP (Publications of the Astronomical Society of the Pacific)

## Summary

The paper asks how much of a computational astrophysics method is actually recoverable from its written description. It frames reconstruction as inference over an algorithm space: given text `X`, an LLM samples candidate reconstructions `Ŷ ~ P(Y | X)`, and the entropy of that distribution measures how much the text fails to pin down. Text is supplied at three nested levels — Title only (T), Title + Abstract (TA), and Title + Abstract + Methods (TAM) — so that information gain between levels can be attributed to specific parts of the manuscript. Two complementary experiments run on the same hierarchy: a distributional analysis with local open-weight models, and a functional stress test in which frontier models must emit executable Python that is scored for scientific validity against the original authors' implementation.

## Tasks

One astrophysical case study: probabilistic spectral reconstruction of Trans-Neptunian Objects from sparse broadband photometry, taken from a companion study whose ground-truth pipeline combines PCA, kernel density estimation and a supervised gradient-boosted regressor. The task is instantiated at three information states (T, TA, TAM). Experiment 1 generates N = 200 reconstructions per information state per model with temperature 0.75 using two open-weight models (DeepSeek-R1-Distill-Qwen-14B and GPT-oss-20b), for distributional analysis. Experiment 2 uses a two-stage prompt — algorithmic extraction, then Python implementation — with three frontier models (Gemini 3.1 Pro, ChatGPT-5.2 and Claude 4.6 Sonnet) at each information state, followed by a data-substitution protocol replacing the models' synthetic spectra with the original study's real observational data. The subject study was unpublished with no public code or preprint during the experiments, and all results were frozen before its release, to limit memorization.

## Domains

Astronomy — the reconstructed method, the ground truth and the evaluated outputs are all astronomical: spectral reconstruction of Trans-Neptunian Objects (Neptune Trojan 2010 TS191 and 2011 WG157 are shown) from sparse photometry, judged on whether reconstructed spectra respect physical constraints such as non-negative reflectance. The information-theoretic framework itself is presented as generally applicable, but astrophysics is the only field instantiated.

## Evaluation

- **Experiment 1 (distributional).** Candidate reconstructions are projected into a lexical space (TF–IDF over a methodological-keyword whitelist, PCA, K-Means with K = 15) and a semantic space (768-dimensional `jina-embeddings-v2-base-code` embeddings, UMAP, HDBSCAN). Cluster frequencies form a discrete distribution over algorithms, from which Shannon entropy `H`, mutual-information gain between information states, inter-state Jensen–Shannon divergence, and alignment to the ground truth (JSD in lexical space, cosine distance in semantic space) are computed. Uncertainty comes from non-parametric bootstrap resampling with 1,000 iterations.
- **Experiment 2 (functional).** Generated pipelines are executed on the original observational data and scored by human-in-the-loop review against the **Hierarchy of Scientific Validity**, an ordinal metric `V ∈ {0,1,2,3}`: 0 invalid/non-executable or non-physical, 1 executable but physically underconstrained, 2 core framework recovered but implicit priors missing, 3 explicit and implicit constraints both recovered. `V ≥ 2` is the stated threshold for "functionally LLM-reconstructable". Three criteria structure the review: algorithmic fidelity, component integration, and operational validity. The authors deliberately avoid global numerical error metrics such as RMSE, arguing that a low error can mask superficial pattern matching on an inherently probabilistic target.
- **Reported.** Lexical entropy falls from 3.65 to 2.62 bits for DeepSeek and 3.54 to 3.06 bits for GPT-oss between the Title-only and full-Methods states, so the full manuscript transmits 1.03 and 0.48 bits of effective algorithmic information respectively — a non-zero "entropy floor" rather than collapse to a single implementation. Ground-truth alignment improves monotonically (lexical JSD 0.68 → 0.16 for DeepSeek, 0.71 → 0.26 for GPT-oss). In Experiment 2, all three frontier models score `V = 0` at Title-only, `V = 1` at Title + Abstract, and `V = 2` at full Methods, while the authors' own implementation is the `V = 3` calibrated reference; final semantic distances to ground truth are 0.13 (Gemini), 0.32 (GPT-5) and 0.34 (Claude). The largest information gain and geometric shift occurs at the Title → Abstract transition, not on adding the Methods section.

## Typical Duration

N/A — single-shot and two-stage prompting rather than multi-step agent trajectories; the paper reports no wall-clock or token budgets. Sampling scale is stated instead: N = 200 reconstructions per information state per local model in Experiment 1, plus a targeted N = 200 ablation with an explicit Gaussian-copula constraint.

## Main Contribution

A quantitative, zero-shot diagnostic for auditing methodological transparency: by measuring the residual divergence between what a paper writes and what an LLM ensemble can reconstruct, authors can identify missing structural constraints. The authors report that the subject study's own authors revised their manuscript before publication to add the previously omitted Gaussian-copula description as a direct result of this experiment.

## Key Design Ideas

- Reconstruction is treated as a probability distribution over algorithms rather than a single pass/fail attempt, so uncertainty is measurable.
- A nested input hierarchy (T ⊂ TA ⊂ TAM) attributes information gain to specific manuscript components.
- Dual representation spaces separate *which* method components are chosen (lexical) from *how* they are implemented (semantic).
- Clustering is performed on the union ensemble across all information states, so the distributions share a common discrete support and divergence is well defined.
- Ground truth is the original authors' actual implementation, manually calibrated in collaboration with the study's principal investigator, not the textual description or a class of similar methods.
- Local open-weight models are used for the distributional experiment specifically to avoid API variability and make sampling reproducible.
- Scoring is an explicit published ordinal rubric with a stated pass threshold, in place of an aggregate numeric error.

## Strengths

- Delivers a reusable, fully specified measurement protocol — sampling scheme, clustering pipeline, metrics, rubric and threshold are all stated.
- Five models across two experiments give genuine external baselines rather than a single-system demonstration.
- Author-validated ground truth and a study that was unpublished during testing together address the memorization confound directly.
- The `V = 2` versus `V = 3` distinction isolates a concrete and generalizable failure: models assemble the explicit pipeline but miss the implicit statistical constraints (latent covariance, choice of non-parametric KDE) that make the result scientifically calibrated.
- The paper is candid that the observed entropy floor may partly be an artifact of embedding resolution rather than a property of the hypothesis space.

## Limitations

- A single case study: one method from one paper. The framework's generality is argued rather than demonstrated across a task set.
- Experiment 2's scientific-validity scores come from qualitative human-in-the-loop review, with no inter-rater agreement reported.
- The two experiments use disjoint model sets (open-weight for distributions, frontier API models for functional scoring), so entropy measurements and validity scores are not attributable to the same systems.
- Repository note: this is an evaluation methodology with a published rubric, not a released benchmark suite — there is no task pool a later system can be scored against, and no code or dataset URL is verifiable from the arXiv record (`TODO(reference)`).
- Repository note: the evaluated systems are prompted models, not tool-using agents; there is no environment interaction, retrieval, or iterative debugging by the model itself.

## Related Works

- [ReplicationBench](./replicationbench.md) — Also measures whether models can reproduce astrophysics papers, but as a task suite with author-co-developed replication tasks.
- [ResearchCodeBench](./researchcodebench.md) — Also scores code generated from paper descriptions against the authors' reference implementation.
- [PaperBench](./paperbench.md) — Also evaluates reproduction from a paper's text, using hierarchical author-designed rubrics.
- [Stargazer](./stargazer.md) — Also targets astronomical analysis pipelines, as an agentic evaluation on archival data.
