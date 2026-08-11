---
name: hardware-insight
description: >-
  Research skill in the Technical Planning Skill Package: structured
  smart-hardware product research — competitor teardown, technical route
  analysis, market opportunity, and decision summary with reports via
  templates/report/. Optional infographics are a Step 8 side path only.
  Use when the user asks for hardware product research, competitor analysis,
  智能硬件调研, 竞品分析, or invokes hardware-insight / basic_flow.
---

# 智能硬件结构化调研

按 [basic_flow.md](basic_flow.md) 执行 Step 0–8。每次调研在 `research/<产品简称>/` 下产出文件。

## 启动

1. 创建或读取目录 `research/<产品简称>/`。
2. 读取 `research/<产品简称>/进度.md`（若存在）确定当前步骤；否则从 Step 0 开始。
3. 若 `调研基调.md` 存在且 `Step 0 状态：已确认` → **跳过 Step 0 问询**，从当前步骤续跑。
4. 否则执行 Step 0 意图发现（**必须**读取 [references/intent-discovery.md](references/intent-discovery.md)）。
5. 每步完成后更新 `进度.md`，再进入下一步。

## 信息时效（核心）

AI 硬件迭代快，Step 3–7 检索与引用**必须**遵守：

**检索策略**
- WebSearch 优先带 `2025`、`2026` 或时间限定
- 关键结论（价格、在售状态、规格、销量、准确率声称、技术路线、融资/发货）：主信源 **≤12 个月**
- 12–24 个月：须第二条近源交叉，标注 `信息时效：YYYY-MM`
- **>24 个月**：不得单独支撑现状判断；仅 >36 个月尽量避免用于现状

**例外（须显式标注）**

| 类型 | 标注 |
|------|------|
| 现状事实 | 默认，须近 12 月主信源 |
| 背景/趋势 | `信息时效：YYYY-MM` |
| T2 历史范式 | `历史参照，非现状` |
| 学术/方法论基线 | `学术基线` + 是否仍适用 |

**与证据分级联动**：超 24 个月的 [A] 源用于现状时降为 [B]，直至有近源印证。

**引用格式**：`[A/B/C] 内容（信息时效：YYYY-MM，来源 URL）`

## 全局规则

- **证据分级**：A（官方/拆解/认证库）> B（权威媒体/供应商）> C（二手信息）；关键结论需 ≥2 处独立来源，标注等级。
- **分析师立场**（Step 0 **必填**，**无默认组织**）：由用户自填身份；填「中立第三方」为中立模式，否则为第一方。第一方下竞品用威胁/机会/可借鉴框架，**建议方向主语必须为我方主体**。详见 [references/report-synthesis.md](references/report-synthesis.md)。
- **中文可读性**：对内可保留 Build/Buy/Partner、O1/M4 等坐标系；写入 brief、决策摘要核心结论、管理层材料时须白话。决策摘要文首宜设「对外口径」对照表。
- **交互闸门**：仅在 Step 0、Step 1、Step 2、Step 8 暂停等人确认；其余步骤自主推进。
- **回退**：审核不通过时，列出缺口并回退至对应步骤，不进入下一步。
- **状态**：Step 0 产出 `调研意图.md`（过程记录）+ `调研基调.md`（结构化结论）；**Step 1–8 只读 `调研基调.md`**，`调研意图.md` 仅供回顾与 Step 0 续跑。

## Step 0：定调（交互闸门）

执行前读取 [references/intent-discovery.md](references/intent-discovery.md)。产出双文件于 `research/<产品简称>/`。

| 子步 | 动作 | 产出 |
|------|------|------|
| **0a 语境扫描** | 读已有 `research/`、WebSearch 公开事实（不问用户） | `调研意图.md` 草稿 |
| **0b 澄清/压测** | agent 判断清晰度：模糊 → full grill（≤8 轮开放题）；清晰 → 简流程（1–3 轮）；含假设压测 | 交错更新两文件草稿 |
| **0c 结构化采集** | `AskQuestion` 收集基本参数（与开放题**分条消息**） | 更新 `调研基调.md` |
| **0d 定稿闸门** | 展示摘要；用户确认后设 `Step 0 状态：已确认` | 勾选进度检查点 |

**交互纪律**（详见 intent-discovery）：一次一题；事实 agent 自查、决策必问；结构化题带推荐+理由，开放决策题只问不推荐；共识前不进入 Step 1。

**`调研基调.md` 必含字段**：

- `调研议题`（一句决策命题）
- `核心决策问题`（3–5 条；Step 7 **不要求**逐条回应）
- `成功标准` / `明确不做`（可短）
- 基本参数表：调研目的、深度、范围、读者、硬件扩展包、必证项、**分析师立场（必填，无默认组织）**、我方主体（第一方必填）
- `竞品分层`（T0/T1/T2 + 分层依据；可 Step 2 再细化）
- `Step 0 状态`：`待确认` / `已确认`

**`调研意图.md`**：章节自由组织；简流程也产出薄版（至少含清晰度判断、扫描摘要、问答摘要）。

**跳过**：`调研基调.md` 已确认 → 整段 Step 0 问询跳过。

**续跑**：`Step 0 状态：待确认` → 读 `调研意图.md` 从最后未决分支续问，不重头。

**重做**：用户说「重做 Step 0」→ 重新生成双文件；旧项目仅有已确认基调、无 `调研意图.md` 时不强制补写。

## Step 1：制定调研模板（交互闸门）

- 输入：目标产品信息、`调研基调.md`
- 输出：`research/<产品简称>/调研模板.md`
- 按基调裁剪维度；启用硬件扩展包时追加：BOM/成本、供应链与量产、认证合规、专利/IP、可靠性售后
- 审核：维度 MECE、匹配调研目的
- **轻量 grill**（≤3 轮，见 [intent-discovery.md](references/intent-discovery.md) §E）：展示模板时给出 **推荐裁剪 + 1–2 替代方案**；单问确认维度取舍；不重复 Step 0 已确认项
- **闸门**：用户确认模板后进入 Step 2

## Step 2：调研竞品列表（交互闸门）

- 输入：目标产品信息、`调研基调.md`
- 输出：`research/<产品简称>/竞品列表.md`（T0/T1/T2、分层依据、直接/间接竞品）
- 审核：覆盖性与分层合理性
- **轻量 grill**（≤3 轮，见 [intent-discovery.md](references/intent-discovery.md) §F）：展示列表 + **T0 覆盖/错层挑战式单问**；不重复 Step 0 已确认项
- **闸门**：用户确认列表后进入 Step 3

## Step 3：填充竞品调研

- 输入：`竞品列表.md`、`调研模板.md`
- 输出：`research/<产品简称>/调研/` 下每竞品一文件，如 `调研/T0-品牌-型号.md`
- **结构**：每文件必须复制 `调研模板.md` 全部章节标题（13 节 + 扩展包节）
- **深度分层**（章节相同，深度不同）：
  - T0：全字段尽力填写，多源交叉
  - T1：全章节标准填充
  - T2：全章节浅扫，可大量「未知」/「不适用」
- **必填字段**：
  - T2：§1、§6、§12、§13
  - T1：T2 + §3–§5、§8–§11
  - T0：全部
- 审核：章节齐全、证据等级达标、**信息时效达标**、交叉校验完成；现状类仅 >24 月信源 → `待更新` 并入 §13

## Step 4：竞品分析

- 输入：结构化调研文件、`调研基调.md`
- 输出：`research/<产品简称>/竞品分析.md`（定位、价格、功能、体验、渠道、销量/口碑）
- 审核：对比维度匹配基调；结论有调研数据支撑；文首附 `调研信息截止：YYYY-MM-DD`；**每个 T0 ≥5 条可引用数据点；含「对我方主体影响」列**。详见 [references/report-synthesis.md](references/report-synthesis.md)
- **边界**：不写实现原理与技术路线（留给 Step 5）

## Step 5：技术分析

- 输入：结构化调研文件
- 输出：`research/<产品简称>/技术分析.md`（架构、核心器件/算法、技术路线、成熟度与优劣势；可检索开源/学术）
- 审核：技术结论属实；路线分析有独立来源交叉验证；文首附 `调研信息截止：YYYY-MM-DD`；**含架构图 + Build/Buy/Partner 三栏**。详见 [references/report-synthesis.md](references/report-synthesis.md)
- **边界**：不写市场表现对比（已在 Step 4）

## Step 6：商业机会分析

- 输入：调研文件、`竞品分析.md`、`技术分析.md`
- 输出：`research/<产品简称>/商业机会.md`（场景/用户、市场规模与趋势、机会与威胁、窗口期）
- 审核：市场判断准确；与 Step 4/5 交叉引用；文首附 `调研信息截止：YYYY-MM-DD`；**含量化字段与竞争响应时间表**。详见 [references/report-synthesis.md](references/report-synthesis.md)

## Step 7：决策综合

- 输入：`竞品分析.md`、`技术分析.md`、`商业机会.md`、`调研基调.md`
- **执行顺序**：先 `决策摘要.md`，再 `swot分析.md`
- 输出：
  - `research/<产品简称>/决策摘要.md`（核心结论、方案选项、主要风险、建议方向）
  - `research/<产品简称>/swot分析.md`（S/W/O/T 四象限 + SO/ST/WO/WT 2×2 策略矩阵；综合 Step 4–6，主语为我方主体）
- 审核：结论有调研支撑；回应 Step 0 调研目的；**建议方向主语为我方主体**；含 12/24 月里程碑、资源粗估、明确不做边界；SWOT 四象限与 2×2 矩阵达标。详见 [references/report-synthesis.md](references/report-synthesis.md)
- **边界**：SWOT 正文**不得**并入 `决策摘要.md`；Step 8 **不强制**读取 `swot分析.md`

## Step 8：调研输出（交互闸门）

**闸门**（一次 `AskQuestion`，两题）：
1. **报告取向**（`allow_multiple: true`）：决策导向 / 科普导向 / 投资人导向
2. **是否生成信息图**（单选）：生成 / 跳过 — 跳过则不再问 `信息图_style`；信息图仅作 `output/infographics/` 参考，**不嵌入**报告

若用户选择「生成」，追加第三题：
3. **信息图 style**（单选）：推荐 `pop-laboratory`；备选 `morandi-journal` / `corporate-memphis` / `craft-handmade`
4. **信息图 aspect**（单选，可选）：`landscape`（默认）/ `portrait` / `square`

写入 `调研基调.md`：`报告取向`、`生成信息图`（是/否）、`信息图_style`（若生成）、`信息图_aspect`（若生成，默认 landscape）。

| 取向 | 执行摘要侧重 | 正文加权 | 骨架模板 |
|------|-------------|----------|----------|
| 决策导向 | 方案选项 + 我方建议 | Step 7 决策综合 | `templates/report/报告-决策导向.md` |
| 科普导向 | 技术路线解释 + 对我方含义 | Step 5 技术分析 | `templates/report/报告-科普导向.md` |
| 投资人导向 | 市场窗口 + 风险 | Step 6 商业机会 | `templates/report/报告-投资人导向.md` |

### 信息图生成（可选）

仅当用户选择 **生成** 时执行：

1. 运行包根脚本确保依赖（缺则自动安装）：
   `bash <本包>/scripts/ensure-optional-deps.sh --only baoyu-infographic`
2. 读取 `~/.cursor/skills/baoyu-infographic/SKILL.md`（或脚本安装后的等价路径）
3. **必须**再读 [references/infographic-rules.md](references/infographic-rules.md) 与 [references/infographic-source-map.md](references/infographic-source-map.md)，按其中 Phase A→B→C 出 4 张参考 PNG（不嵌入报告）

若依赖安装失败或图像后端不可用：记入信息缺口，**跳过信息图**，仍完成报告 MD；不得用 HTML/SVG/表格脚本冒充信息图。

### 报告 MD

综合阅读清单见 [references/report-synthesis.md](references/report-synthesis.md)。

1. 读取 [`templates/report/报告-<取向>.md`](templates/report/) 骨架，复制章节结构
2. 按取向生成 `output/大纲-<取向>.md`（每节要点，**禁止**引用信息图路径）
3. 生成 `output/报告-<取向>.md`（**禁止** `![...](infographics/...)`；用表格 + mermaid 替代）
4. 多取向时先产共用 `决策摘要.md`，派生各报告，结论不得矛盾

### Step 8 完成前自检

见 [references/report-synthesis.md](references/report-synthesis.md) 质量闸门（报告必检；信息图仅在选择生成时检）。

## 进度文件格式

`research/<产品简称>/进度.md`：

```markdown
# 调研进度：<产品名>

- 当前步骤：Step N
- 上次更新：<日期>
- 状态：进行中 / 待确认 / 已完成

## 检查点
- [ Y ] Step 0 意图发现（`调研意图.md`）   <!-- 已完成：[ Y ] -->
- [ Y ] Step 0 基调确认（`调研基调.md`）
- [ Y ] Step 1 模板确认
- [ N ] Step 2 竞品列表确认                 <!-- 未完成：[ N ] -->
- [ N ] Step 3 调研填充
- [ N ] Step 4 竞品分析
- [ N ] Step 5 技术分析
- [ N ] Step 6 商业机会
- [ N ] Step 7 决策综合 + SWOT（`决策摘要.md` + `swot分析.md`）
- [ N ] Step 8 报告输出
```

**硬规则**：每完成一步，立即把对应检查点改为 `- [ Y ]`；未完成用 `- [ N ]`。状态为「已完成」时，全部检查点必须为 `[ Y ]`。
## 续跑与单步执行

- 用户说「继续调研」：读 `进度.md`；若 `Step 0 状态：待确认` → 读 `调研意图.md` 续问 Step 0，不重头；否则从当前步骤续跑。
- 用户指定步骤（如「只跑 Step 3」）：检查前置产出是否存在，缺失则提示先完成依赖步骤。
- 用户说「重做 Step 0」：重新生成 `调研意图.md` + `调研基调.md`（见 [intent-discovery.md](references/intent-discovery.md) §G）。
- 用户说「重做 Step 7」：保留 Step 0–6 产出，按 [report-synthesis.md](references/report-synthesis.md) 重生 `决策摘要.md` 与 `swot分析.md`。
- 用户说「重做 Step 8」：保留 Step 0–7 产出，按 [report-synthesis.md](references/report-synthesis.md) 与 `templates/report/` 重生成大纲/报告；若 `调研基调.md` 中 `生成信息图` 为是，另按 [infographic-rules.md](references/infographic-rules.md) 重生成信息图（先跑 `ensure-optional-deps.sh --only baoyu-infographic`）。

## 参考

- 流程速查：[basic_flow.md](basic_flow.md)（细则以本 SKILL 为准）
- 意图发现与问询：[references/intent-discovery.md](references/intent-discovery.md)
- 产出物模板：[reference.md](reference.md)
- 信息图规范：[references/infographic-rules.md](references/infographic-rules.md)
- 信息图数据源：[references/infographic-source-map.md](references/infographic-source-map.md)
- 报告合成：[references/report-synthesis.md](references/report-synthesis.md)
- 报告骨架模板：[templates/report/](templates/report/)
- 可选依赖安装：[../../scripts/ensure-optional-deps.sh](../../scripts/ensure-optional-deps.sh)
