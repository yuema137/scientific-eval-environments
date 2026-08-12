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

## Related Works

- [PDAgent-Bench](../works/pdagent-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [VerilogEval](../works/verilogeval.md)
- [RTLLM](../works/rtllm.md)
- [RTL-Repo](../works/rtl-repo.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [CVDP](../works/cvdp.md)
- [AssertionBench](../works/assertionbench.md)
- [FVEval](../works/fveval.md)
- [HLS-Eval](../works/hls-eval.md)
- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [EEE-Bench](../works/eee-bench.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [TeleQnA](../works/teleqna.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [ERI Benchmark](../works/eri-benchmark.md)
