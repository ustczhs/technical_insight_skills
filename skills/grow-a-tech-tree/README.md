# grow-a-tech-tree

技术树生长：通过 grill 从产品/品类长出叶→枝→干→根（卡诺叶清单 + DAG），并同步 drawio / 预览图。

流程与规则以 [SKILL.md](./SKILL.md) 为准。术语权威：[CONTEXT.md](./CONTEXT.md)。包公约：[../../CONTEXT.md](../../CONTEXT.md)。

## 何时用

- 要从产品或品类「长技术树 / 找根技术 / 技术树拆解」
- 需要卡诺叶清单，再向下拆到可掌控的枝/干/根
- 显式调用：`/grow-a-tech-tree`（本 skill 默认 `disable-model-invocation`）
- 须已有（或当场最小建）`$PROJECTS_ROOT/<project_slug>/PROJECT.md`

## 产出

```
$PROJECTS_ROOT/<project_slug>/trees/
├── tech-tree.md
├── tech-tree.drawio
├── tech-tree.png
├── tech-tree.jpg
└── notes.md          # 可选
```

本地可自建 `examples/`（md + drawio）对照格式，与运行时 `$PROJECTS_ROOT/<project_slug>/trees/` 区分；该目录已 gitignore，**勿提交**含具体产品的技术树。

须已有（或当场最小建）`$PROJECTS_ROOT/<project_slug>/PROJECT.md`。

## 目录结构

```
skills/grow-a-tech-tree/
├── SKILL.md
├── README.md
├── CONTEXT.md          # 本 skill 领域术语
├── reference.md
├── refs/
├── examples/           # 本地私有，默认不入库
└── scripts/
```

## 可选依赖

结构图优先使用 drawio MCP。若环境未配置，启动时或首次导出前运行：

```bash
# 从本包根目录
./scripts/ensure-optional-deps.sh --only drawio
```

写入 `~/.cursor/mcp.json` 后可能需重启 Cursor / 重载 MCP。无 MCP 时仍可用本 skill 脚本生成 `.drawio` XML。

## 脚本

```bash
python3 skills/grow-a-tech-tree/scripts/sync_status_colors.py $PROJECTS_ROOT/<project_slug>/trees/tech-tree.drawio
python3 skills/grow-a-tech-tree/scripts/gen_tech_tree_drawio.py $PROJECTS_ROOT/<project_slug>/trees/tech-tree.md
```

（已 symlink 时把前缀换成 `.cursor/skills/grow-a-tech-tree/`。）

## 文档索引

- [SKILL.md](./SKILL.md)
- [CONTEXT.md](./CONTEXT.md)
- [reference.md](./reference.md)
- 包总览：[../../README.md](../../README.md)
