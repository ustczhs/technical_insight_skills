#!/usr/bin/env bash
# 检查 opportunities 批次是否达到下限与关键闸门。
# 用法: check-breadth.sh <opportunities_dir>
set -euo pipefail

DIR="${1:-}"
if [[ -z "$DIR" || ! -d "$DIR" ]]; then
  echo "usage: $0 <opportunities_dir>" >&2
  exit 2
fi

fail=0
warn() { echo "WARN: $*"; }
die() { echo "FAIL: $*"; fail=1; }

need() {
  local f="$DIR/$1"
  [[ -f "$f" ]] || die "missing $1"
}

need LANDSCAPE.md
need SESSION_BRIEF.md
need SEED_CATALOG.md
need PEOPLE_LANDSCAPE.md
need SPARK_BOARD.md
need SHORTLIST.md
need HANDOFF_INDEX.md

count_md_rows() {
  # 数 markdown 表数据行（以 | 开头且非分隔行）
  awk '
    /^\|/ && $0 !~ /^\|[-: ]+\|/ { n++ }
    END { print n+0 }
  ' "$1"
}

if [[ -f "$DIR/SEED_CATALOG.md" ]]; then
  # 粗算：兴趣表行 — 不够精确时只警告
  :
fi

cells=$(grep -cE '^\| C[0-9]' "$DIR/PEOPLE_LANDSCAPE.md" 2>/dev/null || echo 0)
sparks=$(grep -cE '^\| S[0-9]' "$DIR/SPARK_BOARD.md" 2>/dev/null || echo 0)

[[ "${cells:-0}" -ge 40 ]] || die "People Cell $cells < 40 (landscape floor)"
[[ "${sparks:-0}" -ge 50 ]] || die "Sparks $sparks < 50 (landscape floor)"

if grep -q '| 12–24' "$DIR/LANDSCAPE.md" 2>/dev/null; then
  warn "LANDSCAPE still mentions 12–24 cells (obsolete floor)"
fi

# shortlist 概念目录
shopt -s nullglob
packs=("$DIR"/concepts/*/HANDOFF_PACK.md)
cards=("$DIR"/concepts/*/OPPORTUNITY_CARD.md)
[[ ${#packs[@]} -ge 1 ]] || die "no HANDOFF_PACK.md under concepts/"
for c in "${cards[@]}"; do
  grep -q '谁付钱' "$c" || die "four-kill missing in $c"
done

# 仓库相对 opportunities 误写无法在本脚本检测；仅提示
echo "OK checks: cells=$cells sparks=$sparks handoff_packs=${#packs[@]}"
exit "$fail"
