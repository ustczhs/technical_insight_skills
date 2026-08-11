#!/usr/bin/env bash
# Ensure optional external deps used by this package:
#   - baoyu-infographic (Cursor skill) — hardware-insight Step 8 信息图
#   - drawio MCP (@next-ai-drawio/mcp-server) — grow-a-tech-tree 结构图预览/导出
#
# Default: install if missing. Use --check to only report.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE_DIR="${TECHNICAL_INSIGHT_DEPS_CACHE:-$HOME/.cache/technical_insight_skills/deps}"
SKILLS_DIR="${CURSOR_SKILLS_DIR:-$HOME/.cursor/skills}"
MCP_JSON="${CURSOR_MCP_JSON:-$HOME/.cursor/mcp.json}"
BAOYU_REPO_URL="${BAOYU_SKILLS_REPO:-https://github.com/JimLiu/baoyu-skills.git}"
DRAWIO_MCP_PKG="${DRAWIO_MCP_PACKAGE:-@next-ai-drawio/mcp-server@latest}"
DRAWIO_MCP_PORT="${DRAWIO_MCP_PORT:-6002}"

MODE="ensure" # ensure | check
DEPS="all"    # all | baoyu-infographic | drawio

usage() {
  cat <<'EOF'
Usage:
  ensure-optional-deps.sh [--check] [--only baoyu-infographic|drawio|all]

  --check   Only report missing deps (exit 1 if any missing).
  --only    Limit to one dependency (default: all).

Env overrides:
  CURSOR_SKILLS_DIR   default ~/.cursor/skills
  CURSOR_MCP_JSON     default ~/.cursor/mcp.json
  TECHNICAL_INSIGHT_DEPS_CACHE  git clone cache (default ~/.cache/technical_insight_skills/deps)
  BAOYU_SKILLS_REPO   default https://github.com/JimLiu/baoyu-skills.git
  DRAWIO_MCP_PACKAGE  default @next-ai-drawio/mcp-server@latest
  DRAWIO_MCP_PORT     default 6002
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check) MODE="check"; shift ;;
    --only)
      DEPS="${2:-}"
      shift 2
      ;;
    -h|--help) usage; exit 0 ;;
    *)
      echo "Unknown arg: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

need_baoyu=0
need_drawio=0
case "$DEPS" in
  all) need_baoyu=1; need_drawio=1 ;;
  baoyu-infographic) need_baoyu=1 ;;
  drawio) need_drawio=1 ;;
  *)
    echo "error: --only must be all|baoyu-infographic|drawio" >&2
    exit 1
    ;;
esac

baoyu_skill_path() {
  local candidates=(
    "$SKILLS_DIR/baoyu-infographic/SKILL.md"
    "$SKILLS_DIR/jimliu/baoyu-skills/baoyu-infographic/SKILL.md"
    "$HOME/.agents/skills/baoyu-infographic/SKILL.md"
  )
  local p
  for p in "${candidates[@]}"; do
    if [[ -f "$p" ]]; then
      echo "$p"
      return 0
    fi
  done
  return 1
}

drawio_mcp_configured() {
  python3 - "$MCP_JSON" <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
if not path.is_file():
    sys.exit(1)
try:
    data = json.loads(path.read_text(encoding="utf-8"))
except Exception:
    sys.exit(1)
servers = data.get("mcpServers") or {}
for name, cfg in servers.items():
    blob = json.dumps(cfg).lower()
    if "drawio" in name.lower() or "next-ai-drawio" in blob or "draw-io" in blob:
        sys.exit(0)
sys.exit(1)
PY
}

install_baoyu() {
  mkdir -p "$CACHE_DIR" "$SKILLS_DIR"
  local repo="$CACHE_DIR/baoyu-skills"
  local urls=(
    "$BAOYU_REPO_URL"
    "https://ghproxy.net/${BAOYU_REPO_URL}"
    "https://mirror.ghproxy.com/${BAOYU_REPO_URL}"
    "https://gitclone.com/${BAOYU_REPO_URL#https://}"
  )
  if [[ -d "$repo/.git" ]]; then
    git -C "$repo" pull --ff-only || true
  else
    rm -rf "$repo"
    local ok=0
    local url
    for url in "${urls[@]}"; do
      echo "cloning baoyu-skills from: $url"
      if GIT_TERMINAL_PROMPT=0 git clone --depth 1 --single-branch "$url" "$repo"; then
        ok=1
        break
      fi
      rm -rf "$repo"
    done
    if [[ "$ok" -ne 1 ]]; then
      cat >&2 <<'EOF'
error: failed to clone baoyu-skills (network/GitHub unreachable).

Manual install:
  git clone --depth 1 https://github.com/JimLiu/baoyu-skills.git \
    ~/.cache/technical_insight_skills/deps/baoyu-skills
  ln -s ~/.cache/technical_insight_skills/deps/baoyu-skills/skills/baoyu-infographic \
    ~/.cursor/skills/baoyu-infographic

Or:
  npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-infographic
EOF
      exit 1
    fi
  fi
  local src="$repo/skills/baoyu-infographic"
  if [[ ! -d "$src" ]]; then
    # older layout fallback
    src="$repo/baoyu-infographic"
  fi
  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "error: baoyu-infographic not found in $repo" >&2
    exit 1
  fi
  local dst="$SKILLS_DIR/baoyu-infographic"
  if [[ -e "$dst" || -L "$dst" ]]; then
    rm -rf "$dst"
  fi
  ln -s "$src" "$dst"
  echo "installed: $dst -> $src"
}

install_drawio_mcp() {
  mkdir -p "$(dirname "$MCP_JSON")"
  python3 - "$MCP_JSON" "$DRAWIO_MCP_PKG" "$DRAWIO_MCP_PORT" <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
pkg = sys.argv[2]
port = sys.argv[3]
if path.is_file():
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        data = {}
else:
    data = {}
servers = data.setdefault("mcpServers", {})
# keep existing drawio-like entry if present
for name, cfg in list(servers.items()):
    blob = json.dumps(cfg).lower()
    if "drawio" in name.lower() or "next-ai-drawio" in blob:
        print(f"drawio MCP already present as '{name}' in {path}")
        sys.exit(0)
servers["drawio"] = {
    "command": "npx",
    "args": [pkg],
    "env": {"PORT": str(port)},
}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote drawio MCP entry to {path}")
print("note: restart Cursor (or reload MCP) for the new server to appear")
PY
}

missing=0

if [[ "$need_baoyu" -eq 1 ]]; then
  if path="$(baoyu_skill_path)"; then
    echo "ok: baoyu-infographic -> $path"
  else
    echo "missing: baoyu-infographic"
    missing=1
    if [[ "$MODE" == "ensure" ]]; then
      install_baoyu
      path="$(baoyu_skill_path)" || {
        echo "error: baoyu-infographic install failed" >&2
        exit 1
      }
      echo "ok: baoyu-infographic -> $path"
      missing=0
    fi
  fi
fi

if [[ "$need_drawio" -eq 1 ]]; then
  if drawio_mcp_configured; then
    echo "ok: drawio MCP configured in $MCP_JSON"
  else
    echo "missing: drawio MCP ($MCP_JSON)"
    missing=1
    if [[ "$MODE" == "ensure" ]]; then
      install_drawio_mcp
      if drawio_mcp_configured; then
        echo "ok: drawio MCP configured in $MCP_JSON"
        missing=0
      else
        echo "error: drawio MCP install failed" >&2
        exit 1
      fi
    fi
  fi
fi

if [[ "$MODE" == "check" && "$missing" -ne 0 ]]; then
  exit 1
fi

exit 0
