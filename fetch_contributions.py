#!/usr/bin/env python3
import os, re, json
from pathlib import Path
from urllib.request import Request, urlopen

username = os.environ.get("GH_PROFILE_USER", "PERO-99")
url = f"https://github.com/{username}/contributions"
req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")

days = []
pattern = re.compile(r'<td[^>]*data-date="([^"]+)"[^>]*data-level="(\d+)"[^>]*>.*?</td>', re.S)
for date, level in pattern.findall(html):
    days.append({"date": date, "count": int(level)})

out = Path("data/contributions.json")
if not days:
    print("Could not parse GitHub contribution calendar; keeping existing data.")
    raise SystemExit(0)

out.write_text(json.dumps({"username": username, "days": days}, indent=2))
print(f"Saved {len(days)} contribution days for {username}")
