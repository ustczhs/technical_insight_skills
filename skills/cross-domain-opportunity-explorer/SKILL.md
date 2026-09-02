---
name: cross-domain-opportunity-explorer
description: >-
  AI/agent cross-domain collision engine for AI × smart-hardware × service/space
  opportunity sparks: Seed Triad → People Cells → constraint×form sparks →
  evidence → four-kill cards → shortlist → validation → Handoff Pack under
  $PROJECTS_ROOT/<project_slug>/opportunities/. Use only when invoked as
  /cross-domain-opportunity-explorer or for 跨域机会探索 / 机会火花 / 跨域碰撞 /
  人群需求探索 / AI智能硬件机会扫描; not for deep hardware research, PRD review,
  SoC selection, technical trees, or project-dossier CRUD alone.
disable-model-invocation: true
---

# cross-domain-opportunity-explorer

借助 **AI/Agent 的跨域碰撞**，从兴趣圈层、人生角色与身心状态场景中撞出 **Opportunity Spark**，再经结构化漏斗收敛为可证伪商业假设与下游交接包。

**四条操作原则**（覆盖、检索、挖掘、呈现 — 全程遵守）：

| # | 原则 | 落地 |
|---|------|------|
| 1 | **覆盖尽量广** | Seed/Cell/Spark 不设上限；Breadth Floor 是下限不是目标。薄记尽量多，深写靠漏斗。 |
| 2 | **检索充分时效** | 外部事实优先最近 12 个月；历史资料只作趋势对照并标时效局限。查询带年份；过期来源不得当现状。 |
| 3 | **挖掘要深、要敢想** | 碰撞走完旅程节点 × 非常规透镜 × 跨域类比；允许 wild。禁止「某人群 + AI 手环」空壳。 |
| 4 | **结果呈现要直接** | 对人先给 `SESSION_BRIEF`：结论、Top 火花、杀伤、下一步。细节进文件，不把 50 行表贴进对话。 |

其余理念：先撞火花再筛真伪；Pain 与 Itch 双轨；对人五闸门 Grill；止于 Handoff，不自动串下游。

术语：[CONTEXT.md](CONTEXT.md)。引擎：[shared/](shared/)。包公约：[../../CONTEXT.md](../../CONTEXT.md)。

## 硬规则

1. **只显式调用**；`landscape` 或 `deep-dive`。不得声称穷尽人群。
2. **Seed Triad 并行**交叉成 People Cell。用户若给出场景直觉，记为 **Seed Spark** 置顶，再反向扩池，不替代广筛。
3. **Breadth Floor（landscape 下限，鼓励超出）**：兴趣 ≥40、角色/阶段 ≥15、状态 ≥10；入选 Cell ≥40（目标 50–80）；去重后火花 ≥50（目标 ≥80）。未达下限不得宣称广筛完成；不得为凑数编造证据或假 URL。
4. **火花段不可跳过**。每入选 Cell ≥2 透镜碰撞。火花必须写**独特场景摩擦**（时间窗口 / 姿态 / 环境）；同一杀伤句在全板不得出现 ≥5 次。对照 [shared/killed-patterns.md](shared/killed-patterns.md)。
5. **证据预算 + 时效**：landscape 每 Cell ≤2 次检索、整批优先覆盖高约束节点；**仅 candidate/shortlist 加厚**（每条 ≥2 个带 URL 的 `fact` 或 `voice`，优先 ≤12 个月）。检索失败降级，不编造。无 `fact/voice` **不得 shortlist**。
6. **四杀伤 + Spark Score** 进 shortlist。晋升 candidate 须写 Spark Score（见 [shared/spark-collision.md](shared/spark-collision.md)）。candidate 中头戴/眼戴占比 ≤50%。
7. **三种介入形态**比较；手机可充分解决则不强造硬件。
8. **医疗边界**仅记录，不进 shortlist。
9. **Decision Grill**：逐步确认下正式跑闸门③④必问（资源、首验对象）；一次一题、选择题+推荐+「其他（请补充）」。**Lazy**：①–⑤全用推荐，不问。
10. **只写** `$PROJECTS_ROOT/<project_slug>/opportunities/`。禁止写入仓库相对 `opportunities/` 或工作区根级旧目录；发现只提示迁移，不双写。
11. 产物中文为主；对人输出套 [shared/session-brief.md](shared/session-brief.md)。只回写 `PROJECT.md` §4 `opportunities` 行及 `updated`。

## 项目闸门与续跑

1. 运行 `project-dossier/scripts/ensure-projects-root.sh`，确认 `project_slug`。
2. 无 `PROJECT.md` 则最小建档或引导 `/project-dossier`。
3. `LANDSCAPE.md` 写 `batch_id` 与 `stage`（0–7）。中断则从断点续，不整批重撞火花。
4. 已有 `opportunities/`：（单选）继续 / 修订 / 新开批次 / 其他（请补充）；不明则问，推荐继续。
5. **空柜第一题是闸门**（slug / 最小建档），不是 Lazy。闸门通过后，新批次或未完成且无 run_mode=lazy：问 Lazy（推荐关）。开则七段连跑，Decision Grill 全跳。格式见 [../project-dossier/shared/ask-and-lazy.md](../project-dossier/shared/ask-and-lazy.md)。

## 七段流程

启动读取 [shared/guided-workflow.md](shared/guided-workflow.md) 及 shared 模板。无冲突继承偏好，**不**问「然后呢」。

| 段 | 名称 | 主产物 | 要点 |
|----|------|--------|------|
| 0 | 项目与续跑 | `LANDSCAPE.md` 进度 | 闸门、`stage` |
| 1 | 探索章程 | `LANDSCAPE.md` | 范围、Seed Spark、原则 1–4 |
| 2 | 人群地图 | `SEED_CATALOG.md`、`PEOPLE_LANDSCAPE.md` | 尽量广 |
| 3 | 证据与痛痒 | `EVIDENCE_LOG.md`、`NEED_BACKLOG.md` | 预算内薄采；检索要新 |
| 4 | **火花碰撞** | `SPARK_BOARD.md` | 深挖+想象力；去重；Score |
| 5 | 概念与四杀伤 | `concepts/*/OPPORTUNITY_CARD.md` | ≤8 candidate |
| 6 | 组合筛选 | `PORTFOLIO_MATRIX.md`、`SHORTLIST.md` | ≤3；须 fact/voice |
| 7 | 验证与交接 | `VALIDATION_BRIEF.md`、`HANDOFF_PACK.md`、`HANDOFF_INDEX.md`、`SESSION_BRIEF.md` | 三维路由 |

`deep-dive`：1 Cell、3–5 场景；豁免数量下限，不豁免火花段与时效检索。火花 ≥15。

碰撞公式与晋升：[shared/spark-collision.md](shared/spark-collision.md)。

## 收尾

跑 [scripts/check-breadth.sh](scripts/check-breadth.sh)（能跑则跑）。对人只贴 `SESSION_BRIEF.md` 正文 + 产物根路径。

```text
$PROJECTS_ROOT/<project_slug>/opportunities/
├── LANDSCAPE.md
├── SESSION_BRIEF.md            ← 对人结论（直接呈现）
├── SEED_CATALOG.md
├── PEOPLE_LANDSCAPE.md
├── EVIDENCE_LOG.md
├── NEED_BACKLOG.md
├── SPARK_BOARD.md
├── PORTFOLIO_MATRIX.md
├── SHORTLIST.md
├── HANDOFF_INDEX.md
└── concepts/<concept_slug>/
    ├── OPPORTUNITY_CARD.md
    ├── VALIDATION_BRIEF.md
    └── HANDOFF_PACK.md
```
