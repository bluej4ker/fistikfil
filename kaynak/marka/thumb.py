import json, asyncio, math, sys
sys.path.insert(0, "brand")
from make import FONT, rays, balloon, shot
P = json.load(open("brand/poses.json"))
sv = P["stomp"].replace('<svg ', '<svg class="abs" style="left:-10px;top:28px;width:660px;height:704px;transform:rotate(-4deg)" ', 1)
def puff(x,y,s): return f'<g transform="translate({x} {y}) scale({s})" fill="#fff" stroke="#E2C9A6" stroke-width="4"><circle cx="0" cy="0" r="34"/><circle cx="38" cy="8" r="26"/><circle cx="-36" cy="10" r="24"/></g>'
def star(x,y,s,c): 
    pts=" ".join(f"{x+math.cos(math.radians(-90+i*36))*(s if i%2==0 else s*.45):.0f},{y+math.sin(math.radians(-90+i*36))*(s if i%2==0 else s*.45):.0f}" for i in range(10))
    return f'<polygon points="{pts}" fill="{c}" stroke="#fff" stroke-width="6" stroke-linejoin="round"/>'
html = f'''<html><head><meta charset="utf-8"><style>{FONT} body{{width:1280px;height:720px;overflow:hidden}}
 .g{{font-size:190px;line-height:.86;-webkit-text-stroke:18px #fff;paint-order:stroke fill;text-shadow:0 12px 0 rgba(0,0,0,.18);white-space:nowrap;font-weight:800}}
 .yeni{{left:24px;top:22px;background:#FF3B5C;color:#fff;font-size:46px;font-weight:800;padding:2px 26px 0;border-radius:18px;transform:rotate(-6deg);border:6px solid #fff;box-shadow:0 6px 0 rgba(0,0,0,.15)}}
 .brand{{right:26px;bottom:20px;background:#fff;border-radius:40px;padding:4px 28px 0;font-size:44px;font-weight:800;box-shadow:0 6px 0 rgba(0,0,0,.12)}}
</style></head><body>
<div class="abs" style="inset:0;background:radial-gradient(circle at 30% 55%, #FFE680 0%, #FFB627 55%, #FF8A1C 100%)"></div>
<svg class="abs" style="inset:0" viewBox="0 0 1280 720">{rays(330,420,22,1500,"#fff",.20)}
  <path d="M0 640 Q320 600 640 630 T1280 620 V720 H0Z" fill="#6CC75A" stroke="#4FAE48" stroke-width="6"/>
  {balloon(1150,140,"#3D9BFF",.62,8)}{balloon(1060,110,"#FF5A5F",.55,-6)}{star(700,90,34,"#FF3B5C")}{star(1210,330,26,"#3FBF6F")}{star(620,560,22,"#A66BFF")}
  <ellipse cx="320" cy="684" rx="200" ry="24" fill="rgba(0,0,0,.18)"/>
  {puff(150,668,1)}{puff(470,672,.9)}
</svg>
{sv}
<div class="abs g" style="left:610px;top:150px;color:#3D7DE0;transform:rotate(-5deg)">GÜM</div>
<div class="abs g" style="left:700px;top:330px;color:#FF4F5E;transform:rotate(3deg)">GÜM!</div>
<div class="abs yeni">YENİ!</div>
<div class="abs brand"><span style="color:#3D9BFF">Fıstık</span> <span style="color:#FF7A3D">Fil</span></div>
</body></html>'''
from playwright.async_api import async_playwright
async def go():
    open("brand/_thumb.html","w").write(html)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1280,"height":720}, device_scale_factor=3)
        await pg.goto("file:///home/claude/fistik-fil/brand/_thumb.html"); await pg.evaluate("document.fonts.ready.then(()=>1)"); await pg.wait_for_timeout(800)
        await pg.screenshot(path="brand/thumb-4k.png"); await b.close()
asyncio.run(go())
