# Value Verdict Template

建议路径：`$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/VALUE_VERDICT.md`  
**前置**：同目录 `CLARIFIED_REQUIREMENT.md` 的 `clarification_status = ready`。  
复制下方全文作为起点。**纯 Markdown**。

# Value Verdict: \<短标题\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| verdict_status | draft |
| project_slug | |
| req_slug | |
| clarified_requirement | ./CLARIFIED_REQUIREMENT.md |
| corpus_relation | （自澄清稿同步） |
| verdict | Do / Defer / Don't |
| confidence | high / mid / low |
| created | YYYY-MM-DD |
| updated | YYYY-MM-DD |

`verdict_status`：`draft` \| `final`  
Conflicts / Already-covered **未解消**时，`verdict` 不得为 `Do`。

## 1. 一句话结论

\<Do / Defer / Don't + 为何\>

## 2. Value Dimensions

| 维 | 档位 | 理由 | 来源 |
|----|------|------|------|
| 用户价值 | 高/中/低 | | Corpus / Web / 用户 |
| 战略契合 | 高/中/低 | | |
| 相对 Corpus 增量 | 高/中/低 | | |
| 成本与复杂度 | 高/中/低（注明：低=有利） | | |
| 风险 | 高/中/低（注明：低=有利） | | |
| 时机 | 高/中/低 | | |

不做加权总分。

## 3. 闸门检查

| 检查项 | 结果 |
|--------|------|
| clarification ready | 是 / 否 |
| Conflicts 已解消 | 是 / 否 / 不适用 |
| Already-covered 已解消 | 是 / 否 / 不适用 |
| 薄 Corpus 风险已声明 | 是 / 否 / 不适用 |

## 4. 建议下一步（可选）

\<例如：补 Corpus 文档、缩范围后再评、进入设计/技术树拆解（人工自行决定，本 skill 无硬衔接）\>

## 5. Web References（可选）

| 要点 | URL | 用户是否确认升格 |
|------|-----|------------------|
| | | 是 / 否（仅参考） |
