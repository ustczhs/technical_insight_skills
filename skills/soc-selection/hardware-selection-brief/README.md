# hardware-selection-brief

选型簇 **Phase 1**：通过 grilling 把产品概念收敛为 **Selection Brief**（纯 Markdown），供同簇 `soc-shortlist` 使用。

流程与规则以 [SKILL.md](./SKILL.md) 为准。术语：[../CONTEXT.md](../CONTEXT.md)。簇说明：[../README.md](../README.md)。

## 何时用

- 需要「会影响主控选型」的需求简报，而不是完整 PRD
- Companion Robot / Wearable AI 等 Product Family 的维度收敛
- 需要产出 Brief Ready，交给同簇 Phase 2

显式调用：`/hardware-selection-brief`（本 skill 默认 `disable-model-invocation`）。  
须已有（或当场最小建）`$PROJECTS_ROOT/<project_slug>/PROJECT.md`。

## 产出

```
$PROJECTS_ROOT/<project_slug>/selection/sources/           # Brief Source（可选输入）
$PROJECTS_ROOT/<project_slug>/selection/SELECTION_BRIEF.md
```

外部材料经抽取成为 Source-Derived Draft，须 Dimension Turn 确认后写入 Brief；文首 `brief_status` = `brief_ready` 后方可进入 Phase 2。

## 与同簇下一 skill

Brief Ready 后调用 `/soc-shortlist`，加载同一 Brief，产出 `SOC_SHORTLIST.md`。

## 关键依赖

- [../shared/brief-template.md](../shared/brief-template.md)
- [../shared/profiles/](../shared/profiles/)（Dimension Profile）

## 文档索引

- [SKILL.md](./SKILL.md)
- 选型术语：[../CONTEXT.md](../CONTEXT.md)
- 选型簇：[../README.md](../README.md)
- 包总览：[../../../README.md](../../../README.md)
