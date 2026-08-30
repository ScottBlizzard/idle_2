# 内生失败条件化 v2.1 交叉纠错 Pilot 结果报告

## 结论先行

冻结自动门返回 **`KILL_NO_SELECTION_REVERSAL`**。本轮 3,840 单元交叉纠错矩阵完整结束，但预注册要求的能力排序反转没有出现，因此不授权 complementarity router、跨供应商扩展或围绕当前种子的论文升级。

实验同时观察到方向一致、置信区间排除零的 Qwen2.5×Qwen3 lineage 交互。这说明“哪个 lineage 更擅长修复错误”确实依赖于“错误由哪个 lineage 产生”。然而，这个信号不能事后替代未通过的主门槛；此外，MATH-500 的输出质量受到严重 token 截断，不能作为干净的跨任务复制证据。

## 完整性与可复现性

- 冻结错误库包含 480 个唯一错误，覆盖 60 个 GSM8K 问题和 60 个 MATH-500 问题。
- 四个精确模型版本各生成 960 个纠错结果，总计 3,840 个唯一 `case_id`，无缺失、无重复。
- 四个输出文件的本地 SHA-256 与各自 manifest 完全一致。
- `scored_matrix.jsonl` 的 SHA-256 为 `39b921b734b55864a0a53468740837784d38b0b17c49de505cee3cdd9b44b7e1`，与 `FINAL_GATE.json` 一致。
- 冻结配置 SHA-256 为 `c3ce5803da434b9d3a6436e06c57814b51f997d27975c65bdd79aa35a9e8103a`；错误库 SHA-256 为 `ae0fcf6d04ed7c3374fa37bb5d1a7874d8eefddbca77056598bd79c95a26e57b`。
- 运行使用 greedy deterministic decoding；共享 GPU 只影响墙钟时间，不是本实验的科学指标。

四个 corrector 的墙钟时间分别为：Qwen2.5-3B 5,678 秒、Qwen2.5-7B 6,238 秒、Qwen3-4B 7,269 秒、Qwen3-8B 9,101 秒。

## 主门槛：没有出现选择排序反转

预注册的反转要求同时满足：对角线上的大模型减小模型效应与标准化后的效应异号，并且二者差至少 5 个百分点。本轮四个 domain×lineage 组合均未通过：

| 数据集 | lineage | 对角线大减小 | 标准化大减小 | 标准化位移 |
|---|---:|---:|---:|---:|
| GSM8K | Qwen2.5 | +5.00 pp | +11.25 pp | +6.25 pp |
| GSM8K | Qwen3 | −11.67 pp | −2.08 pp | +9.58 pp |
| MATH-500 | Qwen2.5 | +3.33 pp | +5.83 pp | +2.50 pp |
| MATH-500 | Qwen3 | +1.67 pp | −1.67 pp | −3.33 pp |

MATH-500/Qwen3 虽然形式上异号，但位移只有 3.33 pp，低于冻结的 5 pp 门槛。因而主张“own-failure selection 会反转模型能力排序”没有获得预注册支持。

## 次级信号：存在强跨-lineage 互补

冻结 family-interaction 统计量在两个数据集、两个 wrapper 下均为负，且 95% 聚类 bootstrap 区间均排除零：

| 数据集 | wrapper | 交互点估计 | 95% CI |
|---|---|---:|---:|
| GSM8K | external neutral | −29.17 pp | [−40.42, −17.92] pp |
| GSM8K | assistant history | −25.42 pp | [−35.42, −16.25] pp |
| MATH-500 | external neutral | −12.50 pp | [−22.08, −4.17] pp |
| MATH-500 | assistant history | −17.08 pp | [−25.83, −9.17] pp |

负号表示交叉 lineage 纠错相对于同 lineage 纠错更有优势：Qwen3 更容易修复 Qwen2.5 产生的错误，而 Qwen2.5 相对更容易修复 Qwen3 产生的错误。GSM8K 上该现象尤其强，并且两个 wrapper 方向一致。

该结果是一个真实的诊断线索，但还不是 Oral 级贡献。原因有三点：它来自同一供应商内部 lineage；冻结的能力排序反转没有出现；当前矩阵没有完成等预算 router 对强单模型和 oracle 上界的比较。

## 输出质量门：MATH-500 严重截断

全矩阵的解析失败或截断率为 **27.55%**，远高于冻结上限 2%。拆分后可见问题几乎全部来自达到 768-token 上限：

| 数据集 | bad/total | bad rate |
|---|---:|---:|
| GSM8K | 46/1,920 | 2.40% |
| MATH-500 | 1,012/1,920 | 52.71% |

总计 1,058 个样本达到 token 上限，其中 987 个没有抽取到可验证答案。MATH-500 的 768-token 预算明显不足；Qwen3-8B 在 MATH-500 上的 bad rate 达 66.04%。因此 MATH-500 的交互效应不能被当作干净复制。即使主反转门槛通过，这一质量门也会阻止升级。

## 约束性解释

本轮不是“什么都没发现”。它排除了原种子的关键版本：在共同错误库上标准化错误难度，并没有产生预注册幅度的模型大小排序反转。与此同时，数据支持一个更窄的现象——错误具有 lineage 条件化的可修复性，跨 lineage 修复可能优于同 lineage 修复。

但是不能使用事后延长 token、删除 MATH-500 截断样本、替换模型或重新定义反转来救当前种子。这些操作会把冻结 falsifier 变成结果导向调参。若未来重新研究跨-lineage 互补，必须作为新问题重新进行文献对抗、预注册独立输出预算和跨供应商复制，并首先证明它超越普通 ensemble diversity、self-correction 和 verifier routing。

## 绑定决定

1. 当前 endogenous-failure-conditioning 种子关闭，决定为 `KILL_NO_SELECTION_REVERSAL`。
2. 不进入 complementarity-router 测试，不自动扩大模型或数据集。
3. 强 lineage interaction 只保留为新种子搜索的异常来源，不作为当前论文的正结果。
4. 项目重新回到 `NO_ACTIVE_SEED`；下一步应寻找能够解释跨-lineage 修复不对称、并产生新可检验后果的独立机制，而不是继续扩充当前矩阵。

## 证据文件

- 自动 gate：[`results/pilot_v2_1_qwen_lineages/results/FINAL_GATE.json`](results/pilot_v2_1_qwen_lineages/results/FINAL_GATE.json)
- 完整评分矩阵：[`results/pilot_v2_1_qwen_lineages/results/scored_matrix.jsonl`](results/pilot_v2_1_qwen_lineages/results/scored_matrix.jsonl)
- 64 个条件单元率：[`results/pilot_v2_1_qwen_lineages/results/cell_rates.csv`](results/pilot_v2_1_qwen_lineages/results/cell_rates.csv)
- 冻结协议修订：[`PILOT_PROTOCOL_AMENDMENT_V2.md`](PILOT_PROTOCOL_AMENDMENT_V2.md)
- 资源共享工程修订：[`RESOURCE_SHARING_AMENDMENT.md`](RESOURCE_SHARING_AMENDMENT.md)
