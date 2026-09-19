import os, json, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

token = os.environ["GITHUB_TOKEN"]
q = """query { viewer { login contributionsCollection { contributionCalendar {
totalContributions weeks { contributionDays { date contributionCount } }
} } } }"""
req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query":q}).encode(),
    headers={"Authorization":"bearer "+token,"Content-Type":"application/json","User-Agent":"PERO-99-profile"}
)
with urllib.request.urlopen(req, timeout=30) as r:
    data=json.load(r)

cal=data["data"]["viewer"]["contributionsCollection"]["contributionCalendar"]
days=[d for w in cal["weeks"] for d in w["contributionDays"]][-371:]
Path("data/contributions.json").write_text(json.dumps({
    "username":data["data"]["viewer"]["login"],
    "total":cal["totalContributions"], "days":days
},indent=2))

font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",11)
rng=__import__("random").Random(99)
mx=max([d["contributionCount"] for d in days] or [1])
def color(n):
    if n==0:return "#161b22"
    r=n/mx
    if r<.25:return "#0e4429"
    if r<.50:return "#006d32"
    if r<.75:return "#26a641"
    return "#39d353"

frames=[]
for frame in range(20):
    im=Image.new("RGB",(1200,220),"#0d1117")
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((2,2,1197,217),radius=18,outline="#30363d",width=2)
    d.text((25,18),f'PERO-99 · contribution activity · {cal["totalContributions"]} total',font=font,fill="#8b949e")
    revealed=min(371,int((frame+1)/19*371))
    for i,item in enumerate(days):
        col,row=divmod(i,7); x,y=42+col*22,55+row*22
        fill=color(item["contributionCount"]) if i<revealed else "#161b22"
        d.rounded_rectangle((x,y,x+16,y+16),radius=3,fill=fill)
    d.text((42,207),"less",font=font,fill="#8b949e")
    d.text((1090,207),"more",font=font,fill="#8b949e")
    frames.append(im)

frames[0].save("contrib-heatmap.gif",save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True)
