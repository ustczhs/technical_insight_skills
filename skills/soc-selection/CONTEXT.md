# SoC Selection（选型簇）术语

本文件是 **soc-selection** 能力簇的领域术语权威。包级公约见仓库根 [CONTEXT.md](../../CONTEXT.md)。

选型与检索遵循 **第一性原理**：以 Brief 中可验证的能力与约束（算力/接口/功耗热/音频视觉链路/软件可落地等）判定去留，**不以**市场品类标签、厂商营销定位或「通常用于某形态」作为整类排除依据。跨形态复用常见（例如 AI 眼镜视觉 SoC 用于桌面机器人底座、视觉蓝牙耳机等），须纳入搜索与比较；类标差异用 Match Band / 取舍说明表达，而非默杀。

v1 内置两个 Product Family：陪伴机器人、可穿戴 AI。

## Language

**Selection Pipeline**:
本簇内可连接的选型两段：`hardware-selection-brief`（Phase 1）→ `soc-shortlist`（Phase 2）。交接闸门为 Brief Ready。本簇在仓库中内聚（叶子 skill + shared + 示例）；不是合并成单一 Cursor skill——安装时分别链接两个叶子目录。
_Avoid_: 把 Brief 与 Shortlist 合成一个 SKILL.md, 把 `skills/soc-selection` 直接 symlink 成单一 skill

**First Principles (选型)**:
从产品必须成立的物理与工程约束出发做筛选与解释：端侧要跑什么、接口要接什么、功耗热能否接受、软件/SDK 能否量产落地。品类叙事（「这是眼镜芯片」「这是耳机 SiP」）只作检索线索，不作 Hard 淘汰理由。
_Avoid_: 仅凭品类刻板印象排除, 为覆盖而覆盖无关料号（仍须能对照 Spec Field）

**Selection Brief**:
Phase 1 的主交付物，也是跨人/跨会话交接的规范工件：一份选型导向的需求简报，只收录会影响选型的功能、约束与规格；含 Product Framing、Spec Field、Framing–Spec Mapping 与约束等级。落盘形态为纯 Markdown（文首元信息表 + 维度表格等）；不使用嵌入 YAML 或 YAML front matter。功能描述深度以能推导硬件约束为限。同会话内也可不落盘直接进入 Phase 2，但仍应能导出 Brief。
_Avoid_: PRD, 完整产品需求文档, 需求说明书, Brief YAML

**SoC Shortlist**:
Phase 2 的主交付物：一组满足 Selection Brief **Hard Constraint**（及已确认 `grade=hard` 探针）的候选型号，附对比维度与取舍说明；数量由筛选结果决定，不预设上下限，也不强制决出唯一赢家。Target Silicon Class 是优先检索锚点，**不是** Shortlist 入场的唯一门禁；满足 Hard 的相邻品类硅片（视觉 SoC、眼镜主控、音频 SiP 等）可入选，用 Match Band 反映贴合度。落盘形态为纯 Markdown（文首元信息表 + 表格/小节）；不使用嵌入 YAML 或 YAML front matter。
_Avoid_: 最终选型结论, Recommended SoC, 固定 3–5 款清单, Shortlist YAML, 仅因类标不符整类删除

**Target Silicon Class**:
某一 Product Family 下 Phase 2 的**默认优先搜索**硅片类别（种子集），用于提高检索效率。v1：Companion Robot 以 AP/SoM 为主；Wearable AI 以音频 SoC、SiP、低功耗主控为主。须同时做 **相邻类覆盖**（adjacent coverage）：凡可能满足 Brief Hard 的跨形态主控（如视觉 SoC、AI 眼镜芯片用于机器人/耳机，或机器人向 AP 用于带屏可穿戴）均应检索评估；不得仅因「非本族默认类」直接排除。
_Avoid_: 芯片类型（过宽）, 唯一零件号, 把默认类当成 Hard 整类门禁

**Hard Constraint**:
Selection Brief 中的硬约束：不满足则该 SoC 不得进入 Shortlist。
_Avoid_: Must, 刚性需求（单独作等级名时）

**Soft Preference**:
Selection Brief 中的软偏好：不满足仍可入选，但应在对比与取舍说明中体现，并用于 Match Band 粗排。
_Avoid_: Nice to have（单独作等级名时）, Should

**Match Band**:
SoC Shortlist 内按 Soft Preference 满足度划分的粗排档位：高匹配 / 中匹配 / 低匹配；不做精确加权打分。相邻品类硅片可用中/低匹配表达贴合度差异，不得仅凭类标将其移出 Shortlist。
_Avoid_: 评分, 排名分数, 权重总分, 用 Match Band 伪装整类 Hard 淘汰

**Core Dimension**:
在某一 Dimension Profile 内始终需要覆盖的选型维度；构成该 Product Family 稳定 schema 的主干，供 Phase 2 筛选使用。
_Avoid_: 基础字段, 必填项（易与 Hard Constraint 混淆）, 全球统一必填项

**Extension Dimension**:
按产品形态追加的选型维度；不在 Core Dimension 集合内，但一旦纳入 Brief 即与 Core 同样可标为 Hard Constraint 或 Soft Preference。
_Avoid_: 可选字段, 自定义字段

**Unconstrained**:
产品端对该维度明确表示「无要求」：不写入 Hard Constraint 或 Soft Preference，Phase 2 不据此筛选或排序。
_Avoid_: Unknown, TBD, 不确定（口语上不等于 Unconstrained）

**Dimension Answer**:
某一维度在 Selection Brief 中的取值：选自 Agent 提供的档位/选项，或产品端手动输入的自定义说明，或显式标记为 Unconstrained。
_Avoid_: 字段值（过于实现向）

**Dimension Turn**:
Phase 1 对某一维度的单次用户回合：在同一回复中同时给出 Dimension Answer 与约束等级（hard / soft / unconstrained）；Agent 须提供推荐等级，但不再拆成「先取值、再单独确认等级」两问。
_Avoid_: 两步等级确认, 取值与等级分问

**Product Framing**:
面向产品端的问法与选项表述（场景、体验、档位），用于 Phase 1 grilling。
_Avoid_: 用户故事（除非真在写用户故事）

**Spec Field**:
面向筛选的规范化 SoC 规格字段；Selection Brief 落盘与 Phase 2 搜索/过滤都以它为准。
_Avoid_: 芯片手册原文照抄

**Framing–Spec Mapping**:
同一维度上 Product Framing 与 Spec Field 的显式对照关系；必须写入 Selection Brief，使产品端与技术端都能看懂「产品说法」如何对应到硬件规格。
_Avoid_: 隐式翻译, 仅存在于对话中的口头转换

**Product Family**:
共享同类 SoC 选型问卷结构的产品族（如陪伴机器人、可穿戴 AI）；先于具体维度填写而确定，并决定采用哪套 Profile。
_Avoid_: 产品品类（口语可混用，正式用语用 Product Family）

**Dimension Profile**:
某一 Product Family 下的维度配置：该族的 Core Dimension 子集、配套 Extension Dimension 包，以及对应的 Framing–Spec Mapping。
_Avoid_: 模板, 问卷模板（可作俗称，正式用语用 Dimension Profile）

**Companion Robot**:
v1 的一个 Product Family：移动或车载等形态的陪伴机器人产品。Target Silicon Class 以 AP/SoM 为主，并覆盖可能满足 Hard 的视觉 SoC / 低功耗影像主控等相邻类。Core Dimension：产品子形态、算力档位、端侧 AI、显示、摄像与视频、高速互联、功耗与散热、工作环境、目标软件栈、交付形态、成本带、供货与生命周期。
_Avoid_: 服务机器人（若未区分用途则勿混用）, 仅搜经典 AP 而忽略可用的眼镜/IPC 视觉主控

**Wearable AI**:
v1 的一个 Product Family：可穿戴 AI 硬件，含视觉蓝牙耳机、AI 眼镜等形态。Target Silicon Class 以音频 SoC、SiP、低功耗主控为主，并覆盖视觉 SoC / 轻量 AP 等相邻类（当 Hard 允许时）。Core Dimension：产品子形态、功耗与续航预算、封装与尺寸约束、音频链路、无线连接、端侧 AI、传感与视觉、目标软件/固件栈、成本带、供货与生命周期。
_Avoid_: 仅写「耳机」而排除其他可穿戴 AI, 仅因「眼镜芯片」标签排除其在耳机/机器人上的可行性

**Out-of-Family**:
产品概念无法诚实归入当前已支持的 Product Family 时的状态：可继续做轻量 grilling，但 Selection Brief / Phase 2 质量不保证，并应提示优先扩展 Dimension Profile，而非硬塞进某一族。
_Avoid_: 其他, 自定义品类（未配套 Profile 时）

**Evidence Grade**:
Phase 2 对公开信息的来源等级：A（官方/拆解/认证库）> B（权威媒体/供应商）> C（二手信息）。每条用于筛选的关键规格须在文档中标注等级与来源；不得编造。引用格式：`[A/B/C] 内容（信息时效：YYYY-MM，来源 URL）`。细则见 [shared/evidence-rules.md](./shared/evidence-rules.md)。
_Avoid_: 可信度（口语）, 星级

**Evidence Freshness**:
用于描述现状时的时效规则：超过 48 个月的 [A] 源降为 [B]，直至有更新近源印证（相对硬件调研常用的更短窗口放宽，以适配长生命周期芯片）。
_Avoid_: 信息过期（口语判断，无阈值）

**Critical Claim**:
会影响 Hard Constraint 判定或 Shortlist 去留的关键结论：须至少 2 处独立来源交叉印证，并标注各来源的 Evidence Grade。
_Avoid_: 一般陈述, 背景介绍

**Brief Ready**:
Selection Brief 可进入 Phase 2 的状态：当前 Dimension Profile 内全部 Core Dimension（及已纳入的 Extension Dimension）均已具备 Dimension Answer（含显式 Unconstrained），且每维约束等级已在 Dimension Turn 中由产品确认。
_Avoid_: Phase 1 结束（口语，无检查标准）

**Near-Miss**:
未进入 SoC Shortlist、但接近满足的候选：必须标明违反了哪些 Hard Constraint；用于协助回退放宽约束，其本身不是 Shortlist 成员。
_Avoid_: 备选, 非正式候选（易与 Shortlist 混淆）

**Phase 2 Clarification**:
Phase 2 允许的有限问询，不含产品维度重 grill，共三类：（1）Hard 判定被 Uncertainty / 缺双源 Critical Claim 阻塞时的证据或事实追问；（2）**Spec Detail Probe**（按需规格细节探针）：以 **Probe Turn** 一次一问，取值与 `hard`/`soft`/`unconstrained` 同回确认；（3）导出前对 Shortlist 与 Near-Miss 归属的轻量确认。
_Avoid_: Phase 2 grilling（过宽）, 产品需求回访, 把 Probe 当成完整产品 Dimension Turn

**Spec Detail Probe**:
Phase 2 在公开检索后按需发起的技术向追问：用于补齐 Brief 未覆盖、却对 Hard/Soft 判定或候选分化有实质影响的规格细节。探针集合须经 **形态门控**（Product Family + `sub_form`）。每一探针为一次 **Probe Turn**：与 Phase 1 **Dimension Turn** 同形——同一回复中给出取值与约束等级 `hard` / `soft` / `unconstrained`；Agent 须给推荐等级。等级语义与 Brief 一致：`hard` 不满足则不得入 Shortlist；`soft` 仅影响 Match Band；`unconstrained` 不筛不排。答案写入 SoC Shortlist 本轮口径，**不自动改写** Selection Brief；若实质是新产品能力边界，应建议产品端回 Phase 1 修订 Brief。启发式清单见 [shared/phase2-spec-probes.md](./shared/phase2-spec-probes.md)。
_Avoid_: 每轮必问全表, 跨形态套用探针, apply_as/run_hard/run_soft/note_only（已废止）, Phase 1 产品 Framing 问卷

**Probe Turn**:
Phase 2 对某一 Spec Detail Probe 的单次用户回合：在同一回复中同时给出探针取值与约束等级（hard / soft / unconstrained）；问法对齐 Dimension Turn（推荐答案 + 推荐等级；允许 `B / Hard` 或自定义）。
_Avoid_: 两步等级确认, 取值与等级分问, apply_as
