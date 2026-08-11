#!/usr/bin/env python3
"""Sync tech-tree node fill colors from [状态：…] labels in a .drawio file.

Canonical location (grow-a-tech-tree skill):
  skills/grow-a-tech-tree/scripts/sync_status_colors.py
  (or .cursor/skills/grow-a-tech-tree/scripts/… when symlinked)

Usage:
  python3 skills/grow-a-tech-tree/scripts/sync_status_colors.py \\
    trees/<slug>/tech-tree.drawio
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

STATUS_COLORS = {
    "已实现": ("#99FF99", "#33AA33", "#000000"),
    "已实现可优化": ("#E6FFCC", "#99CC66", "#000000"),
    "规划中": ("#FFE6CC", "#D79B00", "#000000"),
    "外购合作": ("#E1D5E7", "#9673A6", "#000000"),
    "未实现": ("#A61C00", "#660000", "#FFFFFF"),
}

# 叶 = 竞争力特性，无掌控状态；按 value 中 [状态：…] 识别枝/干/根（不依赖 id 前缀）
STATUS_RE = re.compile(r"\[状态：([^\]]+)\]")


def set_style(style: str, key: str, value: str) -> str:
    if re.search(rf"(?:^|;){re.escape(key)}=[^;]*", style):
        return re.sub(rf"(?:(?<=;)|^){re.escape(key)}=[^;]*", f"{key}={value}", style)
    return style + ("" if style.endswith(";") else ";") + f"{key}={value};"


def sync(path: Path) -> tuple[int, list[str]]:
    tree = ET.parse(path)
    root = tree.getroot()
    updated = 0
    unknown: list[str] = []

    for cell in root.iter("mxCell"):
        cid = cell.get("id") or ""
        if cell.get("vertex") != "1":
            continue
        value = cell.get("value") or ""
        # decode common draw.io entities for matching
        plain = value.replace("&#10;", "\n").replace("&lt;", "<").replace("&gt;", ">")
        m = STATUS_RE.search(plain)
        if not m:
            continue
        status = m.group(1).strip()
        if status not in STATUS_COLORS:
            unknown.append(f"{cid}: unknown status '{status}'")
            continue
        fill, stroke, font = STATUS_COLORS[status]
        style = cell.get("style") or ""
        style = set_style(style, "fillColor", fill)
        style = set_style(style, "strokeColor", stroke)
        style = set_style(style, "fontColor", font)
        cell.set("style", style)
        updated += 1

    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=False)
    return updated, unknown


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"file not found: {path}", file=sys.stderr)
        return 1
    updated, unknown = sync(path)
    print(f"synced {updated} nodes in {path}")
    for item in unknown:
        print(f"warn: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
