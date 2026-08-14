# An LLM-driven framework for cosmological model-building and exploration (2025)

> [English](../../works/an-llm-driven-framework-for-cosmological-model-bui.md) | **简体中文**

## Overview

一套多阶段评估框架，衡量 LLM 驱动的 coding agent 能否在容器化环境中修改 CLASS 玻尔兹曼求解器代码库，自主提出、实现并探索另类宇宙学模型。agent 的提交由三方面自动打分：二元的执行里程碑、与真值参考实现的数值一致性，以及基于真实巡天数据算出的宇宙学似然/张力奖励。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://ml4physicalsciences.github.io/2025/files/NeurIPS_ML4PS_2025_178.pdf>
- **Venue:** Machine Learning and the Physical Sciences Workshop, NeurIPS 2025 (preprint number MIT-CTP/5945)

## Summary

作者称，他们「提出了一个多阶段框架，用于评估 LLM 驱动的 agent 自主提出、实现并探索宇宙学模型的能力」。agent 在一个 Podman/Docker 容器中工作，容器预装了 CLASS 3.3.0，并附带各阶段的 prompt 文件、由 LLM 生成的 `background.c`、`perturbations.c` 与 `input.c` 三个模块的文件索引、模型描述以及辅助测试代码。它要交付的成果是一份针对 CLASS 仓库的补丁，补丁从容器中导出后自动评估。论文的定位明确是评估性的：其结论称这些结果给出了「一个具体的框架，用以评估 AI agent 在融合领域知识、数学推理、编程与实证验证的复杂科学工作流上的表现」。

## Tasks

任务按每个宇宙学模型实例组织成三个顺序阶段。阶段 1（Model Implementation）要求读懂模型描述并修改 CLASS 予以实现，代码能编译且确实实现了目标模型即算成功。阶段 2（Computing Observables）要求用改过的代码，通过提供的辅助脚本在基准参数下计算功率谱等可观测量。阶段 3（Parameter Exploration and Rewards）评估所实现模型与观测的吻合程度，视模型是否适合做优化，分别以 *Minimization* 模式（数值极大似然拟合）或 *Exploration* 模式（agent 自行提出并测试参数组合）运行。

每个模型实例由三份材料界定：模型描述（要么是一份附带深入实现提示的 `description.md`，要么是原始研究论文的 TeX 源码）、用于测试改后代码并支持与目标实现做定量比较的基准参数（Fiducial Parameters），以及一份上下文文件（`problem_context.yaml`）。

受评的目标模型有两个：唯象的 *Thawing Quintessence*（TQ）模型与 *Early Dark Energy*（EDE）模型，难度依次递增，二者都有可用的真值实现。另有两组假设生成实验，要求 agent 自行发明暗能量模型（*One-Shot*，以及 *One-Shot + Summary*——后者额外提供由 `gemini-2.5-pro` 对五篇近期论文所作的摘要）。论文报告，在这两组上下文信息不同的额外假设生成实验中，agent 未能生成通过全部二元执行里程碑的代码。

## Domains

天文学——具体地说是宇宙学：在玻尔兹曼求解器中实现另类暗能量模型与修改宇宙学模型，计算 CMB 与物质功率谱，并将其与 DESI 重子声波振荡测量、Planck 早期宇宙 CMB 三参数先验、Pantheon+ 超新星以及 SH0ES 哈勃常数测量相对照。物理学是名副其实的共同领域（这些模型本身是暗能量场论），而科学软件与系统方面的工作则是工具性的（要给一个约 43,000 行的 C 代码库外加 10,000 行数值文件打补丁）。

## Evaluation

评分是自动的，分层进行：

- **二元执行里程碑**——三个里程碑，分别追踪 agent 是否生成了补丁、补丁能否编译、以及能否据此计算可观测量。
- **数值准确性**——把 agent 算出的物理量（功率谱与暗能量场的演化）与实现同一宇宙学模型的真值仓库比对，报告最大相对偏差。若阶段 2 执行失败，则另调用一个 LLM（`o1-2024-12-17`）比对模型描述与生成的补丁、找出不一致之处，充当 LLM-as-a-Judge。
- **阶段 3 的宇宙学奖励**——（1）数据似然，并配以贝叶斯信息准则（BIC）来惩罚靠增加参数换来的过拟合；（2）哈勃张力，由预测的 `H0` 与 SH0ES 比较得出，或改比 `M_B` 值，作为更稳健的晚期宇宙诊断；（3）CMB 功率谱一致性，即预测 `C_l` 相对 Planck 2018 `C_l` 的最大偏差（以宇宙方差为单位），用作一致性检查。

**已报告结果（表 1，Target Artifact-based Evaluation Results）。** 受评 agent 是搭配 `claude-sonnet-4-20250514` 的 Claude Code。三种设定都通过了执行里程碑。`Ω_X`/mPk(0)/mPk(1) 的最大相对偏差：EDE [curated] 0.026/0.116/0.110；TQ [curated] 2.2e−7/1.1e−4/7.6e−5；TQ [paper] 0.248/0.100/0.027。`ln L`：558（EDE curated）、830（TQ curated）、830（TQ paper）。BIC：N/A、−1616、−1616。`H0` 张力：4.12σ [67.94]、4.73σ [67.19]、3.57σ [68.61]。`M_B` 张力：N/A、5.01σ [−19.42]、5.03σ [−19.42]。

**表 2（LLM-proposed Model Results）。** ΛCDM 参考：`ln L` 831，BIC −1640，`H0` 张力 4.22σ [67.82]，`M_B` 张力 5.25σ [−19.43]。agent 提出的 EDE-RC（One-Shot）：828、−1604、2.75σ [69.63]、4.69σ [−19.41]。agent 提出的 ODEM（One-Shot + Summary）：828、−1612、3.70σ [68.46]、4.70σ [−19.41]。

## Typical Duration

TODO(reference) — 论文未报告逐任务的 wall-clock 时间、轨迹长度或 token 预算。

## Main Contribution

按作者的框定，这是一个多阶段框架，用于评估 LLM 驱动的 agent 能否自主提出、实现并探索宇宙学模型。应用结果表明：给足丰富的领域上下文时，agent 能给出合理的实现，但若没有专家精心编写的 prompt，数值准确性就难以达标；而 agent 自行提出的一个暗能量模型在观测拟合上可与标准模型相当，代价是需要额外的参数。

## Key Design Ideas

- 用的是真实而统一的科学工作流：论文认为宇宙学格外适合这类评估，因为「几乎所有实现另类宇宙学模型的论文都依赖 2–4 个代码库」，另类理论「必须通过一组统一的检验」，因此模型发现「可以重新表述为一个带明确定义指标的优化问题」。
- 把能力层次拆成三个顺序阶段，各有各的成功判据，于是部分进展是看得见的，不会坍缩成单一的通过/失败。
- 用 *curated description* 与 *paper-to-code* 两种条件作对照（把 `description.md` 换成论文的 TeX 源文件），以分离 agent 的成功究竟有多少依赖人工撰写的实现指引。
- 打分锚定在真值目标仓库上，比的是物理量的最大相对偏差，而不是评判代码文本。
- 增加一层实证验证（似然、BIC、哈勃张力、CMB 一致性），使得「能编译的实现」不会自动等同于「成功的实现」。
- 有意切断 agent 的网络访问：启动命令禁用 `WebSearch` 与 `WebFetch` 工具，容器还覆盖了 `ping`、`curl` 等联网命令，让它们经过只放行白名单域名的网络过滤器。
- 为 CLASS 的大模块提供由 LLM（`gemini-2.5-pro`）生成的文件索引，以免导航成本主导整个任务。

## Strengths

- 评分协议是定量且以物理为根基的，而非依据评分细则：既有与参考实现的数值偏差，也有对照 DESI、Planck、Pantheon+ 与 SH0ES 真实数据算出的似然/BIC/张力奖励。
- curated 描述与论文原文两种条件的对比给出了可解读的发现——论文报告，从论文而非从整理好的描述出发，「会显著削弱数值准确性，尽管定性行为仍然正确」。
- 环境是货真价实的可执行任务环境（容器化的 CLASS 3.3.0，以补丁形式提交），而不是一套静态题目。
- 假设生成阶段把评估从实现推进到开放式的模型提出，并对 agent 自己发明的模型施加同样的实证奖励。

## Limitations

- 只评估了两个带真值的宇宙学模型（Thawing Quintessence 与 Early Dark Energy），任务池非常小。
- 只评估了一种 agent 配置（Claude Code 搭配 `claude-sonnet-4-20250514`），没有跨模型对比；文中提到的其他 LLM 只承担评判或摘要，并非受评的 agent。
- 框架没有命名，论文也未报告环境、prompt 或任务规格的任何公开发布。
- 作者指出，真值实现「已知只有 EDE 模型是公开的」，这限制了 TQ 那一组比较的外部可复现性。
- 作者指出，agent 生成的假设「本质上是唯象的，与暗能量的物理场性质无关」，并表示未来工作会加入避免唯象参数化的机制。
- Repository note: 这是一篇 5 页的 workshop 论文；若干协议细节（逐任务预算、prompt 全文、里程碑的完整定义）要么放在附录，要么根本没有报告。

## Related Works

- [ReplicationBench](./replicationbench.md) — 同样评估 agent 从论文复现天体物理研究结果，真值由原作者共同开发。
- [CosmoPaperQA](./cosmopaperqa.md) — 同样面向宇宙学，但评估的是检索增强问答，而非修改代码库。
- [FEABench](./feabench.md) — 同样要求 agent 驾驭一个大型科学仿真代码库，并以与参考输出的数值一致性计分。
- [Gravity-Bench-v1](./gravity-bench.md) — 同样评估对非标准物理的发现能力，而不是对教科书结论的记诵。
