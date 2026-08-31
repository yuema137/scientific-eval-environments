# Robotics

> **English** | [简体中文](../zh/domains/robotics.md) · [← All domains](./README.md)

## Scope

Evaluation on physical robot platforms and robot control. Embodied household simulators and computer-use environments do not fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| RoCo / RoCoBench | 2023 | Coordinate multiple robot arms on shared manipulation tasks through LLM-negotiated plans and waypoint paths. | 6 collaborative manipulation tasks in MuJoCo with semantic variations, plus a 269-question reasoning set; real-UR5 demonstration. | Task success and adaptation under semantic variation; plans executed in MuJoCo and demonstrated on a physical UR5 arm. | [→](../works/rocobench.md) |
| VIKI-Bench | 2025 | Coordinate heterogeneous robot teams: select which robots to activate, plan multi-agent actions, and perceive motion trajectories. | Hierarchical visual-reasoning tasks (3 levels) over 20,000+ samples, 100 scenes, 6 robot embodiments (humanoid, quadruped, wheeled manipulator). | Per-level accuracy and trajectory metrics (RMSE, Hausdorff, directional Fourier) over simulated multi-robot scenes (RoboCasa, ManiSkill3). | [→](../works/viki-bench.md) |
| REFLECT / RoboFail | 2023 | Explain robot manipulation failures from multisensory experience and guide correction planning. | Failure-explanation and correction episodes over tasks with injected failure scenarios (RoboFail). | Failure-explanation quality and correction-planning success, evaluated in simulation and on real-world robot tasks. | [→](../works/robofail.md) |
| AHA | 2024 | Detect and reason over robotic-manipulation failures in free-form natural language. | Failure detection/reasoning over procedurally generated failure trajectories (79 RLBench tasks); evaluated on real-world failure data. | Fuzzy semantic-match, ROUGE-L, and binary-success scoring; generalization to real-world failure datasets and unseen tasks. | [→](../works/aha.md) |
| RoboFAC | 2025 | Analyze and correct robotic manipulation failures across understanding, analysis, and correction. | 9,440 erroneous trajectories, 78,623 QA pairs, 53 scenes (simulation + real); eight QA dimensions. | Per-dimension failure-analysis accuracy; deployed as a supervisor in a real-world VLA control pipeline. | [→](../works/robofac.md) |
| LabRobFail | 2026 | Analyze robotic failures in chemical self-driving laboratories across control, physics, and semantic levels. | 20,000+ simulated trajectories, 70+ scenarios, 5 failure categories / 11 types (Isaac Sim). | Six capability scores incl. detection (90.83%) and temporal localization (77.21%); +4–16 pp downstream success as a supervisor. | [→](../works/labrobfail.md) |
| BadRobot | 2024 | Jailbreak embodied LLM stacks into executing malicious physical actions. | 277 malicious queries across six harm categories against Code-as-Policies, ProgPrompt, VoxPoser and others. | Manipulate Success Rate (avg. 68.57%) and harmfulness scores; executed on real UR3e and myCobot arms. | [→](../works/badrobot.md) |
| ASIMOV | 2025 | Judge the semantic safety of situations and actions for VLMs acting as robot brains. | Static safety-judgment evaluation over injury-report- and visual-scene-grounded data, with generated robot constitutions. | Alignment rate with human preferences on desirability and safety; top rate 84.3% with generated constitutions. | [→](../works/asimov.md) |
| RoboSpatial | 2024 | Understand robot-centric spatial relationships — configuration, context, compatibility — from real scenes. | 1M images, 5K 3D scans, 3M spatial relationships; 2D- and 3D-ready evaluation sets. | Downstream spatial-task performance vs. baselines; real-manipulator grasp success (52.6% vs. 23.7% baseline). | [→](../works/robospatial.md) |
| PAC Bench | 2025 | Understand manipulation prerequisites — object Properties, Affordances, Constraints — from a task-executability view. | 30,000+ annotations: 673 real images (115 classes), 100 humanoid-view scenarios, 120 simulated constraint scenarios. | Per-category accuracy over frontier and open VLMs; real robot-viewpoint (Unitree G1) imagery. | [→](../works/pac-bench.md) |
| Robo2VLM | 2025 | Reason about manipulation scenes — spatial, goal-conditioned, interaction — from robot sensor context. | 684,710 multiple-choice questions over 463 scenes and 3,396 tasks, from 176K real tele-operated trajectories. | Multiple-choice accuracy with sensor-derived (pose, gripper, force) ground truth requiring no human labeling. | [→](../works/robo2vlm.md) |
| ManipBench | 2025 | Reason about low-level robot movements, including object-object interaction and deformables. | 12,617 multiple-choice questions over real robot data, fabric scenarios, and simulated environments; 33 VLMs. | Multiple-choice accuracy correlated with real-world manipulation task performance. | [→](../works/manipbench.md) |
| PhysBench | 2025 | Understand physical-world properties, relationships, scene, and dynamics as the perception substrate for robot agents. | 10,002 interleaved video-image-text entries in 4 domains, 19 subclasses, 8 capability dimensions; 75 VLMs. | Multiple-choice accuracy; demonstrated transfer to the MOKA embodied agent (static VQA, not robot control). | [→](../works/physbench.md) |
| CaP-X | 2026 | Control robot manipulation by synthesizing and executing programs over perception and control primitives. | 7 core tasks (+30 LIBERO-PRO, +2 BEHAVIOR) within a 187-task suite; 12 frontier models across abstraction tiers. | Success rate over 100 trials/task/tier vs. human expert programs; paired methods transfer to real Franka Panda and AgiBot G1. | [→](../works/cap-x.md) |
| VLA-Arena | 2025 | Evaluate Vision-Language-Action models as generalist robot-manipulation policies, with task difficulty factorized along Task Structure, Language Command, and Visual Observation axes to separate robust grounding from memorization. | 11 task suites / 170 simulated manipulation tasks in four dimensions (Safety, Distractor, Extrapolation, Long Horizon), each at three difficulty levels (L0–L2) with language (W0–W4) and visual (V0–V4) perturbation probes; built on RoboSuite, LIBERO, and VLABench. | Success Rate and Cumulative Cost in simulation; fine-tuning restricted to L0 with testing on unseen L1–L2 to measure generalization. Repository note: simulation-only, no real-robot experiments reported. | [→](../works/vla-arena.md) |
| RoboGraphBench | 2026 | Evaluate agentic foundation models as high-level planners for long-horizon embodied tasks (tabletop manipulation and indoor navigation), characterizing difficulty by the task-state horizon — the span of task-relevant state transitions an agent must track, explore, and update. | 588 episodes across 84 household scenes (399 tabletop + 189 indoor-navigation), each a baseline plus six intervention conditions; RoboGraph compiles tasks into symbolic scene graphs (avg. 18.4 nodes, 14.3 subgoals); 15 agentic models. | Unified closed-loop harness (100-step max; goal predicates + stop action) in semantic and visual modes (RoboTwin 2.0, RoboCasa); Success Rate and SSAL plus state-management (maintenance/exploration/updating) and recovery-detection/grounding metrics. Repository note: evaluates high-level planning, not low-level control; simulation only. | [→](../works/compiling-and-benchmarking-task-state-horizons-for.md) |
| EngDesign | 2025 | Robot design and planning posed as design problems with stated goals, constraints and performance requirements rather than as questions with reference answers. | Robotics, 10 of 101 design tasks (473 gradable items) across nine engineering areas; single-turn generation by default, with an iterative protocol allowing up to 10 rounds of simulator feedback. | Structured model output executed by a task-specific evaluation script running the relevant simulator, returning a binary pass/fail, a 0–100 partial-credit score and a detailed log. Repository note: simulation-verified design tasks; no physical robot platform or control policy is evaluated. | [→](../works/engdesign.md) |
| ATOM-Bench | 2026 | Execute real-robot tabletop manipulation factorized into motor atoms (pick-place, reorientation, pushing, stacking, pouring, articulated-object access) and instruction atoms (color, shape, size, counting, exclusion, spatial relations, goal destination), then recombine them into held-out compositional tasks. | 30 atomic and 24 held-out compositional tasks on paired single-arm (Franka Panda) and dual-arm (Agilex Cobot Magic) tracks; 3,000 human teleoperation demonstrations for atomic fine-tuning, and five VLA policies evaluated over 2,700 physical rollouts at 10 shared test seeds per task. | Physical rollouts on real hardware with mask-guided object placement for reproducible initial states; task success rate plus human-annotated per-atom Process Success Rate, aggregated into Atomic Score and Compositional Failure Share to separate weak atoms from failed composition. Repository note: no simulation results are reported. | [→](../works/atom-bench.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the robotics subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`MANIP` manipulation & grasping · `CTRL` low-level control & motion generation · `PLAN` task planning & high-level embodied decision-making · `NAV` mobile robotics & navigation · `PERC` robot perception & scene understanding · `MULTI` multi-robot systems & coordination · `VLA` vision-language-action policies & imitation learning · `DIAG` failure diagnosis, monitoring & recovery · `SAFE` robot safety & adversarial robustness · `LAB` laboratory & self-driving-lab robotics · `DESIGN` robot design & mechanism synthesis · `GEN` curriculum-wide or unspecified, no single subfield

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
| ATOM-Bench | MANIP, VLA | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✘ | ✔ | ✔ | 2 | 1 | 4 | **9** |
| RoboFAC | DIAG, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **2.5** | ✘ | ◐ | ◐ | 2 | 3 | 3 | **9** |
| PAC Bench | PERC, MANIP | ✘ | ✘ | ◐ | ✔ | ✘ | ✔ | ✘ | **2.5** | ✘ | ✘ | ✘ | 3 | 3 | 3 | **9** |
| CaP-X | MANIP, CTRL | ✘ | ✘ | ✘ | ✔ | ✘ | ◐ | ✔ | **2.5** | ✔ | ✘ | ✘ | 3 | 1 | 4 | **9** |
| ManipBench | MANIP, CTRL | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✔ | ✘ | ◐ | 3 | 3 | 3 | **10.5** |
| VLA-Arena | VLA, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✔ | 3 | 2 | 4 | **10** |
| Robo2VLM | PERC, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✔ | ✘ | ✘ | 3 | 3 | 1 | **8** |
| AHA | DIAG, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ◐ | ◐ | **2** | ✘ | ✘ | ◐ | 2 | 3 | 2 | **7.5** |
| RoboSpatial | PERC, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
| RoCo / RoCoBench | MULTI, MANIP | ✘ | ✘ | ◐ | ✘ | ✘ | ◐ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| REFLECT / RoboFail | DIAG, MANIP | ✘ | ✘ | ✘ | ✔ | ✘ | ◐ | ◐ | **2** | ✘ | ◐ | ✘ | 2 | 2 | 2 | **6.5** |
| PhysBench | PERC | ✘ | ✘ | ✘ | ✔ | ✘ | ◐ | ✘ | **1.5** | ✔ | ✘ | ✔ | 3 | 3 | 3 | **11** |
| RoboGraphBench | PLAN, NAV, MANIP | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ◐ | 3 | 2 | 4 | **10** |
| LabRobFail | DIAG, LAB | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ◐ | **1.5** | ✘ | ✘ | ◐ | 3 | 3 | 3 | **9.5** |
| ASIMOV | SAFE | ✘ | ✘ | ✘ | ◐ | ✘ | ✔ | ✘ | **1.5** | ✘ | ✔ | ✔ | 3 | 3 | 1 | **9** |
| VIKI-Bench | MULTI, PLAN, PERC | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
| BadRobot | SAFE, MANIP | ✘ | ✘ | ✘ | ◐ | ✘ | ◐ | ✘ | **1** | ✘ | ◐ | ✘ | 2 | 2 | 3 | **7.5** |
| EngDesign | DESIGN, PLAN | ✘ | ✘ | ✘ | ? | ✘ | ✘ | ◐ | **0.5** | ✘ | ✔ | ◐ | 3 | 1 | 3 | **8.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md)
- [LabRobFail](../works/labrobfail.md)
- [ATOM-Bench](../works/atom-bench.md)
- [CaP-X](../works/cap-x.md)
- [VLA-Arena](../works/vla-arena.md)
- [EngDesign](../works/engdesign.md)
- [PAC Bench](../works/pac-bench.md)
- [VIKI-Bench](../works/viki-bench.md)
- [Robo2VLM](../works/robo2vlm.md)
- [RoboFAC](../works/robofac.md)
- [ManipBench](../works/manipbench.md)
- [ASIMOV](../works/asimov.md)
- [PhysBench](../works/physbench.md)
- [RoboSpatial](../works/robospatial.md)
- [AHA](../works/aha.md)
- [BadRobot](../works/badrobot.md)
- [RoCo / RoCoBench](../works/rocobench.md)
- [REFLECT / RoboFail](../works/robofail.md)
