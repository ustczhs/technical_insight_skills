# 幻灯片中间稿骨架（hardware-insight Step 8）

> 复制到 `research/<产品简称>/output/slides-<取向>.md`  
> 规范：[`html-deck-spec.md`](../../references/html-deck-spec.md)  
> 构建：`python3 .cursor/skills/hardware-insight/scripts/build_deck_ppt.py`

---

## 硬性规则

- 每页 **必须** `layout:`（见下表）
- 普通 bullet **≤40 字**；`summary` 页 `recommendation` **≤120 字**
- `table` 页：≤5 列 × ≤5 行
- **禁止** `image: infographics/`
- **禁止** `aside.notes`
- 页数：决策/科普 **10–14**；投资人 **10–12**

---

## layout 速查

| layout | 关键字段 |
|--------|----------|
| cover | title, subtitle, meta |
| summary | bullets, **recommendation** |
| table | table_headers, table_rows |
| comparison | left_title, left_items, right_title, right_items, right_risks |
| flow | nodes (title + body) |
| timeline | phases (period, milestone, gate) |
| metrics | metrics (value, label, note), bullets |
| bullets | bullets |

---

## 决策导向（12 页示例）

```markdown
---
deck: 决策导向
theme: engineering-whiteprint
slides: 12
---

## slide: 封面
layout: cover
title: [产品] × [课题] 融合评估
subtitle: [一句话副标题]
meta:
  - 立项评估 · [分析师立场：读调研基调.md]
  - 调研截止：YYYY-MM-DD
  - 读者：管理层

## slide: 核心结论
layout: summary
title: 核心结论
bullets:
  - [结论1：能否结合]
  - [结论2：推荐形态]
  - [结论3：必要性判断]
  - [结论4：对外叙事纪律]
recommendation: [从决策摘要.md建议方向摘录，主语为我方主体]

## slide: 竞品格局
layout: table
title: 竞争态势 · 三轨道
table_headers:
  - 轨道
  - 代表
  - 对我方影响
table_rows:
  - [LLM叙事 | PettiChat/Traini | 威胁/机会]
  - [情绪分类 | Petpuls/PurrPurr | 方法论参照]
  - [家庭移动AI | [我方产品] | 融合空白位]

## slide: T0证据
layout: table
title: T0 关键证据
table_headers:
  - 产品
  - 关键事实
  - 证据
table_rows:
  - [产品A | 事实 | [A/B/C]]

## slide: 方案对比
layout: comparison
title: 集成方案对比
left_title: 弃选：硬件合体
left_items:
  - [劣势1]
  - [劣势2]
right_title: 推荐：O2 传感融合
right_items:
  - [优势1]
  - [优势2]
right_risks:
  - [代价1]
  - [代价2]
footer_note: 首选 O2 · 不进 v1.0 首发

## slide: 技术路线
layout: flow
title: 五层融合架构
nodes:
  - title: 采集层
    body: [传感近场 + 我方主体视觉/多模态能力]
  - title: 边缘层
    body: [端侧触发分类]
  - title: 融合层
    body: [家庭情境图谱]
  - title: 推理层
    body: [AIOS + Gemini]
  - title: 输出层
    body: [播报 + Matter + App]

## slide: 商业窗口
layout: metrics
title: 商业窗口与必要性
metrics:
  - value: "1万+"
    label: PettiChat 预售台数
    note: "[B] 2026-05"
  - value: "≤15%"
    label: 建议研发占比
    note: 24月 17-26人月
  - value: 有条件必要
    label: 战略判断
    note: 非 v1.0 刚需
bullets:
  - 12-18 月 Partner 窗口仍开放

## slide: 产品边界
layout: bullets
title: 产品定义与边界
bullets:
  - 做 L1：Pet Insight 事件推送
  - 做 L2：融合播报 + Matter 安抚
  - 不做：宠物机器人主定位
  - 不做：v1.0 捆绑项圈
  - 命名：情绪与需求提示（禁「翻译」）

## slide: 路线图
layout: timeline
title: 路线图
phases:
  - period: 0-6月
    milestone: BD + Pet Skill API 草案
    gate: [我方主体] 量产里程碑确认
  - period: 6-18月
    milestone: 2 款认证项圈 + 融合 v1
    gate: 30日留存 ≥15%
  - period: 18-24月
    milestone: 扩 SKU 或维持 Partner
    gate: 付费转化/NPS 达标

## slide: 风险
layout: table
title: 风险 Top5
table_headers:
  - 风险
  - 概率×影响
  - 缓解
table_rows:
  - [风险1 | 中×高 | 措施]

## slide: 待证
layout: bullets
title: 待证事项
bullets:
  - [待证1] — [验证方式]

## slide: 证据说明
layout: bullets
title: 证据说明
bullets:
  - [A] 官方/论文/认证
  - [B] 权威媒体交叉
  - [C] 预测与二手推断
  - 调研信息截止：YYYY-MM-DD
```

---

## 科普导向（+1 页 explain）

在「技术路线」前插入：

```markdown
## slide: 原理阐释
layout: explain
title: 技术原理（科普）
bullets:
  - PettiChat 非语言学翻译，是分类+LLM润色
  - 项圈近场声学不可替代
  - [我方主体] 价值在视觉+家居闭环
```

---

## 构建命令

```bash
python3 .cursor/skills/hardware-insight/scripts/build_deck_ppt.py \
  --input research/<slug>/output/slides-<取向>.md \
  --output research/<slug>/output/汇报-<取向> \
  --title "<产品> 汇报"
```

---

## 质量自检

- [ ] 每页有 `layout`
- [ ] summary 含 recommendation
- [ ] 竞品/方案/技术/商业非纯 bullets
- [ ] `汇报-<取向>/index.html` 翻页正常
- [ ] 无 infographics 图片引用
