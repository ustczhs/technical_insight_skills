# 技术规划 Skills

面向技术规划的 Cursor skill **集合**：项目档案、智能硬件调研、主控选型、技术树生长、需求评审等能力簇**各自独立**可调用。因理念一致、风格统一而放在同一仓库，便于维护与扩展——不是总流水线。

运行时统一落在 **Projects Root**（`$PROJECTS_PATHS` / `$PROJECTS_PATH`，默认可 `~/projects`）下的 `$PROJECTS_ROOT/<project_slug>/`；详见 [CONTEXT.md](./CONTEXT.md) 与 [skills/project-dossier/shared/projects-root.md](./skills/project-dossier/shared/projects-root.md)。

包公约：[CONTEXT.md](./CONTEXT.md)  
项目档案：[skills/project-dossier/CONTEXT.md](./skills/project-dossier/CONTEXT.md)  
选型术语：[skills/soc-selection/CONTEXT.md](./skills/soc-selection/CONTEXT.md)  
技术树术语：[skills/grow-a-tech-tree/CONTEXT.md](./skills/grow-a-tech-tree/CONTEXT.md)  
需求评审术语：[skills/requirements-review/CONTEXT.md](./skills/requirements-review/CONTEXT.md)

## 能力簇

| 簇 | 说明 | 运行时路径（相对项目档案） | 目录 |
|----|------|---------------------------|------|
| Project Dossier | 项目建档与活档案 CRUD（单 skill） | `$PROJECTS_ROOT/<project_slug>/`（`PROJECT.md`、`corpus/`） | [skills/project-dossier/](./skills/project-dossier/) |
| Hardware Insight | 智能硬件结构化调研（单 skill） | `…/research/` | [skills/hardware-insight/](./skills/hardware-insight/) |
| Cross-Domain Opportunity | AI×硬件跨域碰撞：广覆盖火花 → 可证伪机会与交接 | `…/opportunities/` | [skills/cross-domain-opportunity-explorer/](./skills/cross-domain-opportunity-explorer/) |
| SoC Selection | 主控选型（Brief → Shortlist，簇内衔接） | `…/selection/` | [skills/soc-selection/](./skills/soc-selection/) |
| Tech Tree | 产品技术树生长（单 skill） | `…/trees/` | [skills/grow-a-tech-tree/](./skills/grow-a-tech-tree/) |
| Requirements Review | 模糊需求澄清 + 价值评审（单 skill） | `…/requirements/<req_slug>/` | [skills/requirements-review/](./skills/requirements-review/) |

簇与簇之间无必然分析耦合；可只安装需要的叶子。分析叶子启动须满足 **Project Dossier Gate**（有 `PROJECT.md`）。后续新增 skill 时遵循 [CONTEXT.md](./CONTEXT.md)。

## Skills（叶子）

| Skill | 角色 | 目录 |
|-------|------|------|
| `project-dossier` | 项目档案建档 / CRUD / sync | [skills/project-dossier/](./skills/project-dossier/) |
| `hardware-insight` | 智能硬件结构化调研 | [skills/hardware-insight/](./skills/hardware-insight/) |
| `cross-domain-opportunity-explorer` | 跨域碰撞找 AI×硬件机会火花 | [skills/cross-domain-opportunity-explorer/](./skills/cross-domain-opportunity-explorer/) |
| `hardware-selection-brief` | 选型 Phase 1：Selection Brief | [skills/soc-selection/hardware-selection-brief/](./skills/soc-selection/hardware-selection-brief/) |
| `soc-shortlist` | 选型 Phase 2：SoC Shortlist（需 Brief Ready） | [skills/soc-selection/soc-shortlist/](./skills/soc-selection/soc-shortlist/) |
| `grow-a-tech-tree` | 卡诺叶清单 → 叶/枝/干/根 + drawio | [skills/grow-a-tech-tree/](./skills/grow-a-tech-tree/) |
| `requirements-review` | 模糊需求 → Clarified Requirement → Value Verdict | [skills/requirements-review/](./skills/requirements-review/) |

## 安装

```bash
git clone https://github.com/ustczhs/technical_insight_skills.git ~/code/technical_insight_skills

# 链到当前项目（默认全部叶子；可改 --only）
~/code/technical_insight_skills/scripts/install-skills.sh \
  --target /path/to/your-project/.cursor/skills

# 或安装为个人 skill，并一并确保可选外部依赖（baoyu-infographic / drawio MCP）
~/code/technical_insight_skills/scripts/install-skills.sh \
  --target ~/.cursor/skills \
  --with-optional-deps
```

只装子集示例：

```bash
./scripts/install-skills.sh --target ~/.cursor/skills \
  --only project-dossier,hardware-insight,grow-a-tech-tree \
  --with-optional-deps
```

可选依赖也可单独确保：

```bash
./scripts/ensure-optional-deps.sh              # baoyu + drawio
./scripts/ensure-optional-deps.sh --only drawio
./scripts/ensure-optional-deps.sh --check      # 仅检查
```

安装永远链接**叶子**目录，不要链整个 `skills/soc-selection/`。  
选型叶子经相对路径读同簇 `../shared/` 与簇内 `CONTEXT.md`。若 Agent 按 symlink 路径（而非 realpath）解析导致读不到，请改以本仓为工作区打开，或确认工具按真实路径解析链接目标。  
drawio MCP 写入 `~/.cursor/mcp.json` 后可能需重启 Cursor 才会出现。

## 用法（按簇）

### 项目档案（`project-dossier`）

```
为「<项目>」建项目档案 / 更新档案 / 登记需求
```

或 `/project-dossier`。产出：`$PROJECTS_ROOT/<project_slug>/PROJECT.md` 等。详见 [skills/project-dossier/README.md](./skills/project-dossier/README.md)。

### 调研（`hardware-insight`）

```
对「<产品/方向>」做智能硬件调研
```

或 `/hardware-insight`。产出：`$PROJECTS_ROOT/<project_slug>/research/`。详见 [skills/hardware-insight/README.md](./skills/hardware-insight/README.md)。

### 跨域机会探索（`cross-domain-opportunity-explorer`）

```
探索「<人群/兴趣/生活场景>」的 AI × 智能硬件机会火花
```

或 `/cross-domain-opportunity-explorer`。原则：覆盖尽量广、检索要新、挖掘要深、对人结论要直接。  
产出：`$PROJECTS_ROOT/<project_slug>/opportunities/`（先看 `SESSION_BRIEF.md`）。详见 [skills/cross-domain-opportunity-explorer/README.md](./skills/cross-domain-opportunity-explorer/README.md)。

### 选型（簇内 Brief → Shortlist）

本簇内两段可硬衔接（与其他簇无关）：

1. `/hardware-selection-brief` → `$PROJECTS_ROOT/<project_slug>/selection/SELECTION_BRIEF.md`（`brief_status` = `brief_ready`）
2. `/soc-shortlist` 加载该 Brief → `SOC_SHORTLIST.md`

v1 Product Family：Companion Robot、Wearable AI。  
详见 [skills/soc-selection/README.md](./skills/soc-selection/README.md)。

### 技术树（`grow-a-tech-tree`）

```
为「<产品/品类>」长技术树
```

或 `/grow-a-tech-tree`。产出：`$PROJECTS_ROOT/<project_slug>/trees/`。详见 [skills/grow-a-tech-tree/README.md](./skills/grow-a-tech-tree/README.md)。

### 需求评审（`requirements-review`）

```
对「<模糊需求>」做需求澄清/价值评审
```

或 `/requirements-review`。产出：`$PROJECTS_ROOT/<project_slug>/requirements/<req_slug>/`。详见 [skills/requirements-review/README.md](./skills/requirements-review/README.md)。
