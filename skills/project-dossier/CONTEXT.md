# project-dossier

项目档案（Project Dossier）的领域术语。包公约见仓库根 [CONTEXT.md](../../CONTEXT.md)。本 skill **不**替代调研/选型/技术树/需求评审；只负责建档、活档案 CRUD、索引与归属。

## Language

**Project Dossier**:
某一 `project_slug` 下的完整项目档案目录（`$PROJECTS_ROOT/<project_slug>/`），含扉页、Corpus 柜与各能力簇分目录产物。
_Avoid_: 把四个分析簇焊成一条流水线, 无项目归属的平铺产物根（已废弃作为写入目标）, 写到当前代码仓相对 `projects/`

**Projects Root**:
本机存放全部项目档案的固定父目录。由环境变量 `PROJECTS_PATHS`（或兼容名 `PROJECTS_PATH`）、配置文件或默认 `$HOME/projects` 解析；缺失则创建并固化。详见 [shared/projects-root.md](shared/projects-root.md)。
_Avoid_: 每个仓库各自一套互不相通的相对 projects/

**PROJECT.md**:
档案扉页（MOC）：元信息、简介、Corpus 列表、需求索引、产物索引；可随研发推进增删查改。分析正文不内联于此。
_Avoid_: 把调研报告/技术树全文粘进扉页

**project_slug**:
项目稳定标识（英文或拼音），同时是 Projects Root 下的目录名。
_Avoid_: 与单条需求 slug 混用

**req_slug**:
项目内单条需求的标识；路径为 `requirements/<req_slug>/`。一个项目可有多条需求。
_Avoid_: 用 project_slug 代替需求目录名

**Corpus Cabinet**:
`corpus/` 目录及 PROJECT.md 中的 Corpus 列表；存放 id card、功能清单等说明材料。纳入权威仍须用户确认。
_Avoid_: 把代码仓库整棵树当作 Corpus

**Index Write-back**:
分析叶子在写入本簇产物后，仅更新 PROJECT.md 中约定的「需求索引 / 产物索引」行；不得擅自改简介、状态、Corpus 列表。
_Avoid_: 分析 skill 重写整份 PROJECT.md
