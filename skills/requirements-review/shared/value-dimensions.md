# Value Dimensions（v1）

仅在 `clarification_status = ready` 之后进入。每维给出**推荐档位** + 一句话理由；可用一题确认六维档位，再**单独成题**确认 Do / Defer / Don't。面向用户的确认一律用**选择题**（见 [grill-output.md](grill-output.md)；最后一项为自定义）。

**不做**加权总分或伪精确公式。

| id | 维 | 高档大致意味 | 低档大致意味 |
|----|----|--------------|--------------|
| user_value | 用户价值 | 痛点真实、场景高频或高影响 | 锦上添花、用户含糊 |
| strategy_fit | 战略契合 | 贴合产品定位 / id card 方向 | 偏离主航道 |
| corpus_delta | 相对 Corpus 增量 | 明显 New 或高价值 Extends | Already-covered / 增量很薄 |
| cost_complexity | 成本与复杂度 | 相对价值投入可控 | 牵动面大、成本高且收益不清 |
| risk | 风险 | 假设少、可回滚或可试点 | 依赖多、合规/技术不确定性高 |
| timing | 时机 | 现在做有窗口或解锁后续 | 可等、前置未就绪 |

## 消费 Delivery Sketch（强制）

Value Verdict **必须**包含「交付草图（引自澄清）」节，原文或摘要引用澄清稿中的：

`tech_route` · `integration_surface` · `effort_band` · `duration_band`

并且：

- `cost_complexity` / `risk` / `timing` 的档位与一句话理由须**点名引用** Sketch（路线、触及面、人力档、工期档中至少相关项）
- Do / Defer / Don't 的推荐理由也须带上 Sketch，禁止纯价值空转
- **不**因人力/工期档偏高而设硬闸禁止 Do（那是权衡，不是 Conflicts）

### 待定规则

Delivery Sketch 任一项为「待定」时：

- `confidence` **不得**为 `high`
- 若仍推荐 **Do**：须**单独成题**请用户确认「在路线/触及面/人力/工期仍待定的前提下接受 Do」；未接受则默认偏 **Defer**

## 档位（定性）

每维使用三档之一（可在产物中写中文）：

| 档 | 含义 |
|----|------|
| high | 明显支撑 Do |
| mid | 中性或有条件 |
| low | 明显支撑 Defer/Don't |

`cost_complexity` 与 `risk`：**low 档 = 更有利**（成本低/风险低）；写理由时说清楚方向，避免「low」歧义——产物中建议写「低 / 中 / 高」并注明「成本低=有利」。

## 综合结论规则

| 结论 | 何时推荐 |
|------|----------|
| **Do** | 澄清 Ready；Conflicts / Already-covered 已解消；用户价值与增量不明显偏低；用户接受主要风险；若 Sketch 有待定则已通过显式接受题 |
| **Defer** | 有价值但时机/前置/置信度不足；或 Corpus Unknown 且用户未接受无文档对齐风险；或 Sketch 待定且用户未接受带待定的 Do |
| **Don't** | 增量不足、战略偏离、或 Conflicts/Already-covered 且用户选择不做 |

薄 Corpus / 大量 Unknown → 结论须标 **confidence: low**，默认更偏 **Defer**，除非用户显式接受风险。
