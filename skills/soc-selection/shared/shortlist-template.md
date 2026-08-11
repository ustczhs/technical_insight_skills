# SoC Shortlist Template

建议路径：`selection/<product-slug>/SOC_SHORTLIST.md`  
输入：同目录 `SELECTION_BRIEF.md`（须元信息表 `brief_status` = `brief_ready`）。  
**纯 Markdown**：不要 YAML。

# SoC Shortlist: \<产品名\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| product_slug | |
| product_family | |
| target_silicon_class | |
| brief_path | ./SELECTION_BRIEF.md |
| info_cutoff | YYYY-MM-DD |

## 1. 筛选摘要

- Hard Constraint 条数：
- Shortlist 数量：
- Near-Miss 数量：
- 主要不确定点：
- Phase 2 Clarification：Uncertainty 追问 / Spec Detail Probe / 归属确认（简述）

## 1b. Spec Detail Probe 记录

本轮按需探针（无则写「无触发」）。须写明形态包。每一行为一次 **Probe Turn**（取值 + grade）。启发式见同目录 [phase2-spec-probes.md](./phase2-spec-probes.md)。

| 字段 | 值 |
|------|-----|
| probe_pack | 例：`companion_robot/indoor_mobile` 或 `wearable_ai/ows_vision` |

| probe_id | answer | grade | 影响 |
|----------|--------|-------|------|
| （机器人例）uart_count | >=4 | hard | UART&lt;4 → Near-Miss |
| （可穿戴例）isp_topology | external_ok | hard | 外挂 ISP 可过视觉相关约束 |
| （例）package_pin | mid_ok | soft | 仅 Match Band |

`grade`：`hard` \| `soft` \| `unconstrained`

## 2. Hard Constraints 应用表

| id | Spec 摘要 | 结果策略 |
|----|-----------|----------|

（含已确认 `grade=hard` 的探针，可用 `probe:<id>` 作为 id）

## 3. SoC Shortlist

按 Match Band：**高匹配 → 中匹配 → 低匹配**（不做精确分）。

### 高匹配

#### \<厂商\> \<型号\>

| 字段 | 值 |
|------|-----|
| part | |
| vendor | |
| silicon_class | ap_som / audio_soc / sip / low_power_mcu / vision_soc / other |
| match_band | high |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| example_id | pass | [A] …（信息时效：YYYY-MM，URL）；[A] … |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| cost_band | met / partial / unmet | |

**Uncertainty**

- …

**来源**

| URL | grade | dated |
|-----|-------|-------|
| | A | YYYY-MM |

对比说明（相对 Brief / 其他候选）：…

### 中匹配

…

### 低匹配

…

## 4. Near-Miss（非 Shortlist 成员）

| 型号 | 违反的 Hard Constraint | 建议回谈放宽？ | 证据 |
|------|------------------------|----------------|------|

## 5. 空清单处理

若 Shortlist 为空：写明「正式 Shortlist 为空」；保留 Near-Miss；列出建议优先放宽的 Hard Constraint（产品端回 `hardware-selection-brief`）。

## 6. 证据附录

- 分级：A > B > C；Critical Claim ≥2 独立来源
- Freshness：>48 月的 [A] 用于现状时降为 [B]
- 信息截止：见元信息表 `info_cutoff`
