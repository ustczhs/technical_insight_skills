# Project Dossier 目录布局

唯一写入根：`$PROJECTS_ROOT/<project_slug>/`  
（`PROJECTS_ROOT` 由 [projects-root.md](projects-root.md) 解析/创建/固化，通常来自 `$PROJECTS_PATHS` 或 `$PROJECTS_PATH`。）

```
$PROJECTS_ROOT/<project_slug>/
├── PROJECT.md                 # 扉页 / MOC
├── corpus/                    # 项目说明材料柜
│   └── …                      # id card、功能清单等（用户维护）
├── requirements/
│   └── <req_slug>/
│       ├── CLARIFIED_REQUIREMENT.md
│       └── VALUE_VERDICT.md
├── research/                  # hardware-insight 产出（不再套一层产品简称）
├── opportunities/             # cross-domain-opportunity-explorer 产出
├── trees/                     # grow-a-tech-tree 产出
└── selection/                 # soc-selection 产出（含 sources/）
    └── sources/               # 可选 Brief Source
```

## 链接约定（Obsidian 友好）

- 扉页与索引优先使用**相对路径** Markdown 链接，例如 `[CLARIFIED](./requirements/foo/CLARIFIED_REQUIREMENT.md)`。
- `[[wikilink]]` 鼓励可选，**不强制**；skill 正确性不依赖 Obsidian 插件。
- 可用 Obsidian 打开 `$PROJECTS_ROOT`（或单个项目子树）浏览；不用亦可。

## 废弃写入目标

以下路径**不再作为新写入目标**（若存在，只提示用户迁移/指定归属，不自动搬家）：

- 当前代码工作区下的相对 `projects/`
- 仓库根级平铺：`research/`、`opportunities/`、`selection/`、`trees/`、`requirements/`
