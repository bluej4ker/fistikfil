"""Reel cover 1080x1920: a clean crop of the composition at time t + big title."""
import asyncio, sys, json
from playwright.async_api import async_playwright
comp, t, out, l1, l2, c1, c2, dx = sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], float(sys.argv[8])
GSAP = "/home/claude/fistik-fil/brand/package/dist/gsap.min.js"
CW = 607.5
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await pg.route("**/gsap.min.js", lambda r: r.fulfill(path=GSAP, content_type="application/javascript", headers={"Access-Control-Allow-Origin": "*"}))
        await pg.goto("file://" + comp)
        await pg.wait_for_function("!!(window.__timelines && window.__timelines.main)")
        await pg.add_style_tag(content="""#lyric,#bug,#title,#end,#vignette,.snd{display:none!important}
          #cov{position:absolute;top:0;width:607.5px;height:1080px;z-index:99999;font-family:"Baloo 2";font-weight:800;text-align:center}
          #cov .a,#cov .b2{position:absolute;left:0;right:0;font-size:96px;line-height:.9;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,0,0,.2);white-space:nowrap}
          #cov .lg{position:absolute;left:0;right:0;top:860px}#cov .lg span{display:inline-block;background:#fff;border-radius:34px;padding:6px 26px 0;font-size:40px;box-shadow:0 5px 0 rgba(0,0,0,.15)}
          #cov .new{position:absolute;left:26px;top:150px;background:#FF3B5C;color:#fff;font-size:34px;padding:4px 20px 0;border-radius:16px;border:5px solid #fff;transform:rotate(-7deg)}""")
        x = await pg.evaluate(f"() => {{ window.__timelines.main.seek({t}); const r = document.getElementById('head').getBoundingClientRect(); return r.left + r.width / 2; }}")
        left = min(1920 - CW, max(0, x + dx - CW / 2))
        await pg.evaluate("""([left, l1, l2, c1, c2]) => { const o = document.createElement('div'); o.id = 'cov'; o.style.left = left + 'px';
            o.innerHTML = `<div class="new">YENİ!</div><div class="a" style="top:200px;color:${c1};transform:rotate(-5deg)">${l1}</div><div class="b2" style="top:292px;color:${c2};transform:rotate(3deg)">${l2}</div>
              <div class="lg"><span><b style="color:#3D9BFF">Fıstık</b> <b style="color:#FF7A3D">Fil</b></span></div>`;
            document.getElementById('root').appendChild(o); }""", [left, l1, l2, c1, c2])
        await pg.evaluate("document.fonts.ready.then(()=>1)"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=out, clip={"x": left, "y": 0, "width": CW, "height": 1080})
        await b.close()
asyncio.run(main())
