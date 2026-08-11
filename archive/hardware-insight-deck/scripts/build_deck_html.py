#!/usr/bin/env python3
"""DEPRECATED: use build_deck_ppt.py instead.

Build hardware-insight HTML slide deck from slides-<取向>.md
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TEMPLATE_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{ --bg: #F2F2F2; --primary: #B8D8BE; --accent: #E91E63; --text: #2D2926; --grid: rgba(45,41,38,0.06); }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: "Noto Sans SC","PingFang SC",system-ui,sans-serif; background:#1a1a1a; overflow:hidden; }}
    .slide {{
      display:none; width:100vw; height:100vh; padding:48px 64px; flex-direction:column;
      background:var(--bg);
      background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);
      background-size:24px 24px; color:var(--text);
    }}
    .slide.active {{ display:flex; }}
    .slide h1 {{ font-size:2.2rem; font-weight:800; border-bottom:4px solid var(--primary); padding-bottom:.4rem; margin-bottom:1.2rem; }}
    .slide ul {{ list-style:none; font-size:1.25rem; line-height:1.7; max-width:920px; }}
    .slide li {{ padding:.3rem 0 .3rem 1.2rem; position:relative; }}
    .slide li::before {{ content:"▸"; position:absolute; left:0; color:var(--accent); font-weight:bold; }}
    .slide img {{ max-width:88%; max-height:42vh; margin:.4rem 0 .8rem; border:1px solid #ccc; }}
    .caption {{ font-size:.92rem; color:#555; margin-bottom:.8rem; font-style:italic; max-width:88%; }}
    .footer {{ margin-top:auto; font-size:.82rem; color:#888; }}
    .pager {{ position:fixed; bottom:16px; right:24px; color:#aaa; font-size:.9rem; }}
    @media print {{ .slide {{ display:flex!important; page-break-after:always; min-height:100vh; }} .pager {{ display:none; }} }}
  </style>
</head>
<body><div id="deck">
"""

TEMPLATE_FOOT = """
</div><div class="pager" id="pager"></div>
<script>
(function(){const s=Array.from(document.querySelectorAll('.slide'));let i=0;
function show(n){i=Math.max(0,Math.min(s.length-1,n));s.forEach((e,j)=>e.classList.toggle('active',j===i));
document.getElementById('pager').textContent=(i+1)+' / '+s.length;}
document.addEventListener('keydown',e=>{{
  if(['ArrowRight',' ','PageDown'].includes(e.key)){{e.preventDefault();show(i+1);}}
  if(['ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();show(i-1);}}
  if(e.key==='Home')show(0); if(e.key==='End')show(s.length-1);
}});show(0);})();
</script></body></html>
"""


def parse_slides(text: str) -> list[dict]:
    slides = []
    chunks = re.split(r"\n## slide:\s*", text)
    for chunk in chunks[1:]:
        lines = chunk.strip().splitlines()
        name = lines[0].strip()
        slide: dict = {"name": name, "title": name, "bullets": [], "image": "", "caption": ""}
        i = 1
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("title:"):
                slide["title"] = line.split(":", 1)[1].strip()
            elif line.startswith("image:"):
                slide["image"] = line.split(":", 1)[1].strip()
            elif line.startswith("caption:"):
                slide["caption"] = line.split(":", 1)[1].strip()
            elif line == "bullets:":
                i += 1
                while i < len(lines) and lines[i].startswith("  - "):
                    slide["bullets"].append(lines[i].strip()[2:].strip())
                    i += 1
                continue
            i += 1
        slides.append(slide)
    return slides


def slide_html(s: dict, footer: str) -> str:
    parts = [f'<section class="slide"><h1>{s["title"]}</h1>']
    if s.get("image"):
        parts.append(f'<img src="{s["image"]}" alt="{s["title"]}">')
    if s.get("caption"):
        parts.append(f'<p class="caption">{s["caption"]}</p>')
    if s["bullets"]:
        parts.append("<ul>" + "".join(f"<li>{b}</li>" for b in s["bullets"]) + "</ul>")
    parts.append(f'<div class="footer">{footer}</div></section>')
    return "\n".join(parts)


def footer_text(slides: list[dict], title: str) -> str:
    if slides and slides[0].get("title"):
        return f'{slides[0]["title"]} · hardware-insight'
    return f"{title} · hardware-insight"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--title", default="调研汇报")
    args = ap.parse_args()
    slides = parse_slides(args.input.read_text(encoding="utf-8"))
    footer = footer_text(slides, args.title)
    body = "\n".join(slide_html(s, footer) for s in slides)
    html = TEMPLATE_HEAD.format(title=args.title) + body + TEMPLATE_FOOT
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"Wrote {args.output} ({len(slides)} slides)")


if __name__ == "__main__":
    main()
