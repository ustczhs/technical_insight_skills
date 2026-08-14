#!/usr/bin/env bash
# Resolve, create, and persist Projects Root for project-dossier.
# Prints: PROJECTS_ROOT=<abs-path>
set -euo pipefail

CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/technical-insight-skills"
CONFIG_FILE="$CONFIG_DIR/projects_root"

expand_path() {
  local p="$1"
  if [[ "$p" == ~* ]]; then
    p="${p/#\~/$HOME}"
  fi
  # trim
  p="${p#"${p%%[![:space:]]*}"}"
  p="${p%"${p##*[![:space:]]}"}"
  printf '%s' "$p"
}

read_config() {
  if [[ -f "$CONFIG_FILE" ]]; then
    head -n 1 "$CONFIG_FILE" | tr -d '\r'
  fi
}

candidate=""
if [[ -n "${PROJECTS_PATHS:-}" ]]; then
  candidate="$(expand_path "$PROJECTS_PATHS")"
elif [[ -n "${PROJECTS_PATH:-}" ]]; then
  candidate="$(expand_path "$PROJECTS_PATH")"
else
  cfg="$(read_config || true)"
  if [[ -n "${cfg:-}" ]]; then
    candidate="$(expand_path "$cfg")"
  else
    candidate="$(expand_path "$HOME/projects")"
  fi
fi

if [[ -e "$candidate" && ! -d "$candidate" ]]; then
  echo "error: PROJECTS_ROOT path exists but is not a directory: $candidate" >&2
  exit 1
fi

if [[ ! -d "$candidate" ]]; then
  mkdir -p "$candidate"
  echo "created: $candidate" >&2
fi

# persist config
mkdir -p "$CONFIG_DIR"
printf '%s\n' "$candidate" > "$CONFIG_FILE"

# persist shell exports (bashrc preferred)
rc=""
if [[ -f "$HOME/.bashrc" ]]; then
  rc="$HOME/.bashrc"
elif [[ -f "$HOME/.profile" ]]; then
  rc="$HOME/.profile"
fi

upsert_export() {
  local name="$1" value="$2" file="$3"
  local line="export ${name}=\"${value}\""
  if grep -qE "^[[:space:]]*export[[:space:]]+${name}=" "$file" 2>/dev/null; then
    # replace first matching export line
    local tmp
    tmp="$(mktemp)"
    awk -v n="$name" -v l="$line" '
      BEGIN { done=0 }
      $0 ~ "^[[:space:]]*export[[:space:]]+" n "=" {
        if (!done) { print l; done=1; next }
      }
      { print }
      END { if (!done) print l }
    ' "$file" > "$tmp"
    mv "$tmp" "$file"
  else
    printf '\n# technical-insight-skills Projects Root\n%s\n' "$line" >> "$file"
  fi
}

if [[ -n "$rc" ]]; then
  upsert_export "PROJECTS_PATHS" "$candidate" "$rc"
  upsert_export "PROJECTS_PATH" "$candidate" "$rc"
  echo "persisted shell exports in: $rc" >&2
fi

echo "persisted config: $CONFIG_FILE" >&2
echo "PROJECTS_ROOT=$candidate"
