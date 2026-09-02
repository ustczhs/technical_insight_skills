# 项目闸门与索引回写（分析叶子共用）

各分析 skill（`hardware-insight`、`cross-domain-opportunity-explorer`、`hardware-selection-brief`、`soc-shortlist`、`grow-a-tech-tree`、`requirements-review`）启动与收尾须遵守本节。权威布局见 [project-layout.md](project-layout.md)。Projects Root 见 [projects-root.md](projects-root.md)。

## 启动闸门

1. **解析 Projects Root**：运行 `project-dossier/scripts/ensure-projects-root.sh`（或按 projects-root.md 同等步骤），得到 `PROJECTS_ROOT`；会话内导出 `PROJECTS_PATHS` / `PROJECTS_PATH`。
2. 确认 **project_slug**（推荐答案：从用户表述 / 已有 `$PROJECTS_ROOT/*` 推断）。
3. 检查 `$PROJECTS_ROOT/<project_slug>/PROJECT.md`：
   - **存在** → 读入简介与 Corpus 指针，继续本 skill。
   - **不存在** → 说明须先建档；**推荐**按 [PROJECT-template.md](PROJECT-template.md) 做**最小建档**（元信息 + 一句话简介 + 空表），或请用户改走 `/project-dossier`。逐步确认：用选择题等人确认后写入。**Lazy（分析叶子）**：采用推荐最小建档，不暂停。
4. **只写入** `$PROJECTS_ROOT/<project_slug>/` 下本簇子目录；发现工作区相对 `projects/`、仓库根级旧 `research/` / `opportunities/` 等有同名产物时**提示**迁移，不自动搬家、不双写。
5. 问询形态与 Lazy：见 [ask-and-lazy.md](ask-and-lazy.md)。分析叶子在闸门通过后、业务 Grill 前问 Lazy（推荐关）。`project-dossier` 不提供 Lazy 连跑。

## 索引回写（允许改动的 PROJECT.md 范围）

| 谁 | 可更新 | 不可更新 |
|----|--------|----------|
| 分析叶子 | §3 需求索引相关行；§4 产物索引中本簇一行；`updated` 日期 | 简介正文、status、§2 Corpus 列表、删除需求行、改 project_slug |
| `project-dossier` | 全部章节；Corpus CRUD；需求登记/删除；status；**sync** 扫描重建索引 | — |

`requirements-review`：登记或更新 §3 对应 `req_slug` 行（clarification / verdict 状态与路径）。  
`hardware-insight` / `cross-domain-opportunity-explorer` / `grow-a-tech-tree` / 选型叶子：更新 §4 中本簇状态与入口。

## 非目标

- 分析 skill **不**自动调用其他分析簇。
- **不**把 PROJECT.md 写成总 PRD 或报告合集。
