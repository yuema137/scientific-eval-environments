# Spec-o3 (2026)

> [English](../../works/spec-o3.md) | **简体中文**

## Overview

Spec-o3 是一个带工具的视觉语言 agent，通过自动化的光谱检视来核验稀有天体候选体。除 agent 之外，论文还给出 SpecVI-Bench：一个基于 LAMOST 光谱、包含五项稀有天体识别任务的标准化 benchmark，测试集刻意保持类别不均衡，并配有外部 baseline、跨巡天泛化划分，以及一份公开的专家评分量表，用于给 agent 的推理轨迹打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.06498>
- **Code:** <https://github.com/Maxwell-Jia/spec-o3>
- **Venue:** ACL 2026 Main Conference

## Summary

在光谱巡天中，稀有天体候选体的最终核验至今仍依赖专家目视检查，而这一环节无法随巡天数据量同步扩展。Spec-o3 把这套流程复刻成交错式的多模态思维链：agent 一边围绕光谱推理，一边调用可视化工具重绘任意波段区间，然后才给出结论。它由两阶段的后训练配方产出——先在专家检视轨迹上做冷启动监督微调，再在稀有类型核验上做基于结果的强化学习。作为评估产物的 SpecVI-Bench 定义了五项稀有天体任务，测试集保持真实的稀有比例，对照对象包括专用深度模型以及闭源和开源 VLM，另设一个从 LAMOST 到 SDSS/DESI 的留出巡天迁移划分，并请六位天文学家按五级量表为推理轨迹打分。

## Tasks

SpecVI-Bench 含五项稀有天体识别任务，每类一项：激变变星（CV）、碳星（CS）、S 型星（SS）、M 型巨星（MG）与白矮星（WD）。正样本取自 LAMOST 官方星表。负样本用拒绝采样从 LAMOST 全档案中挖掘，只保留预测正类概率超过 0.8 的光谱——接受率为 1.74%——以保证负样本确实容易混淆，而不是轻易就能分开。总体规模上，训练集为 1,681 正 / 1,683 负，测试集为 1,122 正 / 5,632 负；以 CV 任务为例，训练 343 / 368，测试 229 / 1,229。测试集刻意保持不均衡，以反映真实场景中目标天体的稀有程度。跨巡天划分则单独与 SDSS/DESI 交叉证认，每项任务约 50 个正样本与 250 个负样本，仅覆盖 CV、CS 与 MG——SS 与 WD 的交叉证认样本不足。

## Domains

天文学：受评目标是从巡天光谱中对稀有天体做光谱分类——激变变星、碳星、S 型星、M 型巨星与白矮星——使用 LAMOST 星表与档案数据，并在 SDSS 与 DESI 上检验泛化。次要共属领域是 AI & Machine Learning Research，因为 agent 部分的贡献是一套视觉语言后训练配方。

## Evaluation

- **主要指标。** 各任务的准确率与正类 F1，再在五项任务上取宏平均；由于测试集不均衡，作者以宏平均 F1 为主指标，准确率为辅。
- **报告结果（Table 1）。** Spec-o3-7B 达到 88.7% 宏平均准确率与 76.5% 宏平均 F1，o3 为 85.5% / 52.3%，GPT-4.1 为 48.6% / 29.8%。baseline 涵盖专用深度模型（CarbonNet、AstroCLIP、GaiaNet）、闭源 VLM（GPT-4.1、o3）与开源 VLM（Qwen2.5-VL 3B 与 7B、Qwen3-VL 8B 与 30B-A3B）。
- **巡天迁移。** 同一套协议施加于 LAMOST → SDSS/DESI 交叉证认划分上的 CV、CS 与 MG，作为未见分布的测试。
- **推理轨迹评估。** 六位具备光谱学专长的天文学家按公开的 0–5 量表，就连贯性与物理自洽性为 100 条推理轨迹打分（Spec-o3-3B 与 Spec-o3-7B 各 50 条），量表从「完全幻觉」（0）到「完全正确」（5）。另有一项 Spec-o3 与 o3 的成对偏好比较，每个巡天 50 例。

## Typical Duration

RL 阶段把每条轨迹的工具调用上限设为 8 次，且训练过程中每条轨迹的平均调用次数逐步下降。推理延迟、wall-clock 时间以及 token 或美元成本均未报告。

## Main Contribution

一个带工具的视觉语言 agent，经由专家检视轨迹的冷启动 SFT 加基于结果的 RL 训练，在稀有天体核验上达到 state of the art；以及 SpecVI-Bench——支撑上述结论的标准化五任务评估，含保持稀有比例的负样本、外部 baseline、巡天迁移划分和一份专家推理轨迹量表。

## Key Design Ideas

- 交错式多模态思维链：推理步骤与工具调用交替进行，`spectral_visualization_tool` 按指定波段区间 (λmin, λmax) 重绘光谱并可加标注，模仿天文学家放大查看诊断特征的做法。
- 原始数值光谱被缓存，局部视图按需生成，因此 agent 自己掌控证据的取用，而不是被动接收一张固定图像。
- 负样本以 0.8 的分类器概率阈值做拒绝采样挖掘，使 benchmark 的困难样本正是实际部署的分类器会真正推送来人工核验的那一批。
- 测试集有意保持不均衡，并以正类 F1 作为头条指标，让分数追踪真实核验效用，而非均衡准确率带来的假象。
- 基于结果的 RL 奖励带一个明确的格式项：格式合法且预测正确得 1，预测正确但格式不合法得 1−α，格式合法但预测错误得 0，格式不合法且预测错误得 −α。
- 轨迹质量与标签准确率分开评估，通过五级量表与成对偏好研究实现。

## Strengths

- benchmark 的负样本设计正好瞄准了使人工核验代价高昂的那批易混淆样本，而不是随机抽取档案光谱。
- baseline 确为外部方法，且横跨三个族系——天文专用网络、闭源 VLM、开源权重 VLM——因此比较不局限于作者自身系统的消融。
- 留出的巡天迁移评估（LAMOST → SDSS/DESI）针对的正是实际部署最担心的失效模式。
- 推理轨迹的物理自洽性由领域专家对照公开量表实测，而非靠示例记录断言。

## Limitations

- 跨巡天泛化只覆盖五项任务中的三项；S 型星与白矮星的交叉证认样本不足。
- agent 只有光谱可视化这一件工具，因此评估未涉及星表查询、交叉证认或多仪器证据汇集。
- Repository note: 论文自身的定位是一个 agent 加一套后训练方法，SpecVI-Bench 被作为配套基础设施呈现。此处收录的依据是这个具名 benchmark——划分明确、baseline 外部、评分协议清晰、轨迹量表公开——而非训练配方，后者不在本仓库范围内。
- Repository note: benchmark 构建把 LAMOST 星表归属当作 ground truth，因此星表的不完备或误分类会直接传导到训练与测试标签中。

## Related Works

- [AstroAlertBench](./astroalertbench.md) — 同样是带专家 baseline 的天文巡天探测多模态分类，但对象是 ZTF 警报图像而非光谱，且没有训练过的 agent。
- [Stargazer](./stargazer.md) — 同样是基于真实档案观测的天文评估，但评的是迭代式物理模型拟合，而非分类判断。
- [AstroVisBench](./astrovisbench.md) — 同样是评判协议对照职业天文学家做过校验的天文 benchmark，场景在代码与可视化。
