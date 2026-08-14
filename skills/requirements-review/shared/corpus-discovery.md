# Project Corpus 发现（提示性，非硬闸门）

## 流程

1. **优先**读取 `$PROJECTS_ROOT/<project_slug>/corpus/` 与 `PROJECT.md` §2 已登记项 → 列为候选。
2. 若用户已给出路径/文件列表 → 一并列入，请用户确认纳入/排除。
3. 若仍不足 → 在工作区做**轻量**搜索，列出候选（路径 + 一句话为何像 Corpus），请用户确认。
4. **未确认的文件不得当作权威 Corpus** 写入产物。
5. 零命中或用户清空 → 允许降级开跑（见 SKILL：Unknown + low confidence）。
6. 向用户确认纳入/排除时用**选择题**（见 [grill-output.md](grill-output.md)）：例如「A. 纳入推荐集合（推荐）」「B. 仅功能清单」「C. 空 Corpus 降级」「D. 其他 / 自定义：请列出路径」。

## 默认提示性 glob（可增删，不必全命中）

```
$PROJECTS_ROOT/<project_slug>/corpus/**
**/*id*card*
**/*ID*Card*
**/*功能*清单*
**/*feature*list*
**/PRD*
**/prd*
**/*需求*
**/*product*brief*
docs/**/*.{md,txt,docx}
**/README.md
```

不要递归扫 `node_modules/`、`.git/`、大型二进制目录。候选过多时先按路径相关性截断（例如最多展示 20 条），请用户点名纳入。

## 写入产物

在 `CLARIFIED_REQUIREMENT.md` 的 Corpus 表中记录：

| 路径 | 类型（id card / 功能清单 / 其他） | 纳入 | 备注 |
|------|-----------------------------------|------|------|
