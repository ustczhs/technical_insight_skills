# Selection Brief Template

建议路径：`selection/<product-slug>/SELECTION_BRIEF.md`  
复制下方全文作为起点。**纯 Markdown**：文首元信息表 + 维度表；不要 YAML。

# Selection Brief: \<产品名\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| brief_status | draft |
| product_name | |
| product_slug | |
| product_family | companion_robot / wearable_ai / out_of_family |
| target_silicon_class | |
| created | YYYY-MM-DD |
| updated | YYYY-MM-DD |

`brief_status`：`draft` \| `brief_ready`

## 1. 产品概念（选型所需最小描述）

\<3–8 句：要做什么、给谁、关键场景。不写完整 PRD。\>

## 2. Product Family

| 项 | 内容 |
|----|------|
| 选定 | companion_robot / wearable_ai / out_of_family |
| 推断理由 | … |
| 产品确认 | 是 / 否（修订说明） |

若 `out_of_family`：说明降级风险；Phase 2 不保证质量。

## 3. Target Silicon Class

本族**默认优先类** + **相邻类覆盖**说明（Phase 2 须检索可能满足 Hard 的跨形态主控，例如视觉 SoC / 眼镜芯片用于机器人或耳机；勿把默认类写成唯一门禁）。

## 4. Dimensions

Core 必须全部出现；已触发的 Extension 同样。每维一行主表；过长自定义说明可在表下加「备注」小节。

### 4.1 维度总表

| id | phase | Product Framing（摘要） | Dimension Answer | Spec Field（摘要） | Framing–Spec Mapping | grade | 推荐等级 | 已确认 |
|----|-------|-------------------------|------------------|--------------------|----------------------|-------|----------|--------|
| compute_band | core | 希望本地多任务流畅，可接受中端机体感 | option:`mid` 中端多任务 | CPU 性能带：中端 AP；norms: cpu_band=mid | 「中端多任务」↔ cpu_band: mid | soft | soft | 是 |

`phase`：`core` \| `extension`  
`Dimension Answer`：`option:<id> <label>` \| `custom:…` \| `unconstrained`  
`grade`：`hard` \| `soft` \| `unconstrained`

### 4.2 维度备注（可选）

#### compute_band

- 提供过的选项：entry 入门流畅 / mid 中端多任务 / high 高端重度
- 等级理由：体验目标，可用 Soft；若对标机必须达到再升 Hard

## 5. Hard Constraints（汇总）

从维度总表抽出 `grade=hard` 的 Spec Field，列表化。

## 6. Soft Preferences（汇总）

抽出 `grade=soft` 项，供 Match Band。

## 7. Unconstrained

显式无要求的维度 id 列表。

## 8. Brief Ready 检查

- [ ] Product Family 已确认（或 Out-of-Family 已明示）
- [ ] Profile 内全部 Core 均有 Dimension Answer
- [ ] 已纳入的 Extension 均有 Dimension Answer
- [ ] 每项等级已在 Dimension Turn 中确认
- [ ] Framing–Spec Mapping 均已写明

全部勾选后将元信息表 `brief_status` 设为 `brief_ready`。
