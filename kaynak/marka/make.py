import json, asyncio
from playwright.async_api import async_playwright
P = json.load(open("brand/poses.json"))
FONT = """
@font-face { font-family: "Baloo 2"; font-weight: 400 800; src: url("../assets/fonts/Baloo2-wght.ttf"); }
* { margin:0; padding:0; box-sizing:border-box } body { font-family: "Baloo 2"; font-weight:800 }
.abs { position:absolute }
"""
TC = ["#3D9BFF", "#FF5A5F", "#FFC23D", "#3FBF6F", "#A66BFF", "#FF7A3D"]
def title(txt, size, stroke):
    return "".join(f'<span style="color:{TC[i%6]}">{"&nbsp;" if c==" " else c}</span>' for i,c in enumerate(txt))
def rays(cx, cy, n, r, col, op):
    import math
    out=[]
    for i in range(n):
        a1=math.radians(i*360/n-360/n/4); a2=math.radians(i*360/n+360/n/4)
        out.append(f'<path d="M{cx} {cy} L{cx+r*math.cos(a1):.0f} {cy+r*math.sin(a1):.0f} L{cx+r*math.cos(a2):.0f} {cy+r*math.sin(a2):.0f}Z" fill="{col}" opacity="{op}"/>')
    return "".join(out)
def balloon(x, y, c, s=1, rot=0):
    return f'''<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 92 q-16 40 0 74 q16 38 0 72" stroke="#7B8496" stroke-width="3" fill="none"/>
    <ellipse cx="0" cy="0" rx="72" ry="86" fill="{c}" stroke="rgba(0,0,0,.18)" stroke-width="5"/><ellipse cx="-28" cy="-36" rx="13" ry="25" fill="#fff" opacity=".5" transform="rotate(-25 -28 -36)"/>
    <path d="M-10 94 L10 94 L0 80Z" fill="{c}"/></g>'''
def cloud(x,y,s): return f'<g transform="translate({x} {y}) scale({s})" fill="#fff"><circle cx="80" cy="80" r="50"/><circle cx="150" cy="58" r="62"/><circle cx="222" cy="82" r="46"/><rect x="60" y="80" width="190" height="50" rx="25"/></g>'
def flower(x,y,c,s=1):
    pet="".join(f'<ellipse cx="0" cy="-14" rx="9" ry="14" fill="{c}" transform="rotate({a})"/>' for a in (0,72,144,216,288))
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 V40" stroke="#3E9B47" stroke-width="5"/>{pet}<circle r="8" fill="#FFD84D"/></g>'

def profile(pose, bg1, bg2):
    sv = P[pose].replace('<svg ', '<svg class="abs" style="left:-12px;top:70px;width:824px;height:879px" ', 1)
    return f'''<html><head><meta charset="utf-8"><style>{FONT} body{{width:800px;height:800px;overflow:hidden}}</style></head><body>
<div class="abs" style="inset:0;background:radial-gradient(circle at 50% 45%, {bg1}, {bg2})"></div>
<svg class="abs" style="inset:0" viewBox="0 0 800 800">{rays(400,330,16,700,"#fff",.18)}</svg>
{sv}</body></html>'''

def banner():
    sv = P["trumpet"].replace('<svg ', '<svg class="abs" style="left:560px;top:430px;width:480px;height:512px" ', 1)
    sky = f'''<svg class="abs" style="inset:0" viewBox="0 0 2560 1440">
      <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7CCBFF"/><stop offset="1" stop-color="#DDF3FF"/></linearGradient></defs>
      <rect width="2560" height="1440" fill="url(#sky)"/>
      {rays(800,690,20,1500,"#fff",.10)}
      {cloud(120,250,1.3)}{cloud(1700,330,0.9)}{cloud(2150,520,1.1)}{cloud(330,1010,0.8)}{cloud(1250,230,0.8)}
      <g transform="translate(2280 300)"><circle r="95" fill="#FFD84D" stroke="#F5B921" stroke-width="6"/>
        <ellipse cx="-24" cy="-10" rx="8" ry="11" fill="#9A5B1E"/><ellipse cx="24" cy="-10" rx="8" ry="11" fill="#9A5B1E"/>
        <path d="M-22 18 Q0 40 22 18" stroke="#9A5B1E" stroke-width="7" fill="none" stroke-linecap="round"/></g>
      <path d="M0 960 Q400 840 800 930 T1600 900 T2560 920 V1440 H0Z" fill="#9BDB7A"/>
      <path d="M0 1050 Q640 980 1280 1040 T2560 1020 V1440 H0Z" fill="#6CC75A"/>
      {flower(200,1100,"#FF8FB1",1.4)}{flower(420,1180,"#fff",1.2)}{flower(1500,1120,"#B58CFF",1.3)}{flower(2050,1150,"#FF8FB1",1.4)}{flower(2350,1100,"#FFD84D",1.3)}{flower(1250,1200,"#FFD84D",1.1)}
      {balloon(330,640,"#FF5A5F",0.9,-8)}{balloon(450,560,"#FFC23D",0.8,5)}{balloon(2200,700,"#3D9BFF",0.9,6)}{balloon(2330,610,"#A66BFF",0.75,-6)}{balloon(2100,600,"#3FBF6F",0.7,-3)}
      <ellipse cx="800" cy="935" rx="150" ry="22" fill="rgba(30,80,30,.25)"/>
    </svg>'''
    return f'''<html><head><meta charset="utf-8"><style>{FONT} body{{width:2560px;height:1440px;overflow:hidden}}
      .t{{left:1080px;top:540px;font-size:200px;line-height:1;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 12px 0 rgba(0,0,0,.13);white-space:nowrap}}
      .s{{left:1095px;top:760px;font-size:62px;line-height:1.25;font-weight:700;color:#fff;background:#FF7A3D;border-radius:50px;padding:12px 46px 4px;white-space:nowrap}}
      .n{{left:1100px;top:872px;font-size:44px;color:#2B5FB0;white-space:nowrap}}
    </style></head><body>{sky}{sv}
    <div class="abs t">{title("Fıstık Fil",200,16)}</div>
    <div class="abs s">Eğlenceli Çocuk Şarkıları</div>
    <div class="abs n">♪ Her hafta yeni şarkı! ♪</div>
    </body></html>'''

async def shot(html, path, w, h):
    open("brand/_tmp.html","w").write(html)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":w,"height":h})
        await pg.goto("file:///home/claude/fistik-fil/brand/_tmp.html"); await pg.evaluate("document.fonts.ready.then(()=>1)"); await pg.wait_for_timeout(800)
        await pg.screenshot(path=path); await b.close()

async def main():
    await shot(profile("happy","#FFE07A","#FF9F1C"), "brand/profil-1.png", 800, 800)
    await shot(profile("smile","#9FE09A","#3FBF6F"), "brand/profil-2.png", 800, 800)
    await shot(banner(), "brand/kapak.png", 2560, 1440)
if __name__ == "__main__": asyncio.run(main())
