import asyncio, json
from playwright.async_api import async_playwright
POSES = {"happy": dict(pose="trumpet", mouth=0.75, lookX=4, lookY=-4), "smile": dict(pose="rest", mouth=0.55, lookX=0, lookY=0), "trumpet": dict(pose="trumpet", mouth=0.8, lookX=8, lookY=-6), "stomp": dict(pose="trumpet", mouth=1.0, lookX=-4, lookY=-2, walk=1.3, t=0.2439)}
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1920,"height":1080})
        await pg.route("**/gsap.min.js", lambda r: r.fulfill(path="/home/claude/fistik-fil/brand/package/dist/gsap.min.js", content_type="application/javascript", headers={"Access-Control-Allow-Origin":"*"}))
        await pg.goto("file:///home/claude/fistik-fil/index.html")
        await pg.wait_for_function("!!(window.__timelines && window.__timelines.main)")
        out = {}
        for k, o in POSES.items():
            out[k] = await pg.evaluate("""(o) => { const F = window.__fistik; const P = F.POSE[o.pose];
                Object.assign(F.R, {A: P[0], C: P[1], L: P[2], mouth: o.mouth, lookX: o.lookX, lookY: o.lookY, blink: 0, walk: o.walk || 0, sway: 0, tilt: 0, earAmp: 1});
                F.render(o.t || 0.0); return document.querySelector('#char svg').outerHTML; }""", o)
        json.dump(out, open("brand/poses.json","w"))
        await b.close()
asyncio.run(main())
