# SCR-Bench (2026)

> [English](../../works/scr-bench.md) | **简体中文**

## Overview

SCR-Bench 是面向 Skill Composition Risk（skill 组合风险）的沙箱化 benchmark：它沿组合 skill 的*激活路径*为 agent 行为打分，而不是孤立地评估单个 skill，并且记录下游的状态变化而非文字表述的意图。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 面向组合式 skill 执行的通用型 agent 安全探测；未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.15242>
- **Code:** <https://github.com/saint-viperx/SCR_Bench>
- **Venue:** arXiv preprint (cs.CR), 2026

## Summary

skill 是 LLM agent 把计划落成动作的能力层，但审核通常只单独评估每个 skill，而真实任务却会在同一个执行上下文中调用多个 skill。论文把由此产生的缺口命名为 Skill Composition Risk——单看无害的 skill，一旦其输出、信任信号、授权线索或副作用沿激活路径影响到后续调用，就会变得有害——并构建 SCR-Bench 来测量它。三个子 benchmark 分别隔离三种组合机制，每一个都以沙箱中可观测的下游事件计分，而不看 agent 声称自己要做什么。

## Tasks

三个子 benchmark，均运行在受控的沙箱化 skill 环境中：

- **SCR-CapFlow**（能力流组合）— 150 个案例，覆盖权限与访问控制、模拟上报、设备控制、网络配置与持久化调度，在 mock 的文件、服务、日志、计划任务与状态上运行。
- **SCR-TrustLift**（信任传递组合）— 在模拟的 skill 市场安装环境中，每个 backend 401 次安装试验。
- **SCR-AuthBlur**（授权混淆组合）— 118 个保留案例，覆盖安全、隐私、财务、人力资源、供应链与运营安全类决策，在模拟的审批与政策上下文下运行。

## Domains

面向通用型 LLM agent 的 agent skill 生态；被触发的后果落在系统运维、访问控制、设备与网络配置以及组织审批流程上。不分配任何规范的科学或工程领域。

## Evaluation

- **路径级结果。** 只有当沙箱中出现可观测的下游事件——激活路径上的一次状态变化——才判为成功，而不凭对意图的文字描述或对表层行为的分类。
- **攻击成功率（ASR）**，在案例与试验上取平均，以有害状态是否发生来定义。
- **AuthBlur 的上下文层级：** L0 为无关的对照上下文，L1 为相关的任务上下文，L3 为类授权的建议性上下文；风险性批准率指不安全请求被批准的案例占比。
- **报告。** 在 SCR-CapFlow 中，组合条件下 ASR 达到 33.6%，而孤立基线接近零。在 SCR-TrustLift 中，五个 backend 里有四个 ASR 超过 96.5%，对照条件下的 ASR 则接近 0%。在 SCR-AuthBlur 中，L1 设定下的风险性批准率相对 L0 孤立基线上升 71.8%，报告的平均值为 L0 15.7%、L1 27.0%、L3 34.0%。CapFlow 各条件下共评估九个 backend——GPT-5.5、GPT-5.4、Claude Opus 4.6、Claude Opus 4.5、Gemini 3.1 Pro Preview、MiniMax-M2.7、DeepSeek-V4、GLM-5.1 与 GLM-5——TrustLift 用五个 backend，AuthBlur 用十个。

## Typical Duration

TODO(reference) — 论文报告了逐案例与逐试验的结果率，却未给出轨迹长度、wall-clock 时间或 token 预算。

## Main Contribution

把 Skill Composition Risk 确立为一个独立的评估对象，并给出第一个在激活路径层面测量它的 benchmark，表明组合条件下才显现的风险，在市场目前所做的孤立式逐 skill 审核中基本看不到。

## Key Design Ideas

- 三种组合机制——能力流、信任传递、授权混淆——各自拥有一个子 benchmark，而非被揉进单一的聚合风险分数。
- 每个子 benchmark 都配有匹配的孤立或对照条件，因此所报告的效应可归因于组合本身，而非 skill 本身。
- 打分以沙箱中的状态变化为准，消除了判断 agent 口头意图时的歧义。
- 上下文在 AuthBlur 中是可操纵变量（L0/L1/L3），从而量化仅凭周边任务上下文就能让审批纪律退化多少。

## Strengths

- 孤立与组合的对照被写进了设计本身，使论文的核心主张可直接测量。
- backbone 覆盖异常之广（视子 benchmark 不同，涵盖九到十个前沿与开放权重模型）。
- benchmark 已公开发布。

## Limitations

- 所有环境均为模拟或 mock；没有任何结果取自真实的 skill 市场或线上系统。
- 论文未说明各子 benchmark 究竟包含多少个不同的 skill，留作 TODO(reference)。
- backend 覆盖在三个子 benchmark 之间并不一致（九、五、十），因此跨子 benchmark 的模型比较并非同口径。
- Repository note: 受构造方式所限，被触发的只有成对或较短的激活路径；组合空间呈组合式增长，benchmark 并未声称覆盖它。

## Related Works

- [SLBench](./slbench.md) — 同样以可执行检查测试 skill 诱发的不安全 agent 行为，但针对单个 skill 内部的关系而非跨 skill 的组合。
- [HarmfulSkillBench](./harmfulskillbench.md) — 同样在安装了 skill 的条件下评估 agent 安全性，只是那里的 skill 本身意图即有害，而非孤立看来无害。
- [SkillAudit](./skillaudit.md) — 同样在隔离沙箱中运行 skill 做安全验证，但一次只审计一个包。
- [Skill-Use](./skill-use.md) — 同样测量 agent 是否守住 skill 的边界，但按 skill 而非按激活路径。
