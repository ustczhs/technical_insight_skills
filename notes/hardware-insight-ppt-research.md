# Hardware Insight 两页 PPT 研究笔记

> 目的：为“现状（以 hardware-insight 为主）/未来规划（Web 或数字员工）”两页 PPT 提供一手材料与可讲述结构。
> 研究日期：2026-09-07。除“规划推断”外均来自本仓库源文件。

## 可直接作为现状页的事实

### 1. 工程定位

- 本仓库是“技术规划 Skill 集合”，能力簇可独立调用，明确不是一条总流水线；各簇产物在同一项目档案下分目录隔离。[A] `README.md:1-5,13-24`; `CONTEXT.md:1-4,26-44`
- 当前列出 7 个可安装叶子 Skill：`project-dossier`、`hardware-insight`、`cross-domain-opportunity-explorer`、`hardware-selection-brief`、`soc-shortlist`、`grow-a-tech-tree`、`requirements-review`。[A] `README.md:26-36`
- `hardware-insight` 是当前唯一允许自动触发的 Skill；其余叶子默认需要显式调用。[A] `CONTEXT.md:61-69`

### 2. hardware-insight 能力边界

- 角色：智能硬件结构化调研，覆盖竞品拆解、技术路线、商业机会、决策报告；按 Step 0–8 执行。[A] `skills/hardware-insight/SKILL.md:1-14`; `skills/hardware-insight/README.md:1-7`
- 标准链路：Step 0 定调 → Step 1 调研模板 → Step 2 竞品分层 → Step 3 逐竞品调研 → Step 4 竞品分析 → Step 5 技术分析 → Step 6 商业机会 → Step 7 决策摘要 + SWOT → Step 8 大纲/报告输出。[A] `skills/hardware-insight/basic_flow.md:8-18`
- 主要产物位于 `$PROJECTS_ROOT/<project_slug>/research/`，包括 `调研基调.md`、`竞品列表.md`、逐竞品 `调研/`、`决策摘要.md`、`output/`。[A] `skills/hardware-insight/README.md:15-26`

### 3. 可信与可控机制

- 项目闸门：先解析 Projects Root、确认 `project_slug` 与 `PROJECT.md`，只写入项目的 `research/`，重要里程碑回写项目索引。[A] `skills/hardware-insight/SKILL.md:16-21`
- 默认逐步确认：一次一题、推荐选项；Step 0/1/2/8 是人机交互闸门。显式选择 Lazy 后，按推荐值自动跑完 Step 0–8。[A] `skills/hardware-insight/SKILL.md:23-31,56-64`
- 证据规则：关键结论使用近 12 个月主信源；12–24 个月需交叉验证；超过 24 个月不能单独支撑现状判断；证据按 A（官方/拆解/认证库）> B（权威媒体/供应商）> C（二手）分级，关键结论至少两处独立来源。[A] `skills/hardware-insight/SKILL.md:33-54,56-59`
- 可续跑：读取 `进度.md` 判断当前步骤，每步完成后更新检查点；已确认基调可跳过 Step 0 问询继续执行。[A] `skills/hardware-insight/SKILL.md:23-31,202-230`

## 当前交付形态与缺口

- 活跃流程明确产出 Markdown 大纲和报告，支持决策/科普/投资人三种取向；报告必须综合底层调研文件，而不是只压缩 `决策摘要.md`。[A] `skills/hardware-insight/SKILL.md:158-176,189-196`; `skills/hardware-insight/references/report-synthesis.md:97-143`
- 信息图是可选侧路径，不阻塞主报告，也不嵌入报告。[A] `skills/hardware-insight/SKILL.md:178-187`; `skills/hardware-insight/README.md:40-47`
- 原 HTML 幻灯片产物与构建链已在 2026-08 从活 Skill 路径归档，避免误跑；恢复需把相关资源移回并重新挂接 Step 8。[A] `archive/hardware-insight-deck/README.md:1-19`; `archive/hardware-insight-deck/references/html-deck-spec.md:1-12`
- 因此，仓库现状可准确描述为“文件型、证据驱动的研究工作台”，而不是已有 Web 产品、API 或数字员工。仓库未发现 Web/API/数字员工实现（此句为本次文件扫描结果，不是产品能力声明）。

## 两页 PPT 建议叙事（规划推断，非现有事实）

### 第 1 页｜现状：从问题到决策的硬件洞察工作台

**主结论**：把分散的硬件信息，经过可控流程和证据闸门，沉淀为可执行的技术与产品决策。

**画面建议**：中间画 0→8 的横向链路；下方三张能力卡：

1. 结构化：竞品 / 技术 / 商业三条分析线汇聚决策摘要。
2. 可控：Project Dossier Gate、逐步确认 / Lazy 双模式、`进度.md` 续跑。
3. 可信：A/B/C 证据分级、时效要求、关键结论双源交叉。

**页脚落点**：输出决策摘要、SWOT、路线图与多取向报告，路径可追溯到项目档案。

### 第 2 页｜未来：从文件型 Skill 到 Web / 数字员工

**主结论**：保留证据与闸门，把“调用一次、读一组文件”升级为“持续可运营的研究服务”。

**建议分三阶段表达**：

- **阶段 1：Web 工作台（MVP）**：项目/课题看板；Step 0–8 状态可视化；竞品、技术、商业卡片联动；一键生成报告与浏览器汇报页。优先承接已归档的 HTML deck 能力（规划推断）。
- **阶段 2：数字员工**：自然语言入口；自动识别课题并绑定 `project_slug`；按风险触发一次一题确认，低风险任务可启用 Lazy；主动提醒过期证据、待证事项与里程碑。
- **阶段 3：组织化运营**：权限/审计、来源与时间戳、模板版本、反馈闭环；跨项目复用竞品和技术知识，但保持能力簇边界（规划推断）。

**必须继承的底层原则**：Project Dossier Gate、来源分级与时效、人工闸门、可续跑状态；Web/数字员工是交互与编排层，不应绕过这些质量约束（规划推断）。

## 飞书 / lark-cli 访问记录

- 用户提供页面：`https://tcl-eaglelab.feishu.cn/wiki/Np1tw2aBzifed6k9hcgck30KnAg`
- 本环境未发现 `lark-cli` 或 `lark` 可执行文件；仅存在桌面客户端命令 `bytedance-feishu`，无法以 CLI 读取该 Wiki。
- 本笔记未使用未经验证的飞书内容；如后续提供可用 lark-cli、登录态或导出 Markdown，应将其作为独立来源补充，并标注来源与访问日期。

## 证据说明

- `[A]` 表示仓库一手规范/源文件；本笔记中的规划阶段、Web/数字员工形态均为基于现状缺口的提案，不能回写为当前已实现能力。
