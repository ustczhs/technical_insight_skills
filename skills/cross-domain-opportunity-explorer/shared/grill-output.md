# Grill 输出格式（Decision Grill）

面向用户的每一道 **Decision Grill** 题，**默认用选择题**；对齐 [ask-and-lazy.md](../../project-dossier/shared/ask-and-lazy.md) 与 requirements-review。

## 硬格式

```markdown
### 〈题目标题〉（单选）或（多选）

简要依据（Seed / 既有产物 / 上下文，1–3 行）

**请选择：**

A. 〈选项〉（推荐）
B. 〈选项〉
C. 〈选项〉
D. 其他（请补充）
```

## 规则

1. **实质选项 2–4 个**（不含自定义）；最后一项固定「其他（请补充）」。
2. **必须标推荐项**，通常放 A。
3. **一次一题**；禁止一批多题。
4. 用户回 `A` / `同意推荐` → 视为选中推荐项。
5. 选自定义但未写内容 → 追问一句，勿擅自发明。
6. **Lazy**：不问 Decision Grill，闸门①–⑤全部用推荐值。

## 五闸门示例

### 闸门① Seed/范围

```markdown
### 探索范围（单选）

已继承偏好：大陆+海外、Pain+Itch、硬件+服务+空间、探索阶段尽量多。

**请选择：**

A. landscape 广筛（推荐）— 覆盖尽量广，去重后目标 ≥80 火花
B. deep-dive — 只深挖你指定的 1 个 People Cell
C. 修订既有批次 — 继续 opportunities/ 中未完成段
D. 其他（请补充）
```

### 闸门② 排除轴

```markdown
### 排除轴（多选）

**请选择本批明确不碰的方向：**

A. 无额外排除，尽量多碰撞（推荐）
B. 排除 medical-boundary 相关状态主题
C. 排除纯线下空间重资产形态
D. 其他（请补充）
```

### 闸门⑤ 交接去向

```markdown
### 交接去向（单选）

shortlist 条目建议默认路由如下。

**请选择：**

A. `/hardware-insight` — 需竞品/技术/市场深证（推荐）
B. `/requirements-review` — 值不值得做仍不明
C. 本簇 deep-dive — 证据/场景仍不足
D. 其他（请补充）
```

## 反例

- 段末问「然后呢？」
- 把 Hypothesis Grill 变成十连问
- 对话里贴完整 50+ 行火花表（违反直接呈现）
- 无推荐标记的裸选
- 火花阶段要求用户逐条确认 50 个 idea
