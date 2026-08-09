# CUARewardBench (2025)

> **English** | [简体中文](../zh/works/cuarewardbench.md)

## Overview

CUARewardBench is a benchmark that treats outcome reward models (ORM) and process reward models (PRM) as the judged subjects, testing whether vision-language models can reproduce expert verdicts on computer-using agent trajectories. It pairs 272 trajectory-success annotations with 346 step-correctness annotations over OSWorld rollouts from seven policy models spanning 25.9–50.8% success rates.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.18596>

## Summary

CUARewardBench argues that script-based verifiers for computer-using agents scale poorly and cannot assess individual steps, while the VLM-based reward models proposed as their replacement remain largely unverified. It curates expert-annotated trajectories from OSWorld-verified rollouts and evaluates seven vision-language models under three published CUA reward prompt templates, as both outcome and process reward models. The best single configuration reaches 82.9% precision and 80.1% overall accuracy on trajectory-level judgment, and the authors' Unanimous Prompt Ensemble raises precision to 89.8% and NPV to 93.3% by classifying only when all ensemble members agree.

## Tasks

272 annotated trajectories (139 successful / 133 failed) and 346 annotated actions (182 good / 164 bad), drawn from pre-collected OSWorld-verified rollouts covering all ten OSWorld task categories and seven policy models in ten configurations. Curation preserves category and success–failure balance, excludes tasks that no agent solves or that eight or more configurations solve, and admits only trajectories with fewer than 25 steps; labels are then applied by human annotators rather than taken from OSWorld's verification scripts. The paper describes the annotation as expert work under multi-stage quality control but states no annotator count and no inter-annotator agreement figure.

## Domains

Ubuntu desktop computer use across ten OSWorld software categories: Chrome, Thunderbird, LibreOffice Writer/Calc/Impress, VS Code, GIMP, VLC, OS operations, and multi-app workflows.

## Evaluation

- **Outcome reward model (ORM).** A reward model reads the instruction and the trajectory's screenshot sequence and predicts binary trajectory success, scored against the human trajectory label.
- **Process reward model (PRM).** The same models predict binary correctness for a single annotated action, scored against the human step label.
- **Precision and NPV as primary metrics.** Precision = TP/(TP+FP) and NPV = TN/(TN+FN) are read as reward reliability, with recall = TP/(TP+FN) and specificity = TN/(TN+FP) reported as secondary sample-efficiency indicators.
- **Unanimous Prompt Ensemble (UPE).** Several configurations of VLM and prompt template vote, and a sample is classified only when all members agree, abstaining otherwise.
- **Reported (Tables 4 and 5).** GLM-4.5V-106B with the SE-WSM prompt is the paper's best-performing ORM at 82.9% precision, 77.6% NPV and 80.1% overall accuracy, and the same pairing scores 69.5% / 64.2% / 66.9% as a PRM; UPE reaches 89.8% precision and 93.3% NPV for ORM and 81.7% and 85.1% for PRM. No human baseline is reported.

## Typical Duration

Selected trajectories contain fewer than 25 steps, and the source rollouts were produced under 15-step and 50-step agent limits on OSWorld. Not stated: no wall-clock or token budget is given for the reward model's own judgment pass.

## Main Contribution

An expert-annotated benchmark for evaluating outcome and process reward models on computer-using agent trajectories — presented as the first to cover trajectory-level and step-level CUA reward evaluation jointly — paired with the Unanimous Prompt Ensemble method derived from its findings.

## Key Design Ideas

- Two annotation layers over one trajectory pool: binary trajectory success, and binary correctness of individually selected actions.
- Key-action selection targeting good actions that advance the task while being non-obvious, and bad actions that hinder it while appearing reasonable; redundant actions are largely excluded for annotation objectivity.
- Trajectory curation for category and success–failure balance inside a difficulty band, excluding tasks that no agent solves or that eight or more configurations solve.
- Reward-model implementation factored into VLM × prompt template, reusing three published open-source CUA reward prompts from ZeroGUI, OpenCUA and SE-WSM.

## Strengths

- Trajectory success is human-annotated rather than read off OSWorld's verification scripts, giving labels independent of the script-based verifiers these reward models are meant to replace.
- Trajectories come from seven policy models spanning 25.9–50.8% success rates, so the failure modes on offer are not those of a single agent design.
- Bad actions are annotated inside successful trajectories and good actions inside failed ones, which separates step-level judgment from outcome judgment.

## Limitations

- Repository note: Only selected key actions carry step-correctness labels — 346 across 272 trajectories, with redundant actions largely excluded — so PRM scores measure judgment on deliberately pivotal or deceptive steps rather than uniform per-step accuracy over whole trajectories.
- Repository note: UPE buys precision and NPV by abstaining whenever ensemble members disagree, and the coverage cost is large — overall accuracy is 59.9% for ORM against 80.1% for the configuration the paper designates best by precision, and PRM specificity is 24.4% against 67.7%; the paper does not validate the method inside an actual RL training loop.

## Related Works

- [AgentBoard](./agentboard.md) — Also assigns credit below end-task success, but through annotated subgoal progress inside the environment rather than by testing whether a reward model reproduces human step verdicts.
- [TRACE](./trace.md) — Also evaluates trajectories rather than final answers, but scores agent trajectories on multi-dimensional rubric metrics rather than scoring the judges that issue such verdicts.
