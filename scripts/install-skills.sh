#!/usr/bin/env bash
# Symlink leaf skills from this package into a Cursor skills directory.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

usage() {
  cat <<'EOF'
Usage:
  install-skills.sh --target <skills-dir> [--only name,name,...] [--force]
                    [--with-optional-deps]

  --target              Destination directory (e.g. /path/to/project/.cursor/skills
                        or ~/.cursor/skills). Created if missing.
  --only                Comma-separated leaf names to install (default: all).
  --force               Replace existing destination paths (rm then ln -s).
  --with-optional-deps  Also ensure baoyu-infographic + drawio MCP
                        (see ensure-optional-deps.sh).

Leaf names:
  project-dossier
  hardware-insight
  hardware-selection-brief
  soc-shortlist
  grow-a-tech-tree
  requirements-review
EOF
}

TARGET=""
ONLY=""
FORCE=0
WITH_OPTIONAL=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --only)
      ONLY="${2:-}"
      shift 2
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --with-optional-deps)
      WITH_OPTIONAL=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "error: --target is required" >&2
  usage >&2
  exit 1
fi

# name -> relative path under skills/
declare -A LEAF_PATHS=(
  [project-dossier]="project-dossier"
  [hardware-insight]="hardware-insight"
  [hardware-selection-brief]="soc-selection/hardware-selection-brief"
  [soc-shortlist]="soc-selection/soc-shortlist"
  [grow-a-tech-tree]="grow-a-tech-tree"
  [requirements-review]="requirements-review"
)

ALL_LEAVES=(project-dossier hardware-insight hardware-selection-brief soc-shortlist grow-a-tech-tree requirements-review)

selected=()
if [[ -z "$ONLY" ]]; then
  selected=("${ALL_LEAVES[@]}")
else
  IFS=',' read -ra raw <<<"$ONLY"
  for name in "${raw[@]}"; do
    name="$(echo "$name" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    [[ -z "$name" ]] && continue
    if [[ -z "${LEAF_PATHS[$name]+x}" ]]; then
      echo "error: unknown leaf '$name'" >&2
      usage >&2
      exit 1
    fi
    selected+=("$name")
  done
fi

mkdir -p "$TARGET"

for name in "${selected[@]}"; do
  src="$ROOT/skills/${LEAF_PATHS[$name]}"
  dst="$TARGET/$name"
  if [[ ! -d "$src" ]]; then
    echo "error: missing source directory: $src" >&2
    exit 1
  fi
  if [[ -e "$dst" || -L "$dst" ]]; then
    if [[ "$FORCE" -eq 1 ]]; then
      rm -rf "$dst"
    else
      echo "skip (exists): $dst  (use --force to replace)"
      continue
    fi
  fi
  ln -s "$src" "$dst"
  echo "linked: $dst -> $src"
done

if [[ "$WITH_OPTIONAL" -eq 1 ]]; then
  deps=()
  for name in "${selected[@]}"; do
    case "$name" in
      hardware-insight) deps+=(baoyu-infographic) ;;
      grow-a-tech-tree) deps+=(drawio) ;;
    esac
  done
  if [[ ${#deps[@]} -gt 0 ]]; then
    uniq_deps=$(printf '%s\n' "${deps[@]}" | sort -u)
    while IFS= read -r d; do
      [[ -z "$d" ]] && continue
      "$ROOT/scripts/ensure-optional-deps.sh" --only "$d"
    done <<<"$uniq_deps"
  fi
fi
