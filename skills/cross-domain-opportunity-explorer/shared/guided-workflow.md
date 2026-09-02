# 引导式自动工作流

连续推进七段，禁止段末问「然后呢」。对人简报用 [session-brief.md](session-brief.md) 压缩版。Decision Grill 格式见 [grill-output.md](grill-output.md)。

## 进度机

`LANDSCAPE.md` 必有：

| 字段 | 值 |
|------|-----|
| batch_id | 如 `2026-08-18-landscape` |
| stage | `0` … `7` 或 `done` |
| run_mode | `formal` / `demo` / `lazy` |

中断从当前 `stage` 续跑：已有 Spark Board 则扩写/去重，不整表重生成。

## 七段 × 闸门

| 段 | 名称 | 自动完成 | 提问 | 产物 |
|----|------|----------|------|------|
| 0 | 项目与续跑 | 闸门、读产物、禁写仓库相对 `opportunities/` | slug / 续跑不明 | 进度 |
| 1 | 章程 | 原则 1–4、Breadth、Seed Spark | 闸门① 范围冲突 | `LANDSCAPE.md` |
| 2 | 人群地图 | Seed Triad，尽量广 | 闸门② 排除轴 | `SEED_CATALOG`、`PEOPLE_LANDSCAPE` |
| 3 | 证据与痛痒 | **预算内**薄采；检索要新 | 医疗/隐私边界 | `EVIDENCE_LOG`、`NEED_BACKLOG` |
| 4 | 火花碰撞 | 深挖+类比+去重；目标 ≥80 | 一般不问 | `SPARK_BOARD` |
| 5 | 四杀伤 | Score 晋升 ≤8；形态多样性 | 形态偏好会改排序时 | `OPPORTUNITY_CARD` |
| 6 | 筛选 | 矩阵；shortlist ≤3 且有 fact/voice | **闸门③ 必问**（`demo` 可默认 2 条并行） | `PORTFOLIO_MATRIX`、`SHORTLIST` |
| 7 | 验证交接 | brief + handoff + `SESSION_BRIEF` | **闸门④ 必问**；⑤ 有默认路由仍问一次 | 验证与交接 |

`demo` / 用户说「自动跑一轮」：**视为开 Lazy**（见 [ask-and-lazy.md](../../project-dossier/shared/ask-and-lazy.md)）——闸门①–⑤全部用推荐值，不等人；`SESSION_BRIEF` 写明「Lazy 默认，可改」。

`lazy` 与 `demo`：`lazy` 跳过全部 Decision Grill；旧 `demo` 口径并入 Lazy。

## 默认

- 已表达大陆+海外、Pain+Itch、形态全开、尽量广 → 不重复问。
- 有 Seed Spark → 置顶并仍执行广筛。
- 检索失败 → 缺口 + 低置信，继续；不拿过期来源冒充新事实。
- 每段落盘后先 5–8 行简报，再下一段。

## deep-dive

1 Cell、3–5 场景；豁免 Breadth Floor；火花 ≥15；检索时效与 Unique Friction 不豁免。
