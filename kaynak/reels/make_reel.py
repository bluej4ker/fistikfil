"""Render a 1080x1920 reel from a Fıstık Fil composition.
usage: python make_reel.py <config.json>
Config keys: comp, start, end, audio (mp3/m4a/mp4), lines (list-of-lists or Video-3/4 dict format), hook, hookSecs,
  bias [[t, dx]...], out, optional: gsap (local path to route CDN GSAP to), track [[t, "elementId" | x_px]...], hide ["#sel", ...],
  smooth (crop follow speed), css (extra CSS for this reel), hookHide ["#sel", ...] (hidden while the hook text is on screen),
  fxPull ["#fxSvg text", ".snd", ...] (sound/colour words: redrawn inside the crop so they are never cut at its edge; fxMinY keeps them under the hook),
  cuts [t, ...] (scene camera cuts: crop smoothing restarts there), subTop (karaoke line top in CSS px; default 770 — move it up when the characters stand low), audioOffset (s)
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
LINES = [L["words"] if isinstance(L, dict) else L for L in json.load(open(cfg["lines"], encoding="utf-8"))]
GSAP = cfg.get("gsap")
CHROME = os.environ.get("CHROME") or "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"   # yerelde: CHROME=<kurulu chrome-headless-shell>
TRACK = cfg.get("track", [[T0, "head"]])                       # which element the vertical crop follows, by time
def track_at(t):
    cur = TRACK[0][1]
    for a, v in TRACK:
        if t >= a: cur = v
    return cur

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
#reelOv .fxw { position:absolute; white-space:nowrap; font-weight:800; line-height:1; -webkit-text-stroke:10px #fff; paint-order:stroke fill; text-shadow:0 6px 0 rgba(0,0,0,.18); }
#reelOv .end { position:absolute; inset:0; background:rgba(20,40,80,.55); display:flex; flex-direction:column; align-items:center; justify-content:center; opacity:0; }
#reelOv .end .t { font-size:64px; line-height:1.05; text-align:center; color:#fff; -webkit-text-stroke:10px #2B2D42; paint-order:stroke fill; }
#reelOv .end .c { margin-top:26px; background:#FF3B5C; color:#fff; font-size:38px; border-radius:40px; padding:10px 34px 2px; border:5px solid #fff; }
#lyric, #bug, #title, #end, #vignette { display:none !important; }
""" + "".join(f"{sel} {{ display:none !important; }}\n" for sel in cfg.get("hide", [])) + cfg.get("css", "")
HOOKHIDE = cfg.get("hookHide", [])
if "subTop" in cfg: OVERLAY_CSS += f"#reelOv .rsub {{ top:{cfg['subTop']}px; }}\n"
FXPULL = cfg.get("fxPull", []); FXMINY = cfg.get("fxMinY", 300)

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
        b = await p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        st = {}

        async def setup():                                     # (re)open the page: a stalled renderer is replaced, not waited on
            if st.get("pg"): await st["pg"].close()
            pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
            if GSAP: await pg.route("**/gsap.min.js", lambda r: r.fulfill(path=GSAP, content_type="application/javascript", headers={"Access-Control-Allow-Origin": "*"}))
            await pg.goto("file://" + cfg["comp"])
            await pg.wait_for_function("!!(window.__timelines && window.__timelines.main)")
            await pg.add_style_tag(content=OVERLAY_CSS)
            await pg.evaluate("""(h) => { const o = document.createElement('div'); o.id = 'reelOv';
                o.innerHTML = `<div class="logo"><span><b style="color:#3D9BFF">Fıstık</b> <b style="color:#FF7A3D">Fil</b></span></div><div class="hook">${h}</div><div class="rsub"></div><div class="fxl"></div>
                  <div class="end"><div class="t">${'Şarkının tamamı<br/>kanalda!'}</div><div class="c">▶ Fıstık Fil</div></div>`;
                document.getElementById('root').appendChild(o); }""", cfg["hook"])
            await pg.wait_for_timeout(800)                       # fonts (document.fonts.ready can hang in headless)
            st["pg"] = pg

        async def safe(fn, tries=4):
            for k in range(tries):
                try: return await asyncio.wait_for(fn(st["pg"]), 20)
                except Exception as e:
                    print("retry", k, type(e).__name__, flush=True); await setup()
            raise RuntimeError("page keeps stalling")

        await setup(); print("ready", flush=True)
        # pass 1: where is the tracked subject?
        xs = []
        for f in range(N):
            t = T0 + f / FPS; tg = track_at(t)
            if isinstance(tg, (int, float)): x = float(tg)
            else: x = await safe(lambda pg: pg.evaluate(f"""() => {{ window.__timelines.main.seek({t:.4f});   // "a+b": centre of the union of a and b (missing/empty ones skipped, then #head)
                let l = 1e9, r = -1e9; for (const id of '{tg}'.split('+')) {{ const e = document.getElementById(id); if (!e) continue;
                  const b = e.getBoundingClientRect(); if (b.width < 2) continue; l = Math.min(l, b.left); r = Math.max(r, b.right); }}
                if (r < l) {{ const b = document.getElementById('head').getBoundingClientRect(); l = b.left; r = b.right; }}
                return (l + r) / 2; }}"""))
            xs.append(x)
            if f % 150 == 0: print("track", f, "/", N, flush=True)
        bias = cfg.get("bias", [])                            # [[t, dx], ...] extra pan toward the action
        def bias_at(t):
            if not bias: return 0
            if t <= bias[0][0]: return bias[0][1]
            for (a, va), (b2, vb) in zip(bias, bias[1:]):
                if t <= b2: k = (t - a) / (b2 - a); k = k * k * (3 - 2 * k); return va + (vb - va) * k
            return bias[-1][1]
        sm = xs[:]; a = cfg.get("smooth", 0.06)                   # smoothing both ways so the crop glides (higher = follows faster subjects)
        cut = set(int(round((c - T0) * FPS)) for c in cfg.get("cuts", []))   # camera cuts in the scene: the crop cuts too, never glides across
        for i in range(1, N):
            if i not in cut: sm[i] = sm[i - 1] + a * (sm[i] - sm[i - 1])
        for i in range(N - 2, -1, -1):
            if i + 1 not in cut: sm[i] = sm[i + 1] + a * (sm[i] - sm[i + 1])
        centers = [min(1920 - CW / 2, max(CW / 2, sm[i] + bias_at(T0 + i / FPS))) for i in range(N)]
        # pass 2: render (frames already on disk are kept, so a restart resumes)
        for f in range(N):
            path = f"{FR}/f{f:05d}.png"
            if os.path.exists(path): continue
            t = T0 + f / FPS; L = line_at(t); left = centers[f] - CW / 2
            html = " ".join((f"<b>{w}</b>" if wt <= t + 0.02 else f"<i>{w}</i>") for w, wt in L) if L else ""
            endo = max(0.0, min(1.0, (t - (T1 - 2.2)) / 0.35))
            hooko = 1.0 if t - T0 < cfg.get("hookSecs", 4.0) else max(0.0, 1 - (t - T0 - cfg.get("hookSecs", 4.0)) / 0.4)
            async def shot(pg):
                await pg.evaluate("""([t, left, html, endo, hooko, hh, fx, minY]) => { window.__timelines.main.seek(t);
                    const o = document.getElementById('reelOv'); o.style.left = left + 'px';
                    o.querySelector(".rsub").innerHTML = html; o.querySelector(".rsub").style.opacity = endo > 0.5 ? 0 : 1;
                    o.querySelector('.end').style.opacity = endo; o.querySelector('.hook').style.opacity = hooko;
                    for (const sel of hh) document.querySelectorAll(sel).forEach((n) => n.style.visibility = hooko > 0.02 ? 'hidden' : '');
                    const fxl = o.querySelector('.fxl'); fxl.innerHTML = ''; const placed = [];
                    for (const sel of fx) document.querySelectorAll(sel).forEach((e) => {     // a word cut by the crop edge is useless: redraw it inside
                      e.style.visibility = ''; const txt = e.textContent.trim(); if (txt.length < 2 || e.closest('#lyric')) return;
                      const r = e.getBoundingClientRect(); if (r.width < 5) return;
                      let op = 1; for (let n = e; n && n.nodeType == 1; n = n.parentElement) { const cs = getComputedStyle(n); op *= parseFloat(cs.opacity); if (cs.display == 'none') op = 0; }
                      e.style.visibility = 'hidden'; if (op < 0.03) return;
                      const cs = getComputedStyle(e); const col = e instanceof SVGElement ? cs.fill : cs.color;
                      const fs = Math.min(r.height * 0.95, 96), d = document.createElement('div'); d.className = 'fxw'; d.textContent = txt;
                      d.style.cssText = `font-size:${fs}px;color:${col};opacity:${op}`; fxl.appendChild(d);
                      const w = Math.min(d.getBoundingClientRect().width, 560); if (w >= 560) d.style.fontSize = (fs * 560 / d.getBoundingClientRect().width) + 'px';
                      const cx = Math.min(Math.max(r.left + r.width / 2 - left, w / 2 + 22), 607.5 - w / 2 - 22);
                      let y = Math.min(Math.max(r.top, minY), 640); const h = d.getBoundingClientRect().height;
                      for (const b of placed) if (Math.abs(b[0] - cx) < (b[1] + w) / 2 && Math.abs(b[2] - y) < h * 0.9) y = b[2] + h * 0.9;   // two words clamped onto each other: stack them
                      placed.push([cx, w, y]); d.style.left = (cx - w / 2) + 'px'; d.style.top = y + 'px'; }); }""", [t, left, html, endo, hooko, HOOKHIDE, FXPULL, FXMINY])
                await pg.screenshot(path=path, clip={"x": left, "y": 0, "width": CW, "height": 1080})
            await safe(shot)
            if f % 150 == 0: print("frame", f, "/", N, flush=True)
        await b.close()

asyncio.run(main())
fade = T1 - T0 - 0.8
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{FR}/f%05d.png",
    "-ss", str(T0 + cfg.get("audioOffset", 0)), "-t", str(T1 - T0), "-i", cfg["audio"],   # audioOffset: e.g. 5.6 when the audio is the final video (opening first)
    "-map", "0:v:0", "-map", "1:a:0",                      # the audio source may be a video (e.g. 4K render): never take its picture
    "-vf", "scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p", "-af", f"afade=t=in:d=0.25,afade=t=out:st={fade:.2f}:d=0.8",
    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", OUT + ".mp4"], check=True)
print("done", OUT + ".mp4")
