# SoC Selection（选型簇）术语

本文件是 **soc-selection** 能力簇的领域术语权威。包级公约见仓库根 [CONTEXT.md](../../CONTEXT.md)。

选型与检索遵循 **第一性原理**：以 Brief 中可验证的能力与约束（算力/接口/功耗热/音频视觉链路/软件可落地等）判定去留，**不以**市场品类标签、厂商营销定位或「通常用于某形态」作为整类排除依据。跨形态复用常见（例如 AI 眼镜视觉 SoC 用于桌面机器人底座、视觉蓝牙耳机等），须纳入搜索与比较；类标差异用 Match Band / 取舍说明表达，而非默杀。

**Product Family 只决定 Dimension Profile（怎么问）**；Phase 2 检索范围由 **Silicon Class**（形态种子）+ **Application Domain**（行业加扫）+ **Hard 触发的相邻 Class** 叠成，见 [shared/vendor-seeds.md](./shared/vendor-seeds.md)、[shared/silicon-classes.md](./shared/silicon-classes.md)、[shared/application-domains.md](./shared/application-domains.md)。禁止用 Family 挂靠去间接决定厂商必扫矩阵或探针包。

v1 内置两个 Product Family：陪伴机器人、可穿戴 AI；另支持 Out-of-Family（仅 Profile 缺口）。

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
Phase 2 的主交付物：一组满足 Selection Brief **Hard Constraint**（及已确认 `grade=hard` 探针）的候选型号，附对比维度与取舍说明；数量由筛选结果决定，不预设上下限，也不强制决出唯一赢家。主 Silicon Class 与相邻 Class、Application Domain 决定**必扫覆盖**；满足 Hard 的料号可入选（含矩阵外），用 Match Band 反映贴合度（Domain 命中可抬档）。落盘形态为纯 Markdown：**结论先行**（推荐表 + 取舍摘要 + Near-Miss 一览），**论据与过程随后**（Hard 表、候选卷宗、厂商扫描、探针）；不使用嵌入 YAML 或 YAML front matter。
_Avoid_: 最终选型结论（冒充唯一拍板）, Recommended SoC, 固定 3–5 款清单, Shortlist YAML, 仅因类标不符整类删除, 先堆证据/扫描表再揭示选了谁, 空话式「较适合」结论句

**Silicon Class**:
结构化硅片形态枚举（如 `ap_som`、`display_mcu`、`audio_sip`），是 Phase 2 **形态种子表与 Spec Detail Probe 包**的主键。Brief 须有且仅有一个 **primary** Class，外加 0～N 个 **adjacent** Class；取值见 [shared/silicon-classes.md](./shared/silicon-classes.md)。
_Avoid_: 芯片类型（口语）, Target Silicon Class 散文段落（可作说明，权威以枚举 id 为准）, 用 Product Family 代替 Class

**Target Silicon Class**:
Brief 中对 Silicon Class 选择的可读说明区（主类 + 相邻类 + 理由）；权威仍是元信息表中的 `primary_silicon_class` / `adjacent_silicon_classes`。
_Avoid_: 把本段散文当成唯一机读输入, 唯一零件号

**Application Domain**:
从产品概念确认的**应用域 / 整机品类**标签（可多选，如 `motorcycle`、`light_ev`），决定 Phase 2 的**行业加扫义务**，与 Silicon Class 叠加；不是 Product Family。词表见 [shared/application-domains.md](./shared/application-domains.md)。
_Avoid_: 产品品类（与 Family 口语混淆时）, 只用 Soft 文案「优先车载」代替域标签

**Seed Extension Flag**:
Brief 元信息 `needs_seed_extension`：当自定义 Domain / 未登记 Class 映射不上种子表时须为 true；Phase 2 须显式降级声明并尽力检索，不得假装该域/类已矩阵覆盖完毕。
_Avoid_: seed_gap 一等状态（v1 不单独立名）, 静默忽略未登记域

**Vendor Coverage Matrix**:
Phase 2 的**国内 + 国外/跨国厂商必扫清单**，按 **Silicon Class** 分段，并叠加 **Application Domain** 加扫表（见 [shared/vendor-seeds.md](./shared/vendor-seeds.md)）。每一行须在 SoC Shortlist 的厂商扫描表落盘（`assessed` / `no_public_part` / `out_of_scope`）。矩阵是覆盖义务，**不是** Shortlist 白名单；未完成主 Class ∪ 相邻 Class ∪ Domain 加扫行则不得 `shortlist_status=complete`。
_Avoid_: 按 Product Family 选矩阵, 把矩阵外合格料默杀, 只扫 3～5 家头部就宣称检索完成, 单语泛搜否定某厂商

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
Phase 1 对某一维度的单次用户回合：在同一回复中同时给出 Dimension Answer 与约束等级（hard / soft / unconstrained）；Agent 须提供推荐等级，但不再拆成「先取值、再单独确认等级」两问。题干（单选），末项「其他（请补充）」。**逐步确认一次一维**；**Lazy 跳过等人、采用推荐。**
_Avoid_: 两步等级确认, 取值与等级分问, 一批多维连发

**Brief Source**:
选型线上供 Phase 1 使用的外部输入文件，落在 Case Workspace（如 `$PROJECTS_ROOT/<project_slug>/selection/sources/`）。是 Selection Brief 的输入溯源，不是 Artifact；Portal 负责上传与落盘，**不**在门户侧做维度映射。可在「开始 Brief」前上传（0～N），也可在 Brief Ready 前追加。追加不得静默改写**已确认**的 Dimension Answer / grade；若新源与已确认维冲突，须显式闸门询问是否重开该维的 Dimension Turn。v1 **承诺**可抽取：`.txt` / `.md` / `.csv` / `.xlsx`/`.xls` / 含文本层的 `.pdf` / `.docx`。图片与扫描件 PDF 为**尽力**（失败写入 Source Residue「未能抽取」，不阻塞 Phase 1）。
_Avoid_: 附件（通用协作）, 第三种选型交付物, Portal 产出正式约束, v1 对图片/扫描件与文本格式同等成功承诺, 新源静默覆盖已确认维

**Source Residue（未映射摘录）**:
从 Brief Source 抽出、但无法诚实映射到当前 Dimension Profile（含已纳入 Extension）的内容摘要；写入 Selection Brief 附录供溯源，**不**构成 Hard/Soft。若内容像选型缺口，Agent 可提议纳入 Extension Dimension，经产品确认后再走 Dimension Turn。
_Avoid_: 静默丢弃, 自动自定义维并当正式约束

**Source Provenance（源溯源）**:
某 Dimension Answer / 冲突裁定与 Brief Source 之间的可追溯记录。升格后写入该维备注（文件名 + 短摘录），并在 Brief 附录保留 Source 清单、Source Residue 与冲突裁定；Phase 2 仍只消费正式 Hard Constraint / Soft Preference，不直接消费溯源附录。
_Avoid_: 定稿 Brief 抹掉来源, 维度总表强制 source 列撑爆主表, Phase 2 按溯源附录筛选

**Source-Derived Draft**:
由 **Phase 1 Skill Run**（`hardware-selection-brief`）从 Brief Source 抽取并映射到 **已确认** Product Family 的 Dimension Profile 后的**未确认**草案：含建议的 Dimension Answer 与建议 grade，以及可追溯到原文的摘录。Brief Source 可在 Family 确认前上传，但**不得**在 Family 未定时产出跨 Profile 的结构化草案。升格路径与普通维度相同：走 **Dimension Turn**（逐步确认一次一维；Lazy 用推荐升格）；不引入单独的「Draft 总览确认」回合类型。映射不上的内容进 **Source Residue**，不进 Draft。多份 Brief Source 对同一维冲突时：仍只出**一条** Draft，题面标注各方摘录，由 Agent 给一条推荐（默认偏更严或更可验证的 Spec），用户在 Dimension Turn 裁定（Lazy 采用该推荐）。未确认前不得计入 Brief Ready，也不得静默写入正式 Hard Constraint / Soft Preference（Lazy 的「确认」= 采用推荐并标注）。
_Avoid_: 约束项（口语）, 直接当 Hard, 静默写入 Brief, Family 未定就绑维度 id, Draft Review Turn, Portal 确定性管道直接出 Hard/Soft, 同维多条并行 Draft, 后上传静默覆盖先上传

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
共享同类 SoC 选型**问卷**结构的产品族（如陪伴机器人、可穿戴 AI）；决定采用哪套 Dimension Profile。**不**决定 Vendor Coverage Matrix，也**不**门控 Spec Detail Probe。
_Avoid_: 产品品类（与 Application Domain 混淆）, 用 Family 挂靠代替 Silicon Class / Domain

**Dimension Profile**:
某一 Product Family 下的维度配置：该族的 Core Dimension 子集、配套 Extension Dimension 包，以及对应的 Framing–Spec Mapping。
_Avoid_: 模板, 问卷模板（可作俗称，正式用语用 Dimension Profile）, 检索种子表

**Companion Robot**:
v1 的一个 Product Family：移动或车载等形态的陪伴交互机器人问卷。Core Dimension：产品子形态、算力档位、端侧 AI、显示、摄像与视频、高速互联、功耗与散热、工作环境、目标软件栈、交付形态、成本带、供货与生命周期。推荐 Silicon Class 常为 `ap_som`，但以 Brief 确认的 Class / Domain 为准。
_Avoid_: 服务机器人（若未区分用途则勿混用）, 把本 Family 的厂商矩阵当成唯一检索范围

**Wearable AI**:
v1 的一个 Product Family：可穿戴 AI 硬件问卷，含视觉蓝牙耳机、AI 眼镜等形态。Core Dimension：产品子形态、功耗与续航预算、封装与尺寸约束、音频链路、无线连接、端侧 AI、传感与视觉、目标软件/固件栈、成本带、供货与生命周期。推荐 Silicon Class 常为 `audio_sip`，但以 Brief 确认的 Class / Domain 为准。
_Avoid_: 仅写「耳机」而排除其他可穿戴 AI, 把本 Family 的厂商矩阵当成唯一检索范围

**Out-of-Family**:
当前已支持 Product Family 的 Dimension Profile 都无法诚实覆盖产品概念时的 Family 取值：走轻量约束维（见 Profile）。**只表示问卷/Profile 缺口**；只要 Silicon Class（与 Application Domain）已结构化确认，Phase 2 仍按 Class∪Domain 正常检索，不再一刀切「质量不保证」。
_Avoid_: 其他, 自定义品类（未配套 Profile 时）, 把 Out-of-Family 当成检索降级开关

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
Selection Brief 可进入 Phase 2 的状态：当前 Dimension Profile 内全部 Core Dimension（及已纳入的 Extension Dimension）均已具备 Dimension Answer（含显式 Unconstrained），且每维约束等级已在 Dimension Turn 中确认（逐步确认=产品确认；Lazy=推荐值）。
_Avoid_: Phase 1 结束（口语，无检查标准）

**Near-Miss**:
未进入 SoC Shortlist、但接近满足的候选：必须标明违反了哪些 Hard Constraint；用于协助回退放宽约束，其本身不是 Shortlist 成员。
_Avoid_: 备选, 非正式候选（易与 Shortlist 混淆）

**Phase 2 Clarification**:
Phase 2 允许的有限问询，不含产品维度重 grill，共三类：（1）Hard 判定被 Uncertainty / 缺双源 Critical Claim 阻塞时的证据或事实追问；（2）**Spec Detail Probe**（按需规格细节探针）：以 **Probe Turn** 一次一问，取值与 `hard`/`soft`/`unconstrained` 同回确认；（3）导出前对 Shortlist 与 Near-Miss 归属的轻量确认。
_Avoid_: Phase 2 grilling（过宽）, 产品需求回访, 把 Probe 当成完整产品 Dimension Turn

**Spec Detail Probe**:
Phase 2 在公开检索后按需发起的技术向追问：用于补齐 Brief 未覆盖、却对 Hard/Soft 判定或候选分化有实质影响的规格细节。探针集合须经 **Silicon Class 门控**（主 Class，可选 `sub_form` / Extension 细化）。每一探针为一次 **Probe Turn**：与 Phase 1 **Dimension Turn** 同形——同一回复中给出取值与约束等级 `hard` / `soft` / `unconstrained`；Agent 须给推荐等级。等级语义与 Brief 一致：`hard` 不满足则不得入 Shortlist；`soft` 仅影响 Match Band；`unconstrained` 不筛不排。答案写入 SoC Shortlist 本轮口径，**不自动改写** Selection Brief；若实质是新产品能力边界，应建议产品端回 Phase 1 修订 Brief。启发式清单见 [shared/phase2-spec-probes.md](./shared/phase2-spec-probes.md)。
_Avoid_: 每轮必问全表, 按 Product Family 门控探针, apply_as/run_hard/run_soft/note_only（已废止）, Phase 1 产品 Framing 问卷

**Probe Turn**:
Phase 2 对某一 Spec Detail Probe 的单次用户回合：在同一回复中同时给出探针取值与约束等级（hard / soft / unconstrained）；问法对齐 Dimension Turn（推荐答案 + 推荐等级；末项「其他（请补充）」）。**Lazy 采用推荐、不等人。**
_Avoid_: 两步等级确认, 取值与等级分问, apply_as
