# ChemEBench (2025)

> [English](../../works/chemebench.md) | **简体中文**

## Overview

ChemEBench 是一个化学工程评测 benchmark，随 ChemELLM 一同提出——后者是大连化学物理研究所与科大讯飞基于 Spark-70B 构建的 700 亿参数领域专用语言模型。评测分三个递进层级，覆盖 15 个维度、101 项不同的化学工程任务，从基础领域知识一直延伸到设备选型、分离、传热、过程安全与过程经济等专业工程技能。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://doi.org/10.1016/S1872-2067(25)64725-5>
- **Venue:** Chinese Journal of Catalysis, vol. 73 (2025), pp. 159–173

## Summary

论文题为「From lab to fab: A large language model for chemical engineering」，给出三件相互耦合的成果：ChemEData，一份精选的化学工程语料，含 190 亿预训练 token 与 10 亿微调 token；ChemELLM，在该语料上对 Spark-70B 做领域自适应预训练与监督微调得到的 70B 模型；以及 ChemEBench，作者称之为首个面向化学工程的多维 benchmark。ChemEBench 用来把 ChemELLM 与十四个主流商业及开源权重模型放在同一套分层级的任务集上对比，层级自化学工程的事实性知识逐级上升到应用型专业技能。该 benchmark 的定位是能力测量——作者认为通用模型在这门学科上流于浅表——而非 agentic 或工具使用评测。

## Tasks

ChemEBench 由三个递进层级构成，在 101 项不同的化学任务上评估 LLM 的 15 个能力维度。

- **L1 — 基础知识：** 围绕化学工程基本概念的客观题（选择、填空、判断）与主观题（简答、计算）。
- **L2 — 进阶知识：** SMILES 到 IUPAC 命名的转换、由文字描述生成分子名称、分子性质预测，以及反应预测（反应物/产物、是否高产率）。
- **L3 — 专业技能：** 应用型工程任务，涵盖催化剂（失活、稳定性、工业过程）、设备（反应器、干燥器、离心机、泵、塔器）、流体仿真（CFD、离散元方法、机器学习、DNS）、分离（吸收、精馏、萃取）、换热器、安全（过程、环境、人员、设备、法规、危险化学品）、经济，以及工程建设（电气、自控、材料、设备、土建、热工、给排水、总图、化工系统、消防）。

15 个维度分别是：催化剂、设备、仿真、分离、传热、安全、经济、电气工程、自动控制、材料工程、设备工程、土建工程、热工工程、给排水工程与消防工程。

TODO(reference) — 论文未说明 benchmark 的总题量、各层级的题目数，也未说明题目的来源与专家校验流程。

## Domains

化学工程是主领域：L1 与 L3 层考的是化学工程知识与应用型过程工程技能——反应与分离设备、精馏/吸收/萃取、换热器、过程与工厂安全、过程经济、流体仿真方法，以及工厂工程建设的各个专业（电气、自控、土建、热工、给排水、消防）。化学则借由 L2 层成为真正意义上的共同领域：该层的任务是分子命名转换、分子性质预测与反应预测，目标并非过程工程。

## Evaluation

评分随题型而定。客观题型——选择、填空、判断——按准确率计分。主观题型——简答与计算——按分数量表评判，判分标准要求答案完整清晰、不遗漏关键信息，并要求逐步核查推理链是否存在事实、逻辑、计算或知识性错误，每项按 0–5 分评定。

共评测十四个模型：ChemELLM、DeepSeek-R1、DeepSeek-V3、O1-Preview、O3-mini、GPT-4o、Claude-3.7、ERNIE-4.0、GLM-4、Kimi、LLaMA 3.1-70B、ChemDFM-13B、ChemLLM-7B-Char-1.5-SFT 与 LlaSMol-Mistral-7B。报告的平均分中 ChemELLM 以 72.90 居首，其次是 DeepSeek-R1 的 70.33 与 O1-Preview 的 65.76；化学专用小模型垫底（ChemDFM-13B 31.22、ChemLLM-7B-Char-1.5-SFT 20.67、LlaSMol-Mistral-7B 19.81）。

## Typical Duration

N/A — ChemEBench 是单次作答的静态问答 benchmark；论文未报告单任务的轨迹长度、wall-clock 时间或 token 预算。

## Main Contribution

按作者的表述，论文贡献了三样成果：ChemELLM，一个面向化学工程的 700 亿参数专用 LLM；ChemEData，一份专门构建的领域语料，含 190 亿预训练 token 与 10 亿微调 token；以及 ChemEBench，被呈现为首个面向化学工程的多维 benchmark，跨三个递进能力层级，覆盖 15 个维度与 101 项核心任务。

## Key Design Ideas

- 三级递进结构——基础知识、进阶知识、专业技能——把领域记忆、化学预测与应用型工程判断分开测量，而不是混成一个总分。
- 覆盖工厂工程建设的各个专业，包括电气、自动控制、土建、热工、给排水与消防工程，这些在偏化学的 LLM benchmark 中很少出现。
- 同一层级内混用题型：按准确率计分的客观题与按分数量表评判的计算题、简答题并存，使数值型过程计算不至于被简化成选择题。
- 主观题采用细则评分，逐步为推理链打分（0–5），而不只看最终答案。
- 基线阵容刻意混合通用推理模型、商业 API 与化学专用开源权重模型，从而把「化学专精」与「化工胜任力」之间的落差单独凸显出来。

## Strengths

- 把化学工程当作一门独立学科来覆盖，而非化学的延伸：L3 设有设备、分离、传热、安全、经济与工程建设等维度。
- 层级结构把知识记忆与应用型专业技能区分开，能力短板因此清晰可辨，不会被平均掉。
- 评测了十四个模型，其中含四个化学专用模型，使对比能够区分分子化学专精与过程工程胜任力。
- 建立在有据可查的领域语料之上（预训练用了 106 万篇学术论文、579 万件化学专利与 1,200 部专业书籍），学科覆盖因此扎根于产业文献。

## Limitations

- benchmark 的构建流程未见报告：论文给出了维度数与任务数，却没有总题量、各层级的分布、题目的来源，也未说明题目是否经过化学工程专家校验。
- 题型是静态问答，不含工具使用、仿真器执行或多步 agent 轨迹，因此「专业技能」是靠书面作答来衡量，而非靠实际完成的工程工作。流体仿真与设备两个维度考的是关于这些主题的问题，而不是真的跑一次仿真。
- 主观题与计算题的判分细则只有定性描述（完整性/清晰度与推理链正确性各 0–5 分），论文也未说明判分由谁执行，评分者究竟是人类专家还是模型 judge，并不明确。
- Repository note: 该 benchmark 出自一篇以「作者自家模型 ChemELLM 登顶排行榜」为核心主张的论文，且 benchmark 与该模型的训练管线共享作者团队与 ChemEData 源语料，因此所报告的排名并非独立测量。
- Repository note: ChemEBench 似乎并未公开发布。论文给出的是 ChemELLM 的公开对话部署地址（`https://chemindustry.iflytek.com/chat`），而非 benchmark 数据；查证时，该项目所引的 GitHub 仓库（`DICPZhou/ChemELLM`）里只有一份许可证和一行 README，既无测试数据，也无评测框架。
- Repository note: L2 层与既有的分子化学 benchmark 大量重叠（命名转换、性质预测、反应预测），因此层级结构中约三分之一并不属于化学工程评测。

## Related Works

- [CeProBench](./ceprobench.md) — 同为化工过程开发 benchmark，但通过实际执行的 PFD 与 Aspen Plus 任务来考察同一学科，而非书面作答。
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — 把化学工程评估收窄到热力学计算，与 ChemEBench L1 的计算题可比。
- [ChemEval](./chemeval.md) — 同样的多层级、多维度、多任务 benchmark 形态，只是落在化学而非化学工程上。
- [ChemBench](./chembench.md) — 大规模精选化学题集，带人类专家基线，是 ChemEBench L2 层在化学一侧的对应物。
- [ERI Benchmark](./eri-benchmark.md) — 跨工程学科的指令 benchmark，化学工程是其九个领域之一。
