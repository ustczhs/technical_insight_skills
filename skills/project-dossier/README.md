# project-dossier

项目档案：在 **Projects Root**（`$PROJECTS_PATHS` / `$PROJECTS_PATH`）下建档并维护活档案（`PROJECT.md` MOC、Corpus、需求/产物索引）。缺失根目录时自动创建并固化。Obsidian 友好，不依赖插件。

流程以 [SKILL.md](./SKILL.md) 为准。术语：[CONTEXT.md](./CONTEXT.md)。包公约：[../../CONTEXT.md](../../CONTEXT.md)。

## 何时用

- 新建或更新项目档案、登记/删除需求、维护 Corpus、sync 索引
- 换机器后需要确保 Projects Root 存在并写入环境变量
- 显式调用：`/project-dossier`（默认 `disable-model-invocation`）
- 分析 skill 发现尚无 `PROJECT.md` 时，可按同一模板**最小建档**（见 shared/project-gate.md）

## Projects Root

```bash
bash skills/project-dossier/scripts/ensure-projects-root.sh
# 或：.cursor/skills/project-dossier/scripts/ensure-projects-root.sh
```

优先级：`PROJECTS_PATHS` → `PROJECTS_PATH` → `~/.config/technical-insight-skills/projects_root` → `$HOME/projects`。  
详见 [shared/projects-root.md](./shared/projects-root.md)。

## 产出

```
$PROJECTS_ROOT/<project_slug>/
├── PROJECT.md
├── corpus/
├── requirements/<req_slug>/
├── research/
├── opportunities/
├── trees/
└── selection/
```

## 目录结构

```
skills/project-dossier/
├── SKILL.md
├── README.md
├── CONTEXT.md
├── scripts/ensure-projects-root.sh
└── shared/
    ├── projects-root.md
    ├── project-layout.md
    ├── project-gate.md
    └── PROJECT-template.md
```

## 文档索引

- [SKILL.md](./SKILL.md)
- [CONTEXT.md](./CONTEXT.md)
- [shared/](./shared/)
- 包总览：[../../README.md](../../README.md)
