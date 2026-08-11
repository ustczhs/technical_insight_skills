# soc-shortlist

选型簇 **Phase 2**：读取 **Brief Ready** 的 Selection Brief，按第一性原理检索与过滤，产出 **SoC Shortlist**（必要时含 **Near-Miss**）。

完整筛选要求同簇上游 Brief 已 Ready。流程与规则以 [SKILL.md](./SKILL.md) 为准。术语：[../CONTEXT.md](../CONTEXT.md)。簇说明：[../README.md](../README.md)。

## 何时用

- 已有 Brief Ready 的 `SELECTION_BRIEF.md`，需要候选主控清单
- 需要按需做 Spec Detail Probe / Uncertainty 追问后再导出
- Companion Robot / Wearable AI 等族的相邻类覆盖检索

显式调用：`/soc-shortlist`（本 skill 默认 `disable-model-invocation`）。

## 产出

```
selection/<slug>/SOC_SHORTLIST.md
```

（Brief 通常同目录：`SELECTION_BRIEF.md`。）

## 与同簇上一 skill

若 `brief_status` ≠ `brief_ready`，应拒绝完整 Phase 2，并提示回 `/hardware-selection-brief`。

## 关键依赖

- [../shared/shortlist-template.md](../shared/shortlist-template.md)
- [../shared/evidence-rules.md](../shared/evidence-rules.md)
- [../shared/phase2-spec-probes.md](../shared/phase2-spec-probes.md)

## 文档索引

- [SKILL.md](./SKILL.md)
- 选型术语：[../CONTEXT.md](../CONTEXT.md)
- 选型簇：[../README.md](../README.md)
- 包总览：[../../../README.md](../../../README.md)
