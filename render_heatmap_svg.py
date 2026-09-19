#!/usr/bin/env python3
import json
from pathlib import Path

W, H = 900, 150
CELL, GAP = 11, 3
LEFT, TOP = 55, 32

data = json.loads(Path("data/contributions.json").read_text())
days = data.get("days", [])
mx = max([int(x.get("count", 0)) for x in days] or [1])

def level(n):
    if n <= 0: return "#161b22"
    r = n / mx
    if r < .25: return "#0e4429"
    if r < .50: return "#006d32"
    if r < .75: return "#26a641"
    return "#39d353"

cells = []
for i, item in enumerate(days[-371:]):
    col, row = i // 7, i % 7
    if col >= 53: break
    x, y = LEFT + col * (CELL + GAP), TOP + row * (CELL + GAP)
    cells.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{level(int(item.get("count",0)))}"/>')

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
<rect width="{W}" height="{H}" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="20" y="22" fill="#8b949e" font-family="monospace" font-size="12">PERO-99 · CONTRIBUTIONS</text>
{''.join(cells)}
</svg>"""
Path("contrib-heatmap.svg").write_text(svg)
