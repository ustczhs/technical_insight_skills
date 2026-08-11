---
name: hardware-selection-brief
description: >-
  Runs a grilling interview to turn a product concept into a Selection Brief
  (pure Markdown tables) for SoC/main-silicon selection. Use when the product
  side needs hardware-selection requirements, SoC-oriented specs, companion-robot
  or wearable-AI dimension profiles, or a Brief Ready handoff—not a full PRD.
disable-model-invocation: true
---

# Hardware Selection Brief (Phase 1)

产品端 skill：把产品概念收敛为 **Selection Brief**，供同簇 `soc-shortlist` 使用。  
**不是**完整 PRD。术语以本簇 [CONTEXT.md](../CONTEXT.md) 为准。

## Principles

1. **第一性原理**：维度与约束服务于「产品要成立需要硅片具备什么能力」，而非「这类产品通常用哪一类营销标签的芯片」。
2. **Target Silicon Class 是优先锚，不是排异门**：写清默认类，并在 Brief §3 注明允许 Phase 2 覆盖相邻类（视觉 SoC、眼镜主控、音频 SiP、轻量 AP 等，按概念相关列出）。
3. **Hard 只锁能力边界**：不要用 Hard 变相写死厂商品类（例如「必须是机器人专用 AP」）；若确需排除某架构/栈，写成可验证 Spec Field。

## Before you start

1. Read [CONTEXT.md](../CONTEXT.md)
2. Read the Brief template: [shared/brief-template.md](../shared/brief-template.md)
3. Ask **one Dimension Turn at a time**; for each turn give a **recommended answer** and **recommended constraint grade**
4. Do not start Phase 2 search here — hand off when Brief Ready

## Workflow

Copy and track:

```
Phase 1 Progress:
- [ ] Step 0: 产品概念最小描述
- [ ] Step 1: Product Family（推断 → 确认 / Out-of-Family）
- [ ] Step 2: 加载 Dimension Profile + Target Silicon Class
- [ ] Step 3: 逐维 Dimension Turn（取值 + Hard|Soft|Unconstrained 同一问）
- [ ] Step 4: 触发并完成 Extension Dimensions（同等 Dimension Turn）
- [ ] Step 5: 导出 SELECTION_BRIEF.md 并勾选 Brief Ready
```

### Step 0 — 产品概念

用 3–8 句收集：做什么、给谁、关键场景。深度以能推导硬件约束为限。

### Step 1 — Product Family

根据概念推荐 v1 之一，说明理由，等产品确认：

| Family | Profile |
|--------|---------|
| Companion Robot | [shared/profiles/companion-robot.md](../shared/profiles/companion-robot.md) |
| Wearable AI | [shared/profiles/wearable-ai.md](../shared/profiles/wearable-ai.md) |

若都不贴：标 **Out-of-Family**，可轻量 grill，但明示 Phase 2 质量不保证，并建议扩展 Profile。

### Step 2 — Profile

加载对应 Profile；记下 **Target Silicon Class** 默认优先类（机器人：AP/SoM；可穿戴：音频 SoC/SiP/低功耗主控），并在导出 Brief §3 写明 **相邻类覆盖** 提示（例如机器人可含视觉 SoC/眼镜主控；可穿戴可含视觉 SoC/轻量 AP）。勿暗示 Phase 2 只能搜默认类。

### Step 3 — Dimension Turn（Core）

对 Profile 内每个 **Core Dimension** 做一次 **Dimension Turn**（见 CONTEXT.md）：

1. 用 **Product Framing** 提问，给出档位选项（推荐默认项）
2. 同时给出推荐约束等级 `hard` / `soft` / `unconstrained` + 一句理由（可参考 Profile 默认）
3. 用户**同一回复**中给出：取值（选项 / 自定义 / Unconstrained）**与**约束等级
4. 允许建议回复格式：`B / Hard` 或 `自定义：… / Soft`
5. 落盘时写出 **Spec Field** 与 **Framing–Spec Mapping**

**一次只问一个维度**；**禁止**把取值与等级拆成两问。

若用户只答取值：复述推荐等级并请其在同轮确认，仍算同一 Dimension Turn，不另开维度。

### Step 4 — Extensions

按 Profile 的触发表建议 Extension；产品确认纳入后，按 Core 同等 **Dimension Turn** 答完。

### Step 5 — Export & Brief Ready

写入建议路径：`selection/<product-slug>/SELECTION_BRIEF.md`（纯 Markdown，结构见模板）。

**Brief Ready** 当且仅当：

- Family 已确认（或 Out-of-Family 已明示）
- 全部 Core（及已纳入 Extension）均有 Dimension Answer
- 每项约束等级已在 Dimension Turn 中确认
- Framing–Spec Mapping 齐全
- 文首元信息表 `brief_status` = `brief_ready`

告知产品端：技术端使用 skill **`soc-shortlist`** 加载该 Brief。Phase 2 可能按需做 **Probe Turn**（硅片细节取值 + `hard`/`soft`/`unconstrained`，与 Dimension Turn 同形），**不会**替代本 skill 的产品维度 grilling；若探针暴露新产品能力边界，再回本 skill 修订 Brief。

## Rules

- **第一性原理**：约束写能力与接口，不写死营销品类排异
- 保持 Selection Brief 选型导向；拒绝扩成完整 PRD
- 不确定 ≠ Unconstrained；先给选项逼选
- 不使用嵌入 YAML 或 YAML front matter
- 更新术语冲突时以 CONTEXT.md 为准，必要时就地修订 glossary
- 同会话若直接续 Phase 2：仍须能导出 Brief；规范路径仍是文件交接
