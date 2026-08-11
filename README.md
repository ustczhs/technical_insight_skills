# 技术规划 Skills

面向技术规划的 Cursor skill **集合**：智能硬件调研、主控选型、技术树生长等能力簇**各自独立**可调用，产出互不影响。因理念一致、风格统一而放在同一仓库，便于维护与扩展——不是总流水线。

包公约：[CONTEXT.md](./CONTEXT.md)  
选型术语：[skills/soc-selection/CONTEXT.md](./skills/soc-selection/CONTEXT.md)  
技术树术语：[skills/grow-a-tech-tree/CONTEXT.md](./skills/grow-a-tech-tree/CONTEXT.md)

## 能力簇

| 簇 | 说明 | 运行时产出根 | 目录 |
|----|------|--------------|------|
| Hardware Insight | 智能硬件结构化调研（单 skill） | `research/` | [skills/hardware-insight/](./skills/hardware-insight/) |
| SoC Selection | 主控选型（Brief → Shortlist，簇内衔接） | `selection/` | [skills/soc-selection/](./skills/soc-selection/) |
| Tech Tree | 产品技术树生长（单 skill） | `trees/` | [skills/grow-a-tech-tree/](./skills/grow-a-tech-tree/) |

簇与簇之间无必然耦合；可只安装需要的叶子。后续新增相关技术规划 skill 时，遵循 [CONTEXT.md](./CONTEXT.md) 的扩展约定。

## Skills（叶子）

| Skill | 角色 | 目录 |
|-------|------|------|
| `hardware-insight` | 智能硬件结构化调研 | [skills/hardware-insight/](./skills/hardware-insight/) |
| `hardware-selection-brief` | 选型 Phase 1：Selection Brief | [skills/soc-selection/hardware-selection-brief/](./skills/soc-selection/hardware-selection-brief/) |
| `soc-shortlist` | 选型 Phase 2：SoC Shortlist（需 Brief Ready） | [skills/soc-selection/soc-shortlist/](./skills/soc-selection/soc-shortlist/) |
| `grow-a-tech-tree` | 卡诺叶清单 → 叶/枝/干/根 + drawio | [skills/grow-a-tech-tree/](./skills/grow-a-tech-tree/) |

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
  --only hardware-insight,grow-a-tech-tree \
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

### 调研（`hardware-insight`）

```
对「<产品/方向>」做智能硬件调研
```

或 `/hardware-insight`。产出：`research/<产品简称>/`。详见 [skills/hardware-insight/README.md](./skills/hardware-insight/README.md)。

### 选型（簇内 Brief → Shortlist）

本簇内两段可硬衔接（与其他簇无关）：

1. `/hardware-selection-brief` → `selection/<slug>/SELECTION_BRIEF.md`（`brief_status` = `brief_ready`）
2. `/soc-shortlist` 加载该 Brief → `SOC_SHORTLIST.md`

v1 Product Family：Companion Robot、Wearable AI。  
详见 [skills/soc-selection/README.md](./skills/soc-selection/README.md)。

### 技术树（`grow-a-tech-tree`）

```
为「<产品/品类>」长技术树
```

或 `/grow-a-tech-tree`。产出：`trees/<slug>/`。详见 [skills/grow-a-tech-tree/README.md](./skills/grow-a-tech-tree/README.md)。
