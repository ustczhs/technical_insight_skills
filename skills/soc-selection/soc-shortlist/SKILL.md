---
name: soc-shortlist
description: >-
  Use when the tech side must turn a Brief Ready Selection Brief into an
  evidenced SoC/SiP/SoM Shortlist (and Near-Miss), including Silicon-Class-gated
  on-demand silicon detail probes, Application Domain industry coverage, or when
  handed a hardware-selection Brief (including Out-of-Family profiles).
disable-model-invocation: true
---

# SoC Shortlist (Phase 2)

技术端 skill：读取 **Brief Ready** 的 Selection Brief，以 **primary Silicon Class + adjacent Classes + Application Domain** 为覆盖锚搜索公开资料，产出 **SoC Shortlist**（+ 必要时 **Near-Miss**）。  
允许有限的 **Phase 2 Clarification**（含按需 **Spec Detail Probe**），**不是**产品维度重 grill。  
术语：[CONTEXT.md](../CONTEXT.md)。证据：[shared/evidence-rules.md](../shared/evidence-rules.md)。探针：[shared/phase2-spec-probes.md](../shared/phase2-spec-probes.md）。种子：[shared/vendor-seeds.md](../shared/vendor-seeds.md)。Class/Domain：[shared/silicon-classes.md](../shared/silicon-classes.md)、[shared/application-domains.md](../shared/application-domains.md)。

## Principles

1. **第一性原理**：用 Brief 的 Hard/Soft 判定去留；品类标签不是整类淘汰理由。
2. **Family 不决定检索**：覆盖清单按 Class∪Domain，不按 Product Family；Out-of-Family 不降级检索。
3. **不轻易整类排除**：满足 Hard 的相邻主控须评估；类标差异进 Match Band。
4. **覆盖优先于刻板名单**：须完成 Class 矩阵 + Domain 加扫后再收敛。
5. **双语与原厂优先**；**结论先行**；**证据约束不变**。

## Before you start

1. **项目闸门**：运行 `project-dossier/scripts/ensure-projects-root.sh`；确认 `project_slug`；无 `PROJECT.md` 则最小建档或引导 `/project-dossier`。只写入 `$PROJECTS_ROOT/<project_slug>/selection/`。
2. Read 本簇 [CONTEXT.md](../CONTEXT.md) and [evidence-rules.md](../shared/evidence-rules.md)
3. Load the Brief（`$PROJECTS_ROOT/<project_slug>/selection/SELECTION_BRIEF.md`）
4. Read shortlist-template、vendor-seeds、silicon-classes、application-domains；skim phase2-spec-probes
5. **Refuse** full Phase 2 if `brief_status` ≠ `brief_ready`，或缺少 `primary_silicon_class` / 未确认的 `application_domains` — 列缺口回 Phase 1
6. Shortlist 定稿后回写 `PROJECT.md` §4 selection 一行

## Workflow

```
Phase 2 Progress:
- [ ] Step 0: 校验 Brief Ready + Class + Domain（含 needs_seed_extension）
- [ ] Step 1: 抽出 Hard / Soft / Unconstrained
- [ ] Step 2: 公开源搜索（Class 矩阵 ∪ Domain 加扫；双语）
- [ ] Step 2a: 落盘厂商扫描表（Class∪Domain 行全覆盖）
- [ ] Step 2b: Spec Detail Probe（按 Silicon Class 门控）
- [ ] Step 3: Hard 过滤 → Shortlist / Near-Miss
- [ ] Step 3b: Uncertainty Clarification
- [ ] Step 4: Soft + Domain 命中 → Match Band
- [ ] Step 5: 证据与 Critical Claim
- [ ] Step 5b: 归属轻量确认
- [ ] Step 6: 写出 SOC_SHORTLIST.md
```

### Step 0 — Gate

确认：

- `brief_status` = `brief_ready`
- `primary_silicon_class` 已有；`adjacent_silicon_classes` 已读入
- `application_domains` 已读入（可为空仅当概念确无行业域且已确认 `generic_iot` 或显式无域——否则回 Phase 1）
- `needs_seed_extension`：若 true，文首降级声明「未登记域/类，矩阵不完整」
- 已打开 vendor-seeds 中 **各 Class 段 + 各 Domain 加扫表** 作为覆盖清单

### Step 1 — Extract filters

从 Brief 汇总 Hard / Soft / Unconstrained。Unconstrained **不参与**过滤与排序。

### Step 2 — Search

仅公开网页/手册/认证库等。遵守 evidence-rules。

**检索范围（强制）**：

1. **主 Class**：`primary_silicon_class` 对应 vendor-seeds 段（国内+国外必扫）
2. **相邻 Class**：`adjacent_silicon_classes` 各段同样必扫
3. **Domain 加扫**：每个 `application_domains` 的 Overlay 行必扫（行业方案/料号）
4. 矩阵外合格料仍可入选；营销品类不符 **不得**单独构成 Near-Miss
5. Soft「优先某某」若未落入 Domain，可建议加搜但不挡 complete；**不得**用 Family 旧表替代本清单

**检索质量（强制）**：双语、厂商/料号定向 query、原厂优先、漏检自检（同前）。

按 **Silicon Class 探针包**采集细节供 Step 2b；候选可跨营销品类。

### Step 2a — 厂商扫描表（闸门）

扫描表须覆盖本轮 **所有 Class 必扫行 + Domain 加扫行**。`status`：`assessed` / `no_public_part` / `out_of_scope`。  
缺行则不得 `shortlist_status=complete`。建议增加列 `coverage_source` = `class:<id>` | `domain:<id>`。

### Step 2b — Spec Detail Probe（按需 · Class 门控）

1. `probe_pack` = `primary_silicon_class`（+ 可选 sub_form）
2. **只打开** phase2-spec-probes 中对应 Class 包
3. 禁止按 Product Family 选包（勿因挂靠 companion_robot 而用机器人 AP 包问 display_mcu）

其余 Probe Turn 规则不变：一次一问；选项 + 推荐答案 + 推荐 `hard|soft|unconstrained`；用户同回确认取值与等级；答案不静默写回 Brief；扩大产品能力边界则建议回 Phase 1。

**必须追问**（包内满足任一）：Brief 沉默但候选 Hard 分叉；缺口径无法比 Match Band；公开规格冲突需本轮立场。

**禁止**：全表必问；按 Family 选包；用 Probe 重开产品 Dimension；废弃的 apply_as/run_hard 等口径。

### Step 3 — Hard filter

- 满足全部 Brief Hard **以及** 已确认 `grade=hard` 的探针 → 进入 Shortlist  
- 否则 → **Near-Miss**（列出违反的 Hard id / `probe:<id>`），**不是** Shortlist 成员  
- `grade=unconstrained` 的探针不参与本步  
- 正式 Shortlist **可以为空**；不得为凑数自动放宽 Hard 或 hard 探针
- Selection Brief 的 **§9 源溯源附录**仅供审计；Phase 2 **只读**正式 Hard Constraint / Soft Preference，不按附录筛选

空清单时：输出 Near-Miss + 建议优先回谈放宽的 Hard Constraint / 探针。

### Step 3b — Phase 2 Clarification（Uncertainty）

仅当某候选的 **Hard / grade=hard 探针判定**被 Uncertainty / 缺双源 Critical Claim **阻塞**时：

1. 一次只问一个阻塞点  
2. 选项 + **推荐默认**（常见：未知按不满足 / Near-Miss）  
3. 若追问会**改写本轮探针取值或等级**，仍用 Probe Turn 格式：`选项或自定义 / hard|soft|unconstrained`  
4. 用户确认后继续筛选；**不**借机重开产品维度 grill  
5. 放宽 Brief Hard 语义 → 必须让产品端改 Brief 后重跑  

与 Step 2b 的区别：3b 解决「证据够不够判」；2b 解决「Brief 没说清要什么规格细节」。

### Step 4 — Match Band

对 Shortlist 内候选，按 Brief Soft Preference、`grade=soft` 探针、以及 **Application Domain 命中**（行业方案/产线贴合），粗分为 **高 / 中 / 低** 匹配。禁止假装精确加权总分。`unconstrained` 探针不参与。  
相邻 Class 候选若 Soft 明显弱于主 Class，可落在中/低匹配，但**不得**仅因类标踢出 Shortlist。Domain 命中可抬一档（仍须已过 Hard）。

### Step 5 — Evidence pass

每个 Shortlist 成员：Brief Hard 与 `grade=hard` 探针相关结论证据齐全；Uncertainty 与未追问但已记录的细节缺口显式列出。

### Step 5b — Phase 2 Clarification（归属确认）

写出文件前，用**一问**做轻量确认（此步是名单归属，**不是** Probe Turn）：

- 是否接受当前 Shortlist / Near-Miss 划分？  
- 是否要把某 Near-Miss 升格（仅当不违反 Brief Hard 与 `grade=hard` 探针；否则拒绝并说明）？  

给出推荐（通常：维持证据结论）。用户确认后再落盘。

### Step 6 — Export

写 `$PROJECTS_ROOT/<project_slug>/selection/SOC_SHORTLIST.md`（纯 Markdown，结构见 [shortlist-template.md](../shared/shortlist-template.md)）。数量不限、不强制唯一赢家。

**文档质量（强制）——结论先行、论据随后：**

1. **§1 结论**必须可独立阅读：推荐表（Match Band + 一句话结论 + 主要风险）、取舍摘要、Near-Miss 一览、Uncertainty。读者不应翻到后文才知道「选了谁」。
2. **禁止**把厂商扫描表、探针全表、长证据链放在结论之前；这些进「过程附录」。
3. **每个候选卷宗**先写「结论卡」（过 Hard 要点 / Match Band 理由 / 相对差异 / Uncertainty），再写 Hard/Soft 证据表与来源。
4. 一句话结论须**具体**（能力+相对 Brief），禁止空话（如「较适合」「综合表现好」）。
5. 门户/对话回传的 `reply` 也应先给结论表，再提附录已落盘——与文件结构同构。

须包含（可在附录）：

1. **厂商扫描表**（Step 2a；矩阵必扫行齐全）
2. **检索覆盖**摘要（primary Class / adjacent Classes / Domain 加扫已评估型号）
3. **Spec Detail Probe 记录表**（probe_id / answer / **grade** / 影响；注明 `probe_pack`），即便本轮零探针也写「无触发」

`grade` 仅允许：`hard` \| `soft` \| `unconstrained`。  
仅当 Step 2a 闸门通过（Class∪Domain 行齐）且 Hard 过滤完成时，可将 `shortlist_status` 标为 `complete`。`needs_seed_extension=true` 时 complete 须在 §1 显式降级说明。

## Rules

- **结论先行**；**第一性原理**；**Class∪Domain 矩阵必扫**；**双语检索**
- 矩阵是覆盖清单不是白名单；不按 Product Family 选种子表
- 不修改 Brief Hard 语义；Probe 不静默写回 Brief
- **Out-of-Family 不降级检索**（仅问卷缺口）；`needs_seed_extension` 才是种子不完整降级
- primary Silicon Class 是优先锚，不是唯一入场门禁
- Probe 按 Silicon Class 门控，不按 Family
- 不使用嵌入 YAML；Phase 2 Clarification ≠ 产品需求回访

