# SoC / 主控选型 Skills

产品概念 → **Selection Brief** → **SoC Shortlist**（纯 Markdown 工件）。

| Skill | 角色 | 目录 |
|-------|------|------|
| `hardware-selection-brief` | 产品端 Phase 1（Dimension Turn） | [skills/hardware-selection-brief/](./skills/hardware-selection-brief/) |
| `soc-shortlist` | 技术端 Phase 2（含 Phase 2 Clarification） | [skills/soc-shortlist/](./skills/soc-shortlist/) |

领域语言：[CONTEXT.md](./CONTEXT.md)  
共享模板与 Profile：[shared/](./shared/)  
示例选型工件：[selection/](./selection/)

## 用法

1. 显式调用 `/hardware-selection-brief`，输入产品概念；每维一次 **Dimension Turn**（取值 + 约束等级），产出 `selection/<slug>/SELECTION_BRIEF.md`（元信息表 `brief_status` = `brief_ready`）。
2. 调用 `/soc-shortlist` 加载该 Brief；筛选中可按需做 **Spec Detail Probe**（**Probe Turn**：取值 + hard/soft/unconstrained，与 Phase 1 同形）与 Uncertainty 追问，导出前轻量确认 Shortlist/Near-Miss，产出 `SOC_SHORTLIST.md`。

v1 Product Family：Companion Robot、Wearable AI。
