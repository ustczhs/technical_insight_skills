#!/usr/bin/env python3
"""Generate tech-tree.drawio from tech-tree.md using layout rules in reference.md.

Layout: shared band width (longest row), evenly distribute nodes within each band,
increased layer gaps, recommended font sizes, curved edges with control points.
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

LEAF_COLORS = {
    "必备": ("#F8CECC", "#B85450", "#000000"),
    "期望": ("#F4B183", "#C65911", "#000000"),
    "魅力": ("#DAE8FC", "#6C8EBF", "#000000"),
}
STATUS_COLORS = {
    "已实现": ("#99FF99", "#33AA33", "#000000"),
    "已实现可优化": ("#E6FFCC", "#99CC66", "#000000"),
    "规划中": ("#FFE6CC", "#D79B00", "#000000"),
    "外购合作": ("#E1D5E7", "#9673A6", "#000000"),
    "未实现": ("#A61C00", "#660000", "#FFFFFF"),
}

LEAF_RE = re.compile(
    r"^-\s+`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*类别:\s*(必备|期望|魅力)"
)
TECH_RE = re.compile(
    r"^-\s+`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*supports:\s*([^|]+?)\s*\|\s*状态:\s*(已实现可优化|已实现|规划中|外购合作|未实现)"
)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def display_label(name: str) -> str:
    """Full tech label for diagram nodes. Never truncate with ellipsis."""
    return name.strip()


def estimate_name_lines(name: str, box_w: int, font_size: int) -> int:
    """Rough CJK wrap line count for whiteSpace=wrap."""
    # ~0.95*fontSize px per CJK char; leave padding
    chars_per_line = max(4, int((box_w - 12) / (font_size * 0.95)))
    return max(1, (len(name) + chars_per_line - 1) // chars_per_line)


def node_height_for(name: str, box_w: int, font_size: int, has_status: bool) -> int:
    lines = estimate_name_lines(name, box_w, font_size)
    if has_status:
        lines += 1  # [状态：…]
    # line box ~ font+6, plus vertical padding
    return max(56 if not has_status else 72, lines * (font_size + 8) + 16)


def parse_md(text: str) -> dict:
    title = "技术树"
    m = re.search(r"^#\s*技术树：\s*(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    slug_m = re.search(r"slug:\s*`([^`]+)`", text)
    slug = slug_m.group(1) if slug_m else "tech-tree"

    sections = {"叶": [], "枝": [], "干": [], "根": []}
    current = None
    for line in text.splitlines():
        if re.match(r"^###\s*叶", line):
            current = "叶"
            continue
        if re.match(r"^###\s*枝", line):
            current = "枝"
            continue
        if re.match(r"^###\s*干", line):
            current = "干"
            continue
        if re.match(r"^###\s*根", line):
            current = "根"
            continue
        if current is None:
            continue
        if current == "叶":
            lm = LEAF_RE.match(line)
            if lm:
                sections["叶"].append(
                    {"id": lm.group(1), "name": lm.group(2).strip(), "cat": lm.group(3)}
                )
        else:
            tm = TECH_RE.match(line)
            if tm:
                supports = [s.strip() for s in tm.group(3).split(",") if s.strip()]
                sections[current].append(
                    {
                        "id": tm.group(1),
                        "name": tm.group(2).strip(),
                        "supports": supports,
                        "status": tm.group(4),
                    }
                )
    return {"title": title, "slug": slug, "sections": sections}


def size_for_count(n_max: int) -> tuple[int, int, int, int, int]:
    """Return leaf_w, tech_w, root_w, leaf_h, tech_h baselines (heights may grow for full labels)."""
    if n_max <= 8:
        return 175, 175, 168, 56, 72
    if n_max <= 11:
        return 156, 150, 142, 56, 72
    if n_max <= 14:
        return 138, 132, 124, 56, 74
    if n_max <= 18:
        return 120, 116, 110, 54, 72
    return 108, 104, 98, 52, 70


def font_for_count(n_max: int) -> tuple[int, int, int, int]:
    # title, band, node, legend — prefer recommended, drop toward floor if dense
    if n_max <= 11:
        return 20, 17, 15, 14
    if n_max <= 16:
        return 20, 17, 14, 14
    return 18, 16, 13, 13


def row_span(n: int, w: int, gap: int) -> int:
    return n * w + max(0, n - 1) * gap


def generate(md_path: Path, out_path: Path | None = None) -> Path:
    data = parse_md(md_path.read_text(encoding="utf-8"))
    leaves = data["sections"]["叶"]
    branches = data["sections"]["枝"]
    trunks = data["sections"]["干"]
    roots = data["sections"]["根"]
    if not leaves:
        raise SystemExit(f"no leaves parsed from {md_path}")

    n_max = max(len(leaves), len(branches), len(trunks), len(roots), 1)
    leaf_w, tech_w, root_w, _leaf_h0, _tech_h0 = size_for_count(n_max)
    title_fs, band_fs, node_fs, legend_fs = font_for_count(n_max)
    min_gap = 8 if n_max >= 14 else 10

    # Per-node heights from full labels (no ellipsis); row height = max in layer
    def layer_heights(items: list[dict], w: int, has_status: bool) -> list[int]:
        return [
            node_height_for(display_label(it["name"]), w, node_fs, has_status)
            for it in items
        ] or [56]

    leaf_heights = layer_heights(leaves, leaf_w, False)
    branch_heights = layer_heights(branches, tech_w, True)
    trunk_heights = layer_heights(trunks, tech_w, True)
    root_heights = layer_heights(roots, root_w, True)
    leaf_h = max(leaf_heights)
    tech_h = max(branch_heights + trunk_heights) if (branches or trunks) else 72
    root_h = max(root_heights) if roots else tech_h
    # Uniform height within each layer for aligned look
    row_h = {
        "leaf": leaf_h,
        "branch": max(branch_heights) if branches else tech_h,
        "trunk": max(trunk_heights) if trunks else tech_h,
        "root": root_h,
    }

    spans = [
        row_span(len(leaves), leaf_w, min_gap),
        row_span(len(branches), tech_w, min_gap) if branches else 0,
        row_span(len(trunks), tech_w, min_gap) if trunks else 0,
        row_span(len(roots), root_w, min_gap) if roots else 0,
    ]
    inner_w = max(spans)
    band_x = 20
    inner_pad = 28
    band_w = inner_w + 2 * inner_pad
    title_zone = 40
    band_pad_bottom = 16
    # Band tall enough for title + tallest node in that layer
    def band_height_for(node_h: int) -> int:
        return max(155, title_zone + node_h + band_pad_bottom)

    band_hs = [
        band_height_for(row_h["leaf"]),
        band_height_for(row_h["branch"]),
        band_height_for(row_h["trunk"]),
        band_height_for(row_h["root"]),
    ]
    layer_gap = 45  # increased spacing between bands
    band_ys = [120]
    for i in range(3):
        band_ys.append(band_ys[-1] + band_hs[i] + layer_gap)
    page_w = band_x + band_w + 20
    page_h = band_ys[3] + band_hs[3] + 50
    node_y_offs = [title_zone + 4] * 4  # nodes below layer title

    id_map: dict[str, str] = {}
    cells: list[str] = []
    cell_id = 2
    pos: dict[str, tuple[float, float, float, float]] = {}

    def add(xml: str) -> None:
        nonlocal cell_id
        cells.append(xml)
        cell_id += 1

    # Title
    add(
        f'<mxCell id="{cell_id}" value="{esc(data["title"])} · 技术树" '
        f'style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontStyle=1;fontSize={title_fs};" '
        f'vertex="1" parent="1"><mxGeometry x="40" y="12" width="640" height="34" as="geometry" /></mxCell>'
    )

    # Legend left
    legend_y = 50
    lx = 40
    add(
        f'<mxCell id="{cell_id}" value="图例：" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize={legend_fs};" '
        f'vertex="1" parent="1"><mxGeometry x="{lx}" y="{legend_y}" width="48" height="26" as="geometry" /></mxCell>'
    )
    lx += 50
    for name, (fc, sc, _) in [
        ("必备", LEAF_COLORS["必备"]),
        ("期望", LEAF_COLORS["期望"]),
        ("魅力", LEAF_COLORS["魅力"]),
    ]:
        add(
            f'<mxCell id="{cell_id}" value="{name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};fontColor=#000000;fontSize={legend_fs};align=center;verticalAlign=middle;" '
            f'vertex="1" parent="1"><mxGeometry x="{lx}" y="{legend_y}" width="56" height="26" as="geometry" /></mxCell>'
        )
        lx += 64
    add(
        f'<mxCell id="{cell_id}" value="标签颜色示意：" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize={legend_fs};" '
        f'vertex="1" parent="1"><mxGeometry x="{lx}" y="{legend_y}" width="118" height="26" as="geometry" /></mxCell>'
    )
    lx += 120
    for name, (fc, sc, fontc) in STATUS_COLORS.items():
        ww = 108 if name == "已实现可优化" else (78 if name == "外购合作" else 68)
        add(
            f'<mxCell id="{cell_id}" value="{name}" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};fontColor={fontc};fontSize={legend_fs};align=center;verticalAlign=middle;" '
            f'vertex="1" parent="1"><mxGeometry x="{lx}" y="{legend_y}" width="{ww}" height="26" as="geometry" /></mxCell>'
        )
        lx += ww + 8

    band_titles = [
        ("叶 · 竞争力特性", "#FFF2CC", "#D6B656"),
        ("枝 · 领域技术", "#E2F0D9", "#548235"),
        ("干 · 主干技术", "#DEEBF7", "#5B9BD5"),
        ("根 · 根技术", "#FCE4D6", "#C65911"),
    ]
    for i, ((title, fc, sc), y) in enumerate(zip(band_titles, band_ys)):
        bh = band_hs[i]
        add(
            f'<mxCell id="{cell_id}" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};opacity=40;" '
            f'vertex="1" parent="1"><mxGeometry x="{band_x}" y="{y}" width="{band_w}" height="{bh}" as="geometry" /></mxCell>'
        )
        add(
            f'<mxCell id="{cell_id}" value="{title}" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontStyle=1;fontSize={band_fs};" '
            f'vertex="1" parent="1"><mxGeometry x="32" y="{y + 8}" width="240" height="30" as="geometry" /></mxCell>'
        )

    def place_row(items: list[dict], y: float, w: int, h: int, kind: str) -> None:
        nonlocal cell_id
        n = len(items)
        if n == 0:
            return
        usable = inner_w
        if n == 1:
            xs = [band_x + inner_pad + (usable - w) / 2]
        else:
            free = usable - n * w
            gap = free / (n - 1)
            xs = [band_x + inner_pad + i * (w + gap) for i in range(n)]
        for i, item in enumerate(items):
            lid = item["id"]
            x = xs[i]
            label = display_label(item["name"])
            if kind == "leaf":
                fc, sc, fontc = LEAF_COLORS[item["cat"]]
                value = esc(label)
            else:
                fc, sc, fontc = STATUS_COLORS[item["status"]]
                value = f"{esc(label)}&#10;[状态：{item['status']}]"
            style = (
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={fc};strokeColor={sc};"
                f"fontColor={fontc};fontSize={node_fs};align=center;verticalAlign=middle;"
            )
            cid = str(cell_id)
            cell_id += 1
            id_map[lid] = cid
            pos[lid] = (x, y, w, h)
            cells.append(
                f'<mxCell id="{cid}" value="{value}" style="{style}" vertex="1" parent="1">'
                f'<mxGeometry x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" as="geometry" /></mxCell>'
            )

    place_row(leaves, band_ys[0] + node_y_offs[0], leaf_w, row_h["leaf"], "leaf")
    place_row(branches, band_ys[1] + node_y_offs[1], tech_w, row_h["branch"], "tech")
    place_row(trunks, band_ys[2] + node_y_offs[2], tech_w, row_h["trunk"], "tech")
    place_row(roots, band_ys[3] + node_y_offs[3], root_w, row_h["root"], "tech")

    edge_pairs: list[tuple[str, str]] = []
    for layer in (branches, trunks, roots):
        for node in layer:
            for tgt in node["supports"]:
                if tgt in id_map and node["id"] in id_map:
                    edge_pairs.append((node["id"], tgt))

    out_edges: dict[str, list[str]] = defaultdict(list)
    in_edges: dict[str, list[str]] = defaultdict(list)
    for s, t in edge_pairs:
        out_edges[s].append(t)
        in_edges[t].append(s)

    def frac(i: int, n: int) -> float:
        if n == 1:
            return 0.5
        return 0.2 + 0.6 * i / (n - 1)

    for src, tgt in edge_pairs:
        sx, sy, sw, sh = pos[src]
        tx, ty, tw, th = pos[tgt]
        oi = out_edges[src].index(tgt)
        ii = in_edges[tgt].index(src)
        exit_x = frac(oi, len(out_edges[src]))
        entry_x = frac(ii, len(in_edges[tgt]))
        x1 = sx + sw * exit_x
        y1 = sy
        x2 = tx + tw * entry_x
        y2 = ty + th
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        bulge = 28 + 12 * ((oi + ii) % 3)
        if (oi + ii) % 2 == 0:
            bulge = -bulge
        if abs(x1 - x2) < 20:
            bulge = 36 if bulge > 0 else -36
        cx = mx + bulge
        cy = my
        cid = str(cell_id)
        cell_id += 1
        style = (
            f"endArrow=block;curved=1;edgeStyle=none;strokeColor=#666666;html=1;"
            f"exitX={exit_x:.3f};exitY=0;entryX={entry_x:.3f};entryY=1;"
        )
        cells.append(
            f'<mxCell id="{cid}" style="{style}" edge="1" parent="1" source="{id_map[src]}" target="{id_map[tgt]}">'
            f'<mxGeometry relative="1" as="geometry"><Array as="points">'
            f'<mxPoint x="{cx:.1f}" y="{cy:.1f}" /></Array></mxGeometry></mxCell>'
        )

    xml = f"""<mxfile host="app.diagrams.net" modified="2026-08-07T03:35:00.000Z" agent="grow_a_tech_tree" version="22.1.0">
  <diagram id="{esc(data['slug'])}" name="技术树">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {chr(10).join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""
    if "orthogonalEdgeStyle" in xml:
        raise RuntimeError("orthogonal edges generated")
    out = out_path or (md_path.parent / "tech-tree.drawio")
    out.write_text(xml, encoding="utf-8")
    print(
        f"wrote {out} nodes={len(leaves)+len(branches)+len(trunks)+len(roots)} "
        f"edges={len(edge_pairs)} page={page_w}x{page_h} n_max={n_max}"
    )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("md", type=Path, nargs="+", help="tech-tree.md path(s)")
    args = ap.parse_args()
    for md in args.md:
        generate(md)


if __name__ == "__main__":
    main()
