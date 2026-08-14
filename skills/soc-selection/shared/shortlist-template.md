# SoC Shortlist Template

建议路径：`selection/<product-slug>/SOC_SHORTLIST.md`  
输入：同目录 `SELECTION_BRIEF.md`（须元信息表 `brief_status` = `brief_ready`）。  
**纯 Markdown**：不要 YAML。

**写法强制：结论先行、论据随后。** 读者应在前两屏看到「选谁 / 为何 / 主要风险」；厂商扫描、探针、逐条证据放后文。

# SoC Shortlist: \<产品名\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| product_slug | |
| product_family | |
| application_domains | |
| primary_silicon_class | |
| adjacent_silicon_classes | |
| needs_seed_extension | false |
| target_silicon_class | |
| brief_path | ./SELECTION_BRIEF.md |
| info_cutoff | YYYY-MM-DD |
| shortlist_status | in_progress / complete |

---

## 1. 结论（先读这里）

> 本节是全文重点。后面章节只提供论据与过程，不重复改写结论。

### 1.1 推荐 Shortlist（按 Match Band）

| 优先级 | Match Band | 厂商 · 型号 | 一句话结论（为何入选） | 主要风险 / Uncertainty |
|--------|------------|-------------|------------------------|-------------------------|
| 1 | 高 | | | |
| 2 | 中 | | | |
| … | 低 | | | |

- **不强制唯一赢家**；若有首选，用一行「建议优先评估：…」点明，并说明相对第 2 名的关键差距（1～2 句）。
- Shortlist 为空时：写「正式 Shortlist 为空」+ 建议优先放宽的 Hard（指向 §3 Near-Miss）。

### 1.2 取舍摘要（相对 Brief）

用 3～6 条子弹，只写**决策向**信息：

- 过 Hard 的关键能力（例：单芯片 BT5 + 无 Wi‑Fi、TWS SDK）
- Soft / 探针如何拉开 Match Band（例：OWS 参考、≥2 MB SRAM）
- 明确不选或降档的原因（点名型号即可，细节见后文）

### 1.3 Near-Miss 一览（非 Shortlist）

| 型号 | 卡在哪条 Hard | 若放宽是否值得回谈 |
|------|---------------|--------------------|
| | | 是 / 否 + 半句 |

### 1.4 本轮口径与不确定点

- Hard 条数 / Soft 条数 / 探针 Hard·Soft（各几条）
- Spec Detail Probe：有则一行摘要（取值+grade）；无则「无触发」
- **必须正视的 Uncertainty**（阻塞量产决策的缺数/冲突）；无则写「无阻塞级 Uncertainty」

---

## 2. 论据：Hard 过滤怎么判

| id | Spec 摘要 | 结果策略 |
|----|-----------|----------|

（含已确认 `grade=hard` 的探针，可用 `probe:<id>` 作为 id）

---

## 3. 论据：候选卷宗（Shortlist 成员）

按 Match Band：**高 → 中 → 低**。每个型号先给**判定结论**，再给证据表——禁止一上来大段来源堆砌。

### 高匹配

#### \<厂商\> \<型号\>

| 字段 | 值 |
|------|-----|
| part | |
| vendor | |
| silicon_class | ap_som / audio_soc / sip / low_power_mcu / vision_soc / other |
| match_band | high |

**结论卡（必填，3～5 行）**

- **过 Hard 的要点**：…
- **Match Band 理由**（相对 Soft/探针）：…
- **相对其他候选**：…（半句即可）
- **Uncertainty**：有则一条；无则「无」

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| example_id | pass | [A] …（信息时效：YYYY-MM，URL）；[A] … |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| cost_band | met / partial / unmet | |

**来源**

| URL | grade | dated |
|-----|-------|-------|
| | A | YYYY-MM |

### 中匹配

…

### 低匹配

…

---

## 4. 论据：Near-Miss 明细

| 型号 | 违反的 Hard Constraint | 建议回谈放宽？ | 证据 |
|------|------------------------|----------------|------|

（与 §1.3 对应；此处可写完整证据句。）

---

## 5. 过程附录（检索与探针）

> 供审计 / 复现；**不要**把本节写到结论之前。

### 5.1 检索覆盖

| 类别 | 已评估型号 |
|------|-----------|
| 默认类 | |
| 相邻类 | |

### 5.2 厂商扫描表（强制 · 矩阵闸门）

对应 [vendor-seeds.md](./vendor-seeds.md) 本 Family 国内+国外必扫行。`shortlist_status=complete` 前须行齐全。

| vendor | region | silicon_focus | status | parts_touched | notes |
|--------|--------|---------------|--------|---------------|-------|
| | CN / Global | audio_soc / ap_som / … | assessed / no_public_part / out_of_scope | | |

### 5.3 Spec Detail Probe 记录

本轮按需探针（无则写「无触发」）。须写明形态包。每一行为一次 **Probe Turn**（取值 + grade）。启发式见 [phase2-spec-probes.md](./phase2-spec-probes.md)。

| 字段 | 值 |
|------|-----|
| probe_pack | 例：`companion_robot/indoor_mobile` 或 `wearable_ai/ows_vision` |

| probe_id | answer | grade | 影响 |
|----------|--------|-------|------|
| （例）isp_topology | external_ok | soft | 外挂 ISP 可入选 |

`grade`：`hard` \| `soft` \| `unconstrained`

### 5.4 证据规则备忘

- 分级：A > B > C；Critical Claim ≥2 独立来源
- Freshness：>48 月的 [A] 用于现状时降为 [B]
- 信息截止：见元信息表 `info_cutoff`

## 6. 空清单处理

若 Shortlist 为空：§1.1 已声明；本节可补「建议优先放宽的 Hard」排序（产品端回 `hardware-selection-brief`）。
