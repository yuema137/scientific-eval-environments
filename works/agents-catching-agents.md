# Agents Catching Agents (2026)

> **English** | [简体中文](../zh/works/agents-catching-agents.md)

## Overview

A study of whether committees of language-model agents deliberating on a shared workspace can be gamed by shortcuts — cues a benchmark rewards but a clinician would ignore. Across seven cohorts on six public clinical datasets it finds that agents largely resist such cues in isolation but adopt them when peers assert them, and it evaluates three oversight agents on whether they can tell shortcut adoption from honest agreement.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

N/A — the clinical items serve as a controlled substrate for measuring shortcut contagion and oversight detection, not as an evaluated clinical-research task. No canonical research activity is directly scored.

## Links

- **Paper:** <https://arxiv.org/abs/2608.03744>
- **Code:** <https://github.com/criticaldata/benchmaxxing> (CC BY 4.0)
- **Venue:** arXiv preprint (August 2026).

## Summary

Clinical decision support is moving toward committees of agents deliberating in a shared workspace, and the paper asks what that architecture does to benchmark validity. It separates two questions that are usually conflated. First, is an individual agent susceptible to a shortcut cue — an option ordering, a corner tag on an image, a rescaled unit in a table? Largely not: flip rates in isolation are low. Second, does a socially plausible signal move it? Substantially: when two peers assert the same wrong answer, the holdout under test adopts it in more than a third of cases, and a fabricated "pre-screen" system flag does the same. The asymmetry is the paper's central result, and it is sharpened by a control: tripling a cue's visual salience does not increase contagion, while adding a second peer voice raises it by half again. What games a committee, in other words, is social plausibility rather than perceptual strength. The paper then turns to oversight, evaluating three detector designs and finding that only a referee that privately re-queries the holdout — an interventional check rather than a reading of the transcript — transfers across modalities.

## Tasks

**Seven cohorts on six public datasets** across three modalities. Text: **MedQA-USMLE (100–120 cases)**, **MedMCQA (50–110 cases)**, and **MIMIC-CXR reports rendered as multiple choice (20–600 cases)**. Imaging: **NIH ChestX-ray14 (35 images from 10 patients)**, **MIMIC-CXR-JPG (48–183 images)**, and **CheXpert (35–150 films)**. Tabular: **SUPPORT2 (120 ICU records)**.

Shortcut cues are modality-specific. Text: option reordering, longest-option bias, stem–option lexical overlap. Imaging: cable overlay, corner tag, laterality marker and watermark, at **0.13%–3.17% frame coverage** and opacities of **0.15, 0.30 and 0.45**. Tabular: information-identical re-renderings varying field order, unit rescaling, precision, redundancy and missingness.

The committee is **three agents** — two peers plus one holdout under test — running **Gemini 2.5 Flash and Flash-Lite at temperature 0** on a shared blackboard. Peers assert a predefined incorrect answer; the holdout observes and responds. Isolated and shared conditions are compared.

## Domains

**Medicine & Health.** Every cohort is clinical — USMLE-style examination items, chest radiographs and reports, and ICU records — and the failure mode under study is specifically framed as one affecting clinical decision-support committees. The clinical content is the substrate rather than the object of discovery, which is why no research activity is assigned, but the domain membership is direct.

## Evaluation

Agents largely resist cues presented in isolation, with **flip rates of 5–16%**. Social pressure is a different matter: when two peers assert the same wrong answer the holdout adopts it in **38%** of cases, and a false "pre-screen" system flag produces the same effect, on both capability tiers.

The salience control is the sharpest result: **tripling a cue's visual salience does not move contagion at all**, whereas a second peer voice raises it by about half again.

Three oversight agents are compared:

| Detector | Precision | Recall | False-positive rate |
|---|---|---|---|
| Gate (flags all shared agreement) | 0.35–0.71 | 1.0 | 0.81–1.0 |
| Judge (transcript-only, same lineage) | 0.56–1.0 | 0.93–1.0 | 0.0–0.94 |
| Referee (private re-query) | 0.48–0.88 | 0.75–1.0 | 0.11–0.22 |

The gate cannot separate adoption from honest agreement at all — its false-positive rate reaches 100%. The same-lineage judge reading only the transcript performs excellently on text (precision 100%, recall 93%) but collapses onto the gate in imaging, where it has no access to the images. Only the referee, which privately re-queries the holdout, transfers to imaging (**77–88% precision at 13–21% false-positive rate**).

Rubric gaming is near-silent: of agents that drifted toward a hidden rubric, only **1 of 10 on text and 1 of 134 on imaging** named the rubric they moved toward, confabulating clinical rationales instead.

## Typical Duration

Not reported. The protocol is a single deliberation round per item at temperature 0 rather than a long-horizon trajectory, so no step, turn or wall-clock budget applies. `TODO(reference)` — token cost and runtime are not stated.

## Main Contribution

Evidence that multi-agent deliberation introduces a benchmark-validity failure that single-agent evaluation does not surface — social plausibility, not perceptual salience, is what moves a committee — together with a comparison establishing that only interventional oversight (privately re-querying the agent) detects it across modalities, while transcript-reading judges do not transfer.

## Key Design Ideas

- Isolated and shared conditions are run on the same items, so peer influence is measured as a difference rather than inferred from committee behaviour alone.
- The salience manipulation is a designed control for the obvious alternative explanation: if contagion were perceptual, tripling the cue would move it, and it does not.
- The two-peer versus one-peer comparison quantifies the social channel directly and shows it scales with the number of asserting voices.
- The three detectors form a deliberate ladder — a trivial gate, a transcript reader, and an interventional re-query — so the finding is about what *kind* of oversight works, not which implementation is best.
- The judge shares model lineage with the committee, which tests whether self-monitoring is possible before concluding that external intervention is needed.
- Testing across text, imaging and tabular modalities is what exposes the judge's failure to transfer; a text-only study would have concluded transcript reading suffices.
- Asking whether drifting agents can name the rubric they moved toward separates behavioural drift from reportable drift.

## Strengths

- The central claim rests on a control that could have refuted it (salience) and did not, rather than on the positive result alone.
- Detector comparison is reported with precision, recall and false-positive rate over ranges rather than single favourable numbers, and the gate's 100% false-positive rate is stated plainly.
- Cross-modality design is what makes the judge-versus-referee conclusion possible, and the paper is explicit that the judge collapses in imaging because it cannot see the images.
- The confabulation finding (1 of 134 imaging drifters naming the rubric) shows self-report is not a viable oversight signal, which follows directly from the measurement rather than from speculation.
- All datasets are public, and code is released under CC BY 4.0.
- Temperature 0 removes sampling variance as an explanation for adoption.

## Limitations

- Cohort sizes are small and uneven (35 images in one imaging cohort, 20–600 in a text cohort), and the authors note reduced statistical power in some cohorts.
- Imaging cues are reproducible only under a pinned imaging-library version, owing to a font rasterization defect.
- The honest-peer clean control is unavailable for imaging, so true recall cannot be measured there.
- Hierarchy monitoring and the cross-lineage detector arm remain unimplemented, so it is unknown whether a judge from a different model family would transfer where the same-lineage judge did not.
- Only Gemini 2.5 Flash and Flash-Lite are evaluated, so the two "capability tiers" are close together and the finding is not established across model families.
- Repository note: the work is an evaluation-validity study rather than a task benchmark. What it releases is a protocol and analysis code for probing committees, not a scored task suite others can submit to.

## Related Works

- [MedAgentBench](./medagentbench.md) — Clinical agent evaluation on realistic health-record tasks, measuring capability where this work measures susceptibility to social shortcuts.
- [MedAgentGym](./medagentgym.md) — Biomedical data-science agent environment, sharing the clinical setting with an execution rather than deliberation focus.
- [AutoResearchEval](./autoresearcheval.md) — Also studies how agents fail rather than how well they score, via trajectory annotation over research tasks.
- [Beyond Final Scores](./beyond-final-scores.md) — Also audits whether high scores reflect genuine capability or exploitation of evaluation-specific shortcuts.
