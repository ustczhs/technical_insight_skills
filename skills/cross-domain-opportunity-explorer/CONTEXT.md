# cross-domain-opportunity-explorer

本文件是跨域机会探索的术语权威。它与调研、需求评审、选型和技术树无数据契约；只产出可验证的机会假设与交接材料。全链路指本簇内的商业机会决策闭环，不是跨簇总编排。

## Language

**Commercial Opportunity Loop**:
本 skill 负责的完整决策链：Seed → People Cell → 场景与痛痒 → Opportunity Spark 碰撞 → 证据加厚 → 四杀伤概念卡 → shortlist → 最小验证 → Handoff Pack。止于交接，不自动启动其他簇。
_Avoid_: 跨簇总流水线, 把调研/选型/技术树编进本 skill, 停在创意清单而无商业可证伪层, 无火花碰撞的纯筛选流水线

**Handoff Pack**:
每个 shortlist 概念一份一页交接物，路径 `concepts/<concept_slug>/HANDOFF_PACK.md`；另有批次级 `HANDOFF_INDEX.md`。内容仅含下游开工所需：People Cell、场景、四杀伤结论、证据指针、验证状态、建议入口与勿重读清单。
_Avoid_: 仅口头建议“去跑 hardware-insight”, 把整棵 opportunities/ 当作交接物, 把验证设计与交接混成一个无索引文件

**Decision Grill**:
对人的五闸门：Seed/范围、排除轴、Shortlist 资源、首个验证对象、交接去向。每次一题、选择题（2–4 实质选项 + 推荐 + 自定义）；仅当会显著改变结论时触发。
_Avoid_: 每步问“然后呢”, 把偏好确认伪装成 Grill, 一次抛多题, 把假设杀伤题改成对人审讯

**Hypothesis Grill**:
对候选机会的固定杀伤问题集（付费、留存、手机替代、硬件必要性、最危险假设等）；默认由 Agent 写入卡片与矩阵，仅当杀不死也活不透时升级为 Decision Grill。
_Avoid_: 只写优点不写杀伤, 用红队口号代替可证伪判据, 把假设 Grill 变成对人审讯

**People Cell**：
最小探索单位：`人群 × 地域/文化 × 阶段/角色 × 场景 × 目标`。兴趣、教育、年龄、收入或健康状态单独出现均不足以构成一个 Cell。
_Avoid_: 泛称“年轻人”“高知人群”“健身人群”后直接下结论

**Seed Triad**:
人群种子三路并行：① 兴趣/活动 ② 阶段×角色×消费/采纳（含待验证的采纳假设）③ 状态/场景主题（守医疗边界）。再交叉成 People Cell；广筛默认追求种子与 Cell **尽量多**，以增大火花碰撞面。
_Avoid_: 只按兴趣建人群, 把「高学历/高消费」写成已证实属性, 为省事故意压薄种子池

**Landscape**：
一批 People Cell 的覆盖地图，含入选、暂缓、排除和证据缺口；它追求可追溯的**高覆盖**，不宣称人群穷尽。默认偏向多多益善的种子与 Cell，再用 Funnel Depth 控制深写。
_Avoid_: 无来源的大而全人群罗列, 用过小批次扼杀碰撞面

**Need Signal**：
与具体场景相连的功能、情绪、社交或风险线索；标注为 fact、voice、observation、inference 或 hypothesis。
_Avoid_: “用户需要 AI”“市场很大”等脱离情境的断言

**Pain / Itch**：
Pain 是高频损失、摩擦、失败或安全风险；Itch 是身份、审美、仪式感、成就、展示或社群认可的未满足增益。两者均可成立，但需分开排序。
_Avoid_: 只按痛点严重度淘汰情绪/表达型机会

**Opportunity Card**：
一项可被证伪的产品+商业机会：人群、场景、任务、替代方案、证据、介入形态、四杀伤假设、风险和最小验证齐全。
_Avoid_: 只有功能清单或一句产品口号的“创意”, 有方案无商业杀伤假设

**Commercial Hypothesis**:
用四杀伤假设表达的可证伪商业主张；未写齐四项不得标为 shortlist。
_Avoid_: “市场很大”“AI 很热”式口号, 用 TAM 数字代替谁付钱/为何付钱

**Four Kill Hypotheses**:
每张机会卡必写的四项可证伪假设：① 谁付钱（购买者与使用者分离时分开写）② 为何付钱（相对现状的损失或增益锚）③ 为何不是手机/通用穿戴 ④ 为何能反复用（频率×摩擦）。规模类数字仅作可选背景且默认 `hypothesis`。
_Avoid_: 把定价/TAM/供应链当 shortlist 硬门槛, 四项写成不可证伪的愿景句

**AI-Hardware Fit**：
一项需求是否存在可靠信号、可解释的 AI 判断、有效行动闭环，以及手机不可充分替代的物理介入理由。
_Avoid_: 因有 AI 或传感器而默认值得做硬件

**Medical Boundary**：
涉及诊断、治疗、疗效承诺、医疗器械分类或高后果健康建议的边界。此类机会仅可记录，不可按普通消费产品推荐。
_Avoid_: 对失眠、焦虑、康复等状态做诊断或疗效宣称

**Handoff Route**:
交接去向的默认分流：证据/四杀伤未齐 → 本簇 deep-dive；概念可作 Requirement Seed 但值不值得做不明 → `/requirements-review`；付钱与需求逻辑已过关、需竞品/技术/市场深证 → `/hardware-insight`。医疗边界仅记录并转人工合规，不进 shortlist。均不自动启动下游。
_Avoid_: 默认一律 hardware-insight, 无规则让用户裸选, 把商业杀伤外包给调研簇

**Validation Brief**：
针对最危险假设的最小实验计划，优先验证真实痛点、付费、持续使用和硬件必要性，而非先做完整产品。
_Avoid_: 未验证即进入量产、完整 PRD 或芯片选型

**Loop Stage**:
本 skill 固定七段：章程 → 人群地图 → 证据与痛痒旅程 → 火花碰撞（Spark Board）→ 概念与四杀伤 → 组合筛选 → 验证与交接。发散在火花段最大化；收敛在四杀伤之后。
_Avoid_: 每步结束等人发令, 把七段拆成跨簇流水线, 无 Handoff Pack 的“完成”, 用筛选扼杀火花段

**Funnel Depth**:
薄记尽量广；完整 Opportunity Card 仅 candidate（≤8）；shortlist ≤3 且须 fact/voice；Handoff 仅 shortlist。
_Avoid_: 每个点子开完整卡, 用过小人群池冒充广筛, 无 fact/voice 进 shortlist

**Breadth Floor**:
landscape **下限**（鼓励超出、不设上限）：兴趣 ≥40、角色/阶段 ≥15、状态 ≥10；入选 Cell ≥40（目标 50–80）；去重后火花 ≥50（目标 ≥80）。未达下限不得宣称广筛完成。
_Avoid_: 把下限当目标, 用假 URL 凑条数, 达不到就假装完成

**Opportunity Spark**:
跨域碰撞产生的可命名机会火花：至少一个 People Cell、一个场景约束、一种介入形态；允许大胆与未证伪，默认标 `hypothesis`。先入 Spark Board，再经证据与四杀伤晋升。
_Avoid_: 无场景约束的“某人群需要 AI”, 未碰撞直接写成 shortlist 结论

**Constraint Lens**:
用于激发火花的场景约束透镜，例如双手占用、瞬间不可错过、视线被占、恶劣环境、社交展示、长时间等待、教学/陪练、隐私敏感。透镜用于发散，不代替证据。
_Avoid_: 用透镜口号代替真实行为观察, 把透镜清单当成穷尽真理, 火花无 Unique Friction

**Spark Board**:
批次级火花板 `SPARK_BOARD.md`：记录约束×形态碰撞结果、野念头与待晋升项；在完整机会卡之前产出。
_Avoid_: 把火花板当成已验证需求清单, 跳过火花直接只写深卡

**Breadth First**:
覆盖面尽量广：种子、Cell、火花只设下限不设上限；用 Funnel Depth 控制深写，不用缩小池子控制成本。
_Avoid_: 为省检索故意压到下限附近, 把「12–24 个 Cell」当默认

**Recency First**:
外部证据优先最近 12 个月的可核验来源；查询应带年份或「最新」意图。>24 个月的资料只作趋势/背景，须标明时效局限。
_Avoid_: 用过时评测当现状, 无日期的厂商页当 fact, 历史帖外推当年付费

**Evidence Budget**:
landscape 每 Cell 检索 ≤2 次；深证只跟 candidate/shortlist（每条 ≥2 条带 URL 的 fact 或 voice）。预算用在高约束节点，不均摊到全部 Cell。
_Avoid_: 对 50+ Cell 全量深搜, 对 shortlist 零检索, 用假 URL 凑条数

**Spark Score**:
晋升用的五维 0–2 分：约束强度、替代不足、AI 可触点、差异化、证据线索。candidate 须写出总分；头戴/眼戴在 candidate 中 ≤50%。
_Avoid_: 凭语感从 80 条里随手挑眼镜, 全是「某兴趣 × 智能眼镜」同构

**Unique Friction**:
火花必须写清不可用套话替代的场景摩擦（几秒窗口、哪只手被占、什么环境）。同一杀伤句全板出现 ≥5 次则后条无效，须合并或重写。
_Avoid_: 连续「App 够吗」「手机够吗」模板杀伤

**Seed Spark**:
用户已有的场景直觉（如「上鱼瞬间双手被占」）置顶碰撞，再反向扩 Seed/Cell；它是加速器，不替代广筛。
_Avoid_: 丢掉用户直觉重撒 40 个兴趣, 或只围着这一条不再扩池

**Direct Presentation**:
对人只给 `SESSION_BRIEF.md`：结论先行、Top 火花、关键杀伤、下一步；表格与长清单留在产物文件。
_Avoid_: 对话里贴完整 SPARK_BOARD, 用过程日志代替结论

**Killed Pattern**:
已否决的空壳模式（纯品类+AI、手机已够的云台跟拍、疗效宣称等），下批碰撞前对照，避免重复造轮子。
_Avoid_: 把 killed 当永久真理而不再检验新证据
