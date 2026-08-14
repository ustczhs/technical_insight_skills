---
name: requirements-review
description: >-
  Requirements skill in the Technical Planning Skill Package: grill a fuzzy
  Requirement Seed against a Project Corpus (id card, feature lists, etc.) into
  a Clarified Requirement, then a Value Verdict (Do / Defer / Don't). Writes under
  $PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/. Use when the user invokes
  requirements-review, /requirements-review, or asks for 需求澄清 / 需求评审 /
  模糊需求对齐 / 需求价值评估 — not SoC selection, hardware research, tech-tree,
  or project-dossier CRUD alone.
disable-model-invocation: true
---

# requirements-review

通过 grill，把 **Requirement Seed**（模糊需求）相对 **Project Corpus** 澄清为 **Clarified Requirement**，再给出 **Value Verdict**（Do / Defer / Don't）。

本 skill 属于 Technical Planning Skill Package（包公约见仓库根 CONTEXT.md）。运行时写入 `$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/`。与调研 / 选型 / 技术树**无硬衔接**。

术语权威：[CONTEXT.md](CONTEXT.md)。维表与模板：[shared/](shared/)。项目闸门：若已安装 `project-dossier`，读其 `shared/project-gate.md`；否则遵循下方「项目闸门」。

## 硬规则

1. **项目闸门**：先确认 `project_slug`；无 `PROJECT.md` 则最小建档或引导 `/project-dossier`，再继续。
2. **双产物顺序闸门**：先澄清，再价值。未 `clarification_status = ready` 不得定稿正式 Value Verdict。
3. **一次只推进一个决策**（默认）；低耦合维可一批 ≤3。下列必须**单独成题**：Corpus 纳入确认、Corpus Relation、最终 Do/Defer/Don't。
4. **每个决策必须带推荐答案**；禁止让用户对着空白枚举。
5. **Grill 输出用选择题**：面向用户的决策题按 [shared/grill-output.md](shared/grill-output.md) 输出——实质选项 2–4 个并标注 `（推荐）`，**最后一项固定为「其他 / 自定义」**供用户改写；禁止只写「同意 / 或改写」而无选项列表。
6. **推荐要高质量**：结合 Project Corpus（优先 `$PROJECTS_ROOT/<project_slug>/corpus/`）、本 skill `shared/`、以及**主动联网检索**。检索失败则降级为仅本地，不阻塞。
7. **来源分型**：写入产物时区分 **Corpus（本地权威）** vs **Web（外部参考）**。Web 默认仅参考；升格进结论前须用户确认，并标注 URL。v1 **不设**域名白名单。
8. **Conflicts / Already-covered 未解消 → 不得推荐 Do**。
9. **薄 Corpus / Unknown**：可继续；`confidence` 倾向 low；默认更偏 Defer，除非用户显式接受无文档对齐风险。
10. 能从仓库/上下文查到的事实自己查；**决策权在用户**。未达共同理解前，不宣称评审完成。
11. 产物与追问以**中文**为主；术语可用 CONTEXT 中的英文标签。
12. **索引回写**：完成后更新 `PROJECT.md` §3 需求索引对应行（及 `updated`）；勿改简介/Corpus 列表/status。

## 项目闸门

1. 先解析 Projects Root：运行 `project-dossier/scripts/ensure-projects-root.sh`，导出 `PROJECTS_PATHS` / `PROJECTS_PATH`。
2. 确认 `project_slug`。
3. 若缺少 `$PROJECTS_ROOT/<project_slug>/PROJECT.md`：按 project-dossier 模板最小建档（或请用户先 `/project-dossier`），确认后再写。
4. 若发现工作区相对 `projects/` 或根级旧 `requirements/` 产物：提示迁移，不自动搬家、不双写。

## 会话流程

### 0. 启动

- 通过项目闸门。
- 收集 **Requirement Seed**；确定 **req_slug**（默认英文或拼音）。
- 目录：`$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/`。
- 若目录已有产物：询问继续 / 修订 / 新建。
- 读取 [CONTEXT.md](CONTEXT.md)、[shared/clarification-dimensions.md](shared/clarification-dimensions.md)、[shared/value-dimensions.md](shared/value-dimensions.md)、[shared/corpus-discovery.md](shared/corpus-discovery.md)、[shared/grill-output.md](shared/grill-output.md)。

### 1. Project Corpus

- 优先扫描 `$PROJECTS_ROOT/<project_slug>/corpus/` 与 PROJECT.md §2；再按 [shared/corpus-discovery.md](shared/corpus-discovery.md) 补候选。
- **单独一题**请用户确认纳入/排除（选择题格式，见 grill-output）。
- 读入已纳入文档；未确认文件不得当权威。

### 2. Clarification Dimensions

- 按七维推进。每维：推荐答案 + Corpus/Web 依据 → **选择题**请用户确认（见 [shared/grill-output.md](shared/grill-output.md)）。
- 整条需求标注 **Corpus Relation**——**单独成题**（选择题）。
- 增量写入 `…/CLARIFIED_REQUIREMENT.md`（模板：[shared/clarified-requirement-template.md](shared/clarified-requirement-template.md)）。
- 达成一致后 `clarification_status = ready`（须用户确认；选择题）。

### 3. Value Verdict

- **闸门**：仅当澄清 Ready。
- 六维定性评估（可用一题确认「同意修订六维 / 调整某维 / 自定义」）→ 推荐 Do / Defer / Don't（**单独成题**，选择题）。
- 写入 `…/VALUE_VERDICT.md`；确认后 `verdict_status = final`。

### 4. 收尾

- 回写 `PROJECT.md` 需求索引行。
- 不自动调用其他簇；可口头建议。

## 进度检查清单

```
Requirements Review Progress:
- [ ] Step 0: project_slug 闸门 + Requirement Seed + req_slug
- [ ] Step 1: Project Corpus 确认（可空=降级）
- [ ] Step 2: Clarification Dimensions（7）
- [ ] Step 2b: Corpus Relation + 冲突解消
- [ ] Step 2c: clarification_status = ready
- [ ] Step 3: Value Dimensions（6）
- [ ] Step 3b: Do / Defer / Don't 确认
- [ ] Step 3c: verdict_status = final
- [ ] Step 4: PROJECT.md 需求索引回写
```

## 产出

```
$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/
├── CLARIFIED_REQUIREMENT.md
└── VALUE_VERDICT.md
```

## 非目标

- 不是完整 PRD / 设计文档 / 排期系统 / 项目档案 CRUD（那是 `project-dossier`）
- 不是 SoC 选型、智能硬件调研、技术树生长
- 不建立与其他簇的硬交接闸门
