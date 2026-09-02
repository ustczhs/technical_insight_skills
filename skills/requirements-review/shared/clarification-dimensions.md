# Clarification Dimensions（v1）

澄清阶段固定 **11** 维（原 7 + Delivery Sketch 4）。每一维：给出**推荐答案** + 简短理由（可引用 Corpus / Web）→ 用**选择题**请用户确认（格式见 [grill-output.md](grill-output.md)；最后一项为自定义）。

低耦合维可一批 ≤3；下列必须**单独成题**：Corpus 纳入确认、Corpus Relation、clarification ready 确认。Delivery Sketch 四维彼此可同批，但不得与 Corpus 纳入 / Relation / ready 混批。

| id | 维 | 要澄清什么 | 推荐时注意 |
|----|----|------------|------------|
| problem | 要解决的问题 | 谁在什么情况下痛点/目标是什么；不是解决方案清单 | 用用户语言；避免直接跳到「做个 XX 功能」 |
| user | 对象用户 | 主用户 / 次要用户；是否内部角色 | 与 Corpus 中人物/角色对齐；冲突标 Conflicts |
| scenario | 关键场景 | 1–3 个具体场景（触发→行为→结果） | 场景要可测试；过空则继续追问 |
| success | 成功判据 | 怎样算做成（可观察信号，不必量化指标） | 「更好用」无效；要可验收的描述 |
| non_goals | 非目标 | 明确不做 / 本期不做 | 从 Seed 中容易膨胀的部分挖出来 |
| constraints | 约束 | 平台、合规、依赖系统、性能/功耗等（**不含**工期主责） | 能查 Corpus 的自己查；决策仍问用户；工期见 `duration_band` |
| deps_risks | 依赖与风险 | 上游依赖、不确定假设、主要风险 | Unknown Corpus 时风险维加重写 |
| tech_route | 技术路线 | 本期主推技术路线（可附备选）；粗到栈/方向级 | 按 Corpus 生成 2–4 实质选项 + 自定义；可含「待定」；禁止详细设计 |
| integration_surface | 触及面 | 主要动端侧 / 云 / 算法 / 工具链 / 哪些现有模块 | 估人/工期的锚；不写接口清单；可含「待定」 |
| effort_band | 人力量级 | 大概投入人力的量级档 | **仅用下方固定词表**；禁止精确人天 |
| duration_band | 工期量级 | 大概耗时的量级档 | **仅用下方固定词表**；禁止排期表 |

## Delivery Sketch（交付草图）

总称，**不是**独立 Artifact。由下列四维组成，须全部经用户确认（答案可为「待定」）后，才允许 `clarification_status = ready`：

`tech_route` · `integration_surface` · `effort_band` · `duration_band`

澄清稿用专节列出四字段，供 Value Verdict 整节引用。

### `effort_band` 固定词表

`≤0.5人` · `1–2人` · `3–5人` · `>5人` · `待定`

### `duration_band` 固定词表

`≤1周` · `1–2周` · `2–4周` · `1–2月` · `约一季度` · `>一季度` · `待定`

出题时实质选项从词表选取（可省略明显不合理档），**必须**保留「待定」或「其他 / 自定义」路径；末项仍为 grill 规定的自定义项。

## Corpus Relation（每维或整条需求须标注）

对整条 Clarified Requirement（及必要时对关键维）标注其一：

| 态 | 含义 | 对后续 Value 的默认影响 |
|----|------|-------------------------|
| New | Corpus 中无对应能力/陈述 | 可进入正常价值评审 |
| Extends | 在已有能力上延伸 | 增量价值看「相对 Corpus 增量」维 |
| Conflicts | 与 Corpus 陈述或既有范围冲突 | **未解消前不得 Do** |
| Already-covered | Corpus 已覆盖，无明显增量 | **未解消前不得 Do**（默认偏 Don't / Defer） |
| Unknown | Corpus 缺失/过薄，无法对齐 | 须 low confidence；默认更偏 Defer |

解消 = 用户明确接受冲突/重复策略（改范围、改 Corpus、或接受重复建设理由）并写入澄清稿。
