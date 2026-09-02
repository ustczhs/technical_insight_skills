# PROJECT.md Template

路径：`$PROJECTS_ROOT/<project_slug>/PROJECT.md`  
纯 Markdown。可随研发推进增删查改。

# \<项目显示名\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| project_slug | |
| display_name | |
| status | active |
| created | YYYY-MM-DD |
| updated | YYYY-MM-DD |

`status`：`active` \| `parked` \| `done`

## 1. 项目简介

\<3–10 句：做什么、给谁、当前阶段。随推进更新。\>

## 2. Corpus

| 路径 | 类型 | 备注 |
|------|------|------|
| [./corpus/…](./corpus/) | id card / 功能清单 / 其他 | |

空柜时注明「暂无；分析将降级或待补」。

## 3. 需求索引

| req_slug | 标题 | clarification | verdict | 路径 |
|----------|------|---------------|---------|------|
| | | draft / ready / — | Do / Defer / Don't / — | [./requirements/…](./requirements/) |

## 4. 产物索引

| 簇 | 状态 | 入口 |
|----|------|------|
| research | 无 / 进行中 / 有产物 | [./research/](./research/) |
| opportunities | 无 / 进行中 / 有产物 | [./opportunities/](./opportunities/) |
| trees | 无 / 进行中 / 有产物 | [./trees/](./trees/) |
| selection | 无 / 进行中 / 有产物 | [./selection/](./selection/) |

## 5. 待决（可选）

| 项 | 状态 | 说明 |
|----|------|------|
| | open / resolved | |
