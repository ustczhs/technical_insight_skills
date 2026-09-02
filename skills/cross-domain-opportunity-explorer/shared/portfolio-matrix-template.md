# PORTFOLIO_MATRIX

## 评分原则

分数仅用于**相对排序**，附证据与置信度；不是 TAM 预测。Pain 与 Itch **分开评估**；`基础可行性 = block` 不得 shortlist。

## 矩阵

| concept_slug | spark_id | People Cell | 机会类型 | 刚需价值 | 痒点/传播价值 | 基础可行性 | 四杀伤齐 | 证据置信度 | 决定 | 下一步 |
|--------------|----------|-------------|----------|----------|---------------|------------|----------|------------|------|--------|
| | | | Pain / Itch / 混合 | low / med / high | low / med / high | pass / caution / block | yes / no | low / med / high | backlog / candidate / shortlist / defer / killed | |

## 解释维度

| 维度 | 依据 |
|------|------|
| 刚需价值 | 频率、损失/安全、替代不足、支付、留存、硬件必要性 |
| 痒点/传播价值 | 身份、审美、仪式、成就、分享、社群、装备文化 |
| 基础可行性 | 信号可靠性、AI 可解释性、成本/售后、隐私、法规、失效后果 |
| 四杀伤齐 | 四项均可证伪且非空话 |
| 证据置信度 | 来源质量、地域适配、行为/付费是否一致 |

## Shortlist 闸门（≤3 条）

须同时满足：

- [ ] 来自 Spark Board 晋升，溯源清晰
- [ ] People Cell 与场景具体
- [ ] **四杀伤齐**
- [ ] **≥2 条可复核 fact 或 voice**（优先 ≤12 个月；无则不得 shortlist）
- [ ] 三种介入形态已比较
- [ ] 红队：手机不能充分替代（或明确为何仍选硬件）
- [ ] 无未处理 medical-boundary / block
- [ ] 有最危险假设与验证路径

## 与 Spark Board 同步

- `killed` 条目回写 Spark Board
- `shortlist` 条目触发 Handoff Pack + VALIDATION_BRIEF
