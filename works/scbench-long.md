# scBench-Long (2026)

> **English** | [简体中文](../zh/works/scbench-long.md)

## Overview

scBench-Long is a verifiable benchmark of long-horizon single-cell biology: 21 evaluations in which agents must recover scientific conclusions from raw or near-raw data without prescribed methods, spanning melanoma CD8 T-cell reactivity, RNA+ATAC regulatory inference, human–monkey chimera development, KRAS-driven lung tumor aging, and lethal COVID-19 lung pathology.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.26563>
- **Venue:** arXiv preprint (q-bio.GN, cs.AI), 2026

## Summary

Where scBench isolates single analysis steps, scBench-Long asks for the whole journey: from near-raw data — integrating metadata, assay context, and auxiliary evidence — to the study's actual scientific conclusions, with no prescribed method. Candidate claims are reproduced, reviewed, and converted into controlled answer vocabularies with deterministic grading and trajectory rubrics. Across 1,068 completed trajectories, the strongest model-harness pair passes only 16 of 63 runs (25.4%).

## Tasks

21 long-horizon evaluations over paired scRNA/TCR sequencing, RNA and chromatin (ATAC) profiling, cross-species transcriptomics, single-nucleus RNA-seq, and immune-repertoire data; agents work from raw or near-raw data to scientific conclusions.

## Domains

Long-horizon single-cell biology across melanoma T-cell biology, developmental biology (human–monkey chimera), lung cancer, and COVID-19 lung pathology.

## Evaluation

- Candidate claims reproduced, reviewed, and converted into controlled answer vocabularies; deterministic grading plus trajectory rubrics.
- **Reported.** Across 1,068 completed trajectories, the strongest model-harness pair passes 16/63 runs (25.4%).

## Typical Duration

Long-horizon multi-step analysis trajectories from near-raw data; budgets are TODO(reference).

## Main Contribution

Makes end-to-end biological discovery verifiable: controlled answer vocabularies let deterministic graders score conclusions that agents reached by unprescribed routes.

## Key Design Ideas

- No prescribed methods — the route to the conclusion is the agent's problem, as in real analysis.
- Controlled answer vocabularies reconcile open-ended discovery with deterministic grading.
- Trajectory rubrics score the journey alongside the destination.

## Strengths

- Real studies with real stakes (cancer, COVID-19 pathology) as ground truth.
- The 25.4% ceiling for the best model-harness pair quantifies the distance to autonomous analysis.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [scBench](./scbench.md) — The single-step sibling with the same deterministic-grading philosophy.
- [BAISBench](./baisbench.md) — Also tests recovery of published single-cell discoveries, via annotation and MCQs with a human baseline.
- [FIRE-Bench](./fire-bench.md) — Also full-cycle rediscovery of published findings, in machine-learning research.
