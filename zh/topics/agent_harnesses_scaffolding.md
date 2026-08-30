# Agent Harnesses & Scaffolding

> [English](../../topics/agent_harnesses_scaffolding.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

同一个模型放进两套 agent 系统里，表现可能像两个模型。一套 harness 会先规划再改代码，每改一次就跑测试，失败后还能重试；另一套可能只发一个 prompt，跑完就停。如果只比最终分数，我们很容易把外围软件提供的能力算到 base model 头上。

这个 topic 就是把外围控制逻辑单独拿出来看。以一个 coding task 为例，repository、budget 和 evaluator 都不变，只替换 planning loop 或 verification loop。加上 test-and-repair 以后成功率提高，提升属于 model–harness configuration。这个结果仍不能证明同一组件换个 model 或 task 也一定有效。

## 定义

模型很少单独工作。Harness 会决定它什么时候先做计划、能调哪些工具、上下文留什么、失败后要不要重试，以及什么时候停止。这个 topic 要分清这些选择怎样改变测得的能力，提升究竟来自哪个组件，还有 evaluation 能不能指导 harness 继续改进。

## 为什么重要

Benchmark 看到的是整套 model–harness configuration。如果两套系统的 prompt、工具、权限、memory、verification 或 recovery 规则不同，分数差就不能全算在 base model 头上。所以受控比较要先固定任务、evaluator 和预算，再一次只改一个 harness 组件。

## 现有方法

- **受控 harness 比较。** [Harness-Bench](../works/harness-bench.md) 固定任务、sandbox、预算和 evaluator，只改变 harness。
- **工程过程纪律。** [RigorBench](../works/rigorbench.md) 将 planning、verification、recovery、abstention 与 exploration 同结果分开计分。
- **自动改进 harness。** [Evo-Bench](../works/evo-bench.md)、[HarnessOpt-Bench](../works/harnessopt-bench.md) 与 [VeRO](../works/vero.md) 给 agent evaluator access，再测修改后的 held-out lift。
- **研究 loop 中的 scaffold。** [Curation-Bench](../works/curation-bench.md) 表明，要求引用并改造既有方法的 scaffold 会改变 agent 探索的数据策略。
- **Post-training 配置。** [PostTrainBench](../works/posttrainbench.md) 在同一 GPU 时间协议下比较多种 CLI scaffold。

## 方法对比

| Work | Harness 的角色 | 固定项 | Evaluation feedback | 结果 |
|---|---|---|---|---|
| Harness-Bench | 被比较对象 | 任务、模型、预算、evaluator | 终局分数与过程分数 | Configuration-level capability |
| RigorBench | 工程纪律来源 | Foundation model 与任务 | 仪器化过程指标 | 过程与结果分离 |
| Evo-Bench | Agent 优化的 artifact | 目标任务与 evaluator | 反复 benchmark feedback | 改进后的 harness |
| HarnessOpt-Bench | 可审计的优化目标 | Held-out split 与 eval budget | 计量的 evaluator 调用 | Held-out gain |
| VeRO | 任意程序化 harness | 权限、版本和预算 | 标准 observation interface | Expected lift |
| Curation-Bench | 研究 scaffold | 模型、recipe、evaluator | 每轮 benchmark 结果 | 更好的数据策略 |

## 还没解决的问题

- 哪些 harness 组件真正导致提升，而不只是与提升同时出现？
- Model 与 harness 非线性交互时，应怎样分别报告贡献？
- 怎样防止自适应 harness 优化过拟合或利用 evaluator 漏洞？
- Cost、权限、可复现性和安全约束应如何限制 harness search？
- Harness 结论能否迁移到其他模型、任务和科学环境？

## 相关工作

- [Harness-Bench](../works/harness-bench.md)
- [RigorBench](../works/rigorbench.md)
- [Evo-Bench](../works/evo-bench.md)
- [HarnessOpt-Bench](../works/harnessopt-bench.md)
- [VeRO](../works/vero.md)
- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
