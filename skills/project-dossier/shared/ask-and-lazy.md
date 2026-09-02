# 问询形态与 Lazy（分析叶子共用）

权威：本文件。`hardware-insight` 的 [intent-discovery.md](../../hardware-insight/references/intent-discovery.md) 是调研专用展开，**不得与本节冲突**。

`project-dossier` **只遵守 §A**，**不提供** §Lazy 连跑（禁止静默建档/覆盖索引）。

---

## A. 选择题（所有叶子，含 dossier）

面向用户的每一道决策题：

1. **一次一题**：等答完再继续。同一条消息、同一次 `AskQuestion` **只含一道题**。禁止「一批 1–5 维」连发。
2. 题干标明 **（单选）** 或 **（多选）**。
3. **必须有推荐** + 一句理由；选项上标 `（推荐）`。
4. **最后一项**固定为「其他（请补充）」。用户选此项或自由文本 → 按文本采纳，不强迫套进前几项。
5. 优先 `AskQuestion`（末项 `id: other`，label `其他（请补充）`；多选 `allow_multiple: true`）。无工具时用正文列表。
6. 事实自查，不问；决策在逐步确认下必问。

**正文模板**

```
（单选）<问题>？**推荐：<项>**——<一句理由>。

- A. …
- B. …（推荐）
- C. 其他（请补充）
```

---

## Lazy（仅分析叶子）

**分析叶子**：`hardware-insight`、`cross-domain-opportunity-explorer`、`hardware-selection-brief`、`soc-shortlist`、`grow-a-tech-tree`、`requirements-review`。

**时机**：项目闸门（slug / 最小建档）之后、本 skill 业务 Grill 之前。续跑且本流程已有「已确认/ready/complete」状态则**不问** Lazy。  
**空柜**：隔离根或目标 slug 尚无 `PROJECT.md` 时，对人第一题是闸门（slug / 最小建档），**不是** Lazy。

**第一题**（单选），**推荐关**：

- 关 Lazy，逐步确认（推荐）
- 开 Lazy，用推荐值跑完本 skill 全流程
- 其他（请补充）

首句已明示「lazy / 全自动 / 不用问我」→ 视为开，不再问。

**默认关。** 只有显式开才进入。

**开启后**

1. 用模型推荐填满本 skill 全部须确认字段；中途闸门**全部跳过**（含终稿：Brief Ready、Verdict、Shortlist 归属、技术树定稿、探索闸门③④⑤、调研 Step 8）。
2. 能默认立场则用 **中立第三方**，禁止编造组织名。
3. 产物中标注 `交互模式：Lazy` 或等价（「Lazy 默认，非逐步确认」）。
4. 用户中途说「改成 Lazy」→ 未决闸门改推荐值，从当前步连跑到本 skill 终点。

**各叶子「全流程」**

| 叶子 | Lazy 连跑到 |
|------|-------------|
| hardware-insight | Step 0–8 报告 MD（默认决策导向、不出信息图） |
| requirements-review | Clarified Requirement ready + Value Verdict final + 索引回写 |
| cross-domain-opportunity-explorer | 七段至 SESSION_BRIEF / Handoff（闸门①–⑤用推荐） |
| hardware-selection-brief | 全部 Dimension Turn 用推荐 → `brief_ready` |
| soc-shortlist | 检索+过滤+探针默认 → `SOC_SHORTLIST.md` complete（5b 维持证据结论） |
| grow-a-tech-tree | 叶清单+选定全叶生长+drawio/png/jpg 定稿 |

Probe / Sketch「待定」在 Lazy 下：采用推荐取值，不把「待定」当用户确认；若证据不足则降低 confidence / 标 Uncertainty，**不**把未证实 Hard 写成已确认事实。
