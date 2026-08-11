# Evidence Rules (Phase 2)

Aligned with `ai_hardware_insight`, with a longer freshness window for silicon.

## Evidence Grade

| Grade | Sources |
|-------|---------|
| **A** | 官方 datasheet / 产品页、拆解、认证库 |
| **B** | 权威媒体、代理商/供应商规格页 |
| **C** | 论坛、二手转述、未标注来源汇总 |

**Critical Claim**（影响 Hard Constraint 判定或 Shortlist 去留）：≥2 处**独立**来源；各标 Evidence Grade。

## Evidence Freshness

- 用于描述**现状**时：超过 **48** 个月的 [A] 源降为 [B]，直至有更新近源印证。
- 引用格式：`[A/B/C] 内容（信息时效：YYYY-MM，来源 URL）`

## Uncertainty

缺公开数据、口径冲突、或仅有 [C] / 单源 Critical Claim：标 **Uncertainty**，不得编造参数。该条不得单独作为 Hard Constraint「已满足」的依据。
