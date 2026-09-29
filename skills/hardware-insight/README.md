# hardware-insight

智能硬件结构化调研：竞品拆解、技术路线、商业机会与决策报告（Step 0–8）。

先过项目闸门（slug / `PROJECT.md`），再问分析师立场（推荐 **TCL 技术规划师**），然后问是否 **Lazy**（推荐默认关）。关则逐步确认：一次一题、选择题带推荐、末项「其他」。开则保留已确认立场，用推荐值连跑到报告（默认决策导向、不出信息图）。第一方还会写 `五看三定.md`；第一方且 Lazy 时同时出 `output/报告-五看三定.md`。中立不出五看三定。空柜第一题不是立场，也不是 Lazy。

流程细则以 [SKILL.md](./SKILL.md) 为准；[basic_flow.md](./basic_flow.md) 仅为步骤速查。包公约：[../../CONTEXT.md](../../CONTEXT.md)。

## 何时用

- 需要对某一产品/方向做结构化智能硬件调研
- 竞品分层、技术路线、商业机会、决策摘要、五看三定与报告
- 显式调用：`/hardware-insight` 或 `basic_flow`（允许按 description 自动触发；见包公约）

## 产出

```
$PROJECTS_ROOT/<project_slug>/research/
├── 调研基调.md
├── 竞品列表.md
├── 调研/
├── 决策摘要.md
├── swot分析.md
├── 五看三定.md          # 仅第一方
└── output/
```

须已有（或当场最小建）`$PROJECTS_ROOT/<project_slug>/PROJECT.md`。

## 目录结构

```
skills/hardware-insight/
├── SKILL.md
├── CONTEXT.md
├── README.md
├── basic_flow.md          # 步骤速查（非细则权威）
├── reference.md           # 字段/产出模板
├── references/
└── templates/report/
```

## 可选依赖

| 功能 | 依赖 | 安装 |
|------|------|------|
| 基础调研 Step 0–7 / 报告 MD | 无 | 安装本 skill 即可 |
| Step 8 信息图 | baoyu-infographic | Agent/脚本自动：`scripts/ensure-optional-deps.sh --only baoyu-infographic` |

信息图为可选侧路径；未装或安装失败时跳过信息图，仍交付报告。

## 文档索引

- [SKILL.md](./SKILL.md)
- [basic_flow.md](./basic_flow.md)
- [templates/report/](./templates/report/)
- 包总览：[../../README.md](../../README.md)
