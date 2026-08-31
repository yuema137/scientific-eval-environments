# Model Discovery Agent (2026)

> [English](../../works/model-discovery-agent.md) | **简体中文**

> **首次公开：** 2026-08-10 · **来源：** [arXiv 初次提交](https://arxiv.org/abs/2608.09696v1)

## 概览

Model Discovery Agent（MDA）测的不是“拿到一份现成数据以后能不能拟合出一个模型”。Agent 得自己决定下一步做什么实验，用 Bayesian posterior 维护多种 mechanistic model；要是现有候选都解释不了新证据，还得让 LLM 提出新的假设。论文把 held-out prediction error 和 mechanism recovery 画成随实验次数变化的 learning curve，直接看 agent 用多少数据才能把规律摸准。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## 链接

- **论文：** <https://arxiv.org/abs/2608.09696>
- **Benchmark 代码（NeuronBench）：** <https://github.com/murphyk/neuronbench>
- **发表信息：** arXiv 预印本（cs.AI），2026

## 摘要

每轮实验里，MDA 用三层 sequential Monte Carlo 更新对模型结构、参数，以及必要时 latent state 的 posterior。Value of Information 负责挑下一次 intervention；posterior predictive check 一旦发现手头的候选模型解释不通，LLM 就补充新的可执行模型结构，再由 Bayesian evidence 淘汰不合适的候选。每做完一次实验，系统都会在 agent 没跑过的 intervention 上重新评分，所以这里真正比较的是“谁更快学明白”，不是给无限数据以后谁最后能做出来。

## 任务

实验覆盖四组 interactive model-discovery 任务：ChemBench/ActiveSciBench-Chem 的 36 项子集，包含 12 类 enzyme-kinetic mechanism 和三个难度；由 DiscoverPhysics 封装来的六个双粒子 ForceBench world；七个 BoxingGym probabilistic-programming domain；以及新设计的六个 NeuronBench mystery neuron，每个神经元都有 deterministic Hodgkin–Huxley 和带有限 channel noise 的 stochastic 版本。Agent 要选择实验条件、观察模拟结果、更新模型，再预测自己没做过的 intervention 会得到什么结果。

## 领域

物理学（反事实 force law）、化学（enzyme kinetics）、神经科学（ion-channel mechanism 与 electrophysiology），以及 BoxingGym 覆盖的通用 probabilistic model discovery。

## 评估

- **逐次实验 learning curve。** 每次 intervention 以后，都把当前 Bayes predictor 放到与已做实验分离的 held-out query distribution 上评分。连续目标主要用 normalized MSE，化学 reaction rate 用与 RMSLE 对齐的误差，二元目标用 Brier score。
- **Mechanism recovery。** ChemBench 用 SymPy 检查数学等价；ForceBench 通过 held-out trajectory 检验提交的 force law；NeuronBench 记录发现的 channel class 是否等于隐藏机制。
- **受控比较。** MDA 会和原 benchmark 的 agent、model-free in-context forecaster、适用时的 random experimental design，以及去掉 M-open hypothesis expansion 的 ablation 比较。
- **论文报告。** 所有 LLM 方法固定使用 Opus 4.7 时，MDA 在 ChemBench、ForceBench 和 BoxingGym 上都比原 baseline 用更少实验达到更低的 held-out error。NeuronBench 的 deterministic world 里，两种 information-directed policy 在每个 world 上都胜过 random design；到了 stochastic setting，task-directed Value of Information 略胜 Expected Information Gain。

## 典型时长

每个 episode 用实验预算限制，而不是用论文给出的 wall-clock 上限：主要实验在 ChemBench 最多跑 60 次 designed experiment，ForceBench 8 次，BoxingGym 10 次；NeuronBench 先给两次固定 passive observation，再允许最多 5 次新实验。完整 stochastic NeuronBench 很吃算力，因为每一轮都要在 parameter inference 和 model inference 里面再套 particle filtering。

## 主要贡献

它给出了一套跨领域、以 data efficiency 为中心的 LLM-assisted Bayesian model discovery 评估，并实现了一个能扩展 hypothesis space 的 M-open SMC³ agent；同时新增 stochastic electrophysiology benchmark，专门测试有 latent process noise 时还能不能发现机制。

## 关键设计

- 把 model structure、parameter 和 latent dynamics 三层 uncertainty 分开推断，不让 LLM 靠一段文字硬记所有 belief。
- 只有 posterior predictive check 发现现有 hypothesis pool 不够用时，才让 LLM 提新模型；旧模型和新模型最后都交给 marginal likelihood 筛选。
- Expected Information Gain 和 task-directed Value of Information 把“下一个实验做啥”变成明确的 decision rule，也就能直接测它的数据效率。
- Held-out intervention 和 agent 自己选过的实验互不重叠，防止“训练数据拟合得挺像”冒充真正能预测新情况的 world model。
- NeuronBench 让 novel ion-channel mechanism 在普通 textbook stimulation 下看着没啥异常，逼 agent 用有区分力的 stimulation protocol 把它试出来；deterministic 和 stochastic 情况都测。

## 优点

- 化学、物理、probabilistic modeling 和 electrophysiology 共用一套 agent–environment protocol，原本很不一样的任务可以放在同一种 experiment-efficiency curve 下比较。
- Prediction 和 structural recovery 分开检查，能抓出那种局部数字拟合得不错、mechanism 却压根不对的表达式。
- no-M-open ablation，以及 random / EIG / task-directed design 的对照，能看出提升究竟来自哪一块。

## 局限

- 作者明确指出，hypothesis proposal 是一个瓶颈：LLM 要是从来没提出包含真相的 model family，后面的 Bayesian selection 再严谨也选不出来。
- Full-batch nested SMC 的计算量随实验预算 `B` 和存活模型数 `N_m` 按 `O(B²N_m)` 增长，这直接限制了 stochastic benchmark 能跑多长。
- 仓库说明：四组评估用的都是 simulator 或 probabilistic program，不是实际实验室；所以这里测出的 data efficiency 还不能直接证明它能省下真实仪器、样品或人工成本。
- 仓库说明：实验只用了 Opus 4.7。论文把 inference 和 design machinery 的作用拆得比较清楚，但没有证明换一批 LLM family 以后也一样。

## 相关工作

- [DiscoverPhysics](./discoverphysics.md) — ForceBench 的 counterfactual force-law 环境来自这里；MDA 在上面增加 Bayesian model selection 和 experiment-efficiency evaluation。
- [MaD Physics](./mad-physics.md) — 同样测有限 measurement budget 下的 law discovery，但它给不同 fidelity 的 observation 定价，MDA 则在固定 action space 上优化 Value of Information。
- [NewtonBench](./newtonbench.md) — 同样让 agent 互动实验并恢复 counterfactually shifted law，任务规模更大，最后提交 symbolic expression。
- [Gravity-Bench-v1](./gravity-bench.md) — 同样把 observation planning 放进 simulated physics discovery，并量出数据受限带来的性能损失。
