# Clarified Requirement Template

建议路径：`$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/CLARIFIED_REQUIREMENT.md`  
复制下方全文作为起点。**纯 Markdown**：文首元信息表；不要 YAML front matter。

# Clarified Requirement: \<短标题\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| clarification_status | draft |
| title | |
| project_slug | |
| req_slug | |
| requirement_seed | 〈原始模糊输入摘要〉 |
| corpus_relation | New / Extends / Conflicts / Already-covered / Unknown |
| confidence | high / mid / low |
| created | YYYY-MM-DD |
| updated | YYYY-MM-DD |

`clarification_status`：`draft` \| `ready`  
仅当 `ready` 时可定稿同目录 `VALUE_VERDICT.md`。  
**Ready 前置**：Delivery Sketch 四维均已用户确认（答案可为「待定」）。

## 1. Project Corpus

| 路径 | 类型 | 纳入 | 备注 |
|------|------|------|------|
| | id card / 功能清单 / 其他 | 是 / 否 | |

无 Corpus 时写明「空 / 降级」，并将 `corpus_relation` 倾向 `Unknown`、`confidence` 倾向 `low`。

## 2. Requirement Seed（原文或摘要）

\<保留用户原始表述，便于追溯\>

## 3. Clarification Dimensions

| 维 | 结论 | Corpus 对照 | 来源 |
|----|------|-------------|------|
| 要解决的问题 | | | Corpus / Web / 用户 |
| 对象用户 | | | |
| 关键场景 | | | |
| 成功判据 | | | |
| 非目标 | | | |
| 约束 | | | |
| 依赖与风险 | | | |
| 技术路线 | | | |
| 触及面 | | | |
| 人力量级 | | | |
| 工期量级 | | | |

## 4. Delivery Sketch（交付草图）

| 字段 | 值 |
|------|-----|
| tech_route | |
| integration_surface | |
| effort_band | ≤0.5人 / 1–2人 / 3–5人 / >5人 / 待定 / 自定义 |
| duration_band | ≤1周 / 1–2周 / 2–4周 / 1–2月 / 约一季度 / >一季度 / 待定 / 自定义 |

量级档禁止伪装成精确排期。任一项「待定」时，元信息 `confidence` 不得为 `high`。

## 5. 边界陈述（定稿摘要）

\<一段话：做什么、为谁、在何场景、成功长什么样、明确不做什么；可一句带过交付草图量级\>

## 6. 待决 / 已解消冲突

| 项 | 状态 | 说明 |
|----|------|------|
| | open / resolved | Conflicts 或 Already-covered 的处理 |

## 7. Web References（可选）

| 要点 | URL | 用户是否确认升格 |
|------|-----|------------------|
| | | 是 / 否（仅参考） |
