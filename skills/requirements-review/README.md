# requirements-review

需求澄清与价值评审：通过 grill，把模糊 **Requirement Seed** 相对 **Project Corpus** 收敛为 **Clarified Requirement**（含 **Delivery Sketch**：路线 / 触及面 / 人力 / 工期），再给出 **Value Verdict**（Do / Defer / Don't，须引用交付草图）。

流程与规则以 [SKILL.md](./SKILL.md) 为准。术语权威：[CONTEXT.md](./CONTEXT.md)。包公约：[../../CONTEXT.md](../../CONTEXT.md)。

## 何时用

- 需求表述模糊，需要对照 id card、功能清单等文档挖清边界与大概交付形状
- 需要可辩护的「做 / 暂缓 / 不做」价值结论（与开发量级对齐，而非纯价值空转）
- 显式调用：`/requirements-review`（本 skill 默认 `disable-model-invocation`）
- 须已有（或当场最小建）项目档案：`$PROJECTS_ROOT/<project_slug>/PROJECT.md`

## 产出

```
$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/
├── CLARIFIED_REQUIREMENT.md   # clarification_status: draft → ready（含 Delivery Sketch）
└── VALUE_VERDICT.md           # 须澄清 Ready 后定稿；强制引用草图
```

完成后回写该项目 `PROJECT.md` 需求索引行。Delivery Sketch **不是**独立第三文件。

## 目录结构

```
skills/requirements-review/
├── SKILL.md
├── README.md
├── CONTEXT.md
├── docs/adr/
│   └── 0001-delivery-sketch-in-clarification.md
└── shared/
    ├── grill-output.md              # grill 选择题输出格式
    ├── clarification-dimensions.md
    ├── value-dimensions.md
    ├── corpus-discovery.md
    ├── clarified-requirement-template.md
    └── value-verdict-template.md
```

Grill 对用户默认以**选择题**呈现（末项「其他 / 自定义」），见 [shared/grill-output.md](./shared/grill-output.md)。

## 文档索引

- [SKILL.md](./SKILL.md)
- [CONTEXT.md](./CONTEXT.md)
- [docs/adr/0001-delivery-sketch-in-clarification.md](./docs/adr/0001-delivery-sketch-in-clarification.md)
- [shared/grill-output.md](./shared/grill-output.md)
- [shared/](./shared/)
- 项目档案：[../project-dossier/README.md](../project-dossier/README.md)
- 包总览：[../../README.md](../../README.md)
