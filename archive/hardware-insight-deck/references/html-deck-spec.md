# HTML 幻灯片规范（hardware-insight Step 8）

> **暂时停用（2026-08）**：结构化调研 Step 8 **不再生成** `slides-*.md` / `汇报-*/`。本文件与构建脚本保留备查，恢复前勿在流程中调用。

`output/汇报-<取向>/index.html` 为 **多页幻灯片**（html-ppt runtime），用于对内汇报；支持键盘 ←/→ / Space 翻页。

生成前可读 **html-ppt** skill（Cursor/Codex 内置；主题与 runtime 参考）。`deck-assets/` 已 vendored，不依赖外部安装。

骨架中间稿：[`templates/report/slides-骨架.md`](../templates/report/slides-骨架.md)

构建脚本：[`scripts/build_deck_ppt.py`](../scripts/build_deck_ppt.py)（**勿用**已废弃的 `build_deck_html.py`）

---

## 定位

| 产出 | 用途 |
|------|------|
| `报告-<取向>.md` | 完整分析母版 |
| `slides-<取向>.md` | 幻灯片中间稿（每页 `layout` + 结构化字段） |
| `汇报-<取向>/index.html` | 可翻页汇报幻灯片（含 `assets/`） |

HTML **不是** MD 缩略贴图：每页独立可讲，保留建议句、表格与对比结构。

**纯文字交付**：幻灯片**禁止**嵌入 `infographics/*.png`。竞品/方案/技术/市场页用 **table / comparison / flow / metrics** 等 layout 呈现。

---

## 产出目录结构

```
output/汇报-<取向>/
├── index.html
└── assets/
    ├── base.css
    ├── fonts.css
    ├── hi-deck.css
    ├── runtime.js
    └── themes/
        ├── blueprint.css
        └── engineering-whiteprint.css
```

资源来源：[`deck-assets/`](../deck-assets/)（`scripts/install_deck_assets.sh` 可刷新上游 html-ppt 核心文件）

---

## 主题

| 场景 | `theme:` 值 |
|------|-------------|
| 默认 | `engineering-whiteprint` |
| 深色蓝图 | `blueprint` |
| `信息图_style=pop-laboratory` | `engineering-whiteprint`（与信息图视觉联动，不嵌 PNG） |

`slides-*.md` frontmatter 的 `theme:` 由 builder 读取。

---

## layout 类型（每页必选）

| layout | 用途 | 典型页 |
|--------|------|--------|
| `cover` | 封面 title/subtitle/meta | 封面 |
| `summary` | 结论 bullets + **recommendation** | 核心结论 |
| `table` | `table_headers` + `table_rows` | 竞品格局、T0 证据、风险 |
| `comparison` | 左弃选 / 右推荐 + `right_risks` | 方案对比 |
| `flow` | `nodes` 五层架构 | 技术路线 |
| `timeline` | `phases` 三阶段 + Gate | 路线图 |
| `metrics` | `metrics` 大数字 + bullets | 商业窗口 |
| `bullets` | 增强列表（兜底） | 产品边界、待证、证据说明 |
| `explain` | 同 bullets（科普原理页） | 原理阐释 |

---

## 硬性要求

- 每页 **≤6** bullet（`table` / `comparison` / `flow` 不计入 bullet 限制）
- 普通 bullet 每条 **≤40 字**（中文）
- `summary` 页 **必须**含 `recommendation`（≤120 字，摘自 `决策摘要.md` 建议方向）
- 竞品 / 方案 / 技术 / 商业页须用 `table|comparison|flow|metrics` 之一（**不得**仅用 `bullets`）
- **禁止** `image: infographics/`
- **禁止** `aside.notes`（hardware-insight 不做演讲者模式）
- 键盘 ←/→ / Space 翻页；页脚显示页码
- `@media print`：每 `.slide` 一页
- 打开 `index.html` 无 404（`assets/` 随 deck 复制）

---

## 构建命令

```bash
python3 .cursor/skills/hardware-insight/scripts/build_deck_ppt.py \
  --input research/<slug>/output/slides-决策导向.md \
  --output research/<slug>/output/汇报-决策导向 \
  --title "<课题> 决策汇报"
```

---

## 生成流程

1. 完成 `报告-<取向>.md`
2. 从报告 + `决策摘要.md` 编写 `slides-<取向>.md`（按 layout 结构化，非电报缩写）
3. 运行 `build_deck_ppt.py`
4. 自检：页数、layout 类型、recommendation、键盘翻页、打印

---

## 质量自检（agent）

- [ ] 存在 `output/slides-<取向>.md`，每页含 `layout:`
- [ ] `output/汇报-<取向>/index.html` 可翻页（←/→/Space）
- [ ] 页数 10–14（决策/科普）或投资人 10–12
- [ ] 含封面、summary+recommendation、风险 table、待证
- [ ] 竞品/方案/技术/市场页 layout 合规
- [ ] **无** `image: infographics/`
- [ ] `assets/runtime.js` 无 404
