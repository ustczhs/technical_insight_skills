#!/usr/bin/env python3
"""Build hardware-insight HTML slide deck (html-ppt runtime) from slides-<取向>.md"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DECK_ASSETS = SCRIPT_DIR.parent / "deck-assets" / "assets"

THEMES = {
    "blueprint": "blueprint.css",
    "engineering-whiteprint": "engineering-whiteprint.css",
}


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    meta: dict = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = parts[2]
    return meta, body


def parse_scalar(line: str) -> str:
    v = line.split(":", 1)[1].strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


def parse_list_block(lines: list[str], start: int) -> tuple[list[str], int]:
    items: list[str] = []
    i = start
    while i < len(lines) and lines[i].startswith("  - "):
        items.append(lines[i][4:].strip())
        i += 1
    return items, i


def parse_table_rows(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    rows: list[list[str]] = []
    i = start
    while i < len(lines) and lines[i].startswith("  - "):
        row = lines[i][4:].strip()
        if row.startswith("[") and row.endswith("]"):
            inner = row[1:-1]
            rows.append([c.strip().strip('"').strip("'") for c in inner.split("|")])
        else:
            rows.append([row])
        i += 1
    return rows, i


def parse_nodes(lines: list[str], start: int) -> tuple[list[dict], int]:
    nodes: list[dict] = []
    i = start
    cur: dict | None = None
    while i < len(lines):
        line = lines[i]
        if line.startswith("## slide:"):
            break
        if line.startswith("  - title:"):
            if cur:
                nodes.append(cur)
            cur = {"title": line.split(":", 1)[1].strip().strip('"'), "body": ""}
        elif line.startswith("    body:") and cur:
            cur["body"] = line.split(":", 1)[1].strip().strip('"')
        elif line.strip() and not line.startswith(" ") and not line.startswith("#"):
            break
        i += 1
    if cur:
        nodes.append(cur)
    return nodes, i


def parse_phases(lines: list[str], start: int) -> tuple[list[dict], int]:
    phases: list[dict] = []
    i = start
    cur: dict | None = None
    while i < len(lines):
        line = lines[i]
        if line.startswith("## slide:"):
            break
        if line.startswith("  - period:"):
            if cur:
                phases.append(cur)
            cur = {"period": line.split(":", 1)[1].strip().strip('"'), "milestone": "", "gate": ""}
        elif line.startswith("    milestone:") and cur:
            cur["milestone"] = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("    gate:") and cur:
            cur["gate"] = line.split(":", 1)[1].strip().strip('"')
        elif line.strip() and not line.startswith(" ") and not line.startswith("#"):
            break
        i += 1
    if cur:
        phases.append(cur)
    return phases, i


def parse_metrics(lines: list[str], start: int) -> tuple[list[dict], int]:
    metrics: list[dict] = []
    i = start
    cur: dict | None = None
    while i < len(lines):
        line = lines[i]
        if line.startswith("## slide:"):
            break
        if line.startswith("  - value:"):
            if cur:
                metrics.append(cur)
            cur = {"value": line.split(":", 1)[1].strip().strip('"'), "label": "", "note": ""}
        elif line.startswith("    label:") and cur:
            cur["label"] = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("    note:") and cur:
            cur["note"] = line.split(":", 1)[1].strip().strip('"')
        elif line.strip() and not line.startswith(" ") and not line.startswith("#"):
            break
        i += 1
    if cur:
        metrics.append(cur)
    return metrics, i


def parse_slide_block(chunk: str) -> dict:
    lines = chunk.splitlines()
    name = lines[0].strip()
    slide: dict = {
        "name": name,
        "layout": "bullets",
        "title": name,
        "bullets": [],
        "meta": [],
        "subtitle": "",
        "recommendation": "",
        "table_headers": [],
        "table_rows": [],
        "left_title": "",
        "right_title": "",
        "left_items": [],
        "right_items": [],
        "right_risks": [],
        "footer_note": "",
        "nodes": [],
        "phases": [],
        "metrics": [],
    }
    i = 1
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        if line.startswith("layout:"):
            slide["layout"] = parse_scalar(raw)
        elif line.startswith("title:"):
            slide["title"] = parse_scalar(raw)
        elif line.startswith("subtitle:"):
            slide["subtitle"] = parse_scalar(raw)
        elif line.startswith("recommendation:"):
            slide["recommendation"] = parse_scalar(raw)
        elif line.startswith("left_title:"):
            slide["left_title"] = parse_scalar(raw)
        elif line.startswith("right_title:"):
            slide["right_title"] = parse_scalar(raw)
        elif line.startswith("footer_note:"):
            slide["footer_note"] = parse_scalar(raw)
        elif line == "bullets:":
            slide["bullets"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "meta:":
            slide["meta"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "left_items:":
            slide["left_items"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "right_items:":
            slide["right_items"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "right_risks:":
            slide["right_risks"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "table_headers:":
            slide["table_headers"], i = parse_list_block(lines, i + 1)
            continue
        elif line == "table_rows:":
            slide["table_rows"], i = parse_table_rows(lines, i + 1)
            continue
        elif line == "nodes:":
            slide["nodes"], i = parse_nodes(lines, i + 1)
            continue
        elif line == "phases:":
            slide["phases"], i = parse_phases(lines, i + 1)
            continue
        elif line == "metrics:":
            slide["metrics"], i = parse_metrics(lines, i + 1)
            continue
        i += 1
    return slide


def parse_slides(text: str) -> tuple[dict, list[dict]]:
    meta, body = parse_frontmatter(text)
    slides = []
    for chunk in re.split(r"\n## slide:\s*", body):
        if chunk.strip():
            slides.append(parse_slide_block(chunk))
    return meta, slides


def footer_html(deck_title: str, idx: int, total: int) -> str:
    return (
        f'<div class="hi-footer">'
        f"<span>{esc(deck_title)} · hardware-insight</span>"
        f"<span>{idx:02d} / {total:02d}</span></div>"
    )


def render_cover(s: dict, deck_title: str, idx: int, total: int) -> str:
    active = " is-active" if idx == 1 else ""
    meta_items = "".join(f"<li>{esc(m)}</li>" for m in (s.get("meta") or s.get("bullets") or []))
    sub = f'<p class="hi-sub">{esc(s["subtitle"])}</p>' if s.get("subtitle") else ""
    return f"""<section class="slide{active}">
  <div class="hi-grid-bg"></div>
  <div class="hi-kicker">hardware-insight · 调研汇报</div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  {sub}
  <ul class="hi-meta">{meta_items}</ul>
  {footer_html(deck_title, idx, total)}
</section>"""


def render_summary(s: dict, deck_title: str, idx: int, total: int) -> str:
    bullets = "".join(f"<li>{esc(b)}</li>" for b in s["bullets"])
    rec = ""
    if s.get("recommendation"):
        rec = f'<div class="hi-recommend"><strong>我方建议</strong>{esc(s["recommendation"])}</div>'
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <ul class="hi-bullets">{bullets}</ul>
  {rec}
  {footer_html(deck_title, idx, total)}
</section>"""


def render_table(s: dict, deck_title: str, idx: int, total: int) -> str:
    headers = s.get("table_headers") or []
    rows = s.get("table_rows") or []
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = []
    for row in rows:
        padded = list(row) + [""] * max(0, len(headers) - len(row))
        trs.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in padded[: len(headers)]) + "</tr>")
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <div class="hi-table-wrap"><table class="hi-table"><thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>
  {footer_html(deck_title, idx, total)}
</section>"""


def render_comparison(s: dict, deck_title: str, idx: int, total: int) -> str:
    left = "".join(f"<li>{esc(x)}</li>" for x in s["left_items"])
    right = "".join(f"<li>{esc(x)}</li>" for x in s["right_items"])
    risks = "".join(f"<li>{esc(x)}</li>" for x in s["right_risks"])
    risk_block = f'<div class="hi-risks"><strong>代价/风险</strong><ul>{risks}</ul></div>' if risks else ""
    note = f'<p class="hi-footer-note">{esc(s["footer_note"])}</p>' if s.get("footer_note") else ""
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <div class="hi-compare">
    <div class="hi-col reject"><h3>{esc(s['left_title'])}</h3><ul>{left}</ul></div>
    <div class="hi-col recommend"><h3>{esc(s['right_title'])}</h3><ul>{right}</ul>{risk_block}</div>
  </div>
  {note}
  {footer_html(deck_title, idx, total)}
</section>"""


def render_flow(s: dict, deck_title: str, idx: int, total: int) -> str:
    parts = []
    for n, node in enumerate(s.get("nodes") or [], 1):
        parts.append(
            f'<div class="hi-flow-node"><div class="num">0{n}</div>'
            f'<h4>{esc(node.get("title", ""))}</h4>'
            f'<p>{esc(node.get("body", ""))}</p></div>'
        )
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <div class="hi-flow">{''.join(parts)}</div>
  {footer_html(deck_title, idx, total)}
</section>"""


def render_timeline(s: dict, deck_title: str, idx: int, total: int) -> str:
    parts = []
    for p in s.get("phases") or []:
        parts.append(
            f'<div class="hi-phase"><div class="period">{esc(p.get("period", ""))}</div>'
            f'<div class="milestone">{esc(p.get("milestone", ""))}</div>'
            f'<div class="gate">Gate: {esc(p.get("gate", ""))}</div></div>'
        )
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <div class="hi-timeline">{''.join(parts)}</div>
  {footer_html(deck_title, idx, total)}
</section>"""


def render_metrics(s: dict, deck_title: str, idx: int, total: int) -> str:
    parts = []
    for m in s.get("metrics") or []:
        parts.append(
            f'<div class="hi-metric"><div class="val">{esc(m.get("value", ""))}</div>'
            f'<div class="lbl">{esc(m.get("label", ""))}</div>'
            f'<div class="note">{esc(m.get("note", ""))}</div></div>'
        )
    bullets = "".join(f"<li>{esc(b)}</li>" for b in s.get("bullets") or [])
    extra = f'<ul class="hi-bullets">{bullets}</ul>' if bullets else ""
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <div class="hi-metrics">{''.join(parts)}</div>
  {extra}
  {footer_html(deck_title, idx, total)}
</section>"""


def render_bullets(s: dict, deck_title: str, idx: int, total: int) -> str:
    bullets = "".join(f"<li>{esc(b)}</li>" for b in s["bullets"])
    return f"""<section class="slide">
  <div class="hi-grid-bg"></div>
  <h1 class="hi-h1">{esc(s['title'])}</h1>
  <ul class="hi-bullets">{bullets}</ul>
  {footer_html(deck_title, idx, total)}
</section>"""


RENDERERS = {
    "cover": render_cover,
    "summary": render_summary,
    "table": render_table,
    "comparison": render_comparison,
    "flow": render_flow,
    "timeline": render_timeline,
    "metrics": render_metrics,
    "bullets": render_bullets,
    "explain": render_bullets,
}


def render_slide(s: dict, deck_title: str, idx: int, total: int) -> str:
    layout = s.get("layout") or "bullets"
    return RENDERERS.get(layout, render_bullets)(s, deck_title, idx, total)


def build_html(slides: list[dict], deck_title: str, theme: str) -> str:
    theme_file = THEMES.get(theme, THEMES["engineering-whiteprint"])
    total = len(slides)
    body = "\n".join(render_slide(s, deck_title, i, total) for i, s in enumerate(slides, 1))
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(deck_title)}</title>
  <link rel="stylesheet" href="assets/fonts.css">
  <link rel="stylesheet" href="assets/base.css">
  <link rel="stylesheet" href="assets/themes/{theme_file}">
  <link rel="stylesheet" href="assets/hi-deck.css">
</head>
<body class="tpl-hi-deck">
<div class="deck" id="deck">
{body}
</div>
<script src="assets/runtime.js"></script>
</body>
</html>"""


def copy_assets(dest_assets: Path) -> None:
    if not DECK_ASSETS.is_dir():
        raise SystemExit(f"deck-assets not found: {DECK_ASSETS}")
    if dest_assets.exists():
        shutil.rmtree(dest_assets)
    shutil.copytree(DECK_ASSETS, dest_assets)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build html-ppt slide deck from slides markdown")
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path, help="Output directory (index.html + assets/)")
    ap.add_argument("--title", default="调研汇报")
    args = ap.parse_args()

    meta, slides = parse_slides(args.input.read_text(encoding="utf-8"))
    if not slides:
        raise SystemExit("No slides parsed")

    theme = meta.get("theme", "engineering-whiteprint")
    if theme not in THEMES:
        theme = "engineering-whiteprint"

    args.output.mkdir(parents=True, exist_ok=True)
    copy_assets(args.output / "assets")
    (args.output / "index.html").write_text(build_html(slides, args.title, theme), encoding="utf-8")
    print(f"Wrote {args.output / 'index.html'} ({len(slides)} slides, theme={theme})")


if __name__ == "__main__":
    main()
