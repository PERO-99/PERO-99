#!/usr/bin/env python3
import os, json, urllib.request
from pathlib import Path

token = os.environ["GITHUB_TOKEN"]
query = """query {
  viewer {
    login
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""
req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": query}).encode(),
    headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
             "User-Agent": "PERO-99-profile"}
)
with urllib.request.urlopen(req, timeout=30) as r:
    payload = json.load(r)

cal = payload["data"]["viewer"]["contributionsCollection"]["contributionCalendar"]
days = [d for w in cal["weeks"] for d in w["contributionDays"]][-371:]
Path("data/contributions.json").write_text(json.dumps({
    "username": payload["data"]["viewer"]["login"],
    "total": cal["totalContributions"], "days": days
}, indent=2))

mx = max([d["contributionCount"] for d in days] or [1])
def color(n):
    if n == 0: return "#161b22"
    r = n / mx
    if r < .25: return "#0e4429"
    if r < .50: return "#006d32"
    if r < .75: return "#26a641"
    return "#39d353"

cells = []
for i, d in enumerate(days):
    col, row = divmod(i, 7)
    x, y = 45 + col*15, 34 + row*15
    delay = min(i*.004, 1.8)
    cells.append('<rect x="{}" y="{}" width="11" height="11" rx="2" fill="{}" class="cell" style="animation-delay:{:.3f}s"/>'.format(
        x, y, color(d["contributionCount"]), delay))

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150" viewBox="0 0 860 150">
<style>.cell{opacity:0;animation:reveal .35s steps(1,end) forwards}@keyframes reveal{from{opacity:0}to{opacity:1}}</style>
<rect width="860" height="150" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="16" y="20" fill="#8b949e" font-family="monospace" font-size="11">PERO-99 · contribution activity · """ + str(cal["totalContributions"]) + """ contributions</text>
""" + "".join(cells) + """
<text x="45" y="145" fill="#8b949e" font-family="monospace" font-size="9">less</text>
<text x="785" y="145" fill="#8b949e" font-family="monospace" font-size="9">more</text>
</svg>"""
Path("contrib-heatmap.svg").write_text(svg)
