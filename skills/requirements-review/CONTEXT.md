# requirements-review

通过 grill 交互，把模糊需求收敛为可评审的澄清稿，再给出价值结论。本文件是本 skill 的领域术语权威。包公约见仓库根 [CONTEXT.md](../../CONTEXT.md)。与调研 / 选型 / 技术树无数据契约。

## Language

**Requirement Seed**:
用户输入的模糊需求陈述（一句话、一段口述、或未对齐文档的草稿）。是澄清流程的入口，不是最终需求。
_Avoid_: PRD, 正式需求, Clarified Requirement

**Project Corpus**:
本会话认定为权威的、用于对齐与对照的项目说明文档集合（如 id card、软件功能清单、产品说明）。优先来自 `$PROJECTS_ROOT/<project_slug>/corpus/`；不含代码本身；纳入权在用户。
_Avoid_: 整个代码仓库, 未经确认的搜索命中

**Corpus Relation**:
澄清中每条需求相对 Project Corpus 的关系，取值仅限：New、Extends、Conflicts、Already-covered、Unknown。Unknown 仅用于 Corpus 不足或无法对齐时。
_Avoid_: 相关, 差不多, 重复（口语，须落入五态之一）

**Clarification Dimension**:
澄清阶段的固定问卷维（问题、用户、场景、成功判据、非目标、约束、依赖/风险）。逐维给出推荐答案，并以选择题经用户确认（见 shared/grill-output.md）。
_Avoid_: 开放漫谈无维, 完整 PRD 章节, 无选项列表的「同意或改写」

**Grill Choice**:
面向用户的决策题输出形态：2–4 个实质选项（含标注的推荐项）+ **最后一项「其他 / 自定义」**。用户可回字母或改写自定义项。
_Avoid_: 空白开放题, 自定义项不在末位, 无推荐标记

**Clarified Requirement**:
与 Project Corpus 对齐、边界清楚的需求陈述产物；须 `clarification_status = ready` 后才可进入正式价值结论。
_Avoid_: Requirement Seed, 未确认的推荐草稿

**Value Dimension**:
价值评审的固定定性维（用户价值、战略契合、相对 Corpus 增量、成本/复杂度、风险、时机）。每维给推荐档位与一句话理由，不做伪精确总分。
_Avoid_: 加权打分公式, 纯散文无维

**Value Verdict**:
在 Clarified Requirement Ready 之后给出的价值结论，取值仅限：Do、Defer、Don't，并附各 Value Dimension 理由与置信度。
_Avoid_: P0/P1/P2（优先级不等于价值闸门）, 未澄清即下的正式结论

**Web Reference**:
联网检索得到的外部参考（竞品做法、公开标准、可复核报道等）。默认是参考；写入正式结论前须用户确认，并标注 URL 或等价可复核来源。
_Avoid_: 把营销页直接写成产品事实, 无来源的「业界都这样」
