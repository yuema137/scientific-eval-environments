# Electrical Engineering

> **English** | [简体中文](../zh/domains/electrical_engineering.md) · [← All domains](./README.md)

## Scope

Electrical and electronic engineering.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | Electrical Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| VerilogEval | 2023 | Generate Verilog RTL that meets a functional specification. | 156 HDLBits problems; the LLM generates RTL, checked by simulation against golden solutions. | Functional correctness via simulation vs. golden solution; pass@k. | [→](../works/verilogeval.md) |
| RTLLM | 2023 | Generate complete design RTL from natural-language instructions. | 29 hand-crafted designs (50 in v2.0), graded on three progressive goals. | Syntax, functionality, and design-quality goals; self-planning prompting evaluated on GPT-3.5. | [→](../works/rtllm.md) |
| RTL-Repo | 2024 | Complete Verilog code that fits a large multi-file design project. | 4,000+ Verilog samples from public GitHub, each with full-repository context. | Edit similarity and exact match against the reference completion. | [→](../works/rtl-repo.md) |
| VHDL-Eval | 2024 | Generate functionally correct VHDL from problem descriptions. | 202 problems (Verilog-translated + aggregated public), with self-verifying testbenches. | Functional correctness across zero-shot, in-context learning, and PEFT settings. | [→](../works/vhdl-eval.md) |
| CVDP | 2025 | Solve comprehensive RTL design, verification, and debugging problems. | 783 problems / 13 categories (NVIDIA), in non-agentic and agentic formats. | pass@1 in a containerized OSS-EDA environment; SOTA ≤34% on code generation. | [→](../works/cvdp.md) |
| AssertionBench | 2024 | Generate functionally correct hardware assertions for digital designs. | 100 OpenCores Verilog designs with formally verified reference assertions. | Fraction of functionally correct assertions vs. GoldMine/HARM references. | [→](../works/assertionbench.md) |
| FVEval | 2024 | Perform formal verification tasks for digital hardware. | Three sub-tasks (NL2SVA-Machine, NL2SVA-Human, Design2SVA) with pre-generated datasets. | Correctness of assertions/testbenches validated by the Cadence Jasper formal tool. | [→](../works/fveval.md) |
| HLS-Eval | 2025 | Generate and optimize high-level-synthesis hardware code. | 94 HLS designs with natural-language descriptions and testbenches; two tasks. | Parseability, compilability, runnability, synthesizability + pass@k on Vitis HLS. | [→](../works/hls-eval.md) |
| AnalogCoder | 2024 | Design analog circuits via training-free Python code generation. | Curated analog-design task set (24 tasks in the official repository). | Pass@1/Pass@5 ranked by tasks solved; 20 circuits vs. GPT-4o's 15. | [→](../works/analogcoder.md) |
| AnalogXpert | 2024 | Synthesize analog circuit topologies from design requirements. | 30 real + 2,000 synthetic topology cases; SPICE-code representation. | One-trial structural correctness (programmatic + human review); 40%/23% vs. GPT-4o 3%. | [→](../works/analogxpert.md) |
| EEE-Bench | 2024 | Solve multimodal EE problems requiring circuit and diagram understanding. | 2,860 problems across 10 EE subdomains, with intricate circuit/system-diagram imagery. | Accuracy over 17 LLMs/LMMs (avg 19.48–46.78%); a "laziness" text-over-vision analysis. | [→](../works/eee-bench.md) |
| MMCircuitEval | 2025 | Answer circuit questions across the EDA design flow. | 3,614 multimodal QA pairs across digital and analog circuits and EDA stages. | Accuracy by design stage, circuit type, tested ability, and difficulty. | [→](../works/mmcircuiteval.md) |
| TeleQnA | 2023 | Answer telecommunications-knowledge questions grounded in standards. | 10,000 multiple-choice questions from 3GPP/IEEE standards and research literature. | Multiple-choice accuracy against an active-telecom-professional baseline. | [→](../works/teleqna.md) |
| ControlAgent / ControlEval | 2024 | Design controllers meeting stability and performance specifications. | 500 control-design tasks (ControlEval) across first/second-order, time-delay, and higher-order systems. | Average and agent success rates against design criteria vs. toolbox+human baselines. | [→](../works/controleval.md) |
| PDAgent-Bench | 2026 | VLSI physical design / Electronic Design Automation — chip back-end implementation spanning floorplanning, power planning, placement, clock-tree synthesis, routing, static timing analysis, and engineering change orders. | 353 curated task-level problems across five capability dimensions (foundational knowledge, report comprehension, root-cause analysis, static timing analysis, script generation) plus 10 full-flow design projects, using TSMC 28nm / Nangate 45nm and tools including Cadence Innovus, Synopsys ICC2/PrimeTime, and OpenROAD; 11 models. | Task-level pass@1/pass@5 with script solutions checked by execution and conceptual answers scored against three-expert-validated references; workflow-level full-flow runs assessed by timing closure and DRC-violation outcomes on designs such as TinyRISCV, AES-256, and Ethernet MAC. | [→](../works/pdagent-bench.md) |
| ERI Benchmark | 2026 | Electrical engineering as one of nine covered fields, with six subdomains: circuits, electronics, signals and systems, power systems, electromagnetics, and control systems. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item. | [→](../works/eri-benchmark.md) |
| EngDesign | 2025 | Electrical and electronic design posed as specifications with goals, constraints and performance requirements — control design, digital hardware design, analog IC design and signal processing. | Control Design (18), Signal Processing (18), Digital Hardware Design (17) and Analog IC Design (5) within 101 design tasks carrying 473 gradable items across nine engineering areas; 48 of the 101 tasks require proprietary domain software such as MATLAB or Cadence. | Structured model output executed by a task-specific script running the relevant simulator (MATLAB, SPICE/Cadence), returning a binary pass/fail, a 0–100 partial-credit score and an evaluation log; analog IC design is reported as the weakest of the nine areas. | [→](../works/engdesign.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the electrical engineering subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`DIG` digital design & RTL code generation · `VER` hardware verification & assertions · `HLS` high-level synthesis · `EDA` EDA tooling & VLSI physical design · `ANA` analog & mixed-signal circuit design · `SS` signals, systems & signal processing · `COMM` communications & telecommunications · `CTRL` control systems · `GEN` curriculum-wide or unspecified, no single subfield

**Two scores, not one.** The columns split into **coverage** — what the evaluation setup puts under test — and **rigor** — how far you can trust what it reports. They are summed separately because they pull against each other: a benchmark can put everything under test and verify none of it carefully, and a deliberately narrow one can be the most trustworthy thing on the page. Rows are ordered by `Cov`, highest first, and by `Rig` within equal coverage; remaining ties keep Comparison-table order. Coverage leads because it is the axis a reader scans for — *does this benchmark even put my problem under test* — and `Rig` then says how far to trust what it reports.

### Coverage (`Cov`, max 7)

Yes/no, ordered by rarity — the properties fewest works have come first, so the left of the group is where the field is thin. A property nearly every work satisfies does not earn a column: *writing and running code* was dropped on that ground.

- **Net** — network or live external retrieval permitted; a supplied fixed corpus does not count.
- **E2E** — end-to-end research: a question or goal only, with no source paper, reference implementation, or step-by-step specification supplied, and the agent drives the whole investigation.
- **Cost** — budget or resource cost is a scored or priced dimension, not merely a step cap.
- **MM** — multimodal content is load-bearing, either required as input or scored as an output artifact.
- **Repro** — grounded in a specific published result the agent must match or recover.
- **Real** — real experimental or observational data, as opposed to synthetic or simulated (a digital twin is simulated).
- **Inter** — interactive: the agent takes multiple actions against an environment, tool, or simulator and gets feedback that shapes the next one.

### Rigor (`Rig`, max 13)

- **Human** — a measured human-expert baseline or human reference performance anchors the scale. `◐` where the anchor is a published result or expert reference implementation rather than a measured human run.
- **Rubric** — an expert-authored rubric or official marking scheme with named criteria or weights; a continuous automatic metric is not a rubric.
- **Contam** — a deliberate mechanism makes the answer unmemorizable: post-cutoff sourcing, unpublished or newly authored problems, counterfactual alteration, on-demand generation, or screened leakage. Withholding a published paper at evaluation time is `◐` — it does not remove that paper from a pretraining corpus.
- **Verif** `0`–`3` — how far the score can be trusted without trusting a model. `0` scored only by an LLM judge or rubric, with no validation of that scorer · `1` judge or rubric scoring whose agreement with human experts is measured and reported · `2` deterministic checks alongside judge or rubric scoring · `3` fully deterministic — execution, tests, numerical comparison to a reference, symbolic checking, or a proof kernel, with no judge in the loop. This replaces a plain yes/no *deterministic verification* column, which 85% of works satisfied and which therefore separated nothing; as a ladder it separates a great deal. A separate `Judge` column was dropped as near-redundant with `Verif` < 2.
- **Scale** `0`–`3` — items evaluated **in this domain**: `0` fewer than 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 or more · `?` the source does not give a per-domain count. This counts items, not effort: 30 paper-reproduction tasks are far more work than 3,000 exam questions, and the column cannot see that.
- **Fail** `0`–`4` — how deep the failure analysis goes, because "reports a failure analysis" spans everything from a single remark to a controlled experiment. `0` nothing beyond headline scores · `1` narrative remarks on where models fall short, no classes named · `2` named error classes or illustrative case studies, but no counts or shares · `3` a quantified failure account: a taxonomy with per-class counts or shares, or measured breakdowns isolating specific failure conditions · `4` level 3 plus a controlled experiment or ablation built to test *why* the failures occur.

### Reading the two scores

Yes/no columns score `✔` 1, `◐` 0.5, `✘` 0, `?` 0; graded columns contribute their number, with `?` scoring 0. `Domain` does not score.

Three cautions. A `?` costs exactly what a `✘` costs, so both scores are floors on what a work *demonstrably* does, not verdicts on it. Neither score is a quality ranking: high `Cov` with low `Rig` describes a benchmark that reaches for everything and pins down little, while low `Cov` with high `Rig` describes one that measures a narrow thing carefully — and which of those is the right design depends entirely on the question being asked. And `Cov` is a property of the *evaluation setup*, not of the science: a work can sit at the bottom of this table and still be the most important paper in its subfield.

For multi-domain suites the row describes this domain's slice, as in the Comparison table.
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PDAgent-Bench | EDA | ✘ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| EngDesign | CTRL, DIG, ANA, SS | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ◐ | ✔ | 3 | 1 | 3 | **8.5** |
| AnalogXpert | ANA | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| ControlAgent / ControlEval | CTRL | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | 2 | 1 | **6.5** |
| RTL-Repo | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| EEE-Bench | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ✘ | 2 | 3 | 4 | **9** |
| AssertionBench | VER | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| AnalogCoder | ANA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 1 | 2 | **6** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| CVDP | DIG, VER | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✔ | 2 | 2 | 3 | **8** |
| FVEval | VER | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ◐ | ✘ | ◐ | 3 | 2 | 2 | **8** |
| MMCircuitEval | DIG, ANA, EDA | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ✘ | 2 | 3 | 3 | **8** |
| HLS-Eval | HLS | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ✘ | ✘ | ✘ | 3 | 1 | 0 | **4** |
| TeleQnA | COMM | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✔ | ✘ | ✘ | 3 | 3 | 3 | **10** |
| ERI Benchmark | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✔ | 2 | 2 | 3 | **9** |
| VHDL-Eval | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 1 | **6.5** |
| VerilogEval | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 1 | **6** |
| RTLLM | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ◐ | ✘ | ✘ | 3 | 1 | 1 | **5.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [PDAgent-Bench](../works/pdagent-bench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [EngDesign](../works/engdesign.md)
- [CVDP](../works/cvdp.md)
- [HLS-Eval](../works/hls-eval.md)
- [AnalogXpert](../works/analogxpert.md)
- [EEE-Bench](../works/eee-bench.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [FVEval](../works/fveval.md)
- [AssertionBench](../works/assertionbench.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [RTL-Repo](../works/rtl-repo.md)
- [AnalogCoder](../works/analogcoder.md)
- [TeleQnA](../works/teleqna.md)
- [VerilogEval](../works/verilogeval.md)
- [RTLLM](../works/rtllm.md)
