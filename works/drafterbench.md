# DrafterBench (2025)

> **English** | [简体中文](../zh/works/drafterbench.md)

> **First appeared:** 2025-07-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2507.11527)

## Overview

DrafterBench is an open-source benchmark for LLM agents on technical-drawing revision in civil engineering: 1,920 tasks built from twelve revision task types and 46 custom drawing-manipulation tools, scored by reading the recorded operation chain rather than the rendered drawing.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.11527>
- **Code:** <https://github.com/Eason-Li-AIS/DrafterBench>
- **Dataset:** <https://huggingface.co/datasets/Eason666/DrafterBench>
- **Venue:** arXiv preprint (cs.AI, cs.CE), 2025

## Summary

The authors identify drawing revision as, in their words, "one of the most labor-intensive and low-tech tasks that needs automation in Civil Engineering", based on interviews with more than ten North American construction companies, and turn it into an agent benchmark. Tasks are summarized from 100+ real revision files supplied by design firms and construction companies, and are issued to the model as natural-language revision instructions over PDF drawings containing text, tables and vector entities such as lines, rebars and columns. Beyond plain function calling, the benchmark deliberately probes whether an agent can work from instructions that are unstructured, vague, or incomplete, and whether it applies unstated drafting conventions — what the paper calls implicit policy awareness, for example saving the revised file under a company-policy filename. Scoring is fully automatic: dual functions log the operation path without modifying files, so an agent's operation chain is compared against a reference chain instead of the rendered PDF being inspected visually.

## Tasks

1,920 tasks. Twelve task types come from crossing three object elements (text, tables, vector entities) with four revision operations (adding content, content modification, position mapping, format updating) — for example adding text to a target area, deleting target strokes, replacing or clearing table cells, and changing text color, font type and font size. Each task type is then crossed with five binary instruction controllers — structured vs. unstructured language style, precise vs. vague values, complete vs. incomplete information, single vs. multiple objects per instruction, single vs. multiple operations per object — with five tasks generated per combination (12 × 2^5 × 5 = 1,920); a sixth controller, function-pipeline complexity, varies by task type. The agent is given 46 customized drawing-revision functions implemented over PyMuPDF, Reportlab, OpenCV and pytesseract. Tasks were human-verified for practical applicability.

## Domains

Civil & Structural Engineering: the task universe is civil-engineering construction drawings and the revision workflow that design firms and construction companies run between the design and construction stages, with drawing objects including structural entities such as rebars and columns. No co-domain is claimed — the benchmark evaluates document-level engineering production work rather than analysis of a physical structure.

## Evaluation

- Two-level automatic scoring. Level 1 is code executability, worth 0 or 30 points. Level 2 is target completeness over six subtasks, each computed as (TP − FP) / (TP + FN) and scaled to 70/6 points. Plan execution is additionally scored by intersection-over-union between the agent's recorded operation chain and the reference chain. A comprehensive score takes the mean task score minus a penalty for weak subtasks, so uniformly competent agents are separated from spiky ones.
- Results are reported per instruction controller — structured vs. unstructured phrasing, precise vs. vague detail, complete vs. incomplete instructions, object and operation cardinality — as well as in aggregate.
- **Reported (paper).** OpenAI o1 81.92 average / 79.90 comprehensive; Claude 3.5 Sonnet 76.27 / 73.79; DeepSeek-V3-685B 76.05 / 73.09; Qwen2.5-72B 74.77 / 72.05; ChatGPT-4o 74.49 / 71.76; Llama 3-70B 70.67 / 67.55. Models score markedly higher on precise, complete instructions than on vague or erroneous ones.
- **Reported (official repository leaderboard).** Later models were added after publication: o3-2025 86.03 average, gpt-4.1-2025 80.16, o4-mini-2025 79.93.

## Typical Duration

N/A — tasks are single-instruction revisions resolved by one function-call chain; the paper does not report per-task step counts, wall-clock time, or token budgets.

## Main Contribution

A benchmark that tests LLM agents on an industrial civil-engineering task rather than a synthetic tool-use setting, and that decomposes performance into four capabilities the authors argue the job actually requires — structured-data comprehension, function execution, instruction following, and critical reasoning under degraded instructions — with an evaluation that reads operation chains so that scoring needs no visual inspection of the revised drawing.

## Key Design Ideas

- Dual functions record the operation path without touching files, making the trajectory, not the rendered PDF, the scored artifact.
- Instruction quality is a controlled variable: vagueness, missing information and unstructured phrasing are toggled independently, so a score drop is attributable to a specific instruction defect.
- Implicit policy awareness is scored — correct completion requires drafting conventions the instruction never states.
- The toolset and task generator are open and extensible, so users can register additional revision functions or task types.

## Strengths

- Tasks are derived from 100+ real revision files supplied by North American design and construction firms, and human-verified.
- Deterministic, fully automatic scoring with a per-capability and per-controller breakdown rather than a single pass rate.
- MIT-licensed with a public dataset and a maintained leaderboard.

## Limitations

- Instructions specify what to change; no task requires a structural or code-compliance judgment, so civil-engineering knowledge is exercised mainly as drafting convention rather than as design or verification.
- The vague and incomplete conditions have no unambiguous ground truth, and the paper notes reasoning models sometimes treat vague instructions as errors instead of resolving them.
- Repository note: drawing objects are PDF text, tables and vector entities rather than analysis or BIM models, so the benchmark measures document-level automation, not design verification.
- Repository note: the paper does not disclose per-task token or step budgets.

## Related Works

- [StructureClaw](./structureclaw.md) — Also a civil/structural agent benchmark, but scored on solver-verified structural models rather than drawing edits.
- [AEC-Bench](./aec-bench.md) — Also puts agents on real construction documents, with sandboxed executable verifiers.
- [AECBench](./aecbench.md) — Also an AEC-field LLM benchmark, but knowledge QA rather than tool-executing agents.
