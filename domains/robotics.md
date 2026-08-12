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

## Related Works

- [VLA-Arena](../works/vla-arena.md)
- [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md)
- [RoCo / RoCoBench](../works/rocobench.md)
- [VIKI-Bench](../works/viki-bench.md)
- [REFLECT / RoboFail](../works/robofail.md)
- [AHA](../works/aha.md)
- [RoboFAC](../works/robofac.md)
- [LabRobFail](../works/labrobfail.md)
- [BadRobot](../works/badrobot.md)
- [ASIMOV](../works/asimov.md)
- [RoboSpatial](../works/robospatial.md)
- [PAC Bench](../works/pac-bench.md)
- [Robo2VLM](../works/robo2vlm.md)
- [ManipBench](../works/manipbench.md)
- [PhysBench](../works/physbench.md)
- [CaP-X](../works/cap-x.md)
- [EngDesign](../works/engdesign.md)
