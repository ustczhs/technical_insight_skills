# 信息图生成规范（hardware-insight Step 8）

本文件约束 Step 8 **可选**信息图产出，与 [baoyu-infographic](https://github.com/JimLiu/baoyu-skills) 配合使用。**hardware-insight 侧规则优先于 baoyu 默认出图习惯。**

生成前：

1. 运行包根 `scripts/ensure-optional-deps.sh --only baoyu-infographic`（缺则自动安装到 `~/.cursor/skills/baoyu-infographic`）
2. 读取已安装的 baoyu-infographic `SKILL.md`
3. 再读 [infographic-source-map.md](infographic-source-map.md)

信息图仅作 `output/infographics/` 参考素材，**禁止**嵌入最终报告。

---

## 目录与命名

```
$PROJECTS_ROOT/<project_slug>/research/output/infographics/
├── _style-lock.md
├── _manifest.md
├── competitors/
│   ├── refs/                    # 可选：官方产品素材
│   ├── source.md
│   ├── analysis.md
│   ├── structured-content.md
│   ├── data-manifest.md         # 必填：关键事实 + MustAppear 核对清单
│   ├── prompts/
│   │   └── infographic.md       # 必填：完整出图 prompt（可复现）
│   └── infographic-competitors.png
├── analysis/
├── tech/
└── market/
```

| type | layout | 输出 PNG | 渲染后端 |
|------|--------|----------|----------|
| competitors | comparison-matrix | `infographic-competitors.png` | **imagegen** |
| analysis | binary-comparison | `infographic-analysis.png` | **imagegen** |
| tech | linear-progression | `infographic-tech.png` | **imagegen** |
| market | bridge | `infographic-market.png` | **imagegen** |

**禁止**使用裸名 `infographic.png` 作为最终交付文件名（须为 `infographic-<type>.png`）。

---

## 生成顺序（硬规则）

**禁止并行**生成 4 张图。顺序：

1. `competitors` → 写入 `_style-lock.md`
2. `analysis`
3. `tech`
4. `market`
5. 全部通过 agent 自验后写 `_manifest.md`

每张图：写 prompt → 出图 → agent 自验 → 不通过则修正 prompt 重生成（**最多 2 次重试**）→ 下一 type。

---

## Phase A：内容整合（每张图必做）

按 [infographic-source-map.md](infographic-source-map.md) 执行：

| 步骤 | 产出 | 要求 |
|------|------|------|
| A1 | `source.md` | verbatim 摘录，≥30 行；含证据等级与时效 |
| A2 | `analysis.md` | 主旨锚定三段 + baoyu 六维（类型/目标/受众/复杂度/视觉机会/设计约束） |
| A3 | `structured-content.md` | Overview、Learning Objectives、分 Section（Key Concept / Content / Visual / Text Labels） |
| A4 | `data-manifest.md` | 关键事实 + **MustAppear** 核对清单（见下文） |

`analysis.md` 模板见 baoyu `references/analysis-framework.md`；`structured-content.md` 见 `references/structured-content-template.md`。

---

## Phase B：baoyu 出图（唯一主路径）

**必须**读取并遵循 baoyu-infographic SKILL 全文，尤其是 Image Generation Tools 解析顺序与禁止 SVG/HTML 交付规则。

### B1 布局与风格

| type | layout（固定） | style（来自 `调研基调.md`） | aspect（默认 landscape） |
|------|----------------|----------------------------|--------------------------|
| competitors | `comparison-matrix` | `信息图_style` | `信息图_aspect` 或 16:9 |
| analysis | `binary-comparison` | 同上，与 `_style-lock.md` 一致 | 同上 |
| tech | `linear-progression` | 同上 | 同上 |
| market | `bridge` | 同上 | 同上 |

Step 8 用户已选 `信息图_style`（及可选 aspect）→ 视为 baoyu Step 4 已确认，**无需每张图再问**。

### B2 写 prompt → `prompts/infographic.md`

按 baoyu Step 5 组合：

1. `references/layouts/<layout>.md` 布局定义
2. `references/styles/<信息图_style>.md` 风格定义
3. `references/base-prompt.md` 基础模板
4. `structured-content.md` 全文（数据 verbatim，禁止改写数字）
5. 课题专名、证据等级标注要求
6. 无 `refs/` 官方素材时：prompt 含 `NO_PRODUCT_PHOTOS`（禁止臆造产品实拍）

**备份规则**：若 `prompts/infographic.md` 已存在，重命名为 `infographic-backup-YYYYMMDD-HHMMSS.md` 后再写新版。

### B3 调用图像后端 → `infographic-<type>.png`

按 baoyu Image Generation Tools **解析顺序**：

1. 运行时 native `imagegen` skill（若可用）
2. `baoyu-image-gen`
3. Cursor `GenerateImage`（等效后备）
4. 均不可用 → 写入该图 `data-manifest.md` 底部「信息缺口：图像后端不可用」，**不得**用 HTML/SVG/表格脚本替代

**禁止**：

- 用 SVG/HTML 作为最终交付物
- 在已生成位图上 overlay 改字（须修正 prompt 后重生成）
- 用简单表格排版脚本代替 baoyu 出图

记录实际使用的后端到 `_manifest.md` 的 `render_backend` 字段：`imagegen` / `baoyu-image-gen` / `generate-image`。

---

## data-manifest.md 格式

```markdown
# Data Manifest: <type>

## Title
<精确标题字符串>

## KeyFacts（写入 prompt 的关键数据，verbatim）
- <事实 1 + [A/B/C] + 时效>
- <事实 2>

## MustAppear（agent 读 PNG 核对）
- [ ] 标题含：<精确标题>
- [ ] 出现产品名：<T0-A>, <T0-B>, ...
- [ ] 关键数字可见：<数字> + 证据等级
- [ ] （analysis）推荐方案含 ≥2 条代价/风险
- [ ] （tech）课题专名 ≥3 处
- [ ] （competitors）行数 ≥ T0 文件数
- [ ] Footer：调研信息截止 YYYY-MM-DD

## Table（competitors 可选，辅助写 prompt）
| row | col | value |
|-----|-----|-------|
| 产品A | 价格 | ~$XXX |
...

## Labels（analysis/tech/market 可选）
- label_id: <精确字符串>
```

Agent 自验：视觉阅读 PNG，逐项勾选 MustAppear；以「语义可见」为准，不要求 OCR 级逐字匹配。

---

## 风格锁定

### 首张图（competitors）成功后

1. 读取 baoyu `references/styles/<信息图_style>.md`
2. 写入 `_style-lock.md`（Color Palette、Visual Elements、Forbidden、Annotation Style）

### 第 2–4 张

`prompts/infographic.md` 与 structured-content 的视觉约束须与 `_style-lock.md` 一致。

---

## 产品素材策略（imagery_policy）

无 `refs/` 官方素材时：

- prompt 含 `NO_PRODUCT_PHOTOS`
- 使用图标、几何、排版表达，禁止拟真硬件渲染与 stock photo

禁止：水墨 mascots、未授权品牌 logo 臆造、源文件中不存在的准确率小数。

---

## Phase C：Agent 自验

每张 PNG 生成后**必须**：

1. 读取 PNG + 同目录 `data-manifest.md` 的 **MustAppear**
2. 逐项勾选；记录 `verification: pass|fail` 与 `mismatches: []` 到 `_manifest.md`
3. 核对：competitors 语义上覆盖全部 T0；tech 含课题专名；analysis 推荐侧含代价

**失败处理**：

- 修订 `prompts/infographic.md`（及必要时 structured-content）→ 重出图 → 再验
- 同一 type **最多 2 次**重试
- 仍 fail：该 type `status: failed`；若用户选择生成信息图且有关键 type failed，Step 8 信息图项不得全勾

---

## _manifest.md 模板

```markdown
# Infographic Manifest

| type | path | size_bytes | sha256 | render_backend | verification | generated_at |
|------|------|------------|--------|----------------|--------------|--------------|

## Checks
- [ ] 4 files exist（若用户选择生成）
- [ ] Each type has source / analysis / structured-content / data-manifest / prompts/infographic.md
- [ ] All verification = pass
- [ ] competitors 语义覆盖 T0 count

## Failures
（若有 failed type，列 mismatches）
```

生成 sha256：`sha256sum output/infographics/*/infographic-*.png`

---

## 图像后端优先级（修订）

1. baoyu 规则解析的 runtime-native **imagegen**
2. **baoyu-image-gen**
3. Cursor **GenerateImage**
4. 均不可用 → 报错列入信息缺口；**禁止** HTML/SVG/表格脚本回退
