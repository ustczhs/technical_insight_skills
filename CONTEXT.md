# 技术规划 Skills（包公约）

本仓库是**技术规划 skill 的集合**：各能力簇独立可调用，产出互不影响；因理念一致、风格统一而放在一起，便于维护与后续扩展。  
不是总流水线；簇与簇之间无必然耦合。某一簇内部若有多段流程（例如选型 Brief → Shortlist），属于该簇自己的契约。

领域术语：各簇/skill 自管（选型见 [skills/soc-selection/CONTEXT.md](./skills/soc-selection/CONTEXT.md)；技术树见 [skills/grow-a-tech-tree/CONTEXT.md](./skills/grow-a-tech-tree/CONTEXT.md)）。本文件只定义**包级公约**。

## Language

**Technical Planning Skill Package**:
面向技术规划的 Cursor skill 集合。根 README 按能力簇列表呈现；用户可只安装需要的叶子 skill。安装路径：整包 clone 后，symlink **叶子** skill 目录（勿把多 skill 簇目录当成一个 skill 安装）。
_Avoid_: 强制全簇串联成一条教程, 把本仓写成单一产品流水线, 仅假定本仓已打开而不给安装步骤, 把 `skills/soc-selection` 直接 symlink 成单一 skill, SoC Selection Grill / AI Hardware Insight 等旧仓库身份

**Capability Cluster**:
仓库内按能力边界划分的一级分组。簇可以只含一个叶子 skill（如 `skills/hardware-insight/`、`skills/grow-a-tech-tree/`），也可以含多个叶子 skill 及簇内 `shared/`（如 `skills/soc-selection/`）。Cursor 安装永远按**叶子**分别 symlink。各簇运行时产出使用**独立的工作区根目录**，互不读写对方产物。本地可有 `examples/`（**默认不入库**，见根 `.gitignore`），与运行时产出根区分。
_Avoid_: 把簇目录直接当成一个 skill 名安装, 在仓库根建跨簇 shared 把簇耦在一起, 把本地 `examples/` 与运行时产出目录混用或提交进公开仓库

**Leaf Skill**:
可被 Cursor 发现并调用的最小单位：含 `SKILL.md`（及可选 front matter `name` / `description`）的目录。选型簇内的 `hardware-selection-brief`、`soc-shortlist` 各是一个叶子。
_Avoid_: 把簇 README 或 shared 目录当作可安装 skill

**Skill README**:
每个叶子（或簇）目录下一份面向人的简介：角色、何时用、本簇产出根路径；流程细节以该 skill 的 `SKILL.md` 为准。
_Avoid_: 把完整 Step 流程只写在 README, README 与 SKILL.md 双源维护同一套细则, 在叶子 README 里复述与其他簇的「无强制先后」

**Runtime Output Root**:
某一簇写入消费方工作区的顶层目录约定。当前：`research/`（调研）、`selection/`（选型）、`trees/`（技术树）。各簇下可选的 `examples/` 仅供本地对照，**不作为公开包内容**（已在 `.gitignore`）。
_Avoid_: 多簇共用同一产出根, 把示例目录当成运行时落盘位置, 将含具体产品结论的 examples 提交入库

**Cluster Independence**:
簇与簇之间无数据契约、无调用先后要求；不自动把一簇产物改写成另一簇产物。用户可在会话中自行参考任意已有文档，但 skill 规范不建立跨簇交接闸门。
_Avoid_: 调研→Brief→技术树强制流水线, 包级「软衔接」字段映射表作为硬规范

## 扩展约定（新增能力簇）

新增技术规划相关 skill 时，保持与现有簇同风格：

| 项 | 要求 |
|----|------|
| 目录 | `skills/<cluster>/`；单 skill 簇可将叶子直接放在该目录；多 skill 簇再挂叶子子目录 |
| 人读 | 簇或叶子 `README.md`（何时用 / 产出根；不写完整流程） |
| Agent | 每个叶子 `SKILL.md` + `description`（触发词不抢其他簇） |
| 术语 | 簇内或 skill 内 `CONTEXT.md`；**勿**把簇专有词堆进仓库根 CONTEXT |
| 产出 | 独立的 Runtime Output Root；本地 `examples/` 可选且默认不入库 |
| shared | **仅簇内**；禁止新建包级 shared 耦合多簇 |
| 安装 | 列入 [scripts/install-skills.sh](./scripts/install-skills.sh) 的叶子列表 |
| 可选外部依赖 | 若需要仓外 skill/MCP，写入 ensure-optional-deps 并由 SKILL 在使用前调用 |

## 调用与 description 策略

| 策略 | 说明 |
|------|------|
| `description` | 只写本 skill 的触发语与边界；可标明属 Technical Planning Skill Package；**不要**把其他簇的关键词当作主触发 |
| `disable-model-invocation: true` | **默认**用于需显式调用、grilling 成本高或依赖上游工件的叶子（当前：选型两叶子、技术树） |
| 允许自动触发 | 仅当该 skill 适合「用户一提相关意图即可进入」、且不会与其他簇抢调用时（当前：`hardware-insight`）。新增时须在该 skill README 注明理由 |

_Avoid_: 把任一 skill 的 description 写成规划总入口, 无说明地统一打开/关闭所有叶子的 model invocation

## 可选外部依赖

部分叶子在**可选能力**上依赖仓外 skill / MCP（非簇间耦合）：

| 依赖 | 用途 | 谁需要 | 安装 |
|------|------|--------|------|
| `baoyu-infographic` | 调研 Step 8 可选信息图 | `hardware-insight` | [scripts/ensure-optional-deps.sh](./scripts/ensure-optional-deps.sh) |
| drawio MCP（`@next-ai-drawio/mcp-server`） | 技术树结构图预览/导出 | `grow-a-tech-tree` | 同上 |

约定：Agent 在用到对应能力前运行 ensure 脚本（缺则自动安装）；安装失败则**降级跳过该可选能力**，不阻塞主交付物。`install-skills.sh --with-optional-deps` 可在装叶子时一并确保。

_Avoid_: 把可选外部依赖写成硬前置导致主流程无法跑, 在包内 vendor 整份第三方 skill 源码（除非许可证与维护策略明确要求）
