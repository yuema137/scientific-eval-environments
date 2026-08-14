# DefectBench (2026)

> **English** | [简体中文](../zh/works/defectbench.md)

## Overview

DefectBench is a hierarchical benchmark for structural pathology reasoning on building facades: 12 heterogeneous defect datasets are harmonized into a single annotated corpus under one four-class ontology, and large multimodal models are scored across three escalating cognitive levels — semantic perception, spatial localization, and generative geometry segmentation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.20148>

## Summary

The paper asks whether general-purpose large multimodal models can perform the diagnostic work of a building inspector rather than only detect pixels. It first consolidates 12 previously siloed building-defect datasets — spanning classification, detection and segmentation labels — into one harmonized repository with a shared hierarchical ontology, built through a semi-automated human-in-the-loop annotation platform. On top of that corpus it defines DefectBench, a three-level evaluation that escalates from naming the defect ("what"), through locating and relating it ("where"), to producing a pixel-level mask ("how"), and reports results for a large panel of state-of-the-art open- and closed-weight models under a single zero-shot, multi-turn protocol.

## Tasks

The unified dataset comprises 1,488 annotated images containing 4,527 distinct structural anomalies, drawn from 12 source datasets: CCIC, BDD, BD3 and HS-23k (classification); MBDD2025, BDW and CUBIT-Det (detection); and Bai-2020, CSD, DeepCrack, S2DS and CUBIT-Seg (segmentation). Annotations follow a hierarchical ontology of four primary classes with eleven sub-classes — Crack (linear cracks, map cracking), Material Loss (spalling, peeling, structural bulging), Surface Staining (rust stains, leakage marks, corrosion) and External Fixings (plant growth, graffiti, surface contaminants). The benchmark evaluation subset holds 487 samples: 117 Crack, 102 Material Loss, 134 Surface Stain and 122 External Fixings. Five questions (Q1–Q5) are posed per sample and grouped into the three levels: Q1 identifies which of the four defect types are present and Q2 counts instances (semantic perception); Q3 asks for bounding boxes and Q4 for spatial relationships between defects (spatial localization); Q5 asks the model to generate a binary segmentation mask for a target defect class (generative geometry segmentation). Candidate annotations were produced by a Detection Refinement Module (YOLO variants, Faster R-CNN, RT-DETR) and an Interactive Segmentation Module (SAM-3 plus SegFormer, UNet-VGG16, YOLOv8-crack-seg, SCSegamba) with point-based prompting and brush refinement, then verified by experts.

## Domains

Civil & Structural Engineering. The evaluated objective is a building-condition verdict: identifying, counting, locating and delineating structural pathology — cracking, spalling, corrosion staining, bulging — on building facades, which is the diagnostic core of structural inspection and condition assessment. The paper frames the target application as automated facade inspection for urban resilience and infrastructure maintenance. Materials Science is a secondary contact point, since several defect classes (alkali–silica-driven map cracking, rebar corrosion staining, spalling) are deterioration mechanisms of structural concrete, but the evaluated task is condition assessment of a built structure rather than materials research.

## Evaluation

Each level has its own metric family, all computed against the expert-verified annotations. Semantic perception uses precision, recall and F1 for defect-type identification plus MAE and relative error for instance counting. Spatial localization uses mAP50 and mAP50-95 with F1 for bounding-box prediction, and precision, recall and hit rate for the topological-relationship questions. Generative geometry segmentation uses mIoU, precision, recall, F1 and pixel accuracy against reference masks, with adaptive binarization and spatial gating to the region of interest applied as post-processing because models frequently return RGB textures instead of binary masks. Evaluation is zero-shot and follows a multi-turn dialogue protocol in which each question is explicitly conditioned on the model's preceding answers, so errors at an earlier level can propagate.

## Typical Duration

`TODO(reference)` — the paper does not report per-task wall-clock time, trajectory length, or token budgets; the interaction is a fixed five-turn dialogue per sample.

## Main Contribution

The authors present DefectBench as the first multi-dimensional, hierarchical evaluation framework for structural pathology reasoning by large multimodal models, together with a unified multi-granularity dataset synthesized from 12 previously fragmented data silos, a comprehensive benchmarking study of state-of-the-art models, and an extensible human-in-the-loop annotation platform.

## Key Design Ideas

- One shared ontology (4 classes, 11 sub-classes) imposed over datasets that originally carried incompatible classification, detection and segmentation labels, so a single sample supports all three task levels.
- Three escalating cognitive levels — "what", "where", "how" — that separate semantic understanding from metric precision instead of collapsing both into one detection score.
- A multi-turn protocol conditioning each question on the model's own prior answers, deliberately exposing cascading error propagation.
- Zero-shot generative segmentation asked of general-purpose models and compared against specialized supervised segmentation networks.
- Semi-automated annotation: specialist detectors and segmenters propose candidates, human experts verify, keeping the annotation cost of a multi-granularity corpus tractable.

## Strengths

- Consolidates a fragmented literature: 12 separately published defect datasets become one corpus with consistent labels, which makes cross-dataset comparison possible for the first time.
- Metrics are matched to each level rather than reused, so a model's qualitative competence and its metric precision are reported separately.
- The authors' headline finding is diagnostically useful: models show strong semantic and topological awareness but significant deficiencies in metric localization precision, and zero-shot foundation-model segmentation rivals specialized supervised networks.
- Failure modes are characterized concretely — generative stochasticity, instruction-alignment failures, RGB output instead of binary masks, feature omission and false positives in cluttered regions.

## Limitations

- The dataset and annotation toolkit are stated to be released on a public repository only upon formal acceptance, so at the time of the preprint neither is available for independent verification.
- Evaluation is single-image and perception-centred; no code execution, tool use, or engineering follow-through (severity rating, capacity implication, repair decision) is scored.
- The multi-turn conditioning means level-2 and level-3 scores are not independent of level-1 performance, which the authors note as cascading error propagation.
- Repository note: the abstract and contribution list state 18 state-of-the-art LMMs are evaluated, while the model tables enumerate 12 open-weight and 12 closed-weight systems; the exact evaluated panel size is inconsistent across the preprint.
- Repository note: the benchmark evaluates models prompted directly rather than agents acting over a trajectory, so it measures diagnostic capability rather than autonomous inspection behaviour.

## Related Works

- [StructureClaw](./structureclaw.md) — the other structural-engineering benchmark in the corpus, but on analysis and solver-verified modelling rather than visual condition assessment.
- [MMArch](./mmarch.md) — multimodal reasoning over architecture and civil-engineering figures, sharing the visual-evidence-to-engineering-conclusion setup.
- [AEC-Bench](./aec-bench.md) — agentic evaluation on real construction document sets, a neighbouring built-environment benchmark with executable verification.
- [AECBench](./aecbench.md) — hierarchical, cognition-level-organized knowledge benchmark for the AEC field, sharing the escalating-difficulty design.
