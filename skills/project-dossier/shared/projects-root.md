# Projects Root 解析与固化

档案**不**写在任意代码仓库根下的相对 `projects/`，而写在机器级的 **Projects Root**（固定父目录）下：

```
$PROJECTS_ROOT/<project_slug>/
```

本机示例：`/home/tcl/projects/aime/`。

## 解析顺序（Agent 每次启动 project-dossier / 项目闸门时执行）

按优先级取**第一个非空**值作为候选路径，并展开 `~`：

1. 环境变量 **`PROJECTS_PATHS`**（用户常用名）
2. 环境变量 **`PROJECTS_PATH`**（本机 bashrc 历史名；与上者等价）
3. 配置文件：`$HOME/.config/technical-insight-skills/projects_root`（单行绝对路径）
4. 默认：`$HOME/projects`

得到候选后：

| 情况 | 动作 |
|------|------|
| 目录已存在且可写 | 采用为 `PROJECTS_ROOT` |
| 目录不存在 | **`mkdir -p`** 创建，再采用 |
| 路径存在但是文件（非目录） | 停止并请用户改路径，勿覆盖 |

向用户**简述**本次采用的 `PROJECTS_ROOT`（一行即可）。无需每条路径都追问，除非创建了新目录或改写了固化配置——此时告知「已创建/已固化」。

## 固化（固定下来）

在确认 `PROJECTS_ROOT` 后，**必须**执行固化，使其它终端/其它电脑下次可复用：

1. **配置文件**（跨 shell，优先）：
   ```bash
   mkdir -p "$HOME/.config/technical-insight-skills"
   printf '%s\n' "$PROJECTS_ROOT" > "$HOME/.config/technical-insight-skills/projects_root"
   ```
2. **Shell 环境**（便于 `echo $PROJECTS_PATHS`）：若当前 shell 未导出，或与已解析根不一致，则向用户登录 shell rc 追加/更新（检测 `~/.bashrc`，若无则 `~/.profile`）：
   ```bash
   export PROJECTS_PATHS="…绝对路径…"
   export PROJECTS_PATH="…同一绝对路径…"   # 兼容旧名
   ```
   - 若 rc 中已有同名 export：就地更新为新绝对路径，勿重复堆积多行。
   - **不要**改 git config 或其它无关配置。
3. 当前 Agent 会话内：`export PROJECTS_PATHS` 与 `export PROJECTS_PATH` 到同一路径，供后续命令使用。

可用本 skill 脚本一键完成（推荐）：

```bash
bash <本 skill 或包内路径>/scripts/ensure-projects-root.sh
# 打印：PROJECTS_ROOT=...
```

## 其它电脑

无预置环境变量、无配置文件时：走默认 `$HOME/projects` → 自动创建 → 写入配置文件 + shell rc。用户若要改位置：设置 `PROJECTS_PATHS` 后重新跑 ensure，或改配置文件后再 ensure。

## 与工作区的关系

- **唯一写入根** = `$PROJECTS_ROOT/<project_slug>/`
- 当前 Cursor 工作区（如某代码仓）里的相对 `projects/`、以及仓库根级旧 `research/` 等：**不再作为新写入目标**；若发现仅提示迁移。
