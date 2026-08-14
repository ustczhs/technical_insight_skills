---
name: project-dossier
description: >-
  Project archive skill in the Technical Planning Skill Package: create and
  maintain a Project Dossier under $PROJECTS_ROOT/<project_slug>/ (PROJECT.md MOC,
  corpus cabinet, requirement index, artifact index). Resolves/creates/persists
  Projects Root via PROJECTS_PATHS or PROJECTS_PATH. Obsidian-friendly markdown.
  Use when the user invokes project-dossier, /project-dossier, or asks for
  项目档案 / 建项目档案 / 更新项目档案 / 登记需求 / 项目资料 CRUD — not for running
  research, SoC selection, tech-tree, or requirements grilling themselves.
disable-model-invocation: true
---

# project-dossier

维护 **Project Dossier**：`$PROJECTS_ROOT/<project_slug>/` 下的活档案（增删查改）。  
不串跑调研/选型/技术树/需求评审；那些叶子自行写入分目录，并按约定回写索引。

术语：[CONTEXT.md](CONTEXT.md)。  
Projects Root：[shared/projects-root.md](shared/projects-root.md)。  
布局与闸门：[shared/project-layout.md](shared/project-layout.md)、[shared/project-gate.md](shared/project-gate.md)。  
扉页模板：[shared/PROJECT-template.md](shared/PROJECT-template.md)。

## 硬规则

1. **每次会话先解析 Projects Root**（见下）；档案只写在该根下，不写到当前 git 工作区相对 `projects/`。
2. **一次一个决策**，带推荐答案；关键动作（建档、删需求、改 status、sync 覆盖索引）单独确认。
3. 档案是**活的**：允许对简介、Corpus、需求登记、状态做 CRUD；用 `updated` 反映变更。
4. **Obsidian 友好**：`PROJECT.md` 当 MOC；链接以相对路径为主；`[[wikilink]]` 可选不强制；不依赖插件。
5. 能查到的目录/文件自己查；**决策权在用户**（路径解析/建目录/固化按公约自动执行，并告知用户）。
6. 不自动调用其他簇 skill；可口头建议用户另启。

## Step 0 — 解析 / 创建 / 固化 Projects Root（必做）

在任何 `create` / `show` / CRUD 之前：

1. 运行：
   ```bash
   bash <本 skill>/scripts/ensure-projects-root.sh
   ```
   （若 symlink 安装：`.cursor/skills/project-dossier/scripts/ensure-projects-root.sh` 或包内绝对路径。）
2. 以脚本打印的 `PROJECTS_ROOT=…` 为准；会话内同时：
   ```bash
   export PROJECTS_PATHS="$PROJECTS_ROOT"
   export PROJECTS_PATH="$PROJECTS_ROOT"
   ```
3. 向用户确认一句：本机项目档案根为该路径（若刚 `mkdir` 或刚写入 rc/config，一并说明）。

解析优先级与固化细节见 [shared/projects-root.md](shared/projects-root.md)。  
兼容环境变量名：`PROJECTS_PATHS`（首选）与 `PROJECTS_PATH`（同义）。

## 动作（会话中选一主动作推进）

| 动作 | 做什么 |
|------|--------|
| `create` | 新建 `$PROJECTS_ROOT/<project_slug>/` + `PROJECT.md` + 空 `corpus/` 等目录 |
| `update-meta` | 改显示名、简介、status（active/parked/done） |
| `corpus-add` / `corpus-remove` | 增删 `corpus/` 文件或列表行（移入/移出须用户确认） |
| `req-register` / `req-remove` | 登记或移除需求索引行；remove 时询问是否同时删 `requirements/<req_slug>/` |
| `sync` | 扫描分目录，重建 §3/§4 索引（展示 diff，确认后写入） |
| `show` | 只读汇总档案现状 |
| `ensure-root` | 仅重跑 Step 0（换机器 / 改路径后） |

## 流程摘要

### create

1. 完成 Step 0。  
2. 推荐 `project_slug` 与显示名 → 用户确认。  
3. 若 `$PROJECTS_ROOT/<project_slug>/` 已存在：改为 update / sync，勿覆盖。  
4. 按模板写 `PROJECT.md`；创建 `corpus/`、`requirements/`、`research/`、`trees/`、`selection/sources/`。  
5. 可选：用户指定初始 Corpus 文件，复制或链接进 `corpus/` 并登记。

### 其他动作

先 Step 0；按上表执行；每次写盘后更新 `updated`。删改前简述影响并确认。

## 产出

```
$PROJECTS_ROOT/<project_slug>/PROJECT.md
$PROJECTS_ROOT/<project_slug>/corpus/…
```

（分目录可由本 skill 建空壳；分析内容由其他叶子写入。）
