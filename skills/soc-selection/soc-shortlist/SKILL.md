---
name: soc-shortlist
description: >-
  Use when the tech side must turn a Brief Ready Selection Brief into an
  evidenced SoC/SiP/SoM Shortlist (and Near-Miss), including form-gated
  on-demand silicon detail probes (e.g. robot UART/display/CSI; wearable
  ISP/SRAM/audio I/O), or when handed a hardware-selection Brief for
  companion robots or wearable AI.
disable-model-invocation: true
---

# SoC Shortlist (Phase 2)

技术端 skill：读取 **Brief Ready** 的 Selection Brief，以 **Target Silicon Class 为优先锚**、并做 **相邻类覆盖** 地搜索公开资料，产出 **SoC Shortlist**（+ 必要时 **Near-Miss**）。  
允许有限的 **Phase 2 Clarification**（含按需 **Spec Detail Probe**，见本簇 CONTEXT.md），**不是**产品维度重 grill。  
术语：[CONTEXT.md](../CONTEXT.md)。证据：[shared/evidence-rules.md](../shared/evidence-rules.md)。探针启发式：[shared/phase2-spec-probes.md](../shared/phase2-spec-probes.md）。

## Principles

1. **第一性原理**：用 Brief 的 Hard/Soft（算力、接口、功耗热、音视频链路、软件可落地等）判定去留；品类标签与营销定位只作检索线索，**不是**整类淘汰理由。
2. **不轻易整类排除**：默认类之外，凡可能满足 Hard 的相邻主控均须评估（例：AI 眼镜 / IPC 视觉 SoC → 桌面机器人或视觉耳机；轻量 AP → 可穿戴）。类标差异进 Match Band / 取舍说明，勿默杀。
3. **覆盖优先于刻板名单**：禁止只搜「某形态惯用 3–5 款」；种子集 + 相邻类至少各扫一轮。仍须有 Spec Field 对照，禁止无关料号灌水。
4. **证据约束不变**：不编造；Critical Claim 双源；Uncertainty 显式标出。

## Before you start

1. Read 本簇 [CONTEXT.md](../CONTEXT.md) and [evidence-rules.md](../shared/evidence-rules.md)
2. Load the Brief（路径由用户给出，或 `selection/<slug>/SELECTION_BRIEF.md`）
3. Read [shared/shortlist-template.md](../shared/shortlist-template.md) and skim [shared/phase2-spec-probes.md](../shared/phase2-spec-probes.md)
4. **Refuse** full Phase 2 if 文首元信息表 `brief_status` ≠ `brief_ready` — 列出缺口，让产品端回 `hardware-selection-brief`

## Workflow

```
Phase 2 Progress:
- [ ] Step 0: 校验 Brief Ready + Family + Target Silicon Class（含相邻类覆盖计划）
- [ ] Step 1: 抽出 Hard Constraints / Soft Preferences
- [ ] Step 2: 公开源搜索候选（默认类 + 相邻类；不编造）
- [ ] Step 2b: 规格细节缺口扫描 → 按需 Spec Detail Probe（可多轮，一次一问）
- [ ] Step 3: Hard 过滤（含已确认 grade=hard 的探针）→ Shortlist；失败者进 Near-Miss
- [ ] Step 3b: Uncertainty 阻塞时做 Phase 2 Clarification（可多轮，一次一问）
- [ ] Step 4: Soft → Match Band（含 grade=soft 的探针；类标贴合度可进取舍说明）
- [ ] Step 5: 证据标注与 Critical Claim 双源校验
- [ ] Step 5b: 导出前轻量确认 Shortlist / Near-Miss 归属
- [ ] Step 6: 写出 SOC_SHORTLIST.md
```

### Step 0 — Gate

确认：

- 文首元信息表 `brief_status` = `brief_ready`
- Product Family / Out-of-Family 风险已知
- Target Silicon Class 作为**优先种子**已记下，并列出本轮 **相邻类覆盖**（至少一类跨营销品类，例如机器人 Brief → 视觉 SoC/眼镜主控；可穿戴 Brief → 视觉 SoC 或轻量 AP——按 Hard 相关性选取）

### Step 1 — Extract filters

从 Brief 汇总 Hard / Soft / Unconstrained。Unconstrained **不参与**过滤与排序。

### Step 2 — Search

仅公开网页/手册/认证库等。遵守 evidence-rules：

- 标注 `[A/B/C] …（信息时效：YYYY-MM，URL）`
- Critical Claim ≥2 独立来源
- >48 月 [A] 用于现状 → 降为 [B]
- 缺数据 → Uncertainty，不编造

**检索范围（强制）**：

1. **默认类**：Brief 的 Target Silicon Class（如机器人 AP/SoM；可穿戴音频 SoC/SiP）
2. **相邻类**：可能满足同一组 Hard 的跨形态主控（视觉 SoC、AI 眼镜芯片、IPC/运动相机主控、轻量 AP、部分音频+视觉 SiP 等）
3. 以 Spec Field / Hard 做能力对照；营销品类不符 **不得**单独构成 Near-Miss 理由

搜索时按 **形态包** 主动采集公开可得细节（机器人侧重 UART/总线/显示通道/CSI；可穿戴侧重 ISP/SRAM/麦与封装等）——供 Step 2b 判断是否值得追问。候选可来自跨营销品类；**探针问法**仍按本产品 `probe_pack` 门控，勿改用他形态体验问卷。

### Step 2b — Spec Detail Probe（按需 · 形态门控）

硬件选型常卡在 Brief 未写的硅片细节。在初搜之后、定稿 Hard 过滤之前：

1. 从 Brief 确定 **probe_pack** = Family + `sub_form`（及 Extension）  
2. **只打开** [phase2-spec-probes.md](../shared/phase2-spec-probes.md) 中对应形态包做缺口扫描  
3. 跨包提问视为违规（例如用 OWS 的 SRAM 问卷替代机器人的串口/显示通道）

**必须追问**（在形态包内满足任一即发起，仍一次一问）：

1. Brief 对某属性沉默，但候选因此在 Hard 相关能力上分叉  
2. 缺该口径则无法诚实比较 Match Band  
3. 公开规格冲突，需要本轮筛选立场（非编造参数）

**形态示例（完整表见启发式文件）**：

- Companion Robot：`uart_count`、`iface_types`、`display_channels`、`csi_lanes_cams`、`realtime_io` 等  
- Wearable AI：`isp_topology` / `sram_psram` / `cam_iface`；OWS 的 `audio_iface` / `package_pin`；眼镜的 `display_out` / `wifi_throughput` 等  

**禁止**：

- 把探针总表当每轮必答问卷  
- 用 Probe 重开产品场景 / 体验档（那是 Phase 1 的产品 Dimension Turn）  
- 忽略 `sub_form` 套用错误形态包  
- 在未扫描候选差异前空问「还要什么接口」  
- 使用已废弃的 `run_hard` / `run_soft` / `note_only` / `apply_as` 口径

#### Probe Turn（与 Phase 1 Dimension Turn 对齐）

每一探针视为一次 **Probe Turn**（类比 Dimension Turn）：

1. 声明 `probe_pack` + 为何影响筛选（点名 Brief Hard/Soft id 或候选分叉）  
2. 给出档位/选项（可含自定义），标明**推荐答案**  
3. **同时**给出推荐约束等级 `hard` / `soft` / `unconstrained` + 一句理由  
4. 用户**同一回复**给出：取值 **与** 等级（允许 `B / Hard`、`自定义：UART≥4 / Soft`、`U / Unconstrained`）  
5. 落盘：`Dimension Answer` 风格的取值 + `grade` + 对筛选的影响说明  

| grade | 本轮筛选含义（与 Phase 1 / CONTEXT 一致） |
|-------|------------------------------------------|
| `hard` | 不满足 → **不得**入 Shortlist（进 Near-Miss） |
| `soft` | 不满足仍可入选，计入 **Match Band** |
| `unconstrained` | 显式无要求：不筛、不排序 |

若用户只答取值：复述推荐等级并请其在同轮确认，**仍算同一 Probe Turn**，不另开探针。

若答案实质扩大产品能力边界 → 建议回 `hardware-selection-brief` 改 Brief 后重跑；本轮可将该探针标 `unconstrained` 或暂停该项。

### Step 3 — Hard filter

- 满足全部 Brief Hard **以及** 已确认 `grade=hard` 的探针 → 进入 Shortlist  
- 否则 → **Near-Miss**（列出违反的 Hard id / `probe:<id>`），**不是** Shortlist 成员  
- `grade=unconstrained` 的探针不参与本步  
- 正式 Shortlist **可以为空**；不得为凑数自动放宽 Hard 或 hard 探针

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

对 Shortlist 内候选，按 Brief Soft Preference **与** `grade=soft` 探针满足度，粗分为 **高 / 中 / 低** 匹配。禁止假装精确加权总分。`unconstrained` 探针不参与。  
相邻类候选若 Soft（算力带、软件栈、供货/SDK 成熟度）明显弱于默认类，可落在中/低匹配，但**不得**仅因类标把它踢出 Shortlist。

### Step 5 — Evidence pass

每个 Shortlist 成员：Brief Hard 与 `grade=hard` 探针相关结论证据齐全；Uncertainty 与未追问但已记录的细节缺口显式列出。

### Step 5b — Phase 2 Clarification（归属确认）

写出文件前，用**一问**做轻量确认（此步是名单归属，**不是** Probe Turn）：

- 是否接受当前 Shortlist / Near-Miss 划分？  
- 是否要把某 Near-Miss 升格（仅当不违反 Brief Hard 与 `grade=hard` 探针；否则拒绝并说明）？  

给出推荐（通常：维持证据结论）。用户确认后再落盘。

### Step 6 — Export

写 `selection/<product-slug>/SOC_SHORTLIST.md`（纯 Markdown）。数量不限、不强制唯一赢家。  
须包含：**Spec Detail Probe 记录表**（probe_id / answer / **grade** / 影响），即便本轮零探针也写「无触发」。  
`grade` 仅允许：`hard` \| `soft` \| `unconstrained`。

## Rules

- **第一性原理优先**：Hard/证据 > 品类刻板印象；不整类默杀相邻硅片  
- 不修改 Brief 的 Hard 语义；放宽只能建议产品端改 Brief 后重跑  
- Spec Detail 答案是**本轮 Shortlist 口径**，不静默写回 Brief  
- Probe Turn 的等级语义与 Phase 1 / CONTEXT 的 Hard Constraint、Soft Preference、Unconstrained **同一套词**  
- Out-of-Family Brief：可尽力搜，但文首降级声明  
- Target Silicon Class 是优先锚，**不是**唯一入场门禁；满足 Hard 的相邻类可入 Shortlist（Match Band 可偏低）  
- 与产品端争议规格含义时，以 Brief 中 Framing–Spec Mapping 为准；Probe 仅补 Brief 空白  
- 不使用嵌入 YAML 或 YAML front matter  
- Phase 2 Clarification ≠ 产品需求回访  
 
