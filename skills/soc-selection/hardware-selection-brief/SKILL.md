---
name: hardware-selection-brief
description: >-
  Runs a grilling interview to turn a product concept into a Selection Brief
  (pure Markdown tables) for SoC/main-silicon selection. Use when the product
  side needs hardware-selection requirements, SoC-oriented specs, companion-robot
  or wearable-AI dimension profiles, Out-of-Family light grilling, Application
  Domain / Silicon Class confirmation, or a Brief Ready handoff—not a full PRD.
disable-model-invocation: true
---

# Hardware Selection Brief (Phase 1)

产品端 skill：把产品概念收敛为 **Selection Brief**，供同簇 `soc-shortlist` 使用。  
**不是**完整 PRD。术语以本簇 [CONTEXT.md](../CONTEXT.md) 为准。  
ADR：[docs/adr/0001-retrieval-decoupled-from-family.md](../docs/adr/0001-retrieval-decoupled-from-family.md)。

## Principles

1. **第一性原理**：维度与约束服务于「产品要成立需要硅片具备什么能力」。
2. **Family ≠ 检索范围**：Product Family 只选 Dimension Profile；检索由 **Application Domain + Silicon Class** 决定。
3. **行业优先落 Domain**：如「摩托车/电动车芯片」→ `application_domains`，不要只写 Soft 散文。
4. **Silicon Class 是优先锚，不是排异门**：写清 primary + adjacent；Hard 触发相邻类在 Ready 前复核。
5. **Hard 只锁能力边界**：不要用 Hard 写死厂商品类。
6. **Brief Source 只产草案**：须经 Dimension Turn 升格。

## Before you start

1. Read [CONTEXT.md](../CONTEXT.md)
2. Read [shared/brief-template.md](../shared/brief-template.md)、[shared/application-domains.md](../shared/application-domains.md)、[shared/silicon-classes.md](../shared/silicon-classes.md)
3. Check workspace `selection/<slug>/sources/` and context `brief_sources`（若有）
4. 若 context 已带 `application_domains` / `primary_silicon_class` 等门户预填：作为推荐项，仍须产品确认
5. Ask Dimension Turns in batches (1–5)；每题给 **recommended answer** 与 **recommended constraint grade**
6. Do not start Phase 2 search here

## Workflow

```
Phase 1 Progress:
- [ ] Step 0: 产品概念最小描述
- [ ] Step 0b: Application Domain（推断 → 确认；自定义则 needs_seed_extension）
- [ ] Step 1: Product Family（推断 → 确认 / Out-of-Family）
- [ ] Step 1b: primary Silicon Class（早选确认）
- [ ] Step 2: 加载 Dimension Profile
- [ ] Step 2b: 扫描 Brief Source → Source-Derived Draft（+ Source Residue）
- [ ] Step 3: 逐维 Dimension Turn
- [ ] Step 4: Extension Dimensions
- [ ] Step 4b: Hard → adjacent Silicon Class 复核确认
- [ ] Step 5: 导出 SELECTION_BRIEF.md 并勾选 Brief Ready
```

### Step 0 — 产品概念

用 3–8 句收集：做什么、给谁、关键场景。深度以能推导硬件约束为限。

### Step 0b — Application Domain

从标题/概念推荐词表内域（可多选），说明理由，等产品确认：

- 词表：[shared/application-domains.md](../shared/application-domains.md)
- 例：摩托车机器人 → `motorcycle` + `light_ev`
- 自定义未入表 → 写入 Brief，且 `needs_seed_extension=true`
- 门户若已预填：复述并请确认/修改（可一批题）

### Step 1 — Product Family

根据概念推荐 v1 之一，说明理由，等产品确认：

| Family | Profile |
|--------|---------|
| Companion Robot | [shared/profiles/companion-robot.md](../shared/profiles/companion-robot.md) |
| Wearable AI | [shared/profiles/wearable-ai.md](../shared/profiles/wearable-ai.md) |

若都不贴：标 **Out-of-Family**（轻量 Profile）。明示：这只影响问卷，**不**降低 Phase 2 检索质量（检索看 Class/Domain）。

**闸门**：Family 未确认前，**不得**产出跨 Profile 的结构化 Source-Derived Draft。

### Step 1b — primary Silicon Class

在维度 grilling 前确认 **恰好一个** `primary_silicon_class`（枚举见 silicon-classes.md）。  
可用 Family 推荐作默认（机器人→`ap_som`，可穿戴→`audio_sip`），但 **必须允许按概念改写**（摩托车表情屏→`display_mcu` / `industrial_mcu`）。  
相邻类可先记推荐，正式锁定在 Step 4b。

### Step 2 — Profile

加载对应 Profile。导出 Brief §3 时写清 primary + adjacent 计划；勿暗示 Phase 2 按 Family 旧矩阵检索。

### Step 2b — Brief Source → Source-Derived Draft

若 `sources/` 或 `brief_sources` 非空：按既有规则抽取 Draft / Residue。无源则跳过。

### Step 3 — Dimension Turn（Core）

对 Profile 内每个 Core Dimension 做 Dimension Turn（门户可一批 1～5）。Out-of-Family 仅其轻量维。

### Step 4 — Extensions

按 Profile 触发表与 Source Residue 提议 Extension；确认后同等 Dimension Turn。

### Step 4b — adjacent Silicon Class 复核

根据已确认 Hard（及关键 Soft 能力）套用 [silicon-classes.md](../shared/silicon-classes.md) 触发表，提出 adjacent 列表 → 产品确认一次。  
写入元信息 `adjacent_silicon_classes`。

### Step 5 — Export & Brief Ready

写入 `selection/<product-slug>/SELECTION_BRIEF.md`（结构见模板）。

元信息必须含：`application_domains`、`primary_silicon_class`、`adjacent_silicon_classes`、`needs_seed_extension`。

**Brief Ready** 当且仅当：

- Family 已确认（或 Out-of-Family 已明示）
- Application Domain 已确认
- primary Silicon Class 已确认；adjacent 已复核
- 全部 Core（及已纳入 Extension）均有 Dimension Answer
- 每项约束等级已确认；Framing–Spec Mapping 齐全
- 文首 `brief_status` = `brief_ready`

告知：技术端用 **`soc-shortlist`**；Phase 2 按 Class∪Domain 覆盖检索。

## Rules

- 不把 Family 写成检索范围
- 行业优先必须进 Application Domain
- Soft 不单独改必扫矩阵
- 不使用嵌入 YAML
- Out-of-Family ≠ Phase 2 降级
