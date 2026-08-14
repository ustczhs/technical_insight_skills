# Selection Brief Template

建议路径：`$PROJECTS_ROOT/<project_slug>/selection/SELECTION_BRIEF.md`  
复制下方全文作为起点。**纯 Markdown**：文首元信息表 + 维度表；不要 YAML。

# Selection Brief: \<产品名\>

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| brief_status | draft |
| project_slug | |
| product_name | |
| product_slug | |
| product_family | companion_robot / wearable_ai / out_of_family |
| application_domains | 例：motorcycle, light_ev |
| primary_silicon_class | 例：display_mcu |
| adjacent_silicon_classes | 例：vehicle_soc, industrial_mcu |
| needs_seed_extension | false |
| target_silicon_class | （可读说明：主类 + 相邻 + 理由；权威以三列枚举为准） |
| created | YYYY-MM-DD |
| updated | YYYY-MM-DD |

`brief_status`：`draft` \| `brief_ready`  
`application_domains` / Silicon Class id 见 `shared/application-domains.md`、`shared/silicon-classes.md`。

## 1. 产品概念（选型所需最小描述）

\<3–8 句：要做什么、给谁、关键场景。不写完整 PRD。\>

## 2. Product Family

| 项 | 内容 |
|----|------|
| 选定 | companion_robot / wearable_ai / out_of_family |
| 推断理由 | … |
| 产品确认 | 是 / 否（修订说明） |

若 `out_of_family`：说明仅为 **Profile/问卷缺口**；Phase 2 检索仍按 Silicon Class ∪ Application Domain 执行。

## 2b. Application Domain

| 项 | 内容 |
|----|------|
| 选定 | 域 id 列表（可多选） |
| 推断理由 | 从产品概念/标题 |
| 产品确认 | 是 / 否 |
| needs_seed_extension | 自定义域未入词表时为 true |

「优先某某行业芯片」必须落在本表，不要只写 Soft 散文。

## 3. Target Silicon Class

| 项 | 内容 |
|----|------|
| primary | 一个 Silicon Class id |
| adjacent | 0～N 个 id（含 Hard 触发复核结果） |
| 可读说明 | 默认优先类 + 相邻覆盖理由 |
| 产品确认 | 早选主类已确认；Ready 前相邻类已复核 |

Phase 2 打开 `vendor-seeds` 的 **Class 段 ∪ Domain 加扫**；勿暗示只能搜某一 Family 的旧矩阵。

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

抽出 `grade=soft` 项，供 Match Band。行业优先应已由 Application Domain 消化。

## 7. Unconstrained

显式无要求的维度 id 列表。

## 8. Brief Ready 检查

- [ ] Product Family 已确认（或 Out-of-Family 已明示）
- [ ] Application Domain 已确认（含自定义时的 needs_seed_extension）
- [ ] primary_silicon_class 已确认；adjacent 已按 Hard 复核
- [ ] Profile 内全部 Core 均有 Dimension Answer（Out-of-Family 则为其轻量维）
- [ ] 已纳入的 Extension 均有 Dimension Answer
- [ ] 每项等级已在 Dimension Turn 中确认
- [ ] Framing–Spec Mapping 均已写明

全部勾选后将元信息表 `brief_status` 设为 `brief_ready`。

## 9. 源溯源附录

本附录供交接审计；**不构成** Hard Constraint / Soft Preference。Phase 2 只消费 §5 / §6 与元信息中的 Class/Domain。

### 9.1 Brief Source 清单

| 文件名 | 相对路径 | 备注 |
|--------|----------|------|
| （无） | | |

### 9.2 Source Residue（未映射摘录）

| 来源文件 | 摘录摘要 | 处理 |
|----------|----------|------|
| （无） | | 未映射 / 未能抽取 / 已提议 Extension：… |

### 9.3 冲突裁定

| 维度 id | 各方摘录 | 用户裁定 |
|---------|----------|----------|
| （无） | | |
