"""Render a 1080x1920 reel from a Fıstık Fil composition.
usage: python make_reel.py <config.json>
Seeks the composition frame by frame (DPR 2), follows Fıstık with a smoothed vertical crop,
draws hook text + karaoke subtitles + end card inside the crop, then muxes the song segment."""
import asyncio, json, sys, os, subprocess, math
from playwright.async_api import async_playwright

cfg = json.load(open(sys.argv[1]))
FPS = 30
T0, T1 = cfg["start"], cfg["end"]
N = int(round((T1 - T0) * FPS))
CW = 607.5                     # crop width in CSS px (9:16 of 1080)
OUT = cfg["out"]; FR = OUT + "_frames"; os.makedirs(FR, exist_ok=True)
LINES = json.load(open(cfg["lines"]))
GSAP = "/home/claude/fistik-fil/brand/package/dist/gsap.min.js"

OVERLAY_CSS = """
#reelOv { position:absolute; top:0; height:1080px; width:607.5px; z-index:99999; pointer-events:none; font-family:"Baloo 2",sans-serif; font-weight:800; }
#reelOv .hook { position:absolute; left:20px; right:20px; top:96px; text-align:center; font-size:54px; line-height:1.05; color:#fff;
   -webkit-text-stroke:9px #2B2D42; paint-order:stroke fill; text-shadow:0 5px 0 rgba(0,0,0,.25); }
#reelOv .logo { position:absolute; left:0; right:0; top:26px; text-align:center; }
#reelOv .logo span { display:inline-block; background:#fff; border-radius:30px; padding:4px 20px 0; font-size:28px; box-shadow:0 4px 0 rgba(0,0,0,.12); }
#reelOv .rsub { position:absolute; left:18px; right:18px; top:770px; text-align:center; font-size:44px; line-height:1.15; color:#fff;
   -webkit-text-stroke:9px #2B2D42; paint-order:stroke fill; text-shadow:0 5px 0 rgba(0,0,0,.25); }
#reelOv .rsub b { color:#FFD84D; font-weight:800; }
#reelOv .rsub i { font-style:normal; }
#reelOv .end { position:absolute; inset:0; background:rgba(20,40,80,.55); display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; }
#reelOv .end .t { font-size:64px; line-height:1.05; text-align:center; color:#fff; -webkit-text-stroke:10px #2B2D42; paint-order:stroke fill; }
#reelOv .end .c { margin-top:26px; background:#FF3B5C; color:#fff; font-size:38px; border-radius:40px; padding:10px 34px 2px; border:5px solid #fff; }
#lyric, #bug, #title, #end, #vignette { display:none !important; }
"""

def line_at(t):
    cur = None
    for i, L in enumerate(LINES):
        if L[0][1] - 0.35 <= t: cur = i
    if cur is None: return None
    L = LINES[cur]
    nxt = LINES[cur + 1][0][1] - 0.35 if cur + 1 < len(LINES) else 1e9
    if t > min(nxt, L[-1][1] + 2.5): return None
    return L

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await pg.route("**/gsap.min.js", lambda r: r.fulfill(path=GSAP, content_type="application/javascript", headers={"Access-Control-Allow-Origin": "*"}))
        await pg.goto("file://" + cfg["comp"])
        await pg.wait_for_function("!!(window.__timelines && window.__timelines.main)")
        await pg.add_style_tag(content=OVERLAY_CSS)
        await pg.evaluate("""(h) => { const o = document.createElement('div'); o.id = 'reelOv';
            o.innerHTML = `<div class="logo"><span><b style="color:#3D9BFF">Fıstık</b> <b style="color:#FF7A3D">Fil</b></span></div><div class="hook">${h}</div><div class="rsub"></div>
              <div class="end"><div class="t">${'Şarkının tamamı<br/>kanalda!'}</div><div class="c">▶ Fıstık Fil</div></div>`;
            document.getElementById('root').appendChild(o); }""", cfg["hook"])
        await pg.evaluate("document.fonts.ready.then(()=>1)")
        # pass 1: where is Fıstık's head?
        xs = []
        for f in range(N):
            t = T0 + f / FPS
            x = await pg.evaluate(f"""() => {{ window.__timelines.main.seek({t:.4f}); const r = document.getElementById('head').getBoundingClientRect(); return r.left + r.width / 2; }}""")
            xs.append(x)
        bias = cfg.get("bias", [])                            # [[t, dx], ...] extra pan toward the action
        def bias_at(t):
            if not bias: return 0
            if t <= bias[0][0]: return bias[0][1]
            for (a, va), (b2, vb) in zip(bias, bias[1:]):
                if t <= b2: k = (t - a) / (b2 - a); k = k * k * (3 - 2 * k); return va + (vb - va) * k
            return bias[-1][1]
        # heavy smoothing (exponential both ways) so the crop glides
        sm = xs[:]; a = 0.06
        for i in range(1, N): sm[i] = sm[i - 1] + a * (sm[i] - sm[i - 1])
        for i in range(N - 2, -1, -1): sm[i] = sm[i + 1] + a * (sm[i] - sm[i + 1])
        centers = [min(1920 - CW / 2, max(CW / 2, sm[i] + bias_at(T0 + i / FPS))) for i in range(N)]
        # pass 2: render
        for f in range(N):
            t = T0 + f / FPS; L = line_at(t); left = centers[f] - CW / 2
            html = ""
            if L: html = " ".join((f"<b>{w}</b>" if wt <= t + 0.02 else f"<i>{w}</i>") for w, wt in L)
            endo = max(0.0, min(1.0, (t - (T1 - 2.2)) / 0.35))
            hooko = 1.0 if t - T0 < cfg.get("hookSecs", 4.0) else max(0.0, 1 - (t - T0 - cfg.get("hookSecs", 4.0)) / 0.4)
            await pg.evaluate("""([t, left, html, endo, hooko]) => { window.__timelines.main.seek(t);
                const o = document.getElementById('reelOv'); o.style.left = left + 'px';
                o.querySelector(".rsub").innerHTML = html; o.querySelector(".rsub").style.opacity = endo > 0.5 ? 0 : 1;
                o.querySelector('.end').style.opacity = endo; o.querySelector('.hook').style.opacity = hooko; }""", [t, left, html, endo, hooko])
            await pg.screenshot(path=f"{FR}/f{f:05d}.png", clip={"x": left, "y": 0, "width": CW, "height": 1080})
            if f % 150 == 0: print("frame", f, "/", N, flush=True)
        await b.close()

asyncio.run(main())
fade = T1 - T0 - 0.8
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{FR}/f%05d.png",
    "-ss", str(T0), "-t", str(T1 - T0), "-i", cfg["audio"],
    "-vf", "scale=1080:1920:flags=lanczos,format=yuv420p", "-af", f"afade=t=in:d=0.25,afade=t=out:st={fade:.2f}:d=0.8",
    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", OUT + ".mp4"], check=True)
print("done", OUT + ".mp4")
